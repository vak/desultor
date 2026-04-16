---
kind: issue
created: 2026-04-16
updated: 2026-04-16
status: mitigated
severity: high
priority: high
verification: local-evidence
tags: [issue, process, sidecar, claude-code, budget, external-review, desultor]
session_signature:
  harness: codex
  model_family: gpt-5
  model_exact: not_exposed_in_session
  reasoning_effort: not_exposed_in_session
session_signature_sources:
  harness:
    source: direct_context
    raw_evidence: "You are Codex, a coding agent based on GPT-5."
  model_family:
    source: direct_context
    raw_evidence: "You are Codex, a coding agent based on GPT-5."
  model_exact:
    source: not_exposed_in_session
    raw_evidence: not_exposed_in_session
  reasoning_effort:
    source: not_exposed_in_session
    raw_evidence: not_exposed_in_session
---
# Claude sidecar background review budget incident

## Summary

Two Claude Code sidecar external reviews were launched to help clear active
stories. The requests continued running in the background, consumed Claude Code
budget, and wrote partial assistant chatter into review artifact paths instead
of final review documents.

## Affected paths

- `doc/stories/active/desultor/doc-taxonomy-canonical-spec/review-external-claude-code.md`
- `doc/stories/active/desultor/risk-gated-external-plan-review/review-external-claude-code.md`

## Evidence

- partial files were observed containing intermediate assistant text such as
  "Let me read all the relevant files" rather than valid review artifacts;
- `ps` output showed active `scripts/claude_sidecar.py ask` and `claude -p`
  processes for those review requests after the terminal appeared idle;
- the user explicitly raised the budget concern during cleanup.

## Immediate handling

- the partial review artifacts were deleted;
- `doc/issues/` was added so incidents like this have a durable home;
- lifecycle/process docs were updated so blocking or urgent issues can start a
  high-priority story directly instead of being buried in normal backlog flow;
- an RFC was opened for the remaining budget-safe counterpart-review question.

## Follow-up

See
`doc/rfc/desultor/blocking-issue-preemption-and-budget-safe-counterpart-review.md`
for the still-open policy question about how aggressive counterpart external
review should be when Claude Code budget is constrained.

During the immediate cleanup pass, the safer temporary workaround was:

- do not run counterpart reviews in parallel when budget pressure is visible;
- avoid trusting `--assistant-output` as a final artifact path unless the
  result is validated first;
- recover a review artifact from sidecar raw output only when a real final
  artifact is present there, otherwise keep the story open and ask for a clean
  rerun.
