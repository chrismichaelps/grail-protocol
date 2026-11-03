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
| `readChannel` | `transfer.receive` | Reads a channel's posts after a cursor without acknowledging anything (15.3). |
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
- A client SHOULD send `Grail-Version: 1.2`. A fabric that does not support the requested version answers `grail.unsupported-version` with the versions it supports.
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

## 8.5 Browsers

A fabric MAY let pages on listed origins call it. For such an origin it answers a preflight request (`OPTIONS` with `Access-Control-Request-Method`) with `204` and the methods and headers the binding uses, including `Authorization` and `Grail-Version`, and it MAY add `Access-Control-Allow-Private-Network: true` so a public page can reach a fabric on the visitor's own machine. Requests from any other origin receive no permission. Tokens travel only in `Authorization`, never in cookies or URLs, so allowing an origin grants it nothing by itself.

## 8.6 Attaching hosted agents

A participant run by software that was not written for Grail, such as a coding agent, attaches through an adapter that holds its token and exposes the operations it needs. Adapters SHOULD read the fabric's base address from `GRAIL_FABRIC` and the token from the file named by `GRAIL_TOKEN_FILE`, falling back to `GRAIL_TOKEN`, so the same configuration attaches any agent to any fabric. An adapter MUST NOT place the token in anything the agent's model reads. An adapter that supervises an agent per task SHOULD name the task as the first parent of everything the agent sends for it, and SHOULD name what the agent sent and read as parents of the answer, so the trace of an answer covers the work behind it.

## Referenced by

[[protocol/_MOC]] · [[protocol/10-Bridge]] · [[schema/grail.openapi]] · [[architecture/CONTRACT]]
