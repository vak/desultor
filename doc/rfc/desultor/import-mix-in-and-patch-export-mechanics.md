# Import, mix-in, and patch-export mechanics

## Why this RFC exists

Desultor now has three intended repository-level modes:

1. bootstrap into an empty work directory;
2. guided mix-in into an existing repository;
3. reusable patch export from an existing Desultor-shaped project.

The modes themselves are clear enough. The exact technical choreography is not.

## What is already clear

- the operator is expected to be an AI harness, not a blind copy procedure;
- mode 2 must handle collisions honestly;
- mode 3 must export reusable organizational changes without leaking domain or
  private residue.

## What is still open

- should mix-in be expressed as curated file selection, structured merge
  prompts, generated patches, or all of the above;
- how much of the target repository should be read before the harness proposes
  a merge;
- how aggressively starter-owned docs should stay namespaced under
  `doc/*/desultor/` in imported repositories;
- what the clean export boundary is for a Desultor-shaped project that also
  contains domain-specific extensions;
- whether the export primitive should be a patch, a file bundle, or a narrative
  merge plan plus patch.

## Current safe stance

Until a stronger mechanism exists:

- use Desultor as a guided AI-mediated scaffold;
- treat mode 2 as merge work, not copy work;
- treat mode 3 as curated extraction, not repository cloning.
