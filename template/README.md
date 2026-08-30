# {{WIKI_NAME}}

An **LLM wiki** — Andrej Karpathy's pattern: a human curates sources and asks questions; an
LLM agent (Claude Code) reads the sources, writes and cross-links the pages, and keeps the whole
thing consistent. The wiki is plain Markdown with `[[wikilinks]]`, browsable in Obsidian or in
the built-in web viewer.

<!-- KICKOFF: replace this paragraph with what the wiki is about and who it is for -->
Focus: *not set yet — the first Claude Code session in this folder runs `KICKOFF.md` and fills
this in.*

## Layout

| path | what |
|---|---|
| `CLAUDE.md` | the maintainer rulebook the agent reads before every operation |
| `KICKOFF.md` | first-session procedure (interview → configuration); removed once done |
| `wiki.json` | site name, page types/folders, entity kinds, facets, TOC tables — read by the tools |
| `raw/` | immutable original sources (`raw/sources.md` is the manifest) |
| `inbox/` | triage lists, scout results and plans waiting to be processed |
| `tools/` | `build-site.py` (web viewer generator, assets in `site-assets/`), `lint.py`, extractors |
| `site/` | generated web viewer (git-ignored; `python3 tools/build-site.py`) |
| `wiki/index.md` | catalog of every page — start here |
| `wiki/log.md` | append-only log of every ingest / query / lint |
| `wiki/<type>/` | one folder per page type from `wiki.json` (summaries, techniques, concepts, entities by default) |

## Using it

Open Claude Code in this folder and say:

- `ingest <url or path>` — file a source into the wiki
- `triage <collection>` — build a table of contents for a big multi-article collection
- `query <question>` — answer from the wiki with citations
- `lint` — health-check links, orphans, contradictions, missing pages
- `scout <topic>` — find candidate sources on the web, without ingesting
- `build` — regenerate the viewer (`python3 tools/build-site.py --serve` for a live preview)

## The viewer

```
python3 tools/build-site.py           # renders everything into site/
python3 tools/build-site.py --serve   # …and serves http://127.0.0.1:8080/, rebuilding on change
open site/index.html                  # works from file:// too
```

Zero dependencies. Search with facet filters (`type:`, `kind:`, `tag:` and the facets from
`wiki.json`), backlinks and a local link graph on every page, a whole-wiki graph, browse by
facet, wanted (red-link) pages, a health page, every raw source as a line-addressable page,
optional cheat sheets and TOC tables.

## Page format

Every page has YAML frontmatter (`title`, `type`, `kind`, `tags`, `aliases`, `sources`,
`created`, `updated`, plus any facets) and links other pages with `[[slug]]` or `[[slug|text]]`,
where `slug` is the filename without `.md`, unique across all wiki folders. No Obsidian-only
syntax is used, so any Markdown renderer that resolves `[[slug]]` can display it.
