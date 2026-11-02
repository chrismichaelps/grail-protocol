---
type: module
path: "@root/src/Services/Store.pudu"
layer: 5
grammar: "[[grammar/pudu]]"
tags: [module, services]
---

# Services.Store

> @Services.Store.Memory — every scope's state, changed one scope at a time under a lock

## Purpose

Every scope's state, changed one scope at a time under a lock.

## Interface

### Signatures

```pudu
export type Store = { lock: Sync.Mutex, scopes: Sync.Cell[Map[Str, Scope.State]] }
/// An empty store.
export fn create() -> Store { Store{lock: Sync.mutex(), scopes: Sync.cell(Map.empty())} }
/// A scope's state as it stands; a scope nobody has written to is empty.
export fn read(store: &Store, scopeId: Str) -> Result[Scope.State, Problem.Problem]
/// Applies a change to one scope atomically: the new state is kept only when the change succeeds.
export fn change[T](store: &Store, scopeId: Str, action: fn(Scope.State) -> Result[(T, Scope.State), Problem.Problem]) -> Result[T, Problem.Problem]
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Contract/Problems]] · [[src/Domain/Problem]] · [[src/Domain/Scope]]
- **Standard library:** `Std.Map`, `Std.Result`, `Std.Sync`
- **Consumed by:** [[src/Services/Bridge]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[src/Services/Runtime]]

<!-- authored -->
## Algorithm

The store is one cell holding every scope's state, guarded by one mutex. `change` reads the scope, runs a pure function on it, and keeps the result only when the function succeeds.

## Negative Logic

- ❌ Never hand a caller a reference into the cell; every change is a whole new scope value.

## Grill Log

- **Q:** One lock per scope? **A:** One lock for now. **Rationale:** the runtime offers one mutex primitive and admission is fast; the seam ([[seams/ScopeStore]]) allows a sharded or durable store later without touching any engine. **Rejected:** premature sharding.
<!-- /authored -->

## Referenced by

[[src/Services/_MOC]] · [[src/Services/Bridge]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[src/Services/Runtime]]
