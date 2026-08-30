---
title: Log
type: log
created: 2026-08-30
updated: 2026-08-30
---

# Log

Append-only. One entry per operation: date, operation, source, pages created / updated.

## 2026-08-30 — setup
- Created folder structure, `CLAUDE.md` rulebook, `README.md`, `raw/sources.md`.
- Adapted the LLM-wiki guide (natural20.com) for chiptune: added `techniques/` as a first-class page type, `kind` for entities, slug filenames, per-article ingestion for multi-article sources, `triage` and `scout` operations.

## 2026-08-30 — ingest: SID-Wizard 1.8 User Manual (`raw/sid-wizard/SID-Wizard-1.8-UserManual.txt`)
- Summary: [[s-sid-wizard-manual]].
- Created entities: [[sid-wizard]] (with full cheat sheet), [[sid]], [[commodore-64]], [[hermit]], [[goattracker]], [[vice]], [[sid-format]].
- Created concepts: [[tracker]], [[instrument-tables]], [[adsr-envelope]], [[sid-player-routine]], [[orderlist]].
- Created techniques: [[hard-restart]], [[filter-programming]], [[wavetable-programming]], [[ring-modulation-and-sync]], [[multispeed]]; SID-Wizard sections in [[chord-arpeggio]], [[vibrato]], [[pitch-slide-and-portamento]], [[pulse-width-modulation]], [[shuffle-funktempo]], [[detune]], [[fake-echo]], [[octave-bass]], [[instrument-design]].
- Skipped: nothing; the whole manual is in scope. Key/menu minutiae only partially reproduced (cheat sheet keeps the most-used keys).

## 2026-08-30 — ingest: 0 3 7 lab (`raw/037-lab/037-lab-techniques-and-theory.md`, `raw/037-lab/README.md`)
- Summary: [[s-037-lab]].
- Created entities: [[037-lab]], [[openmpt]], [[impulse-tracker]] (stubs for the last two).
- Created concepts: [[semitone-math]], [[scales-and-modes]], [[diatonic-chords]], [[chord-inversions]], [[chord-progressions]], [[melody-writing]], [[rhythm-and-groove]], [[arrangement]].
- Created techniques: [[chord-arpeggio]], [[vibrato]], [[pitch-slide-and-portamento]], [[pulse-width-modulation]], [[detune]], [[fake-echo]], [[octave-bass]], [[sidechain-pump]], [[channel-interleaving]], [[instrument-design]].
- Open question for the owner: what "DUET" (the `DUET SW` clipboard target) is.

## 2026-08-30 — triage: TraxWeekly archive (`raw/traxweekly/`, 128 files, 5.6 MB)
- Downloaded all issues from https://resources.openmpt.org/traxweekly/ plus the archive index text; summary [[s-traxweekly-archive]], entity [[traxweekly]].
- Generated `inbox/traxweekly-toc.md`: 909 articles, 89 flagged ★ by title keywords. Nothing ingested yet — the owner picks articles.
- Note: `TW-ART1..7.TXT` are ASCII-art logo files, not articles.

## 2026-08-30 — lint
- 45 pages, 0 broken links apart from the 11 intentional "wanted" red links in the index, 0 orphans, all frontmatter valid, 28 `(unverified)` markers across 23 pages awaiting sources (mostly LSDJ/IT commands and SID hardware details).

## 2026-08-30 — ingest: Little Sound Dj v9.2.6 manual (`raw/lsdj/LSDj_9_2_6.pdf`)
- Downloaded the PDF, extracted text with a PDFKit script (`raw/lsdj/LSDj_9_2_6.txt`). Summary: [[s-lsdj-manual]].
- Created entities: [[lsdj]] (screens, instruments, tables, grooves, synth, full command table, workflow, live mode), [[game-boy]], [[game-boy-apu]], [[johan-kotlinski]]. Created concept: [[sync]]. Created techniques: [[retrigger]], [[randomization-and-probability]], [[stereo-panning]].
- Rippled `### LSDj` sections into [[chord-arpeggio]], [[vibrato]], [[pitch-slide-and-portamento]], [[pulse-width-modulation]], [[shuffle-funktempo]], [[fake-echo]], [[detune]], [[instrument-design]], [[wavetable-programming]], [[sidechain-pump]], [[instrument-tables]], [[orderlist]], [[tracker]], [[arrangement]], [[rhythm-and-groove]], [[adsr-envelope]]; replaced the earlier `(unverified)` LSDJ notes with sourced ones.
- Skipped: appendix B allophone list and appendix C SRAM memory map (reference material, in raw), sample-kit history blurbs beyond the kit names.

## 2026-08-30 — ingest (basics only): DUET README (`raw/duet/README.md`)
- Summary: [[s-duet-readme]]. Created entity [[duet]]. Updated [[037-lab]] (DUET question resolved), [[sid-wizard]] (1.97 / `.swq` exist), [[hermit]], [[impulse-tracker]] (`ITTECH.TXT`), [[openmpt]] (clipboard shared with Schism/DUET).
- Per the owner: DUET's docs are not ingested for now.

## 2026-08-30 — ingest: TraxWeekly practical articles (34 articles from 24 issues)
- Articles: Modal and Chord Theory (#1), Beginning the Tracking Experience (#3), The Death of the Chiptune / Chiptunes Aren't Dead! (#37–38), Chord Theory? / Chord What? ×2 (#39–40), Panning / Panning? Hello? (#55–56), Tracking Hints (#59), Motherboard Sampling (#74), Introduction to Musical Theory vols 1–5 (#74, 76, 79, 81, 86), IT Percussion Tips (#75), Realism in MODs (#76), A Chip Off the Block I–II + Chiptune Seminar 3–4 (#77, 78, 80, 81), General Tracking Tips (#77), Impulse Tracker Tip of the Week #1–8 (#81–89) + More Impulse Tracker Tips (#83), A Little Panning (#106; #107 is a reprint).
- Skipped: "Bass: A Perspective" (#5) — a recruitment ad for a group called Bass; the Modsquad's parts 3–4 except their chord list; ads and closing sections.
- Summaries (14, series and debates grouped): [[s-tw001-modal-and-chord-theory]], [[s-tw003-beginning-the-tracking-experience]], [[s-tw037-death-of-the-chiptune-debate]], [[s-tw039-chord-theory-debate]], [[s-tw055-panning-debate]], [[s-tw059-tracking-hints]], [[s-tw074-motherboard-sampling]], [[s-tw074-intro-to-musical-theory]], [[s-tw075-it-percussion-tips]], [[s-tw076-realism-in-mods]], [[s-tw077-chip-off-the-block]], [[s-tw077-general-tracking-tips]], [[s-tw081-it-tip-of-the-week]], [[s-tw106-a-little-panning]].
- Created: concept [[chiptune]], [[tracking-workflow]]; techniques [[chip-samples]], [[new-note-actions]], [[sample-offset]], [[instrument-envelopes]]; entities [[jeffrey-lim]], [[pinion]], [[greg-heo]], [[zinc]], [[trixter]], [[basehead]], [[maelcum]], [[necros]], [[psibelius]], [[leviathan]], [[the-modsquad]], [[kosmic]], [[hornet]], [[20-minute-chip-compo]], [[scream-tracker-3]], [[fasttracker-2]], [[protracker]].
- Rewritten: [[impulse-tracker]] (author, features, command cheat sheet), [[traxweekly]] (staff, distribution, ingested list).
- Rippled: [[vibrato]], [[pitch-slide-and-portamento]], [[chord-arpeggio]], [[stereo-panning]], [[fake-echo]], [[randomization-and-probability]], [[tracker]], [[melody-writing]], [[arrangement]], [[rhythm-and-groove]], [[diatonic-chords]], [[chord-inversions]], [[scales-and-modes]], [[semitone-math]], [[chord-progressions]], [[instrument-design]], [[detune]], [[adsr-envelope]]. Several earlier `(unverified)` IT/S3M command notes are now sourced.
- Next candidates found while reading: Catspaw's frames-and-tempo articles (#58–59), "Perfect Samples: The Piano" (#84), "Wrecking Samples with Impulse Tracker" and "Hexadecimal 101" (#86), "Loops and Extended Samples" (Zapper, #25), "Impulse Tracker v1.01" (#42), Necros's "What it's like to be a PC Musician" (#5), and a possible vol. 6 of Greg Heo's series.

## 2026-08-30 — ingest: TraxWeekly candidate articles (8 articles) + Impulse Tracker docs
- TraxWeekly: What it's like to be a PC Musician (#5, Necros), Impulse Tracker v1.01 (#42, Pulse), The Finishing Touches parts 1–2 (#58–59, Catspaw), Perfect Samples: The Piano (#84, Sklathill), Hexadecimal 101 and Wrecking Samples with Impulse Tracker (#86), Loops and Extended Samples (TW.025, The Zapper). No vol. 6 of Greg Heo's theory series exists; instead the TOC shows the Modsquad's "Music Theory: A Modern Approach" (#87–97) and Zinc's "Layman's Music Theory" (#107) as further candidates. Summaries: [[s-tw005-what-its-like-to-be-a-pc-musician]], [[s-tw042-impulse-tracker-v1-01]], [[s-tw058-the-finishing-touches]], [[s-tw084-perfect-samples-the-piano]], [[s-tw086-hexadecimal-101]], [[s-tw086-wrecking-samples-with-impulse-tracker]], [[s-tw025-loops-and-extended-samples]].
- Impulse Tracker docs (`raw/impulse-tracker/`): `IT.TXT` manual and `HINTS.TXT` ingested in full ([[s-it-manual]], [[s-it-hints]]); `ITTECH.TXT` at the semantic level only — volume/slide/pan formulas, instrument fields, channel allocation ([[s-ittech]]); byte layouts stay in raw per the owner's note that it is a technical reference.
- Created: [[it-format]], [[catspaw]], [[the-zapper]]; techniques [[song-init-and-looping]], [[volume-slides]], [[sample-looping]], [[multisampling]]. Rewritten: [[impulse-tracker]] as a full reference (screens, complete effect table, editing keys, samples, instruments, song variables, community knowledge).
- Rippled into [[necros]] (real name now sourced), [[jeffrey-lim]], [[psibelius]], [[tracker]], [[retrigger]], [[arrangement]], [[chiptune]], [[scream-tracker-3]], [[fasttracker-2]], [[hornet]], [[traxweekly]], [[chip-samples]], [[stereo-panning]], [[fake-echo]], [[detune]], [[vibrato]], [[pitch-slide-and-portamento]], [[chord-arpeggio]], [[randomization-and-probability]], [[instrument-envelopes]], [[new-note-actions]], [[sample-offset]], [[tracking-workflow]], [[instrument-design]], [[volume-slides]].
- Remaining TraxWeekly candidates: Basehead's tracking tips (#15, cited by Catspaw), Catspaw's "Real Music" (#53) and interview (#57), "The Importance of Music Theory" (#7), Modsquad "Music Theory: A Modern Approach" (#87–97), Zinc "Layman's Music Theory" (#107), Necros's reviews.

## 2026-08-30 — query: clean, punchy SID bass without clicks
- Consulted: [[hard-restart]], [[adsr-envelope]], [[instrument-tables]], [[wavetable-programming]], [[pulse-width-modulation]], [[filter-programming]], [[octave-bass]], [[instrument-design]], [[ring-modulation-and-sync]], [[sid]]; grep of `raw/` for "click"/"bass" (TraxWeekly only covers sample clicks — not relevant to the SID).
- Answered from the wiki: hard-restart settings (ADHR, timer, type, frame-1 waveform), gate-off / legato in patterns, envelope + short pitch-drop table + 25 % pulse or filtered waveform for punch. General-knowledge additions (typical ADHR/timer values, ADSR-bug explanation, test-bit phase reset) marked unverified.
- Offered to save the synthesis as a technique page (`sid-bass-design`); not created yet.

## 2026-08-30 — scout: SID sound design
- Wrote `inbox/scout-sid-sound-design-2026-08-30.md`: 10 ranked candidates (GoatTracker 2.72 readme, WitchMaster's *Creating Chip Tunes with SID-Wizard*, Chordian's SID Factory II instruments tutorial, two Lemon64 ADSR/hard-restart threads, Linus Walleij's SID player notes, C64 Programmer's Reference Guide ch. 4, chipmusic.org "C64 Music for Dummies", Newman's *Driving the SID chip*, a Lemon64 resource thread, Furnace's C64 docs) plus 7 lower-priority sightings. Nothing ingested.
- Noted a contradiction to check on ingest: Walleij says hard restart matters only on the 6581; the Lemon64 threads describe the envelope lockup generically.
- chipmusic.org blocks non-browser fetchers (curl with a browser UA works); sidmusic.org was unreachable.

## 2026-08-30 — ingest: GoatTracker v2.72 readme (`raw/goattracker/goattracker-2.72-readme.txt`)
- Fetched from the leafo/goattracker2 GitHub mirror; Latin-1 original plus a UTF-8 copy. Summary: [[s-goattracker-readme]].
- Created: [[lasse-oorni]]. Rewrote [[goattracker]] from a stub into a full reference (keys, commands, instrument parameters, four tables, tick schedule, hard restart, packer options).
- Added `### GoatTracker` sections to [[hard-restart]], [[wavetable-programming]], [[pulse-width-modulation]], [[filter-programming]], [[chord-arpeggio]], [[vibrato]], [[pitch-slide-and-portamento]], [[multispeed]], [[shuffle-funktempo]], [[octave-bass]], [[instrument-design]]; GoatTracker sections in [[instrument-tables]], [[orderlist]], [[sid-player-routine]], [[adsr-envelope]]; waveform bits and routing in [[sid]], [[ring-modulation-and-sync]]; notes in [[tracker]], [[vice]], [[sid-format]], [[tracking-workflow]], [[sid-wizard]].
- Skipped: the byte-level `.SNG`/`.INS`/SFX file-format sections and the version history beyond the value-changing notes.

## 2026-08-30 — ingest: Creating Chiptunes with SID-Wizard, 2nd edition (`raw/sid-wizard/Creating-Chiptunes-with-SID-Wizard-2nd-edition.pdf`)
