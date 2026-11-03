---
type: module
path: "@root/src/Services/Fabric.pudu"
layer: 5
grammar: "[[grammar/pudu]]"
tags: [module, services]
---

# Services.Fabric

> @Services.Fabric.UseCases — every operation of the protocol over one scope at a time

## Purpose

Every operation of the protocol over one scope at a time.

Graph creation and mutation apply the custody exposure guard to the submitted change, graph name, and actor before journaling. Refused graph writes persist the existing tripwire strikes but never graph revisions or ledger entries.

Payload erasure requires `ledger.erase` and checks the stored envelope's graph against the token's graph restriction before changing state. An `owner` audience does not bypass a graph restriction. Refusal preserves the payload, erasure mark, digest, and ledger link.

Custody revelation receives the verified caller authority. A batch refused by custody commits neither delivery acknowledgment marks nor reveal counters; a delegated executor identity alone is insufficient when its issuer lacked custody authority.

## Interface

### Signatures

```pudu
/// Creates a graph and records its creation.
export fn createGraph(runtime: &Runtime.Runtime, call: &Request.Call[Request.Creation]) -> Result[Graph.Graph, Problem.Problem]
/// Reads a graph.
export fn readGraph(runtime: &Runtime.Runtime, call: &Request.Call[Str]) -> Result[Graph.Graph, Problem.Problem]
/// Applies a mutation and records it.
export fn mutateGraph(runtime: &Runtime.Runtime, call: &Request.Call[Request.Change]) -> Result[Graph.Graph, Problem.Problem]
/// Admits an envelope, or answers the original receipt of a repeated delivery key. Custody refuses an envelope that holds a secret's value and counts each reference it makes.
export fn send(runtime: &Runtime.Runtime, call: &Request.Call[Request.Sending]) -> Result[Transfer.Receipt, Problem.Problem]
/// Reads an envelope and where its lifecycle stands.
export fn readTransfer(runtime: &Runtime.Runtime, call: &Request.Call[Str]) -> Result[Transfer.View, Problem.Problem]
/// Reads the causal ancestry of an envelope.
export fn traceTransfer(runtime: &Runtime.Runtime, call: &Request.Call[Str]) -> Result[Request.Traced, Problem.Problem]
/// Reads deliveries for the participant the token acts for, acknowledging everything up to the cursor; with a wait, looks again until one arrives or the wait runs out. Secret references are revealed here and only here, for recipients in the secret's audience.
export fn pullDeliveries(runtime: &Runtime.Runtime, call: &Request.Call[Request.Pulling]) -> Result[Transfer.Page, Problem.Problem]
/// Reads a range of the ledger.
export fn readLedger(runtime: &Runtime.Runtime, call: &Request.Call[Request.Paging]) -> Result[Transfer.Page, Problem.Problem]
/// Issues a narrower token to another participant.
export fn delegateToken(runtime: &Runtime.Runtime, call: &Request.Call[Capability.Request]) -> Result[Request.Granted, Problem.Problem]
/// Describes the presented token and how deep in its delegation chain it sits.
export fn inspectToken(runtime: &Runtime.Runtime, call: &Request.Call[()]) -> Result[(Capability.Token, Int), Problem.Problem]
/// Revokes a token the caller issued, or any token when the caller is the owner; every token delegated from it falls with it.
export fn revokeToken(runtime: &Runtime.Runtime, call: &Request.Call[Str]) -> Result[Str, Problem.Problem]
/// Erases an envelope's payload; its digest and link stay so the chain still verifies.
export fn eraseTransfer(runtime: &Runtime.Runtime, call: &Request.Call[Str]) -> Result[Request.Erased, Problem.Problem]
/// The authority a call's token grants over the scope it names.
export fn authorized[T](state: &Scope.State, call: &Request.Call[T], secret: Str, now: Int) -> Result[Capability.Authority, Problem.Problem]
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Constants/Security]] · [[src/Constants/Server]] · [[src/Contract/Limits]] · [[src/Contract/Members]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Capability]] · [[src/Domain/Envelope]] · [[src/Domain/Graph]] · [[src/Domain/Ledger]] · [[src/Domain/Lifecycle]] · [[src/Domain/Mutation]] · [[src/Domain/Problem]] · [[src/Domain/Request]] · [[src/Domain/Scope]] · [[src/Domain/Transfer]] · [[src/Engine/Admission]] · [[src/Engine/Authority]] · [[src/Engine/Codec/Graph]] · [[src/Engine/Custody]] · [[src/Engine/Delivery]] · [[src/Engine/Erasure]] · [[src/Engine/Journal]] · [[src/Engine/Mutations]] · [[src/Services/Runtime]] · [[src/Services/Store]]
- **Standard library:** `Std.Concurrent`, `Std.Json`, `Std.Math`, `Std.Option`, `Std.Result`
- **Consumed by:** [[src/App/Handlers]] · [[src/Services/Bridge]] · [[src/Services/Custody]] · [[src/Services/Handoffs]]

## Referenced by

[[src/Services/_MOC]] · [[src/App/Handlers]] · [[src/Services/Bridge]] · [[src/Services/Custody]] · [[src/Services/Handoffs]]
