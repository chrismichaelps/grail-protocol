---
type: tool
path: "@root/tools/Site/Pages.pudu"
grammar: "[[grammar/pudu]]"
tags: [tool]
---

# Site.Pages

> @Tools.Site.Pages — turns vault pages into site pages

## Purpose

Turns vault pages into site pages.

## Interface

### Signatures

```pudu
export fn published(text: Str, from: Str) -> Str
export fn withoutFrontMatter(text: Str) -> Str
export fn withoutBacklinks(text: Str) -> Str
export fn linked(text: Str, from: Str) -> Str
export fn rendered(body: Str, from: Str) -> Str
export fn titleOf(text: Str, fallback: Str) -> Str
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** the runner

## Referenced by

[[tools/Site/_MOC]]
