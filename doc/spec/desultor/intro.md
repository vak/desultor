# Desultor Intro

Desultor is a repository starter for teams that want a cleaner operating model
than ad hoc chat-driven project drift, but do not yet have a real orchestrator.

The starter assumes:

- one repository should carry durable project state;
- multiple AI harnesses may participate;
- review boundaries and authorship boundaries should be visible in files, not
  left implicit;
- temporary runtime state is useful, but it should not become the only source
  of truth.

It also assumes three practical operating modes:

- bootstrap a brand-new project directory;
- mix the scaffold into an existing repository through guided AI-assisted
  merging;
- export a reusable patch out of an already Desultor-shaped project.

This repository is not a product domain, research domain, or code framework.
Its job is organizational:

- separate stable contracts from findings;
- force multi-step work into lifecycle containers;
- make cross-harness review honest;
- keep the public scaffold free of personal or domain-specific residue.

Starter-owned reference material should remain namespaced under `doc/*/desultor/`
or `doc/desultor/` so it can be separated from host-project docs after import.

When imported into a target repository, Desultor should be adapted quickly:

- rewrite the target repo's own root README;
- author or rewrite target architecture and spec documents at non-namespaced
  host-project paths such as `doc/ARCHITECTURE.md` and `doc/spec/intro.md`;
- keep or remove `doc/*/desultor/` and `doc/desultor/` deliberately as a
  starter-owned reference layer instead of blurring them into host docs;
- keep the lifecycle rules only where they still help;
- delete starter content that becomes misleading.
