# Operation Modes v0.1

## Purpose

Desultor is not only a starter repository. It is also a reusable operating
shape that should support three practical repository-level modes.

## Mode 1: tabula-rasa bootstrap

Use this mode when the target work directory is empty or intentionally new.

Expected behavior:

- use the source repository as reference, but do not mirror it wholesale into
  the new host project by default;
- allow either Codex or Claude Code to perform the initial bootstrap;
- treat the harness that performs the first substantive bootstrap pass as the
  initial primary harness unless ownership is explicitly handed off;
- default to a minimal host-project scaffold:
  - adapted `AGENTS.md` and `CLAUDE.md`
  - host-project `README.md`
  - host-project `doc/ARCHITECTURE.md`
  - host-project `doc/spec/intro.md`
  - `doc/` layer skeleton and story workflow shape
  - optional sidecar tooling only when actually wanted;
- do not import starter-owned Desultor internals such as `doc/desultor/`,
  `doc/spec/desultor/`, `doc/kb/desultor/`, `doc/rfc/desultor/`, or
  `doc/stories/*/desultor/` into the new host project unless explicitly asked
  to keep them as local reference material;
- do not import `runtime/` into the new host project;
- write target-project docs at host-project paths early instead of rewriting
  the starter namespace into project truth;
- open the first active story rather than relying on chat residue.

## Mode 2: guided mix-in into an existing repository

Use this mode when the target repository already has content and naming
collisions are possible.

Expected behavior:

- import should be performed by an AI harness, not by blind overwrite;
- existing `README.md`, architecture notes, and project-specific docs remain
  authoritative unless explicitly superseded;
- starter-owned Desultor docs should land in clearly separable namespaced paths
  rather than silently replacing host-project docs;
- collisions should be resolved by inspection and merge, not by assuming the
  starter always wins.

This is a mix-in mode, not a naive copy mode.

## Mode 3: patch export from an existing Desultor-shaped project

Use this mode when a project has already evolved inside a Desultor-like shape
and part of that operational layer should be extracted for reuse elsewhere.

Expected behavior:

- export only reusable organizational or tooling changes;
- prefer namespaced starter-owned docs over mixed host-project residue when
  selecting what to export;
- exclude runtime state, credentials, private paths, and target-project domain
  residue;
- prefer an AI-curated patch or file selection over a raw repository dump.

## Shared rule across all modes

All three modes assume a capable AI harness such as Codex or Claude Code as the
operator. Both are supported entrypoints. The design target is not a blind
human copy procedure but an inspect-merge-adapt workflow.

## What remains open

The high-level modes are stable enough to state. The exact mechanics for safe
mix-in and clean patch export remain open and therefore belong in RFC material
rather than here.
