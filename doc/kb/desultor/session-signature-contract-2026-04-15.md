---
kind: kb
created: 2026-04-15
updated: 2026-04-15
status: stable
verification: project-rule
tags: [workflow, provenance, harness, frontmatter, authorship]
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
# Session signature contract

## Why this note exists

For authored artifacts, content alone is not enough. A useful repository also
needs visible provenance:

- which harness authored the artifact;
- what model information was honestly observable;
- whether a claim came from direct observation or from inference.

Filenames are helpful hints, but they are not the canonical source of truth.

## Scope

This contract is required for authored artifacts such as:

- `plan.md`
- `review-*.md`
- `notes-*.md`

It is recommended for one-shot KB or RFC notes as well.

It is not required for rolling overview files such as:

- `README.md`
- `STATUS.md`
- `ARCHITECTURE.md`

## Required block

```yaml
session_signature:
  harness:
  model_family:
  model_exact:
  reasoning_effort:
```

## Required provenance block

```yaml
session_signature_sources:
  harness:
    source:
    raw_evidence:
  model_family:
    source:
    raw_evidence:
  model_exact:
    source:
    raw_evidence:
  reasoning_effort:
    source:
    raw_evidence:
```

## Source classes

Use coarse provenance classes:

- `direct_context`
- `local_env`
- `ui_signal`
- `official_docs`
- `inference`
- `not_exposed_in_session`

## Honesty rule

Do not guess.

If a field is not directly observable in the current session, write
`not_exposed_in_session` instead of inventing precision.

This applies both to bootstrap self-probe and to authored artifacts.

## Minimal example

```yaml
---
artifact_kind: story-review
author_role: external_reviewer
created: YYYY-MM-DD
updated: YYYY-MM-DD
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
```
