# Doc Taxonomy v0.1

## Purpose

This spec is the canonical contract for the structure and semantics of
Desultor's `doc/` tree.

Its job is to define what each top-level documentation bucket means and how the
bucket semantics relate to the more focused starter specs.

## Scope

This spec covers:

- the meaning of the top-level `doc/` buckets;
- the distinction between stable contract, reusable knowledge, open design,
  work tracking, and temporary exploration;
- the role of namespaced starter-owned documentation inside the taxonomy;
- which files are navigational indexes versus canonical contracts.

This spec does not replace the more focused subcontracts for:

- issue and incident handling;
- starter namespacing;
- story lifecycle;
- inbox triage and parking;
- public-neutral starter behavior.

## Canonical reading model

- `doc/README.md` is the navigational map for the tree.
- layer README files such as `doc/kb/README.md` or `doc/rfc/README.md` are
  local usage guides for their bucket.
- this file is the canonical stable contract for overall `doc/` taxonomy.
- focused starter specs under `doc/spec/desultor/` own the detailed rules for
  narrower concerns.

## Top-level bucket semantics

- `doc/desultor/`
  - starter-owned self-documentation that describes Desultor itself outside the
    generic layer buckets
  - remains detachable from host-project documentation after import
- `doc/inbox/`
  - transient intake for raw incoming material that may matter but is not yet
    normalized
  - must not become a permanent shadow archive or shadow knowledge base
- `doc/issues/`
  - explicit blocking or urgent problems that are already normalized enough to
    track as issues
  - may trigger direct high-priority story activation when the problem is not a
    small local fix
- `doc/spec/`
  - stable contracts the repository is willing to treat as defaults
  - for Desultor-owned contracts, the stable home is `doc/spec/desultor/`
- `doc/kb/`
  - reusable findings and operational knowledge worth preserving outside one
    story
  - holds observations, lessons, workflow notes, and provenance rules rather
    than stable normative contracts
- `doc/rfc/`
  - open design questions, broad seeds, and option comparisons that are not yet
    stable enough for spec
- `doc/stories/`
  - lifecycle-tracked multi-step work
  - active work, deferred accepted work, and archived history stay separated by
    state
- `doc/scratch/`
  - temporary exploration and rough fragments that are not yet durable enough
    for the other buckets

## Separation rules

- a stable contract belongs in `spec/`, not in `kb/` or `rfc/`;
- a reusable finding belongs in `kb/`, not in `spec/`;
- an unresolved question belongs in `rfc/`, not in `spec/`;
- an urgent or blocking incident belongs in `issues/`, not only in chat,
  backlog prose, or inbox residue;
- multi-step execution history belongs in `stories/`, not in `kb/`;
- rough exploration belongs in `scratch/` unless and until it deserves a more
  durable home;
- raw external material may land in `inbox/`, but its durable meaning should be
  transferred out of `inbox/` rather than left there indefinitely.

These categories are intentionally distinct. Desultor drifts when one bucket
quietly becomes a substitute for another.

## Starter boundary inside the taxonomy

Because Desultor is a reusable starter, starter-owned material should remain
namespaced and detachable:

- `doc/desultor/` for starter self-docs outside the generic buckets;
- `doc/issues/desultor/` for starter-owned issue tracking;
- `doc/*/desultor/` for starter-owned spec, KB, RFC, and story material.

When Desultor is imported into a host project, the host project's own durable
docs should use the non-namespaced layer roots, while the starter-owned
`desultor` namespaces remain removable until deliberately replaced.

## Specialized subcontracts

This file is canonical for overall taxonomy, but it delegates narrower rules:

- `issues-and-incident-handling-v0_1.md` for blocking issues and how they
  trigger stories, RFCs, KB notes, or specs;
- `starter-doc-namespacing-v0_1.md` for starter-vs-host path boundaries;
- `project-lifecycle-v0_1.md` for story activation, required review trail, and
  closure rules;
- `inbox-triage-and-parking-v0_1.md` for intake drain semantics and
  backlog-as-parking;
- `public-neutrality-v0_1.md` for starter-level publication and rewrite
  boundaries.

## Failure modes

The taxonomy is being used incorrectly when:

- `inbox/` becomes a passive archive;
- `issues/` becomes a second inbox or a passive graveyard;
- `kb/` starts carrying settled normative contracts that should be in `spec/`;
- `spec/` starts carrying unresolved branches that should still be in `rfc/`;
- `stories/` become the only place where durable conclusions exist;
- starter-owned documentation blurs into host-project source-of-truth paths.
