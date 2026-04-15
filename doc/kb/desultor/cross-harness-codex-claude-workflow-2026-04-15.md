---
kind: kb
created: 2026-04-15
updated: 2026-04-15
status: stable
verification: project-rule
tags: [workflow, cross-harness, codex, claude-code, review, handoff, sop]
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
# Cross-harness workflow: Codex and Claude Code

## Why this note exists

Projects that use both Codex and Claude Code need a clean distinction between:

- external review by another harness;
- a genuine ownership handoff to another harness.

Those are different modes and should not be blurred.

## Bootstrap entry rule

A Desultor-shaped project may start in Codex or in Claude Code.

The harness that performs the first substantive bootstrap or import pass is the
primary harness by default.

Do not switch ownership by casual alternation in chat. Use explicit review mode
or an explicit handoff artifact.

## Mode A: primary harness plus external review

Use this mode when:

- the main plan and implementation already happened in one harness;
- you want an independent review pass from the counterpart harness;
- the source of truth stays in the current repository state.

### Minimal procedure

1. Finish the local story pass first.
2. Narrow the review scope:
   - exact files
   - what changed
   - expected output artifact path
3. Ask the counterpart harness for review, not for implementation.
4. Save the result as `review-external-*.md`.
5. Process findings back in the primary harness.

### Example shape

```bash
python3 scripts/claude_sidecar.py ask --new-session --effort medium \
  --label external-review \
  --assistant-output doc/stories/active/<story>/review-external-claude-code.md \
  "<review prompt with exact files, scope, and artifact contract>"
```

## Mode B: ownership handoff

Use this mode only when the next substantive pass should be owned by the other
harness.

### Minimal procedure

1. Write an explicit handoff artifact.
2. State:
   - current goal
   - files to read first
   - what is already done
   - what remains open
   - output expectations
   - do-not-regress constraints
3. Start the other harness as the new primary author.
4. Let resulting authored artifacts carry honest provenance.

### Example shape

```bash
python3 scripts/claude_sidecar.py handoff --effort high \
  --assistant-output runtime/claude-sidecar/handoff/latest.md
```

## Decision rule

Ask first:

1. Do we need independent review only?
2. Or do we want the next substantive pass to move to the other harness?

If the answer is 1, stay in review mode.

If the answer is 2, write a handoff and switch ownership honestly.
