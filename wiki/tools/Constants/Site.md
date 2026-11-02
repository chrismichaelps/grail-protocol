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
/// The folder the site's sources are assembled in; it is rebuilt every time.
export const SITE_DIRECTORY: Str = "build/site"
/// The vault the published pages come from.
export const VAULT: Str = "wiki"
/// The vault folders published as sections of the site, with their titles.
export const SECTIONS: Array[(Str, Str)] = [("protocol", "Specification"), ("decisions", "Decisions")]
/// The page of a vault folder that becomes its section's index.
export const MAP_PAGE: Str = "_MOC.md"
/// The name a section's index takes on the site.
export const INDEX_PAGE: Str = "index.md"
/// The paper that becomes the site's landing page.
export const README: Str = "README.md"
/// The contract rendered as the HTTP API reference.
export const CONTRACT: Str = "schema/grail.openapi.json"
/// Where the contract is placed in the site.
export const CONTRACT_PAGE: Str = "rest/grail.openapi.json"
/// The repository links outside the site point to.
export const REPOSITORY: Str = "https://github.com/chrismichaelps/grail-protocol/blob/main/"
/// The address the published site answers at.
export const SITE_URL: Str = "https://grail-protocol.chrisperezsantiago1.workers.dev"
/// The site's title.
export const TITLE: Str = "Grail Protocol"
/// What the site's footer says.
export const FOOTER: Str = "Grail · Apache License 2.0"
/// The configuration file docgen reads.
export const CONFIGURATION: Str = "docgen.json"
/// The table of contents docgen reads in each folder.
export const TOC: Str = "toc.yml"
/// Opens a wikilink.
export const LINK_OPEN: Str
/// Closes a wikilink.
export const LINK_CLOSE: Str = "]]"
/// Separates a wikilink's target from its text.
export const LINK_ALIAS: Str = "|"
/// Separates a wikilink's page from its heading.
export const LINK_HEADING: Str = "#"
/// Fences the front matter of a vault page.
export const FRONT_MATTER: Str = "---"
/// The heading the backlinks section starts with; it is not published.
export const BACKLINKS: Str = "## Referenced by"
/// The Markdown extension.
export const MARKDOWN: Str = ".md"
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** the runner

## Referenced by

[[tools/Constants/_MOC]]
