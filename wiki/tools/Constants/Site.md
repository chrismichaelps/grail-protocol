---
type: tool
path: "@root/tools/Constants/Site.pudu"
grammar: "[[grammar/pudu]]"
tags: [tool]
---

# Constants.Site

> @Tools.Constants.Site — where the documentation site is assembled from and built to

## Purpose

Where the documentation site is assembled from and built to.

## Interface

### Signatures

```pudu
export const SITE_DIRECTORY: Str = "build/site"
export const VAULT: Str = "wiki"
export const SECTIONS: Array[(Str, Str)] = [("protocol", "Specification"), ("decisions", "Decisions")]
export const MAP_PAGE: Str = "_MOC.md"
export const INDEX_PAGE: Str = "index.md"
export const SOURCE_DIRECTORY: Str = "website"
export const CONTENT_DIRECTORY: Str = "docs"
export const CONTRACT: Str = "schema/grail.openapi.json"
export const CONTRACT_PAGE: Str = "rest/grail.openapi.json"
export const TOC: Str = "toc.yml"
export const LINK_OPEN: Str = "[["
export const LINK_CLOSE: Str = "]]"
export const LINK_ALIAS: Str = "|"
export const LINK_HEADING: Str = "#"
export const FRONT_MATTER: Str = "---"
export const BACKLINKS: Str = "## Referenced by"
export const MARKDOWN: Str = ".md"
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** the runner

## Referenced by

[[tools/Constants/_MOC]]
