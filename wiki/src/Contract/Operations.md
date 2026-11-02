---
type: module
path: "@root/src/Contract/Operations.pudu"
layer: 0
generated: true
grammar: "[[grammar/pudu]]"
tags: [module, contract]
---

# Contract.Operations

> @Contract.Operations.Generated — every operation of the bindings

## Purpose

Every operation of the bindings. Projected from the contract by [[tools/Contract]]; it is regenerated, never edited, and the contract check fails when it is stale.

## Interface

### Signatures

```pudu
export type Operation = { … }
/// `GET /.well-known/grail`.
export const DISCOVER: Str = "discover"
/// `GET /openapi.json`.
export const DESCRIBE_CONTRACT: Str = "describeContract"
/// `GET /v1/health`.
export const CHECK_HEALTH: Str = "checkHealth"
/// `GET /v1/scopes/{scope}/graphs/{graph}`.
export const READ_GRAPH: Str = "readGraph"
/// `PUT /v1/scopes/{scope}/graphs/{graph}`.
export const CREATE_GRAPH: Str = "createGraph"
/// `POST /v1/scopes/{scope}/graphs/{graph}/mutations`.
export const MUTATE_GRAPH: Str = "mutateGraph"
/// `POST /v1/scopes/{scope}/transfers`.
export const SEND_ENVELOPE: Str = "sendEnvelope"
/// `GET /v1/scopes/{scope}/transfers/{transfer}`.
export const READ_TRANSFER: Str = "readTransfer"
/// `GET /v1/scopes/{scope}/transfers/{transfer}/trace`.
export const TRACE_TRANSFER: Str = "traceTransfer"
/// `POST /v1/scopes/{scope}/transfers/{transfer}/erasure`.
export const ERASE_TRANSFER: Str = "eraseTransfer"
/// `GET /v1/scopes/{scope}/graphs/{graph}/participants/{participant}/deliveries`.
export const PULL_DELIVERIES: Str = "pullDeliveries"
/// `GET /v1/scopes/{scope}/ledger`.
export const READ_LEDGER: Str = "readLedger"
/// `POST /v1/scopes/{scope}/tokens`.
export const DELEGATE_TOKEN: Str = "delegateToken"
/// `GET /v1/scopes/{scope}/tokens/self`.
export const INSPECT_TOKEN: Str = "inspectToken"
/// `POST /v1/scopes/{scope}/tokens/{token}/revocation`.
export const REVOKE_TOKEN: Str = "revokeToken"
/// `POST /v1/scopes/{scope}/graphs/{graph}/bridge/{participant}`.
export const BRIDGE_RPC: Str = "bridgeRpc"
/// `POST /v1/scopes/{scope}/graphs/{graph}/participants/{participant}/handoffs`.
export const EXPORT_HANDOFF: Str = "exportHandoff"
/// `PUT /v1/scopes/{scope}/graphs/{graph}/participants/{participant}/handoffs/{handoff}`.
export const IMPORT_HANDOFF: Str = "importHandoff"
/// `GET /v1/scopes/{scope}/handoffs/{handoff}`.
export const READ_HANDOFF: Str = "readHandoff"
/// `POST /v1/scopes/{scope}/handoffs/{handoff}/verification`.
export const VERIFY_HANDOFF: Str = "verifyHandoff"
/// Every operation, in contract order.
export const ALL: Array[Operation]
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/App/Messages]] · [[src/Cli/Commands]] · [[src/Engine/Paths]] · [[src/Web/Description]] · [[src/Web/Handlers]] · [[src/Web/Router]] · [[test/Web/RouterTest]]

## Referenced by

[[src/Contract/_MOC]] · [[src/App/Messages]] · [[src/Cli/Commands]] · [[src/Engine/Paths]] · [[src/Web/Description]] · [[src/Web/Handlers]] · [[src/Web/Router]] · [[test/Web/RouterTest]]
