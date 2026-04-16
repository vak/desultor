# Archive topology for KB, issues, and stories

## Why this RFC exists

Desultor already has explicit archival structure for stories:

- `doc/stories/archived/`

But similar archival pressure will likely appear for:

- resolved or obsolete issue files in `doc/issues/`
- superseded or stale operational notes in `doc/kb/`

That raises a topology question:

- should archival stay layer-local;
- should it be consolidated under something like
  `doc/archived/{stories,kb,issues}/`;
- or should tracked history in git be treated as sufficient and explicit
  archive structure avoided?

## What is already clear

- stories benefit from an explicit archived state because current focus and
  historical trail should not live in the same bucket;
- some KB and issue artifacts will eventually become stale, superseded, or no
  longer operationally relevant while still being worth keeping;
- relying on git alone preserves history, but removes obvious in-tree signals
  about whether an artifact is current, superseded, or merely old.

## Candidate directions

### Option A: keep archival local to each layer

Examples:

- `doc/stories/archived/`
- `doc/kb/archived/`
- `doc/issues/archived/`

Pros:

- preserves each layer's local semantics;
- makes archived material discoverable near active material;
- minimizes disruption to the current story layout.

Cons:

- spreads `archived/` across the tree;
- may feel mechanically repetitive;
- creates more topology surface area to explain.

### Option B: centralize archival under `doc/archived/`

Example:

- `doc/archived/stories/`
- `doc/archived/kb/`
- `doc/archived/issues/`

Pros:

- keeps all non-current historical material in one obvious place;
- avoids sprinkling `archived/` subtrees everywhere;
- may simplify broad "current vs archived" scanning for humans and harnesses.

Cons:

- weakens the immediate semantic link between a layer and its archived history;
- would require reshaping the existing story topology;
- may complicate starter namespacing and import rules.

### Option C: rely on git history and avoid explicit archive topology

Pros:

- minimal in-tree complexity;
- no new rules or directory structure to maintain;
- avoids duplicate "active plus archived" layouts.

Cons:

- current-vs-historical state becomes less explicit in the repository tree;
- targeted search for superseded artifacts may become less obvious;
- git history is not always the right semantic signal for humans or AI harnesses
  trying to understand the present operating model quickly.

## What is still open

- whether KB and issue artifacts truly need explicit archival states, or should
  mostly remain in place with metadata such as `status: superseded`;
- whether stories should keep their current `doc/stories/{active,backlog,archived}/`
  lifecycle shape even if KB/issues move toward centralized archival;
- how starter-owned archived material should be namespaced if a central
  `doc/archived/` layer exists;
- whether RFC and spec material should ever use the same archive topology, or
  whether supersession inside their native layer is enough;
- what the promotion/demotion rules would be for moving something into archive.

## Current safe stance

Until this is decided:

- keep the current explicit story archive as-is;
- do not introduce `doc/kb/archived/`, `doc/issues/archived/`, or
  `doc/archived/` yet;
- treat git history as a fallback source of old state, but not as a fully
  equivalent replacement for explicit archive semantics;
- only archive by explicit design, not by ad hoc folder growth.
