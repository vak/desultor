---
kind: kb
created: 2026-04-15
updated: 2026-04-15
status: stable
verification: project-rule
tags: [starter, adoption, bootstrap, import, workflow]
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
# Desultor adoption checklist

Use this note when adopting Desultor in any of its intended modes.

## Choose the mode first

- `tabula-rasa bootstrap`
- `guided mix-in into an existing repository`
- `patch export from an existing Desultor-shaped project`

## Default bootstrap surface for a brand-new host project

- adapted `AGENTS.md`
- adapted `CLAUDE.md`
- target repository `README.md`
- target-project `doc/ARCHITECTURE.md`
- target-project `doc/spec/intro.md`
- `doc/` layer skeleton and story workflow shape
- `scripts/claude_sidecar.py` only if repo-local sidecar tooling is actually
  wanted

## Do not import by default during tabula-rasa bootstrap

- `doc/desultor/`
- `doc/spec/desultor/`
- `doc/kb/desultor/`
- `doc/rfc/desultor/`
- `doc/stories/*/desultor/`
- `runtime/`

## Starter-owned namespace rule

- if any Desultor reference layer is imported deliberately, keep its notes and
  contracts under `doc/*/desultor/` and `doc/desultor/` so they remain
  detachable after import;
- do not blur those namespaced starter docs into the host project's own docs
  by default.

## Bootstrap entrypoint rule

- for humans, the normal bootstrap path is:
  - create an empty directory
  - open it in Codex or Claude Code
  - ask the harness to import Desultor from GitHub as a minimal host-project
    scaffold;
- a brand-new Desultor-shaped project may start from either Codex or Claude
  Code;
- the harness that performs the first substantive bootstrap/import pass is the
  primary harness by default;
- change that ownership only through an explicit handoff, not informal
  alternation.

## Rewrite immediately

- target repository `README.md`
- target-project `doc/ARCHITECTURE.md`
- target-project `doc/spec/intro.md`
- any placeholder backlog stories that do not fit the target project

## Decide early

- whether the current starting harness remains primary by default;
- when the counterpart harness is used as reviewer;
- whether repo-local sidecar tooling is actually needed;
- whether any Desultor reference layer should be imported deliberately at all,
  instead of staying only in the source starter repository;
- whether backlog placeholders should stay or be replaced.

## Mix-in guardrails

- inspect collisions instead of overwriting blindly;
- preserve existing authoritative project docs unless the merge deliberately
  replaces them;
- preserve the distinction between namespaced starter docs and host-project
  docs during the merge;
- let the AI harness explain why each conflicting file should be kept, merged,
  or replaced.

## Patch-export guardrails

- export reusable scaffold, not domain residue;
- exclude `runtime/` state and other disposable artifacts;
- scrub private paths, credentials, and operator-specific traces before the
  patch leaves the source repository.

## Keep

- public-neutrality discipline;
- story lifecycle discipline;
- authored-artifact provenance rules;
- explicit handoff versus review distinction.
