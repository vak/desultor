---
kind: kb
created: 2026-04-15
updated: 2026-04-15
status: stable
verification: project-rule
tags: [claude-code, sidecar, tmux, session-id, runtime, effort, rate-limit]
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
# Claude Code sidecar: generic operational note

## Working control plane

The recommended control path is:

1. `claude -p --verbose --output-format stream-json ...`
2. persist the returned `session_id`
3. continue later with `claude -p ... -r <session_id> ...`
4. keep raw envelopes, normalized state, and a readable transcript

This is a stronger foundation than treating pane scraping as the primary
protocol.

## What tmux is good for

`tmux` is best used as an observability companion:

- a visible window for an interactive Claude resume session;
- a visible transcript tail;
- keep-open behavior after an interactive command exits.

The repo-local control plane should still be repository files plus structured
CLI output, not terminal screenshots.

## Effort discipline

Keep these concepts separate:

- `requested_model`
- `configured_default_model`
- `effective_session_model`
- `requested_effort`
- `requested_permission_mode`
- `configured_default_effort`
- `effective_session_effort`

Only claim what is honestly observable. If the runtime does not expose the
effective session model, effort, or permission mode, do not invent it.

## Permission-mode discipline

For non-interactive sidecar runs, do not assume the default Claude permission
mode is sufficient for write-capable tasks.

If the intent is an authored pass rather than a read-only probe, the control
plane should be able to pass an explicit `--permission-mode` through to the
Claude CLI.

## Rate-limit discipline

Record any direct rate-limit metadata the runtime exposes.

Do not invent a remaining-percent number from partial metadata.

## Minimal workflow

1. Start or resume a single Claude session via stored `session_id`.
2. Pass explicit model, effort, or permission mode only when the task actually
   needs it.
3. Persist envelopes and normalized state after every call.
4. Use `tmux` only as a companion view, not as the source of continuity.
5. If context quality degrades, generate a handoff note and start a fresh
   session instead of pretending the old one is still coherent.
