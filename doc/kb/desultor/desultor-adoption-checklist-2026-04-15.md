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

## Copy

- `doc/`
- `AGENTS.md`
- `CLAUDE.md`
- `scripts/`
- relevant `.gitignore` lines

## Starter-owned namespace rule

- keep Desultor's own notes and contracts under `doc/*/desultor/` and
  `doc/desultor/` so they remain detachable after import;
- do not blur those namespaced starter docs into the host project's own docs
  by default.

## Bootstrap entrypoint rule

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
- whether the imported `doc/*/desultor/` layer stays as a reference or is
  removed after harvesting what is needed;
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
