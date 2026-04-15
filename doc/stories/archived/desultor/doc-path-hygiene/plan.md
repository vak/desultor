---
kind: story
created: 2026-04-15
updated: 2026-04-15
status: archived
verification: local-evidence
tags: [story, hygiene, docs, namespacing, desultor]
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

Make Desultor easier to separate from a host project by moving starter-owned
documentation under explicit `desultor` namespaces and updating the import
contract accordingly.

## Plan

1. Move starter-owned docs into `doc/desultor/` and `doc/*/desultor/`.
2. Update root indexes and harness instructions to point at namespaced paths.
3. Change the import semantics so host-project docs are authored separately
   instead of rewriting starter-owned docs in place.
4. Preserve the current Codex/Claude dual-harness workflow while changing only
   documentation layout and references.
5. Record the hygiene outcome and any remaining risks.
