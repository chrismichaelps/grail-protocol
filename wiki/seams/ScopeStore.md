---
type: seam
capacity: EXPLORATORY
capacity_score: 3
lifecycle: EXPLORATORY
drift_score: 0
drift_status: HEALTHY
production_adapters: 1
tags: [seam]
---

# ScopeStore (seam)

## Classification

EXPLORATORY: one production adapter, [[src/Services/Store]], which keeps every scope in memory under one lock. A durable adapter (a database, or an append-only file per scope) is the expected second adapter.

## Interface

`read(store, scopeId)` and `change(store, scopeId, fn(Scope.State) -> Result[(T, Scope.State), Problem])`. Every engine is pure over `Scope.State`, so an adapter only has to load a scope, run the function, and persist the result atomically.

## Promotion

Promote to CRITICAL when a durable adapter is written; the ledger's hash chain then doubles as the integrity check of what was persisted.

## Referenced by

[[seams/_MOC]] · [[src/Services/Store]]
