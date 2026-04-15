# desultor

Desultor is a public-neutral project starter for teams that want a disciplined
docs layout, an explicit work lifecycle, and a practical Codex/Claude Code
operating model before a serious harness orchestrator exists.

Starter-owned documentation is namespaced under `doc/*/desultor/` and
`doc/desultor/` so it remains separable from host-project documentation after
import.

It is intentionally a stopgap. The point is not to pretend that markdown files
and a few scripts are a real orchestration system. The point is to make project
state, review boundaries, and cross-harness work less sloppy until something
better replaces them.

It is also meant to support three repository-level operations:

1. bootstrap into a tabula-rasa work directory;
2. mix into an existing repository where collisions are expected and must be
   handled by an AI harness rather than by blind overwrite;
3. export a reusable patch from an existing Desultor-shaped project.

## What it gives you

- a `doc/` taxonomy that separates stable contracts, reusable findings, open
  design questions, and lifecycle-tracked work;
- starter-owned reference docs kept under `desultor`-namespaced paths so they
  can be removed from a host project cleanly later;
- a story workflow that forces plan, review, implementation, and external
  cross-harness review to become explicit artifacts;
- starter instructions for both Codex (`AGENTS.md`) and Claude Code
  (`CLAUDE.md`);
- a lightweight repo-local Claude sidecar controller in
  `scripts/claude_sidecar.py`;
- backlog placeholders for Desultor's own next development steps.

## What it is not

- not a domain template;
- not a replacement for a target project's own product or research README;
- not a promise that Codex and Claude Code behave identically;
- not the final orchestrator.

## Start a brand-new project

If you want to use Desultor as the initial operating scaffold for a new
repository, use this sequence:

1. Create an empty repository or work directory.
2. Copy in the Desultor scaffold:
   - `doc/`
   - `AGENTS.md`
   - `CLAUDE.md`
   - `scripts/`
   - relevant `.gitignore` entries
3. Open the new repository in either Codex or Claude Code and ask it to
   perform the first substantive bootstrap pass. The starting harness becomes
   the initial primary harness until an explicit handoff or external review
   changes it.
4. Write the host project's own root `README.md` early. Desultor's root
   `README.md` explains the starter and should not become the host project's
   main README.
5. Follow the post-import checklist in
   [Suggested first pass after import](#suggested-first-pass-after-import).

If you are mixing into an existing repository instead of starting fresh, use
the guided merge contract below rather than this bootstrap sequence.

## Importing into another repository

If you copy Desultor into a real project, treat this repository as a reference
implementation of the operating model, not as text to overwrite blindly.

The expected operator for this step is an AI harness such as Codex or Claude
Code. For a brand-new repository, use the bootstrap sequence above. For an
existing repository, this is a guided merge, not a dumb file copy.

The host project's root `README.md` should stay the source of truth for that
project's purpose, setup, and user-facing entry points. Desultor's root
`README.md` is about the starter itself.

For the high-level contract of fresh bootstrap, guided mix-in, and patch export,
see
[doc/spec/desultor/operation-modes-v0_1.md](doc/spec/desultor/operation-modes-v0_1.md).
For the still-open mechanics question, see
[doc/rfc/desultor/import-mix-in-and-patch-export-mechanics.md](doc/rfc/desultor/import-mix-in-and-patch-export-mechanics.md).

## Suggested first pass after import

At this point, the target project's own root `README.md` should already exist.

1. Write or rewrite the target project's own `doc/ARCHITECTURE.md`.
2. Write or rewrite the target project's own `doc/spec/intro.md`.
3. Keep `doc/*/desultor/` and `doc/desultor/` as a detachable starter-owned
   reference layer until you deliberately remove or replace it.
4. Keep or adapt the lifecycle rules in `doc/stories/README.md`.
5. Confirm whether the starting harness stays primary or whether you want an
   explicit early handoff to the counterpart harness.
6. Open the first active story instead of relying on chat residue.

## Repository map

- [AGENTS.md](AGENTS.md) - Codex-facing project rules
- [CLAUDE.md](CLAUDE.md) - Claude Code-facing project
  rules
- [doc/README.md](doc/README.md) - documentation map
- [doc/desultor/ARCHITECTURE.md](doc/desultor/ARCHITECTURE.md) -
  architecture of the starter itself
- [doc/spec/desultor/intro.md](doc/spec/desultor/intro.md) - starter
  intent and operating stance
- [doc/spec/desultor/project-lifecycle-v0_1.md](doc/spec/desultor/project-lifecycle-v0_1.md)
  - lifecycle contract
- [doc/spec/desultor/operation-modes-v0_1.md](doc/spec/desultor/operation-modes-v0_1.md)
  - bootstrap, mix-in, and patch-export contract
- [doc/spec/desultor/starter-doc-namespacing-v0_1.md](doc/spec/desultor/starter-doc-namespacing-v0_1.md)
  - separation contract for starter-owned docs
- [doc/kb/desultor/session-signature-contract-2026-04-15.md](doc/kb/desultor/session-signature-contract-2026-04-15.md)
  - authored-artifact provenance rules
- [doc/kb/desultor/cross-harness-codex-claude-workflow-2026-04-15.md](doc/kb/desultor/cross-harness-codex-claude-workflow-2026-04-15.md)
  - review vs handoff workflow
- [doc/stories/](doc/stories/) - lifecycle-tracked
  work
- [scripts/claude_sidecar.py](scripts/claude_sidecar.py)
  - repo-local Claude sidecar controller

## Tool prerequisites

The repo-local sidecar helper assumes:

- `python3`
- `claude`
- `tmux` for the optional observability windows

If those are absent, the documentation structure still works. Only the sidecar
tooling becomes unavailable.
