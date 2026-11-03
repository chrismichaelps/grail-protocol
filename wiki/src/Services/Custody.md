---
type: module
path: "@root/src/Services/Custody.pudu"
layer: 5
grammar: "[[grammar/pudu]]"
tags: [module, services]
---

# Services.Custody

> @Services.Custody.UseCases — giving secrets to custody, listing what is held, and destroying it

## Purpose

Public metadata is checked against both the previously held values and the incoming sealed value before a deposit or rotation is committed. The guard covers descriptions, names, and policies, so neither a response nor a listing can echo the write-only value.

Giving secrets to custody, listing what is held, and destroying it.

## Interface

### Signatures

```pudu
/// Seals a value under a name as its next version. Every audience member and sender must be a participant of the graph, and every audience member a tool or service.
export fn putSecret(runtime: &Runtime.Runtime, call: &Request.Call[Custody.Deposit]) -> Result[Custody.Held, Problem.Problem]

/// Destroys a held secret; references to it stop resolving at once.
export fn deleteSecret(runtime: &Runtime.Runtime, call: &Request.Call[Str]) -> Result[Custody.Held, Problem.Problem]

/// The secrets of the graphs the token may read, in name order, without their values.
export fn listSecrets(runtime: &Runtime.Runtime, call: &Request.Call[()]) -> Result[Array[Custody.Held], Problem.Problem]
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Contract/Limits]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Custody]] · [[src/Domain/Graph]] · [[src/Domain/Problem]] · [[src/Domain/Request]] · [[src/Domain/Scope]] · [[src/Engine/Authority]] · [[src/Engine/Codec/Custody]] · [[src/Engine/Custody]] · [[src/Services/Fabric]] · [[src/Services/Runtime]] · [[src/Services/Store]]
- **Standard library:** `Std.Crypto`, `Std.List`, `Std.Map`, `Std.Option`, `Std.Result`
- **Consumed by:** [[src/App/Handlers]]

## Referenced by

[[src/Services/_MOC]] · [[src/App/Handlers]]
