---
kind: kb
created: 2026-04-16
updated: 2026-04-16
status: stable
verification: local-evidence
tags: [claude-code, sidecar, tmux, review, observability, budget, workflow]
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
# Observable Claude review launch

## Why this note exists

The previous sidecar surface had a visibility gap:

- `ask` could launch a one-shot review run;
- `tmux-log` could tail the normalized transcript after the fact;
- `tmux-claude` could resume an already-established session interactively;
- but there was no first-class path that let a human watch the raw one-shot
  Claude review stream live while the controller still kept normalized state.

## Recommended path

When a human wants live review visibility, use `tmux-ask` rather than a blind
background `ask`.

Example shape:

```bash
python3 scripts/claude_sidecar.py tmux-ask --new-session --effort low \
  --model sonnet \
  --label external-review \
  --assistant-output-contract markdown-heading \
  --assistant-output doc/stories/active/<story>/review-external-claude-code.md \
  "<review prompt with exact files, scope, and artifact contract>"
```

## What this changes

- the returned launcher JSON points to a per-run directory under
  `runtime/claude-sidecar/runs/<run-id>/`;
- the `tmux` window shows Claude's own live raw stream, not only quiet wrapper
  chatter;
- if you want post-run inspection, pass `--keep-open-on-exit`; otherwise the
  window is only guaranteed to exist while the command is actually running;
- the run directory keeps `prompt.txt`, `stream.stdout`, `stream.stderr`,
  `status.json`, and `result.json`;
- normalized transcript/state updates still land in the usual sidecar runtime
  files.

## Artifact discipline

For review artifacts, use `--assistant-output-contract markdown-heading`.

That contract is intentionally small:

- it does not pretend to prove review quality;
- it does stop obvious progress chatter such as "Let me read the files" from
  being written directly into `review-external-*.md`.

If the contract fails:

- the Claude request may still have succeeded as a sidecar call;
- the review artifact file is not written;
- the normalized result keeps the validation failure so the story can remain
  honestly open.

## Budget-safe stance

- For smoke tests or routine validation runs, pass an explicit cheaper model
  such as `--model sonnet` rather than silently inheriting an expensive
  default like `opus` from `~/.claude/settings.json`.
- Prefer `--effort low` for narrow consistency checks or routine review passes
  unless the scope honestly demands more.
- Use the observable `tmux` path when timeout choice would otherwise be blind.
- Do not invent a remaining-budget percentage from partial runtime metadata.

## Long-lived sessions

Long-lived sessions are not merely a workaround for bad observability.

They remain a valid story-scope cost-control tool when:

- the chosen review profile is expensive, for example `opus` with `high`
  effort;
- early turns pay a large context-acquisition cost before real review begins;
- multiple narrow follow-up passes would otherwise restart that cost from
  scratch.

Observable `tmux-ask` reduces blind startup cost, but it does not eliminate
the legitimate need for a story-local long-lived Claude session when the review
shape actually benefits from continuity.

## Observed smoke on 2026-04-16

A real `tmux-ask` smoke was run on April 16, 2026 with:

- `--model sonnet`
- `--effort low`
- a tiny markdown-only prompt
- `--assistant-output-contract markdown-heading`

Observed result:

- the visible `tmux` launch path completed successfully;
- the artifact contract passed and wrote the assistant output file;
- the effective model was `claude-sonnet-4-6`;
- `modelUsage` also reported a small internal `claude-haiku-4-5-20251001`
  bucket alongside the main Sonnet usage;
- a follow-up smoke with `--keep-open-on-exit` confirmed that a finished window
  can be left open intentionally for human inspection;
- runtime still reported a substantial startup/context cost:
  - `cache_creation_input_tokens: 18499`
  - `total_cost_usd: 0.06994025`

Implication:

- cheaper model plus low effort is useful for smoke testing and narrow checks;
- it does **not** make repeated fresh one-shot sessions cheap enough to dismiss
  the value of story-scope long-lived sessions.

## Limit

This note mitigates the observability/control-surface problem. It does not
solve the deeper product gap that Claude Code still does not expose a
trustworthy remaining-budget meter in this workflow.
