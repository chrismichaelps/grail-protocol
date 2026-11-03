---
type: moc
tags: [moc, architecture]
aliases: [Architecture]
maturity: EXPLORING
---

# Architecture

## Shape

The fabric is one executable. An HTTP request, or one line of the line binding, reaches [[src/Web/Router]], whose routes are built from the contract's operations and nothing else. A handler in [[src/Web/Handlers]] reads the body with the codecs in `Engine/Codec`, which check it against the contract's shapes, and calls one typed operation in [[src/App/Commands]]. The command sends a message through the mediator assembled in [[src/App/Assembly]]: every message is recorded, guarded by a concurrency limit and a deadline ([[src/App/Resilience]]), and validated by the rules in `Validation/` before its handler calls a use case in [[src/Services/Fabric]]. A use case changes one scope atomically through [[src/Services/Store]], running the pure engines: [[src/Engine/Authority]] for tokens, [[src/Engine/Admission]] for envelopes, [[src/Engine/Mutations]] for graphs, and [[src/Engine/Delivery]] for pages. After a change, the command announces a notification ([[src/App/Events]]).

## Layers

Dependencies point down the table only. A module may import from its own row's folders and the folders its row names, never from a row below it. The [[architecture/LAYERS|layer gate]] enforces this table and refuses cycles.

| # | Layer | Folder | Holds | Imports beyond the standard library |
| --- | --- | --- | --- | --- |
| 0 | Constants | `Constants/` | names, limits, messages, separators | — |
| 0 | Contract | `Contract/` | modules projected from the contract | — |
| 1 | Utils | `Utils/` | canonical JSON, typed JSON reads, pointers | Constants |
| 2 | Domain | `Domain/` | records and sums of the protocol; `Problem` | Constants, Contract, Utils |
| 3 | Engine | `Engine/` | pure engines: codecs, shapes, authority, admission, routing, gating, lifecycles, mutations, ledger, delivery | Domain and below |
| 3 | Config | `Config/` | settings bound from the environment | environment, validator, Constants |
| 3 | Validation | `Validation/` | rules beyond shape, with the validator package | validator, Domain and below |
| 4 | Api | `Api/` | the JSON-RPC inspection of the bridge; the peer client | mcp, httpclient, resilience, log, Engine and below |
| 5 | Services | `Services/` | the store, the runtime, the use cases, the bridge carrier | Api, Engine, Validation, Config and below |
| 6 | App | `App/` | messages, handlers, pipeline, resilience guards, notifications, commands | mediator, log, validator, resilience, Services and below |
| 7 | Web | `Web/` | router, handlers, responses, description gate, line binding | App, Engine, Config and below |
| 7 | Cli | `Cli/` | commands of the `grail` executable | App, Api, Web, Engine, Config and below |
| 8 | Entry | `Main` | process start | everything |

Layers 0 through 3 other than `Config/` are pure: they may not read the clock, the network, files, randomness, or the environment. `Web/` and `Cli/` never reach `Services/`: every action is a message, so authorization, validation, and limits cannot be skipped by an interface.

## Pages

- [[architecture/LANGUAGE]] — the vocabulary every page uses.
- [[architecture/LAYERS]] — the dependency layer gate.
- [[architecture/CONTRACT]] — how one schema file drives the bindings.
- [[architecture/SECURITY-REVIEW-2026-11-02]] — custody findings, corrections, and operating boundaries.
- [[architecture/SECURITY]] — threats and the control in each layer.
- [[architecture/ATTACKS]] — the attack and stress campaign, what broke, and how it was fixed.
- [[architecture/CODE_STYLE]] — spacing, constants, and comments.

## Governance dashboard

| Measure | Now |
| --- | --- |
| Modules | 95 in `src/`, 0 refused imports, 0 cycles |
| Deepest module | [[src/Main]] at structural depth 15 |
| Suites | 18 suites, 428 assertions; tool suites 29 assertions |
| Seams | [[seams/ScopeStore]] EXPLORATORY · [[seams/RpcBridge]] EXPLORATORY · [[seams/PeerTransport]] EXPLORATORY |
| Conformance | every check of [[protocol/11-Conformance#11.2 Required checks]], Portable and Custody included, has a test |

## Referenced by

[[00-INDEX]]
