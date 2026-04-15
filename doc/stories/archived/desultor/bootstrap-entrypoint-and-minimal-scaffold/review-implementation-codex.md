---
kind: story
created: 2026-04-15
updated: 2026-04-15
status: archived
verification: local-evidence
tags: [story, review, implementation, docs, bootstrap, import, scaffold, desultor]
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

No blocking local findings after the bootstrap-guidance correction pass.

## Checks performed

- rewrote the public bootstrap entrypoint in `README.md` around the real human
  flow: empty directory -> open Codex or Claude Code -> give an import prompt
  -> continue with actual project work;
- changed tabula-rasa guidance from "copy the starter repo" to "adapt a minimal
  host-project scaffold";
- made the default non-imported Desultor internals explicit in `README.md`,
  `operation-modes-v0_1.md`, and the adoption checklist;
- aligned the transport RFC with the same host-oriented bootstrap boundary;
- removed the remaining inconsistency where the post-import checklist assumed a
  Desultor reference layer was always imported.

## Residual risk

- The exact transport mechanism is still RFC material rather than stable
  manifest tooling. The current state is a coherent behavioral contract, not an
  automated enforcement layer.
