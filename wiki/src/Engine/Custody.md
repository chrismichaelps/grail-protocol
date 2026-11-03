---
type: module
path: "@root/src/Engine/Custody.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Custody

> @Engine.Custody.Guard — seals secrets, keeps their values out of every envelope, and reveals them only in deliveries to their audience

## Purpose

Seals secrets, keeps their values out of every envelope, and reveals them only in deliveries to their audience.

## Interface

### Signatures

```pudu
/// A deposit sealed as the next version of its name. The value is bound to the scope, the name, and the version, so a sealed value moved anywhere else does not open.
export fn sealed(state: &Scope.State, sealing: &Custody.Sealing, secret: Str) -> Result[Custody.Held, Problem.Problem]

/// The value of a held secret, or `None` when it does not open under this fabric's key for this scope.
export fn valueOf(held: &Custody.Held, secret: Str, scopeId: Str) -> Option[Str]

/// Nothing when a body holds no held value; a body that holds one, as written or in a common encoding, is refused before anything else is checked, so a leak is always reported as a leak.
export fn screened(state: &Scope.State, body: &Json.Json, secret: Str) -> Result[(), Problem.Problem]

/// The scope after an admitted record's references are checked and counted: each must name a secret of the record's graph whose policy admits its sender, its kind, and every recipient.
export fn guarded(state: &Scope.State, record: &Ledger.Record, now: Int) -> Result[Scope.State, Problem.Problem]

/// Whether a JSON value holds the value of any secret the scope keeps, as written or in one of its disguises.
export fn exposes(state: &Scope.State, value: &Json.Json, secret: Str) -> Bool

/// The record as one recipient receives it: references to secrets whose audience holds the recipient become their values; everything else is left as stored.
export fn revealed(state: &Scope.State, record: &Ledger.Record, recipient: &Envelope.Address, secret: Str, now: Int) -> Ledger.Record

/// Every secret name a value references, each once, in the order they appear.
export fn references(value: &Json.Json) -> Array[Str]

/// The forms a value is looked for in: as written, escaped inside JSON text, in base64 of both alphabets, and in hex.
export fn disguises(value: Str) -> Array[Str]
```

### Linkage

- **Requires:** [[src/Constants/Custody]] · [[src/Constants/Details]] · [[src/Contract/Members]] · [[src/Contract/Problems]] · [[src/Domain/Custody]] · [[src/Domain/Envelope]] · [[src/Domain/Ledger]] · [[src/Domain/Problem]] · [[src/Domain/Scope]]
- **Standard library:** `Std.Bytes`, `Std.Crypto`, `Std.Json`, `Std.List`, `Std.Map`, `Std.Option`, `Std.Result`
- **Consumed by:** [[src/Engine/Handoff]] · [[src/Services/Bridge]] · [[src/Services/Custody]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[test/Engine/CustodyTest]]

## Referenced by

[[src/Engine/_MOC]] · [[src/Engine/Handoff]] · [[src/Services/Bridge]] · [[src/Services/Custody]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[test/Engine/CustodyTest]]
