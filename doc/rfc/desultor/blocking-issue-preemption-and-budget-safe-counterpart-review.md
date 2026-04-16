# Blocking issue preemption and budget-safe counterpart review

## Why this RFC exists

An operational incident surfaced two related problems:

1. urgent process failures did not have a dedicated issue bucket in `doc/`;
2. counterpart external reviews were launched in a way that spent Claude Code
   budget in the background and produced partial non-artifact output.

The issue layer and lifecycle updates can be stabilized now. The exact
budget-safe review policy is still not fully settled.

## What is already clear

- blocking or urgent problems deserve explicit tracking in `doc/issues/`;
- such issues may start or activate a story directly, potentially at higher
  priority than normal backlog sequencing;
- partial or aborted external-review chatter should not remain as authoritative
  `review-external-*.md` artifacts.

## What is still open

- whether counterpart external review should require explicit budget approval
  before multiple sidecar requests are launched in one pass;
- whether sidecar review output should first land in a temporary file and only
  be promoted to `review-external-*.md` after a valid final artifact exists;
- when it is better to defer external review and keep a story active versus
  spending scarce counterpart-review budget immediately.
- whether external review is always mandatory or should sometimes remain
  optional for narrow, low-risk work where the extra counterpart pass adds
  little value;
- how requested review effort (`low`, `medium`, `high`, `max`) should be chosen
  relative to story complexity, impact, and the current practical strength of
  the counterpart harness.

## Additional tension: optionality and effort calibration

The current stable lifecycle contract requires counterpart external review
before final story closure, and for serious stories it may also require a
pre-implementation external-plan review.

That may still be too rigid as a long-term rule. A stronger policy may need to
say:

- some reviews are mandatory, others are optional or honestly deferrable;
- requested review effort should scale with the complexity and risk of the
  question being reviewed, not mirror the effort of the primary harness by
  default;
- `low` effort may be enough for narrow consistency checks or closure reviews;
- `medium` or `high` may be justified for broad contract changes, architecture,
  migration risk, or subtle semantic regressions;
- the right effort rule should be capability-based rather than tied forever to
  one harness being "stronger" than another, because model and harness strength
  changes over time.

## Current safe stance

Until a stronger contract exists:

- do not bulk-launch counterpart external reviews just to clear `active/`;
- prefer one tightly scoped review at a time when Claude Code budget is a
  concern;
- choose the lowest review effort that is honest for the scope being reviewed;
- if budget pressure blocks honest review, record the issue explicitly and keep
  the affected story open rather than faking closure.
