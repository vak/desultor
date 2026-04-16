# Project Lifecycle v0.1

## Core flow

The baseline lifecycle is:

`scratch -> rfc -> story -> spec -> code/tests`

Not every change touches every stage. The point is that rough exploration,
decisions, work tracking, and stable contracts should be separated whenever the
task is large enough to justify the distinction.

Blocking or urgent incidents may also enter through `doc/issues/` and trigger a
story directly when normal backlog sequencing would be too slow or too
dishonest for the problem.

## Story activation rule

If the work is larger than a small local edit, create or update a story.

Blocking or urgent issues should start or activate a story promptly. They may
start directly in `active/` with elevated priority instead of waiting through
normal backlog order.

Backlog stories may remain lightweight placeholders with:

- `README.md`
- `STATUS.md`

Once a story becomes active, it should carry the full authored trail.

## Required active-story loop

1. Write `plan.md`.
2. Write `review-plan-*.md`.
3. Rework the plan until it is good enough.
4. For serious stories, obtain `review-external-plan-*.md` from the counterpart
   harness and process findings before the implementation pass.
5. Run the implementation pass.
6. Write `review-implementation-*.md`.
7. Fix findings.
8. Repeat implementation and review until local closure is honest.
9. Obtain `review-external-*.md` from the counterpart harness.
10. Process external findings before final closure.

## Serious-story gate

Serious stories are stories where complexity or impact makes a bad plan
expensive enough that counterpart review should happen before implementation,
not only before closure.

Treat a story as serious when one or more of these apply:

- it changes stable or public-facing contracts;
- it changes repository-level defaults or lifecycle semantics;
- it crosses multiple files or buckets with nontrivial coordination;
- it affects starter-vs-host boundaries, import/export behavior, or ownership
  boundaries between harnesses;
- the likely regression cost is high or the change is hard to reverse honestly.

For serious stories:

- local `review-plan-*.md` still happens first;
- counterpart pre-implementation review should be recorded as
  `review-external-plan-*.md`;
- implementation should begin only after the serious-story plan findings have
  been processed honestly.

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
