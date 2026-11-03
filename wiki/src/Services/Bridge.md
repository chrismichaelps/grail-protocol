---
type: module
path: "@root/src/Services/Bridge.pudu"
layer: 5
grammar: "[[grammar/pudu]]"
tags: [module, services]
---

# Services.Bridge

> @Services.Bridge.Carrier — carries one JSON-RPC message through a graph as an envelope

## Purpose

Carries one JSON-RPC message through a graph as an envelope.

## Interface

### Signatures

```pudu
/// Admits a JSON-RPC message from the token's participant to a tool participant; a response is linked to the request it answers.
export fn carry(runtime: &Runtime.Runtime, call: &Request.Call[Request.Bridging]) -> Result[Transfer.Receipt, Problem.Problem]
```

### Linkage

- **Requires:** [[src/Api/Bridge]] · [[src/Constants/Fabric]] · [[src/Constants/Rpc]] · [[src/Contract/Members]] · [[src/Contract/Vocabulary]] · [[src/Domain/Envelope]] · [[src/Domain/Lifecycle]] · [[src/Domain/Problem]] · [[src/Domain/Request]] · [[src/Domain/Scope]] · [[src/Domain/Transfer]] · [[src/Engine/Admission]] · [[src/Engine/Bridge]] · [[src/Engine/Codec/Envelope]] · [[src/Engine/Custody]] · [[src/Services/Fabric]] · [[src/Services/Runtime]] · [[src/Services/Store]] · [[src/Utils/JsonRead]]
- **Standard library:** `Std.Json`, `Std.Option`
- **Consumed by:** [[src/App/Handlers]]

## Referenced by

[[src/App/Handlers]] · [[src/Services/_MOC]]
