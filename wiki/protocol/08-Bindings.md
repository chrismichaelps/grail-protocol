---
type: specification
chapter: 8
tags: [protocol, specification]
---

# 8. Bindings

A binding maps the protocol's operations onto a transport. Each operation has a stable identifier, its `operationId` in [[schema/grail.openapi|the contract]]. Every binding carries the same operations with the same request and response bodies, so a fabric that implements one binding implements the others by changing only framing.

## 8.1 Operations

| Operation | Ability | Summary |
| --- | --- | --- |
| `discover` | none | The discovery document (8.4). |
| `describeContract` | none | The contract itself. |
| `checkHealth` | none | Liveness of the fabric. |
| `createGraph` | `graph.write` | Creates a graph. |
| `readGraph` | `graph.read` | Reads a graph at its current revision. |
| `mutateGraph` | `graph.write` | Applies a mutation (6.2). |
| `sendEnvelope` | `transfer.send` | Submits an envelope. |
| `readTransfer` | `transfer.read` | Reads an envelope and its lifecycle. |
| `traceTransfer` | `ledger.read` | Reads the causal ancestry (5.5). |
| `pullDeliveries` | `transfer.receive` | Reads deliveries for a participant after a cursor. |
| `readLedger` | `ledger.read` | Reads a range of ledger entries with their links. |
| `delegateToken` | `token.delegate` | Issues a narrower token (7.5). |
| `inspectToken` | none | Describes the presented token: its scope, graph, audience, abilities, window, and depth. |
| `revokeToken` | `token.delegate` | Revokes a token the caller issued, and with it every token delegated from it (7.5). The owner may revoke any token. |
| `eraseTransfer` | `ledger.erase` | Erases an envelope's payload, keeping its digest and link (5.6). |
| `bridgeRpc` | `transfer.send` | Carries one JSON-RPC message through a graph (10). |
| `exportHandoff` | `handoff.export` | Seals a participant's context into a portable handoff (13.1). |
| `importHandoff` | `handoff.import` | Admits a handoff from another fabric (13.4). |
| `readHandoff` | `ledger.read` | Reads a handoff the scope exported or imported. |
| `verifyHandoff` | none | Says whether this fabric sealed a handoff (13.3). |
| `putSecret` | `secret.manage` | Gives a secret to custody or rotates it (14.2). |
| `deleteSecret` | `secret.manage` | Destroys a secret in custody (14.2). |
| `listSecrets` | `graph.read` | Lists secret names and policies, never values (14.2). |

## 8.2 HTTP binding

- Requests and responses use `application/json`; problems use `application/problem+json`.
- The token travels as `Authorization: Bearer <token>`.
- A client SHOULD send `Grail-Version: 1.1`. A fabric that does not support the requested version answers `grail.unsupported-version` with the versions it supports.
- Paths, methods, parameters, bodies, and status codes are exactly those in the contract.
- Pulling deliveries is cursor based: `after` is the last ledger sequence the recipient has processed. Passing a cursor acknowledges every delivery up to it, which is how `at-least-once` delivery learns that redelivery can stop. `limit` bounds the page and defaults to 100, at most 1000. `wait` (milliseconds, at most 30 000) holds the request open until a delivery arrives or the time runs out, so a participant behind a firewall or on a laptop receives work as it happens without the fabric ever calling it.

## 8.3 Line binding

For local participants started as child processes, the line binding carries one JSON object per line on standard input and output:

```json
{"operation": "sendEnvelope", "token": "…", "params": {"scope": "s"}, "body": {…}}
```

The answer is one line: `{"status": 202, "body": {…}}`, or `{"status": 4xx, "problem": {…}}`. `params` holds the path and query parameters of the HTTP binding by name. Because both bindings are read from the same contract, an operation added to the contract appears in both without further specification.

## 8.4 Discovery

`GET /.well-known/grail` returns:

| Member | Meaning |
| --- | --- |
| `grail` | Supported protocol versions, newest first. |
| `fabric` | Name and version of the implementation. |
| `bindings` | The bindings offered, with their base addresses. |
| `limits` | The limits of [[protocol/03-Envelope#3.4 Limits]] and [[protocol/06-Graphs#6.4 Limits]] as this fabric enforces them. |
| `kinds` | The reserved kinds it understands. |
| `abilities` | The abilities it recognizes. |
| `extensions` | Extension names it supports. |

Discovery reveals nothing about any scope.

## Referenced by

[[protocol/_MOC]] · [[protocol/10-Bridge]] · [[schema/grail.openapi]] · [[architecture/CONTRACT]]
