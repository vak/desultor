---
kind: story
created: 2026-04-15
updated: 2026-04-15
status: archived
verification: external-review
tags: [story, review, external, claude-code, docs, readme, bootstrap, desultor]
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

## First pass

Claude Code initially reported one blocking issue:

- the new bootstrap section duplicated the existing `Importing into another
  repository` and `Suggested first pass after import` sections too closely,
  creating drift risk.

## Adjustment made

The README was revised so that:

- the quickstart stays a concise bootstrap entrypoint;
- detailed post-import guidance remains canonical in the existing checklist;
- the root-README boundary stays explicit without repeating the whole lower
  section set.

## Final verdict

Claude Code re-reviewed the updated README and reported:

- no blocking findings;
- non-blocking wording suggestions only.

The remaining suggestions were incorporated locally:

- `Copy in the usual Desultor import set` was changed to `Copy in the Desultor
  scaffold`;
- a bridge sentence was added before `Suggested first pass after import` to
  make the bootstrap flow read continuously.
