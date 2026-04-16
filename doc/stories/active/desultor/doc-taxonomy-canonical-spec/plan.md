---
kind: story
created: 2026-04-16
updated: 2026-04-16
status: active
verification: local-evidence
tags: [story, docs, taxonomy, semantics, spec, doc, desultor]
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

Create one canonical Desultor spec for the structure and semantics of `doc/`
without flattening the existing specialized contracts for namespacing, inbox
triage, lifecycle, or public neutrality.

## Why this needs a full story

The current meaning exists, but it is distributed across:

- `doc/README.md`;
- layer README files under `doc/`;
- multiple starter specs under `doc/spec/desultor/`;
- architecture prose under `doc/desultor/ARCHITECTURE.md`.

A careless consolidation pass could create duplicated rules, contradict the
starter/host boundary, or silently shift semantics while "summarizing."

## Non-goals

- redesign the doc taxonomy itself;
- merge all specialized specs into one giant file;
- change the story lifecycle contract;
- change namespacing policy for starter-owned docs.

## Plan

1. Inventory the current semantics and identify which rules are canonical,
   which are layer-local, and which already belong to specialized specs.
2. Write a canonical taxonomy spec under `doc/spec/desultor/` that defines the
   `doc/` layer model and delegates specialized subcontracts by reference.
3. Tighten `doc/README.md` so it acts as the navigational map, while the new
   spec becomes the stable semantic contract.
4. Update `doc/spec/README.md`, the root `README.md`, and any directly affected
   layer README files so discovery points to the canonical spec cleanly.
5. Run a local review for duplication, contradictions, and missed references.

## Expected outcome

After this story, a reader should be able to answer "what does each top-level
`doc/` bucket mean and how do they relate?" by reading one canonical spec plus
the specialized specs it explicitly references.
