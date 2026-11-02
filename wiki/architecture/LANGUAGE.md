---
type: architecture
tags: [architecture, language]
---

# Language

| Term | Definition | Not |
| --- | --- | --- |
| Module | One source file with an interface and an implementation. | A folder. |
| Interface | Everything a caller must know: types, errors, ordering, effects. | Only the signature. |
| Depth | Behavior a caller gets for the interface it learns. | Size. |
| Seam | A boundary where an implementation can be replaced without editing callers. | Any function call. |
| Layer | A folder's rank in the dependency table. | Structural depth, which is measured. |
| Factory | A table that chooses behavior by name once. | A chain of `if` on names. |
| Projection | A module generated from the contract. | Code that may be edited. |
| Pure | Free of clock, network, files, randomness, and environment. | Free of allocation. |

Protocol terms are defined in [[domain/_MOC]].

## Referenced by

[[architecture/_MOC]]
