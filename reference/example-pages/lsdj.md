---
title: LSDj (Little Sound Dj)
type: entity
kind: tool
platforms: [gameboy]
tags: [gameboy, tracker, editor]
aliases: [LSDJ, Little Sound Dj, Little Sound DJ]
sources: [s-lsdj-manual, s-pandocs-audio-registers, s-pandocs-audio-details, s-intense-tech-09-lets-table-this-discussion, s-intense-tech-10-kicks-part-1, s-intense-tech-11-kicks-part-2, s-intense-tech-13-kotlinski-interview, s-intense-tech-17-the-joys-of-noise, s-intense-tech-18-adsr-makes-life-easier, s-intense-tech-01-wave-synth-deep-dive-part-1, s-intense-tech-02-wave-synth-deep-dive-part-2, s-intense-tech-06-groove-and-tick-tricks-part-1, s-intense-tech-07-groove-and-tick-tricks-part-2, s-infu-getting-started-with-lsdj, s-chipmusic-lsdj-faq, s-chipmusic-lsdj-advanced-tricks, s-chipmusic-noise-drum-threads, s-chipmusic-tables-and-chords-threads, s-chipmusic-kotlinski-interviews, s-intense-tech-03-dont-sleep-on-z, s-intense-tech-04-liblsdj, s-intense-tech-05-wave-cruncher-instrument-library, s-intense-tech-08-dotcnts-wave-cruncher, s-intense-tech-12-scoping-out-new-features, s-intense-tech-14-lets-appreciate-version-8, s-intense-tech-15-lets-mix-it-up-and-down, s-intense-tech-16-cartridge-family, s-intense-tech-19-new-noise-and-910-news, s-intense-tech-20-lsdpatch, s-intense-tech-21-whats-new-in-lsdj-92, s-sabrepulse-getting-started-with-lsdj]
created: 2026-08-30
updated: 2026-08-30
---

# LSDj — Little Sound Dj

A [[tracker]] that runs on the [[game-boy]] itself (as a cartridge ROM), written by [[johan-kotlinski]]; version 9.2.6 dates from May 2021. It drives the four channels of the [[game-boy-apu]] — PU1, PU2, WAV, NOI — through a song → chain → phrase hierarchy, instruments with tables, grooves and a wave-channel soft synth (source: [[s-lsdj-manual]]).

## Screens (SELECT+CURSOR moves between them)

```
Project  Synth   Wave
Song     Chain   Phrase   Instr.   Table
                 Groove
```

This two-row map dates from version 8 (three rows before); going up returns to the top-row screen last used — up from Song always opens Project, up from a `G` command the Groove screen (source: [[s-intense-tech-14-lets-appreciate-version-8]]). Hidden screens: file, word (speech), help. `START` plays the current screen's channel; in the song screen, or with `SELECT+START`, all four. `A,A` on any parameter or command shows quick help.

- **Song** — four columns (PU1 PU2 WAV NOI) of chain numbers, played top-down. `A` twice on an empty step creates a new chain/phrase; `B+A` on an empty step pulls chains up; mark rows with `B,B,B` and jump with `B+UP/DOWN`; `B+LEFT/RIGHT` pans a channel.
- **Chain** — list of phrases, each with an optional transpose (semitones). Chains are shared between channels; playing one chain on both pulse channels is a classic ([[detune]]).
- **Phrase** — 16 steps of note · instrument · command · value. Phrases are shared between channels. `A+LEFT/RIGHT` changes note, `A+UP/DOWN` octave; `B+A` deletes; cut the instrument column with `B+A` to change a note without retrig (legato). KIT/SPEECH instruments show sample names; NOISE shows a byte value (15-bit) or note (7-bit).
- **Instrument**, **Table**, **Groove**, **Synth**, **Wave**, **Project**, **File** — see below.

## Instruments

Five types; the type must match the channel: **PULSE** (PU1/PU2), **WAVE** and **KIT** (WAV), **NOISE** (NOI), **SPEECH** (instrument 40, WAV).

Common parameters: NAME · TYPE · LENGTH · OUTPUT (L/R/both/none) · **PITCH** — how `P`, `L`, `V` behave: FAST (360 Hz updates), TICK (per tick, vibrato synced to the music), STEP (P sets pitch instantly), DRUM (logarithmic fall-off for kicks); `A+L/R` picks the vibrato shape (triangle/saw/square, up or down) · TRANSP. (obey chain/project transposes) · CMD/RATE (slows `C`/`R`, and `P`/`V` in TICK mode; 0 fastest, F slowest) · TABLE (table to run on every note; TICK/STEP — STEP advances one table row per trigger).

| type | own parameters |
|---|---|
| PULSE | ENV. = three amplitude/speed pairs (`32/AD/10`: attack from 3 to A at speed 2, slow decay to 1, hold; speed 0 = hold, 1 fastest); WAVE (duty); SWEEP (PU1 only: time digit, pitch ± digit); PU2 TSP. (transpose PU2); FINETUNE (PU1 down, PU2 up) |
| WAVE | VOLUME 0/25/50/100 % + output; FINETUNE; WAVE or SYNTH; PLAY MANUAL/ONCE/LOOP/PINGPONG; SPEED; LENGTH; LOOP POS |
| KIT | two KITs (left and right note columns); VOLUME; FINETUNE; OFFSET; LEN (ALL = whole sample); LOOP OFF/ON/ATK; SPEED full/half; CLIP HARD/SOFT (tape-like)/FOLD/WRAP, `A+(LEFT,LEFT)` on HARD = raw memory mix |
| NOISE | ENV. as pulse; PITCH FREE (pitch changes may randomly mute) / SAFE (restart after pitch change) — introduced in 9.1.3 in place of S MODE FREE/STABLE: FREE equals the old STABLE (restart only when going from long-loop to short-loop noise), SAFE restarts on every change and never mutes; TRANSP. setting since 9.2 (source: [[s-intense-tech-21-whats-new-in-lsdj-92]]) |
| SPEECH | 14 word slots `W-0`…`W-D` built from 59 allophones in the word screen (allophone + duration per row) |

Sample kits shipped: SP0256-AL2 speech, Roland TR-606/707/727/808/909, CR-78, CR-8000, Boss DR-55/DR-110, E-mu Drumulator, Oberheim DMX, Korg KR-55, LinnDrum, Ace Tone Rhythm Ace FR-1, Sequential Tom, "Acieed" house vocals, "Animals". Kits, fonts, palettes and songs are replaced/managed with [[lsdpatch]] (LSDPatcher), which since 2021 also imports and exports songs as `.lsdsng` and `.lsdprj` (song plus the kits it uses) and resamples new kit samples with dithering and a fix for the wave-RAM refresh bug (source: [[s-intense-tech-20-lsdpatch]]). Sampled *tonal* instruments take another route: [[lsdj-wave-cruncher]] turns a one-note sample into a 16-frame wavetable that [[liblsdj]]'s `lsdj-wavetable-import` patches into the save, playable at any pitch (sources: [[s-intense-tech-05-wave-cruncher-instrument-library]], [[s-intense-tech-08-dotcnts-wave-cruncher]]).

## Tables

Six columns: **envelope** (amplitude digit + ticks; loop by putting the target step in the first digit and `H` in the second — e.g. tremolo), **transpose** (semitones; the classic table arpeggio), and two **command + value** pairs. Default speed one tick per step; `G` changes it. Started by the instrument's TABLE setting or by `Axx` in a phrase (`A20` stops); `SELECT+RIGHT` on an `A` command edits that table; `B+CURSOR` browses tables. See [[instrument-tables]].

## Grooves

Ticks per step for phrases and tables. Default groove 0 = 6/6; at 125 BPM a tick is 1/50 s. `8/5` = swing; `A+UP/DOWN` changes the swing percentage keeping the total ticks (6/6 = 50 % → 7/5 = 58 %); triplets and odd rhythms likewise. `Gxx` selects a groove; `SELECT+DOWN` on a `G` command edits it. See [[shuffle-funktempo]].

## Synth and wave screens

16 synth sounds × 16 waves (sound 0 = waves `00–0F`). Fixed settings: SIGNAL square/saw/triangle/custom (W.FX uses a wave in `F0–FF`), FILTER low/high/band/all-pass, DIST CLIP/FOLD/WRAP, PHASE PINCH/WARP/RESYNC/RESYN2. Variable settings with a smooth fade from first to last wave: VOLUME, CUTOFF, Q, VSHIFT, LIMIT (`0–F` lowers volume, `10–FF` wraps for overtones), PHASE. The wave screen edits individual waves. See [[wavetable-programming]].

## Commands (phrases and tables)

| cmd | name | effect |
|---|---|---|
| `Axx` | table | start table xx; `A20` stop |
| `Bxy` | MayBe | phrase: probability of playing (x = left kit, y = note/right kit; `B08` ≈ 50 %); table: hop to row y with probability x — new in version 7 (source: [[s-intense-tech-12-scoping-out-new-features]]) |
| `Cxy` | chord | arpeggio base, +x, +y: `C37` minor, `C47` major, `C0C`, `CC0`, `CCC`; `C00` reset; slowed by CMD/RATE; on noise since 9.1.0, limited to the noise notes (`F 5` + `C12` = F, G#, C) (source: [[s-intense-tech-19-new-noise-and-910-news]]) |
| `Dxx` | delay | delay the note by xx ticks |
| `Exy` | envelope | pulse/noise: x initial amplitude, y release (0/8 none, 1–7 decrease, 9–F increase); wave: `E00`–`E03` = 0/25/50/100 % |
| `Fxy` | frame/finetune | pulse: x = PU2 TSP, y = finetune in 1/32 semitones; kit: sample position (`00–7F` forward, `80–FF` back); wave: relative wave frame (`F10` = next synth sound) |
| `Gxx` | groove | select groove |
| `Hxy` | hop | phrase: `H00–H0F` next phrase at step y; `H10–HFE` hop back x times to step y; `HFF` stop; table: loop x times (0 = forever) to step y, nestable. Waltz: `H00` on step C |
| `Kxx` | kill | stop instantly (click) or after xx ticks; click-free alternatives `E00` (wave) / `E11` (pulse, noise) |
| `Lxx` | slide | slide to the note over xx (ticks if PITCH = TICK, else xx/360 s); in tables the transpose column sets the target |
| `Mxy` | master volume | x left, y right: 0–7 absolute, 8 none, 9–B up, D–F down (`M77` max) |
| `Oxx` | output | pan channel L / R / both / none |
| `Pxx` | pitch bend | speed (`PFE` = −2); DRUM log, FAST linear, TICK per tick, STEP instant; noise: sweeps the noise notes — since 9.1.0 `P01` applies `S01` every 4 ticks and `P04` every tick (source: [[s-intense-tech-19-new-noise-and-910-news]]) |
| `Rxy` | retrig/resync | x volume change (1–7 up, 9–F down), y rate (1 fastest, F slowest, 0 once); `R8x` resync at high rate (`R80` 360 Hz, `R8F` stop; pulse quirk: half an octave deeper); `RF4` = echo; `R8x` came with version 7 and takes a pulse kick about three whole tones below the channel's normal range (source: [[s-intense-tech-12-scoping-out-new-features]]) |
| `Sxy` | sweep/shape | pulse: frequency sweep (x time, y pitch ±; PU1 only); kit: loop offset/length; noise: shape (relative) |
| `Txx` | tempo | `T28–TFF` = 40–255 BPM, `T00–T27` = 256–295; exact for 6-tick grooves, else bpm = desired × ticks/step ÷ 6 |
| `Vxy` | vibrato | x speed, y depth in semitones (0=0.125, 1=0.25, 2=0.375, 3=0.5, 4=0.75, 5=1, 6=1.5, 7=2, 8=2.5, 9=3, A=3.5, B=4, C=5, D=6, E=7, F=8); `V00` off; on noise since 9.1.0 (always tick-based); since 9.1 the TICK-mode speeds match phrase steps — `V0x` = 16 steps, `V1x` = 12, `V2x` = 32/3, `V3x` = 8, `V4x` = 6, `V5x` = 16/3 … `VFx` = ½ (source: [[s-intense-tech-19-new-noise-and-910-news]]) |
| `Wxy` | wave | pulse: duty (resets the LENGTH timer — hardware oddity); wave: x synth speed, y length |
| `Zxy` | randomize | repeat the last non-Z/H command adding random 0..x / 0..y to its digits — every command except `H` since version 8 (source: [[s-intense-tech-14-lets-appreciate-version-8]]); worked examples in [[randomization-and-probability]] |

## Editing, cloning, workflow

`B+A` cut · `SELECT+A` paste · `SELECT+B` + cursor marks a block (`SELECT+(B,B)` column/row, `SELECT+(B,B,B)` screen) · `A+CURSOR` on a marked block changes all values (quick transpose) · `SELECT+(B,A)` clones a chain/phrase/instrument/table/synth · **deep** cloning copies the phrases, **slim** cloning reuses them (project screen) · `B+SELECT` mute, `B+START` solo · CLEAN SONG DATA / CLEAN INSTR DATA merge duplicates and free memory · project screen: TEMPO (tap `A` to tap-tempo), TRANSPOSE, SYNC, CLONE, LOOK, KEY DELAY/REPEAT, PRELISTEN, HELP, WORKED/PLAY/TOTAL clocks · file screen: up to 32 songs, 512-byte blocks, `BF` blocks = 97,792 bytes, songs compressed on save; `SELECT+A` loads without leaving the list, `START` plays — handy for live sets · `SELECT+A+B` on LOAD/SAVE = total memory reset · **back up your songs**: cartridge batteries die.

## Files, tools and cartridges

- **Files**: `.sav` — a cartridge's or emulator's save (up to 32 songs, one in working memory); `.lsdsng` — one song; `.lsdprj` — a song bundled with the kits it uses, the sharing format since LSDPatch's song manager; `.snt` — a wave-synth wavetable for `lsdj-wavetable-import`; `.lsdpal` — a palette (sources: [[s-intense-tech-04-liblsdj]], [[s-intense-tech-05-wave-cruncher-instrument-library]], [[s-intense-tech-20-lsdpatch]]).
- **Tools**: [[lsdpatch]] (ROM upgrade, kits, fonts, palettes, songs), [[liblsdj]] (`lsdsng-export`, `lsdsng-import`, `lsdj-wavetable-import`), [[lsdj-wave-cruncher]] (sample → wavetable); the older LSDManager by [[johan-kotlinski]] is superseded (source: [[s-intense-tech-20-lsdpatch]]).
- **Hardware**: a flash cartridge with 128 kB SRAM or FRAM — Everdrive GB X5, insideGadgets' carts with the GBxCart flasher; "LSDJ cartridges" on auction sites are unlicensed bootlegs, since the licence forbids selling LSDj on cartridges (source: [[s-intense-tech-16-cartridge-family]]; details on [[game-boy]]).
- **Emulators** for 9.2 and later: BGB 1.5.9 or newer, SameBoy, Gambatte, Emulicious — others get the new envelopes wrong (source: [[s-intense-tech-21-whats-new-in-lsdj-92]]).

## Live mode and sync

`SELECT+LEFT` toggles live mode: `START` starts the selected chain(s), `SELECT+START` stops them, `LEFT+START` starts a whole row; changes are queued until the playing chain (or, with a double press, the phrase) finishes. Sync modes: LSDJ (two Game Boys on a link cable, LEAD/SYNC/WAIT, clipboard transfer between them), MIDI, ANALOG IN/OUT, KEYBD — see [[sync]].

## Noise shape cheat sheet (versions up to 9.0)

The NOISE instrument's shape byte: first digit = octave, second digit = clock divisor and loop mode; `S`, `P`, `C` and transposes act on it as described in [[pitch-slide-and-portamento]] (source: [[s-intense-tech-17-the-joys-of-noise]]).

| digit | as first digit: octave | as second digit: divisor (`8–F` long-loop = white-noise-like, `0–7` short-loop = tonal, metallic) |
|---|---|---|
| `F` | highest | ×2, long-loop |
| `E` | one lower | ×1, long-loop |
| `D` | two lower | ÷2, long-loop |
| `C` | three lower | ÷3, long-loop |
| `B` | four lower | ÷4, long-loop |
| `A` | five lower | ÷5, long-loop |
| `9` | six lower | ÷6, long-loop |
| `8` | seven lower | ÷7, long-loop |
| `7` | eight lower | ×2, short-loop |
| `6` | nine lower | ×1, short-loop |
| `5` | ten lower | ÷2, short-loop |
| `4` | eleven lower | ÷3, short-loop |
| `3` | twelve lower | ÷4, short-loop |
| `2` | thirteen lower | ÷5, short-loop |
| `1` | no sound | ÷6, short-loop |
| `0` | no sound | ÷7, short-loop |

Before 8.6.0 the *octave* of the phrase note selected the first digit (octave 5 = the instrument's digit; octave 6 before 5.1.6) and the pitch class did nothing; since 8.6.0 shapes go directly into phrases. Short-loop pitches follow a "negative harmonic series" (the base frequency divided by 1, 2, 3 …), nearest to C, F, A♭ and D. Going from long-loop to short-loop has a 1-in-256 chance of muting the channel; the instrument's S MODE (earlier S CMD; FREE/STABLE) set to STABLE blocks that direction. 9.1.0 removed FREE/STABLE, and 9.1.3 added PITCH FREE/SAFE after mutes were found to happen even inside one loop mode: FREE behaves like the old STABLE, SAFE restarts the noise on every change and never mutes (sources: [[s-intense-tech-19-new-noise-and-910-news]], [[s-intense-tech-21-whats-new-in-lsdj-92]]). The hardware behind it is on [[game-boy-apu]].

### Since 9.1.0: ordered noise notes

Version 9.1.0 replaced the shape byte with values ordered by frequency: the long-loop noises first, lowest to highest, as `00`–`3B`; above them the short-loop noises as note names C, D, F and G# (the pitches each frequency is closest to) in octaves −9 to 8 — all four notes in octaves −9…4, only C in octaves 5–8 plus an extra F in octave 5. Old songs are converted on loading **except their transposes and `S` values**; Defense Mechanism's converter (defensem3ch.github.io/noise-convert) maps them. Read from its table: old short-loop shapes `X0`…`X7` become D, F, G#, C, F, C, C, C in rising octaves (`90` → `D-2`, `93` → `C-1`, `95` → `C 0`, `97` → `C 2`, `A5` → `C 1`, `80` → `D-3`, `70` → `D-4`), and old long-loop shapes `X8`…`XF` become `4·(X−2)` plus 0, 1, 2, 3, 5, 7, 11, 15 (`98` → `1C`, `9F` → `2B`), compressed near the top (`FF` → `3B`). `P`, `C` and `V` work on the new notes (see the command table) (source: [[s-intense-tech-19-new-noise-and-910-news]]).

## Version history (from the sources)

| version | change | source |
|---|---|---|
| ≈ 2000 | first release, for the Game Boy Color; cartridges sold online and through a Stockholm record store | [[s-intense-tech-13-kotlinski-interview]] |
| 2001-01 | live mode, inspired by Ableton Live's beta | [[s-intense-tech-13-kotlinski-interview]] |
| 1.4.0 | optimised dual-kit sample mixing, fast enough for the DMG | [[s-intense-tech-13-kotlinski-interview]] |
| 3.0.0 | file screen with RLE compression: many songs per cartridge | [[s-intense-tech-13-kotlinski-interview]] |
| 3.9.2 (2008-12-26) | "purge sequencer/instruments" becomes "free unused data" (also frees tables, synths, waves) | [[s-chipmusic-lsdj-faq]] |
| 3.9.5 | prelisten | [[s-intense-tech-13-kotlinski-interview]] |
| 3.9.e (2009-07-26) | "free unused data" split into CLEAN SONG DATA and CLEAN INSTR DATA | [[s-chipmusic-lsdj-faq]] |
| 5.1.0 | new pitch engine; the old logarithmic slides were lost until version 6 | [[s-intense-tech-13-kotlinski-interview]], [[s-intense-tech-10-kicks-part-1]] |
| 5.1.6 | the phrase octave that selects a noise shape's first digit moves from 6 to 5 | [[s-intense-tech-17-the-joys-of-noise]] |
| 6.x (6.9.0, 2019-10) | instrument setting P/L/V: FAST (formerly HF), TICK, STEP, DRUM | [[s-intense-tech-10-kicks-part-1]] |
| 7.0 (7.0.6, 2019-11) | P/L/V renamed PITCH; transpose works with DRUM | [[s-intense-tech-11-kicks-part-2]] |
| 7.7.4 (2020-01) | `B` (mayBe) probability command; FX/SPEED (later CMD/RATE); wave-channel oscilloscope; silky wave — click-free wave switching, SPEED `01` synths audible; `R8x` super-fast retrig; wave FINETUNE ±F; maximum tempo 295 (`T00–T27`); fast load/save. Still crashy: 6.9.0 stayed the stable release | [[s-intense-tech-12-scoping-out-new-features]] |
| 8 stable (2020) | accurate vibrato, de-clicked WAV playback, slowed-down `C`, probability sequencing, higher maximum tempo, wave finetune, optimised playback, high-speed retrig | [[s-intense-tech-13-kotlinski-interview]] |
| 8 (2020-03) | two-row screen map; ADSR replaces ENVELOPE on pulse and noise; `Z` on every command but `H`; tables PLAY/STEP (STEP = the old Automate); FX/SPEED renamed CMD/RATE; wave LOOP POS instead of REPEAT; `R` restarts the wave synth from its first frame; wave instruments default to MANUAL; `xF` in the table volume column hops to row x; synth cloning from the instrument screen; CLEAN SONG/INSTR DATA remove duplicates; `V` in three channels no longer crashes | [[s-intense-tech-14-lets-appreciate-version-8]] |
| 8.1.0 | ADSR for pulse and noise instruments (8.1.8 by 2020-02) | [[s-intense-tech-18-adsr-makes-life-easier]], [[s-intense-tech-13-kotlinski-interview]] |
| 8.5.1 stable / 9.2.A dev | the pair Infu's course was written against; noise notes and the envelope differ between them | [[s-infu-getting-started-with-lsdj]] |
| 8.1.9 | `Z` works with `H`, `G` and `D` (a note added to article 03; article 14 says every command except `H` — the wiki records both) | [[s-intense-tech-03-dont-sleep-on-z]] |
| 8.6.0 | noise shapes can be typed directly in phrases | [[s-intense-tech-17-the-joys-of-noise]] |
| 8.8.0 | software volume for pulse and noise: click-free `E`, table volume column and `K` | [[s-intense-tech-18-adsr-makes-life-easier]] |
| 8.9.3 | `R01` retrigs every tick | [[s-intense-tech-17-the-joys-of-noise]] |
| 9.0.1 | sprite-based play-position indicators at 60 Hz | [[s-intense-tech-19-new-noise-and-910-news]] |
| 9.1.0 (2021-01) | noise channel reorganised into ordered notes (long-loop `00–3B`, then short-loop C/D/F/G# by octave); `P`, `C` and `V` on noise; TICK vibrato rates match phrase steps; two-digit FINETUNE and LIMIT (overdrive above `0F`); wave `F` immediate again; FREE/STABLE removed; row bookmarks | [[s-intense-tech-19-new-noise-and-910-news]] |
| 9.1.3 | noise PITCH FREE/SAFE | [[s-intense-tech-21-whats-new-in-lsdj-92]] |
| 8.5.1 stable / 9.1.8 dev / 8.4.1 Arduinoboy (2021-02) | the builds LSDPatch 1.10.4 offered for ROM upgrades | [[s-intense-tech-20-lsdpatch]] |
| 9.2.H (2021-08) | rewritten kit timing (kits from LSDPatcher ≥ 1.11.5); synth PHASE modes PINCH/WARP/RESYNC/RESYN2; waves no longer inverted; noise TRANSP; ENV visualiser and `A,A` tooltips; wave instrument RESYNC play mode; `LEFT+START` queues song rows in SONG mode; song rows `FF` → `BF`, 14 speech words; 60 fps screen; needs BGB ≥ 1.5.9, SameBoy, Gambatte or Emulicious | [[s-intense-tech-21-whats-new-in-lsdj-92]] |
| 9.2.6 (2021-05) | the manual ingested in this wiki (its version number precedes 9.2.H in the letter-suffixed 9.2 series) | [[s-lsdj-manual]] |

## Hardware behind the parameters

How the instrument screen and commands map onto the [[game-boy-apu]] registers documented in [[pan-docs]]. The correspondences are inferred from the two descriptions (LSDj's source is not ingested); the hardware column is sourced (sources: [[s-lsdj-manual]], [[s-pandocs-audio-registers]], [[s-pandocs-audio-details]]).

| LSDj | hardware |
|---|---|
| PULSE instrument WAVE, `Wxy` on pulse | `NRx1` bits 7–6: 12.5 / 25 / 50 / 75 % duty — 25 and 75 % sound the same; the duty shares the register with the length timer, hence the LENGTH reset |
| LENGTH | the length timer: 1/256 s ticks, cuts at 64 steps (256 on WAV) |
| ENV first pair, `Exy` | `NRx2`: initial volume `0–F`, direction, pace 1–7 (× 1/64 s); the second and third ENV pair and speeds above 7 are beyond the hardware ramp, so software |
| SWEEP (PU1), `Sxy` on pulse | `NR10`: pace, direction, step — an upward sweep that overflows silences the channel |
| WAVE VOLUME 0/25/50/100 %, `E00`–`E03` | `NR32` output level (a bit shift); the wave channel has no envelope |
| synth waves, `F` frames, kits, speech | wave RAM `$FF30–$FF3F`, 16 bytes = 32 × 4-bit samples, rewritable only while the channel is stopped |
| NOISE instrument 7-bit / 15-bit values, PITCH FREE / SAFE | `NR43` bit 3 LFSR width; switching 15 → 7 can lock the LFSR silent, a retrigger resets it |
| OUTPUT, `Oxx`, `B+LEFT/RIGHT` | `NR51` left/right bits per channel; a change while the channel plays pops |
| `Mxy` | `NR50` master volume, 0 = 1/8 … 7 = full per side, never mutes |
| `Kxx` click vs `E00`/`E11` | switching a DAC off pops; volume 0 with the DAC on is silent |
| any new note, `R` retrig | bit 7 of `NRx4`: switch on, reload period, restart envelope and sweep, reset the LFSR; a pulse channel's phase is never reset |

## Related

[[game-boy]] · [[game-boy-apu]] · [[pan-docs]] · [[johan-kotlinski]] · [[intense-tech]] · [[defense-mechanism]] · [[infu]] · [[chipmusic-org]] · [[instrument-tables]] · [[chord-arpeggio]] · [[shuffle-funktempo]] · [[wavetable-programming]] · [[instrument-design]] · [[retrigger]] · [[randomization-and-probability]] · [[liblsdj]] · [[lsdpatch]] · [[lsdj-wave-cruncher]] · [[sabrepulse]] · [[hypnogram]] · [[4ntler]]

## Sources

[[s-lsdj-manual]] · [[s-pandocs-audio-registers]] · [[s-pandocs-audio-details]] · [[s-intense-tech-09-lets-table-this-discussion]] · [[s-intense-tech-10-kicks-part-1]] · [[s-intense-tech-11-kicks-part-2]] · [[s-intense-tech-13-kotlinski-interview]] · [[s-intense-tech-17-the-joys-of-noise]] · [[s-intense-tech-18-adsr-makes-life-easier]] · [[s-intense-tech-01-wave-synth-deep-dive-part-1]] · [[s-intense-tech-02-wave-synth-deep-dive-part-2]] · [[s-intense-tech-06-groove-and-tick-tricks-part-1]] · [[s-intense-tech-07-groove-and-tick-tricks-part-2]] · [[s-infu-getting-started-with-lsdj]] · [[s-chipmusic-lsdj-faq]] · [[s-chipmusic-lsdj-advanced-tricks]] · [[s-chipmusic-noise-drum-threads]] · [[s-chipmusic-tables-and-chords-threads]] · [[s-chipmusic-kotlinski-interviews]] · [[s-intense-tech-03-dont-sleep-on-z]] · [[s-intense-tech-04-liblsdj]] · [[s-intense-tech-05-wave-cruncher-instrument-library]] · [[s-intense-tech-08-dotcnts-wave-cruncher]] · [[s-intense-tech-12-scoping-out-new-features]] · [[s-intense-tech-14-lets-appreciate-version-8]] · [[s-intense-tech-15-lets-mix-it-up-and-down]] · [[s-intense-tech-16-cartridge-family]] · [[s-intense-tech-19-new-noise-and-910-news]] · [[s-intense-tech-20-lsdpatch]] · [[s-intense-tech-21-whats-new-in-lsdj-92]] · [[s-sabrepulse-getting-started-with-lsdj]]
