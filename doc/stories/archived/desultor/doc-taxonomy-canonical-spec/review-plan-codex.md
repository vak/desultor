---
kind: story
created: 2026-04-16
updated: 2026-04-16
status: archived
verification: local-evidence
tags: [story, review, plan, docs, taxonomy, semantics, spec, desultor]
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
# Plan Review

- Scope is appropriate for a full story: the task affects the canonical reading
  path for Desultor's documentation model, not just one layer README.
- The plan avoids the main failure mode of over-compression by keeping
  specialized policies in dedicated specs and using the new document as the
  canonical map of semantics, not as a replacement for every sub-contract.
- The primary review criteria should be:
  - no semantic contradictions between `doc/README.md`, layer README files, and
    `doc/spec/desultor/*`;
  - no accidental starter/host boundary drift;
  - no duplication that forces future edits to be synchronized across too many
    files.
- A new RFC is not required unless the inventory finds unresolved semantic
  conflict rather than mere scattering.
