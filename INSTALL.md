# Install Desultor Into A New Project

This file is the canonical bootstrap contract for importing Desultor into a
brand-new host project through Codex or Claude Code.

It is not a package-manager install recipe. It is an AI-harness import
instruction.

## Human entrypoint

1. Create an empty directory or repository for your real project.
2. Open that directory in Codex or Claude Code.
3. Give this prompt:

   ```text
   Import Desultor according to github.com/vak/desultor/INSTALL.md
   ```

4. Verify that the scaffold landed. You should now see project-specific
   `AGENTS.md` / `CLAUDE.md`, a host-project `README.md`, and `doc/`.
5. In the same session, continue with a separate prompt:

   ```text
   Then help me build: ...
   ```

## Default bootstrap target

For a fresh host project, adapt a minimal scaffold:

- project-specific `AGENTS.md`
- project-specific `CLAUDE.md`
- the host project's own `README.md`
- the host project's own `doc/ARCHITECTURE.md`
- the host project's own `doc/spec/intro.md`
- the `doc/` layer skeleton and story workflow shape
- optional `scripts/claude_sidecar.py` only if repo-local sidecar tooling is
  actually wanted

## Do not import by default

Do not copy Desultor self-docs or internal history into a fresh host project
unless explicitly asked.

Default exclusions:

- `doc/desultor/`
- `doc/spec/desultor/`
- `doc/kb/desultor/`
- `doc/rfc/desultor/`
- `doc/stories/*/desultor/`
- `runtime/`

## Ownership rule

Either Codex or Claude Code may perform the initial bootstrap.

The harness that performs the first substantive bootstrap pass is the initial
primary harness until an explicit handoff or external review flow changes that.
