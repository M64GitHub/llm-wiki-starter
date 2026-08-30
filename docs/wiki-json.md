# wiki.json — the wiki's configuration

Read by `tools/build-site.py` and `tools/lint.py` in every wiki. Every key has a default, so a
missing `wiki.json` still builds (as "LLM Wiki" with the four default page types). The kickoff
writes it; edit it by hand whenever the page model grows.

```json
{
  "name": "Chiptune Wiki",              // site title; <title> suffix, hero heading
  "mark": "CHIPTUNE WIKI",              // logo text in the top bar (default: name in capitals)
  "tagline": "How to make chip music …",   // hero paragraph on the home page (optional)
  "search_placeholder": "search pages, cheat sheets, TraxWeekly articles…",   // optional, generated otherwise
  "search_help": "hex and tracker notation search as typed (<code>$0E</code>)", // extra HTML in the search help line

  "types": [                            // page types, in display order; each has a folder under wiki/
    {"id": "technique", "folder": "techniques", "label": "Techniques", "color": "cyan",
     "description": "how-to pages"},    // description is documentation only
    {"id": "concept",   "folder": "concepts",   "label": "Concepts",   "color": "amber"},
    {"id": "entity",    "folder": "entities",   "label": "Entities",   "color": "pink",
     "kinds": [{"id": "tool", "label": "Tools"}, {"id": "person", "label": "People"}]},   // sub-kinds: frontmatter `kind`
    {"id": "summary",   "folder": "summaries",  "label": "Summaries",  "color": "green", "prefix": "s-"}
  ],
  "facets": [                           // extra list-valued frontmatter keys shown as chips and search filters
    {"key": "platforms", "label": "Platforms",
     "values": {"c64": "C64 / SID", "gameboy": "Game Boy"}}   // value -> label; unknown values still work
  ],
  "cheatsheets": {                      // null to disable
    "type": "entity", "kind": "tool",   // which pages are "tools"
    "heading": "cheat sheet",           // a ## heading starting with this is the page's own reference part …
    "skip_headings": ["related", "sources", "to verify"],   // … otherwise all ## sections except these
    "skip_prefixes": ["features"],
    "section_type": "technique",        // pages whose ### headings name a tool contribute those sections
    "generic": {"slug": "generic-trackers", "title": "Generic / PC trackers", "match": "tracker"},   // catch-all sheet (optional)
    "description": "…"                  // intro text on the cheat-sheets page (optional)
  },
  "tocs": [                             // Markdown tables in inbox/ rendered as filterable, sortable pages
    {"file": "inbox/traxweekly-toc.md", "id": "tw", "title": "TraxWeekly — table of contents",
     "nav": "TraxWeekly", "label": "TW article",       // nav = top-bar item and search group; label = badge
     "collection": "traxweekly", "file_column": "issue",   // rows link into raw/<collection>/<file-column value>
     "num_column": "#", "title_column": "title",           // the title links to the article anchor with that number
     "flags_column": "flags", "summary_column": "summary", "star": "★",   // flags become chips; a non-empty summary = ingested
     "meta_columns": ["issue", "date", "author", "flags"], // shown under search results
     "filters": [{"flag": "★", "label": "★ know-how"}, "interview", "review"],   // filter buttons
     "facets": {"platforms": ["pc-tracker"]}}            // facet values given to every row in search
  ],
  "raw_collections": {                  // per raw/<collection>/ folder: titles, dates and article anchors
    "traxweekly": {
      "name_pattern": "TRAXWEEK\\.(\\w+)", "title": "TraxWeekly #{n}",   // {n} = group 1 without leading zeros, {name} = file name
      "dates_file": "archive-index.txt",                               // a file in the collection listing dates …
      "dates_pattern": "(TRAXWEEK\\.\\w+)\\s*\\([\\d.]+ kB\\)\\s*([^\\n]+)",  // … as (file name, date) pairs
      "article_pattern": "^\\s*-{1,3}\\s*\\[\\s*(?:(?P<num>\\d+)[.)]\\s*)?(?P<title>[^\\]]+?)\\s*\\]",   // named groups num/title
      "skip_until": "\\[\\s*contents\\s*\\]"                            // ignore matches before this line
    }
  },
  "stub_words": 180,                    // pages shorter than this count as stubs on the health page
  "wanted_heading": "## Wanted pages"   // lint: the index section listing intentional red links
}
```

Notes

- `types[].id` is what `type:` in frontmatter must say; the folder maps files without a `type` to
  it. Colours: `cyan amber pink green violet blue lime orange teal magenta grey` or a hex value.
- A type with `kinds` gets one sidebar group per kind and a `kind:` search filter; lint requires
  `kind:` on its pages.
- Facet keys are read from frontmatter as lists (`platforms: [c64, gameboy]`); they appear on the
  meta strip, on the Browse page and as `platforms:c64` in search.
- TOC tables: the first Markdown table in the file is used; column names are matched
  case-insensitively; columns not named in the config are shown as text.
- `raw_collections` is optional; without it a raw file is shown with its file name and no article
  anchors. Patterns are Python regexes (escape backslashes in JSON).
- Reference example: `reference/chiptune-wiki/wiki.json`.
