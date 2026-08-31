# llm-wiki-starter

Everything needed to start a new **LLM wiki** — Andrej Karpathy's pattern: you curate sources
and ask questions, Claude Code reads the sources, writes and cross-links the pages, and keeps
the wiki consistent — so that every wiki we make works the same way, operates with the same
commands (`ingest`, `triage`, `query`, `lint`, `scout`, `build`) and shares one look and feel,
while each has its own page model for its own topic.

Extracted from a chiptune wiki (476 pages, 300+ raw sources) after its first days. That wiki
is not public — its raw sources are third-party material — but a snapshot of its non-page files
is the worked example under `reference/`.

## Quick start

```
./new-wiki.sh ../ai-models-wiki "AI Models Wiki"   # copy the template, fill the name, git init
cd ../ai-models-wiki
claude                                             # first session: finds KICKOFF.md, runs the interview
```

Or stay in this repo, open Claude Code here and say **`new wiki ../ai-models-wiki`** — Claude
runs the script and then the kickoff interview for the new wiki right away, so you can `cd` into
a wiki that is already configured.

The kickoff asks about topic, scope, reader, the page model (types, kinds, an optional facet),
notation, known sources and habits; then it rewrites the rulebook, `wiki.json`, README and index
for the topic, writes a first-ingest plan (optionally a scout), lints, builds the viewer and
removes itself. After that the next command is `ingest …`.

## What is in here

```
llm-wiki-starter/
  README.md            this file
  CLAUDE.md            rules for maintaining the starter + the `new wiki` / `update tools` operations
  new-wiki.sh          create a wiki from template/
  template/            copied verbatim into every new wiki
    CLAUDE.md          generic maintainer rulebook (operations, conventions, boundaries) with a first-session hook
    KICKOFF.md         the interview + configuration procedure; deletes itself when done
    wiki.json          site name, page types/folders, kinds, facets, TOC tables, cheat-sheet rule
    README.md          human intro (placeholders filled by the kickoff)
    wiki/index.md, wiki/log.md, raw/sources.md, inbox/README.md, .gitignore
    tools/build-site.py      static viewer generator, driven by wiki.json (zero dependencies)
    tools/site-assets/       stylesheet + search/graph scripts (the shared look and feel)
    tools/lint.py            broken links, orphans, frontmatter, index coverage, unverified count
    tools/pdf-to-text.swift, html-to-text.py, extract-forum-posts.py, add-section.py   ingest helpers
    tools/fetch-docs.py      mirror a documentation site into raw/, driven by its llms.txt
  tools/
    update-tools.sh    push template tools into an existing wiki (never touches its pages or config)
    selftest.sh        create a throwaway wiki, lint + build it; build the reference wiki through the template
  docs/
    wiki-json.md       the configuration schema, with the chiptune example
  reference/
    chiptune-wiki/     the chiptune wiki's CLAUDE.md, README, index, sources manifest, wiki.json,
                       triage/extract scripts, a scout file and a plan file — a complete worked example
    example-pages/     one real page per type (technique, concept, entity ×2, summary ×2)
    lessons-learned.md what the chiptune wiki taught us and what to decide at kickoff
```

## The viewer

`tools/build-site.py` renders `wiki/`, `inbox/` tables and `raw/` into a static site with search
(facet filters `type:` `kind:` `tag:` + your facets), backlinks and a local link graph on every
page, a whole-wiki graph, browse-by-facet pages, wanted (red-link) pages, a health page, every raw
source as a line-addressable page, optional per-tool cheat sheets and filterable TOC tables. It
reads everything topic-specific from `wiki.json` — see `docs/wiki-json.md`. A 654-page wiki
builds through this exact generator with `reference/chiptune-wiki/wiki.json` (that is what
`tools/selftest.sh` checks when that wiki is present locally), so improvements made here can be
pushed to every wiki with `tools/update-tools.sh`.

## Keeping wikis in sync

- Improve the viewer or lint **here**, run `tools/selftest.sh`, then `tools/update-tools.sh <wiki>`
  for each wiki.
- If you improve a tool inside a wiki, port it back here (Claude: `sync from <wiki>`), keeping the
  template topic-neutral.
- The rulebook text (`template/CLAUDE.md`) is copied, not linked: each wiki's rulebook diverges on
  purpose after the kickoff. When the generic parts change, apply the change by hand where it matters.
