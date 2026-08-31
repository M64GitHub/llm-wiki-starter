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

- what the wiki is about, and what is explicitly **out** of scope
- who reads it, what they want to *do* with it, and the 2–5 pillars that structure the index
- which page types and entity kinds fit *this* topic — it proposes a model, you correct it
- an optional cross-cutting facet (`era`, `agency`, `propulsion` …), and whether cheat sheets fit
- how the field writes its values, what goes stale, which sources you have and what to scout

It asks in small batches, offers a default for every question so you can just say "yes", and
works in your language. Then it rewrites the rulebook, `wiki.json`, README and index for your
topic, writes a first-ingest plan, lints, builds the viewer, deletes itself, and hands you the
page model, the first sources to ingest and the questions still open.

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

The generated site is good to read — search, backlinks, graphs, cheat sheets. But the site is
the surface, not the product. Three things separate this from notes plus a static site generator:

**The content is fully managed by the agent.** You do not hand-write pages. You bring a source;
the agent summarizes it, decides which existing pages change, rewrites those, creates the
missing ones, updates the catalog and logs what it did. Your job is curation and questions.

**Opening an agent in the repo gives it the whole topic.** `CLAUDE.md` is a rulebook it reads
before every operation — the focus, the page model, the domain's notation, the citation rules.
`wiki/index.md` is the catalog it reads first on any question; `wiki/log.md` is the append-only
history. So a fresh session, or a second one running in parallel, starts out knowing the
vocabulary, what is established and what is still unverified, with nothing re-explained. The
wiki is the codebase, the agent is the programmer, the viewer is just the IDE.

**Raw sources stay addressable.** Originals live immutable under `raw/`, one folder per
collection, with a manifest of origin, fetch date and license. Every claim cites a summary page;
every summary records the `source-path` it came from — an unbroken chain from a claim to the
exact lines of the original, walkable by you and by the agent. When a question needs the primary
text rather than the compression, the agent opens the raw file and reads it.

Pages are plain Markdown with `[[wikilinks]]` and YAML frontmatter — no Obsidian-only syntax —
so a wiki opens in Obsidian, in the built-in viewer, or in anything else you write.

## What it is, and what it isn't

- **Not a second brain.** A second brain is written by a human for that human's later recall.
  Here the agent is the author — and a topic wiki is about the domain, not about you.
- **Adjacent to a skill.** A skill holds *know-how*: procedures, human-written, mostly static. A
  wiki holds *know-what*: facts compiled from sources and rewritten as new ones land. The
  strongest combination is both — a skill that tells an agent how to maintain a particular wiki.
- **Not RAG.** RAG retrieves chunks at query time, rediscovering the domain on every question
  and keeping nothing. A wiki does the synthesis at write time and saves it: knowledge treated
  the way a compiler treats source code — pre-process once, run fast forever.

The cost of compiling at write time is that mistakes compile in too — one misunderstanding can
propagate across every page linking it. That is why `lint` is a first-class operation, why every
claim cites a summary, and why every summary records the raw lines it came from.

→ **[docs/what-is-an-llm-wiki.md](docs/what-is-an-llm-wiki.md)** — the long version, and the
four places the design guards against that failure mode.

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

Two conventions carry weight. **Wanted pages**: a link to a page that does not exist yet is a
TODO, not an error — the viewer lists who links to each one, so red links become the ingest
queue. **`(unverified)`**: model knowledge is allowed only when marked and collected under a
`## To verify` heading, which is the best planning tool in the wiki — the next sources are picked
to retire the markers.

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
- **Browse** by type, kind, facet or tag, a **health** page mirroring lint, and **sources** —
  every raw file as a numbered, line-addressable page, which is what makes citations clickable.

Everything topic-specific — page types and their folders, entity kinds, facets, TOC tables,
cheat-sheet rules — is data in `wiki.json`, never code. See `docs/wiki-json.md`.

## What is in here

Three parts: **`template/`** — the wiki you get, copied verbatim, with everything topic-specific
living in `wiki.json` rather than in code. **`tools/`** — create a wiki, push tool improvements
into existing ones, self-test. **`reference/`** — a real 654-page wiki's rulebook, index, sources
manifest and configuration as a worked example, never copied into a new wiki.

→ **[docs/repo-layout.md](docs/repo-layout.md)** — the full tree, and how to keep several wikis
in sync as the tools improve. **[docs/wiki-json.md](docs/wiki-json.md)** — the config schema.

## License

MIT — see `LICENSE`.
