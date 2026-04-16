# inbox/

`inbox/` is the intake bucket for raw incoming material that may matter but is
not yet normalized into the repository's proper artifact layers.

Typical inbox contents:

- incoming requests or questions that should not stay only in chat;
- dumped documents that still need triage;
- risks, caveats, or open concerns that are not yet classified;
- potentially useful links;
- images, screenshots, or other loose reference material;
- rough notes that arrived from outside the normal authored flow.

## Rule

`inbox/` is not a permanent archive.

Anything worth keeping should be triaged out of `inbox/` into the right
artifact class:

- `doc/rfc/` or `doc/rfc/desultor/` for open design questions;
- `doc/stories/` for actionable multi-step work;
- `doc/kb/` or `doc/kb/desultor/` for reusable operational knowledge;
- `doc/spec/` or `doc/spec/desultor/` for settled contracts;
- `doc/scratch/` for temporary exploration that still is not durable enough.

Once the durable meaning has been transferred elsewhere, the inbox copy should
normally be removed. Accepted but deferred work should be parked through
`doc/stories/backlog/`, not through a separate top-level `parked/` bucket.

If something turns out not to matter, it can be deleted instead of being
promoted.

## Hygiene

- keep filenames descriptive enough that later triage is possible;
- prefer small companion notes next to raw material when context would
  otherwise be lost;
- do not let `inbox/` become the repository's shadow knowledge base.
- see `doc/spec/desultor/inbox-triage-and-parking-v0_1.md` for the stable
  intake and parking contract.
