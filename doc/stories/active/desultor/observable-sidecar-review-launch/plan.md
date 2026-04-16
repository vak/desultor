---
kind: story
created: 2026-04-16
updated: 2026-04-16
status: active
verification: local-evidence
tags: [story, sidecar, claude-code, tmux, observability, review, budget, desultor]
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
# Plan

## Goal

Mitigate the Claude sidecar blind-observability incident by adding a visible
one-shot review launch path and by refusing to promote obviously invalid review
output into final artifact files.

## Why this is its own story

This is not just a small script tweak. It changes:

- the sidecar controller surface;
- the recommended external-review workflow;
- the incident response trail for a budget-sensitive failure mode.

## Non-goals

- invent a fake remaining-budget meter for Claude Code;
- redesign the whole sidecar controller around long-lived sessions;
- make `tmux` mandatory for ordinary unattended one-shot asks;
- settle the broader policy question of when counterpart external review is
  mandatory versus honestly deferrable.

## Plan

1. Add a visible one-shot launcher to `scripts/claude_sidecar.py` that runs the
   raw `claude -p --output-format stream-json` path inside `tmux` while still
   writing normalized runtime state and transcripts.
2. Add an explicit assistant-output contract so review artifacts are written
   only when the output satisfies a minimal markdown-artifact check.
3. Update starter documentation and KB workflow notes so the observable launch
   path becomes the canonical review mode when a human wants live visibility.
4. Record local implementation review and keep counterpart external review
   honestly deferred until budget conditions permit it.
