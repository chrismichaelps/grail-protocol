---
type: domain
tags: [domain, portability]
aliases: [Handoff]
---

# Handoff

- **Definition:** A sealed document holding one participant's working context, its anchor transfers and their whole causal ancestry, carried from the fabric that exported it to a fabric that imports it.
- **Canonical name:** Handoff; its id is also the id of the ledger entry that records it in each scope it passes through.
- **Not:** A live connection between fabrics, a copy of the origin ledger, or a grant of authority. The receiving owner decides what the arriving participant may do. Also not the work-in-flight notes kept in `handoffs/` of this vault.
- **Example:** Handoff `move-1` leaves fabric `studio` from `demo/g/writer` carrying `t1`, `h1` (withheld), and `r1`, and arrives at fabric `desk` for `support/desk/assistant`.

## Referenced by

[[protocol/13-Portability]] · [[src/Domain/Handoff]] · [[domain/_MOC]]
