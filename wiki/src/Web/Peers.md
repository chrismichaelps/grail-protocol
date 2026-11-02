---
type: module
path: "@root/src/Web/Peers.pudu"
layer: 7
grammar: "[[grammar/pudu]]"
tags: [module, web]
---

# Web.Peers

> @Web.Peers.Identity — names a peer by its host, so a new connection is not a new peer

## Purpose

Names a peer by its host, so a new connection is not a new peer.

## Interface

### Signatures

```pudu
/// A step that replaces the request's peer, written host and port, with its host alone; placed before rate limiting, it keeps a client from earning a fresh window by opening a new connection.
export fn byHost() -> Route.Middleware
/// The host of a peer written `host:port` or `[v6]:port`.
export fn hostOf(peer: Str) -> Str
```

### Linkage

- **Requires:** [[src/Constants/Text]]
- **Standard library:** `Std.Http.Server.Route`
- **Consumed by:** [[src/Web/Router]] · [[test/Security/AttackTest]]

## Referenced by

[[src/Web/Router]] · [[src/Web/_MOC]] · [[test/Security/AttackTest]]
