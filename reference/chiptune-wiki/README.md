# Chiptune Wiki

An **LLM wiki** about chiptune — how to make it, the tools, the chips, the
theory, the history and the people. Built on Andrej Karpathy's LLM Wiki
pattern: a human curates sources and asks questions; an LLM agent (Claude Code)
reads the sources, writes and cross-links the pages, and keeps the whole thing
consistent. The wiki is plain Markdown with `[[wikilinks]]`, so it can be
browsed in Obsidian or in a self-written web viewer.

Focus platforms: **C64 / SID** (SID-Wizard, GoatTracker …), **Game Boy**
(LSDJ), **PC trackers** (Scream Tracker 3, Impulse Tracker, OpenMPT, Schism).

## Layout

| path | what |
|---|---|
| `CLAUDE.md` | the maintainer rulebook the agent reads before every operation |
| `raw/` | immutable original sources (`raw/sources.md` is the manifest) |
| `inbox/` | triage lists and candidate sources waiting to be processed |
| `tools/` | `build-site.py` (the web viewer generator, assets in `site-assets/`), `lint.py` (link/orphan/frontmatter check), `triage-traxweekly.py`, `extract-traxweekly-article.py` |
| `site/` | generated web viewer (git-ignored; rebuild with `python3 tools/build-site.py`) |
| `wiki/index.md` | catalog of every page — start here |
| `wiki/log.md` | append-only log of every ingest / query / lint |
| `wiki/summaries/` | one summary per ingested source or article (`s-…`) |
| `wiki/techniques/` | one page per technique, with per-tool how-to sections |
| `wiki/concepts/` | theory, terminology, history, workflow |
| `wiki/entities/` | people, groups, tools, chips, platforms, formats, songs, publications |

## Using it

Open Claude Code in this folder and say:

- `ingest <url or path>` — file a source into the wiki
- `triage traxweekly` — refresh the article table of contents in `inbox/`
- `query <question>` — answer from the wiki with citations
- `lint` — health-check links, orphans, contradictions, missing pages
- `scout <topic>` — find candidate sources, without ingesting

## Page format

Every page has YAML frontmatter (`title`, `type`, `kind`, `platforms`, `tags`,
`aliases`, `sources`, `created`, `updated`) and links other pages with
`[[slug]]` or `[[slug|text]]`, where `slug` is the filename without `.md`,
unique across all wiki folders. No Obsidian-only syntax is used.

## The viewer

```
python3 tools/build-site.py           # renders everything into site/ (0.3 s)
python3 tools/build-site.py --serve   # …and serves http://127.0.0.1:8080/, rebuilding on change
open site/index.html                  # works from file:// too
```

Zero dependencies (Python 3, no packages). `tools/site-assets/` holds the
stylesheet and the two scripts (`app.js`: search, navigation, TraxWeekly table,
cheat-sheet tabs; `graph.js`: the link graph). What the site offers:

- **Search** (`/`): title, alias, heading and full-text search over every page,
  cheat sheet and the 909 TraxWeekly articles, with filters such as
  `type:technique`, `kind:tool`, `platform:c64`, `tag:sid`; tick *raw sources*
  to search the full text of every original source, results deep-link to the
  line.
- **Pages**: frontmatter strip, on-page TOC, backlinks, local link graph,
  citations and `(unverified)` markers highlighted, red links to *wanted* pages
  (each wanted page lists who links to it).
- **Link graph** (`graph.html`): the whole wiki or the neighbourhood of one page
  (`?focus=slug`), filter by type, drag / zoom / highlight.
- **Cheat sheets**: per tool, the tool page's reference tables plus every
  technique page's `### <Tool>` section, with a print stylesheet.
- **Browse** by type / kind / platform / tag; **Health** (wanted pages,
  unverified claims, stubs, orphans, recent changes); **Sources** — every raw
  file as a numbered, line-addressable page (TraxWeekly issues get per-article
  anchors that the TOC table links into); the **TraxWeekly TOC** as a
  filterable, sortable table.

## Building a viewer (notes for the website)

The wiki is plain files; a renderer needs only:

- **Frontmatter** (YAML between `---` lines) on every page: `title`, `type` (technique / concept / entity / summary / index / log), `kind` (entities), `platforms`, `tags`, `aliases`, `sources`, `created`, `updated`. Summaries add `source-path`, `source-url`, `author`, `date`, `article`.
- **Links**: `[[slug]]` and `[[slug|display text]]`; `slug` = filename without `.md`, unique across all `wiki/` folders (resolve by scanning `wiki/**/*.md`). Unresolved links (the "wanted pages" in `index.md`) should render as red links, not errors.
- **Markdown**: headings, paragraphs, bullet lists, tables (used heavily for cheat sheets), fenced and inline code (tracker notation like `C-4 01 .. G08`, hex like `$7F`), blockquotes, bold/italic. No HTML, embeds, callouts or footnotes are used.
- **Navigation**: `wiki/index.md` is the home page; `wiki/log.md` the changelog; `inbox/traxweekly-toc.md` is a large Markdown table (~910 rows). Backlinks can be computed by scanning links. Aliases are useful for search.
- **Raw sources** in `raw/` are plain text (some CP437 originals with UTF-8 copies alongside) and one PDF; they can be shown as `<pre>` or linked.
