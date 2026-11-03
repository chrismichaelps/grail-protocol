---
type: test
path: "@root/test/Agent/AdapterTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test]
---

# Agent.AdapterTest

> @Test.Agent.Adapter.Suite — a hosted model meets the participant's tools: the handshake, the catalog, refusals, payloads, and the prompt a runner writes

## Purpose

A hosted model meets the participant's tools: the handshake, the catalog, refusals, payloads, and the prompt a runner writes.

## Interface

### Signatures

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/Agent/Mcp]] · [[src/Agent/Runner]] · [[src/Agent/Session]] · [[src/Agent/Tools]] · [[src/Agent/Wire]] · [[src/Api/Peer]] · [[src/Contract/Vocabulary]] · [[src/Domain/Capability]] · [[src/Engine/Authority]] · [[src/Utils/JsonRead]]
- **Packages:** `PuduLangMcp`
- **Standard library:** `Std.Json`, `Std.List`, `Std.Option`, `Std.Result`, `Std.Sync`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Agent/_MOC]]
