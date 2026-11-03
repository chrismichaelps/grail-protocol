---
type: test
path: "@root/test/Security/ChannelTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test]
---

# Security.ChannelTest

> @Test.Security.Channel.Suite — through the HTTP binding, a channel's history is closed to non-members, held values stay in custody, and observers can watch but never act

## Purpose

Through the HTTP binding, a channel's history is closed to non-members, held values stay in custody, and observers can watch but never act.

## Interface

### Signatures

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/App/Assembly]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Utils/JsonRead]] · [[src/Web/Router]]
- **Standard library:** `Std.Http`, `Std.Http.Server.Reply`, `Std.Http.Server.Route`, `Std.Json`, `Std.List`, `Std.Map`, `Std.Option`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Security/_MOC]]
