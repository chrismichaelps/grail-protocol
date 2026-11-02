---
type: module
path: "@root/src/App/Commands.pudu"
layer: 6
grammar: "[[grammar/pudu]]"
tags: [module, app]
---

# App.Commands

> @App.Commands.Surface — every operation as one typed call, announced when it changes something

## Purpose

Every operation as one typed call, announced when it changes something.

## Interface

### Signatures

```pudu
/// Creates a graph.
export fn createGraph(app: &Assembly.App, call: Request.Call[Request.Creation]) -> Result[Graph.Graph, Problem.Problem]
/// Reads a graph.
export fn readGraph(app: &Assembly.App, call: Request.Call[Str]) -> Result[Graph.Graph, Problem.Problem] { Assembly.send(app, &app.kinds.readGraph, call) }
/// Mutates a graph.
export fn mutateGraph(app: &Assembly.App, call: Request.Call[Request.Change]) -> Result[Graph.Graph, Problem.Problem]
/// Sends an envelope.
export fn sendEnvelope(app: &Assembly.App, call: Request.Call[Request.Sending]) -> Result[Transfer.Receipt, Problem.Problem]
/// Reads a transfer.
export fn readTransfer(app: &Assembly.App, call: Request.Call[Str]) -> Result[Transfer.View, Problem.Problem] { Assembly.send(app, &app.kinds.readTransfer, call) }
/// Traces a transfer.
export fn traceTransfer(app: &Assembly.App, call: Request.Call[Str]) -> Result[Request.Traced, Problem.Problem] { Assembly.send(app, &app.kinds.traceTransfer, call) }
/// Pulls deliveries.
export fn pullDeliveries(app: &Assembly.App, call: Request.Call[Request.Pulling]) -> Result[Transfer.Page, Problem.Problem] { Assembly.send(app, &app.kinds.pullDeliveries, call) }
/// Reads the ledger.
export fn readLedger(app: &Assembly.App, call: Request.Call[Request.Paging]) -> Result[Transfer.Page, Problem.Problem] { Assembly.send(app, &app.kinds.readLedger, call) }
/// Delegates a token.
export fn delegateToken(app: &Assembly.App, call: Request.Call[Capability.Request]) -> Result[Request.Granted, Problem.Problem]
/// Bridges a JSON-RPC message.
export fn bridgeRpc(app: &Assembly.App, call: Request.Call[Request.Bridging]) -> Result[Transfer.Receipt, Problem.Problem]
/// Describes the presented token and its depth in its delegation chain.
export fn inspectToken(app: &Assembly.App, call: Request.Call[()]) -> Result[(Capability.Token, Int), Problem.Problem] { Assembly.send(app, &app.kinds.inspectToken, call) }
/// Revokes a token and everything delegated from it.
export fn revokeToken(app: &Assembly.App, call: Request.Call[Str]) -> Result[Str, Problem.Problem]
/// Erases an envelope's payload.
export fn eraseTransfer(app: &Assembly.App, call: Request.Call[Str]) -> Result[Request.Erased, Problem.Problem]
/// Exports a participant's context as a sealed handoff.
export fn exportHandoff(app: &Assembly.App, call: Request.Call[Handoff.Asked]) -> Result[Handoff.Stored, Problem.Problem]
/// Imports a handoff from another fabric.
export fn importHandoff(app: &Assembly.App, call: Request.Call[Handoff.Arriving]) -> Result[Handoff.Receipt, Problem.Problem]
/// Reads a handoff.
export fn readHandoff(app: &Assembly.App, call: Request.Call[Str]) -> Result[Handoff.Stored, Problem.Problem] { Assembly.send(app, &app.kinds.readHandoff, call) }
/// Verifies a handoff against the fabric that may have sealed it.
export fn verifyHandoff(app: &Assembly.App, call: Request.Call[Handoff.Presented]) -> Result[Handoff.Check, Problem.Problem] { Assembly.send(app, &app.kinds.verifyHandoff, call) }
```

### Linkage

- **Requires:** [[src/App/Assembly]] · [[src/Domain/Capability]] · [[src/Domain/Graph]] · [[src/Domain/Handoff]] · [[src/Domain/Problem]] · [[src/Domain/Request]] · [[src/Domain/Transfer]]
- **Consumed by:** [[src/Web/Handlers]]

<!-- authored -->
## Grill Log

- **Q:** Publish notifications from the services? **A:** From this surface, after the message succeeded. **Rationale:** services stay free of the mediator, and a failed listener never undoes an accepted change. **Rejected:** post-processors that would need the mediator inside itself.
<!-- /authored -->

## Referenced by

[[src/App/_MOC]] · [[src/Web/Handlers]]
