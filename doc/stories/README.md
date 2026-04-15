# stories/

Stories hold multi-step work by lifecycle state:

- `active/` - work in progress right now
- `backlog/` - accepted but not currently active work
- `archived/` - completed, cancelled, or superseded work kept for history

State buckets may contain namespaced subtrees such as `active/desultor/` when a
reusable starter or scaffold needs to keep its own work clearly separable from
host-project work.

## Story shape

When a story is only a backlog placeholder, it may start with:

- `README.md`
- `STATUS.md`

Once a story becomes active, the expected authored trail is:

- `plan.md`
- `review-plan-*.md`
- `review-implementation-*.md`
- `review-external-*.md`
- optional `notes-*.md`

## Required active-story loop

1. write `plan.md`
2. review the plan
3. rework until the plan is good enough
4. run the implementation pass
5. review the implementation
6. fix findings
7. repeat until local closure is honest
8. obtain external review from the counterpart harness
9. process external findings before closure

## Authored artifact provenance

Authored story artifacts should carry session-signature frontmatter. The
canonical rule is in
`doc/kb/desultor/session-signature-contract-2026-04-15.md`.

## Closure

A story is not honestly closed until:

- the review trail exists;
- external review was processed or explicitly shown to add no new findings;
- durable conclusions have been moved into the right project layer.
