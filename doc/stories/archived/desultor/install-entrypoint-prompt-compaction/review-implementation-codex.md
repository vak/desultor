---
kind: story
created: 2026-04-15
updated: 2026-04-15
status: archived
verification: local-evidence
tags: [story, review, implementation, docs, install, bootstrap, prompt, readme, desultor]
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

No blocking local findings after the install-entrypoint compaction pass.

## Checks performed

- added a root `INSTALL.md` as the canonical bootstrap contract for fresh
  projects;
- reduced the root `README.md` quickstart to a short two-prompt entrypoint;
- made `Then help me build: ...` an explicit second prompt in the same session;
- moved detailed fresh-project boundary notes out of the quickstart and into
  `INSTALL.md` and surrounding explanatory sections;
- shortened the opening README description and moved the longer stopgap/scope
  explanation into a lower `Operating scope` section;
- added a minimal scaffold sanity-check in `INSTALL.md`;
- inserted a public-facing Desultor image near the top of `README.md`.

## Residual risk

- the public README is now lighter, but it still carries some operational
  detail beyond the quickstart;
- import and merge mechanics remain documented contracts rather than tooling.
