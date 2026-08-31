# Lessons learned from the chiptune wiki (2026-08-30)

Notes from building the first wiki: 110 pages on day one, 476 by the end of the day, one
viewer. What held up, what we changed, and what a kickoff for the next topic should settle.

## What held up

- **The article is the unit of ingestion, not the file.** Newsletters, forum threads and manuals
  are bundles. One summary per article/chapter (`s-tw058-the-finishing-touches`) keeps
  citations precise and lets a 900-article archive be triaged instead of swallowed.
- **Summaries are the citation anchors.** Every claim on a technique/concept/entity page says
  `(source: [[s-…]])`. Because the summary page records `source-path`, the viewer links the
  claim → summary → raw line. Never skip the summary "to save time".
- **Raw is immutable, but derived copies are fine next to it** — `IT-utf8.txt` beside the CP437
  `IT.TXT`, `.txt` extracts beside PDFs, one-line provenance headers on scraped pages. The
  manifest `raw/sources.md` (one row per collection: origin, date, notes) is what makes the
  Sources page useful.
- **`(unverified)` + `## To verify`.** Model knowledge is allowed only when marked. It turned
  out to be the best planning tool: the next ingests were chosen to retire unverified markers,
  and the health page lists them.
- **Wanted pages as red links.** Linking to pages that don't exist yet (and listing the
  deliberate ones under `## Wanted pages` in the index) shows what to ingest next; the viewer
  gives each wanted slug a page listing who links to it.
- **Ripple is where the value is.** A manual touched 20 pages, an interview touched people,
  groups, tools and songs. A source that produces one summary and nothing else was ingested
  wrong. `tools/add-section.py` made the mechanical part cheap.
- **Tool pages carry cheat sheets; technique pages carry `### <Tool>` sections.** The viewer
  collects both into per-tool cheat sheets. The rule "one technique page, a section per tool"
  is what makes a multi-platform wiki readable.
- **Triage tables for big collections.** A script builds `inbox/<collection>-toc.md` (one row
  per article, keyword flags, a summary column that survives regeneration); the user picks
  rows; the viewer renders the table with filters. Write the script per collection — formats
  differ too much for a generic one.
- **Scout files with a status line.** `inbox/scout-<topic>-<date>.md` lists 5–10 fetched-and-
  skimmed candidates with flags and the pages they would touch; once ingested, a **Status**
  line maps candidates to summaries. Plans (`inbox/plan-…`) get "done when" criteria and a
  status per step and are deleted when finished.
- **The log is append-only and per operation**; the index is the catalog and is read first on
  every query. Both are cheap to maintain when done every time and impossible to reconstruct.
- **Lint after every ingest, build when the user looks.** `tools/lint.py` is mechanical (links,
  orphans, frontmatter, index coverage, unverified count); contradictions are read for. The
  health page mirrors lint in the viewer.
- **Memory across sessions**: a plan file in `inbox/` plus the log lets a fresh session (or a
  parallel one) continue without re-deriving state.

## What we changed along the way

- Started with the guide's `Raw/ Wiki/Entities/Concepts/Summaries` and "S - Title.md" names;
  moved to lowercase folders, slug filenames and a first-class `techniques/` type because the
  wiki is *about doing things*. Slugs made the web viewer trivial.
- Added `kind` to entities early (tool / chip / platform / format / person / group / event /
  publication / song) — the sidebar and browse pages depend on it.
- Added the `platforms` facet as a frontmatter list — the one cross-cutting axis every page
  has. Other topics will have a different one (or none); it is configuration now.
- Person pages started as stubs from mentions; the rule that settled it: create a page when a
  name appears in 3+ sources or has an article of its own, otherwise mention inline.
- The viewer grew from "render Markdown" to search with facets, backlinks, local graphs, cheat
  sheets, TOC tables, raw line anchors and a health page in one day — each feature answered a
  concrete "where is…" question while ingesting. Keep it dependency-free; it rebuilds in 1 s.

## What a kickoff must decide (see template/KICKOFF.md)

1. **Scope and pillars** — the 2–5 sub-areas that structure the index and the facet.
2. **Page types and kinds** — few types (3–5), kinds for the nouns; keep `summary`.
3. **The facet** — one cross-cutting list key, or none.
4. **Cheat sheets** — only if the topic has tools with commands/values worth tabulating.
5. **Notation** — how values are written (in chiptune: `$7F`, `C-4`, `3xx`, `0 3 7`); for an AI
   wiki: model ids with versions and dates, benchmark names with versions, prices with dates.
6. **Verification rules for the field** — what goes stale (prices, "current best", versions)
   and must carry a date.
7. **Sources at hand and canonical references** — copy local files into `raw/` at kickoff;
   list the big collections that need triage scripts.
8. **Habits** — commit policy, rebuild policy, language.

## The second lesson: consolidation (2026-08-31, at 676 pages)

Everything above is about getting material *in*. A day and 200 pages later the wiki had the
opposite problem, and the fix generalises better than anything in the ingest half.

- **Measure the layers before deciding what to do next.** 363 summaries against 61
  technique+concept pages — six inputs per page a reader actually opens. That ratio was the
  whole diagnosis, and it is one `ls | wc -l` per folder. The thinnest reader pages turned out
  to sit on the *best*-sourced topics.
- **Anywhere the wiki states the same fact twice, or states an intention, is a lint check
  waiting to be written.** Two came out of this and are now in `template/tools/lint.py`:
  **unlanded ripples** (a summary lists a page under `## Pages touched`; that page never cites
  the summary — the ingest stopped at the summary layer) and **citation drift** (`sources:` in
  the frontmatter and the `## Sources` section naming different sets). The first found 462
  claims across 133 pages and has driven six working sessions; the second found 35 pages the
  day it was written. Look for the redundancy in your own conventions and diff the halves.
- **A metric must not count its own reporting.** The unverified-marker count included `log.md`
  and `index.md` — files that *discuss* the markers — so every write-up about reducing it
  raised the number. Exclude the bookkeeping pages, or the metric is noise. (Fixed in the
  template.)
- **The list is a review list, not a defect list.** "Pages touched" sometimes means "relevant
  to". The rule that keeps the metric honest: decide *per summary* whether it is material or
  merely relevant, and for merely-relevant ones write one honest pointer sentence naming the
  page where the material really lives. Never manufacture a section to absorb a citation.
- **One page per sitting, top-down by count, and report before/after numbers every time.** Six
  sessions took it from 462 to 170. The numbers in the log are what let a fresh session pick it
  up without re-deriving the state.
- Six recurring shapes, now a checklist in the `consolidate` operation: a whole tool missing
  from a concept page; a forward reference never landed; primary research not reaching the
  reader page; a page with no *earliest* entry; a tool's changelog being a source about the
  technique; a tool page with its fans but not the reason people left it.

## Pitfalls

- Shell cwd drift once created a stray `wiki/raw/` tree: anchor writes to absolute paths.
- Sites that 403 plain fetchers need a browser User-Agent (`html-to-text.py` docs).
- PDF text extraction on macOS: `swift tools/pdf-to-text.swift` (PDFKit) — no pip needed.
- Article numbering in newsletters restarts per section; link TOC rows by title, not number.
- Keep topic words out of the tools; everything topic-specific belongs in `wiki.json` or the
  rulebook.
