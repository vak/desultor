# doc/

```text
doc/
├── desultor/              Starter-owned docs kept separable from host docs
├── inbox/                 Intake bucket for untriaged incoming material
├── spec/                   Stable contracts and operating intent
├── kb/                     Reusable findings, operational notes, project memory
├── rfc/                    Open design questions and broad seeds
├── stories/                Lifecycle-tracked multi-step work
│   ├── active/
│   ├── backlog/
│   └── archived/
└── scratch/                Temporary notes and rough exploration
```

## Principles

- durable knowledge is separate from work tracking;
- stable contracts are separate from empirical notes;
- raw incoming material should enter through `inbox/` and then be normalized
  into the right durable layer;
- open design debate lives in `rfc/`, not in scattered comments;
- multi-step work lives in `stories/`;
- parked work is expressed by backlog state, not by a separate top-level
  parking lot;
- reusable scaffold or starter docs should stay namespaced under `desultor/`
  subtrees instead of pretending to be host-project documents;
- external review artifacts stay inside the relevant story instead of being
  moved into a detached review silo.

## What goes where

- `desultor/`
  - starter-owned docs that should remain removable after import
  - architecture of the starter itself
  - starter-local indexes that do not belong in host-project layers
- `inbox/`
  - incoming requests, documents, screenshots, links, and loose references
  - risks and questions that are not yet classified
  - material waiting to be triaged into RFC, story, KB, spec, or scratch
- `spec/`
  - stable intent
  - lifecycle rules
  - semantic contracts
  - namespaced starter contracts can live in `spec/desultor/`
- `kb/`
  - reusable operational notes
  - findings worth keeping
  - incidents, quirks, and repeatable lessons
  - namespaced starter notes can live in `kb/desultor/`
- `rfc/`
  - unresolved questions
  - option comparisons
  - broad seeds that are not yet stable contracts
  - namespaced starter RFCs can live in `rfc/desultor/`
- `stories/`
  - containers for multi-step work
  - active stories carry the full authored trail
  - backlog stories may remain lightweight placeholders until activation
  - starter-owned work may be grouped under `stories/<state>/desultor/`
- `scratch/`
  - rough notes
  - quick exploration
  - temporary fragments that are not yet durable

## Recommended workflow

The baseline flow is:

`scratch -> rfc -> story -> spec -> code/tests`

Not every task touches every layer, but this ordering keeps exploratory work,
decisions, implementation, and stable contracts from collapsing into one
document.

Incoming external material may first land in `inbox/`, but `inbox/` is only an
intake stage. It should be drained into the proper layers instead of becoming a
second long-term knowledge base.

## Story rule

Once a story becomes active, the repository expects an explicit loop:

`plan -> review-plan -> implement -> review-implementation -> follow-up -> external review -> external follow-up`

Backlog placeholders are allowed to start smaller than that. Their job is to
mark accepted work, not to pretend that planning has already happened.

## Authored artifact provenance

Authored artifacts such as `plan.md`, `review-*.md`, and `notes-*.md` should
carry session-signature frontmatter. The canonical rule is in
`doc/kb/desultor/session-signature-contract-2026-04-15.md`.
