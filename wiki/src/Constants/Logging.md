---
type: module
path: "@root/src/Constants/Logging.pudu"
layer: 0
grammar: "[[grammar/pudu]]"
tags: [module, constants]
---

# Constants.Logging

> @Constants.Logging.Events — names and templates of the fabric's log events

## Purpose

Names and templates of the fabric's log events.

## Interface

### Signatures

```pudu
/// The property every event carries naming the application.
export const APPLICATION_PROPERTY: Str = "Application"
/// The source of the mediator's events.
export const MESSAGES_SOURCE: Str = "Grail.Messages"
/// A fault of the fabric rather than an answer to a caller.
export const FAULT: Str = "\{MessageName\} failed unexpectedly: \{Failure\}"
/// The server started.
export const LISTENING: Str = "listening on \{Url\}"
/// The server stopped.
export const STOPPED: Str = "stopped"
/// An envelope was accepted.
export const ACCEPTED: Str = "accepted \{Transfer\} at \{Sequence\} for \{Recipients\} recipient(s)"
/// A graph changed.
export const CHANGED: Str = "graph \{Graph\} is at revision \{Revision\}"
/// A token was delegated.
export const DELEGATED: Str = "delegated a token expiring at \{Expires\}"
/// A notification could not be delivered.
export const UNANNOUNCED: Str = "could not announce \{Event\}: \{Failure\}"
/// The name the logging notification handlers are registered under.
export const RECORDER: Str = "recorder"
/// The notification of an accepted envelope.
export const EVENT_ACCEPTED: Str = "envelope.accepted"
/// The notification of a changed graph.
export const EVENT_CHANGED: Str = "graph.changed"
/// The notification of a delegated token.
export const EVENT_DELEGATED: Str = "token.delegated"
/// A token was revoked.
export const REVOKED: Str = "revoked token \{Token\} and every token delegated from it"
/// A payload was erased.
export const ERASED: Str = "erased the payload of \{Transfer\} at \{Sequence\}"
/// The notification of a revoked token.
export const EVENT_REVOKED: Str = "token.revoked"
/// The notification of an erased payload.
export const EVENT_ERASED: Str = "transfer.erased"
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/App/Assembly]] · [[src/App/Events]] · [[src/App/Logging]] · [[src/App/Pipeline]] · [[src/Main]]

## Referenced by

[[src/App/Assembly]] · [[src/App/Events]] · [[src/App/Logging]] · [[src/App/Pipeline]] · [[src/Constants/_MOC]] · [[src/Main]]
