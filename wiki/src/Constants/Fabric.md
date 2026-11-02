---
type: module
path: "@root/src/Constants/Fabric.pudu"
layer: 0
grammar: "[[grammar/pudu]]"
tags: [module, constants]
---

# Constants.Fabric

> @Constants.Fabric.Identity — the reference fabric's name, release, and claims

## Purpose

The reference fabric's name, release, and claims.

## Interface

### Signatures

```pudu
/// The implementation name published in discovery.
export const NAME: Str = "grail-fabric"
/// The release this build is.
export const VERSION: Str = "0.1.2"
/// The name of the command-line executable.
export const EXECUTABLE: Str = "grail"
/// Protocol versions this fabric speaks, newest first.
export const PROTOCOLS: Array[Str] = ["1.0"]
/// The conformance profiles this fabric claims.
export const PROFILES: Array[Str] = ["core"]
/// The bindings this fabric offers.
export const BINDINGS: Array[Str] = ["http", "lines"]
/// Extensions this fabric supports.
export const EXTENSIONS: Array[Str] = []
/// The status the health operation reports.
export const ALIVE: Str = "alive"
/// The member naming the implementation in discovery.
export const NAME_MEMBER: Str = "name"
/// The member giving the implementation's version in discovery.
export const VERSION_MEMBER: Str = "version"
/// The member listing claimed profiles in discovery.
export const PROFILES_MEMBER: Str = "profiles"
/// The member giving the contract version in discovery.
export const CONTRACT_MEMBER: Str = "contract"
/// The name of the client a peer connection is configured under.
export const PEER_CLIENT: Str = "grail-peer"
/// Milliseconds a peer request may take.
export const PEER_TIMEOUT_MILLIS: Int = 30000
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/Api/Peer]] · [[src/App/Logging]] · [[src/Cli/Commands]] · [[src/Engine/Admission]] · [[src/Engine/Codec/Views]] · [[src/Engine/Journal]] · [[src/Main]] · [[src/Services/Bridge]] · [[src/Web/Caller]]

## Referenced by

[[src/Api/Peer]] · [[src/App/Logging]] · [[src/Cli/Commands]] · [[src/Constants/_MOC]] · [[src/Engine/Admission]] · [[src/Engine/Codec/Views]] · [[src/Engine/Journal]] · [[src/Main]] · [[src/Services/Bridge]] · [[src/Web/Caller]]
