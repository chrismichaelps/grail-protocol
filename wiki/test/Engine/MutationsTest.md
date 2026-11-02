---
type: test
path: "@root/test/Engine/MutationsTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test]
---

# Engine.MutationsTest

> @Test.Engine.Mutations.Suite — graphs change atomically, by revision, and never into a cycle

## Purpose

Graphs change atomically, by revision, and never into a cycle.

The resource-bound checks accept exactly the participant, edge, and operation limits and refuse one more.

A cycle witness must exclude an acyclic path leading into the cycle; otherwise incorrect incoming-edge counts can report a nonexistent self-cycle.

## Interface

### Signatures

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** [[src/Contract/Limits]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[src/Domain/Graph]] · [[src/Domain/Mutation]] · [[src/Domain/Problem]] · [[src/Engine/Mutations]]
- **Standard library:** `Std.Json`, `Std.List`, `Std.Map`, `Std.Result`, `Std.Test`
- **Consumed by:** the runner

## Referenced by

[[test/Engine/_MOC]]
