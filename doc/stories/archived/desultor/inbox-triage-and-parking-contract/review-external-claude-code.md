---
artifact_kind: story-review
author_role: external_reviewer
created: 2026-04-16
updated: 2026-04-16
status: archived
verification: local-evidence
tags: [story, review, external, inbox, triage, parking, backlog, spec, rfc, desultor]
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
# External Review — inbox-triage-and-parking-contract

## Scope

Reviewed the full deliverable set of the story against the plan and prior
reviews:

- `doc/rfc/desultor/inbox-triage-and-parking-policy.md` (new RFC)
- `doc/spec/desultor/inbox-triage-and-parking-v0_1.md` (new spec)
- `doc/inbox/README.md` (updated)
- `doc/stories/backlog/README.md` (updated)
- `doc/README.md` (updated)
- `doc/spec/README.md` (updated)
- `README.md` (updated)

Also checked cross-references from `doc/spec/desultor/doc-taxonomy-v0_1.md`
and the story trail (`plan.md`, `review-plan-codex.md`,
`review-implementation-codex.md`).

## Blocking findings

None.

## Checks performed

1. **Plan coverage.** The plan listed five steps. All five are satisfied:
   RFC written, spec written, layer READMEs updated, higher-level indexes
   updated, and the triaged inbox source removed (only `README.md` remains
   in `doc/inbox/`).

2. **RFC-to-spec coherence.** The RFC at
   `doc/rfc/desultor/inbox-triage-and-parking-policy.md` states the
   ambiguity, proposes four contract points, and records that the spec was
   created. The spec at `doc/spec/desultor/inbox-triage-and-parking-v0_1.md`
   covers all four points (inbox as transient intake, cleanup after
   normalization, backlog-as-parking, archived vs. "maybe later") and adds
   triage targets and failure modes. No contradiction between RFC and spec.

3. **Layer README consistency.** `doc/inbox/README.md` now explicitly states
   the transient-intake rule, lists triage targets matching the spec, warns
   against shadow-archive drift, and cross-references the spec.
   `doc/stories/backlog/README.md` now explicitly states the parking role
   and cross-references the spec. Both are consistent with the spec text.

4. **Index discoverability.** `doc/README.md` lists the new spec in its
   "Read this next" section. `doc/spec/README.md` lists it in the starter
   specs index. `README.md` lists it in the repository map. The spec is
   reachable from all three navigational entry points.

5. **Doc-taxonomy alignment.** `doc/spec/desultor/doc-taxonomy-v0_1.md`
   already delegates inbox triage and parking rules to the new spec via its
   "Specialized subcontracts" section. The `inbox/` bucket description in
   the taxonomy spec is consistent with the new spec's contract.

6. **No stale `parked/` references.** Grep for `parked/` shows only
   intentional occurrences: the RFC explaining why a separate bucket is
   excluded, the spec's contract and failure-modes sections, and
   `doc/inbox/README.md` repeating the rule. No file proposes or creates a
   `doc/parked/` directory.

7. **Inbox cleanliness.** `doc/inbox/` contains only `README.md`. The raw
   source that triggered this story has been removed, consistent with the
   plan and the new spec's cleanup rule.

8. **Session-signature compliance.** All story artifacts (`plan.md`,
   `review-plan-codex.md`, `review-implementation-codex.md`) carry valid
   session-signature frontmatter per the contract.

## Residual risks

- **No automated inbox-staleness check.** The spec defines failure modes
  (inbox becoming a shadow archive, parked bucket competing with backlog)
  but enforcement is purely convention-based. A future CI lint or periodic
  audit story could catch drift, but this is a tooling improvement, not a
  gap in the current story's scope.

- **RFC left open-ended.** The RFC records that it triggered the spec but
  does not carry an explicit "resolved" or "superseded" status in its
  frontmatter. This is consistent with the current RFC convention (RFCs in
  this repo lack YAML frontmatter), but a future pass could add status
  tracking to RFCs for clarity.

## Verdict

The story delivers what the plan intended. The spec is well-scoped, the
RFC motivates it cleanly, the layer READMEs and indexes are updated, and
the triaged inbox source has been removed. No blocking findings. The story
is ready for closure.
