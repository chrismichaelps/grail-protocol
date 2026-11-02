---
date: 2026-11-02
topic: reference-fabric
from_role: Forensic Guardian
to_role: Architect
status: OPEN
maturity: EXPLORING
tags: [handoff]
---

# Handoff — Reference fabric 0.1.0

## Done

- Specification in twelve chapters; [[decisions/ADR-0001-specification-review]] lists every change from the draft.
- Contract and its projection; HTTP and line bindings served from it.
- Engines for authority, admission, routing, gating, lifecycles, mutations, ledger, and delivery; every conformance check has a test.
- Gates: layers, spacing, contract projection, formatter, mutation testing.
- Token inspection, revocation, erasure, and waiting pulls; the attack and stress campaign ([[architecture/ATTACKS]]) and its fixes.

## Decided (do not re-litigate)

- Answers route back to the task's source and need no return edge.
- Cross-scope requests are unauthorized before any lookup.
- The contract is the only definition of the wire.

## Open / Remaining

- A durable adapter for [[seams/ScopeStore]].
- Push delivery as a minor version ([[decisions/ADR-0007-long-polling-and-bounds]]).
- Report the two standard-library defects upstream ([[grammar/pudu#Known compiler issues]]).
- A distributed flood test from many hosts ([[architecture/ATTACKS#Limits of this campaign]]).

## Exact next action

Architect: design the durable scope store adapter behind [[seams/ScopeStore]], replaying the ledger on start and verifying its links.

## Links

[[protocol/_MOC]] · [[architecture/_MOC]] · [[seams/ScopeStore]]
