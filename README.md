# llm-wiki-starter

Start a new **LLM wiki**: a knowledge base about one topic that an AI agent writes, cross-links
and maintains for you.

This is Andrej Karpathy's LLM Wiki pattern, packaged. You curate sources and ask questions;
Claude Code reads the sources, writes the pages, links them, and keeps the whole thing
consistent. The repo holds a template, a kickoff interview that bakes your topic into the
agent's rulebook, a zero-dependency web viewer and a lint pass — so every wiki you make works
the same way and shares one look and feel, while each has its own page model for its own topic.

## Quick start

The whole thing is operated in plain language. Open Claude Code in this repo and say what you
want — for example:

> **Please let's create a new LLM wiki about space ships**

That is the entire command. The agent proposes a folder (`../space-ships-wiki`), confirms it,
copies the template, and then — without leaving the session — runs the kickoff interview:

- what the wiki is about and what is explicitly **out** of scope
- who reads it, and what they want to *do* with it
- the 2–5 pillars that will structure the index
- which page types and entity kinds fit *this* topic — it proposes a model, you correct it
- whether there is one cross-cutting facet (`era`, `agency`, `propulsion` …), and whether cheat
  sheets make sense
- how the field writes its values, and what goes stale and needs a date
- which sources you already have, which canonical ones to ingest first, what to scout

It asks in small batches, offers a default for every question so you can just say "yes", and
works in your language. Then it rewrites the rulebook, `wiki.json`, README and index for your
topic, writes a first-ingest plan, lints, builds the viewer, deletes the kickoff file, and hands
you the page model, the first three sources to ingest and the questions still open.

If you would rather script it, the shell path does the same setup:

```
./new-wiki.sh ../space-ships-wiki "Space Ships Wiki"   # copy the template, fill the name, git init
cd ../space-ships-wiki
claude                                                 # first session finds KICKOFF.md, runs the interview
```

### Then you just talk to it

`cd` into the new wiki, start Claude Code and speak normally. The operation names in the table
below are how the rulebook labels things — you never type them literally:

- *"Please scout for new articles covering ion propulsion"* — searches, fetches and skims
  candidates, writes them to `inbox/` with flags and the pages each would touch. Ingests nothing.
- *"Which of those are most valuable? Recommend what to ingest first"* — it has read them, so it
  argues for a shortlist. You decide what enters the wiki.
- *"Ingest the top three, plus the PDF I put in raw/"* — summaries, then the ripple through
  every page each source touches.
- *"That NASA archive is huge — triage it first"* — builds a filterable table of contents, one
  row per article, so you pick instead of swallowing 900 articles.
- *"What do we actually know about specific impulse? Cite it"* — answers from the wiki with
  `[[citations]]`, keeping model knowledge visibly separate.
- *"This page contradicts that one — check both against the raw sources"* — it follows the
  citation chain back to the original lines and reports.
- *"Lint, fix what's mechanical, then build the site and serve it"*

The starter repo itself works the same way: *"update the tools in ../space-ships-wiki"* or
*"sync the improvements from ../space-ships-wiki back into the template"*.

## The point: the repo *is* the knowledge

The generated site is genuinely good to read — full-text search, backlinks, link graphs, cheat
sheets. But the site is the surface, not the product. Three things separate this from "a folder
of notes with a static site generator":

**The content is fully managed by the agent.** You do not hand-write pages. You bring a source;
the agent summarizes it, decides which existing pages it changes, rewrites those, creates the
ones that are missing, updates the catalog and logs what it did. Your job is curation and
questions — what enters the wiki, and what you want to know.

**Opening an agent in the repo gives it the whole topic.** `CLAUDE.md` is a rulebook the agent
reads before every operation: the focus, the page model, the domain's notation, the citation
rules. `wiki/index.md` is a catalog it reads first on any question. `wiki/log.md` is the
append-only history of every operation. So a fresh session — or a second one running in
parallel — starts out knowing the domain's vocabulary, what is already established and what is
still unverified, without you re-explaining anything. The wiki is the codebase, the agent is the
programmer, the viewer is just the IDE.

**Raw sources stay in the repo and stay addressable.** Originals live immutable under `raw/`,
one folder per collection, with a manifest recording origin, fetch date and license. Every claim
on a page cites a summary page; every summary records the `source-path` it came from. That makes
an unbroken chain — claim → summary → the exact lines of the original — which both you and the
agent can walk. When a question needs the primary text rather than the compression (the actual
register table, a spec's exact wording), the agent opens the raw file and reads it.

Pages are plain Markdown with `[[wikilinks]]` and YAML frontmatter — no Obsidian-only syntax —
so the same wiki opens in Obsidian, in the built-in viewer, or in anything else you write.

## What it is, and what it isn't

**Not a second brain.** A second brain (PARA, Zettelkasten, a hand-built Obsidian vault) is
written *by* a human *for* a human's later recall. This flips the division of labor: rather than
you maintaining a knowledge base and occasionally asking an AI about it, the agent builds and
maintains the whole thing. Same substrate, same goal of knowledge that accumulates, different
author. And a second brain is personal by definition, while a topic wiki has nothing to do with
you — it is about the domain. A second brain is one thing you *could* build with this pattern,
not what the pattern is.

**Adjacent to a skill, on a different axis.** Skills and wikis rhyme structurally — both are
progressive-disclosure filesystems where an agent reads a short index first and loads only the
files it needs. But a skill is *know-how*: procedures, mostly static, human-written. A wiki is
*know-what*: facts about a domain, compiled from sources, cross-linked, and continuously
rewritten as new sources land. The strongest combination is a skill that tells an agent how to
consult and maintain a particular wiki — the librarian's procedures next to the library. A
static "how to configure X" skill rots; a wiki keeps absorbing the new sizing tables and
gotchas.

**Not RAG.** RAG retrieves chunks at query time, so the model rediscovers the domain from
scratch on every question and nothing accumulates. A wiki moves that work to write time —
knowledge treated the way a compiler treats source code: pre-process once, run fast forever. The
synthesis, the contradictions found, the cross-links drawn are all done and saved before you
ever ask.

## The operations

These are defined in the wiki's own `CLAUDE.md`, which the agent reads before it does
anything. The names are labels, not syntax — phrase them however you like.

| operation | what it does |
|---|---|
| `ingest <url or path>` | File a source: fetch it verbatim into `raw/`, register it in the manifest, write one summary per *article*, then **ripple** it through the wiki. |
| `triage <collection>` | For big multi-article sources (newsletters, forum dumps, doc sets): a script builds a filterable table of contents in `inbox/`, one row per article with relevance flags. You pick rows; nothing is ingested behind your back. |
| `scout <topic>` | Search the web for candidate sources, fetch and skim each, and write 5–10 candidates to `inbox/` with flags and the pages each would touch. Again: no auto-ingest, you choose what enters. |
| `query <question>` | Answer from the wiki with `[[citations]]`, keeping what the wiki knows separate from what the model adds — and offering to save a good synthesis as a new page. |
| `lint` | Broken links, orphans, contradictions, stale claims, pages missing from the index, `(unverified)` claims a new source could now confirm, frontmatter violations, duplicate slugs. |
| `build` | Render the viewer into `site/`; `--serve` also serves it and rebuilds on change. |

**Ripple is where the value is.** It is step 4 of every ingest and the reason this compounds: a
good source does not produce one summary and stop — it updates 5–15 pages. A tool manual touches
the tool's page, every technique that tool implements (a new per-tool subsection with the
concrete steps), the file formats, the author. An interview touches people, groups, tools and
works. A source that produced a summary and nothing else was ingested wrong.

Two conventions carry a lot of weight. **Wanted pages**: linking `[[to-a-page-that-does-not-exist-yet]]`
is a TODO, not an error — the viewer gives each wanted slug a page listing who links to it, so
the red links become the ingest queue. **`(unverified)` markers**: the agent may add general
knowledge only when marked, collected under a `## To verify` heading — which turns out to be the
best planning tool there is, because the next sources are chosen to retire those markers.

## The viewer

`python3 tools/build-site.py` renders `wiki/`, the `inbox/` tables and `raw/` into a static site.
Zero dependencies, Python 3 only; the reference wiki's 654 pages build in about 1.4 s.

- **Search** over every page, heading, cheat sheet and TOC row, with facet filters (`type:`,
  `kind:`, `tag:` and whatever facet your topic defines) — and an option to search the full text
  of every raw source, where results deep-link to the line.
- **Pages** with an on-page TOC, backlinks, a local link graph, highlighted citations and
  `(unverified)` markers, and red links to wanted pages.
- **Link graph** for the whole wiki or the neighbourhood of one page; drag, zoom, filter by type.
- **Cheat sheets** per tool: the tool page's reference tables plus every technique page's
  section for that tool, with a print stylesheet.
- **Browse** by type, kind, facet or tag; a **health** page mirroring lint (wanted pages,
  unverified claims, stubs, orphans, recent changes); **sources** — every raw file as a numbered,
  line-addressable page, which is what makes the citation chain clickable.

Everything topic-specific — page types and their folders, entity kinds, facets, TOC tables,
cheat-sheet rules — is data in `wiki.json`, never code. See `docs/wiki-json.md`.

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
    wiki-json.md       the configuration schema, with a worked example
  reference/
    chiptune-wiki/     a real wiki's CLAUDE.md, README, index, sources manifest, wiki.json,
                       triage/extract scripts, a scout file and a plan file — a complete worked example
    example-pages/     one real page per type (technique, concept, entity ×2, summary ×2)
    lessons-learned.md what the first wiki taught us and what to decide at kickoff
```

Extracted from a chiptune wiki (476 pages and 300+ raw sources in its first days, 654 pages now)
once the pattern had proven itself. That wiki is not public — its raw sources are third-party
material — but a snapshot of its non-page files is the worked example under `reference/`, and it
is what `tools/selftest.sh` builds through the template's own generator.

## Keeping wikis in sync

- Improve the viewer or lint **here**, run `tools/selftest.sh`, then `tools/update-tools.sh <wiki>`
  for each wiki. Only `tools/` is touched — never a wiki's pages or its config.
- If you improve a tool inside a wiki, port it back here (Claude: `sync from <wiki>`), keeping
  the template topic-neutral.
- The rulebook text (`template/CLAUDE.md`) is copied, not linked: each wiki's rulebook diverges
  on purpose after the kickoff. When the generic parts change, apply the change where it matters.

## The failure mode to watch

Because the agent compresses sources into pages, one misunderstanding can propagate quietly
across every page it links. That is the reason `lint` exists as a first-class operation rather
than a nicety, why every claim is required to cite a summary and every summary to record its raw
`source-path`, and why unverified model knowledge has to be marked as such. Spot-check generated
pages against the raw text they came from — the chain is there to make that cheap.

## License

MIT — see `LICENSE`.
