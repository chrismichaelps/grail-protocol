---
type: test
path: "@root/test/Engine/CompositionTest.pudu"
grammar: "[[grammar/pudu]]"
tags: [test]
---

# Engine.CompositionTest

## Purpose

Nested teams preserve dependency gates, graph-qualified producer identity, and the routing witness retained when a task enters a team. Unrelated internal work cannot supply enclosing-team evidence.

## Linkage

- **Requires:** [[src/Domain/Graph]] · [[src/Domain/Scope]] · [[src/Contract/Problems]] · [[src/Contract/Vocabulary]] · [[test/Support/Fixtures]] · [[test/Support/Runner]]
- **Standard library:** `Std.Json`, `Std.Map`, `Std.Result`, `Std.Test`

## Referenced by

[[test/Engine/_MOC]]
