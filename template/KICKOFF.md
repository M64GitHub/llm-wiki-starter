# Kickoff — the first session of this wiki

This file exists only until the wiki is set up. `CLAUDE.md` says: if `KICKOFF.md`
exists, follow it first. You (Claude Code) run this procedure in the folder that
contains this file — or, when started from the `llm-wiki-starter` repo's
`new wiki` operation, in the wiki folder you were given; every path below is
relative to that wiki root. Work in the user's language.

The goal: leave behind a configured, topic-specific wiki with an agreed page
model, a rulebook that reads as if written for this topic, a first list of
sources, and a plan — so the very next command can be `ingest …`.

## 1. Orient

- Read `CLAUDE.md`, `wiki.json`, `README.md`, `wiki/index.md` as they are now.
- Tell the user in two sentences what an LLM wiki does with their sources and
  that you will ask a handful of questions, then configure everything.

## 2. Interview

Ask in small batches (use the question tool when available, otherwise plain
questions). Offer a concrete default for every question so the user can just
say "yes"; recommend when you have an opinion. Skip what the user already told
you. Record the answers — they go into `inbox/kickoff-<date>.md` at the end.

**A. Topic and purpose**
1. What is the wiki about, in one or two sentences? What is explicitly out of scope?
2. What does the reader want to *do* with it — create things (how-to focus), understand a field, track a moving landscape, make decisions? Who reads it: just the owner, a team, the public?
3. What are the 2–5 main sub-areas or pillars? (In the chiptune reference wiki these were the platforms: C64/SID, Game Boy, PC trackers.)

**B. Page model** — propose, then confirm
4. Propose page types for *this* topic. Start from the defaults — how-to
   (`technique`), `concept`, `entity` (with kinds), `summary` — and adapt the
   names and the kinds to the topic. Examples: an AI-models wiki might use
   `technique` (prompting / evaluation / fine-tuning how-tos), `concept`,
   `entity` with kinds `model`, `lab`, `harness`, `benchmark`, `paper`,
   `person`, `event`, plus `summary`; a cooking wiki might use `recipe`,
   `technique`, `concept`, `entity` (`ingredient`, `tool`, `cuisine`, `person`,
   `book`). Keep `summary` in every wiki — it is the citation anchor. Keep the
   number of types small (3–5); kinds carry the detail.
5. Is there a cross-cutting **facet** that most pages should carry — like
   `platforms` in the chiptune wiki (e.g. `models`, `languages`, `cuisines`,
   `eras`)? Propose the key and its values, or none.
6. Do **cheat sheets** make sense (pages of one kind that carry reference
   tables, plus per-tool `###` sections on how-to pages)? If yes, which type
   and kind (default: `entity` / `tool`) and which how-to type feeds them.

**C. Conventions**
7. Domain notation: how should values be written (units, code, versions,
   commands, symbols, names of models/tools)? Language of the wiki?
8. Anything special about verification for this field (fast-moving facts that
   need dates, benchmark numbers that need the exact version, …)?

**D. Sources**
9. What sources are already at hand — local files/folders, URLs, big
   collections that need triage (newsletters, forums, mailing lists, doc sets)?
10. What are the canonical references for the topic (manuals, specs, papers,
    books, communities, newsletters, podcasts)? Which 2–3 should be ingested
    first? What should be scouted?

**E. Site and habits**
11. Site name (default: the folder name in title case), a one-sentence tagline,
    and the short logo mark (default: the name in capitals).
12. Commit policy (default: never commit unless asked), whether to rebuild the
    viewer after every ingest (default: yes when the user is watching), and
    anything else about how the user likes to work.

## 3. Configure

Apply the answers. Do all of it, then show the tree.

1. **`wiki.json`** — name, mark, tagline, search placeholder/help, the `types`
   (id, folder, label, colour, description, kinds), `facets`, `cheatsheets`
   (or `null`), empty `tocs`/`raw_collections`. Colours: pick distinct names
   from cyan, amber, pink, green, violet, blue, lime, orange, teal, magenta.
2. **Folders** — create `wiki/<folder>/` for every type; remove default
   folders that are not used (they are empty).
3. **`CLAUDE.md`** — rewrite: the **Focus** paragraph (topic, scope, pillars,
   reader), the **Map** (real folders and types), **Domain notation**, the
   **Page templates** (one per chosen type, with sections that fit the topic),
   the ripple examples in **ingest** (which page types a typical source of
   this field touches), any field-specific verification rule. Delete the
   **First session** section and every `<!-- KICKOFF -->` comment. Keep the
   operations and boundaries; they are the same in every wiki.
4. **`README.md`** — the focus paragraph, the layout table (real folders), the
   viewer section, the renderer notes.
5. **`wiki/index.md`** — one `## <Type label>` group per type in the order of
   `wiki.json` (subgroups per kind for kinded types), a `## Summaries` group, a
   `## Wanted pages` section seeded with the 5–15 slugs the interview makes
   obvious (the pillars, the canonical tools/models/works), and the `## Inbox`
   section. `index.md` and `log.md` are the only pages that may exist without a
   source.
6. **`inbox/plan-first-ingests-<date>.md`** — the prioritized list of sources
   from the interview: what to ingest first (with paths/URLs), what to triage,
   what to scout, and the "done when" criteria. Copy local sources the user
   named into `raw/<collection>/` now and record them in `raw/sources.md`.
7. **Scout** — if the user wants and web access exists, run `scout <topic>`
   for the first pillar and write the scout file.
8. **Checks** — `python3 tools/lint.py` and `python3 tools/build-site.py`; open
   `site/index.html` for the user (or `--serve`). Fix anything they report.
9. **Log** — append a `## <date> — kickoff` entry to `wiki/log.md` listing the
   decisions.
10. **Record and remove** — write the interview answers and decisions to
    `inbox/kickoff-<date>.md`, then delete `KICKOFF.md`.
11. **Commit** — if the user agreed to commits, commit "Kickoff: configure the
    wiki for <topic>"; otherwise say the tree is ready to commit.

## 4. Hand over

End with: the page model in one table, the first three things to ingest as
literal commands (`ingest <path or url>`), and the open questions. Then wait —
the user's next message is usually the first ingest.
