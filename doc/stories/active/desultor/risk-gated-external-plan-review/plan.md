---
kind: story
created: 2026-04-16
updated: 2026-04-16
status: active
verification: local-evidence
tags: [story, lifecycle, review, external-review, planning, risk, desultor]
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

Strengthen the story lifecycle so that serious stories receive counterpart
external review before the implementation pass, not only before closure.

## Why this is its own story

This changes the repository's operating contract, not just one checklist line.
If done carelessly, it can:

- add review bureaucracy to every story instead of gating by risk;
- blur plan-stage review with post-implementation external review;
- create naming confusion between different external-review artifacts;
- contradict the existing cross-harness workflow note.

## Non-goals

- require pre-implementation external review for every story;
- replace local `review-plan-*` with external review;
- change ownership handoff rules;
- redesign the broader story lifecycle beyond this gate.

## Plan

1. Define a serious-story gate in the lifecycle contract using the user's
   intent: complex or high-impact work gets pre-implementation external review.
2. Introduce a distinct artifact name for that pass:
   `review-external-plan-*.md`.
3. Update `doc/spec/desultor/project-lifecycle-v0_1.md` and
   `doc/stories/README.md` so the normative contract and local guide stay in
   sync.
4. Update the cross-harness workflow KB note so the operational procedure
   matches the new lifecycle rule.
5. Write local implementation review and leave the story active until external
   counterpart review lands or is explicitly deferred.
