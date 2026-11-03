---
type: specification
chapter: 3
tags: [protocol, specification]
---

# 3. Envelope

## 3.1 Shape

An envelope is a JSON object. Unknown top-level members MUST be refused unless their name starts with `x-` (see [[protocol/12-Evolution]]).

| Member | Type | Required | Meaning |
| --- | --- | --- | --- |
| `grail` | string | yes | Protocol version, `"1.0"` for this document. |
| `id` | identifier | yes | The transfer identifier. Unique in the scope. |
| `scope` | identifier | yes | The scope the envelope lives in. MUST equal the scope of the presented token. |
| `graph` | identifier | yes | The graph whose edges route it. |
| `source` | participant id | yes | The sender. MUST be the token's audience or a participant the token is delegated to act for. |
| `target` | selector | yes | Exactly one of `{"participant": id}`, `{"role": name}`, `{"ability": name}`. |
| `kind` | kind | yes | See 3.2. |
| `parents` | array of transfer ids | no | Causal parents. At most 64. Each MUST already be in the ledger of the same scope. |
| `schema` | string | no | A URI or name identifying the payload's type. At most 512 characters. |
| `payload` | any JSON | no | The content. Its encoded size MUST NOT exceed 1 048 576 bytes. An object whose only member is `$secret` is a secret reference ([[protocol/14-Custody]]). |
| `delivery` | object | no | `{"mode": "at-most-once" \| "at-least-once" \| "effectively-once", "key": string}`. Default mode `at-least-once`. `key` is REQUIRED for `effectively-once`. |
| `priority` | integer | no | 0 (lowest) to 9 (highest). Default 4. |
| `deadline` | integer | no | Milliseconds since the Unix epoch after which the envelope MUST NOT be delivered. |
| `clock` | object | no | The sender's hybrid logical clock `{"wall": int, "counter": int, "node": string}` (see 5.1). |
| `visibility` | string | no | `scope` (default), `graph`, or `recipients`. Narrows who may later read this envelope through provenance queries. |
| `encryption` | object | no | Present when `payload` is sealed end to end: `{"scheme": string, "recipients": [id]}`. The fabric routes sealed payloads without reading them. |

The fabric adds three members when it accepts an envelope. A sender MUST NOT set them, and the fabric MUST refuse an envelope that does.

| Member | Meaning |
| --- | --- |
| `sequence` | Position in the scope's ledger, starting at 1. |
| `digest` | `sha256:` followed by the lowercase hex SHA-256 of the envelope's canonical form (3.3). |
| `accepted` | Fabric time, milliseconds since the Unix epoch. |

## 3.2 Kinds

A kind is a dotted lowercase name. The kinds below are reserved and drive fabric behavior. Any other kind is carried as opaque content; extension kinds MUST start with `x-` (for example `x-acme.quote`).

| Kind | Meaning | Fabric behavior |
| --- | --- | --- |
| `task` | Asks the target to do work. | Subject to dependency gating. Opens a lifecycle. |
| `result` | The successful outcome of a task. | MUST name the task among its parents. Completes the task's lifecycle. |
| `error` | The failed outcome of a task. Payload is a problem document. | MUST name the task among its parents. Fails the task's lifecycle. |
| `progress` | Intermediate status of a task. | MUST name the task among its parents. Moves it to `working`. |
| `input.request` | The target needs more information before continuing. | MUST name the task among its parents. Moves it to `input-required`. |
| `cancel` | Asks that a task stop. | MUST name the task among its parents. Moves it to `canceled` if not final. |
| `thought` | A participant's reasoning made visible. | Recorded only. |
| `observation` | Something a participant perceived. | Recorded only. |
| `memory` | Information offered for retention. | Recorded only. |
| `tool.call` | An invocation of a named ability. | Opens a lifecycle, like `task`. |
| `tool.result` | The answer to a `tool.call`. | Completes it, like `result`. |
| `stream.open` | Opens a stream. | The envelope id becomes the stream id. |
| `stream.chunk` | One fragment of a stream. | MUST name the `stream.open` among its parents. |
| `stream.close` | Ends a stream. | MUST name the `stream.open` among its parents. Later chunks are refused. |
| `ability.advert` | A participant advertises abilities. | Recorded; fabrics MAY index it for discovery. |
| `graph.mutation` | A change to a graph, recorded for provenance. | Emitted by the fabric, never accepted from senders. |
| `handoff.export` | A participant's context sealed and sent to another fabric ([[protocol/13-Portability]]). | Emitted by the fabric, never accepted from senders. |
| `handoff.import` | A participant's context received from another fabric, delivered to that participant. | Emitted by the fabric, never accepted from senders. |
| `bridge.rpc` | A JSON-RPC message of a tool protocol. | See [[protocol/10-Bridge]]. |

## 3.3 Canonical form and digest

The canonical form of an envelope is the JSON text produced by:

1. removing the members `sequence`, `digest`, and `accepted`;
2. sorting the members of every object, at every depth, by key in ascending order of Unicode code points;
3. writing with no insignificant whitespace, strings escaped with the minimal JSON escapes, and integers in plain decimal without exponent or leading zeros.

Fractional numbers inside `payload` are written exactly as they were received. Protocol members never hold fractional numbers.

The digest is computed over the UTF-8 bytes of the canonical form. Two envelopes with equal digests are the same envelope.

## 3.4 Limits

| Limit | Value |
| --- | --- |
| Encoded envelope | 1 114 112 bytes |
| Encoded payload | 1 048 576 bytes |
| Parents | 64 |
| Identifier | 128 characters |
| Name (role, ability) | 64 characters |
| Schema reference | 512 characters |
| Handoff anchors | 64 |
| Handoff entries | 10 000 |
| Encoded handoff | 4 194 304 bytes |
| Secrets per scope | 256 |
| Secret value | 12 to 4 096 characters |
| Secret audience or senders | 64 |
| Secret fragment | 16 characters |
| Custody strikes before revocation | 3 |
| Handoff lifetime | 86 400 000 milliseconds |

A fabric MAY lower these limits and MUST advertise its own in the discovery document ([[protocol/08-Bindings#8.4 Discovery]]).

## Referenced by

[[protocol/_MOC]] · [[protocol/02-Model]] · [[protocol/04-Transfer]] · [[protocol/05-Causality]] · [[domain/Envelope]]
