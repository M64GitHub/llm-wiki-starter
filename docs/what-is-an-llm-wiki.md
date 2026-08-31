# What an LLM wiki is

The pattern is Andrej Karpathy's: **the human curates sources and asks questions; the agent does
everything else** — summarizing, cross-referencing, keeping the whole thing consistent, and the
bookkeeping. The wiki is the codebase, the agent is the programmer, the viewer is just the IDE.

What comes out is a folder of plain Markdown pages with `[[wikilinks]]` and YAML frontmatter,
next to the immutable original sources they were written from. Nothing about it is locked to one
tool: it opens in Obsidian, in the viewer this repo generates, or in anything else you write.

The rest of this page is about what the pattern is *not*, because the useful part is in the
contrasts.

## Not a second brain

A second brain — PARA, Zettelkasten, a hand-built Obsidian vault — is written *by* a human *for*
that human's later recall. The LLM wiki flips the division of labor. Instead of you maintaining
a knowledge base and occasionally asking an AI questions about it, the agent builds and
maintains the entire knowledge base, and you spend your attention on what enters it and what you
want to know.

Same substrate (Markdown, wikilinks, Obsidian-compatible), same goal (knowledge that
accumulates), different author.

There is a second difference that matters more than it sounds: a second brain is *personal* by
definition — it is organized around your projects, your areas, your recall. A topic wiki has
nothing to do with you. It is about the domain, and it would be just as useful to anyone else
working in that domain. A second brain is one thing you *could* build with this pattern; it is
not what the pattern is.

## Adjacent to a skill, on a different axis

Skills and wikis rhyme structurally. Both are progressive-disclosure filesystems: the agent
reads a short index or description first, then loads only the files it actually needs. Neither
tries to hold everything in context at once.

But they sit on different axes:

| | skill | wiki |
|---|---|---|
| holds | *know-how* — procedures | *know-what* — facts about a domain |
| written by | a human, mostly once | the agent, continuously |
| changes when | you change the procedure | a new source lands |
| grows | rarely | every ingest |

A static "how to configure X" skill rots as X moves. A wiki about X keeps absorbing the new
sizing tables, the new defaults and the gotchas people hit last month.

The strongest combination is both: a skill that tells an agent how to consult and maintain a
*particular* wiki — the librarian's procedures next to the library.

## Not RAG

This is the sharpest contrast, and the one that explains why the pattern compounds.

RAG retrieves chunks at query time. Every question starts from the raw corpus, so the model
rediscovers the domain from scratch each time, and nothing it works out survives the answer.
Ask the same question twice and the second answer costs exactly as much as the first.

A wiki moves that work to **write time**. The reading, the synthesis, the contradictions found
between two sources, the cross-links drawn between pages — all of it happens once, when the
source is ingested, and is saved. Knowledge treated the way a compiler treats source code:
pre-process once, run fast forever.

That is also why *ripple* is the operation that matters. A source that produces one summary and
changes nothing else was ingested wrong; the value is in the 5–15 pages it should have updated.

## The failure mode

Because the agent compresses sources into pages, one misunderstanding can propagate quietly
across every page that links to it. This is the real cost of doing synthesis at write time —
mistakes are also compiled in.

The design answers it in four places, and they are worth keeping even when they feel like
overhead:

- **Every claim cites a summary page**, and every summary records the `source-path` it was
  written from. The chain claim → summary → original lines is walkable, by you and by the agent.
- **`raw/` is immutable.** The original text is always there to check against, and the viewer
  renders every raw file as a numbered, line-addressable page so a citation is one click from
  its evidence.
- **`(unverified)` markers.** The agent may add general knowledge only when it marks it, and
  such items collect under a `## To verify` heading — which doubles as the best planning tool in
  the wiki, since the next sources get chosen to retire the markers.
- **`lint` is a first-class operation**, not a nicety: broken links, orphans, contradictions
  between pages, stale claims, index gaps, unverified items a new source could now confirm.

None of that removes the need to spot-check generated pages against the raw text they came from.
The chain exists to make that cheap, not unnecessary.

## When it is worth building one

Roughly: when the topic is one you keep coming back to, when sources keep arriving rather than
being read once, and when you want more than one session — or more than one person — to start
from what is already established instead of re-deriving it. A wiki you ingest into three times
and abandon is worse than a folder of bookmarks. One you feed for a week starts answering
questions you would not have thought to ask it.
