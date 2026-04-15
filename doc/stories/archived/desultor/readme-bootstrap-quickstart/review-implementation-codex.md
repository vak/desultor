---
kind: story
created: 2026-04-15
updated: 2026-04-15
status: archived
verification: local-evidence
tags: [story, review, implementation, docs, readme, bootstrap, desultor]
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

No blocking local findings after the README quickstart pass.

## Checks performed

- added a new `Start a brand-new project` section near the top of the root
  `README.md`;
- made bootstrap support for both Codex and Claude Code explicit through a
  harness-neutral bootstrap step;
- made the root-README boundary explicit: the starter README explains
  Desultor and must not become the host project's main README;
- reduced duplication between the new quickstart and the existing `Importing`
  and `Suggested first pass after import` sections;
- added a short bridge line before the post-import checklist so the bootstrap
  flow reads continuously.

## Residual risk

- The quickstart is now clearer for bootstrap, but the exact transport
  mechanics remain open RFC territory rather than stable spec or tooling.
