---
kind: story
created: 2026-04-15
updated: 2026-04-15
status: archived
verification: local-evidence
tags: [story, docs, install, bootstrap, prompt, readme, desultor]
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

Make Desultor's human bootstrap entrypoint feel closer to a short install
command by moving the detailed bootstrap contract into a dedicated
top-level `INSTALL.md` and shrinking the prompt shown in `README.md`.

## Plan

1. Add a root `INSTALL.md` that defines the canonical minimal-scaffold import
   contract for a fresh host project.
2. Replace the long bootstrap prompt in `README.md` with a compact
   `according to .../INSTALL.md` form.
3. Make `Then help me build: ...` a separate explicit next prompt.
4. Link the new file from the repo map so a public GitHub reader finds it
   immediately.
