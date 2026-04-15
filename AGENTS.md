# desultor - starter instructions

Desultor is a public-neutral starter for projects that need explicit
documentation, work tracking, and cross-harness discipline before a stronger
orchestrator exists.

## Defaults

- Default language for repository artifacts is English unless the target
  project explicitly overrides it.
- Keep public repositories free of operator-specific identity, preferences, or
  private context.
- Keep domain specifics out of shared organizational documents until they are
  actually part of the target project's stable contracts.

## Read First

- `README.md`
- `doc/README.md`
- `doc/desultor/ARCHITECTURE.md`
- `doc/spec/desultor/intro.md`
- `doc/spec/desultor/project-lifecycle-v0_1.md`
- `doc/stories/README.md`
- relevant notes in `doc/kb/desultor/`

## Operating Model

### Task assessment

- Assess feasibility before tool use.
- If an external resource is likely to require authentication and no authorized
  access is available, block instead of probing.
- Distinguish orchestration work from execution work.
- Use direct execution for bounded local inspection and small local changes.
- Use narrow delegation for multi-step evidence gathering or remote probing
  when the harness supports it.

### Evidence discipline

- Do not describe content you did not actually obtain.
- If retrieval was partial, garbled, or login-gated, say so plainly.
- Separate fully obtained content, partial retrieval, and failure to retrieve.

### Documentation discipline

- `doc/inbox/` holds untriaged incoming material.
- `doc/spec/` holds stable contracts.
- `doc/kb/` holds reusable findings and operational notes.
- `doc/rfc/` holds open design questions and broad seeds.
- `doc/stories/` holds multi-step work.
- `doc/scratch/` holds temporary exploration.
- starter-owned documentation should stay namespaced under `doc/*/desultor/`
  or `doc/desultor/` so it remains detachable after import into a host repo.
- material in `doc/inbox/` should be triaged into `spec/`, `kb/`, `rfc/`,
  `stories/`, or `scratch/` instead of accumulating there indefinitely.
- If semantics change, update documentation in the same pass.
- If work is larger than a small local edit, create or update a story.

### Story lifecycle

- Active stories require `plan.md`.
- Plan review comes before implementation.
- Implementation review comes before closure.
- External `review-external-*` from the counterpart harness comes before final
  closure.
- Backlog placeholders may start as `README.md` plus `STATUS.md`; the full
  authored trail begins when the story moves to `active/`.

### Cross-harness boundary

- A brand-new Desultor-shaped project may start in Codex or in Claude Code.
- If this harness performs the first substantive bootstrap/import pass, treat
  it as the primary harness until explicit handoff or external review says
  otherwise.
- External review and ownership handoff are different modes.
- If ownership switches between harnesses, write an explicit handoff artifact.
- Do not blur "review by another harness" with "continue implementation in
  another harness".

### Closure

- Durable outcomes belong in `spec/`, `kb/`, `rfc/`, or story artifacts, not
  only in chat history.
- If a reusable rule or workflow appears twice, write it down.
