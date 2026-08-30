# Plan: next ingests (temporary, written 2026-08-30)

Working plan for the next sessions, agreed with the owner on 2026-08-30. Delete this file when the steps are done. The maintainer rules in `CLAUDE.md` apply to every step: raw first, one summary per article/chapter, ripple into 5–15 pages, `python3 tools/lint.py`, `python3 tools/build-site.py`, log entry, no commit unless asked.

## State at the time of writing

- 126 pages; wanted (red) pages: `schism-tracker`, `s3m-format`, `mod-format`, `nes-2a03`, `amiga-paula`; 34 `(unverified)` markers across 30 pages (`python3 tools/lint.py` lists counts; `site/health.html` lists pages).
- Stubs: [[openmpt]], [[scream-tracker-3]], [[fasttracker-2]], [[protracker]], [[vice]] and ten TraxWeekly people pages (basehead, necros, psibelius, trixter, the-zapper, leviathan, maelcum, greg-heo, zinc, catspaw, pinion, the-modsquad, kosmic, hornet).
- Platform coverage: pc-tracker 45 pages, c64 39, gameboy 25 (all from the single LSDj manual source), amiga 4, nes 0.
- Last commit: `d6ab26f` (five SID sound-design sources). `inbox/scout-sid-sound-design-2026-08-30.md` has the SID leftovers.

## Step 1 — Game Boy depth (highest value)

1. **`scout lsdj sound design`** → `inbox/scout-lsdj-sound-design-<DATE>.md`. Look for: LSDj tutorials/threads with concrete instrument and table recipes (kick, snare, wave-channel bass, table tricks, `R`/`D`/`H` idioms), interviews with Johan Kotlinski, the LSDj wiki/FAQ. Skip gear/mod guides. The owner picks from the scout file.
2. **Ingest Pan Docs, audio chapter** — https://gbdev.io/pandocs/Audio.html (+ `Audio_Registers.html`, `Audio_details.html`; verify the exact page names on the site). Save as `raw/pandocs/*.md` or `.txt` (the source is Markdown on GitHub: gbdev/pandocs — fetch the rendered pages or the `src/Audio*.md` files). Ripple: [[game-boy-apu]] (register-level spec like [[sid]] now has), [[pulse-width-modulation]] (the four fixed duties — confirms an `(unverified)`), [[wavetable-programming]] (wave RAM: 32 × 4-bit samples), [[adsr-envelope]] (envelope units), [[retrigger]], [[randomization-and-probability]]/noise (LFSR 7/15-bit), [[stereo-panning]] (NR51), [[game-boy]]. Create `pan-docs` publication entity.
3. Ingest the owner's picks from the scout.

**Status 2026-08-30:** 1.1 done (`inbox/scout-lsdj-sound-design-2026-08-30.md`, 10 candidates — Defense Mechanism's *Intense Tech* series is the top pick); 1.2 done (Pan Docs audio section ingested: `raw/pandocs/`, three summaries, [[pan-docs]], [[game-boy-apu]] rewritten); 1.3 started: Intense Tech articles 09, 10, 11, 13, 17, 18 ingested (six summaries, [[intense-tech]], [[defense-mechanism]], [[johan-kotlinski]] rewritten, [[lsdj]] version history) ; then Intense Tech 01, 02, 06, 07, Infu's course and the chipmusic.org threads (FAQ, Advanced Tricks, noise drums, tables/chords, two Kotlinski interviews) — later the same day the remaining 11 Intense Tech articles (the series has 21, not 22) and Sabrepulse's tutorial (candidate 7) were ingested; candidate 10 is covered on [[lsdj-wave-cruncher]]; only candidate 9 (old manuals) remains open. Step 1 is done; Step 2 started on 2026-08-30.

Done when: [[game-boy-apu]] has a sourced register/feature table, Game Boy `(unverified)` markers are resolved or re-marked, and at least one non-manual source backs the LSDj technique sections.

## Step 2 — PC-tracker references

Goal: turn the four stubs into references and fill the three wanted format pages.

1. **OpenMPT manual** — https://wiki.openmpt.org/Manual:_Main_page (effect reference per format, format quirks, instrument/sample screens). It is many pages: ingest per chapter (`s-openmpt-manual-<chapter>`), starting with the effect reference and the "compatibility"/format pages. Ripple: [[openmpt]] (full cheat sheet), [[impulse-tracker]] (cross-check), [[it-format]], new [[s3m-format]], [[mod-format]], `xm-format`, plus every technique page's `### Impulse Tracker / OpenMPT` section.
2. **Scream Tracker 3 docs** — `ST3.DOC` and `TECH.DOC` from the ST 3.21 distribution (find a mirror: modland/archive.org; the owner may download it). Fills [[scream-tracker-3]] and [[s3m-format]].
3. **FastTracker 2 docs** — `FT2.DOC` from the FT2 distribution. Fills [[fasttracker-2]] and `xm-format`; confirms the "(unverified) MOD/XM use `0xy`" arpeggio note and FT2 volume-column panning.
4. **ProTracker manual** (PT 2.3 docs) → [[protracker]], [[mod-format]]; also touches [[amiga-paula]] if the manual describes the hardware (otherwise see step 5).
5. **Schism Tracker** — its docs/help (https://schismtracker.org/ → wiki/help; `schismtracker/schismtracker` on GitHub has docs) → new [[schism-tracker]] entity (a focus tool per `CLAUDE.md`).
6. Only IT docs exist locally (`~/space/docs`); `~/Downloads/OpenMPT-1/` has an OpenMPT install with `History.txt` (low value, skip unless a version fact is needed).

**Status 2026-08-30:** done — OpenMPT manual (8 chapters ingested, 6 more in raw), ST3.DOC + TECH.DOC, the FT2 2.08 manual (OCR), ProTracker 2.3 docs and the 2.3d help file, the Schism wiki and cmatsuoka's tracker-history notes are in; the four tools have cheat sheets, `s3m-format`, `mod-format`, `xm-format` and `schism-tracker` exist, the `0xy` and FT2-panning items are sourced. Not done: `amiga-paula` (no hardware source yet — see Step 5); the original FT2.DOC was not found (the manual stands in for it).

Done when: no stub among the four tools, `s3m-format` / `mod-format` / `schism-tracker` exist, and lint shows the arpeggio/`0xy` and FT2 panning items resolved.

## Step 3 — TraxWeekly: interviews and the remaining ★

1. `grep -n 'interview' inbox/traxweekly-toc.md` and match names against existing people pages (Basehead, Necros, Psibelius, Trixter, the Zapper, Leviathan, Maelcum, Zinc, Catspaw, Pinion, Greg Heo…). Ingest those interviews first — one summary per interview (`s-twNNN-interview-<person>`), ripple into the person page, group pages ([[kosmic]], [[hornet]]), tool and song pages.
2. Then the remaining ★ articles (63 not yet ingested; `grep '★' inbox/traxweekly-toc.md | grep -v 's-tw'`), grouped by theme like before: sampling/mixing, composing/theory, IT/FT2 tips, scene/history.
3. Tool: `python3 tools/extract-traxweekly-article.py` — edit its hard-coded `targets` list (issue|number|title) to pull articles into `inbox/tw-extracts/` (git-ignored) for reading. Re-run `python3 tools/triage-traxweekly.py raw/traxweekly inbox/traxweekly-toc.md` afterwards so the TOC's summary column links the new summaries.

**Status 2026-08-30:** done — 16 interviews (all matches for existing people pages, plus Five Musicians, Chuck Biscuits, Jugi, Skaven, the #trax mass interview and the newbie interviews) and all 63 ★ articles ingested or marked skipped (backlog 0): 53 new summaries in five themed batches (interviews; tracking tips/IT; theory; sampling/mixing/realism; scene/history/business), 19 new pages (`skaven`, `purple-motion`, `five-musicians`, `epinicion`, `phoenix`, `jugi`, `the-grey-note`, `gravis-ultrasound`, `lead-articulation`, `midi-in-trackers`, `serial-composition`, `sample-ripping`, `realism-in-tracked-music`, `reverb-and-compression`, `recording-samples`, `tracker-scene-history`, `compos`, `commercial-tracking`, `live-tracking`), every people page multi-sourced (Jugi single-sourced, stated). Open: the other ~45 interviews and the reviews (not ★; listed in the TOC), Necros's later "In Review" columns.

Done when: every person page has more than one source or a clearly stated single source, and the TOC shows the ★ backlog under 30.

## Step 4 — Cheap C64 confirmations (leftovers of the SID scout)

- **C64 Programmer's Reference Guide, ch. 4 + Appendix O**: HTML pages https://www.devili.iki.fi/Computers/Commodore/C64/Programmers_Reference/Chapter_4/page_184.html … page_207 (Appendix O's URL was not found — locate it from the contents page `page_iii.html` or use the commodore.ca PDFs, e.g. `c64-programmers_reference_guide-04-programming_sound.pdf`). Ripple: [[sid]], [[adsr-envelope]] (second, official source for the timing table), [[ring-modulation-and-sync]], [[filter-programming]].
- **HVSC SID file format doc** (`SID_file_format.txt` in HVSC's DOCUMENTS folder — verify the URL on hvsc.c64.org) → [[sid-format]] (PSID/RSID header) and [[hvsc]].
- **Linus Walleij, "A SID player routine"** — https://www.df.lth.se/~triad/krad/sidmidi.html → [[sid-player-routine]], [[hard-restart]] (it claims HR matters only on the 6581 — record the contradiction with the Lemon64 threads on the page and in the log).
- Local: `~/Downloads/SID-Wizard-1.7/manuals/Charts and Tables for SID-Wizard 1.6.pdf` — skim for cheat-sheet tables (extract with `swift tools/pdf-to-text.swift`); the 1.7 manual is near-identical to 1.8 (skip).
- chipmusic.org pages (e.g. "C64 Music for Dummies") return 403 to the fetch tool; `curl -A "Mozilla/5.0 …"` works — save the HTML into `raw/` and extract the post text (see the Lemon64 extraction in this session's log for the approach).

**Status 2026-08-30:** done — all five items ingested (`raw/c64-prg/`, `raw/mos-6581-datasheet/` standing in for Appendix O, `raw/hvsc/`, `raw/walleij/`, `raw/chipmusic/c64-music-for-dummies-t8104.txt`, `raw/sid-wizard/Charts-and-Tables-…`): six summaries, [[linus-walleij]] and [[c64-programmers-reference-guide]] created, 19 SID/C64 pages rippled; the ADSR timing table has its official source; the hard-restart "6581 only" contradiction is recorded on [[hard-restart]] and in the log. Appendix O itself is not transcribed on devili — the 6502.org datasheet PDF is the same text.

**Leftovers, 2026-08-30 (later the same day):** the two open items were ingested — the SID scout's low-priority leftovers (#9, #10 and the whole "also seen" list, incl. sidmusic.org's Yannes/Tel/Galway/Hubbard interviews and Alstrup's waveform pages: 15 summaries) and the 56 non-★ TraxWeekly interviews (55 summaries + the FITC "Complaints" article; five batches, then integration passes over the shared pages). Steps 1–4 are complete; only the optional step 5 remains, so this file can be deleted whenever the owner likes.

## Step 5 — Breadth (optional, only when the owner wants it)

- NESdev wiki APU pages (https://www.nesdev.org/wiki/APU and its sub-pages) → [[nes-2a03]].
- Amiga Hardware Reference Manual, "Audio Hardware" chapter (online at amigadev.elowar.com — verify) → [[amiga-paula]]; complements the ProTracker manual.

## Practicalities learned on 2026-08-30

- PDF text: `swift tools/pdf-to-text.swift in.pdf out.txt` (PDFKit; no pdftotext/pypdf on this Mac).
- Raw web pages: keep the extracted text (with a one-line header: title, URL, fetch date, extraction note) rather than HTML; record every collection in `raw/sources.md`.
- Never edit `raw/` after creation; the Latin-1/CP437 originals get a `-utf8.txt` sibling, which the viewer renders.
- After every ingest: `python3 tools/lint.py` (0 broken links, 0 orphans, all pages in `wiki/index.md`), `python3 tools/build-site.py` (rebuilds `site/`, git-ignored), and a log entry per source in `wiki/log.md`.
- The viewer's cheat-sheet page picks up any `kind: tool` entity with tables and every technique `###` heading that names a tool or one of its aliases — write new tool sections with the tool's exact name.
- Commit only when the owner asks (they did after each big step so far).
