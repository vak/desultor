# Portable sidecar controller hardening

## Why this story exists

The starter already includes a minimal Claude sidecar controller, but it is
still intentionally small. A stronger public starter should harden portability,
error handling, and verification.

## Desired outcome

- clearer runtime schema and transcript guarantees;
- smoke-test guidance for new environments;
- cleaner failure modes around missing `claude` or `tmux`;
- explicit permission-mode control for non-interactive Claude-side write passes;
- optional companion support for other harness control patterns.

## Likely artifacts

- controller improvements in `scripts/claude_sidecar.py`
- KB note for smoke-test expectations
- story-local plan and review trail once activated
