---
title: "Little Sound Dj v9.2.6 Operating Manual (summary)"
type: summary
source-path: raw/lsdj/LSDj_9_2_6.pdf (text extract: raw/lsdj/LSDj_9_2_6.txt)
source-url: https://www.littlesounddj.com/lsd/latest/documentation/LSDj_9_2_6.pdf
author: Johan Kotlinski
date: 2021-05-09
tags: [gameboy, lsdj, tracker, manual]
created: 2026-08-30
updated: 2026-08-30
---

# Little Sound Dj v9.2.6 Operating Manual

The official manual of [[lsdj]] (79 pages, dated 9 May 2021) by [[johan-kotlinski]]. Chapter 1 covers the [[game-boy]]'s four sound channels, keys and hex; chapter 2 walks through the nine screens (song, chain, phrase, instrument, table, groove, synth, wave, project, plus the hidden file, word and help screens); chapter 3 has advanced techniques (copy/paste, cloning, backups, mute/solo/pan, live mode, synthetic drums); chapter 4 is the command reference (A B C D E F G H K L M O P R S T V W Z); chapter 5 synchronisation (Game Boy link, MIDI, analog in/out, PS/2 keyboard); appendices list the sample kits, the 59 speech allophones and the SRAM memory map.

## Key claims

- The Game Boy sound chip has four 4-bit channels: pulse 1 (envelope + sweep), pulse 2 (envelope), wave (soft synth, sample playback, speech), noise (envelope + shape) — see [[game-boy-apu]].
- Sequencing is a tree: **song** (four columns of chains) → **chain** (list of phrases, each with an optional transpose) → **phrase** (16 steps of note, instrument, command, value). Phrases and chains are shared between channels; a chain can be played on both pulse channels. See [[orderlist]], [[tracker]].
- Five instrument types: PULSE, WAVE, KIT (ROM samples, two kits as left/right note columns), NOISE (7-bit or 15-bit), SPEECH (instrument 40, 14 word slots built from allophones). Instrument types must match the channel.
- Instrument PITCH setting (FAST 360 Hz / TICK / STEP / DRUM) governs the P, L and V commands; CMD/RATE slows C and R (and P/V in TICK mode); TRANSP. opts an instrument out of chain/project transposes.
- **Tables**: six columns — amplitude envelope, transpose, two command/value pairs — run at one tick per step by default, started by the instrument or by `Axx`; loops with `H`, probabilistic hops with `B`. They are LSDj's [[instrument-tables]].
- **Grooves** set ticks per step (default 6/6; at 125 BPM there are 50 ticks per second); 8/5 makes swing; `A+UP/DOWN` changes swing percentage at constant total; `G` selects a groove in phrases or tables ([[shuffle-funktempo]]).
- The wave channel's **synth** generates 16 sounds of 16 waves each from a signal (square/saw/triangle/custom), filter (LP/HP/BP/AP), distortion (CLIP/FOLD/WRAP), phase (PINCH/WARP/RESYNC), with start/end values for volume, cutoff, Q, vshift, limit and phase; WAVE instruments play them MANUAL/ONCE/LOOP/PINGPONG ([[wavetable-programming]]).
- Commands: `C` chord arps (`C37` minor, `C47` major), `V` vibrato with a depth table in semitones, `L` slide to note over a duration, `P` pitch bend, `R` retrig/resync (`RF4` = echo, `R8x` resync), `S` sweep/loop points/noise shape, `E` amplitude, `F` frame/finetune/sample offset, `H` hop (also waltz time: `H00` on step C), `B` MayBe probability, `Z` randomize, `T` tempo (BPM formula for non-6-tick grooves), `M` master volume, `O` output, `D` delay, `K` kill, `A` table, `G` groove, `W` wave.
- Synthetic drum recipes: pulse bass drum (ENV `C3/0/0`, SWEEP `63`, note `C-6`, TRANSP. OFF), noise snare (ENV `F1/D3/0`, note value ≈ `30`), hi-hats (≈ `38`), wave bass drum (PITCH DRUM, triangle, table `P C0` then TSP `80` + `L30`).
- Workflow: clipboard (B+A cut, SELECT+A paste, SELECT+B block marks), deep vs slim cloning (`SELECT+(B,A)`), CLEAN SONG/INSTR DATA, up to 32 songs per cartridge in 512-byte blocks (`BF` blocks = 97,792 bytes), always back up because cartridge batteries die.
- Live mode (`SELECT+LEFT`) queues chain starts/stops per channel; sync modes LSDJ (link cable, LEAD/SYNC/WAIT, clipboard transfer between Game Boys), MIDI (needs a sync cable), ANALOG IN/OUT (spliced link cable + 3.5 mm, Volca/Monotribe), KEYBD (PS/2 keyboard as piano). Use 6-tick grooves when synced.

## Practical takeaways

Everything expressive in LSDj comes from three places: the instrument PITCH/ENV/TABLE settings, the six-column tables, and a small set of single-letter commands that double as table columns. Learn `C V L P R S E H G` first. Kits (TR-808/909/606/707/727, CR-78, LinnDrum, DMX, Drumulator…) cover drums; the synthetic-drum recipes free the wave channel for bass.

## Notable quotes

> "Tables are sequences of transposes, commands and amplitude changes which can be run at any speed and applied to any channel."

> "Some words of caution from many peoples hard-earned experience: When using a Game Boy cartridge, backup your songs!"

## Relevance

Primary reference for the Game Boy branch: fills the wanted pages [[lsdj]], [[game-boy]], [[game-boy-apu]] and adds an `### LSDj` section to most technique pages.

## Pages touched

Created: [[lsdj]], [[game-boy]], [[game-boy-apu]], [[johan-kotlinski]], [[sync]], [[retrigger]], [[randomization-and-probability]], [[stereo-panning]]. Updated: [[chord-arpeggio]], [[vibrato]], [[pitch-slide-and-portamento]], [[pulse-width-modulation]], [[shuffle-funktempo]], [[fake-echo]], [[detune]], [[instrument-design]], [[wavetable-programming]], [[sidechain-pump]], [[instrument-tables]], [[orderlist]], [[tracker]], [[arrangement]], [[rhythm-and-groove]], [[adsr-envelope]].
