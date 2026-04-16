---
kind: story
created: 2026-04-16
updated: 2026-04-16
status: active
verification: local-evidence
tags: [story, review, plan, lifecycle, external-review, risk, desultor]
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

- The scope is correct for a standalone story because this modifies the
  repository's normative lifecycle rather than a single project note.
- The key design constraint is risk-gating: serious stories should gain an
  additional external plan review, but ordinary stories should not inherit a
  blanket requirement.
- The artifact split must stay explicit:
  - `review-plan-*.md` for local plan review
  - `review-external-plan-*.md` for counterpart pre-implementation review
  - `review-external-*.md` for post-implementation external review
- A separate RFC is not required unless the repository surfaces conflicting
  definitions of "serious story" during implementation.
