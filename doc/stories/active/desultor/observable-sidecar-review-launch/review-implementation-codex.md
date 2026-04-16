---
kind: story
created: 2026-04-16
updated: 2026-04-16
status: active
verification: local-evidence
tags: [story, review, implementation, sidecar, tmux, observability, desultor]
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
# Implementation Review

## Findings

No blocking local findings after the observable-sidecar-review-launch pass.

## Checks performed

- added a visible `tmux-ask` launch path that keeps the raw Claude stream in
  the `tmux` window while persisting normalized sidecar result data under a
  per-run directory;
- kept `ask` compatible by making review-artifact validation an explicit
  `--assistant-output-contract` instead of a blanket behavior change;
- updated the root README, cross-harness workflow KB note, umbrella backlog
  status, and the incident document so the new path is documented as a
  mitigation rather than left as script-only behavior;
- verified locally with:
  - `python3 -m py_compile scripts/claude_sidecar.py`
  - `python3 scripts/claude_sidecar.py --help`
  - `python3 scripts/claude_sidecar.py ask --help`
  - `python3 scripts/claude_sidecar.py tmux-ask --help`
  - direct contract checks for `markdown-heading` via a local Python import.
- ran a real cheap smoke through the new visible path:
  - `python3 scripts/claude_sidecar.py tmux-ask --new-session --model sonnet --effort low ...`
  - observed successful completion, valid artifact writing, and effective model
    `claude-sonnet-4-6`;
  - corrected an initial overcorrection where keeping the window open by
    default would have multiplied idle shells; the final behavior is explicit
    `--keep-open-on-exit` rather than a sticky default;
  - observed that even this cheap smoke still paid a large startup cache cost
    (`cache_creation_input_tokens: 18499`, `total_cost_usd: 0.06994025`).

## Residual risk

- the deeper budget-meter problem remains unsolved, so the incident is
  mitigated rather than fully closed;
- counterpart external review is deliberately deferred for this story because
  the incident itself is about expensive blind Claude review launches.
