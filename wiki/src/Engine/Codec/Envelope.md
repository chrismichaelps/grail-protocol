---
type: module
path: "@root/src/Engine/Codec/Envelope.pudu"
layer: 3
grammar: "[[grammar/pudu]]"
tags: [module, engine]
---

# Engine.Codec.Envelope

> @Engine.Codec.Envelope — envelopes to and from JSON

## Purpose

Envelopes to and from JSON.

## Interface

### Signatures

```pudu
/// The envelope a body describes, or every way it departs from the contract.
export fn decode(body: &Json.Json) -> Result[Envelope.Envelope, Problem.Problem]
/// The body as stored, with the members the fabric adds on acceptance.
export fn stamped(body: &Json.Json, stamp: &Envelope.Stamp) -> Json.Json
/// A selector as JSON.
export fn selectorJson(selector: &Envelope.Selector) -> Json.Json
/// An address as JSON.
export fn addressJson(address: &Envelope.Address) -> Json.Json
```

### Linkage

- **Requires:** [[src/Constants/Details]] · [[src/Constants/Extras]] · [[src/Constants/Graphs]] · [[src/Contract/Limits]] · [[src/Contract/Members]] · [[src/Contract/Problems]] · [[src/Contract/Schemas]] · [[src/Contract/Vocabulary]] · [[src/Domain/Envelope]] · [[src/Domain/Problem]] · [[src/Engine/Codec/Shapes]] · [[src/Utils/JsonRead]]
- **Standard library:** `Std.Json`, `Std.Option`
- **Consumed by:** [[src/Engine/Codec/Views]] · [[src/Engine/Journal]] · [[src/Services/Bridge]] · [[src/Web/Handlers]] · [[test/Engine/AdmissionTest]] · [[test/Engine/CustodyTest]] · [[test/Engine/LedgerTest]] · [[test/Engine/ShapesTest]] · [[test/Support/Fixtures]]

## Referenced by

[[src/Engine/Codec/_MOC]] · [[src/Engine/Codec/Views]] · [[src/Engine/Journal]] · [[src/Services/Bridge]] · [[src/Web/Handlers]] · [[test/Engine/AdmissionTest]] · [[test/Engine/CustodyTest]] · [[test/Engine/LedgerTest]] · [[test/Engine/ShapesTest]] · [[test/Support/Fixtures]]
