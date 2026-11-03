---
type: module
path: "@root/src/Constants/Cli.pudu"
layer: 0
grammar: "[[grammar/pudu]]"
tags: [module, constants]
---

# Constants.Cli

> @Constants.Cli.Commands — the commands and options of the executable

## Purpose

The commands and options of the executable.

## Interface

### Signatures

```pudu
/// Serves the HTTP binding until stopped.
export const SERVE: Str = "serve"
/// Serves the line binding over standard input and output.
export const LINES: Str = "lines"
/// Issues a scope owner's token.
export const TOKEN: Str = "token"
/// Calls an operation of a remote fabric.
export const CALL: Str = "call"
/// Carries a participant's context from one fabric to another.
export const HANDOFF: Str = "handoff"
/// Prints the contract.
export const CONTRACT: Str = "contract"
/// Prints the version.
export const VERSION: Str = "version"
/// Prints the usage.
export const HELP: Str = "help"
/// The scope a token is issued for.
export const SCOPE_OPTION: Str = "--scope"
/// The id of an issued token.
export const ID_OPTION: Str = "--id"
/// The audience of an issued token.
export const AUDIENCE_OPTION: Str = "--audience"
/// The abilities of an issued token, separated by commas.
export const ABILITIES_OPTION: Str = "--abilities"
/// The graph an issued token is restricted to.
export const GRAPH_OPTION: Str = "--graph"
/// Days an issued token lives.
export const DAYS_OPTION: Str = "--days"
/// The base address of a remote fabric.
export const FABRIC_OPTION: Str = "--fabric"
/// The token presented to a remote fabric.
export const TOKEN_OPTION: Str = "--token"
/// The parameters of a remote call, as a JSON object.
export const PARAMS_OPTION: Str = "--params"
/// The body of a remote call, as JSON.
export const BODY_OPTION: Str = "--body"
/// The fabric a handoff leaves.
export const FROM_OPTION: Str = "--from"
/// The token presented to the fabric a handoff leaves.
export const FROM_TOKEN_OPTION: Str = "--from-token"
/// The fabric a handoff arrives at.
export const TO_OPTION: Str = "--to"
/// The token presented to the fabric a handoff arrives at.
export const TO_TOKEN_OPTION: Str = "--to-token"
/// The participant whose context leaves.
export const PARTICIPANT_OPTION: Str = "--participant"
/// The scope a handoff arrives in.
export const TO_SCOPE_OPTION: Str = "--to-scope"
/// The graph a handoff arrives in.
export const TO_GRAPH_OPTION: Str = "--to-graph"
/// The participant a handoff arrives for.
export const TO_PARTICIPANT_OPTION: Str = "--to-participant"
/// The anchor transfers of a handoff, separated by commas.
export const TRANSFERS_OPTION: Str = "--transfers"
/// What a handoff refused at its origin's check prints.
export const NOT_ATTESTED: Str = "the origin fabric does not attest this handoff"
/// The member naming each step of a carried handoff.
export const STEP_MEMBER: Str = "step"
/// The member holding the answer of a step.
export const ANSWER_MEMBER: Str = "answer"
/// The member giving the status of a step.
export const STATUS_MEMBER: Str = "status"
/// The step that seals the context at its origin.
export const STEP_EXPORT: Str = "export"
/// The step that asks the origin whether it sealed the handoff.
export const STEP_VERIFY: Str = "verify"
/// The step that admits the handoff at its destination.
export const STEP_IMPORT: Str = "import"
/// What separates listed abilities.
export const LIST_SEPARATOR: Str = ","
/// Days a token lives when none are given.
export const DAYS_DEFAULT: Int = 30
/// Milliseconds in a day.
export const DAY_MILLIS: Int = 86400000
/// The default base address of a remote fabric.
export const FABRIC_DEFAULT: Str = "http://127.0.0.1:7420"
/// How to use the executable.
export const USAGE: Array[Str]
/// A command that needs an option it was not given.
export const MISSING_OPTION: Str = "missing option "
/// A command nobody knows.
export const UNKNOWN_COMMAND: Str = "unknown command "
/// A remote operation nobody knows.
export const UNKNOWN_OPERATION: Str = "the contract has no operation "
/// JSON that does not parse.
export const NOT_JSON: Str = " is not JSON"
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** [[src/Cli/Commands]] · [[src/Main]]

## Referenced by

[[src/Cli/Commands]] · [[src/Constants/_MOC]] · [[src/Main]]
