# Drop Transport Filter And Harness-File Collision Policy

## Why this RFC exists

Desultor currently describes import and mix-in behavior in prose across
`README.md`, starter specs, and adoption notes. That is not a strong enough
contract for an AI harness that needs to decide what to carry into a host
project during:

1. tabula-rasa bootstrap;
2. guided mix-in into an existing repository;
3. patch export from an existing Desultor-shaped project.

The most dangerous collision class is not an ordinary documentation file but
the harness-control files `AGENTS.md` and `CLAUDE.md`, because a host project
may already have authoritative versions of them.

## Problem statement

We need a transport contract that answers three separate questions:

1. which paths are excluded from drop-in transport;
2. which paths require explicit merge rather than blind copy or blind skip;
3. whether the answer changes by mode (`bootstrap`, `mix-in`, `export`).

## Preliminary conclusion

A separate transport artifact is justified.

The strongest current candidate is no longer a simple ignore-style file but a
small transport manifest. It should not be treated as a clone of `.gitignore`,
because the transport problem has at least three semantics:

- `exclude` — do not carry this path into the host project;
- `merge-required` — do not silently overwrite or silently skip; inspect and
  merge;
- `mode-sensitive` — a path may be copied in bootstrap but excluded or merged
  in mix-in/export.

A minimal example shape would be:

```text
copy:    doc/                 # all modes
copy:    scripts/             # all modes
merge:   AGENTS.md            # bootstrap, mix-in, export
merge:   CLAUDE.md            # bootstrap, mix-in, export
exclude: README.md            # mix-in, export
exclude: doc/scratch/         # all modes
```

The exact syntax is still open. The important point is that the contract needs
first-class actions, not only path exclusion.

For tabula-rasa bootstrap into a genuinely new host project, the default
transport target should be a minimal host-oriented scaffold, not a full mirror
of Desultor's own self-docs and internal history.

## Open design options

### Option A: exclude-list file

Use a file analogous to `.gitignore` that lists paths or globs that must not be
transported.

Pros:

- simple and familiar;
- easy for a harness or script to consume;
- better than prose-only transport rules.

Risks:

- not expressive enough for `AGENTS.md` and `CLAUDE.md`;
- can blur mode-specific behavior unless the format grows sections or tags.

### Option B: allowlist core plus exclude overlay

Keep a small explicit transport core and optionally add an exclude file on top.

Pros:

- safer when Desultor wants a stable "usual import set";
- reduces accidental transport of new internal files.

Risks:

- easy to drift if new useful starter files are added and the allowlist is not
  updated;
- may be too rigid for the AI-mediated mix-in model.

### Option C: transport manifest with multiple actions

Use a Desultor-specific manifest rather than a pure ignore file.

Example action classes:

- `copy`
- `exclude`
- `merge-required`
- `copy-on-bootstrap-only`

Pros:

- matches the real semantics better;
- makes `AGENTS.md` and `CLAUDE.md` first-class special cases.

Risks:

- more design work;
- less immediately familiar than a `.gitignore`-style file.

## Harness-file policy

`AGENTS.md` and `CLAUDE.md` should not be treated as ordinary drop-in files.

For `bootstrap` into a genuinely empty repository:

- copying them as-is is acceptable.

For `mix-in` into an existing repository:

- they should be `merge-required`;
- host-project instructions remain authoritative unless deliberately replaced;
- Desultor-specific additions should be inserted as clearly marked detachable
  sections rather than as silent overwrite.

For `export`:

- starter-specific sections should be extractable without exporting the host
  project's own harness instructions.

## Failure modes to avoid

1. Silent overwrite of `AGENTS.md` or `CLAUDE.md`.
2. Silent omission of useful starter files because a rigid allowlist drifted.
3. Prose-only transport rules interpreted differently by different harness
   sessions.
4. One rule set being applied blindly across `bootstrap`, `mix-in`, and
   `export`.
5. Transporting the transport-control file itself into host projects by
   default.

## Current recommendation

Do not settle this yet as a stable spec.

But the current recommendation has narrowed:

- do not use a pure `.gitignore`-style exclude file as the primary transport
  contract;
- prefer a small transport manifest with explicit action semantics and per-mode
  applicability;
- treat `AGENTS.md` and `CLAUDE.md` as mandatory `merge-required` paths outside
  ordinary copy/skip handling.

For `mix-in`, the safe rule is:

- host-project sections stay authoritative;
- Desultor additions are inserted as clearly marked detachable blocks;
- irreconcilable semantic conflicts are surfaced explicitly rather than
  auto-resolved by the harness.
