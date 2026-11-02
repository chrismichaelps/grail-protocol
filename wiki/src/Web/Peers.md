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

Names a peer by its host, so a new connection is not a new peer. With `GRAIL_CLIENT_IP_HEADER` configured, a nonempty header replaces the connection host. The proxy must overwrite that header and be the fabric's only ingress; otherwise callers can choose their own rate-limit windows. Missing, empty, and whitespace-only headers fall back to the connection host.

## Interface

### Signatures

```pudu
/// Names peers before rate limiting so new connections share a window. A configured header must be overwritten by a trusted proxy that is the fabric's only ingress.
export fn byHost(header: Str) -> Route.Middleware
/// Uses the connection host unless the configured proxy header carries a nonempty address.
export fn peerOf(request: &Route.Request, header: Str) -> Str
/// The host of a peer written `host:port` or `[v6]:port`.
export fn hostOf(peer: Str) -> Str
```

### Linkage

- **Requires:** [[src/Constants/Text]]
- **Standard library:** `Std.Http.Server.Route`, `Std.Option`
- **Consumed by:** [[src/Web/Router]] · [[test/Security/AttackTest]]

## Referenced by

[[src/Web/Router]] · [[src/Web/_MOC]] · [[test/Security/AttackTest]]
