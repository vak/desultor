---
kind: story
created: 2026-04-15
updated: 2026-04-15
status: archived
verification: external-review
tags: [story, review, external, claude-code, docs, install, bootstrap, prompt, readme, desultor]
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

Claude Code reviewed the initial `INSTALL.md` introduction and reported:

- no blocking findings;
- non-blocking duplication between `README.md` and `INSTALL.md`;
- a wording concern around the second prompt and session continuity.

## Adjustment made

The bootstrap entrypoint was tightened again so that:

- the root `README.md` quickstart became nearly telegraphic;
- `README.md` now points to `INSTALL.md` as the canonical contract;
- the second prompt is explicitly stated as happening in the same session.

## Final pass

Claude Code re-reviewed the micro-pass and reported:

- no blocking findings;
- non-blocking suggestions only, mainly that the root `README.md` still keeps
  some heavier operational sections outside the quickstart.

## Post-review local nits

After the final external review, two cosmetic local edits were made:

- `INSTALL.md` changed `adapted` to `project-specific` in the scaffold
  verification sentence;
- `README.md` gained a decorative Desultores image at the top.

One further local copy-only polish was applied before push:

- the opening README description was shortened, and the longer stopgap/scope
  explanation moved into a lower `Operating scope` section.

These do not change the bootstrap contract that Claude Code reviewed.
