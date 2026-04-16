# Issues and Incident Handling v0.1

## Purpose

Desultor needs an explicit place for blocking or urgent problems that are more
structured than inbox material but are not yet the full authored trail of a
story.

This spec defines the role of `doc/issues/` and how issues relate to stories,
RFCs, KB notes, and stable specs.

## Contract

- `doc/issues/` holds explicit normalized issues such as blocking incidents,
  urgent regressions, process failures, or tooling failures.
- `doc/issues/` is not a raw intake bucket. Raw external material still lands
  in `doc/inbox/` first.
- `doc/issues/` is not a substitute for story artifacts. Multi-step execution
  work still belongs in `doc/stories/`.
- starter-owned issues should live under `doc/issues/desultor/`.

## Story activation from issues

Blocking or urgent issues should start or activate a story promptly.

They may:

- start directly in `doc/stories/active/` instead of waiting through backlog;
- enter with elevated priority compared with normal accepted-but-not-urgent
  backlog work;
- remain linked to the originating issue so the problem statement does not get
  lost inside implementation detail.

## Relationship to other layers

- issue becomes multi-step remediation: start or activate a story;
- issue exposes unresolved design questions: open an RFC;
- issue yields a durable lesson: write or update a KB note;
- issue settles a stable rule: write or update a spec.

The issue file should not be the only durable home for those downstream
outcomes.

## Failure modes

Desultor drifts when:

- `doc/issues/` becomes a second inbox for raw material;
- `doc/issues/` becomes a graveyard of old problems with no linked story, RFC,
  KB note, or spec outcome;
- urgent incidents stay only in chat and never become explicit repository
  artifacts;
- issues are treated as implementation trails instead of problem statements and
  triage anchors.
