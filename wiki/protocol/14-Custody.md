---
type: specification
chapter: 14
tags: [protocol, specification, security, custody]
---

# 14. Custody

Agents need keys: an API token, a database password, a signing key. The usual answer puts them in environment variables or in the prompt. Then a model that reads untrusted text can be talked into repeating them. A tool that logs its input writes them down. A message to another agent carries them further. Custody gives Grail a different answer: **participants use secrets by name, and the value exists only where the work is done.**

The fabric is on every path a message can take, so it can enforce this. It is the one place that sees every envelope, knows every recipient, and decides what each delivery contains.

## 14.1 Principles

1. **Reference, never value.** Participants write `{"$secret": "<name>"}` where a value would go. The reference is what is digested, stored, traced, read, and exported.
2. **Late binding.** The fabric replaces a reference with its value only in a delivery, at the moment the recipient pulls it, and only for recipients in the secret's audience. The audience is normally a tool executor, not a model.
3. **Least privilege, counted.** A secret belongs to one graph. Its policy names who receives it (`audience`), who may ask for it (`senders`), which kinds may carry it (`kinds`), how often (`uses`), and until when (`expires`).
4. **Tripwire.** No envelope, bridged message, or imported handoff may contain a held value, in plain text or in a common disguise.
5. **Write only.** A value is given to custody once and can never be read back through any operation.
6. **Never portable.** Values do not travel. A handoff names the secrets its context needs, and the receiving owner binds its own.

## 14.2 Deposits

`putSecret` (`secret.manage` for the graph) gives a value to custody under a name:

| Member | Meaning |
| --- | --- |
| `value` | `secretLengthMin` to `secretBytes` characters. Write-only. |
| `graph` | The graph whose envelopes may reference it. |
| `audience` | Participants of that graph whose deliveries receive the value. At least one. |
| `senders` | Participants that may reference it. Empty means any participant of the graph. |
| `kinds` | Kinds that may carry a reference. Empty means any. |
| `uses` | Admitted envelopes that may reference it before it is spent. Absent means unbounded. |
| `expires` | When references stop being admitted or revealed. |
| `description` | What the secret is for, so agents can choose it by purpose. |

Putting a name again rotates it: the version grows by one and later deliveries reveal the new value. A name belongs to one graph for its whole life. A scope holds at most `secrets` names. Every audience member and sender MUST be a participant of the graph, or the deposit is refused with `grail.not-found`.

The answer, and `listSecrets`, return the name, version, graph, policy, remaining uses, and creation time. Neither returns the value. `listSecrets` needs `graph.read` and lists only secrets of the graph a token is bound to, or of every graph for an unbound token. This is how agents learn which secrets exist and what they are for. `deleteSecret` destroys a secret. References to it stop resolving at once, including references already admitted and not yet delivered.

## 14.3 Admission

Custody checks every envelope before anything is appended:

1. Before any other check, so that a leak is always reported as a leak: if the envelope's body contains the value of any secret the scope holds, the envelope is refused with `grail.secret-exposed`. The disguises checked are the value as written, as escaped inside JSON text, in standard and URL-safe base64, and in hexadecimal.
2. After routing resolves the recipients, for each distinct reference in the payload, the named secret MUST belong to the envelope's graph (`grail.not-found` otherwise) and must not have expired (`grail.expired`). It MUST have uses left, the sender MUST be listed when `senders` is not empty, the kind MUST be listed when `kinds` is not empty, and every resolved recipient MUST be in the audience (each `grail.forbidden` otherwise).
3. Each reference consumes one use.

The same checks apply to messages carried by the bridge ([[protocol/10-Bridge]]). An imported handoff is refused with `grail.secret-exposed` when its document contains a held value ([[protocol/13-Portability]]).

The rule that every recipient must be in the audience is deliberately strict. A reference routed to a model must be refused, not quietly delivered unresolved, so the sender learns at once that it asked for the wrong thing.

## 14.4 Delivery

When a recipient pulls its deliveries, each reference whose secret still exists, has not expired, and lists that recipient in its audience is replaced by the value, as a JSON string. Nothing else ever reveals a value. That includes `readTransfer`, `traceTransfer`, `readLedger`, `readHandoff`, `exportHandoff`, discovery, and logs. Because the stored body keeps the reference, the ledger proves which secret, at which point in the conversation, was handed to which executor, without holding the secret itself.

## 14.5 Storage

The reference fabric seals each value with an authenticated cipher. The key is derived from the fabric secret and the scope, a fresh nonce is drawn for every version, and the scope, name, and version are bound as associated data. A sealed value moved to another scope, name, or version does not open. Values are opened only to reveal them in a delivery and to check admissions. They never appear in log lines; notifications name a secret and its version only.

## 14.6 Across fabrics

A handoff's `needs` lists the secret names its readable entries reference. The receiving owner deposits its own values under those names in the destination graph, with its own policy. The two fabrics never exchange a value, and a stolen handoff contains nothing to steal.

## 14.7 What custody does not promise

- **Values in the executor.** The audience receives the value and can misuse it. Keep audiences to executors you trust with the key, and keep models out of them. An executor MUST decide for itself where a key may be sent. It pins the destination host and accepts only plain paths or arguments from the request, because a sender that can choose the address, for example with `@other.host` in a path, can make the executor carry the key anywhere.
- **Disguises beyond those listed.** The tripwire catches the value verbatim and in the listed encodings, wherever they appear. It does not catch a value split across messages, re-encoded another way, or paraphrased. It narrows exfiltration through Grail; it does not replace keeping secrets out of reach of untrusted instructions.
- **Probing.** A sender can learn whether a guess equals a held value by being refused. Guessing a full value of at least `secretLengthMin` characters is as hard as guessing the secret itself. Short or low-entropy secrets do not belong in custody.
- **Persistence.** The reference store is in memory, so custody empties on restart, like the rest of the fabric.

## 14.8 Threats

| Threat | Control |
| --- | --- |
| A model repeats a key it was shown | Models are never shown keys; references resolve only for the audience. |
| Prompt injection asks an agent to post a key elsewhere | The agent never held the key, and the tripwire refuses any envelope that does. |
| An executor echoes a key in its result | `grail.secret-exposed`. |
| A reference routed to the wrong participant | Every recipient must be in the audience. |
| A compromised participant asks for a key it should not use | `senders`, `kinds`, and `uses`. |
| A key leaks through a trace, ledger read, or handoff | Only references are stored, traced, or exported. |
| A key outlives its purpose | `expires`, `uses`, rotation, and deletion. |
| A stored value is copied | It is sealed and bound to its scope, name, and version. |

## Referenced by

[[protocol/_MOC]] · [[protocol/07-Security]] · [[protocol/13-Portability]] · [[decisions/ADR-0010-custody]] · [[src/Engine/Custody]] · [[src/Services/Custody]]
