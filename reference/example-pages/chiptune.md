---
title: Chiptune — what the word means
type: concept
platforms: [general, pc-tracker, c64, gameboy, amiga]
tags: [chiptune, definition, history, aesthetics]
aliases: [chip music, chip tune, chiptunes, chips]
sources: [s-tw037-death-of-the-chiptune-debate, s-tw032-20-minute-chip-compo, s-tw064-potted-tracking-history, s-tw077-chip-off-the-block, s-tw076-realism-in-mods, s-037-lab, s-tw058-the-finishing-touches, s-newman-driving-the-sid-chip, s-pandocs-audio-overview, s-intense-tech-13-kotlinski-interview, s-chipmusic-kotlinski-interviews, s-openmpt-manual-module-formats, s-tw070-realism-debate, s-tw109-interview-skaven, s-tw033-4channel-lives-on, s-sidmusic-yannes-interview, s-sidmusic-hubbard-interviews, s-remix64-galway-interview, s-hugi38-interview-jeroen-tel, s-sidmusic-jeroen-tel-interviews, s-chipmusic-typical-sid-sounds, s-lemon64-learning-sid-sound-design, s-tw041-interview-mick-rippon, s-tw040-interview-zalt, s-tw055-interview-clef, s-tw054-interview-quantam-porcupine, s-tw005-interview-thehacker]
created: 2026-08-30
updated: 2026-08-30
---

# Chiptune

Two related things share the name:

1. **Music made on sound chips** — the [[sid]] of the [[commodore-64]], the [[game-boy-apu]], the NES, AY/YM chips — where every note is a register write from a player routine ([[sid-player-routine]]) and instruments are tables ([[instrument-tables]]). This is what the C64 and Game Boy halves of this wiki are about.
2. **Tiny tracker modules that imitate that sound** — the PC scene's meaning in the 1990s: an `.s3m`/`.mod`/`.xm` built from looped waveform samples of a few hundred bytes, so the whole song is a few kilobytes. DennisC in 1995: "the bleepy little s3ms and mods" made by "looping bits of bytes" — he once tracked one "using only st3.doc for samples"; the sound is "nostalgic … to those who remember earlier forms of personal-computer music" (source: [[s-tw037-death-of-the-chiptune-debate]]). The Modsquad's taxonomy of 1996 chip songs: Amiga-style 3-channel, "new-school" many-channel, non-chip samples sampled down, AdLib; their size chart gives ten stars to songs of 11–20 k and the ideal reaction is "I didn't know you could do that with 4k samples!" (source: [[s-tw077-chip-off-the-block]]).

A note on the word "8-bit" from [[pan-docs]]: it "does not refer to the bit depth of the sound generated, but rather that it has sound capabilities typical of 8-bit consoles" — the [[game-boy-apu]]'s channels are 4-bit, and the SID is an analog-filtered synthesizer (source: [[s-pandocs-audio-overview]]).

The techniques are the same in both worlds because the constraints are: few channels, simple waveforms, no reverb — hence [[chord-arpeggio]], [[channel-interleaving]], [[fake-echo]], [[pulse-width-modulation]] (or duty-switching samples), [[octave-bass]], [[instrument-design]] and, for the module kind, [[chip-samples]] plus disciplined effect memory to keep the file tiny — "especially important for cutting down the size of chip songs" ([[volume-slides]]; source: [[s-tw058-the-finishing-touches]]).

## History notes from the sources

- Chiptunes were "a cute novelty item" collected from Purple Motion, Skaven, the Zapper and [[necros]] until the weekly [[20-minute-chip-compo]] produced a flood of them in late 1995 — "chiptune burnout" for some, "bring on the crappy chiptunes" for others (source: [[s-tw037-death-of-the-chiptune-debate]]).
- The compo's own rules are the tightest period definition of a PC chiptune: ≤ 20 KB uncompressed, ≤ 4 channels, a shared pack of detuned chip samples, MOD/XM/S3M, made in 20 minutes; its organiser paused it after Christmas 1995 because people "complained that the scene was full of chiptunes, which were of a really bad quality", and restarted it bi-weekly in March 1996 (source: [[s-tw032-20-minute-chip-compo]]).
- Trixter of [[hornet]] in November 1995 called the compo the current trend in "bare-metal" tracking — "how fast you can build a tune with chip samples" — alongside the older four-channel constraint, which "requires more skill" (source: [[s-tw033-4channel-lives-on]]).
- Ganja Man's 1996 history gives the scene's etymology of the module kind: when the C64 generation moved to Amiga and Atari ST they "continued to write tunes very similar to those they had on the C64, what we now know as 'chip' tunes", before discovering they could sample any instrument (source: [[s-tw064-potted-tracking-history]]).
- The opposite pole in the same scene was "realism": multi-megabyte modules with sampled synths, argued over in #70–#73 ([[necros]]'s multisampled sax against "tracked music is inherently synthetic") and defended by Behemoth in 1996 (sources: [[s-tw070-realism-debate]], [[s-tw076-realism-in-mods]]; see [[realism-in-tracked-music]]).
- In 1997 [[skaven]] "made that little chip tune for the Emissions #3 music disk" (source: [[s-tw109-interview-skaven]]).
- An earlier dated example: [[thehacker]]'s *Alarm* (`ALRM_KLF`, 1994) is labelled a "chip tune" in his own list of releases (source: [[s-tw005-interview-thehacker]]).
- [[johan-kotlinski]] on the word in the early-1990s Swedish BBS scene: "chip music" then "was mostly synonymous with what is today known as keygen music, .mod files with tiny looped samples … considered neat and clever, but not something anyone would do exclusively". The Game Boy movement grew out of his CD-R label Bleep Street (1998), Goto80's *Papaya EP* on 7″ vinyl (2000, about a thousand copies), [[lsdj]] cartridges sold online and micromusic.net, until "it got recognized as a movement of sorts" (source: [[s-intense-tech-13-kotlinski-interview]]).
- Kotlinski again, in 2014: "communication through computer networks always was an important part of chip music culture" — 1980s bulletin boards, then micromusic.net, "very energetic around 2000" (source: [[s-chipmusic-kotlinski-interviews]]).
- The formats behind the module kind, in OpenMPT's history: MOD from Karsten Obarski's Ultimate SoundTracker via NoiseTracker and [[protracker]] ("one of the most widespread tracker formats (also due to its use in many computer games and demos)"), then S3M, XM and IT — see [[mod-format]], [[s3m-format]], [[xm-format]], [[it-format]] (source: [[s-openmpt-manual-module-formats]]).
- Today's browser-synth view of the same aesthetic: "three channels sound like a band" through the tricks in [[037-lab]] (source: [[s-037-lab]]).

## Chip music as a discipline, in the 1996 interviews

- [[mick-rippon]] (January 1996): "Chip tunes are a different art altogether. It shows how a composer can cope with limited resources … more of a challenge than an attempt to write an enjoyable piece of music"; and "There's as much shit 'non-chip' music as there is 'chip music'" (source: [[s-tw041-interview-mick-rippon]]).
- [[zalt]]: a good four-channel tune is worth more than a good multichannel one — "it's so much easier to make good tunes with 28 channels than 4"; he misses "the old amiga 4chn pops". A FastTracker 2 pitfall for the module kind: a friend's chiptune used sixth-octave notes, which the `.MOD` export turned into Bs in the fifth octave on the Amiga compo machine (source: [[s-tw040-interview-zalt]]; see [[fasttracker-2]], [[mod-format]]).
- [[clef]]'s reasons for writing chips: no sample worries, small files, "I like optimizing stuff like code, and the same with chip tunes"; menu chips for the [[epinicion]] disks; a 16k compo at OZ'96 (source: [[s-tw055-interview-clef]]).
- [[quantam-porcupine]]'s "as few channels as possible" aesthetic — one of the few statements of it outside the chip compos (source: [[s-tw054-interview-quantam-porcupine]]).

## The SID and the birth of the aesthetic

Newman's argument: "more than any other device, the SID chip is responsible for shaping the sound of videogame music" — against the "brutal atonality" of Atari's TIA (a 5-bit divider with mostly out-of-tune pitches) it offered a real subtractive synthesizer, and its composer-programmers' bespoke drivers turned its "affordances" (including the undocumented ones, like volume-register samples) into techniques: pseudo-polyphony by 50 Hz arpeggiation, channel sharing, wavetable drums, portamento. Karen Collins' description of the resulting "unique aesthetic": "screaming guitar-like square wave solos, full-length songs, [and] attempts to re-create traditional 'rock band' line-ups". Altice's caveat is worth keeping: "The output of the GameBoy, NES and Commodore 64 are now subsumed under the chiptune moniker, but the sonic character of those machines are far more unique" than that of later consoles — which is why this wiki keeps per-platform sections. The music outlived the games in archives such as [[hvsc]] and in hardware/software re-housings of the chip (SidStation, Therapsid, chipsounds, QuadraSID) that gain DAW integration but lose driver-level tricks (source: [[s-newman-driving-the-sid-chip]]).

## The afterlife of SID music, in the composers' words

- 1996: [[bob-yannes]], told of SIDPLAY and PlaySID by [[andreas-varga]], was "constantly amazed and gratified at the number of people who have been positively affected by the SID chip and the Commodore 64 … and who continue to do productive things with them despite their 'obsolescence'" (source: [[s-sidmusic-yannes-interview]]).
- 1997: [[rob-hubbard]] had heard ProTracker module renditions of his tunes ("Ace2 and Sanxion … very good") and used SidPlay as his own archive — the C64 and module worlds of the two definitions above meeting in one composer's listening (source: [[s-sidmusic-hubbard-interviews]]). [[jeroen-tel]] the same year: "The limits of the soundchip makes me wanna push it to its maximum" (source: [[s-sidmusic-jeroen-tel-interviews]]).
- 2001: [[martin-galway]] on why the scene survived — "Well you gotta admit those tunes are catchy. Catchy tunes will prevail. Modern game music is too obsessed with being like a film … There ought to be a game or two where the music is playing just for the heck of it"; on remixes, the arranger must add "creative influences of his own"; and "There's no way that original C64 music will be featured on Top Of The Pops. (famous last words?)" (source: [[s-remix64-galway-interview]]).
- 2014: Tel DJs at game events "remixing old and new Commodore 64 SID, gameboy and other '8bit music' / 'Chiptunes'" — the word now covering both chips in this wiki — and wants to be remembered for "composing extremely complex melodies, arrangements using extreme intervals without having to worry that those can't be played by real live musicians": the freedom that defines the idiom on any chip (source: [[s-hugi38-interview-jeroen-tel]]).

## The SID aesthetic in musicians' words (2015, 2020)

Asked what makes a SID tune sound like one, chipmusic.org answered with a list rather than a theory: "awesome buzzy ring modulator, flabby distorted filter, weird adsr, Pulse width modulation on your leads too!" (Jellica); "PWM is a *huge* part of the C64 sound", and the sound "is mostly used dry with the only effects being those you can make by hand in a tracker" — chorus and delay bought with extra channels ([[detune]], [[fake-echo]]); harsh, brittle digital synths imitate it better than warm analogue ones "since that's pretty much what the original hardware was" (n00bstar); and what a chip does that a synth does not is "bend and switch their pitches and tones at will" (chunter) (source: [[s-chipmusic-typical-sid-sounds]]). Against the mystique — "pure magic … out of the 29 parameters available" — a Lemon64 composer's reply: "there are only 4 waveforms, and typically waveforms only change a couple of times per instrument (if at all) It's in the overall composition" (source: [[s-lemon64-learning-sid-sound-design]]).

## Related

[[chip-samples]] · [[20-minute-chip-compo]] · [[compos]] · [[tracker-scene-history]] · [[scream-tracker-3]] · [[protracker]] · [[the-modsquad]] · [[traxweekly]] · [[realism-in-tracked-music]] · [[tracking-workflow]]

## Sources

[[s-tw037-death-of-the-chiptune-debate]] · [[s-tw032-20-minute-chip-compo]] · [[s-tw064-potted-tracking-history]] · [[s-tw077-chip-off-the-block]] · [[s-tw076-realism-in-mods]] · [[s-037-lab]] · [[s-newman-driving-the-sid-chip]] · [[s-pandocs-audio-overview]] · [[s-intense-tech-13-kotlinski-interview]] · [[s-chipmusic-kotlinski-interviews]] · [[s-openmpt-manual-module-formats]] · [[s-tw070-realism-debate]] · [[s-tw109-interview-skaven]] · [[s-tw033-4channel-lives-on]] · [[s-sidmusic-yannes-interview]] · [[s-sidmusic-hubbard-interviews]] · [[s-remix64-galway-interview]] · [[s-hugi38-interview-jeroen-tel]] · [[s-sidmusic-jeroen-tel-interviews]] · [[s-chipmusic-typical-sid-sounds]] · [[s-lemon64-learning-sid-sound-design]] · [[s-tw041-interview-mick-rippon]] · [[s-tw040-interview-zalt]] · [[s-tw055-interview-clef]] · [[s-tw054-interview-quantam-porcupine]]




