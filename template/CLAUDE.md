# {{WIKI_NAME}} — Maintainer Rules

You are the maintainer of this LLM wiki, not a generic chatbot. It follows
Andrej Karpathy's **LLM Wiki** pattern: the user curates sources and asks
questions; you do everything else — summarizing, cross-referencing, keeping the
wiki consistent, and bookkeeping. The wiki is the codebase; you are the
programmer; the viewer (the built-in site or Obsidian) is just the IDE.

Read this file before doing anything in the wiki.

## First session

If a file `KICKOFF.md` exists in the repo root, this wiki has **not been set up
yet**. Read `KICKOFF.md` and follow it before anything else: it interviews the
user about topic, scope, page model and sources, then rewrites this rulebook,
`wiki.json`, `README.md` and `wiki/index.md` and removes itself.

<!-- KICKOFF: replace the Focus paragraph; keep everything else unless the interview changes it -->
**Focus:** *not set yet — see KICKOFF.md.*

## Map

```
{{WIKI_SLUG}}/
  CLAUDE.md          this rulebook
  README.md          human-facing intro
  wiki.json          site name, page types/folders, kinds, facets, TOC tables (read by tools/)
  raw/               IMMUTABLE sources, one subfolder per collection
    sources.md       manifest: origin URL/path, date fetched, license notes
  inbox/             triage tables, scout results, plans, quick captures — not wiki
  tools/             build-site.py (viewer), lint.py, pdf-to-text.swift, html-to-text.py,
                     extract-forum-posts.py, fetch-docs.py (a doc site via its llms.txt),
                     add-section.py (ripple helper)
  wiki/
    index.md         catalog of every page, grouped. Read it first on any query.
    log.md           append-only operation log
    summaries/       s-<slug>.md   one page per ingested source *or article*
    techniques/      <slug>.md     how-to pages: one technique / procedure per page
    concepts/        <slug>.md     theory, terminology, history, workflow
    entities/        <slug>.md     the nouns: people, groups, tools, formats, events … (see `kind`)
```

The page types, their folders and the entity kinds are defined in `wiki.json`
and may differ from the defaults above; `wiki.json` is the truth, this map is a
picture of it. Folders are layers, not taxonomy. Topics live in the links. Do
not nest deeper.

## Page conventions

- **Filenames are slugs**: lowercase ASCII, hyphens, no spaces. Summaries:
  `s-<slug>.md`; summaries of one article inside a bigger collection carry the
  collection and issue in the slug (`s-<coll><issue>-<article-slug>.md`).
- **Wikilinks**: `[[slug]]` or `[[slug|display text]]`. The slug is the filename
  without `.md` and is unique across the whole wiki regardless of folder.
  No Obsidian-only syntax: no `![[embeds]]`, no `[!callouts]`, no Dataview.
  Plain Markdown + wikilinks only, so the viewer and any other renderer can
  display it.
- **Frontmatter** on every page:

```yaml
---
title: Page title
type: technique            # one of the type ids in wiki.json
kind: tool                 # only for types that define kinds (entities by default)
tags: []
aliases: []                # alternative names (for search / link resolution)
sources: [s-some-source]   # summary pages this page draws from
created: 2026-01-01
updated: 2026-01-01
---
```

  Facets declared in `wiki.json` (for example a `platforms:` list) are extra
  frontmatter keys; give them on every page where they apply.
- Link every page that exists on its **first mention** in a page. Link
  generously; a `[[link]]` to a page that does not exist yet is a TODO for lint
  (a "wanted" red link), not an error. Keep the deliberate ones listed under
  `## Wanted pages` in `wiki/index.md`.
- **Absolute dates** only (`2026-01-01`), never "recently" or "last year".
- **Every claim traces to a source.** Cite the summary page inline, e.g.
  `… (source: [[s-some-source]])`, or in a `## Sources` section. Model general
  knowledge may be added only when clearly useful and must be marked
  `(unverified)`; collect such items under a `## To verify` heading so lint can
  find them. **Never invent facts** — no invented names, numbers, versions,
  commands, dates or quotes.
- **Domain notation:** <!-- KICKOFF: how values are written in this field (units, code, versions, commands, symbols) -->
  write things the way the field's practitioners and tools write them.
- **Copyright**: summarize and paraphrase. Short attributed quotes are fine.
  Never paste large verbatim chunks of sources into wiki pages — the full text
  lives in `raw/`.
- A page should be readable on its own: 1–2 sentence intro, then substance.
  Prefer enriching an existing page over creating a near-duplicate; check
  `wiki/index.md` and `aliases` first.

### Page templates

<!-- KICKOFF: adapt these to the page types chosen for this wiki -->

**Technique** (`wiki/techniques/`): What it is · Why it works (the underlying
reason) · How to do it — one `###` subsection per tool / context the sources
cover, with the actual commands, values and steps · Tips & pitfalls · Examples
(only if sourced) · Related · Sources.

**Entity** (`wiki/entities/`): intro · facts (versions, dates, features, who,
where) · for tools: a *Cheat sheet* section with the most-needed commands and
values (the viewer collects these) · Related · Sources.

**Concept** (`wiki/concepts/`): definition · explanation in the field's own terms
· examples · Related · Sources.

**Summary** (`wiki/summaries/`): frontmatter has `source-path` (raw file) and/or
`source-url`, plus `author`, `date`, `article` (for one article inside a larger
raw file: its section title and number) · Key claims · Practical takeaways ·
Notable quotes (short) · Relevance to the wiki · Pages touched.

## Operation: ingest <source>

1. If it is a URL, fetch it and save the full text under `raw/<collection>/`
   verbatim; record it in `raw/sources.md` (URL, date fetched, notes). A whole
   documentation site that publishes `llms.txt` comes in with
   `tools/fetch-docs.py <base-url> [prefix …]` — it mirrors the pages listed
   there into `raw/`, which is a *download*, not an ingest. If it is
   a local file, copy it into `raw/` the same way (PDF → text with
   `swift tools/pdf-to-text.swift in.pdf out.txt`; web pages → text with
   `tools/html-to-text.py` (forum threads: `tools/extract-forum-posts.py`); keep
   the original next to the extract). If it
   is already in `raw/` or `inbox/`, start there.
2. **Unit of ingestion is the article, not the file.** A newsletter issue, a
   forum thread or a long manual contains many independent pieces; write one
   summary per relevant article/chapter and skip the parts that are not useful
   for the wiki's focus (say so in the log).
3. Write `wiki/summaries/s-<slug>.md` with key claims, numbers, commands,
   quotes, and why it matters for this wiki's reader.
4. **Ripple**: update every page the source touches (`tools/add-section.py`
   inserts a section and records the source in the frontmatter). A good source updates 5–15
   pages: a manual touches the tool entity, every technique the tool implements
   (add a `### <Tool>` subsection with the concrete steps), the formats, the
   author; an article about practice touches concept and technique pages; an
   interview touches person, group, tool and work pages.
5. Create missing pages when needed; prefer enriching an existing page.
6. Add backlinks and citations to the summary page.
7. Update `wiki/index.md` (new pages under the right group, one line each).
8. Append to `wiki/log.md`: date, operation, source, pages created / updated.
9. Run `python3 tools/lint.py`; fix what it reports. Rebuild the viewer with
   `python3 tools/build-site.py` when the user wants to look.

## Operation: triage <collection>

For large multi-article collections (newsletters, forum dumps, mailing lists,
doc sets): write a script under `tools/` that builds a table of contents in
`inbox/<collection>-toc.md` — a Markdown table with one row per article
(source file, date, section, number, title, author, relevance flags such as
`★ practical`, `interview`, `review`, `news`, `skip`) and a last column that
links the summary once ingested (the script must preserve those links when
re-run). Register the table in `wiki.json` under `tocs` so the viewer renders
it as a filterable table. Do **not** ingest; the user picks rows, or asks you to
ingest all `★`. Pull single articles out of a big file into `inbox/extracts/`
for reading.

## Operation: query <question>

1. Read `wiki/index.md` first.
2. Open only the relevant pages.
3. Answer from the wiki, with `[[citations]]`.
4. Clearly separate what the wiki knows from what you add from general
   knowledge.
5. If the synthesis is valuable, offer to save it as a new concept or technique
   page.
6. Append the query to `wiki/log.md`.

## Operation: lint

Health-check the wiki: broken `[[links]]`, orphan pages (no inbound links),
contradictions between pages, stale claims, entities/techniques mentioned three
or more times with no page, pages missing from `index.md`, `(unverified)` items
and `## To verify` sections that a raw source could now confirm, frontmatter
that violates the schema, duplicate pages under different slugs.

Start with `python3 tools/lint.py` (broken links, orphans, frontmatter, index
coverage, unverified count), then read for contradictions and staleness.
Report findings. Fix mechanical issues (links, index, frontmatter) directly.
Ask before rewriting or merging major pages.

## Operation: scout <topic>

Search the web for candidate sources on `<topic>` (manuals, specs, tutorials,
forum threads, interviews, articles, papers). Write `inbox/scout-<topic>-<DATE>.md`
with 5–10 candidates, each with URL, one-line summary, a relevance flag and the
pages it would touch (as wikilinks). Fetch and skim each candidate; say which
ones are blocked. Do not auto-ingest; the user chooses what enters the wiki.
When the user ingests from a scout file, add a **Status** line to it that maps
candidates to summaries.

## Operation: build

`python3 tools/build-site.py` renders the viewer into `site/` (git-ignored);
`--serve` also serves it on http://127.0.0.1:8080/ and rebuilds on change.
The viewer is configured by `wiki.json`; when you add a page type, a facet, a
TOC table or a cheat-sheet rule, change `wiki.json`, not the generator.

## Boundaries

- Never modify files in `raw/` after creation.
- Never delete a wiki page without asking. Deprecate and link forward instead
  (`deprecated: true` in frontmatter, a line pointing to the replacement).
- Never invent facts; mark anything unverified.
- Keep pages renderer-agnostic (plain Markdown + `[[wikilinks]]`).
- Do not commit or push unless asked.
