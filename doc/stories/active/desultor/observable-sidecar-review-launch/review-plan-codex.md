---
kind: story
created: 2026-04-16
updated: 2026-04-16
status: active
verification: local-evidence
tags: [story, review, plan, sidecar, tmux, observability, desultor]
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

- The scope is correct for a standalone story because the failure mode spans
  controller behavior, issue handling, and the documented review workflow.
- The visible launch path should reuse the existing normalization and
  transcript-writing pipeline instead of inventing a parallel state schema.
- Assistant-output validation must stay explicit and opt-in so generic `ask`
  calls are not broken by a review-specific contract.
- The likely outcome is mitigation, not full closure: the starter can expose
  live raw output and reject malformed artifacts, but it still cannot claim a
  trustworthy remaining-budget meter.
