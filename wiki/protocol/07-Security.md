---
type: specification
chapter: 7
tags: [protocol, specification, security]
---

# 7. Security

## 7.1 Threats in scope

- A principal reading, writing, or learning of the existence of another principal's scope.
- A participant acting beyond what it was granted, including through delegation.
- A replayed, altered, or forged envelope or token.
- A recipient flooded beyond its capacity.
- Silent rewriting of history after the fact.

Compromise of the fabric host itself is outside the threat model of this document; end-to-end payload encryption (7.6) limits what such a compromise reveals.

## 7.2 Scope isolation

The fabric derives one key per scope from a fabric secret, `scopeKey = HMAC-SHA-256(fabricSecret, "grail-scope:" + scope)`, and signs every token of that scope with it. A token signed for scope `A` therefore fails verification when presented for scope `B`, regardless of what it claims.

Every lookup the fabric performs is keyed by scope first. A token is always verified with the key of the scope the request names, so a token of another scope fails verification and the request is refused with `grail.unauthorized` before any lookup happens. That answer is the same whether the named scope exists or not, and the same whether the object inside it exists or not, so a request outside its own scope learns nothing about what is there. Inside its own scope, a token restricted to one graph receives `grail.forbidden` for every other graph. The protocol gives no way to enumerate scopes.

## 7.3 Capability tokens

A token is a JSON object, transported as its canonical form encoded with unpadded base64url, a `.`, and the signature encoded the same way.

| Member | Meaning |
| --- | --- |
| `id` | Token identifier, unique in the scope. |
| `scope` | The scope it grants over. |
| `graph` | Optional. When present the token is valid only for that graph. |
| `issuer` | Who issued it: `owner` for the scope owner, otherwise a participant id. |
| `audience` | The participant id the token is issued to, or `owner`. |
| `abilities` | The operations it allows (7.4). |
| `notBefore`, `expires` | Validity window, milliseconds since the Unix epoch. `expires` is REQUIRED. |
| `parent` | Optional. The id of the token it was delegated from, which MUST be supplied in `chain`. |
| `chain` | The encoded parent tokens, root first, when `parent` is present. |

The signature is `HMAC-SHA-256(scopeKey, canonical form without the signature)`. A fabric MAY additionally support asymmetric signatures; they are an extension.

## 7.4 Abilities

| Ability | Allows |
| --- | --- |
| `graph.read` | Reading a graph. |
| `graph.write` | Creating and mutating graphs. |
| `transfer.send` | Sending envelopes whose `source` is the token's audience. |
| `transfer.receive` | Pulling deliveries addressed to the token's audience. |
| `transfer.read` | Reading the status of transfers. |
| `ledger.read` | Reading traces and ledger ranges. |
| `ledger.erase` | Erasing payloads. |
| `token.delegate` | Issuing narrower tokens to other participants. |
| `*` | Every ability. Only tokens issued by `owner` may hold it. |

## 7.5 Delegation

A participant holding `token.delegate` may issue a token to another participant of the same scope. The fabric accepts a delegated token only when, for each adjacent pair in its chain (parent, child):

1. both verify under the same scope key and name the same scope;
2. the child's `issuer` equals the parent's `audience`;
3. the child's abilities are a subset of the parent's (with `*` covering everything);
4. if the parent names a graph, the child names the same graph;
5. the child's validity window lies inside the parent's;
6. the chain holds at most 8 tokens.

Revoking a token revokes every token delegated from it. A fabric MUST check revocation for every token in the chain. A participant may revoke the tokens it issued; the owner may revoke any token of the scope.

## 7.6 End-to-end encryption

A sender MAY seal the payload for its recipients and mark it with `encryption`. The fabric routes, stores, digests, and traces sealed envelopes like any other, but cannot read the payload. The protocol does not mandate a sealing scheme; the scheme name identifies one. Dependency gating and lifecycles depend only on envelope members, never on payloads, so they keep working on sealed traffic.

## 7.7 Resource bounds

A fabric bounds what one scope can consume: entries in its ledger, live delivery keys, and the ancestry it walks to gate one task. Deduplication keys older than the deduplication window are forgotten. A walk of ancestry that reaches its bound without finding a dependency's result refuses the task (`grail.dependency-unmet`): gating fails closed. Exhausted bounds answer `grail.limit-exceeded`.

Transfer ids beginning with `mutation:` are reserved for the records the fabric writes when a graph changes, and are refused from senders.

## 7.8 Replay

Every envelope id is unique in its scope, and the fabric refuses a second envelope with an existing id (`grail.duplicate`) unless it is an `effectively-once` retry with the same key and digest. Tokens expire. Clock skew is bounded (5.1).

## Referenced by

[[protocol/_MOC]] · [[architecture/SECURITY]] · [[domain/Capability]] · [[domain/Scope]]
