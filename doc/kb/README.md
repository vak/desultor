# kb/

`kb/` stores reusable findings and operational notes that are worth keeping
outside a single story.

If the repository is itself a reusable scaffold or starter, keep scaffold-owned
notes under a namespaced subtree such as `kb/desultor/` instead of mixing them
indistinguishably with host-project knowledge.

Typical contents:

- harness quirks;
- workflow notes;
- provenance rules;
- repeatable lessons;
- compact handoffs that should stay discoverable later.

KB notes are a good place for lightweight YAML frontmatter:

```yaml
---
kind: kb
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: stable | draft
verification: project-rule | local-evidence | external-data | mixed
tags: [tag1, tag2]
---
```

If a note becomes a stable contract rather than a reusable observation, move
the settled part into `doc/spec/` or `doc/spec/desultor/`, depending on whether
it belongs to the host project or to the starter layer.
