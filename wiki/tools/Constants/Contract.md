---
type: tool
path: "@root/tools/Constants/Contract.pudu"
grammar: "[[grammar/pudu]]"
tags: [tool]
---

# Constants.Contract

> @Tools.Constants.Contract — where the contract lives and how it is projected

## Purpose

Where the contract lives and how it is projected.

## Interface

### Signatures

```pudu
/// The contract every binding and vocabulary is read from.
export const SCHEMA_PATH: Str = "schema/grail.openapi.json"
/// The folder the projected modules are written to.
export const OUTPUT_DIRECTORY: Str = "src/Contract"
/// The module path prefix of the projected modules.
export const MODULE_PREFIX: Str = "Contract."
/// How a projected file names its source and its generator.
export const PROVENANCE: Str = "projected from schema/grail.openapi.json by tools/Contract.pudu; edit the schema, not this file"
/// The HTTP methods an operation may use, in the order they are read.
export const METHODS: Array[Str] = ["get", "put", "post", "patch", "delete"]
/// Each enumeration schema: its name, the prefix of each value's constant, and the name of the collection.
export const ENUMERATIONS: Array[(Str, Str, Str)]
/// The prefix every problem code carries in the contract.
export const PROBLEM_CODE_PREFIX: Str = "grail."
/// The prefix of a component reference.
export const REFERENCE_PREFIX: Str = "#/components/"
/// The component group a parameter reference points into.
export const PARAMETER_GROUP: Str = "parameters/"
/// What the check mode prints when a projection is stale.
export const STALE: Str = "stale: "
/// What the check mode prints when a projection is missing.
export const MISSING: Str = "missing: "
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** the runner

## Referenced by

[[tools/Constants/_MOC]]
