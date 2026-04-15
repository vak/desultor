# Architecture

## Purpose of this file

`doc/desultor/ARCHITECTURE.md` describes the structure of Desultor itself: what the
starter contains today, what boundaries it enforces, and what a future
replacement should preserve.

It is not a target-project product spec. When Desultor is imported into another
repository, that repository should rewrite this file for its own architecture.

## Current architecture

Desultor is intentionally lightweight and docs-first:

1. `Governance layer`
   - project instructions in `AGENTS.md` and `CLAUDE.md`
   - default public-neutral stance
2. `Starter self-documentation layer`
   - `doc/desultor/` for starter-owned docs outside the layered buckets
   - `doc/*/desultor/` for starter-owned notes, specs, RFCs, and stories
3. `Documentation layer`
   - stable contracts in `doc/spec/`
   - reusable notes in `doc/kb/`
   - open questions in `doc/rfc/`
4. `Work-tracking layer`
   - lifecycle containers in `doc/stories/`
5. `Runtime tooling layer`
   - repo-local Claude sidecar helper in `scripts/claude_sidecar.py`
   - `runtime/` reserved for local state and transcripts

## Invariants

- The starter stays public-neutral.
- The starter remains separable from host-project docs through `desultor`
  namespaces inside `doc/`.
- The root README of an imported target project remains project-specific.
- Stable contracts, findings, and open debates do not collapse into one bucket.
- Cross-harness review remains explicit instead of being implied by chat
  history.
- Runtime state is local and disposable; durable meaning lives in tracked
  files.

## Expected replacement boundary

Desultor is expected to be replaced or subsumed by a more serious orchestrator.
That future system should preserve at least:

- explicit project state in repo artifacts;
- clear authorship and review boundaries;
- durable storage of findings and decisions;
- a clean distinction between review, handoff, and ownership transfer.

What should be replaceable:

- the exact helper scripts;
- the exact CLI choreography;
- the current file naming patterns where a better system exists.

## What does not belong here

- target-project domain content;
- chat transcripts;
- rough exploration notes;
- unresolved option comparison that still belongs in `doc/rfc/`;
- step-by-step task tracking that belongs in stories.
