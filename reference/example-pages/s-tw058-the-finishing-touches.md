---
title: "TW #58–59 — The Finishing Touches (Catspaw)"
type: summary
source-path: raw/traxweekly/TRAXWEEK.058, raw/traxweekly/TRAXWEEK.059
article: "#58 2. The Finishing Touches; #59 1. The Finishing Touches"
author: Catspaw / Rat
date: 1996-05-16 / 1996-05-23
tags: [traxweekly, technique, looping, frames, volume, retrig, s3m, impulse-tracker]
created: 2026-08-30
updated: 2026-08-30
---

# TW #58–59 — The Finishing Touches

[[catspaw]]'s two-part guide to "the finer technical points of writing module-based music", in ST3/IT notation (`| C#5 16 48 H83 |` = note, sample, volume, effect). Greg Heo later pointed readers here for frames and tempo.

## Key claims

**Part 1 (#58) — looping and transitions**
- Songs that loop or sit in playlists break when the last pattern sets `AFF` (speed 255) for a pause but never issues `C00`, and when the first pattern relies on the *default* speed/tempo/panning — defaults only apply at start, so on loop the song is still at speed 255. Fix: **initialise everything with commands** at the start — a silent dummy first pattern with `^^^` note cuts, `Xxx` pan positions, `T7D` and `A06` (tempo 125, speed 6) and a `C00` break; and put `C00` on the same row as the final `AFF` so the song pauses a moment then restarts cleanly. (The Cubic player stops instantly on `C00`, so give it a row or two at `AFF` first.)
- Speed changes mid-melody (`A06` → `A07`) sound abrupt. Slide the **tempo** down over the last beats instead (`T7A`, `T75`, `T70`, `T6C`, `T68`, `T64`, then back to `T7D` with the new speed): tempo doesn't disturb volume slides and retrigs that depend on frames per row.

**Part 2 (#59) — spring cleaning, frames, volume slides, retrigs**
- Delete unused patterns (one early tune carried "almost 30k in dead patterns") and forgotten samples; `Alt-L` twice + clear block in ST3/IT.
- Use **effect memory**: a `00` parameter repeats the last value (`D10, D00, D00`; `G03, G00`; `Q43, Q00`) — "especially important for cutting down the size of chip songs"; beware shared memories (`Exy`/`Fxy` and others, format-dependent).
- Reset **global volume** at the start if you fade it out at the end, or the song loops silently.
- **Frames**: a tick of the clock; speed `Axx` = frames per row (speed 6 → 24 frames over four rows). A volume slide `D0y` moves the volume by y × (speed − 1) per row: at speed 6, `D01` = −5, `D02` = −10; `D03` at speed 4 = −9. Use this to plan fades exactly (`34 → D01 → 39 → D02 D02 → 59`), and combine volume-column values with slides and vibrato (`K20`, `UC3`, `E0E` …).
- **Retrig `Qxy`**: y = frames between retrigs, so at speed 6 `Q03` hits again exactly halfway through the row, `Q02` gives three hits; avoid odd speeds (5, 7, 9) because a half-row retrig is impossible — use tempo to get the feel. The x digit changes the volume per retrig (0 none, 1–5: −1 −2 −4 −8 −16, 6: ×2/3, 7: ×1/2, 9–D: +1 +2 +4 +8 +16, E: ×3/2, F: ×2). Recipes: ride cymbal `Q43` (32 → 24), snare roll `Q53` then `Q43`, and the tom "thwump" `QC2` from volume 04 up by 8 each frame.
- Cites Basehead's tracking-tips article in TW #15 as the model for pattern diagrams.

## Relevance

Source of the new technique pages [[song-init-and-looping]] and [[volume-slides]], and of the frame arithmetic in [[retrigger]] and [[tracker]].

## Pages touched

[[catspaw]], [[song-init-and-looping]], [[volume-slides]], [[retrigger]], [[tracker]], [[arrangement]], [[chiptune]], [[scream-tracker-3]].
