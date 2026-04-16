# desultor

Desultor is a public-neutral starter for docs-first or mixed projects that are
being driven by multiple AI harnesses and need explicit operational discipline.

## Read first

- `README.md`
- `doc/README.md`
- `doc/desultor/ARCHITECTURE.md`
- `doc/spec/desultor/intro.md`
- `doc/spec/desultor/project-lifecycle-v0_1.md`
- `doc/stories/README.md`
- relevant `doc/kb/desultor/` notes

## Core rules

- Default repository language is English unless the target project says
  otherwise.
- Keep the starter public-neutral. Do not leak operator-specific identity,
  private preferences, or unrelated host details into repo artifacts.
- Treat `doc/inbox/`, `doc/spec/`, `doc/kb/`, `doc/rfc/`, `doc/stories/`, and
  `doc/scratch/` as distinct layers with distinct purposes.
- Keep starter-owned documentation namespaced under `doc/*/desultor/` or
  `doc/desultor/` so it can be separated from host-project documentation after
  import.
- Do not let `doc/inbox/` become a shadow archive; triage useful material into
  the proper durable layer.
- If the change is larger than a small local edit, use or update a story.
- Active stories require the full trail:
  - `plan.md`
  - `review-plan-*`
  - for serious stories: `review-external-plan-*`
  - implementation pass
  - `review-implementation-*`
  - external `review-external-*`
- Backlog placeholders may exist with `README.md` and `STATUS.md` only until
  they are promoted to active work.
- A brand-new Desultor-shaped project may start in Claude Code or in Codex.
- If Claude Code performs the first substantive bootstrap/import pass, it is
  the primary harness until explicit handoff or external review says
  otherwise.
- If authorship or ownership moves across harnesses, create an explicit
  handoff note instead of relying on chat residue.
- Authored artifacts should carry session-signature frontmatter as defined in
  `doc/kb/desultor/session-signature-contract-2026-04-15.md`.

## Tooling

The repo includes `scripts/claude_sidecar.py` as a minimal repo-local control
plane for Claude Code sidecar sessions. Use it when a persistent Claude review
or side session is useful, but keep the repository state itself as the source
of truth.
