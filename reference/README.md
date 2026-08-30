# reference/ — the chiptune wiki as a worked example

Snapshot of the non-page files of `../chiptune-wiki` (taken 2026-08-30, 476 pages) plus a few
real pages. Use it to see what a finished rulebook, index, sources manifest, scout file and
plan look like, and how the generic viewer is configured for a specific topic. Nothing here is
copied into new wikis by `new-wiki.sh`.

| file | what to learn from it |
|---|---|
| `chiptune-wiki/CLAUDE.md` | a rulebook after the topic is baked in: focus, notation rules, page templates with per-tool sections, triage scripts |
| `chiptune-wiki/wiki.json` | the full configuration: four types, nine entity kinds, a `platforms` facet, cheat sheets, the TraxWeekly TOC table and raw-collection anchors |
| `chiptune-wiki/index.md` | a 400-line catalog: groups per type and kind, summaries grouped by collection, wanted pages |
| `chiptune-wiki/sources.md` | the raw manifest after 40 collections |
| `chiptune-wiki/README.md` | the human intro incl. viewer feature list and renderer notes |
| `chiptune-wiki/example-scout.md` | a scout file with a status line mapping candidates to summaries |
| `chiptune-wiki/example-plan.md` | a multi-step ingest plan with "done when" criteria and status |
| `chiptune-wiki/log-excerpt.md` | the first log entries |
| `chiptune-wiki/triage-traxweekly.py`, `extract-traxweekly-article.py` | a collection-specific triage TOC builder and article extractor (the pattern to copy for newsletters/forums) |
| `example-pages/hard-restart.md`, `chord-arpeggio.md` | technique pages: what / why / how per tool / tips / related / sources |
| `example-pages/chiptune.md` | a concept page that became the hub of the wiki |
| `example-pages/lsdj.md`, `jeffrey-lim.md` | a tool page with a full cheat sheet; a person page |
| `example-pages/s-lsdj-manual.md`, `s-tw058-the-finishing-touches.md` | summaries of a manual and of a two-part newsletter article |
| `lessons-learned.md` | what the first days taught us; the decisions a kickoff should make |
