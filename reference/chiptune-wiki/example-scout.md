# Scout: LSDj sound design (2026-08-30)

Candidates for step 1.3 of `inbox/plan-next-ingests-2026-08-30.md`. Wanted: concrete instrument and table recipes (kick, snare, hi-hat, wave-channel bass, `R`/`D`/`H` idioms), interviews with [[johan-kotlinski]], the LSDj FAQ. Gear and mod guides were skipped. Nothing here is ingested; pick by number.

**Status 2026-08-30:** candidate 1 partly ingested — articles 09, 10, 11, 13, 17, 18 → [[s-intense-tech-09-lets-table-this-discussion]], [[s-intense-tech-10-kicks-part-1]], [[s-intense-tech-11-kicks-part-2]], [[s-intense-tech-13-kotlinski-interview]], [[s-intense-tech-17-the-joys-of-noise]], [[s-intense-tech-18-adsr-makes-life-easier]]; then 01, 02, 06, 07 → [[s-intense-tech-01-wave-synth-deep-dive-part-1]], [[s-intense-tech-02-wave-synth-deep-dive-part-2]], [[s-intense-tech-06-groove-and-tick-tricks-part-1]], [[s-intense-tech-07-groove-and-tick-tricks-part-2]]; candidate 2 → [[s-infu-getting-started-with-lsdj]]; candidates 3, 4, 5, 6, 8 → [[s-chipmusic-lsdj-faq]], [[s-chipmusic-lsdj-advanced-tricks]], [[s-chipmusic-noise-drum-threads]], [[s-chipmusic-kotlinski-interviews]], [[s-chipmusic-tables-and-chords-threads]]. Later on 2026-08-30 the remaining Intense Tech articles 03, 04, 05, 08, 12, 14, 15, 16, 19, 20, 21 → [[s-intense-tech-03-dont-sleep-on-z]], [[s-intense-tech-04-liblsdj]], [[s-intense-tech-05-wave-cruncher-instrument-library]], [[s-intense-tech-08-dotcnts-wave-cruncher]], [[s-intense-tech-12-scoping-out-new-features]], [[s-intense-tech-14-lets-appreciate-version-8]], [[s-intense-tech-15-lets-mix-it-up-and-down]], [[s-intense-tech-16-cartridge-family]], [[s-intense-tech-19-new-noise-and-910-news]], [[s-intense-tech-20-lsdpatch]], [[s-intense-tech-21-whats-new-in-lsdj-92]] (the series has 21 published articles, not 22; an unlisted draft *22 Advanced Wave Tech* is an outline only — raw kept, not summarised); candidate 7 → [[s-sabrepulse-getting-started-with-lsdj]]; candidate 10's lsdjsynths repository is now described on [[lsdj-wave-cruncher]]. Still open: 9 (old manuals, version dating only).

Fetching notes: chipmusic.org returns 403 to the fetch tool but serves pages to `curl -A "Mozilla/5.0 …"`; defensemech.com and learnlsdj.github.io fetch normally; wiki.littlesounddj.com (named in the LSDj manual) does not answer any more, and its Fandom mirror (littlesounddj.fandom.com) blocks both fetchers.

## Ranked candidates

### 1. Defense Mechanism — *Intense Tech with Defense Mech* (LSDj tutorial series) ★★★
- URL: https://defensemech.com/intense-tech/ (English index; articles at `…/intense-tech/en/NN-<slug>.md.html`; also mirrored on the ChipWIN blog, chiptuneswin.com/blog/)
- 21 articles (the earlier count of 22 included an unlisted draft), 2018–2021, CC BY-NC-SA 4.0 ("unless otherwise noted"), written for LSDj 6–9. The best single source of concrete recipes found. Priority articles:
  - 09 *Let's Table This Discussion!* (2019-07-23) — envelope-column digits (volume + ticks, e.g. `36`), transpose `01–7F` up / `80–FF` down, nested `A` tables, `A20`+ to stop a table without killing the note, the even/odd-row trick when one automate instrument plays on two channels → [[instrument-tables]], [[wavetable-programming]]
  - 10 *Get Your Kicks with Version 6, part 1* (2019-10-29) and 11 *Kicks part 2: Kick Heaven in Version 7* — wave kicks (fast `P`, then `L` with transpose `80`, DRUM mode), a noise-attack "Kyoto" wave switched with `F01`, 808 kick-to-bass tables → [[instrument-design]]
  - 17 *The Joys of Noise* (2020-11-05) — noise kick (`S` sweeps `A5 → 93 → 91 → 90 → 80 …`, STABLE mode), `Z`-randomised crashes, pitched noise via `R80`–`R8F` → [[instrument-design]], [[retrigger]], [[randomization-and-probability]]
  - 18 *ADSR Makes Life Easier!* (2020-11-29) — the ADSR envelope of LSDj 8.1.0 and the software volume of 8.8.0, examples `54/00/--`, `03/A2/71`, `74/07/43` → [[adsr-envelope]]
  - 01–02 *Wave Synth Deep Dive* — SIGNAL / FILTER / Q / CUTOFF, then DIST / PHASE / VSHIFT / LIMIT → [[wavetable-programming]]
  - 06–07 *Groovy Groove and Tick Tricks* → [[shuffle-funktempo]]; 03 *Don't Sleep on Z* → [[randomization-and-probability]]; 15 *Let's Mix It Up (and Down)* → [[volume-slides]], [[stereo-panning]]
  - 13 *Interview with LSDj developer Johan Kotlinski* (2020-02-20) — LSDj released around 2000 for the Game Boy Color, written in assembly as his first big program; C64 / Amiga / ProTracker / Musicline background; alias "rolemodel"; milestones 1.4.0 dual-kit mixing, 3.0.0 file screen, 3.9.5 prelisten, 5.1.0 pitch engine → [[johan-kotlinski]], [[lsdj]] (resolves the `(unverified)` alias and date on the person page)
  - 12, 14, 19, 21 (features of versions 7 / 8 / 9.1.0 / 9.2), 20 (LSDPatch), 04–05, 08 (libLSDj, Wave Cruncher) → [[lsdj]] version history and tools; lower priority.
- Suggested unit: one summary per article (`s-intense-tech-NN-<slug>`), starting with 09, 10, 11, 17, 18, 13.

### 2. Infu — *Getting started with LSDj* ★★
- URL: https://learnlsdj.github.io/ (single page, 14 sections, zip download; CC BY-NC 4.0; redesign by Torsten Hansson)
- A structured beginner course: sections 05–10 cover commands, the noise channel (hi-hat / snare / kick settings), tables ("advances every 6 ticks by default"), instruments, WAV kicks, synthesis and KIT sampling. Less deep than #1 but systematic — a second source for the manual's drum recipes → [[instrument-design]], [[instrument-tables]], [[lsdj]], [[tracking-workflow]].

### 3. chipmusic.org — *LSDJ FAQ* ★★
- URL: https://chipmusic.org/forums/topic/543/lsdj-faq (thread started 2010-01-29, 6 pages)
- The community FAQ: clicks and how tables avoid them, chords via tables, common questions. Forum text — extract post by post with author and date, like the Lemon64 threads → [[lsdj]], [[instrument-tables]], [[chord-arpeggio]].

### 4. chipmusic.org — *LSDJ Advanced Tricks* ★★
- URL: https://chipmusic.org/forums/topic/8992/lsdj-advanced-tricks/ (2012-11-02, 2 pages)
- Trick collection (`G` inside a table to change its speed, table-driven sound design, `A` tables independent of the instrument) → [[instrument-tables]], [[retrigger]], [[fake-echo]].

### 5. chipmusic.org — *LSDJ Complete Drum Kit on Noise Channel* ★★
- URL: https://chipmusic.org/forums/topic/15681/lsdj-complete-drum-kit-on-noise-channel/ (2014-11-29)
- Noise-only kick / snare / hat recipes with instrument values; related thread *Noise snare* (https://chipmusic.org/forums/topic/15443/noise-snare/) — toned noise morphed into white noise with a quick `S`, FREE pitch mode → [[instrument-design]].

### 6. Kotlinski interviews on chipmusic.org ★
- *Johan Kotlinski Lost Interview from 2014* — https://chipmusic.org/forums/topic/16194/johan-kotlinski-lost-interview-from-2014 (posted 2015-03-11; originally written for Devise Magazine)
- *Interview With Johan Kotlinski* — https://chipmusic.org/forums/topic/6612/interview-with-johan-kotlinski/ (2012-02; questions for a school paper on Game Boy music history)
- Both short; useful for dates and motivations → [[johan-kotlinski]], [[lsdj]]. Candidate 1's article 13 is the better-edited interview; ingest that first and use these as cross-checks.

### 7. Sabrepulse — *Getting started with LSDJ* (mirror at Adventure Kid) ★
- URL: https://www.adventurekid.se/akrt/glossary/lsdj/sabrepulses-getting-started-little-sound-dj/
- A well-known artist's beginner tutorial; probably overlaps the manual, but a second voice on workflow → [[tracking-workflow]], [[lsdj]]. Not read in detail.

### 8. chipmusic.org — tables and chords ★
- *Any Specific Advice On Learning Tables (LSDJ)?* — https://chipmusic.org/forums/topic/16432/any-specific-advice-on-learning-tables-lsdj/ (2015-04-17, 2 pages)
- *LSDJ Chord Cheat Sheet* — https://chipmusic.org/forums/topic/15949/lsdj-chord-cheat-sheet/ (2015-01-20, 2 pages) — `C`-command values per chord type → [[chord-arpeggio]], [[diatonic-chords]].

### 9. Older LSDj manuals (version history) ○
- https://www.littlesounddj.com/lsd/latest/documentation/ — `LSDj_3_7_4.pdf` (2007-05-21), `LSDj_4_9_5.pdf`, `LSDj_2_2_5.pdf`, `LSDj_1_4_0.pdf`, `LSDj_1_3_5d.pdf`. Only for dating features (when `R8x` resync, the DRUM pitch mode or the synth appeared) → [[lsdj]]. Skim, do not ingest in full.

### 10. psgcabal/lsdjsynths — wave-channel synth patches ○
- https://github.com/psgcabal/lsdjsynths — patches converted with the LSDj Wave Cruncher (slap basses by tobokegao and others). Data rather than prose; at most a mention on [[wavetable-programming]].

## Lower-priority sightings

- Synthtopia, "Making Music On A Game Boy With LSDj" (2016-05-06) — news / video pointer; skip.
- MATRIXSYNTH (2013-07) and the chipmusic thread *LSDJ Video Tutorial – Combining Wav Kicks w/ Basses; Pre Snare Instr* (https://chipmusic.org/forums/topic/11228/) — video tutorials; the thread text may hold the recipe (making a WAV kick and a WAV bass start on the same downbeat, a "pre-snare" instrument).
- ohmnohmnohm.com, *LSDJ Pitch Control – Interview with gwEm* — a hardware pitch-control mod; gear, skip unless the wiki gets a hardware section.
- Retrovolve, Low-Gain interview part 3 — scene politics; skip.
- YouTube: *Sunday Jam* LSDj episode with Kotlinski (2021-06-13), the *LSDj Learning Lab* wave-channel playlist — video, no transcript fetched.
