---
title: Index
type: index
created: 2026-08-30
updated: 2026-08-30
---

# Chiptune Wiki — Index

Catalog of every page. Read this first on any query. Pages link by slug (filename without `.md`); folders are only layers. Operations are logged in [[log]].

## Techniques

**Sound design (per voice)**
- [[instrument-design]] — instrument library beats note count; drum/lead/bass recipes
- [[wavetable-programming]] — waveform/arp tables, table drums with sourced recipes (SID-Wizard, GoatTracker, SID Factory II, Hubbard)
- [[pulse-width-modulation]] — duty-cycle sweeps, the SID shimmer, faking it with samples
- [[filter-programming]] — SID filter table, cutoff/resonance, keyboard tracking, filter priority
- [[hard-restart]] — clean note attacks on the SID: the envelope bug, ADHR/HR timer, GoatTracker and SID Factory II settings
- [[chip-samples]] — tiny looped waveforms for PC-tracker chiptunes; generating, normalising, tuning
- [[instrument-envelopes]] — IT/FT2 volume/pan/pitch envelopes: reverb tails, sirens, analog sweeps
- [[sample-offset]] — `9xx`/`Oxx`: timestretch, flange, reversed loops
- [[sample-looping]] — perfect loops, sustain loops, long loops in time
- [[multisampling]] — note translation tables, drum-kit instruments, sampling a piano
- [[ring-modulation-and-sync]] — ring / sync / test bits: datasheet behaviour, routing, noise lock-up
- [[detune]] — two-channel unison, fine detune values
- [[multispeed]] — running the player 2×–8× per frame
- [[opl-fm-instruments]] — AdLib/OPL two-operator FM patches in S3M and OpenMPT
- [[reverb-and-compression]] — reverb parameters with club numbers, compressor settings per sound, gated reverb and preverb, in-tracker equivalents
- [[recording-samples]] — sources, cabling, 1996 sound cards, formats and rates, mixdown media

**Pitch & expression**
- [[pitch-slide-and-portamento]] — `3xx`/`Gxx`/SID-Wizard `$01–$03`, calculated slides, legato
- [[vibrato]] — delayed vibrato, `4xy`, SID-Wizard vibrato types
- [[chord-arpeggio]] — the `0 3 7` trick, chord tables, arp speed
- [[lead-articulation]] — velocity by hand, `GF0` legato, late vibrato, the echo rule, drop-off tables, staccato and grace notes

**Channel economy & space**
- [[channel-interleaving]] — one channel, two jobs
- [[fake-echo]] — delayed quieter copies, same-channel echo
- [[octave-bass]] — `0 12 0 12` drive
- [[new-note-actions]] — IT NNAs: sustain and polyphony in one channel
- [[volume-slides]] — `Dxy` frame arithmetic, effect memory, channel/global volume
- [[song-init-and-looping]] — dummy first pattern, `AFF`+`C00`, tempo-slide transitions
- [[stereo-panning]] — L/R/both per channel, `O` command, pan per format (MOD fixed, XM per instrument, S3M/IT per channel)

**Timing & feel**
- [[shuffle-funktempo]] — swing via FunkTempo / tempo programs / speed alternation
- [[sidechain-pump]] — volume ducking on the beat
- [[retrigger]] — LSDj `R` retrig/resync: rolls, stutters, echo
- [[randomization-and-probability]] — LSDj `B` MayBe and `Z` RandomiZe

## Concepts

**Chiptune basics**
- [[chiptune]] — what the word means: chip music vs tiny sample modules; 1995–96 scene history
- [[tracking-workflow]] — learn, write, release: the scene's advice
- [[sample-ripping]] — taking samples from other modules: practice, the 1995–96 debates, etiquette, legal notes
- [[realism-in-tracked-music]] — the 1996 "realism" debate: positions, Nyquist and sample rates, what works in tracker terms
- [[tracker-scene-history]] — the PC scene 1995–98 in its own words: origins, FTP/BBS channels, ratings, compos, the 1995 tracker wish list, the 1997–98 debates
- [[compos]] — compo format (sample pack, limits, votes), what they train, the chiptune glut
- [[commercial-tracking]] — the 1997–98 "commercially viable?" debate: real cases and MarkVM's release-quality workflow
- [[live-tracking]] — pattern switching on cue, instruments over the module, channel cuts, keyboard through FT2

**Tracker basics**
- [[tracker]] — rows, patterns, instruments, effects, note naming
- [[orderlist]] — sequence, transposes, jumps, subtunes
- [[instrument-tables]] — SID-Wizard's wave/pulse/filter tables and value schemes
- [[adsr-envelope]] — the SID envelope, timing table, worked examples, per-note overrides
- [[sid-player-routine]] — player types, rastertime, memory, calling exported tunes
- [[effect-command-crosswalk]] — the same effects in MOD/XM numbers and S3M/IT letters, side by side
- [[sync]] — LSDj link/MIDI/analog/keyboard sync, SID-Wizard MIDI clock
- [[midi-in-trackers]] — IT MIDI output: controllers, `Zxx`/`SFx` macros, velocity vs volume, note-off timing

**Theory in semitones**
- [[semitone-math]] — intervals table, transposition
- [[scales-and-modes]] — scale formulas with moods, relative minor, pentatonics
- [[diatonic-chords]] — why it is not always `0 3 7`; sevenths, sus, power chords
- [[chord-inversions]] — voice leading and top-note control
- [[chord-progressions]] — tonic/dominant/subdominant, stock progressions by degree
- [[melody-writing]] — chord tones on strong beats, phrases, peaks
- [[rhythm-and-groove]] — strong rows, syncopation, off-beat stabs
- [[arrangement]] — 4s and 8s, transitions, finale transposition
- [[serial-composition]] — twelve-tone rows and the four row forms as tracker edits, serial percussion

## Entities

**Tools**
- [[sid-wizard]] — C64-native SID tracker by Hermit; full cheat sheet
- [[goattracker]] — GoatTracker 2 by Cadaver: full cheat sheet (commands, instrument parameters, the four shared tables, tick schedule, hard restart, playroutine options)
- [[vice]] — C64 emulator; key mapping, SID-Wizard setup from the book
- [[sid-factory-ii]] — cross-platform SID editor; instrument bytes, wave table, hard restart (from Chordian's tutorial)
- [[impulse-tracker]] — full reference: screens, effects, editing keys, samples, instruments, song variables
- [[scream-tracker-3]] — Future Crew's DOS tracker (1994): full cheat sheet (screens, effects, editor keys, MOD export)
- [[fasttracker-2]] — Triton's tracker (1994–97): effects, volume column, instruments, keys, quirks
- [[protracker]] — the Amiga tracker (1990–94): song model, effects with examples, keys, sample tools
- [[openmpt]] — the Windows tracker: formats, IT/MPTM effect and volume-column cheat sheet, tempo modes, filters, compatible playback
- [[schism-tracker]] — cross-platform Impulse Tracker reimplementation
- [[lsdj]] — Little Sound Dj for the Game Boy; full command and key cheat sheet, noise shape chart (old and 9.1.0 layouts), version history to 9.2, files/tools/cartridges
- [[liblsdj]] — 4ntler's save-file library and tools: `lsdsng-export`, `lsdsng-import`, `lsdj-wavetable-import` cheat sheet
- [[lsdj-wave-cruncher]] — DOTCNT's sample → 16-frame wavetable tool: `crunch` syntax and flags
- [[lsdpatch]] — LSDPatcher: ROM upgrades, kit editor (resampling, wave-RAM bug fix, half speed), `.lsdprj`, fonts, palettes
- [[furnace]] — multi-system tracker; its C64 docs as a cheat sheet: `10xx` waveform, `3xxx` duty, `4xxx` cutoff, `20xy`/`21xy` ADSR, envelope reset (`15xx`), macros, chip config
- [[siddump]] — register-dump tool for `.sid` files: `-tX` usage, output columns, the 1.05 multispeed limits, the Abs byte = GoatTracker's note numbering
- [[duet]] — the owner's own tracker: Impulse Tracker + SID-Wizard on one grid (basics only)
- [[037-lab]] — the owner's music-theory / melody-generator app
- [[soundmonitor]] — Hülsbeck's 1986 editor + Musicmaster driver (64'er 10/1986): full key/register cheat sheet, sound recipes, history and users
- [[tfmx]] — Hülsbeck's 1988 script-driven driver (C64 unreleased; Amiga, DOS, SNES, MusyX)
- [[matt-gray-player]] — Matt Gray's driver (Driller 1987 → PLAYER V4.2 / Dominator): pattern bytes, 8+8-byte instruments, arpeggio, vibrato, drum table, rastertime
- [[musicfile]] — the Maniacs of Noise driver by Charles Deenen ("MUSICFILE V01-07-1988"): tables, instruments and routines from the Cybernoid II source
- [[turbo-assembler]] — the C64 assembler that was MoN's "editor"
- [[rockmonitor]] — the scene's Soundmonitor with a sampled drum track (Dutch USA-Team, 1987); Digitronix lineage
- [[future-composer]] — Finnish Gold's 1988 editor on the first MoN player
- [[sidid]] — Cadaver's player-signature list: canonical names for every driver and editor (cheat sheet maps wiki pages to SIDId names)

**Chips & platforms**
- [[sid]] — MOS 6581/8580: register map, control byte, combined waveforms, test bit, filter, chip variants, history
- [[commodore-64]] — platform notes, frame rates, transfer hardware, noise fixes
- [[game-boy]] — platform notes, cartridges, link port, models and their sound (DMG / Color / Advance / SGB)
- [[game-boy-apu]] — the four channels, full register map, pitch/noise formulas, signal path and pops, quirks mapped to LSDj (Pan Docs)
- [[gravis-ultrasound]] — the scene's wavetable card: what the trackers, manuals and interviews say about it (RAM budgets, `S8x` panning, the GF1 mixing myth, `.pat` patches)

**Formats**
- [[sid-format]] — `.sid` export and calling convention, SID-Maker and SWMconvert
- [[it-format]] — the `.it` module format (ITTECH.TXT), limits and semantics
- [[s3m-format]] — the `.s3m` format (TECH.DOC): header, C2Spd, periods, packed patterns, AdLib instruments
- [[mod-format]] — the ProTracker `.mod` layout, period table, limits and player quirks
- [[xm-format]] — FastTracker 2's `.xm`: instruments, envelopes, effects, quirks

**People**
- [[hermit]] — Mihaly Horvath, author of SID-Wizard and HerMIDI
- [[lasse-oorni]] — Cadaver, author of GoatTracker; the concise ADSR-bug explanation
- [[witchmaster]] — Mikael Norrgård, author of *Creating Chiptunes with SID-Wizard*
- [[chordian]] — Jens, SID Factory II tutorial series
- [[rob-hubbard]] — C64 composer-coder: wavetable drums, multiplexing, skydive
- [[martin-galway]] — Ocean's composer: PWM, ring mod, sample playback
- [[bob-yannes]] — designer of the SID chip
- [[linus-walleij]] — Triad; MIDIslave, the SID player pseudo-code, the "6581-only" hard-restart claim
- [[asger-alstrup]] — the 1995 register-dump examinations of the SID's triangle and noise waveforms (REU sampling, the 23-bit noise LFSR)
- [[jeroen-tel]] — WAVE, Maniacs of Noise co-founder: BASIC player at 12, studied Hubbard 1985–87, "average" filter settings, Turbo Outrun samples, Renoise in 2014
- [[charles-deenen]] — Maniacs of Noise co-founder and programmer of the first MoN routine; Interplay audio director
- [[andreas-varga]] — the SID Homepage; interviewed Bob Yannes by e-mail in 1996
- [[johan-kotlinski]] — author of LSDj; background, scene history and design decisions from the 2020 interview
- [[defense-mechanism]] — Game Boy musician, author of the Intense Tech LSDj tutorials
- [[infu]] — author of the *Getting started with LSDj* course
- [[sabrepulse]] — chiptune artist; beginner LSDj tutorial (pulse kick interleaved with bass, panning between notes)
- [[hypnogram]] — Game Boy musician; the original *Don't Sleep on Z* post, groove numbering convention
- [[4ntler]] — author of libLSDj
- [[jeffrey-lim]] — Pulse, author of Impulse Tracker; release dates 1995–99
- [[sami-tammilehto]] — Psi, author of Scream Tracker and TECH.DOC
- [[lars-hamre]] — ZAP, author of the original ProTracker and the MOD format doc
- [[peter-hanning]] — Crayon, ProTracker 2.1A–2.3d
- [[olivier-lapicque]] — ModPlug Tracker, the root of OpenMPT and Schism's engine
- [[storlek]] — original Schism Tracker developer
- [[pinion]] — Ryan Hunt, "IT Tip of the Week"
- [[greg-heo]] — "Introduction to Musical Theory" series
- [[zinc]] — Justin Ray / Radiance; IT percussion, stereo samples and studio tips, ImpromptuCompo
- [[trixter]] — Jim Leonard / Hornet
- [[basehead]] — Dan Grandpre; Kosmic/FM; ST3 mood-first workflow, *Lotus Position*
- [[maelcum]] — Kosmic musician, "Chord Theory?"
- [[necros]] — Andy Sega; FM co-founder, the Advanced Tracking Tips series, the scene's most-cited musician
- [[psibelius]] — Gene Wie, TraxWeekly editor
- [[leviathan]] — Renaissance/Kosmic, modal and chord theory
- [[catspaw]] — "The Finishing Touches": looping, frames, retrigs
- [[the-zapper]] — Force Ten; loops and extended samples
- [[skaven]] — Future Crew musician; ST3's AdLib song, IT releases, Remedy in 1997
- [[purple-motion]] — Future Crew's demo-music reference; Five Musicians member
- [[jugi]] — Jukka Kaartinen / Complex, *Dope* (TG 1995); keyboard-first workflow, six tips
- [[phoenix]] — Andrew Voss, Kosmic musician
- [[leinad]] — Daniel Falk / MAGE; Amiga-era Swede on GUS, FT2 and Extreme's Tracker; samples-first workflow, four channels for the compos
- [[nemesis]] — Andrew Wise / Renaissance, Kosmic; "professional, not realistic", chords first, 28–30 hours a song
- [[stalker]] — Ariel Gross / OTM, Defiance; Composer 669 → MultiTracker → ST3, the *Sonic CD* loop
- [[thehacker]] — Krisjanis Gale / Kosmic; GUS and MODEDIT in 1993, MultiTracker on a 386, samples lead the song
- [[island-of-reil]] — Jesse Rothenberg / Epinicion; eyewitness of the NAID 1995 music compo
- [[mosaic]] — Renaissance; 4th at NAID 1995 with *Tears*; judge tunes without the author's name
- [[ryan-cramer]] — Iguana / Renaissance; GUS returned and re-bought, chord pattern first, demo music as film music
- [[blaze-runner]] — Christian Desnoyers / PURE; AWE32 + FT2 + AWEplay to DAT, SABAM registration, vinyl plans
- [[perisoft]] — David Wiernicki / Defiance president (1995), Capacala (1997); two ST3 workflows, his side of the Basehead ripping row, IT "CD quality by diskwriting"
- [[beaner]] — Sean Cummins / ACiD, Epinicion; KingMod → ModEdit → ST3 3.21b, no new samples no song, drums first
- [[big-jim]] — James Storer / Valhalla, FM; guitar-first tracking, *Foreign Skys*, the 1994 sound-card ladder to a GUS
- [[claim]] — Defiance / Lithium coder-musician; FT2 from its first week, ST3 unusable on an SB Pro clone, the "FC fixation"
- [[populus]] — Nicolas Roberge; TraxWeekly co-founder (with Neurosis) and first interviewer, Epinicion/Defiance; the June 1995 "dumb techno" complaint
- [[amusic]] — Sotiris Varotsis; Bass Productions, Athens; organiser of the 20mc; Amiga-first taste
- [[lord-pegasus]] — Zack Smith; Kosmic/ACiD; PC speaker → Sound Blaster → ModEdit → ST3, Basehead's samples and phone lessons
- [[quarex]] — Drew Hunt; Kosmic/Epinicion/TFX, *PORK.MOD*; Maelcum's unedited log
- [[jase]] — Jason Chong; Oxygen/Enigma; won Music Contest 3 (1995) with an XM; idea → structure → samples workflow
- [[kal-zakath]] — John Townsend / Inferno; created and ran "Faces in the Crowd" (from #26)
- [[master-of-darkness]] — Todd Andlar; founder of AIM Higher, FITC interviewer; ST3 because FT2's IRQs fail
- [[mesonyx]] — Jon Dal Kristbjornsson, 15, Reykjavik; *Xixit*'s three tunes in a day; "one big sample" is not tracking
- [[smeghead]] — David Oranchak / Terraformer; ST3 stream-of-consciousness techno, 18 S3Ms, the four-rater complaint
- [[ender]] — Andrew Burke, Foundation (Albany NY); violin-trained newcomer of 1995, "impossible to track without any theory"
- [[paganus]] — Epinicion / Aim Higher; piano-and-chords writer from the Toronto BBS scene, on hero-worship and snobbery
- [[luv-kohli]] — Empyrean (Virginia); ModEdit → Whacker → FastTracker → ST3 lineage, BBS distribution, sample provenance
- [[vicious]] — founder of VSL (Toronto house/dance); "house music was born from stealing", GUS ACE and sample CDs
- [[fred-ink]] — Fred of iNK (Hampton VA); ST3 since 1994, quality over quantity, the overused Purple Motion beat
- [[deus-ex]] — founder of Chill Productions (Toronto, 1995), GUS/FT2 trance composer; the group Zinc later joined
- [[loki]] — Charles Odom, SPiCE / Radiance (Oregon); breakbeat and classical, "midi is too expensive"
- [[blackwolf]] — Bobby Tamburrino, Epinicion / Mystique; UGA pit percussionist, commercialism in 1995, the Olympic parody
- [[zalt]] — Tobias Garder (Stockholm), Icing'95 runner-up; FT2 from NoiseTracker, four channels over 28, FT2's broken MOD export
- [[mick-rippon]] — Newcastle (Australia) composition student; ProTracker to ST3/FT2, "a sample is only an instrument", Oz96
- [[shawnm]] — Shawn of NOISE; McGill percussionist, ST3, ear over theory, "do what you hear"; the "Serial Composition" author
- [[balrog]] — Samuel Cote; Kosmic then Ultrabeat; ST 2.23 → X-Tracker → FT2; trance; modules belong in games
- [[pariah]] — Edwin de la Vega, V.S.L (Toronto dance); "examine, don't rip"; MTM releases
- [[acidfrog]] — Cam Goodman, Radiance/Spice DJ; jungle in FT2 on a GUS MAX; MIDI vs tracking
- [[vadimvs]] — Vadim Shustov, Simbirsk; NOISE; ST3 on borrowed hardware; ripping as the scene's problem
- [[daedalus]] — Brian Bennetts, Neophyte/Epinicion; ModEdit → ST3 3.21; Tangerine Dream; "let that argument die"
- [[ganja-man]] — Sam Bashton, LoK founder; handbag house in XM; sort Hornet by style; the #64 history
- [[saxy]] — Courtney Risch, XX; first tune in FT2, orchestral niche, NAID 96 jury rules
- [[quantam-porcupine]] — Joshua Shagam; C64 Music Construction Set → Whacker Tracker → ST3; as few channels as possible
- [[scirocco]] — Ian Lyman; Tetra Compositor → MTM → FT2; "don't upload unless proud"; the five-star XM
- [[injekted]] — Brandon Balliett, ex-Zer0/Defiance; Ultrabeat's founder; "sounds like real vinyl"
- [[subhuman]] — Seth Miller; Ultrabeat co-founder; goa/trance; first release on *Lucid*
- [[clef]] — Phil Sweeney, Australia; two 20mc wins, Epinicion menu chips, OZ'96 16k; ST3 → IT
- [[rage]] — Harri Blom, Jade / Night55; 2nd at Assembly '95 with "Guild of Sounds"; never rips, dislikes timed compos
- [[fisherman]] — Matt Overington, MindTap; the "Thai tracking scene" of 1996, ModEdit → ST3 → IT
- [[vegas]] — T.J. Lerner, Mystique; IT saved as S3M, theory "improved tenfold", three tips (volume tail, centred bass/drums, even retrigs)
- [[ryan-sprott]] — founder of Grey (not Ryan Cramer, not Pinion); FT2, pro-ripping, the MC4 player controversy
- [[liam-the-lemming]] — Liam Hesse, S!P / Mach One; *AutoEmotive*, Bass Productions to Mach One with AmusiC, TP5 and NAID '96
- [[u4ia]] — James Young / F8; Amiga SoundTracker veteran, FT2 2.06, jungle, the 1994 retirement and the F8 hype experiment
- [[cosmic]] — Matthias Ksoll, Radical Rhythms; ~100 DMF/XM tracks, FT2 as "pt clone", GUS 2.4 + daughterboard
- [[mikmak]] — Jean-Paul Mikkers, author of MikMod / MikIT; ST3 as S3M replay reference, the 1997 Windows/MP3 forecast
- [[khyron]] — Paul Schultz, Kosmic; builds Moogs, MIDI versus tracking, the 1 MB GUS ceiling
- [[mental-floss]] — Andrew McCallum, Kosmic; playing tracked music live (mute/unmute, two GUS PCs, CS1x), IT wishes, POTS
- [[popcorn]] — Chris Campbell; TraxWeekly editor 1995 (Populus → Popcorn → Psibelius), six early interviews, Hornet/MC3, 20mc sponsor
- [[atlantic]] — Barry Freeman; FITC tips writer/reviewer (Neophyte, Aim Higher), "Not So Advanced Tracking Tips", sparked the chord debate
- [[dennisc]] — Dennis Courtney; FITC interviewer (#29–#41), "Chiptunes Aren't Dead!"
- [[mellow-d]] — Jaakko Manninen; FM co-founder, the "virtual band" idea, by-ear tracker
- [[behemoth]] — David Menkes; TW staff writer, "Realism in MODs", the commercial-viability debate, Mikmak/newbie interviews
- [[chris-huelsbeck]] — Shades, Soundmonitor, The Final Musicplayer, TFMX; Rainbow Arts; PWM "the holy grail"; dated timeline 1984–1998
- [[matt-gray]] — Driller, Last Ninja 2, Dominator; own driver from late 1986; System 3 and Codemasters; the 2014 source release
- [[reyn-ouwehand]] — MoN member 1989–90, then System 3; Rubicon with Tel
- [[laxity]] — Thomas E. Petersen: from Hubbard's player at 14 to his own driver; MoN since 1990; SID Factory
- [[johannes-bjerregaard]] — Danish composer with his own driver; first non-founding MoN member (1988)

**Groups & events**
- [[the-modsquad]] — satirical chiptune seminar authors
- [[kosmic]] — Kosmic Free Music Foundation
- [[hornet]] — Hornet archive / Demonews
- [[future-crew]] — the Finnish demogroup behind Scream Tracker 3
- [[triton]] — Fredrik Huss and Magnus Högdahl, FastTracker 2
- [[maniacs-of-noise]] — Tel and Deenen's group: founding, division of labour, CDs, the 2014 line-up
- [[20-minute-chip-compo]] — 20mc: origin, rules table, three 1995 result tables, the stop and the bi-weekly return
- [[five-musicians]] — FM: Necros, Mellow-D, Big Jim, Basehead, Purple Motion (1995)
- [[epinicion]] — Psibelius's newcomer-friendly group; TraxWeekly's early interviewers
- [[defiance]] — Zer0's 1994–95 group: Perisoft president, Stalker, Claim; its early TraxWeekly column
- [[esper-division]] — Montreal two-man band (de Brienne, Jean-Claude): lyrics over tracked pieces on stage; 11th veteran at MC3
- [[ultrabeat]] — music-only techno group (1996): *Lucid*, *Happiness is a 303*, FM as template, Balrog
- [[noise-group]] — N.O.I.S.E., Shawn's Quebec group with a TraxWeekly column; VadimVS
- [[lok]] — Ganja Man's UK jungle group; Acidfrog "in limbo"
- [[renaissance]] — early PC demo group (The Sound Barrier BBS, *Amnesia*, MultiTracker); Nemesis, Mosaic, Ryan Cramer, Leviathan; "serious coma" by March 1995
- [[aim-higher]] — Master of Darkness's Toronto newcomers' group (1995), home of the Faces in the Crowd crew; *Foundation* and *Unification* disks
- [[rainbow-arts]] — the German developer that hired Hülsbeck (Giana Sisters, Katakis, R-Type, Turrican)
- [[system-3]] — Mark Cale's Last Ninja house: Matt Gray exclusive 1987–89, then Maniacs of Noise
- [[hewson]] — MoN's first client (Battle Valley, Cybernoid I/II); Tel's employer 1987–90; Gray's Maze Mania and Deliverance
- [[codemasters]] — the Darlings' budget label that made Gray write his own player
- [[compunet]] — the UK C64 online service where Matt Gray's demos found him work

**Publications**
- [[traxweekly]] — 1995–98 tracker-scene newsletter (archive in raw/)
- [[hvsc]] — High Voltage SID Collection, the C64 music archive
- [[c64-programmers-reference-guide]] — the 1982 PRG: chapter 4 (sound), Appendix O (the 6581 datasheet), its slips, the devili transcription
- [[pan-docs]] — the gbdev Game Boy hardware reference (CC0); audio section ingested
- [[intense-tech]] — Defense Mechanism's LSDj tutorial series (2018–2021); all 21 articles ingested (plus an unlisted draft)
- [[chipmusic-org]] — the chip-music forum; five LSDj thread summaries
- [[commodore-zone]] — British C64 magazine of the mid-1990s; the Tel, Galway and Hubbard interviews
- [[sid-homepage]] — Andreas Varga's sidmusic.org (1996–): the Yannes interview, composer interviews, Alstrup's waveform examinations, Appendix O, the patent
- [[64er]] — the German C64 magazine: 1986 music contest (Shades), Soundmonitor as Listing des Monats 10/1986, Tel interview 3/91
- [[sidin]] — Stefano Tognon's SID e-zine (15 issues, 2002–2015); #2 documents Matt Gray's Driller routine

**Songs**
- [[commando]] — Hubbard 1985: drums multiplexed over three voices, no kick
- [[monty-on-the-run]] — Hubbard 1985: skydive + octave arpeggio, pitch-bend code
- [[sanxion]] — Hubbard 1986: bass with a noise attack = bass + hi-hat
- [[helikopter-jagd]] — Galway 1986 (as "Cyclone", 1984): the first pulse-width sweeps; a Neverending Story B-side
- [[the-grey-note]] — Necros: sax from sampled passages + offsets; the un-rippable sample; realism exhibit
- [[shades]] — Hülsbeck's 64'er contest winner (February 1986), typed in with SMON
- [[great-giana-sisters]] — 7 songs + 15 SFX from Soundmonitor into The Final Musicplayer; reggae and True Blue; 6581/8580 notes
- [[driller]] — Matt Gray, 1987 (Incentive): four weeks around the Great Storm; the SIDin-documented player
- [[last-ninja-2]] — Matt Gray, 1988 (System 3): Central Park first, 14–16 weeks, his proudest work
- [[dominator]] — Matt Gray, 1989 (System 3): dance influence; subtune 6 source released 2014 (CC BY-NC)
- [[cybernoid]] — Jeroen Tel, 1988 (Hewson): the first 'behind the notes' video
- [[cybernoid-ii]] — Jeroen Tel, 1988 (Hewson): two songs in MUSICFILE V01-07-1988; instrument rows, drums and chords as numbers

## Summaries (one per ingested source)
- [[s-sid-wizard-manual]] — SID-Wizard 1.8 user manual
- [[s-037-lab]] — 0 3 7 lab techniques & theory cards
- [[s-traxweekly-archive]] — TraxWeekly archive index
- [[s-lsdj-manual]] — Little Sound Dj v9.2.6 operating manual
- [[s-duet-readme]] — DUET README (basics)
- [[s-it-manual]] — Impulse Tracker User's Manual (IT.TXT)
- [[s-it-hints]] — Impulse Tracker HINTS.TXT (Pulse, Greebo, StereoMan, Onix4MAN, Nacho Segura …)
- [[s-ittech]] — ITTECH.TXT, the .it format reference (semantics only)
- [[s-goattracker-readme]] — GoatTracker v2.72 readme (Cadaver)
- [[s-witchmaster-creating-chiptunes-with-sid-wizard]] — *Creating Chiptunes with SID-Wizard*, 2nd edition (WitchMaster & Hermit, 2014)
- [[s-chordian-sf2-instruments]] — Chordian: Composing in SID Factory II, part 4 — instruments (2022)
- [[s-lemon64-hard-restart-threads]] — Lemon64: SID and ADSR re-triggering? (2008) / Hard restart – what's the story? (2015)
- [[s-newman-driving-the-sid-chip]] — Newman: Driving the SID chip (G|A|M|E 2017)
- [[s-c64-prg-chapter-4-sound]] — C64 Programmer's Reference Guide ch. 4 (1982): POKE register model, frequency/pulse formulas, ADSR table and presets, filter, OSC3/ENV3 tricks, sync/ring examples
- [[s-mos-6581-datasheet]] — the MOS 6581 datasheet (= Appendix O): register map, formulas, control bits, Table 2 envelope rates, filter, readbacks, envelope presets
- [[s-hvsc-sid-file-format]] — HVSC SID file format: PSID v1–v4 / RSID header fields, flags, RSID rules
- [[s-walleij-sid-player-routine]] — Walleij: a MIDI-driven SID player in pseudo-code, macros, note table, the "6581 only" hard-restart claim
- [[s-chipmusic-c64-music-for-dummies]] — chipmusic.org: ant1's SID-Wizard 1.0 beginner tutorial (2012) with three instruments, SID-Maker, VICE engines
- [[s-sid-wizard-charts-and-tables]] — Charts and Tables for SID-Wizard 1.6: table value schemes, full key map, SDI layout, 1.6→1.8 differences, tempo→BPM

**SID leftovers — forums, docs, waveform measurements**
- [[s-lemon64-learning-sid-sound-design]] — Lemon64 (2020): how to learn SID sound design — datasheet, PRG examples, the book, siddump and SIDViz, Lasse's order, sync from the bass
- [[s-lemon64-sid-wizard-instrument-recommendations]] — Lemon64 (2021): SID-Wizard example instruments (the 808 kick is an image), SID-Maker export troubleshooting, VICE 3.1 → 3.5
- [[s-furnace-c64-docs]] — Furnace's C64 system and instrument pages: AND-mixed waveforms, envelope reset, the 6581 software-PCM channel, effects and macros
- [[s-chipmusic-typical-sid-sounds]] — chipmusic.org (2015): what makes a sound "SID" — PWM, dry signal, two-channel chorus and delay, the 10 % → 50 % lead
- [[s-chipmusic-sid-music-hints-n-tips]] — chipmusic.org (2013): siddump usage and 1.05, 4mat's reading of a 5× tune, the "metal noise" control-byte list, hi-hats
- [[s-ucapps-wavetable-sounds-tutorial-1]] — Thorsten Klose: the *Auf Wiedersehen Monty* bass drum frame by frame from a siddump trace; the 30 ms gate delay
- [[s-commodore-64-eu-sid-chip]] — commodore-64.eu: 6581 vs 8580 table (12 V / 9 V, 1982 / 1987), the "sample bug", ARMSID / SwinSID Nano / SIDFX — secondary source
- [[s-sidmusic-alstrup-waveform-examinations]] — Alstrup (1995): REU sampling of `$D41B`; triangle counter and the test bit; the 23-bit noise LFSR, its period and its delayed reset

**SID chip and composer interviews (sidmusic.org, Remix64, Hugi)**
- [[s-sidmusic-yannes-interview]] — Bob Yannes to Andreas Varga (1996): design goals, oscillator/waveform/envelope/filter internals, Pro-1-measured ADSR rates, the AND-ed waveforms, the filter's failure, Ensoniq
- [[s-sidmusic-creation-of-the-sid-chip]] — Rindeblad: January 1981 project, spring 1981 start, 4–5 months, the inaccurate spec
- [[s-sidmusic-hubbard-interviews]] — Commodore Zone (c. 1997) + Happy Computer 7/86: assembler and no editor, the Commando night, three phases, Sanxion's origin, samples, SidPlay as archive
- [[s-sidmusic-galway-interviews]] — Commodore Zone 6–7 + Happy Computer 11/86: Ocean 1984, Zeus 64 and C128D, samples via the volume register, first PWM sweeps, Parallax, "that damn filter"
- [[s-sidmusic-jeroen-tel-interviews]] — Commodore Zone June 1997 + 64'er 3/91: founding Maniacs of Noise, Turbo Outrun, average filter settings, CDs, Probe Software
- [[s-remix64-galway-interview]] — Neil Carr (2001): the filter, the "school band effect", Arkanoid's samples, Street Hawk, on remixes
- [[s-hugi38-interview-jeroen-tel]] — Magic/Hugi #38 (2014): biography, studying Hubbard, composing in assembly, MoN in 2014, X and Assembly 2012
- [[s-pandocs-audio-overview]] — Pan Docs, Audio Overview: channels, triggering, envelope, length timer, period values
- [[s-pandocs-audio-registers]] — Pan Docs, Audio Registers: NR10–NR52 and wave RAM bit by bit, pitch and noise formulas
- [[s-pandocs-audio-details]] — Pan Docs, Audio Details: DACs, mixer, HPF, sweep/duty/LFSR internals, GBA differences, obscure behaviour
- [[s-st3-manual]] — Scream Tracker 3.2 User's Manual (ST3.DOC): effects, editor, MOD export, AdLib
- [[s-st3-tech-doc]] — TECH.DOC: the S3M format, C2Spd, periods, mixing
- [[s-ft2-manual]] — FastTracker 2.08 manual (Urban Jonsson): effects, instruments, keys, FAQ
- [[s-protracker-23d-help]] — ProTracker 2.3d help file: screens, effects with examples, keys, tips
- [[s-protracker-23-readme-and-docs]] — PT 2.3A ReadMe and history, 2.0A effect list and MOD file format, version table
- [[s-tracker-history-notes]] — release lineages of PT, FT2, ST3, IT, Schism and OpenMPT with dates
- [[s-schism-tracker-wiki]] — Schism Tracker wiki: project, IT background, FAQ, links, config

**OpenMPT manual chapters**
- [[s-openmpt-manual-effect-reference]] — every MOD/XM/S3M/IT/MPTM effect, memory rules, waveforms, retrigger table
- [[s-openmpt-manual-module-formats]] — MOD, S3M, XM, IT, MPTM and which to choose; import-only formats
- [[s-openmpt-manual-compatible-playback]] — the quirks of FT2, IT, ST3 and ProTracker that players emulate
- [[s-openmpt-manual-zxx-macros]] — `Zxx` macros and the resonant filter
- [[s-openmpt-manual-about-openmpt]] — features, limitations, ModPlug history
- [[s-openmpt-manual-instruments]] — sample map, envelopes, NNAs, filter and swing settings
- [[s-openmpt-manual-samples]] — sample tools, loops, auto-vibrato, draw mode, OPL instrument editor
- [[s-openmpt-manual-song-properties]] — playback flags, mix levels, tempo modes, tempo swing

**Intense Tech articles (LSDj)**
- [[s-intense-tech-01-wave-synth-deep-dive-part-1]] — wave synth 1: harmonic series, SIGNAL/FILTER/CUTOFF/Q, the sine recipe
- [[s-intense-tech-02-wave-synth-deep-dive-part-2]] — wave synth 2: PHASE and Resync, DIST Clip/Fold/Wrap, LIMIT, VSHIFT
- [[s-intense-tech-06-groove-and-tick-tricks-part-1]] — ticks, grooves, Hypnogram's numbering, per-channel swing, `H` phrase length
- [[s-intense-tech-07-groove-and-tick-tricks-part-2]] — table grooves, 3/4 and triplets from grooves, the groove delay
- [[s-intense-tech-09-lets-table-this-discussion]] — tables: volume column, nested `A`, `A20` stop, even/odd-row stereo trick, attack tricks
- [[s-intense-tech-10-kicks-part-1]] — wave kicks, P/L/V and DRUM pitch, the `P`-then-`L 80` table, Kyoto kick, kick → bass
- [[s-intense-tech-11-kicks-part-2]] — LSDj 7: DRUM + transpose, wave/pulse snares and toms, sweep drums, noise kicks, layering
- [[s-intense-tech-13-kotlinski-interview]] — Kotlinski: background, LSDj's origins, live mode, milestone versions, the v8 roadmap
- [[s-intense-tech-17-the-joys-of-noise]] — noise shape chart, `S`/`P`/`C`/transpose semantics, the random mute, `Z` crashes, noise kick, retrig pulses
- [[s-intense-tech-18-adsr-makes-life-easier]] — LSDj 8.1.0 ADSR, 8.8.0 software volume, speed chart, transients, tremolo
- [[s-intense-tech-03-dont-sleep-on-z]] — `Z` worked examples (after Hypnogram): random vibrato, duty, panning, gating, PU2 melody, major/minor, sweep; the mod-4 wrap
- [[s-intense-tech-04-liblsdj]] — `lsdsng-export` / `lsdsng-import`: listing saves, per-song folders, working-memory rescue, building live-set saves
- [[s-intense-tech-05-wave-cruncher-instrument-library]] — crunched wavetables as a wave-channel sampler, the lsdjsynths `.snt` library, `lsdj-wavetable-import`
- [[s-intense-tech-08-dotcnts-wave-cruncher]] — the `crunch` command line: pitch argument, `--linear`/`--exp`/`--normalize`/`--channel`/`--analyze`, which samples work
- [[s-intense-tech-12-scoping-out-new-features]] — LSDj 7.7.4: `B` mayBe probabilities, FX/SPEED, oscilloscope, silky wave, `R8x`, wave finetune, 295 BPM
- [[s-intense-tech-14-lets-appreciate-version-8]] — LSDj 8: two-row screens, ADSR digits, `Z` on all but `H`, PLAY/STEP tables, CMD/RATE, LOOP POS, `xF` hop, no more three-`V` crash
- [[s-intense-tech-15-lets-mix-it-up-and-down]] — mixing on four channels: panning as space, octave separation, the snare transient, wave LIMIT `9`–`E` as volume, ADSR fade-ins
- [[s-intense-tech-16-cartridge-family]] — flash cartridges for LSDj: SD (Everdrive X5), USB (EMS, LinkNLoad32), flasher-based (insideGadgets + GBxCart), the bootleg warning; 2024 update
- [[s-intense-tech-19-new-noise-and-910-news]] — LSDj 9.1.0: ordered noise notes and the old→new conversion rule, `P`/`C`/`V` on noise, TICK vibrato step table, two-digit FINETUNE/LIMIT, FREE/STABLE removed
- [[s-intense-tech-20-lsdpatch]] — LSDPatch 1.10.4: ROM upgrade, `.lsdprj` song manager, kit editor with dithering and the wave-RAM refresh-bug fix, half-speed samples, fonts, palettes
- [[s-intense-tech-21-whats-new-in-lsdj-92]] — LSDj 9.2: compatible emulators, rewritten kit timing, PHASE PINCH/WARP/RESYNC/RESYN2, noise PITCH FREE/SAFE, ENV visualiser, RESYNC play mode, row queueing

**LSDj course and forum threads**
- [[s-infu-getting-started-with-lsdj]] — Infu's beginner course: sequencer, ENV, three noise drums, snare table, wave kick and bass, synth screen, silent chains
- [[s-sabrepulse-getting-started-with-lsdj]] — Sabrepulse's beginner tutorial (mirror): one song from bass to hats, cloning, `C07`, panning between notes, `PF1`+`K00` pulse kick, `EF` snare
- [[s-chipmusic-lsdj-faq]] — LSDJ FAQ thread (2010–11): `L` placement, volume/panning clicks, half-clocked sync, chords
- [[s-chipmusic-lsdj-advanced-tricks]] — Advanced Tricks thread (2012): channel economy
- [[s-chipmusic-noise-drum-threads]] — noise snare / noise-only drum kit threads (2014): recipes and layering
- [[s-chipmusic-tables-and-chords-threads]] — chord cheat sheet / learning tables threads (2015): arp tables, table grooves, think in ticks, `VFF`
- [[s-chipmusic-kotlinski-interviews]] — two Kotlinski interviews (2012, 2014)

**TraxWeekly articles — tips and tools**
- [[s-tw003-beginning-the-tracking-experience]] · [[s-tw012-advanced-tracking-tips]] · [[s-tw015-advanced-tracking-tips-ii]] · [[s-tw018-advanced-tracking-tips-iii]] · [[s-tw021-tracking-tips]] · [[s-tw032-not-so-advanced-tracking-tips]] · [[s-tw033-4channel-lives-on]] · [[s-tw042-impulse-tracker-v1-01]] · [[s-tw044-impulse-tracker-trivia]] · [[s-tw058-the-finishing-touches]] · [[s-tw059-tracking-hints]] · [[s-tw075-it-percussion-tips]] · [[s-tw077-general-tracking-tips]] · [[s-tw081-it-tip-of-the-week]] · [[s-tw086-hexadecimal-101]] · [[s-tw094-stereo-samples-in-impulse-tracker]] · [[s-tw096-studio-tracking-tips]] · [[s-tw098-impulse-tracker-investment]] · [[s-tw098-impulse-tracker-midi]] · [[s-tw100-tracking-on-impulse]]

**TraxWeekly articles — theory and composing**
- [[s-tw001-modal-and-chord-theory]] · [[s-tw007-the-importance-of-music-theory]] · [[s-tw039-chord-theory-debate]] · [[s-tw046-serial-composition]] · [[s-tw050-aesthetics-of-composition]] · [[s-tw072-composing-whole-modules]] · [[s-tw074-intro-to-musical-theory]] · [[s-tw087-music-theory-a-modern-approach]] (satire, #87–#97) · [[s-tw107-laymans-music-theory]]

**TraxWeekly articles — samples, panning, mixing, realism**
- [[s-tw009-samples-lameness-preconceptions]] · [[s-tw024-sample-ripping-debate]] (#24/#25/#64/#65) · [[s-tw025-loops-and-extended-samples]] · [[s-tw055-panning-debate]] · [[s-tw066-sound-recording]] · [[s-tw070-realism-debate]] (#70–#73) · [[s-tw074-motherboard-sampling]] · [[s-tw076-realism-in-mods]] · [[s-tw084-perfect-samples-the-piano]] · [[s-tw086-wrecking-samples-with-impulse-tracker]] · [[s-tw106-a-little-panning]] · [[s-tw118-reverb-and-compression]] · [[s-tw119-reverb-and-audio-gear]]

**TraxWeekly articles — chiptune and scene**
- [[s-tw005-what-its-like-to-be-a-pc-musician]] · [[s-tw011-how-to-enhance-your-music-collection]] · [[s-tw024-in-review-asm95]] · [[s-tw032-20-minute-chip-compo]] (#26–#33, #50) · [[s-tw032-tracker-survey]] · [[s-tw037-death-of-the-chiptune-debate]] · [[s-tw044-hornet-ratings]] · [[s-tw051-how-to-listen-to-tracked-music]] · [[s-tw064-potted-tracking-history]] · [[s-tw065-tracking-as-an-olympic-sport]] · [[s-tw077-chip-off-the-block]] · [[s-tw099-why-tracking-is-the-perfect-artform]] · [[s-tw114-live-tracking]] · [[s-tw114-commercial-tracking-debate]] (#113–#118) · [[s-tw115-tracking-semantics]] · [[s-tw118-tracking-the-format]] · [[s-tw032-fitc-complaints]]

**TraxWeekly interviews**
- [[s-tw001-interview-basehead]] · [[s-tw001-interview-phoenix]] · [[s-tw003-interview-five-musicians]] · [[s-tw003-interview-chuck-biscuits]] · [[s-tw009-interview-maelcum]] · [[s-tw010-interview-jugi]] · [[s-tw014-interview-pinion]] · [[s-tw018-interview-basehead]] · [[s-tw027-interview-basehead-lotus-position]] · [[s-tw027-interview-zapper]] · [[s-tw032-interview-zinc]] · [[s-tw041-interview-zinc]] · [[s-tw057-interview-catspaw]] · [[s-tw080-trax-mass-interview]] · [[s-tw105-newbie-interviews]] · [[s-tw109-interview-skaven]] · [[s-tw002-interview-leinad]] · [[s-tw004-interview-nemesis]] · [[s-tw004-interview-stalker]] · [[s-tw005-interview-thehacker]] · [[s-tw006-naid-opinion-interviews]] · [[s-tw007-interview-ryan-cramer]] · [[s-tw008-interview-blaze-runner]] · [[s-tw011-interview-perisoft]] · [[s-tw011-interview-beaner]] · [[s-tw013-interview-big-jim]] · [[s-tw015-interview-claim]] · [[s-tw015-interview-sv]] · [[s-tw016-interview-populus]] · [[s-tw017-interview-amusic]] · [[s-tw018-interview-lord-pegasus]] · [[s-tw019-interview-quarex]] · [[s-tw022-interview-jase]] · [[s-tw026-faces-in-the-crowd-intro]] · [[s-tw027-faces-in-the-crowd-master-of-darkness]] · [[s-tw028-faces-in-the-crowd-mesonyx]] · [[s-tw029-faces-in-the-crowd-smeghead]] · [[s-tw029-faces-in-the-crowd-esper-division]] · [[s-tw030-interview-ender]] · [[s-tw030-interview-paganus]] · [[s-tw031-interview-luv-kohli]] · [[s-tw031-interview-vicious]] · [[s-tw031-interview-fred]] · [[s-tw034-interview-deus-ex]] · [[s-tw035-interview-loki]] · [[s-tw040-interview-blackwolf]] · [[s-tw040-interview-zalt]] · [[s-tw041-interview-mick-rippon]] · [[s-tw041-interview-shawnm]] · [[s-tw042-interview-balrog]] · [[s-tw043-interview-pariah]] · [[s-tw044-interview-acidfrog]] · [[s-tw050-interview-vadimvs]] · [[s-tw052-interview-daedalus]] · [[s-tw052-interview-ganja-man]] · [[s-tw054-interview-saxy]] · [[s-tw054-interview-quantam-porcupine]] · [[s-tw054-interview-scirocco]] · [[s-tw054-interview-injekted-and-subhuman]] · [[s-tw055-interview-clef]] · [[s-tw060-interview-rage]] · [[s-tw060-interview-fisherman]] · [[s-tw062-interview-vegas]] · [[s-tw063-interview-ryan-sprott]] · [[s-tw066-interview-liam-the-lemming]] · [[s-tw067-interview-u4ia]] · [[s-tw087-interview-perisoft]] · [[s-tw090-interview-cosmic]] · [[s-tw103-interview-mikmak]] · [[s-tw111-interview-khyron]] · [[s-tw119-interview-mental-floss]]

**C64 legends — Hülsbeck, Matt Gray, Maniacs of Noise (drivers, sources, interviews)**
- [[s-64er-soundmonitor-article]] — 64'er 10/1986 "Musik wie noch nie": the Soundmonitor manual — keys, track/step table, bars at $B000, arpeggios, the 24 sound registers, demo sounds
- [[s-vgmpf-chris-huelsbeck]] — VGMPF timeline: Musicmaster 1985, Shades Feb 1986, sampler 1986–87, The Final Musicplayer July 1987, TFMX summer 1988, Rainbow Arts
- [[s-vgmpf-soundmonitor-tfmx]] — VGMPF: Soundmonitor's model, Musicmaster effects, Rockmonitor, its users; TFMX Editor (C64, unreleased); Giana Sisters' 7 songs + 15 SFX
- [[s-remix64-huelsbeck-interview]] — Neil Carr 2001: Shades and Rainbow Arts, "PWM is the holy grail", the filter lottery, composing basics
- [[s-emuwiki-huelsbeck-interview]] — Retrogaming Planet 2011: two C64s, hex with A-2/G#3 notes, the sampler, TFMX's per-note script and drum-before-bass trick
- [[s-sidin02-matt-gray-driller]] — SIDin #2 (2002): Tognon's reverse-engineering of the Driller routine — pattern bytes $FA–$FF, two 8-byte instrument tables, arpeggio, vibrato, 10–34 rasterlines
- [[s-matt-gray-dominator-source]] — Gray's own PLAYER V4.2 source (2014, CC BY-NC): bars, PLEX chord tables, drum table, hi-hat; the Reformation competition
- [[s-c64com-matt-gray-interview]] — C64.COM 2014: the sequencer approach, the "incorrect" vibrato, year-by-year games and timescales, Codemasters and System 3
- [[s-vgmpf-matt-gray]] — VGMPF: Soundmonitor and the Ariston driver before his own; gameography 1987–2010
- [[s-realdmx-sid-players]] — GitHub collection of recovered players: the Cybernoid II source in Deenen's MUSICFILE (constants, routines, instrument rows, drums, arps, filters), the MoN SFX player, the Driller listing in ACME
- [[s-vgmpf-maniacs-of-noise]] — VGMPF + C64-Wiki: MoN's founding, the Musicfile driver in Turbo Ass, 2–6 days and £100–1000 per game, roster with dates, Tel's three-channel quote, Deenen's page
- [[s-charles-deenen-interviews]] — Domination #11 (1998) and Designing Sound (2010): "the driver that I wrote", Turbo Assembler as editor, 2 days per SID, how MoN began
- [[s-cybernoid-behind-the-notes]] — the two 2014 videos (metadata) and the Lemon64 thread: driver by Deenen, notes by Tel, Turbo Assembler on screen
- [[s-recollection-brief-history-of-sid]] — SIDwave's 2015 memoir: Galway invents the "wibble", Hubbard's player structure, Soundmonitor as "the greatest gift", Rockmonitor's origin, TMC's MON player, multispeed, sampled drums two ways, JCH and hard restart
- [[s-vandalism63-matt-gray-interview]] — Jazzcat 2014: learning 6502 by disassembly, "a player is like a brand of guitar", the Sanxion bass-with-hat trick, Hewson's liquidation, System 3 → MoN, the pop years
- [[s-rvg-matt-gray-interview]] — RVG 2016: chord plex + PWM sweep, drums by waveform switching, vibrato as a routine, Laser Genius, tunes under 4 KB
- [[s-retrogamesmaster-matt-gray-interview]] — Peter Ward: game-by-game notes (LN2 13 tracks Jan–May 1988, Dominator's cut track, fees), the assembler workflow
- [[s-arcadeattack-matt-gray-interview]] — 2020/21: the LN2 brief, the NES port of his player, Reformation 1–3
- [[s-remix64-ninja-remix]] — Chris Abbott: why Ninja Remix was rescored by Reyn Ouwehand — "no room for two music drivers"
- [[s-csdb-huelsbeck-tfmx-thread]] — CSDb 2006: the C64 TFMX editor never leaked; 1987 vs 1988 dating
- [[s-csdb-soundmonitor-and-shades]] — CSDb release pages: downloads, October 1986, Shades 9.4/10, "massive impact" but "not a scene release"
- [[s-audiogang-huelsbeck-interview]] — G.A.N.G. 2011: "the first tracker-like music editor", self-taught, own scripting system
- [[s-chordian-sid-musicians]] — JCH's 2018 verdicts: Hubbard's freelance block, Galway's pulsating in Rambo, Tel's instruments; Hülsbeck and Gray "overrated"
- [[s-sidid-player-list]] — SIDId's names, authors and years for Soundmonitor/MusicMaster, TFMX and its scene editors, Matt Gray (+ Rodger), MoN/Deenen variants, Future Composer, Galway's Digidrums quote, the 1983–92 editors
- [[s-soundmonitor-lineage-wikis]] — tracker-history lineage (1.0 → 1.1 → 1.3 → Rockmonitor II → Digitronix), C64-Wiki.de keys and versions, de.wikipedia
- [[s-wikipedia-chris-huelsbeck]] — the encyclopedia article: 64'er 6/1986 contest announcement, TFMX with Peter Thierolf (unverified), concerts, discography

## Wanted pages (focus topics with no source yet)

These are deliberately unresolved links; ingest a source to fill them: [[nes-2a03]], [[amiga-paula]].

## Inbox
- `inbox/traxweekly-toc.md` — TraxWeekly articles with relevance flags; 184 rows link a summary or are marked skipped: every ★ article and every interview (the 16 of step 3 plus the 56 non-★ ones ingested on 2026-08-30) is done; the reviews, columns and letters remain open.
- `inbox/scout-sid-sound-design-2026-08-30.md` — SID sound-design candidates; all ten candidates and the "also seen" list ingested on 2026-08-30 (the last batch: Lemon64 #9/#10, Furnace docs, two chipmusic.org threads, uCApps, commodore-64.eu, Hugi #38, Remix64, and sidmusic.org's Yannes/Tel/Galway/Hubbard interviews and Alstrup's waveform pages); nothing open.
- `inbox/scout-lsdj-sound-design-2026-08-30.md` — LSDj sound-design candidates; all 21 Intense Tech articles, Infu's course, the chipmusic.org threads and Sabrepulse's tutorial ingested on 2026-08-30; only the old LSDj manuals (candidate 9) remain open.
- `inbox/scout-c64-legends-2026-08-30.md` — Hülsbeck / Matt Gray / Jeroen Tel candidates (tunes, drivers, documentation); everything ingested on 2026-08-30 except #15 (the Retro Hour podcast, audio only) and the fetch-blocked sightings (Forum64, Exotica, Kickstarter)
