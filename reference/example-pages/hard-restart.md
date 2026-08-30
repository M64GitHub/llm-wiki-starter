---
title: Hard restart
type: technique
platforms: [c64]
tags: [sid, envelope, instrument, c64, adsr-bug]
aliases: [HR, hardrestart, ADHR, ADSR bug, envelope bug]
sources: [s-sid-wizard-manual, s-goattracker-readme, s-lemon64-hard-restart-threads, s-chordian-sf2-instruments, s-witchmaster-creating-chiptunes-with-sid-wizard, s-walleij-sid-player-routine, s-chipmusic-c64-music-for-dummies, s-hvsc-sid-file-format, s-furnace-c64-docs, s-ucapps-wavetable-sounds-tutorial-1, s-commodore-64-eu-sid-chip, s-sidmusic-yannes-interview, s-remix64-galway-interview, s-sidmusic-jeroen-tel-interviews, s-sidin02-matt-gray-driller, s-realdmx-sid-players, s-64er-soundmonitor-article, s-recollection-brief-history-of-sid]
created: 2026-08-30
updated: 2026-08-30
---

# Hard restart

## What it is

A player-routine trick that gates a [[sid]] voice off and loads a special ADSR value one or two frames *before* the next note, so that every note's attack starts from a known envelope state. It exists because of the SID's envelope bug: "SID provides quite bad accuracy on attack after releasing a note, resetting the ADSR registers before a note is played helps with this problem" (source: [[s-witchmaster-creating-chiptunes-with-sid-wizard]]); "Hard restart was invented to defeat this ADSR bug" (source: [[s-chordian-sf2-instruments]]). Every C64 tracker in the wiki implements it per instrument or per driver.

## Why it works

- The failure mode, in [[lasse-oorni]]'s words: "trying to trigger a sound when the envelope is still at max. volume will result in silence and lockup that lasts until the gatebit gets cleared again"; the cure is "the minimum 2 frame period with gatebit off". The test bit is *not* the cure — it "will be reset immediately" on the oscillator but "doesn't affect the envelope generator at all" (source: [[s-lemon64-hard-restart-threads]]).
- [[chordian]]: in a run of short notes each kept gated until the next, "you would probably hear the ADSR stumble here and there"; some ADSR values alleviate it, "but it's easy to keep running into this problem". The restart "works by gating off and resetting the ADSR values a few ticks before the next note triggers" — two ticks in SID Factory II's drivers; a 15-tick note plays 13 ticks, then the HR ADSR takes over, possibly "a tiny bit staccato", and "the next note always triggers perfectly" (source: [[s-chordian-sf2-instruments]]).
- The bug is deterministic in emulators (reSID's `envelope.h`, also in VICE) but hard to be deterministic about from 6502 code, because it depends on exact timing (encore, source: [[s-lemon64-hard-restart-threads]]); the [[goattracker]] readme accordingly warns that packed players with unbuffered writes and "unpredictable timing variation" can still ADSR-bug (source: [[s-goattracker-readme]]).
- The same bug seen from a hardware synthesizer: rebuilding a Hubbard drum on a MIDIbox SID, Thorsten Klose found the first (triangle) frame missing from the real chip's output — "the gate is delayed by up to ca. 30mS", an effect "reverse engineered by Dag Lem, and documented in the source code of reSID"; a release rate of 0 removes the delay entirely (at the price of no fade), which is why most MIDIbox SID presets use no release, and why his wavetables end with a step that "resets the envelope registers in order to avoid 'ADSR hick-ups'" (source: [[s-ucapps-wavetable-sounds-tutorial-1]]). Compare Walleij's "33 ms = 2^15 cycles" below — the same figure.
- **What the chip's designer says — and does not say**: [[bob-yannes]]'s 1996 account explains the envelope generator's design (an 8-bit up/down counter, a rate divider with a look-up table, a sustain comparator — see [[adsr-envelope]]) but does **not** describe the re-gating lock-up; the nearest statements are that the sustain comparator stops the envelope clock only "when the counter counted down to the Sustain value" and that the counter "would not count UP if the Sustain level were set higher" (source: [[s-sidmusic-yannes-interview]]). Do not cite the interview as the cause of the bug. The same interview does give a silicon reason for the `$09` first frame: zero-volume "signal leakage … could be dealt with by stopping the oscillator" (source: [[s-sidmusic-yannes-interview]]).

## How to do it

### SID-Wizard

Instrument main settings (`F7`):

| setting | meaning |
|---|---|
| `ADHR` | the ADSR loaded "1-2 frames before a new note is triggered"; common values `0F00` and `F800` |
| HardRestart timer | `0..2` frames before the note |
| HardRestart type | normal, or *staccato / aggregated*: the test bit is also reset at hard restart, "adds 1-2 frames of gap between consequent notes" |
| Frame-1 waveform | waveform/control byte for the note's first frame (enable with `RETURN`, on by default); Hermit: its purpose "is the same as in Goattracker, to test / reset the oscillators with waveform $09 (test-bit set) before the sound starts and get a short 'sexy' start of the sound" |

In SID-Wizard 1.0 the beginners' tutorial had every instrument set `HRTY` to `2` (a square symbol appears next to the number) "so that the gate bit is reset between each note, which is important because otherwise notes will not sound if they come after another note rather than a note off" — later versions do this by default (source: [[s-chipmusic-c64-music-for-dummies]]). The Medium player drops the HR type and frame-1 setting; the Demo player has no hard-restart/frame-1 settings ([[sid-player-routine]]) (sources: [[s-sid-wizard-manual]], [[s-witchmaster-creating-chiptunes-with-sid-wizard]]).

### GoatTracker

- Per instrument: **HR/Gate timer** = how many ticks before the next note the note fetch, gate-off and hard restart happen (at most tempo−1; with tempo 6 and timer 2 they happen on tick 4, "2 ticks before first frame"); bit `$80` disables hard restart, `$40` disables gate-off. **1stFrame Wave** is "usually `$09` (gate + testbit)".
- Global: the HR ADSR value (`-Axx`, `SHIFT+F7`), default `0F00` — "0000 is probably too hard to be useful, except perhaps with gateoff timer value 1. 0F00 (default) is a lot softer, and 0F01 adds also a little bit of release to the gateoff phase for even softer sound. 000F makes the note start very pronounced." Attack `F` enables an alternative playroutine that writes the waveform before ADSR, "more reliable note triggering, especially for very fast releases 0 & 1".
- Legato without restart: timer bit `$40` and 1stFrame `$00` (tables and ADSR still re-initialise).
- Multispeed: multiply the timer with the speed (2 → 4 at 2×). If a packed tune still bugs: make note-init take more cycles (nonzero pulse start position, 1stFrame `$09` → `$0B`), use buffered writes, or attack `F`; since v2.68 notes with attack 0 and release 1 are the sensitive case.

(source: [[s-goattracker-readme]])

### SID Factory II

Set bit `$80` of the instrument's third flag byte; the second nibble points into the HR table, whose default pair `0F 00` is the ADSR used for the last two ticks — "I have never had to change it" (source: [[s-chordian-sf2-instruments]]).

### Furnace

[[furnace]] calls it **envelope reset**: in the chip configuration, *Hard reset envelope* is the ADSR "used during the short reset before a note" and *Envelope reset time* the number of ticks — "0 disables reset, which prevents notes from triggering. 1 is short, but may exhibit SID envelope bugs. 2 is a good value." From the pattern, `15xx` sets the reset time (`00`, or more than the song speed, = no reset) and `1Axx` disables it for the channel; per instrument, *Don't test before new note* "disables the one-tick hard reset and test bit before a new note" — so Furnace, like GoatTracker's `$09`, sets the test bit during the reset (source: [[s-furnace-c64-docs]]).

### In your own player routine

iAN CooG's retrigger sequence for a sound effect: write `$09` (gate + test) to the control register, wait two frames, write `$00`, then set ADSR and pitch and gate on. encore's three strategies: hard restart; "finding safe ADSR-values in a song where the bug never triggers (and this depends entirely on the situation/arrangement/instrument/bpm)"; or "keep a voice continuously in its sustain mode and simulating new notes with changes in pwm or filter instead" (source: [[s-lemon64-hard-restart-threads]]).

[[linus-walleij]]'s version, from the JCH player he admired: "write 0x00 to all registers at $d400–$d406 2/50 second (2 frames) before next attack" — "the actual minimum time is 33 ms = 2^15 cycles according to Dag Lem, author of reSID"; "some say setting the test bit … is just as good" (the Lemon64 threads above say it is not — the test bit resets the oscillator, not the envelope); and "hard restart only fixes problems with attack, not the ever-present problem with release". For a live MIDI player the technique is "a catch 22": you cannot know a frame ahead that a note is coming, so the SIDstation either hard-restarts every voice on key press, delaying all notes by 1/50 s, or on key release, which "kills the voice effectively, and makes all release settings superfluous" (source: [[s-walleij-sid-player-routine]]).

## Before hard restart existed

[[martin-galway]]'s workaround at Ocean (1984–87) was avoidance: "Certain ADSR settings totally screw up and play too early – as I recalled it was with long attacks and long decays. The key-on/key-off circuitry had a problem, evidently. I called it the school band effect and simply had to stay away from certain ADSR settings, which was a drag sometimes on original works" (source: [[s-remix64-galway-interview]]) — the same strategy encore lists above as "finding safe ADSR-values".

## Does the 8580 need it? (a contradiction between sources)

Walleij: the problem "only affects the 6581 version of the SID chip (or so I am told...) and not the later 8580 version, so for some MIDI appliances the 8580 is a lot better choice" (source: [[s-walleij-sid-player-routine]]). The wiki's other sources do not make that distinction: the Lemon64 explanations describe the lock-up as a property of the envelope generator without naming a revision (source: [[s-lemon64-hard-restart-threads]]); the SID-Wizard book only credits the 8580 with "maybe more predictable ADSR envelope-handling" (source: [[s-witchmaster-creating-chiptunes-with-sid-wizard]]); HVSC's format document speaks of "the ADSR bugs in the SID chip" in general (source: [[s-hvsc-sid-file-format]]); and every tracker on this page applies hard restart regardless of the model selected. Walleij himself hedges ("or so I am told"). Two later descriptions do not distinguish the chips either: Furnace applies its envelope reset whichever model is selected (source: [[s-furnace-c64-docs]]), and commodore-64.eu describes "a well-known bug in the envelope generator" as a property of the SID as such (source: [[s-commodore-64-eu-sid-chip]]; secondary). The composer interviews add nothing decisive either: none tests the 8580; Galway's "school band effect" comes from 6581-era work at Ocean (1984–87), and [[jeroen-tel]]'s remark about chip versions that "varied a lot" concerns the filter, not the envelope (sources: [[s-remix64-galway-interview]], [[s-sidmusic-jeroen-tel-interviews]]). Until a source tests both chips, treat hard restart as needed on both and the 8580 as at most *less* sensitive.

## Ancestors in the classic drivers

- [[matt-gray-player]] (1987): instrument byte 6 is "Control register set at the end of the note, but in the same frame of when setting the new note", and effect bit 2 plays a separate control register "for the first two frames" of a note before the normal one — a gate-off and a different first-frame waveform at note boundaries, done per instrument; a pattern byte `$00` re-plays the previous note "with the gate bit set to 0, so the release phase will start" (source: [[s-sidin02-matt-gray-driller]]).
- [[musicfile]] (1988): per-instrument `starttabel` (`$81,$81,$81,$81, $41,$11,$11,$81 …`) and `startlen` (`$02 … $06`) tables, read as a first-frames waveform (mostly noise) and its length — the same idea as [[goattracker]]'s 1st-frame waveform (interpretation of the source, unverified; source: [[s-realdmx-sid-players]]).
- [[soundmonitor]] (1986) separates the waveform at key-on (register 0, gate bit set) from the waveform at key-off (register 8, gate cleared), and lets a note be entered with `SHIFT` so it is *not* retriggered — legato versus restart decided per note (source: [[s-64er-soundmonitor-article]]).


- Who invented it, per the scene: "JCH is the inventor of what we call a hard-restart. It's a little pause-trick code, so that a sound never fails and the oscillator starts from point 0 of the waveform of the SID, not somewhere in middle where it was running before. This has been developed by GRG to also a soft-restart, so that sounds go from very hard start, to softer hit on key, when starting" ([[chordian]]; source: [[s-recollection-brief-history-of-sid]]).


## Tips & pitfalls

- HR shortens the previous note by the timer length; on very fast runs that is audible (commodorejohn's objection to cutting notes "a very audible fraction of a second before"). The HR ADSR trades this: `0F01` softer, `000F` harder attacks (sources: [[s-lemon64-hard-restart-threads]], [[s-goattracker-readme]]).
- Leave the HR ADSR at `0F00` unless you hear a reason (Chordian); in SID-Wizard `F800` is the other common value.
- Timer 2 is the norm; timer 1 only with the hardest HR ADSR (`0000`) (GoatTracker readme).
- A staccato HR type or the test bit in frame 1 also fixes the *noise lock-up* and resets oscillator phase — see [[ring-modulation-and-sync]].
- Drums lose their first frame to the envelope delay unless the release is short: Klose's MIDIbox drums (release `8`) played the noise and pulse frames but not the opening triangle frame (source: [[s-ucapps-wavetable-sounds-tutorial-1]]).

## Related

[[adsr-envelope]] · [[instrument-design]] · [[sid-wizard]] · [[goattracker]] · [[sid-factory-ii]] · [[furnace]] · [[sid-player-routine]] · [[multispeed]] · [[linus-walleij]] · [[sync]] · [[martin-galway]] · [[bob-yannes]]

## Sources

[[s-sid-wizard-manual]] · [[s-goattracker-readme]] · [[s-lemon64-hard-restart-threads]] · [[s-chordian-sf2-instruments]] · [[s-witchmaster-creating-chiptunes-with-sid-wizard]] · [[s-walleij-sid-player-routine]] · [[s-chipmusic-c64-music-for-dummies]] · [[s-hvsc-sid-file-format]] · [[s-furnace-c64-docs]] · [[s-ucapps-wavetable-sounds-tutorial-1]] · [[s-commodore-64-eu-sid-chip]] · [[s-sidmusic-yannes-interview]] · [[s-remix64-galway-interview]] · [[s-sidmusic-jeroen-tel-interviews]] · [[s-sidin02-matt-gray-driller]] · [[s-realdmx-sid-players]] · [[s-64er-soundmonitor-article]] · [[s-recollection-brief-history-of-sid]]
