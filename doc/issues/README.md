# issues/

`issues/` holds explicit blocking or urgent problems that need visible tracking
as issues rather than being left in chat, buried in backlog prose, or confused
with raw inbox material.

Use this bucket for things such as:

- regressions that block progress;
- urgent process failures;
- broken tooling or workflow incidents;
- budget or safety incidents that change how the harness should proceed;
- externally reported urgent problems that are already normalized into project
  language.

## Rule

`issues/` is not a raw intake bucket and not a full implementation trail.

- raw external material still belongs in `doc/inbox/` first;
- accepted multi-step remediation belongs in `doc/stories/`;
- unresolved design questions exposed by an issue belong in `doc/rfc/`;
- durable lessons and stable rules still belong in `doc/kb/` or `doc/spec/`.

Blocking or urgent issues should start or activate a story promptly, and may do
so directly in `doc/stories/active/` with elevated priority instead of waiting
through normal backlog sequencing.

Starter-owned issues should stay under `doc/issues/desultor/`.

## Hygiene

- do not let `issues/` become a second inbox;
- do not leave resolved durable meaning only in issue files;
- if an issue introduces an open design question, open an RFC explicitly;
- see `doc/spec/desultor/issues-and-incident-handling-v0_1.md` for the stable
  contract.
