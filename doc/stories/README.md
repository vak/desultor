# stories/

Stories hold multi-step work by lifecycle state:

- `active/` - work in progress right now
- `backlog/` - accepted but not currently active work
- `archived/` - completed, cancelled, or superseded work kept for history

State buckets may contain namespaced subtrees such as `active/desultor/` when a
reusable starter or scaffold needs to keep its own work clearly separable from
host-project work.

Blocking or urgent issues may activate a story directly from `doc/issues/`,
potentially in `active/` and at higher priority than normal backlog sequencing.

## Story shape

When a story is only a backlog placeholder, it may start with:

- `README.md`
- `STATUS.md`

Once a story becomes active, the expected authored trail is:

- `plan.md`
- `review-plan-*.md`
- for serious stories: `review-external-plan-*.md`
- `review-implementation-*.md`
- `review-external-*.md`
- optional `notes-*.md`

## Required active-story loop

1. write `plan.md`
2. review the plan
3. rework until the plan is good enough
4. for serious stories, obtain external plan review from the counterpart
   harness before implementation
5. run the implementation pass
6. review the implementation
7. fix findings
8. repeat until local closure is honest
9. obtain external review from the counterpart harness
10. process external findings before closure

See `doc/spec/desultor/project-lifecycle-v0_1.md` for the serious-story gate
and the criteria for when `review-external-plan-*.md` is required.

## Authored artifact provenance

Authored story artifacts should carry session-signature frontmatter. The
canonical rule is in
`doc/kb/desultor/session-signature-contract-2026-04-15.md`.

## Closure

A story is not honestly closed until:

- the review trail exists;
- external review was processed or explicitly shown to add no new findings;
- durable conclusions have been moved into the right project layer.
