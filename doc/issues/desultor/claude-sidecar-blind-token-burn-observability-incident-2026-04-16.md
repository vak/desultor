---
kind: issue
created: 2026-04-16
updated: 2026-04-16
status: mitigated
severity: high
priority: high
verification: local-evidence
tags: [issue, process, sidecar, claude-code, budget, observability, tmux, external-review, desultor]
session_signature:
  harness: codex
  model_family: gpt-5.4
  model_exact: gpt-5.4
  reasoning_effort: xhigh
session_signature_sources:
  harness:
    source: direct_context
    raw_evidence: "You are Codex, a coding agent based on GPT-5."
  model_family:
    source: local_env
    raw_evidence: "model = \"gpt-5.4\""
  model_exact:
    source: local_env
    raw_evidence: "model = \"gpt-5.4\""
  reasoning_effort:
    source: local_env
    raw_evidence: "model_reasoning_effort = \"xhigh\""
---
# Claude sidecar blind token burn and observability incident

## Summary

A host project that had recently synchronized itself against the current
Desultor organization ran into a sharper sidecar-control failure mode than the
starter currently documents away.

Claude Code external-review runs were started through sidecar-oriented tooling,
but the launch path was effectively blind:

- the initiating Codex session could not see useful live Claude activity;
- the human operator in `tmux` could not see the same stdout stream either;
- timeout choice therefore became guesswork rather than an informed boundary;
- at least one `CC/high` run reportedly consumed about `~25%` of a five-hour
  budget window without producing a valid review artifact.

The exact budget fraction was reported by the human operator rather than read
from an honest runtime meter. Current sidecar/runtime output still does not
expose a trustworthy remaining-budget field, which is part of the incident.

## Trigger context

The incident happened while trying to obtain an external Claude Code review for
organization-alignment work in a separate project that had already aligned
itself with Desultor-style docs/process structure.

This matters for Desultor because the host project was not doing something
exotic. It was exercising exactly the kind of cross-harness review flow that
Desultor is supposed to make less sloppy.

## Evidence from the recent run

- multiple `claude -p --verbose --output-format stream-json --effort high`
  review runs were launched through sidecar-related orchestration paths;
- one reviewed artifact path ended up containing only:
  - `API Error: Unable to connect to API (FailedToOpenSocket)`;
- a sidecar retry was then launched in `tmux`, but the chosen wrapper path
  still presented the human with effectively silent wrapper sessions rather
  than a trustworthy mirror of the raw Claude stdout stream;
- the operator explicitly complained that about `~25%` of a five-hour Claude
  window had been burned blindly;
- the operator's original reason for wanting `tmux` was not interactive manual
  typing, but shared visibility into what the running Claude session was doing;
- long-lasting session ideas were considered partly because the one-shot launch
  path lacked clear observability and timeout confidence.

## Why the current gap is serious

The problem is not only budget cost. It is a control-surface mismatch.

Desultor currently has useful pieces:

- `ask` for managed one-shot requests;
- `tmux-claude` for visible resume of an already established session;
- `tmux-log` for transcript-tail observability;
- `handoff` for restart notes.

But this incident exposed the missing piece:

- there is no clean, first-class way to launch a one-shot or review-style
  Claude run such that the human sees the same meaningful live output that the
  orchestrator relies on.

That gap creates several secondary failures:

- budget is spent before the operator can tell whether the run is healthy;
- timeout selection becomes arbitrary because the run may appear silent even
  while doing retries/backoff or while hanging in an unclear state;
- wrappers can give the illusion of observability while only showing a quiet
  Python control script instead of Claude's own output;
- the temptation rises to keep long-lived sessions alive merely to avoid paying
  the startup-visibility penalty again.

## Why the obvious workaround is not enough

Ad-hoc `tmux send-keys` and manual capture are not a clean answer.

They are unattractive because they:

- mix orchestration with brittle terminal driving;
- blur responsibility between human and orchestrator;
- are hard to reason about when the human also wants to inspect or type;
- do not define a stable contract for what stdout/stderr stream is considered
  canonical;
- can still leave artifact-writing and validation logic scattered outside the
  controller.

In short: raw terminal puppeteering is exactly the sort of accidental control
surface Desultor was supposed to replace, not institutionalize.

## Immediate handling in the host-project incident

- blind Claude review runs were stopped;
- bogus partial or error-only review artifact output was not kept as a valid
  external review document;
- the temporary experimental wrapper path that still produced silent sessions
  was removed again instead of being normalized;
- the host-project story was left honestly open without claiming that an
  external Claude review had succeeded.

## Mitigation now available in the starter

The starter now has a concrete mitigation path:

- `python3 scripts/claude_sidecar.py tmux-ask ...` launches a visible one-shot
  Claude run in `tmux` while still writing normalized sidecar state and
  transcripts;
- per-run observability lands under `runtime/claude-sidecar/runs/<run-id>/`
  with `prompt.txt`, `stream.stdout`, `stream.stderr`, `status.json`, and
  `result.json`;
- review-artifact writing can now use
  `--assistant-output-contract markdown-heading` so obvious progress chatter is
  not promoted directly into `review-external-*.md`.

This is an honest mitigation, not full closure. The workflow still lacks a
trustworthy remaining-budget meter, so timeout and retry policy remain partly
judgment-based even though the launch path is no longer blind.

## Follow-up questions for Desultor

1. What is the canonical observable launch path for one-shot Claude review runs
   where a human wants to see the same live state as the orchestrator?
2. Should Desultor define a first-class raw-stream `tmux` launcher that runs
   Claude itself visibly while still preserving normalized sidecar state and
   artifact discipline?
3. What timeout policy is honest for `CC/high` review runs when live output is
   sparse or backoff-heavy?
4. How should budget-safe review policy change when the runtime still cannot
   expose a trustworthy remaining-budget meter?
5. To what extent are long-lived sessions a real product need versus a symptom
   of missing observable startup paths?

## Suggested direction

Desultor likely needs an explicit contract for:

- visible raw-stream review launch;
- distinction between controller stdout and Claude stdout;
- artifact validation before treating `--assistant-output` as a real review;
- budget-safe retry/timeout policy under weak runtime observability.

Without that, the starter still leaves a high-cost blind spot exactly where
cross-harness review is supposed to be routine.
