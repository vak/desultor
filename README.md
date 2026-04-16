# desultor

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/9f/Desultores%2C_Pietro_Santi_Bartoli%2C_Antiche_Lucerne_Sepolcrali%2C_1691%2C_image_24.gif" alt="Desultores, Pietro Santi Bartoli, 1691">
</p>

Desultor is a public-neutral starter for bootstrapping documented,
lifecycle-tracked projects with Codex and Claude Code.

Starter-owned documentation stays namespaced under `doc/*/desultor/` and
`doc/desultor/` so it can be detached cleanly from a host project later.

It works best as a two-harness loop: let one harness own the current writing
or implementation pass, and use the counterpart harness for external review.

## 30-second start

For a brand-new project, in an empty directory or repository opened in Codex
or Claude Code, paste:

   ```text
   Import Desultor according to github.com/vak/desultor/INSTALL.md
   ```

Then, in the same session, continue with:

   ```text
   Then help me build: ...
   ```

That is the normal human entrypoint. The exact bootstrap contract lives in
[INSTALL.md](INSTALL.md).

Recommended working mode: keep one primary harness for the current pass, and
bring in the other harness early as the external reviewer.

## What it gives you

- a `doc/` taxonomy that separates stable contracts, reusable findings, open
  design questions, blocking issues, and lifecycle-tracked work;
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

## Operating scope

Desultor is intentionally a stopgap. The goal is not to pretend that markdown
files and a few scripts are a real orchestration system. The goal is to make
project state, review boundaries, and cross-harness work less sloppy until
something better replaces them.

It is meant to support three repository-level operations:

1. bootstrap into a tabula-rasa work directory;
2. mix into an existing repository where collisions are expected and must be
   handled by an AI harness rather than by blind overwrite;
3. export a reusable patch from an existing Desultor-shaped project.

## Fresh-project boundary

For humans, the normal path is not to copy this repository by hand.

Use the short entrypoint above and treat [INSTALL.md](INSTALL.md) as the
canonical bootstrap contract.

For a fresh host project, the default expectation is a minimal scaffold, not a
mirror of this repository. Desultor's self-docs, internal history, and
starter-owned reference layers stay out unless you explicitly ask for them.

If you are mixing into an existing repository instead of starting fresh, use
the guided merge contract below rather than this bootstrap sequence.

## Importing into another repository

If you copy Desultor into a real project, treat this repository as a reference
implementation of the operating model, not as text to overwrite blindly.

The expected operator for this step is an AI harness such as Codex or Claude
Code. For a brand-new repository, use the bootstrap sequence above and adapt a
minimal host-project scaffold instead of mirroring this repository wholesale.
For an existing repository, this is a guided merge, not a dumb file copy.

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
3. If you deliberately imported any Desultor reference layer, keep
   `doc/*/desultor/` and `doc/desultor/` detachable until you deliberately
   remove or replace them.
4. Keep or adapt the lifecycle rules in `doc/stories/README.md`.
5. Confirm whether the starting harness stays primary or whether you want an
   explicit early handoff to the counterpart harness.
6. Open the first active story instead of relying on chat residue.

## Repository map

- [INSTALL.md](INSTALL.md) - canonical bootstrap contract for fresh projects
- [AGENTS.md](AGENTS.md) - Codex-facing project rules
- [CLAUDE.md](CLAUDE.md) - Claude Code-facing project
  rules
- [doc/README.md](doc/README.md) - documentation map
- [doc/desultor/ARCHITECTURE.md](doc/desultor/ARCHITECTURE.md) -
  architecture of the starter itself
- [doc/spec/desultor/doc-taxonomy-v0_1.md](doc/spec/desultor/doc-taxonomy-v0_1.md)
  - canonical structure and semantics of the `doc/` tree
- [doc/spec/desultor/intro.md](doc/spec/desultor/intro.md) - starter
  intent and operating stance
- [doc/spec/desultor/issues-and-incident-handling-v0_1.md](doc/spec/desultor/issues-and-incident-handling-v0_1.md)
  - blocking-issue and incident-handling contract
- [doc/spec/desultor/inbox-triage-and-parking-v0_1.md](doc/spec/desultor/inbox-triage-and-parking-v0_1.md)
  - intake-drain and backlog-as-parking contract
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
- [doc/issues/](doc/issues/) - blocking and urgent issue tracking
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
