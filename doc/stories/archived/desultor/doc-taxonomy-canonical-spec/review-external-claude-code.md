---
kind: story
created: 2026-04-16
updated: 2026-04-16
status: archived
verification: local-evidence
tags: [story, review, external, docs, taxonomy, semantics, spec, desultor]
session_signature:
  harness: claude-code
  model_family: claude
  model_exact: claude-opus-4-6[1m]
  reasoning_effort: low
session_signature_sources:
  harness:
    source: claude_sidecar_observation
    raw_evidence: "observed via scripts/claude_sidecar.py ask session e85f2397-85e1-411b-a0d9-31b2c88bd669"
  model_family:
    source: claude_sidecar_observation
    raw_evidence: "observed.model_exact=claude-opus-4-6[1m]"
  model_exact:
    source: claude_sidecar_observation
    raw_evidence: "observed.model_exact=claude-opus-4-6[1m]"
  reasoning_effort:
    source: claude_sidecar_observation
    raw_evidence: "observed.requested_effort=low"
---
# External Review — doc-taxonomy-canonical-spec

## Scope

External counterpart review of the doc-taxonomy-canonical-spec story, covering
the canonical taxonomy spec, updated navigational indexes, and root README
changes, checked against the plan and surrounding specs.

## Blocking findings

None.

## Checks performed

1. Plan satisfaction — all five plan steps are addressed:
   - inventory captured in `notes-current-taxonomy-map.md`;
   - canonical spec written as `doc/spec/desultor/doc-taxonomy-v0_1.md`;
   - `doc/README.md` reduced to navigational map with explicit pointer to the
     canonical spec;
   - `doc/spec/README.md` updated to list the new spec;
   - root `README.md` updated with a direct link to the canonical taxonomy
     spec.

2. Canonical spec quality — `doc-taxonomy-v0_1.md` is a clean taxonomy
   contract, not a duplicate giant file. It defines bucket semantics in
   concise entries and delegates specialized concerns by explicit reference to
   five named subcontracts. No lifecycle detail, no full namespacing rules,
   and no inbox/parking mechanics are absorbed.

3. Boundary clarity — the three-tier reading model (canonical spec vs
   navigational index vs layer README) is stated explicitly in the spec's
   "Canonical reading model" section and echoed in `doc/README.md`'s "Reading
   stance" paragraph. Roles do not overlap.

4. Cross-spec consistency checks:
   - `starter-doc-namespacing-v0_1.md` paths (`doc/desultor/`,
     `doc/*/desultor/`) match the taxonomy spec's "Starter boundary" section;
   - `issues-and-incident-handling-v0_1.md` semantics (issues as normalized
     problem statements, not raw intake) match the taxonomy spec's `issues/`
     bucket definition and failure-mode list;
   - the taxonomy spec references `public-neutrality-v0_1.md` as a subcontract
     but does not restate its rules, preserving delegation;
   - no contradiction found with `project-lifecycle-v0_1.md` or
     `inbox-triage-and-parking-v0_1.md`.

5. Public neutrality — no operator-specific identity, private preferences, or
   host-project details leaked into any of the deliverables.

6. Non-goal compliance — the implementation does not redesign the taxonomy,
   merge all specs into one file, or change lifecycle or namespacing policy.
   All four plan non-goals are respected.

## Residual risks

- layer README files (`kb/README.md`, `rfc/README.md`, etc.) do not yet
  back-reference the canonical taxonomy spec. This is optional hygiene noted in
  the implementation review and is not a correctness blocker;
- the taxonomy spec references `public-neutrality-v0_1.md`, which exists in
  `doc/spec/README.md`'s index. If that file were missing or renamed, the
  delegation link would break silently. A future pass could add a validation
  check, but this is not blocking for closure.

## Verdict

The story satisfies its plan, introduces no semantic contradictions with
surrounding specs, and maintains clean separation between canonical contract,
navigational index, and layer-local guides. Ready for closure.
