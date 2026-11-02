---
type: module
path: "@root/src/Constants/Rpc.pudu"
layer: 0
grammar: "[[grammar/pudu]]"
tags: [module, constants]
---

# Constants.Rpc

> @Constants.Rpc.Bridge — names the tool protocol bridge relies on

## Purpose

Names the tool protocol bridge relies on.

## Interface

### Signatures

```pudu
/// The schema reference of a bridged JSON-RPC message.
export const SCHEMA: Str = "jsonrpc:2.0"
/// The member that names a request's or notification's method.
export const METHOD: Str = "method"
/// The member that identifies a request and its response.
export const ID: Str = "id"
/// The member of a failed response.
export const ERROR: Str = "error"
/// The prefix of transfer ids the bridge gives the messages it carries.
export const TRANSFER_PREFIX: Str = "rpc-"
/// Random bytes in a bridged transfer id.
export const ID_BYTES: Int = 16
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/Engine/Bridge]] · [[src/Engine/Kinds]] · [[src/Services/Bridge]]

## Referenced by

[[src/Constants/_MOC]] · [[src/Engine/Bridge]] · [[src/Engine/Kinds]] · [[src/Services/Bridge]]
