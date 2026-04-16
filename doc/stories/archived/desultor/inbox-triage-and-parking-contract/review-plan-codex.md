---
kind: story
created: 2026-04-16
updated: 2026-04-16
status: archived
verification: local-evidence
tags: [story, review, plan, docs, inbox, triage, parking, desultor]
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

- Scope is narrow and justified: this pass is about intake normalization and
  parking semantics, not a broader redesign of the doc taxonomy.
- The main risk is over-compressing two distinct rules into one slogan. The
  resulting artifacts must separately cover `inbox` cleanup and
  backlog-as-parking.
- Deletion of the raw inbox note is acceptable only if the new durable docs
  preserve the meaningful content and the raw file is no longer needed as a
  project asset.
