---
artifact_kind: story-review
author_role: external_reviewer
created: 2026-04-15
updated: 2026-04-15
status: archived
verification: local-evidence
tags: [story, review, external, hygiene, docs, namespacing, desultor]
session_signature:
  harness: claude-code
  model_family: claude-opus-4-6
  model_exact: claude-opus-4-6
  reasoning_effort: not_exposed_in_session
session_signature_sources:
  harness:
    source: direct_context
    raw_evidence: "You are a Claude agent, built on Anthropic's Claude Agent SDK."
  model_family:
    source: direct_context
    raw_evidence: "You are powered by the model named Opus 4.6 (with 1M context). The exact model ID is claude-opus-4-6[1m]."
  model_exact:
    source: direct_context
    raw_evidence: "The exact model ID is claude-opus-4-6[1m]."
  reasoning_effort:
    source: not_exposed_in_session
    raw_evidence: not_exposed_in_session
---
# External Review — doc-path-hygiene

## Scope

Reviewed the following files for namespacing correctness, internal
consistency, and link integrity:

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `doc/README.md`
- `doc/desultor/ARCHITECTURE.md`
- `doc/spec/desultor/intro.md`
- `doc/spec/desultor/operation-modes-v0_1.md`
- `doc/spec/desultor/starter-doc-namespacing-v0_1.md`
- `doc/kb/desultor/desultor-adoption-checklist-2026-04-15.md`
- `doc/stories/README.md`

## Blocking findings

None.

## Checks performed

1. **Namespace discipline.** All starter-owned docs live under
   `doc/desultor/`, `doc/spec/desultor/`, `doc/kb/desultor/`,
   `doc/rfc/desultor/`, or `doc/stories/<state>/desultor/`. No
   starter-owned doc exists at a non-namespaced path. The only
   non-namespaced file in `doc/` is `doc/README.md`, which is the shared
   taxonomy index — explicitly allowed by the namespacing spec.

2. **Link integrity.** Every markdown link target in the reviewed files
   resolves to an existing file. No broken links found.

3. **Stale reference sweep.** Grep for non-namespaced `doc/ARCHITECTURE.md`
   and `doc/spec/intro.md` across the repo returns only legitimate
   occurrences: host-project instruction text (telling adopters what to
   create) and `runtime/` smoke-test fixtures. No stale link points to a
   starter-owned file that was moved.

4. **Cross-file consistency.** The "Read first" lists in `CLAUDE.md` and
   `AGENTS.md` both point to `doc/desultor/ARCHITECTURE.md` and
   `doc/spec/desultor/intro.md`. The root `README.md` repository map and
   the "Suggested first pass" section are consistent with the namespacing
   contract. `doc/README.md` describes namespaced subtrees correctly.

5. **Import contract coherence.** The adoption checklist, the intro spec,
   the operation-modes spec, and the namespacing spec all agree on the
   same boundary: starter docs stay namespaced; host docs are authored at
   non-namespaced paths. No contradictions found.

6. **Session-signature compliance.** Prior story artifacts (`plan.md`,
   `review-plan-codex.md`, `review-implementation-codex.md`) all carry
   valid session-signature frontmatter per the contract.

## Residual risks

- **`runtime/` fixtures reference pre-refactor paths.** The smoke-test
  bootstrap fixtures under `runtime/bootstrap-smoke/` (e.g.
  `codex-first-hello/CLAUDE.md`, `claude-first-hello/AGENTS.md`) still
  contain `doc/ARCHITECTURE.md` and `doc/spec/intro.md` in their
  read-first lists. These are snapshot fixtures of bootstrapped host
  projects, not Desultor starter files, so they are not incorrect. However,
  if those fixtures are ever reused as templates, the non-namespaced paths
  would be the expected host-project convention, not a bug. No action
  required unless the fixtures are promoted to authoritative templates.

- **No automated link-checking.** The refactor was verified by manual grep.
  A future CI lint for broken internal links would prevent regression, but
  this is a tooling improvement, not a hygiene finding.

## Verdict

The namespacing refactor achieves what the plan intended. Starter-owned
docs are cleanly separated, all reviewed cross-references are correct,
and the import contract is internally consistent. No blocking findings
for the intended hygiene scope.
