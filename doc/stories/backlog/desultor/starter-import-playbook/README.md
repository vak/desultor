# Starter import playbook

## Why this story exists

Desultor is meant to support:

- fresh bootstrap into a new repository;
- guided mix-in into an existing repository;
- reusable patch export from a Desultor-shaped repository.

That deserves a better playbook than "copy some files and improvise".
Users also should not have to infer whether Codex or Claude Code is the
intended bootstrap entrypoint.

## Desired outcome

- a short import guide for new repositories;
- explicit guidance that fresh bootstrap may start in either Codex or Claude
  Code;
- explicit rules for keeping starter-owned docs under `doc/*/desultor/` and
  `doc/desultor/` instead of collapsing them into host-project docs;
- a short merge guide for existing repositories;
- a repeatable patch-export rule for reusable scaffold changes;
- explicit rules for what to rewrite immediately versus what to preserve;
- a minimal validation path for both harness starters.

## Likely artifacts

- KB note or spec for import choreography
- Codex-first and Claude-first bootstrap notes
- example adaptation sequence
- patch-export checklist
- possible starter checklist refinement
- starter smoke-check for both harness entrypaths
