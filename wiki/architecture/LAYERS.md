---
type: architecture
status: ACTIVE
tags: [architecture, dependencies, graph]
aliases: [Dependency layers, Layer gate]
---

# Dependency Layers

Actual imports define the dependency graph. [[tools/Layers]] reads every module under `src/`, takes the edges its `import` lines declare, and judges them against an explicit catalog ([[tools/Constants/Layers]]) rather than against the graph itself: a graph's own shape can never authorize an edge.

## Rules

1. **Catalogued.** Every module belongs to exactly one folder listed in the catalog. A module in an unlisted folder fails.
2. **Allowed folders.** A module may import only from the folders its row lists in the [[architecture/_MOC#Layers|layer table]], its own folder included.
3. **Allowed packages.** A package root (`PuduLangMediator`, `PuduLangResilience`, …) may be imported only where its row lists it.
4. **Purity.** `Constants`, `Contract`, `Utils`, `Domain`, `Engine`, and `Validation` may not import effectful standard modules, the clock included.
5. **Acyclic.** Any strongly connected component of more than one module fails, inside a folder too.
6. **Measured depth.** The report gives each module's structural depth in the condensed graph; depth is information, the layer is law.

The same rule governs the protocol itself: dependency edges of a graph and graph containment must be acyclic ([[protocol/06-Graphs#6.3 The acyclicity rule]]), and the fabric refuses a mutation that would close a cycle with the cycle in order. The code is held to the shape it asks of its users.

## Grill Log

- **Q:** Infer permission from imports that already exist? **A:** No; the catalog is explicit. **Rationale:** a new dependency must never authorize itself. **Rejected:** "whatever compiles is allowed".
- **Q:** Where does the generated contract sit? **A:** Layer 0 beside constants, importing nothing. **Rationale:** every layer may read the contract, and the contract may read nobody. **Rejected:** placing it in `Domain`, which would let it see records.
- **Q:** Is resilience an App concern? **A:** Yes for messages, Api for outbound calls. **Rationale:** the mediator's guards live where messages are composed; retries live where the network is. **Rejected:** retries inside services.

## Referenced by

[[architecture/_MOC]] · [[tools/Layers]] · [[tools/Layers/Catalog]] · [[tools/Layers/Graph]]
