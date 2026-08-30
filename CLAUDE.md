# llm-wiki-starter — rules for Claude Code

This repo is the template and toolkit for our LLM wikis (Karpathy's pattern). It is **not** a
wiki itself. Read `README.md` for the layout. Two jobs happen here: creating new wikis, and
maintaining the shared template/tools so every wiki works and looks the same.

## Operation: new wiki <path> [name]

1. Run `./new-wiki.sh <path> ["Name"]` (refuses non-empty targets). If the user gave only a
   topic, choose a slug like `<topic>-wiki` as a sibling of this repo and confirm it.
2. Then **run the kickoff for the new wiki without leaving this session**: read
   `<path>/KICKOFF.md` and follow it with `<path>` as the wiki root — every file you read or
   write is under `<path>`; run the tools as `python3 <path>/tools/lint.py` and
   `python3 <path>/tools/build-site.py`. Interview the user as KICKOFF.md says, apply the
   configuration, remove `<path>/KICKOFF.md` at the end, and hand over with the page model, the
   first three `ingest` commands and the open questions.
3. Do not copy anything topic-specific from `reference/` into the new wiki; use it as an example
   of the level of detail a rulebook and an index should reach.

## Operation: update tools <path>

`tools/update-tools.sh <path> --dry-run` first, show the summary, then without `--dry-run` if the
user agrees. Only `tools/` is touched. If the wiki has no `wiki.json`, offer to write one from
its actual folders and kinds (read a few pages) — the generator works without it but the site
will say "LLM Wiki".

## Operation: sync from <path>

Compare `<path>/tools/` with `template/tools/`; port improvements into the template, keeping it
topic-neutral (no topic words, no hard-coded folders, facets or collections — those belong in
`wiki.json`). Run `tools/selftest.sh` after every change to the template tools.

## Operation: selftest

`tools/selftest.sh`: creates a throwaway wiki, lints and builds it, and builds `../chiptune-wiki`
through the template generator with `reference/chiptune-wiki/wiki.json`. Must pass before a
commit that touches `template/tools/`.

## Maintaining the template

- `template/` must work for *any* topic: page types, kinds, facets, TOC tables and cheat-sheet
  rules are data in `wiki.json`; the rulebook's generic parts (conventions, operations,
  boundaries) stay identical across wikis; topic-specific text lives only behind
  `<!-- KICKOFF -->` markers that the kickoff replaces.
- `{{WIKI_NAME}}`, `{{WIKI_SLUG}}` and `{{DATE}}` are the only placeholders `new-wiki.sh` fills.
- The viewer's look and feel (`template/tools/site-assets/`) is shared by all wikis; per-type
  colours come from `wiki.json` (`assets/types.css` is generated). Change the stylesheet here,
  never in a wiki.
- `docs/wiki-json.md` documents every config key; update it when `load_config()` in
  `template/tools/build-site.py` changes.
- Keep `reference/` a faithful snapshot of the chiptune wiki's non-page files; refresh it
  deliberately (say so in the commit), don't let it drift.

## Boundaries

- Never edit a wiki's pages from here; only its `tools/`.
- Do not commit or push unless asked.
