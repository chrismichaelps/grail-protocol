# Grail documentation

Practical guides live in `docs/`. The site also publishes the specification and decisions from `wiki/` and the HTTP reference from `schema/grail.openapi.json`.

## Build and preview

From the repository root, with Pudu 0.1.3 and Python 3.12 or later:

```bash
python3 tools/BuildDocs.py
python3 tools/BuildDocs.py --serve --port 8080
```

The build assembles sources into `build/site` and renders them into `build/site/_site`. Warnings fail the build. The renderer source revision and archive checksum are pinned in `tools/Constants/Docs.py`; it is downloaded into an ignored build cache. A one-line compatibility patch for Pudu 0.1.3 is applied only to that cached renderer, never to the fabric or installed dependencies.

## Sources

| Path | Purpose |
| --- | --- |
| `docs/index.yml` | Landing page and topic entry points. |
| `docs/guides/` | Task-based guides and sidebar navigation. |
| `docgen.json` | Search, templates, metadata, and resource configuration. |
| `template/public/main.css` | Site styles layered over the default theme. |
| `assets/` | The graph mark and other static resources. |
| `../wiki/protocol/`, `../wiki/decisions/` | Authoritative protocol and decision pages. |
| `../schema/grail.openapi.json` | HTTP operations, schemas, errors, and limits. |

The website hosts documentation only. The fabric API remains on localhost. Publish only `build/site/_site` with the existing assets-only Worker configuration after reviewing a successful local build.
