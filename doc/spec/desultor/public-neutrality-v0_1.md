# Public Neutrality v0.1

## Purpose

Desultor is meant to be publishable and reusable. The starter therefore treats
public neutrality as a first-class contract.

## Contract

Starter-level documents should not carry:

- domain residue from the repository they were copied from;
- operator-specific identity;
- personal language preferences unless they are truly project requirements;
- private host paths, credentials, or machine-local assumptions;
- hidden "favorite workflow" claims framed as universal truth.

## Allowed content

The starter may contain:

- generic workflow guidance;
- harness-specific operational notes when they are clearly scoped;
- namespaced starter-owned docs such as `doc/*/desultor/`;
- example commands with placeholder paths;
- explicit statements about what must be rewritten after import.

## Rewrite rule after import

When Desultor is imported into a real project:

- keep the organizational structure if it helps;
- keep starter-owned `desultor` namespaces separable until you deliberately
  remove or replace them;
- rewrite any starter text that pretends to know the target project;
- keep the target repo's own README authoritative for that project.

## Failure mode

The starter fails this contract if a public reader can infer unrelated private
project semantics or operator-specific identity from repository scaffolding that
was supposed to be generic.
