---
kind: story
created: 2026-04-16
updated: 2026-04-16
status: active
verification: local-evidence
tags: [story, docs, inbox, triage, parking, backlog, spec, rfc, desultor]
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

Make Desultor's `inbox` drain semantics and parking semantics explicit enough
that raw incoming material does not linger as shadow knowledge and `parked/`
does not compete with `stories/backlog/`.

## Plan

1. Capture the ambiguity as a focused RFC rooted in the triaged inbox item.
2. Write a stable spec for inbox triage, inbox cleanup after normalization, and
   backlog-as-parking semantics.
3. Update the relevant index/README files so the rule is discoverable from the
   layer docs instead of being implied only by scattered prose.
4. Remove the now-triaged inbox source if the new RFC and spec fully preserve
   its durable meaning.
5. Keep the story active until local review is written and external review is
   obtained or explicitly deferred.
