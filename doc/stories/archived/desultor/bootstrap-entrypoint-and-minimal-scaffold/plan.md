---
kind: story
created: 2026-04-15
updated: 2026-04-15
status: archived
verification: local-evidence
tags: [story, docs, bootstrap, import, scaffold, desultor]
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

Fix Desultor's public bootstrap guidance so that:

- a human can start from an empty directory by opening Codex or Claude Code and
  giving a natural import prompt;
- tabula-rasa bootstrap defaults to a minimal host-project scaffold rather than
  copying Desultor's own self-docs and internal backlog/RFC/KB layers into the
  new project.

## Plan

1. Rewrite the root `README.md` bootstrap section around the human-facing
   harness entrypoint instead of manual file copying.
2. Define the default minimal host-project scaffold and the default
   non-imported Desultor internals.
3. Align `doc/spec/desultor/operation-modes-v0_1.md` and
   `doc/kb/desultor/desultor-adoption-checklist-2026-04-15.md` with the new
   bootstrap semantics.
4. Record the same boundary in the transport RFC so the open mechanics note
   does not drift away from the public guidance.
