---
kind: kb
created: 2026-04-15
updated: 2026-04-15
status: stable
verification: mixed
tags: [starter, bootstrap, smoke-test, codex, claude-code, workflow]
session_signature:
  harness: codex
  model_family: gpt-5
  model_exact: not_exposed_in_session
  reasoning_effort: not_exposed_in_session
session_signature_sources:
  harness:
    source: direct_context
    raw_evidence: "You are Codex, a coding agent based on GPT-5."
  model_family:
    source: direct_context
    raw_evidence: "You are Codex, a coding agent based on GPT-5."
  model_exact:
    source: not_exposed_in_session
    raw_evidence: not_exposed_in_session
  reasoning_effort:
    source: not_exposed_in_session
    raw_evidence: not_exposed_in_session
---
# Dual-harness bootstrap smoke testing

## Why this note exists

If Desultor claims that a brand-new project may start in Codex or in Claude
Code, that claim should be tested as an actual bootstrap path, not left as a
documentation assumption.

## Recommended smoke shape

Use two disposable hello-world fixtures:

- `codex-first`
- `claude-first`

Each fixture should start from an empty work directory and perform the same
minimal adaptation pass:

1. place the Desultor scaffold into the new directory;
2. rewrite the target `README.md` for the hello-world project;
3. write or rewrite target-project `doc/ARCHITECTURE.md`;
4. write or rewrite target-project `doc/spec/intro.md`;
5. open the first active story;
6. record which harness is primary after bootstrap;
7. request counterpart review rather than silently alternating authorship.

## Acceptance criteria

The smoke is good enough when both fixture paths show that:

- the starter can be adapted without leaving starter text as the fake project
  truth;
- harness ownership after bootstrap is explicit;
- the first story exists instead of relying on chat residue;
- the counterpart harness can review the result through the normal external
  review path.

## Harness-specific interpretation

For `codex-first`, the current Codex session is itself the bootstrap operator.
There is no need to "start Codex from Codex" as a separate control plane.

For `claude-first`, the repo-local path is `python3 scripts/claude_sidecar.py
ask --new-session ...` followed by normal Claude-side authored work in the
target directory.

## Environment caveat

In this Codex harness environment, a sandboxed Claude sidecar probe timed out
on repeated API retries, but the same probe succeeded when rerun outside the
sandbox. Treat that as harness-environment behavior, not as evidence that the
Desultor Claude entrypoint is broken.

That means:

- `claude` being installed is not enough;
- a real `claude_sidecar.py ask` probe is the honest feasibility check;
- when run under a network-restricted Codex sandbox, Claude-side smoke tests may
  require an escalated command path.

## Observed run on 2026-04-15

The recommended smoke was exercised in this repository with two disposable
fixtures:

- `runtime/bootstrap-smoke/codex-first-hello`
- `runtime/bootstrap-smoke/claude-first-hello`

Observed outcome:

- both fixtures replaced the starter-facing `README.md`,
  `doc/ARCHITECTURE.md`, and `doc/spec/intro.md` with target-facing text;
- both fixtures contain a runnable `src/hello.py`;
- both fixtures opened an explicit `doc/stories/active/hello-bootstrap/`
  story;
- both fixtures carry counterpart external review artifacts.

Verification:

- `python3 runtime/bootstrap-smoke/codex-first-hello/src/hello.py`
- `python3 runtime/bootstrap-smoke/claude-first-hello/src/hello.py`

Both commands printed the expected hello-world message.

## Defect found during the smoke

The initial `claude-first` authored pass did not write files even though the
sidecar session itself started successfully.

Cause:

- `scripts/claude_sidecar.py ask` hardcoded Claude's default permission mode
  and did not expose a way to request a write-capable mode for non-interactive
  runs.

Resolution:

- add `--permission-mode` to `claude_sidecar.py ask`;
- pass it through to the underlying `claude` CLI;
- record the requested permission mode in normalized observed metadata.

After that change, `claude-first` bootstrap succeeded with
`--permission-mode acceptEdits`.
