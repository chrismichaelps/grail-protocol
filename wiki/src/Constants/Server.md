---
type: module
path: "@root/src/Constants/Server.pudu"
layer: 0
grammar: "[[grammar/pudu]]"
tags: [module, constants]
---

# Constants.Server

> @Constants.Server.Capacity — bounds of the HTTP server

## Purpose

Bounds of the HTTP server.

## Interface

### Signatures

```pudu
/// The largest request head the server reads.
export const HEAD_BYTES_MAX: Int = 32768
/// Milliseconds a connection may take to send or receive.
export const SOCKET_DEADLINE_MILLIS: Int = 45000
/// Milliseconds in-flight requests have to finish at shutdown.
export const DRAIN_MILLIS: Int = 10000
/// Requests one peer may make per window.
export const RATE_REQUESTS: Int = 600
/// The rate window in seconds.
export const RATE_WINDOW_SECONDS: Int = 60
/// Requests served at once before the rest wait.
export const INFLIGHT_MAX: Int = 256
/// Milliseconds a handler may run.
export const HANDLER_TIMEOUT_MILLIS: Int = 45000
/// Seconds a client is told to wait after backpressure.
export const RETRY_AFTER_SECONDS: Int = 1
/// Messages handled at once by the mediator.
export const MESSAGE_PERMITS: Int = 256
/// Messages waiting for a permit before new ones are refused.
export const MESSAGE_QUEUE: Int = 1024
/// Milliseconds one message may take.
export const MESSAGE_TIMEOUT_MILLIS: Int = 10000
/// Milliseconds between looks at the ledger while a pull waits.
export const POLL_MILLIS: Int = 100
/// Milliseconds a waiting pull may take beyond its wait before the mediator stops it.
export const WAIT_GRACE_MILLIS: Int = 5000
/// Waiting pulls may hold one worker in this many.
export const WAITING_SHARE: Int = 2
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/App/Pipeline]] · [[src/App/Resilience]] · [[src/Main]] · [[src/Services/Fabric]] · [[src/Services/Runtime]] · [[src/Web/Router]]

## Referenced by

[[src/App/Pipeline]] · [[src/App/Resilience]] · [[src/Constants/_MOC]] · [[src/Main]] · [[src/Services/Fabric]] · [[src/Services/Runtime]] · [[src/Web/Router]]
