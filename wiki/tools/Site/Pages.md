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
/// A vault page as a site page in folder `from`: no front matter, no backlinks, and wikilinks rewritten.
export fn published(text: Str, from: Str) -> Str { linked(withoutBacklinks(withoutFrontMatter(text)), from) }
/// The text with front matter removed.
export fn withoutFrontMatter(text: Str) -> Str
/// The text without its backlinks section.
export fn withoutBacklinks(text: Str) -> Str
/// Every wikilink of the text as a site link when its page is published, or as its text when it is not.
export fn linked(text: Str, from: Str) -> Str
/// One wikilink's body as Markdown.
export fn rendered(body: Str, from: Str) -> Str
/// The paper's links as site links: vault sections become site sections, other repository paths point at the repository.
export fn paperLinks(text: Str) -> Str
/// The first level-one heading of a page.
export fn titleOf(text: Str, fallback: Str) -> Str
```

### Linkage

- **Requires:** nothing inside the fabric
- **Consumed by:** the runner

## Referenced by

[[tools/Site/_MOC]]
