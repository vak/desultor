---
kind: story
created: 2026-04-16
updated: 2026-04-16
status: active
verification: local-evidence
tags: [story, review, implementation, docs, inbox, triage, parking, desultor]
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
# Implementation Review

## Findings

No blocking local findings after the inbox-triage and parking-contract pass.

## Checks performed

- added a focused RFC for the ambiguity exposed by the triaged inbox item;
- added a stable spec for inbox cleanup after normalization and
  backlog-as-parking semantics;
- tightened `doc/inbox/README.md` and `doc/stories/backlog/README.md` so the
  rule is visible at the layer entrypoints;
- updated the higher-level doc indexes so the new spec is discoverable;
- removed the raw inbox source after its durable meaning was carried into RFC
  and spec artifacts.

## Residual risk

- external counterpart review is still pending, so the story should remain
  active until that review either lands or is explicitly deferred.
