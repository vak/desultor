# Inbox triage and parking policy

## Why this RFC exists

A raw thread staged in `doc/inbox/` described a separate `parked/` bucket for
set-aside work. The current repository already says something stricter in two
different places:

- `doc/inbox/` is an intake bucket, not a permanent archive;
- `doc/stories/backlog/` already plays the parking role.

That meaning was present, but it was scattered. This RFC records the ambiguity
that surfaced during inbox triage and motivates a focused stable spec.

## What was already true before this RFC

- `doc/inbox/README.md` says inbox material should be triaged out into RFC,
  story, KB, spec, or scratch instead of accumulating there.
- `doc/README.md` says parked work is expressed by backlog state rather than by
  a separate top-level parking lot.
- `doc/stories/backlog/README.md` says backlog already plays the parking role.

## Question

Should Desultor keep relying on scattered prose for this behavior, or should it
state a dedicated stable contract for:

- inbox as transient intake;
- cleanup of inbox copies once durable meaning has been transferred elsewhere;
- backlog as the only parking mechanism for accepted deferred work?

## Proposed direction

Yes. The repository should treat this as stable enough for spec, not as an
unresolved open design branch.

The stable contract should say:

- raw incoming material may land in `doc/inbox/` first, but should not stay
  there after it has been normalized;
- accepted but deferred work belongs in `doc/stories/backlog/`, not in a
  separate `doc/parked/` bucket;
- `archived/` is for finished, cancelled, or superseded stories rather than
  "maybe later";
- if a raw external artifact itself remains important, it should gain an
  explicit durable home with context instead of lingering in `inbox/`.

## Result of this RFC pass

This RFC triggered the addition of a stable spec at
`doc/spec/desultor/inbox-triage-and-parking-v0_1.md` and the cleanup of the
triaged inbox source that exposed the drift.
