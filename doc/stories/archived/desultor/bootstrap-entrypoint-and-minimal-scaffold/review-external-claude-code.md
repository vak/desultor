---
kind: story
created: 2026-04-15
updated: 2026-04-15
status: archived
verification: external-review
tags: [story, review, external, claude-code, docs, bootstrap, import, scaffold, desultor]
session_signature:
  harness: claude-code
  model_family: claude
  model_exact: claude-opus-4-6
  reasoning_effort: medium
session_signature_sources:
  harness:
    source: claude_sidecar_observation
    raw_evidence: "observed.harness=claude-code via scripts/claude_sidecar.py ask"
  model_family:
    source: claude_sidecar_observation
    raw_evidence: "observed.model_exact=claude-opus-4-6[1m]"
  model_exact:
    source: claude_sidecar_observation
    raw_evidence: "observed.model_exact=claude-opus-4-6[1m]"
  reasoning_effort:
    source: claude_sidecar_observation
    raw_evidence: "observed.requested_effort=medium"
---
# External Review

## Verdict

Claude Code reported no blocking findings.

It explicitly confirmed that the repository now says, consistently across the
reviewed docs, that a human should:

- start from an empty directory;
- open Codex or Claude Code;
- give a natural import prompt; and
- avoid importing Desultor self-docs, RFCs, KB notes, backlog/history, and
  `runtime/` into a fresh host project by default.

## Minor follow-up

Claude Code noted one non-blocking symmetry issue:

- `runtime/` was already listed among default exclusions in `README.md` and the
  adoption checklist, but had not yet been named explicitly in
  `operation-modes-v0_1.md`.

That follow-up was applied in the same pass.
