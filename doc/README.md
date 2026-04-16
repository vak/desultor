# doc/

`doc/README.md` is the navigation map for Desultor's documentation tree.

The canonical stable contract for the structure and semantics of `doc/` lives
in `doc/spec/desultor/doc-taxonomy-v0_1.md`.

```text
doc/
├── desultor/              Starter-owned docs kept separable from host docs
├── inbox/                 Intake bucket for untriaged incoming material
├── issues/                Explicit blocking and urgent problems
├── spec/                  Stable contracts and operating intent
├── kb/                    Reusable findings, operational notes, project memory
├── rfc/                   Open design questions and broad seeds
├── stories/               Lifecycle-tracked multi-step work
│   ├── active/
│   ├── backlog/
│   └── archived/
└── scratch/               Temporary notes and rough exploration
```

## Read this next

- `doc/spec/desultor/doc-taxonomy-v0_1.md` for the canonical `doc/` taxonomy
  contract
- `doc/spec/desultor/issues-and-incident-handling-v0_1.md` for blocking issues
  and incident handling
- `doc/spec/desultor/starter-doc-namespacing-v0_1.md` for starter-vs-host doc
  boundaries
- `doc/spec/desultor/project-lifecycle-v0_1.md` for story lifecycle rules
- `doc/spec/desultor/inbox-triage-and-parking-v0_1.md` for intake drain and
  backlog-as-parking

## Bucket map

- `desultor/`
  - starter-owned self-documentation outside the generic layer buckets
- `inbox/`
  - raw incoming material waiting to be triaged
- `issues/`
  - explicit blocking or urgent problems that may trigger immediate story work
- `spec/`
  - stable repository contracts
- `kb/`
  - reusable findings and operational notes
- `rfc/`
  - unresolved design questions and broad seeds
- `stories/`
  - lifecycle-tracked multi-step work
- `scratch/`
  - temporary exploration not yet durable enough for other buckets

## Reading stance

Layer README files under `doc/` are local guides for their bucket. The
canonical semantics live in the starter specs under `doc/spec/desultor/`.
