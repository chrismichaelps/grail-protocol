---
type: specification
chapter: 12
tags: [protocol, specification]
---

# 12. Versioning and extensions

## 12.1 Versions

The protocol version has the form `major.minor`. A minor version only adds: new optional members, new kinds, new operations, new problem codes. A major version may remove or change meaning. Envelopes carry their version in `grail`; HTTP requests carry it in `Grail-Version`. A fabric MUST refuse a major version it does not implement with `grail.unsupported-version`, and SHOULD accept any minor version of a major it implements, ignoring members it does not know only when their names start with `x-`.

Version 1.1 is the first minor version. It adds the operations, kinds, abilities, limits, and problem code of [[protocol/13-Portability]], and changes nothing that 1.0 defined. A 1.1 fabric accepts 1.0 envelopes and requests.

## 12.2 Extensions

- Extension kinds, members, abilities, and operations start with `x-` followed by an owner name and a dot: `x-acme.quote`.
- An extension MUST NOT change the meaning of a reserved member, kind, or ability.
- A fabric lists the extensions it supports in discovery. A participant MUST NOT rely on an extension the fabric does not list.

## 12.3 Changing the contract

The contract file is the single place a field, an enumeration value, an operation, a status code, or a problem code is defined. Every change to it is a protocol change and follows 12.1. The reference implementation regenerates its contract modules from that file and fails its checks when the generated code is stale (see [[architecture/CONTRACT]]).

## Referenced by

[[protocol/_MOC]] · [[protocol/03-Envelope]] · [[architecture/CONTRACT]]
