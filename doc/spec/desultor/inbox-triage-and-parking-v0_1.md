# Inbox Triage and Parking v0.1

## Purpose

Desultor needs an explicit contract for how raw incoming material becomes
durable repository state. The repository already separates intake, open
questions, reusable knowledge, and lifecycle-tracked work. This spec makes the
intake and parking rules explicit so they do not drift into shadow archives or
duplicate buckets.

## Contract

- `doc/inbox/` is a transient intake bucket, not a permanent archive.
- Anything worth keeping must be normalized out of `doc/inbox/` into the
  correct durable layer or deleted if it does not deserve retention.
- Once the durable meaning of an inbox item has been transferred elsewhere, the
  inbox copy should be removed unless the raw artifact itself remains an
  intentional project asset and has been moved to a more appropriate durable
  home with context.
- Parking accepted but deferred work is done through `doc/stories/backlog/`,
  not through a separate top-level `doc/parked/` bucket.
- `doc/stories/archived/` is for completed, cancelled, or superseded stories,
  not for "maybe later" work.
- `doc/scratch/` is for rough exploration, not for accepted deferred work.

## Triage targets

- stable contract: `doc/spec/` or `doc/spec/desultor/`
- reusable operational note: `doc/kb/` or `doc/kb/desultor/`
- unresolved design question or option comparison: `doc/rfc/` or
  `doc/rfc/desultor/`
- accepted multi-step work: `doc/stories/active/` or `doc/stories/backlog/`
- rough fragment that is not yet durable: `doc/scratch/`

## Parking rule

When a user or agent wants to set aside a real initiative:

1. create or keep a backlog story;
2. record the current state and reason in `STATUS.md` when the story is a
   backlog placeholder;
3. move it to `active/` only when it becomes the current focus.

A separate top-level parked bucket is intentionally excluded because it
duplicates backlog semantics and weakens lifecycle tracking.

## Failure modes

Desultor drifts when:

- `doc/inbox/` becomes a shadow knowledge base or passive archive;
- raw source dumps remain in `doc/inbox/` after their durable meaning has
  already been carried into KB, RFC, spec, or story artifacts;
- a separate `parked/` tree competes with `stories/backlog/` for the same role.
