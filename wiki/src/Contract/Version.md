---
type: module
path: "@root/src/Contract/Version.pudu"
layer: 0
generated: true
grammar: "[[grammar/pudu]]"
tags: [module, contract]
---

# Contract.Version

> @Contract.Version.Generated — protocol version, media types, and headers

## Purpose

Protocol version, media types, and headers. Projected from the contract by [[tools/Contract]]; it is regenerated, never edited, and the contract check fails when it is stale.

## Interface

### Signatures

```pudu
/// The protocol version this contract describes.
export const PROTOCOL: Str = "1.1"
/// The version of the contract document.
export const CONTRACT: Str = "1.1.0"
/// The contract's title.
export const TITLE: Str = "Grail Protocol"
/// The media type of requests and answers.
export const MEDIA_TYPE: Str = "application/json"
/// The media type of problem documents.
export const PROBLEM_MEDIA_TYPE: Str = "application/problem+json"
/// The prefix of every problem type.
export const PROBLEM_PREFIX: Str = "urn:grail:problem:"
/// The `version` header.
export const HEADER_VERSION: Str = "Grail-Version"
/// The `authorization` header.
export const HEADER_AUTHORIZATION: Str = "Authorization"
/// The `retryAfter` header.
export const HEADER_RETRY_AFTER: Str = "Retry-After"
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/Api/Peer]] · [[src/Engine/Codec/Views]] · [[src/Web/Caller]] · [[src/Web/Description]] · [[src/Web/Lines]] · [[src/Web/Respond]]

## Referenced by

[[src/Api/Peer]] · [[src/Contract/_MOC]] · [[src/Engine/Codec/Views]] · [[src/Web/Caller]] · [[src/Web/Description]] · [[src/Web/Lines]] · [[src/Web/Respond]]
