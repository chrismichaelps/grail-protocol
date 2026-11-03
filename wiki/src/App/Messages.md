---
type: module
path: "@root/src/App/Messages.pudu"
layer: 6
grammar: "[[grammar/pudu]]"
tags: [module, app]
---

# App.Messages

> @App.Messages.Vocabulary — every request the fabric answers, one kind per contract operation

## Purpose

Every request the fabric answers, one kind per contract operation.

## Interface

### Signatures

```pudu
export type Kinds = {
  createGraph: Kind.Kind[Request.Call[Request.Creation], Graph.Graph, Problem.Problem],
  readGraph: Kind.Kind[Request.Call[Str], Graph.Graph, Problem.Problem],
  mutateGraph: Kind.Kind[Request.Call[Request.Change], Graph.Graph, Problem.Problem],
  sendEnvelope: Kind.Kind[Request.Call[Request.Sending], Transfer.Receipt, Problem.Problem],
  readTransfer: Kind.Kind[Request.Call[Str], Transfer.View, Problem.Problem],
  traceTransfer: Kind.Kind[Request.Call[Str], Request.Traced, Problem.Problem],
  pullDeliveries: Kind.Kind[Request.Call[Request.Pulling], Transfer.Page, Problem.Problem],
  readChannel: Kind.Kind[Request.Call[Request.Pulling], Transfer.Page, Problem.Problem],
  readLedger: Kind.Kind[Request.Call[Request.Paging], Transfer.Page, Problem.Problem],
  delegateToken: Kind.Kind[Request.Call[Capability.Request], Request.Granted, Problem.Problem],
  bridgeRpc: Kind.Kind[Request.Call[Request.Bridging], Transfer.Receipt, Problem.Problem],
  inspectToken: Kind.Kind[Request.Call[()], (Capability.Token, Int), Problem.Problem],
  revokeToken: Kind.Kind[Request.Call[Str], Str, Problem.Problem],
  eraseTransfer: Kind.Kind[Request.Call[Str], Request.Erased, Problem.Problem],
  exportHandoff: Kind.Kind[Request.Call[Handoff.Asked], Handoff.Stored, Problem.Problem],
  importHandoff: Kind.Kind[Request.Call[Handoff.Arriving], Handoff.Receipt, Problem.Problem],
  readHandoff: Kind.Kind[Request.Call[Str], Handoff.Stored, Problem.Problem],
  verifyHandoff: Kind.Kind[Request.Call[Handoff.Presented], Handoff.Check, Problem.Problem],
  putSecret: Kind.Kind[Request.Call[Custody.Deposit], Custody.Held, Problem.Problem],
  deleteSecret: Kind.Kind[Request.Call[Str], Custody.Held, Problem.Problem],
  listSecrets: Kind.Kind[Request.Call[()], Array[Custody.Held], Problem.Problem]
}
/// Every kind, named after the contract operation it serves.
export fn kinds() -> Kinds
```

### Linkage

- **Requires:** [[src/Contract/Operations]] · [[src/Domain/Capability]] · [[src/Domain/Custody]] · [[src/Domain/Graph]] · [[src/Domain/Handoff]] · [[src/Domain/Problem]] · [[src/Domain/Request]] · [[src/Domain/Transfer]]
- **Packages:** `PuduLangMediator`
- **Consumed by:** [[src/App/Assembly]] · [[src/App/Handlers]] · [[src/App/Pipeline]] · [[src/App/Resilience]]

## Referenced by

[[src/App/Assembly]] · [[src/App/Handlers]] · [[src/App/Pipeline]] · [[src/App/Resilience]] · [[src/App/_MOC]]
