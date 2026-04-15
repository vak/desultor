---
kind: story
created: 2026-04-15
updated: 2026-04-15
status: archived
verification: local-evidence
tags: [story, review, docs, readme, bootstrap, desultor]
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

- Scope is intentionally narrow: public-facing bootstrap guidance in the root
  `README.md`, not a full transport or import-mechanics spec.
- The main risk is mixing up the starter's own public README with the host
  project's README contract; the quickstart should reinforce that boundary.
- The quickstart should help a new reader scan the repo fast without repeating
  entire spec documents inline.
