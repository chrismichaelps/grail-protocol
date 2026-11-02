---
type: specification
chapter: 10
tags: [protocol, specification, bridge]
---

# 10. Tool protocol bridge

Tool servers that speak a JSON-RPC 2.0 tool protocol can join a graph without changing. The bridge wraps each JSON-RPC message in an envelope of kind `bridge.rpc`.

## 10.1 Mapping

| JSON-RPC message | Envelope |
| --- | --- |
| Request (`method`, `id`) | `bridge.rpc`, payload is the message unchanged, `schema` is `jsonrpc:2.0`. Opens a lifecycle like `tool.call`. |
| Notification (`method`, no `id`) | `bridge.rpc`, recorded only. |
| Result or error response | `bridge.rpc` naming the request's envelope as parent. Completes or fails its lifecycle. |

The JSON-RPC `id` is kept inside the payload and is never used as the transfer id: two clients may reuse the same JSON-RPC id, but transfer ids are unique per scope. The bridge maps responses back to requests through `parents`, not through the JSON-RPC id.

## 10.2 Handshake and version

The bridge forwards handshake messages like any other request. A bridge MAY answer a version negotiation itself when the tool server is not reachable, using the versions it has been configured to accept; it MUST NOT invent capabilities the tool server did not declare.

## 10.3 What the bridge does not do

- It does not translate tool-protocol permissions into abilities. Authority inside the graph comes from Grail tokens alone.
- It does not merge two protocols' error models. A JSON-RPC error stays a JSON-RPC error inside the payload; only the lifecycle moves to `failed`.

## Referenced by

[[protocol/_MOC]] · [[protocol/01-Overview]] · [[seams/RpcBridge]]
