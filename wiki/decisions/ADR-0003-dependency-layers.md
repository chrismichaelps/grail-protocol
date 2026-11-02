---
type: adr
status: ACCEPTED
date: 2026-11-02
decision_risk: MEDIUM
tags: [adr, architecture]
---

# ADR-0003 — Thirteen layers, checked on every change

## Decision

Folders are ranked in the [[architecture/_MOC#Layers|layer table]]. [[tools/Layers]] refuses upward or sideways imports outside a row's allowed set, cycles of any size, effectful imports in pure layers, and packages outside the rows that may use them. The protocol applies the same discipline to its users: dependency edges and containment must stay acyclic.

## Consequences

- Engines are pure and tested without a server; services own the only mutable state.
- Interfaces (`Web/`, `Cli/`) cannot skip authorization, validation, or limits.

## Alternatives

- **Convention only.** Rejected: conventions drift silently.

## Referenced by

[[decisions/_MOC]] · [[architecture/LAYERS]]
