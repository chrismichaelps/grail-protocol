---
type: module
path: "@root/src/Api/Peer.pudu"
layer: 4
grammar: "[[grammar/pudu]]"
tags: [module, api]
---

# Api.Peer

> @Api.Peer.Client — calls a remote fabric's operations through a resilient HTTP client

## Purpose

Calls a remote fabric's operations through a resilient HTTP client.

## Interface

### Signatures

```pudu
export type Peer = { client: Client.Client }
export type Answer = { status: Int, body: Json.Json }
/// A peer at a base address, presenting a token, with retries, a circuit breaker, and timeouts. One attempt may last as long as the longest wait a pull or a channel read may ask for, so a long poll is never cut off and retried as if it had failed.
export fn connect(base: Str, token: Str) -> Result[Peer, Str]
/// One operation's answer: the method, the request target, and an optional JSON body.
export fn call(peer: &Peer, method: Str, target: Str, body: &Option[Json.Json]) -> Result[Answer, Str]
```

### Linkage

- **Requires:** [[src/Constants/Fabric]] · [[src/Constants/Security]] · [[src/Contract/Limits]] · [[src/Contract/Version]]
- **Packages:** `PuduLangHttpClient`, `PuduLangResilience`
- **Standard library:** `Std.Http`, `Std.Json`, `Std.Option`, `Std.Result`
- **Consumed by:** [[src/Agent/Session]] · [[src/Agent/Tools]] · [[src/Cli/Commands]]

## Referenced by

[[src/Api/_MOC]] · [[src/Cli/Commands]]
