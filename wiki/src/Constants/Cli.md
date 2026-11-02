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
