---
type: tool
path: "@root/tools/Site.pudu"
grammar: "[[grammar/pudu]]"
tags: [tool]
---

# Site

> @Tools.Site.Builder — assembles authored documentation, the specification, and the API contract

## Purpose

Assembles the authored `website/` project, the wiki specification and decisions, and the OpenAPI contract into `build/site`. It does not render or serve the site. `python3 tools/BuildDocs.py` performs assembly and rendering with a pinned renderer in an isolated build cache; `--serve` adds a local preview. Warnings are errors. The API remains local; only static documentation is published.

## Interface

### Signatures

The module exposes no names; it is an entry point run directly.

### Linkage

- **Requires:** nothing inside the fabric
- **Standard library:** `Std.Fs`, `Std.Io`, `Std.Result`
- **Consumed by:** the runner

## Referenced by

[[tools/_MOC]]
