#!/usr/bin/env python3
"""Minimal repo-local controller for a persistent Claude Code sidecar."""

from __future__ import annotations

import argparse
import json
import os
import shlex
import subprocess
import sys
import threading
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RUNTIME_DIR = ROOT / "runtime" / "claude-sidecar"
RAW_DIR = RUNTIME_DIR / "raw"
ARCHIVE_DIR = RUNTIME_DIR / "archive"
HANDOFF_DIR = RUNTIME_DIR / "handoff"
RUNS_DIR = RUNTIME_DIR / "runs"
STATE_PATH = RUNTIME_DIR / "state.json"
TRANSCRIPT_NDJSON = RUNTIME_DIR / "transcript.ndjson"
TRANSCRIPT_MD = RUNTIME_DIR / "transcript.md"
TMUX_HELPER_ENV = os.environ.get("CLAUDE_SIDECAR_TMUX_HELPER")
TMUX_HELPER = Path(TMUX_HELPER_ENV).expanduser() if TMUX_HELPER_ENV else None
EFFORT_CHOICES = ["low", "medium", "high", "max"]
PERMISSION_MODE_CHOICES = [
    "acceptEdits",
    "auto",
    "bypassPermissions",
    "default",
    "dontAsk",
    "plan",
]
ASSISTANT_OUTPUT_CONTRACT_CHOICES = ["none", "markdown-heading"]


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso_now() -> str:
    return now_utc().replace(microsecond=0).isoformat().replace("+00:00", "Z")


def ts_slug() -> str:
    return now_utc().strftime("%Y%m%dT%H%M%S%fZ")


def ensure_runtime_dirs() -> None:
    for path in [RUNTIME_DIR, RAW_DIR, ARCHIVE_DIR, HANDOFF_DIR, RUNS_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
    )


def append_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(text)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def load_claude_settings() -> dict[str, Any]:
    settings_path = Path.home() / ".claude" / "settings.json"
    if not settings_path.exists():
        return {
            "settings_path": str(settings_path),
            "configured_default_model": None,
            "configured_default_effort": None,
            "always_thinking_enabled": None,
        }
    try:
        payload = json.loads(settings_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {
            "settings_path": str(settings_path),
            "configured_default_model": None,
            "configured_default_effort": None,
            "always_thinking_enabled": None,
        }
    return {
        "settings_path": str(settings_path),
        "configured_default_model": payload.get("model"),
        "configured_default_effort": payload.get("effortLevel"),
        "always_thinking_enabled": payload.get("alwaysThinkingEnabled"),
    }


def default_state() -> dict[str, Any]:
    return {
        "version": 1,
        "project_root": str(ROOT),
        "controller": {
            "script": str(Path(__file__).resolve()),
            "updated_at": iso_now(),
        },
        "conversation": None,
        "last_observed": {},
        "tmux": {},
        "last_reset": None,
        "last_handoff": None,
    }


def load_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        return default_state()
    try:
        data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"State file is malformed: {STATE_PATH}: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit(f"State file is malformed: {STATE_PATH}: expected object")
    merged = default_state()
    merged.update(data)
    return merged


def save_state(state: dict[str, Any]) -> None:
    payload = deepcopy(state)
    payload["controller"] = {
        "script": str(Path(__file__).resolve()),
        "updated_at": iso_now(),
    }
    write_json(STATE_PATH, payload)


def truncate(text: str, limit: int = 240) -> str:
    compact = " ".join(text.strip().split())
    if len(compact) <= limit:
        return compact
    return compact[: limit - 1] + "…"


def shell_join(parts: list[str]) -> str:
    return " ".join(shlex.quote(part) for part in parts)


def wrap_command_keep_open(command: list[str]) -> list[str]:
    shell = os.environ.get("SHELL") or "/bin/sh"
    script = (
        f"{shell_join(command)}\n"
        "rc=$?\n"
        "printf '\\n[claude-sidecar] command exited with status %s\\n' \"$rc\"\n"
        "printf '[claude-sidecar] Window kept open for inspection. Type exit to close it.\\n'\n"
        f"exec {shlex.quote(shell)} -i\n"
    )
    return [shell, "-lc", script]


def read_prompt(args: argparse.Namespace) -> str:
    if args.prompt_file:
        return Path(args.prompt_file).read_text(encoding="utf-8")
    if args.prompt is not None:
        return args.prompt
    if not sys.stdin.isatty():
        return sys.stdin.read()
    raise SystemExit("Prompt required: pass text, --prompt-file, or stdin.")


def parse_stream(stdout: str) -> tuple[list[dict[str, Any]], list[str]]:
    events: list[dict[str, Any]] = []
    raw_non_json: list[str] = []
    for line in stdout.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        try:
            event = json.loads(stripped)
        except json.JSONDecodeError:
            raw_non_json.append(line)
            continue
        if isinstance(event, dict):
            events.append(event)
        else:
            raw_non_json.append(line)
    return events, raw_non_json


def extract_assistant_text(events: list[dict[str, Any]]) -> str:
    parts: list[str] = []
    for event in events:
        if event.get("type") != "assistant":
            continue
        message = event.get("message") or {}
        content = message.get("content") or []
        if not isinstance(content, list):
            continue
        text = "".join(
            item.get("text", "")
            for item in content
            if isinstance(item, dict) and item.get("type") == "text"
        ).strip()
        if text:
            parts.append(text)
    return "\n\n".join(parts).strip()


def build_claude_command(
    *,
    prompt: str,
    resume_session_id: str | None,
    requested_model: str | None,
    requested_effort: str | None,
    requested_permission_mode: str | None,
    extra_args: list[str] | None = None,
) -> list[str]:
    command = ["claude", "-p", "--verbose", "--output-format", "stream-json"]
    if extra_args:
        command.extend(extra_args)
    if requested_model:
        command.extend(["--model", requested_model])
    if requested_effort:
        command.extend(["--effort", requested_effort])
    if requested_permission_mode:
        command.extend(["--permission-mode", requested_permission_mode])
    if resume_session_id:
        command.extend(["-r", resume_session_id])
    command.append(prompt)
    return command


def validate_assistant_output_contract(
    assistant_text: str, contract: str | None
) -> tuple[bool, str | None]:
    normalized = assistant_text.strip()
    if not contract or contract == "none":
        return True, None
    if not normalized:
        return False, "Assistant output is empty."
    if contract == "markdown-heading":
        if any(line.lstrip().startswith("#") for line in normalized.splitlines()):
            return True, None
        return (
            False,
            "Assistant output does not contain the markdown heading required by the contract.",
        )
    return False, f"Unsupported assistant output contract: {contract}"


def apply_assistant_output_contract(
    result: dict[str, Any], contract: str | None
) -> dict[str, Any]:
    normalized_contract = contract or "none"
    valid, error = validate_assistant_output_contract(
        result.get("assistant_text", ""), normalized_contract
    )
    result["assistant_output_contract"] = normalized_contract
    result["assistant_output_valid"] = valid
    result["assistant_output_validation_error"] = error
    result["claude_ok"] = result.get("ok", False)
    if result["claude_ok"] and not valid:
        result["ok"] = False
    return result


def normalize_result(
    *,
    command: list[str],
    prompt: str,
    resume_session_id: str | None,
    completed: subprocess.CompletedProcess[str] | None,
    timeout_sec: int,
    timed_out: bool,
    requested_model: str | None,
    requested_effort: str | None,
    requested_permission_mode: str | None,
    configured_defaults: dict[str, Any],
) -> dict[str, Any]:
    stdout = completed.stdout if completed else ""
    stderr = completed.stderr if completed else ""
    events, raw_non_json = parse_stream(stdout)
    system_init = next(
        (
            event
            for event in events
            if event.get("type") == "system" and event.get("subtype") == "init"
        ),
        {},
    )
    result_event = next(
        (event for event in reversed(events) if event.get("type") == "result"),
        {},
    )
    rate_limit_event = next(
        (event for event in reversed(events) if event.get("type") == "rate_limit_event"),
        {},
    )
    rate_limit_info = rate_limit_event.get("rate_limit_info") or {}
    assistant_text = extract_assistant_text(events)
    if not assistant_text and result_event.get("result"):
        assistant_text = str(result_event.get("result")).strip()
    ok = bool(
        not timed_out
        and completed
        and completed.returncode == 0
        and result_event
        and not result_event.get("is_error", False)
    )
    return {
        "ok": ok,
        "claude_ok": ok,
        "timed_out": timed_out,
        "timeout_sec": timeout_sec,
        "command": command,
        "command_string": shell_join(command),
        "prompt": prompt,
        "resume_session_id_requested": resume_session_id,
        "session_id": result_event.get("session_id") or system_init.get("session_id"),
        "assistant_text": assistant_text,
        "result_text": result_event.get("result"),
        "exit_code": None if completed is None else completed.returncode,
        "stderr": stderr.strip(),
        "non_json_stdout_lines": raw_non_json,
        "event_count": len(events),
        "events": events,
        "system_init": system_init,
        "result_event": result_event,
        "rate_limit_event": rate_limit_event,
        "observed": {
            "model_exact": system_init.get("model"),
            "requested_model": requested_model,
            "permission_mode": system_init.get("permissionMode"),
            "claude_code_version": system_init.get("claude_code_version"),
            "cwd": system_init.get("cwd"),
            "requested_effort": requested_effort,
            "requested_permission_mode": requested_permission_mode,
            "configured_default_model": configured_defaults.get(
                "configured_default_model"
            ),
            "configured_default_effort": configured_defaults.get(
                "configured_default_effort"
            ),
            "always_thinking_enabled": configured_defaults.get(
                "always_thinking_enabled"
            ),
            "settings_path": configured_defaults.get("settings_path"),
            "rate_limit_info": rate_limit_info,
        },
    }


def run_claude(
    *,
    prompt: str,
    resume_session_id: str | None,
    timeout_sec: int,
    requested_model: str | None,
    requested_effort: str | None,
    requested_permission_mode: str | None,
    extra_args: list[str] | None = None,
) -> dict[str, Any]:
    ensure_runtime_dirs()
    configured_defaults = load_claude_settings()
    command = build_claude_command(
        prompt=prompt,
        resume_session_id=resume_session_id,
        requested_model=requested_model,
        requested_effort=requested_effort,
        requested_permission_mode=requested_permission_mode,
        extra_args=extra_args,
    )
    try:
        completed = subprocess.run(
            command,
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = (
            exc.stdout.decode("utf-8", errors="replace")
            if isinstance(exc.stdout, bytes)
            else (exc.stdout or "")
        )
        stderr = (
            exc.stderr.decode("utf-8", errors="replace")
            if isinstance(exc.stderr, bytes)
            else (exc.stderr or "")
        )
        if stderr:
            stderr = stderr.rstrip() + f"\nTimed out after {timeout_sec}s"
        else:
            stderr = f"Timed out after {timeout_sec}s"
        completed = subprocess.CompletedProcess(command, 124, stdout=stdout, stderr=stderr)
        return normalize_result(
            command=command,
            prompt=prompt,
            resume_session_id=resume_session_id,
            completed=completed,
            timeout_sec=timeout_sec,
            timed_out=True,
            requested_model=requested_model,
            requested_effort=requested_effort,
            requested_permission_mode=requested_permission_mode,
            configured_defaults=configured_defaults,
        )
    return normalize_result(
        command=command,
        prompt=prompt,
        resume_session_id=resume_session_id,
        completed=completed,
        timeout_sec=timeout_sec,
        timed_out=False,
        requested_model=requested_model,
        requested_effort=requested_effort,
        requested_permission_mode=requested_permission_mode,
        configured_defaults=configured_defaults,
    )


def mirror_stream(
    stream: Any,
    *,
    sink_path: Path,
    mirror: Any,
    buffer: list[str],
) -> None:
    if stream is None:
        return
    sink_path.parent.mkdir(parents=True, exist_ok=True)
    with sink_path.open("a", encoding="utf-8") as handle:
        for line in iter(stream.readline, ""):
            if not line:
                break
            buffer.append(line)
            handle.write(line)
            handle.flush()
            mirror.write(line)
            mirror.flush()


def run_claude_visible(
    *,
    prompt: str,
    resume_session_id: str | None,
    timeout_sec: int,
    requested_model: str | None,
    requested_effort: str | None,
    requested_permission_mode: str | None,
    stdout_path: Path,
    stderr_path: Path,
    extra_args: list[str] | None = None,
) -> dict[str, Any]:
    ensure_runtime_dirs()
    configured_defaults = load_claude_settings()
    command = build_claude_command(
        prompt=prompt,
        resume_session_id=resume_session_id,
        requested_model=requested_model,
        requested_effort=requested_effort,
        requested_permission_mode=requested_permission_mode,
        extra_args=extra_args,
    )
    stdout_path.parent.mkdir(parents=True, exist_ok=True)
    stderr_path.parent.mkdir(parents=True, exist_ok=True)

    process = subprocess.Popen(
        command,
        cwd=str(ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )
    stdout_buffer: list[str] = []
    stderr_buffer: list[str] = []
    stdout_thread = threading.Thread(
        target=mirror_stream,
        args=(process.stdout,),
        kwargs={
            "sink_path": stdout_path,
            "mirror": sys.stdout,
            "buffer": stdout_buffer,
        },
        daemon=True,
    )
    stderr_thread = threading.Thread(
        target=mirror_stream,
        args=(process.stderr,),
        kwargs={
            "sink_path": stderr_path,
            "mirror": sys.stderr,
            "buffer": stderr_buffer,
        },
        daemon=True,
    )
    stdout_thread.start()
    stderr_thread.start()

    timed_out = False
    try:
        return_code = process.wait(timeout=timeout_sec)
    except subprocess.TimeoutExpired:
        timed_out = True
        process.kill()
        return_code = process.wait()
    stdout_thread.join()
    stderr_thread.join()
    if timed_out:
        timeout_line = f"Timed out after {timeout_sec}s\n"
        stderr_buffer.append(timeout_line)
        append_text(stderr_path, timeout_line)
        sys.stderr.write(timeout_line)
        sys.stderr.flush()

    completed = subprocess.CompletedProcess(
        command,
        return_code,
        stdout="".join(stdout_buffer),
        stderr="".join(stderr_buffer),
    )
    result = normalize_result(
        command=command,
        prompt=prompt,
        resume_session_id=resume_session_id,
        completed=completed,
        timeout_sec=timeout_sec,
        timed_out=timed_out,
        requested_model=requested_model,
        requested_effort=requested_effort,
        requested_permission_mode=requested_permission_mode,
        configured_defaults=configured_defaults,
    )
    result["visible_stream_paths"] = {
        "stdout": str(stdout_path),
        "stderr": str(stderr_path),
    }
    return result


def append_transcript(result: dict[str, Any], *, label: str | None, mode: str) -> dict[str, str]:
    stamp = ts_slug()
    raw_path = RAW_DIR / f"{stamp}.json"
    write_json(raw_path, result)

    session_id = result.get("session_id") or "unknown-session"
    transcript_entry = {
        "timestamp": iso_now(),
        "label": label,
        "mode": mode,
        "session_id": session_id,
        "ok": result.get("ok"),
        "claude_ok": result.get("claude_ok"),
        "timed_out": result.get("timed_out"),
        "prompt": result.get("prompt"),
        "assistant_text": result.get("assistant_text"),
        "raw_result_path": str(raw_path),
        "observed": result.get("observed"),
        "requested_effort": (result.get("observed") or {}).get("requested_effort"),
        "requested_model": (result.get("observed") or {}).get("requested_model"),
        "configured_default_effort": (result.get("observed") or {}).get(
            "configured_default_effort"
        ),
        "rate_limit_info": (result.get("observed") or {}).get("rate_limit_info"),
        "assistant_output_contract": result.get("assistant_output_contract"),
        "assistant_output_valid": result.get("assistant_output_valid"),
        "assistant_output_validation_error": result.get(
            "assistant_output_validation_error"
        ),
    }
    append_text(TRANSCRIPT_NDJSON, json.dumps(transcript_entry, ensure_ascii=True) + "\n")

    assistant_text = result.get("assistant_text") or ""
    observed = result.get("observed") or {}
    rate_limit_info = observed.get("rate_limit_info") or {}
    rate_limit_line = ""
    if rate_limit_info:
        rate_limit_line = (
            f"- rate_limit: status={rate_limit_info.get('status')} "
            f"type={rate_limit_info.get('rateLimitType')} "
            f"resets_at={rate_limit_info.get('resetsAt')} "
            f"overage_status={rate_limit_info.get('overageStatus')} "
            f"is_using_overage={rate_limit_info.get('isUsingOverage')}\n"
        )
    block = (
        f"\n## {transcript_entry['timestamp']}"
        + (f" [{label}]" if label else "")
        + f"\n- mode: {mode}\n- session_id: {session_id}\n- ok: {result.get('ok')}\n"
        + f"- claude_ok: {result.get('claude_ok')}\n"
        + f"- requested_model: {observed.get('requested_model')}\n"
        + f"- requested_effort: {observed.get('requested_effort')}\n"
        + f"- configured_default_effort: {observed.get('configured_default_effort')}\n"
        + f"- assistant_output_contract: {result.get('assistant_output_contract')}\n"
        + f"- assistant_output_valid: {result.get('assistant_output_valid')}\n"
        + f"- raw_result: {raw_path}\n\n### Prompt\n```text\n{result.get('prompt', '').rstrip()}\n```\n\n"
        + rate_limit_line
        + "### Reply\n``````markdown\n"
        + assistant_text.rstrip()
        + "\n``````\n"
    )
    append_text(TRANSCRIPT_MD, block)
    return {"raw_path": str(raw_path), "transcript_md": str(TRANSCRIPT_MD)}


def update_state_after_ask(
    state: dict[str, Any],
    result: dict[str, Any],
    *,
    label: str | None,
    transcript_paths: dict[str, str],
) -> None:
    previous = state.get("conversation") if isinstance(state.get("conversation"), dict) else None
    previous_session_id = previous.get("session_id") if previous else None
    session_id = result.get("session_id")
    started_at = (
        previous.get("started_at")
        if previous and previous_session_id == session_id
        else iso_now()
    )
    turn_count = (
        previous.get("turn_count", 0)
        if previous and previous_session_id == session_id
        else 0
    )

    if session_id:
        state["conversation"] = {
            "session_id": session_id,
            "started_at": started_at,
            "last_used_at": iso_now(),
            "turn_count": turn_count + 1,
            "last_label": label,
            "last_prompt_summary": truncate(result.get("prompt", "")),
            "last_raw_result_path": transcript_paths["raw_path"],
            "last_requested_effort": (result.get("observed") or {}).get(
                "requested_effort"
            ),
            "last_requested_model": (result.get("observed") or {}).get(
                "requested_model"
            ),
            "configured_default_effort": (result.get("observed") or {}).get(
                "configured_default_effort"
            ),
        }
    observed = result.get("observed") or {}
    state["last_observed"] = {
        "model_exact": observed.get("model_exact"),
        "requested_model": observed.get("requested_model"),
        "permission_mode": observed.get("permission_mode"),
        "claude_code_version": observed.get("claude_code_version"),
        "cwd": observed.get("cwd"),
        "requested_effort": observed.get("requested_effort"),
        "configured_default_model": observed.get("configured_default_model"),
        "configured_default_effort": observed.get("configured_default_effort"),
        "always_thinking_enabled": observed.get("always_thinking_enabled"),
        "settings_path": observed.get("settings_path"),
        "rate_limit_info": observed.get("rate_limit_info"),
        "updated_at": iso_now(),
        "last_result_path": transcript_paths["raw_path"],
        "transcript_md": transcript_paths["transcript_md"],
    }


def update_state_after_failure(
    state: dict[str, Any],
    result: dict[str, Any],
    *,
    prompt_summary: str,
    transcript_paths: dict[str, str],
) -> None:
    observed = result.get("observed") or {}
    state["last_observed"] = {
        "model_exact": observed.get("model_exact"),
        "requested_model": observed.get("requested_model"),
        "permission_mode": observed.get("permission_mode"),
        "claude_code_version": observed.get("claude_code_version"),
        "cwd": observed.get("cwd"),
        "requested_effort": observed.get("requested_effort"),
        "configured_default_model": observed.get("configured_default_model"),
        "configured_default_effort": observed.get("configured_default_effort"),
        "always_thinking_enabled": observed.get("always_thinking_enabled"),
        "settings_path": observed.get("settings_path"),
        "rate_limit_info": observed.get("rate_limit_info"),
        "updated_at": iso_now(),
        "last_failure_path": transcript_paths["raw_path"],
        "last_failure_prompt_summary": prompt_summary,
        "transcript_md": transcript_paths["transcript_md"],
    }


def maybe_write_outputs(
    result: dict[str, Any],
    *,
    stdout_format: str,
    assistant_output: str | None,
    json_output: str | None,
    assistant_text_override: str | None = None,
    emit_stdout: bool = True,
) -> None:
    assistant_text = (
        assistant_text_override
        if assistant_text_override is not None
        else result.get("assistant_text", "")
    )
    if assistant_output:
        if result.get("assistant_output_valid", True):
            write_text(Path(assistant_output), assistant_text)
            result["assistant_output_written"] = True
        else:
            result["assistant_output_written"] = False
        result["assistant_output_path"] = assistant_output
    if json_output:
        result["json_output_path"] = json_output
        write_json(Path(json_output), result)
    if not emit_stdout:
        return
    if stdout_format == "assistant-text":
        sys.stdout.write(assistant_text)
        if assistant_text:
            sys.stdout.write("\n")
    else:
        sys.stdout.write(json.dumps(result, ensure_ascii=True, indent=2) + "\n")


def persist_ask_result(
    result: dict[str, Any],
    *,
    label: str | None,
    mode: str,
    prompt_summary: str,
    stdout_format: str,
    assistant_output: str | None,
    json_output: str | None,
    assistant_text_override: str | None = None,
    emit_stdout: bool = True,
) -> int:
    transcript_paths = append_transcript(result, label=label, mode=mode)
    latest_state = load_state()
    if result.get("claude_ok", result.get("ok")):
        update_state_after_ask(
            latest_state,
            result,
            label=label,
            transcript_paths=transcript_paths,
        )
    else:
        update_state_after_failure(
            latest_state,
            result,
            prompt_summary=prompt_summary,
            transcript_paths=transcript_paths,
        )
    save_state(latest_state)
    maybe_write_outputs(
        result,
        stdout_format=stdout_format,
        assistant_output=assistant_output,
        json_output=json_output,
        assistant_text_override=assistant_text_override,
        emit_stdout=emit_stdout,
    )
    return 0 if result.get("ok") else 1


def command_status(args: argparse.Namespace) -> int:
    ensure_runtime_dirs()
    state = load_state()
    sys.stdout.write(json.dumps(state, ensure_ascii=True, indent=2) + "\n")
    return 0


def archive_state_snapshot(state: dict[str, Any], reason: str) -> str | None:
    conversation = state.get("conversation")
    if not isinstance(conversation, dict) or not conversation.get("session_id"):
        return None
    archive_path = ARCHIVE_DIR / f"{ts_slug()}-{reason}.json"
    write_json(archive_path, state)
    return str(archive_path)


def command_reset(args: argparse.Namespace) -> int:
    ensure_runtime_dirs()
    state = load_state()
    archived_path = archive_state_snapshot(state, "reset")
    preserved_tmux = state.get("tmux") or {}
    new_state = default_state()
    new_state["tmux"] = preserved_tmux
    new_state["last_reset"] = {
        "at": iso_now(),
        "reason": args.reason,
        "archived_state": archived_path,
    }
    save_state(new_state)
    sys.stdout.write(
        json.dumps(
            {
                "ok": True,
                "reason": args.reason,
                "archived_state": archived_path,
                "state_path": str(STATE_PATH),
            },
            ensure_ascii=True,
            indent=2,
        )
        + "\n"
    )
    return 0


def command_ask(args: argparse.Namespace) -> int:
    ensure_runtime_dirs()
    state = load_state()
    prompt = read_prompt(args)
    conversation = state.get("conversation") if isinstance(state.get("conversation"), dict) else None
    resume_session_id = None if args.new_session else (conversation or {}).get("session_id")
    result = run_claude(
        prompt=prompt,
        resume_session_id=resume_session_id,
        timeout_sec=args.timeout_sec,
        requested_model=args.model,
        requested_effort=args.effort,
        requested_permission_mode=args.permission_mode,
        extra_args=[],
    )
    apply_assistant_output_contract(result, args.assistant_output_contract)
    return persist_ask_result(
        result,
        label=args.label,
        mode="new" if not resume_session_id else "resume",
        prompt_summary=truncate(prompt),
        stdout_format=args.stdout_format,
        assistant_output=args.assistant_output,
        json_output=args.json_output,
        emit_stdout=True,
    )


def run_tmux_helper(
    session: str,
    window_name: str,
    cwd: str,
    command: list[str],
    *,
    keep_open: bool = False,
) -> dict[str, Any]:
    effective_command = wrap_command_keep_open(command) if keep_open else command
    if TMUX_HELPER and TMUX_HELPER.exists():
        helper_command = [
            str(TMUX_HELPER),
            session,
            window_name,
            cwd,
            "--",
            shell_join(effective_command),
        ]
        completed = subprocess.run(
            helper_command,
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            check=False,
        )
        target = completed.stdout.strip()
        return {
            "ok": completed.returncode == 0,
            "helper": str(TMUX_HELPER),
            "command": helper_command,
            "target": target,
            "stderr": completed.stderr.strip(),
            "exit_code": completed.returncode,
        }

    tmux_command = [
        "tmux",
        "new-window",
        "-P",
        "-F",
        "#{session_name}:#{window_index}",
        "-t",
        f"{session}:",
        "-n",
        window_name,
        "-c",
        cwd,
        shell_join(effective_command),
    ]
    completed = subprocess.run(
        tmux_command,
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    return {
        "ok": completed.returncode == 0,
        "helper": "tmux new-window",
        "command": tmux_command,
        "target": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
        "exit_code": completed.returncode,
    }


def find_tmux_window(session: str, window_name: str) -> str | None:
    completed = subprocess.run(
        [
            "tmux",
            "list-windows",
            "-t",
            f"{session}:",
            "-F",
            "#{session_name}:#{window_index}:#{window_name}",
        ],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        return None
    for line in completed.stdout.splitlines():
        parts = line.split(":", 2)
        if len(parts) != 3:
            continue
        session_name, window_index, observed_name = parts
        if observed_name == window_name:
            return f"{session_name}:{window_index}"
    return None


def command_tmux_log(args: argparse.Namespace) -> int:
    ensure_runtime_dirs()
    TRANSCRIPT_MD.touch(exist_ok=True)
    existing_target = find_tmux_window(args.session, args.window_name)
    if existing_target:
        response = {
            "ok": True,
            "helper": "tmux reuse",
            "command": ["tmux", "list-windows", "-t", f"{args.session}:"],
            "target": existing_target,
            "stderr": "",
            "exit_code": 0,
            "reused": True,
        }
    else:
        response = run_tmux_helper(
            session=args.session,
            window_name=args.window_name,
            cwd=str(ROOT),
            command=["tail", "-n", str(args.lines), "-F", str(TRANSCRIPT_MD)],
            keep_open=False,
        )
    if response["ok"]:
        latest_state = load_state()
        latest_state["tmux"] = {
            "mode": "transcript-tail",
            "target": response["target"],
            "window_name": args.window_name,
            "updated_at": iso_now(),
        }
        save_state(latest_state)
    sys.stdout.write(json.dumps(response, ensure_ascii=True, indent=2) + "\n")
    return 0 if response["ok"] else 1


def command_tmux_claude(args: argparse.Namespace) -> int:
    ensure_runtime_dirs()
    state = load_state()
    conversation = state.get("conversation") if isinstance(state.get("conversation"), dict) else None
    session_id = (conversation or {}).get("session_id")
    if not session_id:
        raise SystemExit("No stored Claude session_id. Run ask first or use tmux-log.")
    state_tmux = state.get("tmux") if isinstance(state.get("tmux"), dict) else {}
    reuse_target = None
    if (
        state_tmux.get("mode") == "interactive-claude-resume"
        and state_tmux.get("window_name") == args.window_name
        and state_tmux.get("session_id") == session_id
        and state_tmux.get("requested_effort") == args.effort
    ):
        reuse_target = find_tmux_window(args.session, args.window_name)
    if reuse_target:
        response = {
            "ok": True,
            "helper": "tmux reuse",
            "command": ["tmux", "list-windows", "-t", f"{args.session}:"],
            "target": reuse_target,
            "stderr": "",
            "exit_code": 0,
            "reused": True,
        }
    else:
        command = ["claude", "-r", session_id]
        if args.model:
            command.extend(["--model", args.model])
        if args.effort:
            command.extend(["--effort", args.effort])
        response = run_tmux_helper(
            session=args.session,
            window_name=args.window_name,
            cwd=str(ROOT),
            command=command,
            keep_open=False,
        )
    if response["ok"]:
        latest_state = load_state()
        latest_state["tmux"] = {
            "mode": "interactive-claude-resume",
            "target": response["target"],
            "window_name": args.window_name,
            "session_id": session_id,
            "requested_effort": args.effort,
            "requested_model": args.model,
            "updated_at": iso_now(),
        }
        save_state(latest_state)
    sys.stdout.write(json.dumps(response, ensure_ascii=True, indent=2) + "\n")
    return 0 if response["ok"] else 1


def command_tmux_ask(args: argparse.Namespace) -> int:
    ensure_runtime_dirs()
    state = load_state()
    prompt = read_prompt(args)
    conversation = state.get("conversation") if isinstance(state.get("conversation"), dict) else None
    resume_session_id = None if args.new_session else (conversation or {}).get("session_id")
    mode = "new" if not resume_session_id else "resume"

    run_id = ts_slug()
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    prompt_path = run_dir / "prompt.txt"
    status_path = run_dir / "status.json"
    result_path = run_dir / "result.json"
    stream_stdout_path = run_dir / "stream.stdout"
    stream_stderr_path = run_dir / "stream.stderr"
    write_text(prompt_path, prompt)
    write_json(
        status_path,
        {
            "state": "launched",
            "run_id": run_id,
            "mode": mode,
            "label": args.label,
            "resume_session_id_requested": resume_session_id,
            "requested_effort": args.effort,
            "requested_model": args.model,
            "requested_permission_mode": args.permission_mode,
            "assistant_output_contract": args.assistant_output_contract,
            "launched_at": iso_now(),
        },
    )

    command = [
        sys.executable,
        str(Path(__file__).resolve()),
        "run-visible-ask",
        "--run-dir",
        str(run_dir),
        "--prompt-file",
        str(prompt_path),
        "--timeout-sec",
        str(args.timeout_sec),
    ]
    if args.label:
        command.extend(["--label", args.label])
    if args.model:
        command.extend(["--model", args.model])
    if args.effort:
        command.extend(["--effort", args.effort])
    if args.permission_mode:
        command.extend(["--permission-mode", args.permission_mode])
    if resume_session_id:
        command.extend(["--resume-session-id", resume_session_id])
    if args.assistant_output:
        command.extend(["--assistant-output", args.assistant_output])
    if args.assistant_output_contract:
        command.extend(
            ["--assistant-output-contract", args.assistant_output_contract]
        )
    if args.json_output:
        command.extend(["--json-output", args.json_output])

    response = run_tmux_helper(
        session=args.session,
        window_name=args.window_name,
        cwd=str(ROOT),
        command=command,
        keep_open=args.keep_open_on_exit,
    )
    response.update(
        {
            "run_id": run_id,
            "run_dir": str(run_dir),
            "status_path": str(status_path),
            "result_path": str(result_path),
            "stream_stdout_path": str(stream_stdout_path),
            "stream_stderr_path": str(stream_stderr_path),
            "mode": mode,
            "label": args.label,
        }
    )
    if response["ok"]:
        latest_state = load_state()
        latest_state["tmux"] = {
            "mode": "visible-one-shot-ask",
            "target": response["target"],
            "window_name": args.window_name,
            "run_id": run_id,
            "run_dir": str(run_dir),
            "status_path": str(status_path),
            "result_path": str(result_path),
            "stream_stdout_path": str(stream_stdout_path),
            "stream_stderr_path": str(stream_stderr_path),
            "requested_effort": args.effort,
            "requested_model": args.model,
            "requested_permission_mode": args.permission_mode,
            "resume_session_id_requested": resume_session_id,
            "assistant_output_contract": args.assistant_output_contract,
            "keep_open_on_exit": args.keep_open_on_exit,
            "updated_at": iso_now(),
        }
        save_state(latest_state)
    sys.stdout.write(json.dumps(response, ensure_ascii=True, indent=2) + "\n")
    return 0 if response["ok"] else 1


def command_run_visible_ask(args: argparse.Namespace) -> int:
    ensure_runtime_dirs()
    run_dir = Path(args.run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)
    status_path = run_dir / "status.json"
    result_path = run_dir / "result.json"
    stream_stdout_path = run_dir / "stream.stdout"
    stream_stderr_path = run_dir / "stream.stderr"
    prompt = read_prompt(args)
    mode = "new" if not args.resume_session_id else "resume"
    write_json(
        status_path,
        {
            "state": "running",
            "label": args.label,
            "mode": mode,
            "resume_session_id_requested": args.resume_session_id,
            "requested_effort": args.effort,
            "requested_model": args.model,
            "requested_permission_mode": args.permission_mode,
            "assistant_output_contract": args.assistant_output_contract,
            "started_at": iso_now(),
        },
    )

    result = run_claude_visible(
        prompt=prompt,
        resume_session_id=args.resume_session_id,
        timeout_sec=args.timeout_sec,
        requested_model=args.model,
        requested_effort=args.effort,
        requested_permission_mode=args.permission_mode,
        stdout_path=stream_stdout_path,
        stderr_path=stream_stderr_path,
        extra_args=[],
    )
    apply_assistant_output_contract(result, args.assistant_output_contract)
    result["run_dir"] = str(run_dir)
    result["visible_stream_paths"] = {
        "stdout": str(stream_stdout_path),
        "stderr": str(stream_stderr_path),
    }

    exit_code = persist_ask_result(
        result,
        label=args.label,
        mode=mode,
        prompt_summary=truncate(prompt),
        stdout_format="json",
        assistant_output=args.assistant_output,
        json_output=args.json_output,
        emit_stdout=False,
    )
    write_json(result_path, result)
    write_json(
        status_path,
        {
            "state": "completed",
            "ok": result.get("ok"),
            "claude_ok": result.get("claude_ok"),
            "timed_out": result.get("timed_out"),
            "exit_code": result.get("exit_code"),
            "session_id": result.get("session_id"),
            "assistant_output_contract": result.get("assistant_output_contract"),
            "assistant_output_valid": result.get("assistant_output_valid"),
            "assistant_output_validation_error": result.get(
                "assistant_output_validation_error"
            ),
            "assistant_output_written": result.get("assistant_output_written"),
            "assistant_output_path": result.get("assistant_output_path"),
            "json_output_path": result.get("json_output_path"),
            "result_path": str(result_path),
            "completed_at": iso_now(),
        },
    )
    return exit_code


def command_handoff(args: argparse.Namespace) -> int:
    ensure_runtime_dirs()
    state = load_state()
    conversation = state.get("conversation") if isinstance(state.get("conversation"), dict) else None
    session_id = (conversation or {}).get("session_id")
    if not session_id:
        raise SystemExit("No stored Claude session_id for handoff.")

    focus_clause = (
        f"Focus specifically on: {args.focus.strip()}\n\n"
        if args.focus and args.focus.strip()
        else ""
    )
    prompt = (
        "Prepare a concise handoff note for a fresh Claude Code session.\n"
        "Return markdown only, no preamble.\n\n"
        f"{focus_clause}"
        "Do not include current session_id values, tmux targets, or other "
        "ephemeral runtime identifiers in the handoff body.\n"
        "If you mention previous runtime details at all, mark them explicitly "
        "as historical debug context, not active instructions.\n\n"
        "Required sections:\n"
        "1. Current goal\n"
        "2. Established facts\n"
        "3. Files and paths that matter\n"
        "4. Open risks or uncertainties\n"
        "5. Immediate next steps\n"
        "6. Do not regress\n"
    )
    result = run_claude(
        prompt=prompt,
        resume_session_id=session_id,
        timeout_sec=args.timeout_sec,
        requested_model=args.model,
        requested_effort=args.effort,
        requested_permission_mode=None,
        extra_args=[],
    )
    transcript_paths = append_transcript(result, label="handoff", mode="resume")
    if not result.get("ok"):
        latest_state = load_state()
        update_state_after_failure(
            latest_state,
            result,
            prompt_summary=truncate(prompt),
            transcript_paths=transcript_paths,
        )
        save_state(latest_state)
        maybe_write_outputs(
            result,
            stdout_format=args.stdout_format,
            assistant_output=args.assistant_output,
            json_output=args.json_output,
        )
        return 1

    assistant_text = result.get("assistant_text", "")
    heading_markers = ("\n# ", "\n## ", "\n### ")
    heading_positions = [
        assistant_text.find(marker)
        for marker in heading_markers
        if assistant_text.find(marker) != -1
    ]
    if assistant_text.startswith("#"):
        sanitized_handoff = assistant_text
    elif heading_positions:
        sanitized_handoff = assistant_text[min(heading_positions) + 1 :]
    else:
        sanitized_handoff = assistant_text
    handoff_valid = any(line.lstrip().startswith("#") for line in sanitized_handoff.splitlines())

    result["raw_assistant_text"] = assistant_text
    result["sanitized_handoff_text"] = sanitized_handoff
    result["handoff_sanitized"] = sanitized_handoff != assistant_text
    latest_state = load_state()
    update_state_after_ask(
        latest_state,
        result,
        label="handoff",
        transcript_paths=transcript_paths,
    )
    handoff_path = None
    if handoff_valid:
        handoff_path = HANDOFF_DIR / f"{ts_slug()}-handoff.md"
        write_text(handoff_path, sanitized_handoff)
        latest_state["last_handoff"] = {
            "path": str(handoff_path),
            "created_at": iso_now(),
            "sanitized": result["handoff_sanitized"],
            "valid": True,
        }
    else:
        result["ok"] = False
        result["handoff_validation_error"] = (
            "No markdown heading found in sanitized handoff text."
        )
        latest_state["last_handoff"] = {
            "path": None,
            "created_at": iso_now(),
            "sanitized": result["handoff_sanitized"],
            "valid": False,
        }
    save_state(latest_state)
    if handoff_path is not None:
        result["handoff_path"] = str(handoff_path)
    maybe_write_outputs(
        result,
        stdout_format=args.stdout_format,
        assistant_output=args.assistant_output,
        json_output=args.json_output,
        assistant_text_override=sanitized_handoff,
    )
    return 0 if handoff_valid else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Repo-local Claude sidecar controller")
    subparsers = parser.add_subparsers(dest="command", required=True)

    status = subparsers.add_parser("status", help="Show current sidecar state")
    status.set_defaults(func=command_status)

    reset = subparsers.add_parser(
        "reset", help="Archive current state and clear stored session"
    )
    reset.add_argument(
        "--reason", default="manual-reset", help="Why the session is being reset"
    )
    reset.set_defaults(func=command_reset)

    ask = subparsers.add_parser(
        "ask", help="Ask Claude, reusing stored session_id by default"
    )
    ask.add_argument("prompt", nargs="?", help="Prompt text")
    ask.add_argument("--prompt-file", help="Read prompt from a file")
    ask.add_argument(
        "--new-session", action="store_true", help="Ignore stored session_id"
    )
    ask.add_argument("--label", help="Short transcript label")
    ask.add_argument(
        "--model",
        help="Explicit Claude model alias or full model name for this request",
    )
    ask.add_argument(
        "--effort",
        choices=EFFORT_CHOICES,
        help="Explicit Claude effort for this request",
    )
    ask.add_argument(
        "--permission-mode",
        choices=PERMISSION_MODE_CHOICES,
        help="Explicit Claude permission mode for this request",
    )
    ask.add_argument(
        "--timeout-sec", type=int, default=90, help="Timeout for the Claude CLI call"
    )
    ask.add_argument(
        "--stdout-format",
        choices=["json", "assistant-text"],
        default="json",
        help="What to print to stdout",
    )
    ask.add_argument("--assistant-output", help="Write assistant text to a file")
    ask.add_argument(
        "--assistant-output-contract",
        choices=ASSISTANT_OUTPUT_CONTRACT_CHOICES,
        default="none",
        help="Minimal contract required before assistant output is written",
    )
    ask.add_argument("--json-output", help="Write normalized result JSON to a file")
    ask.set_defaults(func=command_ask)

    tmux_log = subparsers.add_parser(
        "tmux-log", help="Open a tmux window tailing the transcript"
    )
    tmux_log.add_argument("--session", default="0", help="tmux session name or index")
    tmux_log.add_argument(
        "--window-name", default="claude-sidecar-log", help="tmux window name"
    )
    tmux_log.add_argument(
        "--lines", type=int, default=80, help="How many transcript lines to show initially"
    )
    tmux_log.set_defaults(func=command_tmux_log)

    tmux_claude = subparsers.add_parser(
        "tmux-claude",
        help="Open an interactive Claude resume window in tmux",
    )
    tmux_claude.add_argument("--session", default="0", help="tmux session name or index")
    tmux_claude.add_argument(
        "--window-name", default="claude-sidecar", help="tmux window name"
    )
    tmux_claude.add_argument(
        "--model",
        help="Explicit Claude model alias or full model name for the interactive resume session",
    )
    tmux_claude.add_argument(
        "--effort",
        choices=EFFORT_CHOICES,
        help="Explicit Claude effort for the interactive resume session",
    )
    tmux_claude.set_defaults(func=command_tmux_claude)

    tmux_ask = subparsers.add_parser(
        "tmux-ask",
        help="Launch a visible one-shot Claude ask in tmux and persist normalized results",
    )
    tmux_ask.add_argument("prompt", nargs="?", help="Prompt text")
    tmux_ask.add_argument("--prompt-file", help="Read prompt from a file")
    tmux_ask.add_argument(
        "--new-session", action="store_true", help="Ignore stored session_id"
    )
    tmux_ask.add_argument("--label", help="Short transcript label")
    tmux_ask.add_argument(
        "--model",
        help="Explicit Claude model alias or full model name for this visible request",
    )
    tmux_ask.add_argument(
        "--effort",
        choices=EFFORT_CHOICES,
        help="Explicit Claude effort for this visible request",
    )
    tmux_ask.add_argument(
        "--permission-mode",
        choices=PERMISSION_MODE_CHOICES,
        help="Explicit Claude permission mode for this visible request",
    )
    tmux_ask.add_argument(
        "--assistant-output",
        help="Write assistant text to a file only if the contract passes",
    )
    tmux_ask.add_argument(
        "--assistant-output-contract",
        choices=ASSISTANT_OUTPUT_CONTRACT_CHOICES,
        default="none",
        help="Minimal contract required before assistant output is written",
    )
    tmux_ask.add_argument(
        "--json-output", help="Write normalized result JSON to a file"
    )
    tmux_ask.add_argument(
        "--timeout-sec", type=int, default=90, help="Timeout for the Claude CLI call"
    )
    tmux_ask.add_argument("--session", default="0", help="tmux session name or index")
    tmux_ask.add_argument(
        "--window-name", default="claude-sidecar-visible", help="tmux window name"
    )
    tmux_ask.add_argument(
        "--keep-open-on-exit",
        action="store_true",
        help="Keep the tmux window open in an interactive shell after the command exits",
    )
    tmux_ask.set_defaults(func=command_tmux_ask)

    handoff = subparsers.add_parser(
        "handoff", help="Ask current Claude session for a restart handoff note"
    )
    handoff.add_argument("--focus", help="Optional focus for the handoff note")
    handoff.add_argument(
        "--model",
        help="Explicit Claude model alias or full model name for generating the handoff",
    )
    handoff.add_argument(
        "--effort",
        choices=EFFORT_CHOICES,
        help="Explicit Claude effort for generating the handoff",
    )
    handoff.add_argument(
        "--timeout-sec", type=int, default=120, help="Timeout for the Claude CLI call"
    )
    handoff.add_argument(
        "--stdout-format",
        choices=["json", "assistant-text"],
        default="json",
        help="What to print to stdout",
    )
    handoff.add_argument("--assistant-output", help="Write assistant text to a file")
    handoff.add_argument("--json-output", help="Write normalized result JSON to a file")
    handoff.set_defaults(func=command_handoff)

    run_visible_ask = subparsers.add_parser(
        "run-visible-ask",
        help="Internal helper used by tmux-ask",
    )
    run_visible_ask.add_argument("prompt", nargs="?", help=argparse.SUPPRESS)
    run_visible_ask.add_argument("--prompt-file", help=argparse.SUPPRESS)
    run_visible_ask.add_argument("--run-dir", required=True, help=argparse.SUPPRESS)
    run_visible_ask.add_argument(
        "--resume-session-id", help=argparse.SUPPRESS
    )
    run_visible_ask.add_argument("--label", help=argparse.SUPPRESS)
    run_visible_ask.add_argument("--model", help=argparse.SUPPRESS)
    run_visible_ask.add_argument(
        "--effort", choices=EFFORT_CHOICES, help=argparse.SUPPRESS
    )
    run_visible_ask.add_argument(
        "--permission-mode",
        choices=PERMISSION_MODE_CHOICES,
        help=argparse.SUPPRESS,
    )
    run_visible_ask.add_argument(
        "--assistant-output", help=argparse.SUPPRESS
    )
    run_visible_ask.add_argument(
        "--assistant-output-contract",
        choices=ASSISTANT_OUTPUT_CONTRACT_CHOICES,
        default="none",
        help=argparse.SUPPRESS,
    )
    run_visible_ask.add_argument("--json-output", help=argparse.SUPPRESS)
    run_visible_ask.add_argument(
        "--timeout-sec", type=int, default=90, help=argparse.SUPPRESS
    )
    run_visible_ask.set_defaults(func=command_run_visible_ask)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
