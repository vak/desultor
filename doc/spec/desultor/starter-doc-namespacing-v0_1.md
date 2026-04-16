# Starter Doc Namespacing v0.1

## Purpose

Desultor is a reusable starter. Its own documentation should therefore remain
separable from the documentation of a host project that imports it.

## Rule

Starter-owned documents should live under explicit `desultor` namespaces:

- `doc/desultor/` for starter self-docs outside the layer buckets;
- `doc/issues/desultor/` for starter issues;
- `doc/spec/desultor/` for starter contracts;
- `doc/kb/desultor/` for starter operational notes;
- `doc/rfc/desultor/` for starter design questions;
- `doc/stories/<state>/desultor/` for starter-owned work.

## Host-project boundary

When Desultor is imported into a host project:

- host-project docs should use the non-namespaced paths such as
  `doc/ARCHITECTURE.md`, `doc/spec/intro.md`, and host-owned KB/RFC/story/issue
  paths;
- the imported `desultor` namespaces should stay detachable until the host
  project deliberately removes or replaces them;
- a harness should not silently rewrite starter-owned namespaced docs into the
  host project's own source of truth.

## Why this matters

This naming discipline reduces three common failure modes:

1. starter docs pretending to be host-project docs;
2. mixed starter/project history that cannot be cleanly removed later;
3. import instructions that depend on blind overwrite rather than explicit
   adaptation.

## Allowed exceptions

Generic layer indexes such as `doc/README.md`, `doc/spec/README.md`,
`doc/kb/README.md`, and `doc/issues/README.md` may remain non-namespaced
because their job is to explain the shared taxonomy itself.
