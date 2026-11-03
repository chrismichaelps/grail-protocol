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

/// The refusal of a message that holds a held value, and the scope with a strike against the token that sent it. The owner's own tokens are never struck. The problem says how many strikes the token has.
export fn caught(state: &Scope.State, authority: &Capability.Authority) -> (Problem.Problem, Scope.State)

/// The scope after an admitted record's references are checked and counted: each must name a secret of the record's graph whose policy admits its sender, its kind, and every recipient.
export fn guarded(state: &Scope.State, record: &Ledger.Record, now: Int) -> Result[Scope.State, Problem.Problem]

/// Whether a JSON value holds the value of any secret the scope keeps, as written or in one of its disguises.
export fn exposes(state: &Scope.State, value: &Json.Json, secret: Str) -> Bool

/// The record as one recipient receives it: references to secrets whose audience holds the recipient become their values; everything else is left as stored.
export fn revealed(state: &Scope.State, record: &Ledger.Record, recipient: &Envelope.Address, secret: Str, now: Int) -> Ledger.Record

/// The records as one recipient receives them, and the scope with every reveal counted on the secret it revealed.
export fn delivered(state: &Scope.State, records: &Array[Ledger.Record], recipient: &Envelope.Address, secret: Str, now: Int) -> (Array[Ledger.Record], Scope.State)

/// Whether a participant of a graph is an executor custody may reveal a value to.
export fn executes(state: &Scope.State, graph: Str, participant: Str) -> Bool

/// The scope with one more strike against a token that tried to carry a held value, and the strikes it now has. At the contract's limit the token is revoked, and every token delegated from it falls with it.
export fn struck(state: &Scope.State, tokenId: Str) -> (Scope.State, Int)

/// Every secret name a value references, each once, in the order they appear.
export fn references(value: &Json.Json) -> Array[Str]
```

### Linkage

- **Requires:** [[src/Constants/Custody]] · [[src/Constants/Details]] · [[src/Constants/Extras]] · [[src/Constants/Security]] · [[src/Contract/Limits]] · [[src/Contract/Members]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Capability]] · [[src/Domain/Custody]] · [[src/Domain/Envelope]] · [[src/Domain/Graph]] · [[src/Domain/Ledger]] · [[src/Domain/Problem]] · [[src/Domain/Scope]] · [[src/Engine/Disguise]]
- **Standard library:** `Std.Bytes`, `Std.Crypto`, `Std.Json`, `Std.List`, `Std.Map`, `Std.Option`, `Std.Result`
- **Consumed by:** [[src/Engine/Handoff]] · [[src/Services/Bridge]] · [[src/Services/Custody]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[test/Engine/CustodyTest]]

## Referenced by

[[src/Engine/_MOC]] · [[src/Engine/Handoff]] · [[src/Services/Bridge]] · [[src/Services/Custody]] · [[src/Services/Fabric]] · [[src/Services/Handoffs]] · [[test/Engine/CustodyTest]]
