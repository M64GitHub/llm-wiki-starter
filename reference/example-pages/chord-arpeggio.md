---
title: Chord arpeggio (the 0 3 7 trick)
type: technique
platforms: [general, c64, pc-tracker, gameboy]
tags: [arpeggio, chords, channel-economy, signature-sound]
aliases: [chip arp, arp, arpeggio, "0 3 7", chord table]
sources: [s-037-lab, s-sid-wizard-manual, s-lsdj-manual, s-tw077-chip-off-the-block, s-tw081-it-tip-of-the-week, s-tw039-chord-theory-debate, s-it-manual, s-goattracker-readme, s-witchmaster-creating-chiptunes-with-sid-wizard, s-newman-driving-the-sid-chip, s-intense-tech-17-the-joys-of-noise, s-intense-tech-09-lets-table-this-discussion, s-chipmusic-tables-and-chords-threads, s-infu-getting-started-with-lsdj, s-intense-tech-06-groove-and-tick-tricks-part-1, s-protracker-23d-help, s-ft2-manual, s-st3-manual, s-openmpt-manual-compatible-playback, s-openmpt-manual-song-properties, s-walleij-sid-player-routine, s-intense-tech-19-new-noise-and-910-news, s-intense-tech-12-scoping-out-new-features, s-intense-tech-14-lets-appreciate-version-8, s-intense-tech-03-dont-sleep-on-z, s-sabrepulse-getting-started-with-lsdj, s-furnace-c64-docs, s-chipmusic-typical-sid-sounds, s-hugi38-interview-jeroen-tel, s-64er-soundmonitor-article, s-sidin02-matt-gray-driller, s-matt-gray-dominator-source, s-realdmx-sid-players, s-vgmpf-maniacs-of-noise, s-c64com-matt-gray-interview, s-recollection-brief-history-of-sid, s-rvg-matt-gray-interview, s-soundmonitor-lineage-wikis]
created: 2026-08-30
updated: 2026-08-30
---

# Chord arpeggio

## What it is

Chips rarely have enough channels for real chords, so one channel cycles through the chord tones extremely fast. At roughly 25–50 notes per second the ear fuses them into one shimmering chord — the signature chiptune sound. Slower rates (10–15 notes/s) sound like a deliberate arpeggio riff instead of a chord; both are useful (source: [[s-037-lab]]).

## Why it works

The numbers are semitone offsets from the base note ([[semitone-math]]): `0 3 7` minor, `0 4 7` major, `0 3 6` diminished. A fast arp is heard mostly by its **highest** note, so the inversion you choose decides which tone "sings" ([[chord-inversions]]). Which formula fits which scale degree is not constant — `0 3 7` on every note of a major scale clashes on three degrees; see [[diatonic-chords]] or let [[037-lab]] compute them.

## How to do it

### SID-Wizard

- **Chord table** (`C=+F5` or `C=+K`): entries `$00–$7D` = semitones up, `$80–$FF` = semitones down, `$7F` = loop the chord forever, `$7E` = return from the chord to the instrument's arp table. `C=+N` toggles *note-mode*, where you set the root note outside the table and type the chord's notes as notes (select editing mode with Space). `Shift+K/L` selects a chord from anywhere, `+`/`-` inside the table.
- **Assign it**: each instrument has a *default chord number*; override per note with `$70–$7F` in the instrument column or `$07 xx` in the effect column.
- **Speed**: `$0C xx` (big effect) or `$Cx` (small effect) sets the chord/arpeggio speed.
- **Arps in the instrument** instead: the Arp column of the WF-ARP-Detune table (`$01–$5F` up, `$E0–$FF` down, `$81–$DF` absolute pitch, `$7F` jump to the chord) — see [[instrument-tables]]. Note: an arp entry cancels a running slide or vibrato.
- The chord table is not available in the Light, Bare and Demo player types ([[sid-player-routine]]).

(source: [[s-sid-wizard-manual]])

The SID-Wizard book's arpeggio instrument: WF-ARP `11 7F` (triangle, jump to the default chord), chord table `00 03 07 0C 07 03` ending in `7F` (loop) — "it runs quite fast", so set chord speed `02` in the instrument or in the WF column left of the `7F`; attack `8`, release `B`. Chords "are essentially arpeggios in SID-Wizard, but they don't depend on instruments"; `7E` returns to the wave table's next row; note-mode (default since 1.5, `C=+N` toggles) lets you type or play chord notes from a MIDI keyboard with the root shown above the table (source: [[s-witchmaster-creating-chiptunes-with-sid-wizard]]).

A player author's confirmation of the idiom: in [[linus-walleij]]'s SID player the arpeggio macro is a table of bytes that "represents the number of halftones to transpose the current note UPWARDS. For example macro 0x00 0x03 0x07 creates a minor chord"; the table "can loop or end", and the arpeggio step is skipped while the instrument's vibrato runs (source: [[s-walleij-sid-player-routine]]).

### GoatTracker

GoatTracker 2 removed v1's arpeggio *command*: "Everything that this command does can also be done with wavetables". A looping arp is a wavetable whose right bytes are the semitone offsets and whose left bytes keep the waveform: `41 00` / `00 04` / `00 07` / `00 0C` / `00 00` / `FF 02` (4-note pulse arpeggio, waveform unchanged in the loop); with delays in the left byte the arp slows — `21 00` / `02 03` / `02 07` / `02 00` / `FF 02` is "a delayed minor chord arpeggio with sawtooth waveform. Each step takes 3 ticks". Because the wavetable "is never skipped", arps keep time at any tempo (source: [[s-goattracker-readme]]).

### Furnace

The instrument's **Arpeggio** macro is a per-tick "pitch sequence" in semitones — the same table idea, with the waveform and duty in parallel macros ([[furnace]]; source: [[s-furnace-c64-docs]]).

### LSDj

- **`Cxy` chord command**: runs an arpeggio of base, +x, +y semitones once per tick: `C37` plays 0, 3, 7, 0, 3, 7… (minor), `C47` major, `C0C` = 0, 0, C (octave on every third step), `CC0` = 0, C alternating, `CCC` = 0, C, C; `C00` resets. The instrument's CMD/RATE slows it down (0 fastest, F slowest).
- **Table arpeggios** for anything longer than three notes or with its own rhythm: put semitone offsets in the table's transpose column (the manual's example forms a major chord) and loop with `H`; the table speed follows the groove selected with `G` ([[instrument-tables]]).
- Chains carry a transpose per phrase, so the same arp phrase serves every chord of a progression ([[orderlist]]).

(source: [[s-lsdj-manual]])

Before 9.1.0, `C` on noise instruments alternates between the base shape and base + value on every tick (`C01` on shape `FF` gives `FF`, `F0`, `FF` …) rather than a pitch interval; the table transpose column is `01–7F` up, `80–FF` down (sources: [[s-intense-tech-17-the-joys-of-noise]], [[s-intense-tech-09-lets-table-this-discussion]]). From 9.1.0, with the noise channel reorganised into ordered notes, `C` on noise arpeggiates like on pulse and wave, limited to the notes the channel has: `F 5` with `C12` gives F, G# and C — an F minor triad — and larger values span octaves (source: [[s-intense-tech-19-new-noise-and-910-news]]).

Two more [[intense-tech]] details: the speed setting began as FX/SPEED in version 7 (7.7.4), renamed CMD/RATE in version 8 (sources: [[s-intense-tech-12-scoping-out-new-features]], [[s-intense-tech-14-lets-appreciate-version-8]]); and `C37` followed by `Z10` on later steps plays the chord randomly as minor or major, possible since version 6 made the `Z` digits independent ([[randomization-and-probability]]; source: [[s-intense-tech-03-dont-sleep-on-z]]). [[sabrepulse]]'s tutorial introduces the command with `C07` on the first note of the lead — "magically transformed into a chord" — and suggests trying it on a couple more notes (source: [[s-sabrepulse-getting-started-with-lsdj]]).

Community practice (sources: [[s-chipmusic-tables-and-chords-threads]], [[s-infu-getting-started-with-lsdj]], [[s-intense-tech-06-groove-and-tick-tricks-part-1]]): LazierGunz's cheat sheet writes chords as hex transposes — the values are interval positions counted from 0, so a major-seventh table is `00 04 07 0B 0C 07 04 00` (C E G B C B G E); slow it with `G01` on the table's first line and groove `01` = `2/2` rather than doubling rows; `00 04 00 07 00 0B 00 0C` is a texture. The `C` command's speed is fixed, which is why tables win for anything expressive; danimal cannon: go down, out of order, add octave notes, use five-note patterns over more than an octave — "just don't go up the chord every time the same way". Arpeggios can also be phrases: a 3-tick groove and `H71`/`H5A` loops turn one phrase into a long arp. Infu's beginner pair: `C47` major, `C37` minor.

### Impulse Tracker / Scream Tracker 3

`Jxy` cycles base, +x, +y once per tick — the IT manual calls it "an effect similar to old C-64 chords" (source: [[s-it-manual]]): the Modsquad's chip lead has a chord channel of `J47` (major) and `J37` (minor) at volume 64 with `J00` to stop, and their rules are "chords in one channel — never two — and no percussion inside them" (source: [[s-tw077-chip-off-the-block]]). Pinion admits that for "really neato chords" `Jxx` is "a bit… shitty sounding" in a sample tracker — but on a looped noise sample with a long falling pitch envelope a column of `Jxx` makes analog-style sweeps ([[instrument-envelopes]]; source: [[s-tw081-it-tip-of-the-week]]). Trixter's reminder that "a chord isn't a thing, it's any combination of notes" applies: an arp is a chord spread in time (source: [[s-tw039-chord-theory-debate]]).

MOD and XM use `0xy` for the same command: ProTracker's help calls it "used to simulate chords … noisy and grainy on most samples, but ok on monotone ones" — `C-3 00047` C major, `037` C minor — and FT2 plays the note on tick 1, +x on tick 2, +y on tick 3 (sources: [[s-protracker-23d-help]], [[s-ft2-manual]]). ST3's manual says the same in its own letters: `Jxy` changes the pitch "50 times per second … best to use it with clear or tight-looped (chip) instruments. Old users of the Commodore 64 remember this effect which was used to make chords" (`J37` = C minor) (source: [[s-st3-manual]]). Two quirks players emulate: Fasttracker 2's arpeggio runs backwards (the second parameter's note comes first), and in ProTracker mode arpeggios that leave the Amiga range wrap around an octave (sources: [[s-openmpt-manual-compatible-playback]], [[s-openmpt-manual-song-properties]]).

### In the classic drivers (1986–1988)

- [[soundmonitor]]: an arpeggio is always eight steps of semitone offsets on the ARP/S page — minor `0c 07 03 00 0c 07 03 00`, "as if you played a chord with four fingers … A minor: A (0C), E' (07), C' (03), A (00)"; the note's option bit 3 turns it on and the byte after the last note picks the arpeggio (`08` first, `10` second, `18` third …). VGMPF calls arpeggios in Musicmaster "a first in an editor" (sources: [[s-64er-soundmonitor-article]], [[s-vgmpf-soundmonitor-tfmx]]).
- [[matt-gray-player]]: shared offset lists (`$00,$08,$12`; `$00,$08`; `$00,$04,$08`) with the instrument choosing table *and* how many entries to use (`$30` = table 0 × 3, `$22` = table 2 × 2); V4.2's PLEX tables `$07,$03,$00`, `$09,$05,$00`, `$08,$03,$00`, `$18,$0C,$00`, `$07,$05,$00`, `$07,$04,$00`, `$08,$05,$00` are Gray's "note or chord plex"; he liked "the arpeggio chords" in *Treasure Island Dizzy* (sources: [[s-sidin02-matt-gray-driller]], [[s-matt-gray-dominator-source]], [[s-c64com-matt-gray-interview]]).
- [[musicfile]]: `arp0–arp7` with a length byte first — `$02,$00,$03,$07` (minor), `$02,$00,$04,$07` (major), `$02,$00,$05,$08`, `$02,$00,$05,$09`, `$02,$00,$03,$08`, `$02,$00,$04,$09`, `$02,$00,$03,$06` — and one 24-step descending run; a `wavearp` (`$80,$10,$80,$10`) and a `pulsearp` beside the tone arpeggio (source: [[s-realdmx-sid-players]]). [[jeroen-tel]]: "By quickly switching between three notes on one channel, you saved two channels" (source: [[s-vgmpf-maniacs-of-noise]]).


## Heard in / history

The 50 Hz arpeggio is, for Newman, "perhaps more than any other, characteristic of chip music": composers "deployed rapid arpeggios cycling around two or more notes at 50Hz to simulate the effect of multiple notes playing simultaneously", the rate being "a function of the C64's processor and screen-update interrupt-system", not a musical choice — with Akesson's reminder that Bach simulated polyphony with arpeggiation in the Partita No. 2. [[martin-galway]]: "fast arpeggios, and chorusing/echoes" make three channels sound like more; [[rob-hubbard]]'s driver had an octave-arpeggio flag, and [[commando]]'s channel 2 is "pseudo-polyphonic chordal backing through rapid arpeggiation" (source: [[s-newman-driving-the-sid-chip]]). Magnar Harestad on [[jeroen-tel]]: "his way of using funky bass lines with lively leads and arpeggios" (source: [[s-hugi38-interview-jeroen-tel]]).

Seen from a synthesizer keyboard (2015): chord arps "will be out of reach because you can't play them by hand … I don't think I know of a single traditional arpegiator that is fast enough for the purpose" (n00bstar); a Nord Lead's arpeggiator, or 160 notes per second, is "more than enough" (chunter); and a hand-drawn four-step LFO on pitch — "prime-fifth-octave-fifth" — reproduces the sound on a rompler, its jump-or-glide option standing in for "the pitch bend instructions" (Murenius) (source: [[s-chipmusic-typical-sid-sounds]]).

### Who invented it, and the PWM trick

- SIDwave credits [[martin-galway]]: "In the process, Martin invented the chord, aka arpeggio — to play 3 or more notes in the same voice, very fast, one after another, so that it sounds like a chord. People from the UK called it the arpeggio, it was also known as wibble, or wibbles" (1984–85; source: [[s-recollection-brief-history-of-sid]]). de.wikipedia describes Soundmonitor's arpeggios the same way — "sehr oft zu hören" in C64 games (source: [[s-soundmonitor-lineage-wikis]]).
- [[matt-gray]]: "the note or chord plex where you go very quickly between 2,3 or even 4 notes to give the impression of a full chord being played. That sound became unique almost to the SID and everyone is using it as a retro sound now … And if you put a pulse width mod on it such as a sweep, the bubbling chord took on a life of it's own" ([[pulse-width-modulation]]; source: [[s-rvg-matt-gray-interview]]).


## Tips & pitfalls

- Choose inversions so the top notes of successive chords move by small steps: the chord channel then plays a hidden second melody for free.
- Use the diatonic formula per scale degree; keep a cheat sheet of inversions (`0 3 7 → 0 4 9 → 0 5 8` minor, `0 4 7 → 0 3 8 → 0 5 9` major).
- Too slow and it stops being a chord; too many notes in a chord thins each one out (an inference from the fusion principle — unverified beyond the 3-note examples in the source).

## Related

[[chord-inversions]] · [[diatonic-chords]] · [[chord-progressions]] · [[instrument-tables]] · [[channel-interleaving]] · [[furnace]]

## Sources

[[s-037-lab]] · [[s-sid-wizard-manual]] · [[s-goattracker-readme]] · [[s-witchmaster-creating-chiptunes-with-sid-wizard]] · [[s-newman-driving-the-sid-chip]] · [[s-intense-tech-17-the-joys-of-noise]] · [[s-intense-tech-09-lets-table-this-discussion]] · [[s-chipmusic-tables-and-chords-threads]] · [[s-infu-getting-started-with-lsdj]] · [[s-intense-tech-06-groove-and-tick-tricks-part-1]] · [[s-protracker-23d-help]] · [[s-ft2-manual]] · [[s-st3-manual]] · [[s-openmpt-manual-compatible-playback]] · [[s-openmpt-manual-song-properties]] · [[s-walleij-sid-player-routine]] · [[s-intense-tech-19-new-noise-and-910-news]] · [[s-intense-tech-12-scoping-out-new-features]] · [[s-intense-tech-14-lets-appreciate-version-8]] · [[s-intense-tech-03-dont-sleep-on-z]] · [[s-sabrepulse-getting-started-with-lsdj]] · [[s-furnace-c64-docs]] · [[s-chipmusic-typical-sid-sounds]] · [[s-hugi38-interview-jeroen-tel]] · [[s-64er-soundmonitor-article]] · [[s-sidin02-matt-gray-driller]] · [[s-matt-gray-dominator-source]] · [[s-realdmx-sid-players]] · [[s-vgmpf-maniacs-of-noise]] · [[s-c64com-matt-gray-interview]] · [[s-recollection-brief-history-of-sid]] · [[s-rvg-matt-gray-interview]] · [[s-soundmonitor-lineage-wikis]]
