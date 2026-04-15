# Project Lifecycle v0.1

## Core flow

The baseline lifecycle is:

`scratch -> rfc -> story -> spec -> code/tests`

Not every change touches every stage. The point is that rough exploration,
decisions, work tracking, and stable contracts should be separated whenever the
task is large enough to justify the distinction.

## Story activation rule

If the work is larger than a small local edit, create or update a story.

Backlog stories may remain lightweight placeholders with:

- `README.md`
- `STATUS.md`

Once a story becomes active, it should carry the full authored trail.

## Required active-story loop

1. Write `plan.md`.
2. Write `review-plan-*.md`.
3. Rework the plan until it is good enough.
4. Run the implementation pass.
5. Write `review-implementation-*.md`.
6. Fix findings.
7. Repeat implementation and review until local closure is honest.
8. Obtain `review-external-*.md` from the counterpart harness.
9. Process external findings before final closure.

## Meaning of implementation

Implementation is not limited to code. It may be:

- documentation;
- specs;
- KB notes;
- RFC updates;
- scripts;
- code and tests.

## Authored artifact provenance

Authored artifacts should carry session-signature frontmatter:

- `plan.md`
- `review-*.md`
- `notes-*.md`

The canonical rule lives in
`doc/kb/desultor/session-signature-contract-2026-04-15.md`.

## Closure rule

A story is not closed honestly unless:

- the review trail exists;
- external cross-harness review was processed or explicitly shown to have no
  new findings;
- durable conclusions were moved into the right project layer instead of being
  left only in chat context.
