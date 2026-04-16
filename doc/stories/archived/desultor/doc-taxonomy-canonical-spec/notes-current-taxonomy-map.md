---
kind: story-note
created: 2026-04-16
updated: 2026-04-16
status: archived
verification: local-evidence
tags: [story, notes, docs, taxonomy, inventory, desultor]
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
# Current taxonomy map

## Current semantic sources

- `doc/README.md`
  - top-level map of buckets
  - high-level semantics and baseline workflow
- `doc/desultor/ARCHITECTURE.md`
  - architectural placement of documentation and work-tracking layers
- `doc/spec/desultor/intro.md`
  - starter intent and adaptation boundary after import
- `doc/spec/desultor/starter-doc-namespacing-v0_1.md`
  - starter-vs-host doc namespace boundary
- `doc/spec/desultor/project-lifecycle-v0_1.md`
  - story lifecycle and active-story obligations
- `doc/spec/desultor/inbox-triage-and-parking-v0_1.md`
  - inbox drain semantics and backlog-as-parking
- layer README files under `doc/`
  - per-bucket usage hints and examples

## Observed gap

The repository has pieces of a taxonomy contract, but no single stable spec
whose job is to define:

- the meaning of each top-level `doc/` bucket;
- the relationship between bucket semantics and specialized subcontracts;
- which files are canonical contracts versus friendly indexes or local guides.

## Canonical-spec target

The new spec should centralize:

- bucket semantics for `desultor/`, `inbox/`, `spec/`, `kb/`, `rfc/`,
  `stories/`, and `scratch/`;
- the distinction between stable contract, reusable knowledge, open design,
  work tracking, and temporary exploration;
- pointers to specialized specs for namespacing, lifecycle, and inbox/parking.

The new spec should not absorb:

- full story lifecycle detail already owned by `project-lifecycle-v0_1.md`;
- full namespacing rules already owned by
  `starter-doc-namespacing-v0_1.md`;
- full intake/parking detail already owned by
  `inbox-triage-and-parking-v0_1.md`.
