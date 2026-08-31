# What is in this repo

`llm-wiki-starter` is the template and toolkit for LLM wikis. It is **not** a wiki itself —
nothing here accumulates knowledge; it is what you use to create wikis that do, and to keep them
working the same way.

```
llm-wiki-starter/
  README.md            the pitch and the quick start
  CLAUDE.md            rules for maintaining the starter + the `new wiki` / `update tools` operations
  new-wiki.sh          create a wiki from template/
  template/            copied verbatim into every new wiki
    CLAUDE.md          generic maintainer rulebook (operations, conventions, boundaries) with a first-session hook
    KICKOFF.md         the interview + configuration procedure; deletes itself when done
    wiki.json          site name, page types/folders, kinds, facets, TOC tables, cheat-sheet rule
    README.md          human intro (placeholders filled by the kickoff)
    wiki/index.md, wiki/log.md, raw/sources.md, inbox/README.md, .gitignore
    tools/build-site.py      static viewer generator, driven by wiki.json (zero dependencies)
    tools/site-assets/       structural stylesheet + search/graph scripts (the shared look and feel)
    tools/site-assets/themes/  one file per visual theme; wiki.json "style" picks it
    tools/lint.py            broken links, orphans, frontmatter, index coverage, unverified count,
                             citation drift, unlanded ripples
    tools/pdf-to-text.swift, html-to-text.py, extract-forum-posts.py, add-section.py   ingest helpers
    tools/fetch-docs.py      mirror a documentation site into raw/, driven by its llms.txt
  tools/
    update-tools.sh    push template tools into an existing wiki (never touches its pages or config)
    selftest.sh        create a throwaway wiki, lint + build it; build the reference wiki through the template
  docs/
    what-is-an-llm-wiki.md   the pattern, and how it differs from a second brain, a skill and RAG
    repo-layout.md           this file
    wiki-json.md             the configuration schema, with a worked example
  reference/
    chiptune-wiki/     a real wiki's CLAUDE.md, README, index, sources manifest, wiki.json,
                       triage/extract scripts, a scout file and a plan file — a complete worked example
    example-pages/     one real page per type (technique, concept, entity ×2, summary ×2)
    lessons-learned.md what the first wiki taught us and what to decide at kickoff
```

## The three parts

**`template/`** is the wiki you get. `new-wiki.sh` copies it verbatim and fills three
placeholders — `{{WIKI_NAME}}`, `{{WIKI_SLUG}}`, `{{DATE}}`. Everything topic-specific in a
finished wiki gets there through the kickoff interview, not through the template: page types,
folders, entity kinds, facets, TOC tables and cheat-sheet rules are all data in `wiki.json`
(see [wiki-json.md](wiki-json.md)), and the topic-specific prose in the rulebook lives behind
`<!-- KICKOFF -->` markers the interview replaces. The template must stay usable for *any*
topic.

**`tools/`** (the starter's own, not the template's) is maintenance. `update-tools.sh` pushes
improved template tools into an existing wiki and touches only its `tools/` — never its pages,
never its `wiki.json`. `selftest.sh` creates a throwaway wiki, lints and builds it, and — if a
`../chiptune-wiki` sibling is present — builds that through the template's generator too; it
must pass before any commit that touches `template/tools/`.

**`reference/`** is a worked example, and nothing in it is ever copied into a new wiki. It is
there to show the level of detail a finished rulebook, index and sources manifest reach after a
few hundred pages, and how the generic viewer is configured for one specific topic.

It is a snapshot of the non-page files of a chiptune wiki — 476 pages and 300+ raw sources in
its first days, 654 pages now — taken once the pattern had proven itself. That wiki is not
public, because its `raw/` holds third-party material, but its configuration builds through this
repo's generator unchanged, which is exactly what `selftest.sh` checks.

## Keeping several wikis in sync

The rulebook (`template/CLAUDE.md`) is *copied* into each wiki, not linked — every wiki's
rulebook is meant to diverge after its kickoff. The tools are not: they should stay identical
everywhere.

- Improve the viewer or the lint **here**, run `tools/selftest.sh`, then
  `tools/update-tools.sh <wiki>` for each wiki. Run it with `--dry-run` first to see the diff.
- If you improved a tool *inside* a wiki, port it back (say `sync from <wiki>` to Claude in this
  repo), keeping the template topic-neutral — no topic words, no hard-coded folders, facets or
  collections, since those belong in `wiki.json`.
- When the generic parts of the rulebook change, apply the change by hand where it matters.
  There is no mechanism for this on purpose.
