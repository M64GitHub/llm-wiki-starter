#!/usr/bin/env python3
# Extract single TraxWeekly articles (by issue, contents number, title) into text files for reading during ingest.
# Edit the `targets` list, then: python3 tools/extract-traxweekly-article.py [outdir]   (default inbox/tw-extracts, git-ignore it)
import re, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, 'raw', 'traxweekly')
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'inbox', 'tw-extracts')
os.makedirs(OUT, exist_ok=True)
targets = [l.split('|') for l in """001|3|Interviews
003|4|Interviews
009|3|Samples, Lameness
009|6|Interview
010|4|Interview
014|6|Pinion
018|4|Basehead
027|2|Zapper
032|8|Interview with Zinc
041|6|Interview With Zinc
057|4|Interview with Catspaw
080|7|Mass Interview
105|7|Newbie Interviews
109|3|Skaven
033|2|4Channel Lives On
044|8|HORNET Ratings
045|7|The HORNET Response
007|2|The Importance of Music Theory
011|3|How to enhance your music collection
012|4|Impulse 1995
012|5|Advanced Tracking Tips
014|5|Trax Tutorial Update
014|7|Bass Productions
015|3|Advanced Tracking Tips II
018|2|Advanced Tracking Tips III
021|4|Tracking Tips
024|4|Ripping
024|5|Food for Tracking
025|5|Ripping
027|3|20 Minute Chip Compo
028|2|Minute Chip Compo
032|2|The 20 Minute Chip Compo
032|5|Tracker Survey
032|10|Not So Advanced Tracking Tips
033|3|Tracker Survey
044|3|Impulse Tracker Trivia
046|2|Serial Composition
050|5|Aesthetics of Composition
051|5|How to listen to tracked music
064|6|Sample Ripping
064|8|Potted Tracking History
065|1|Tracking as an Olympic Sport
065|2|Sample Ripping Settled
066|3|Tracking as an Olympic sport
066|4|Sound Recording
070|3|Realism
071|3|Realism in Tracked Music
072|2|The Realism Thang
072|3|Realism in Tracked Music
072|4|Composing Whole Modules
073|4|Realism
087|3|Music Theory
088|2|Music Theory
089|4|Music Theory
092|5|Music Theory
093|1|Music Theory
094|2|Stereo Samples in Impulse Tracker
094|3|Music Theory
096|3|Studio Tracking Tips
097|4|Music Theory
098|3|Impulse Tracker Investment
098|5|Impulse Tracker MIDI
099|5|Why Tracking is a Perfect Artform
100|7|Tracking on Impulse
107|2|Layman's Music Theory
110|7|Blitz Beat Productions
114|8|Live Tracking
114|9|Commercial Tracking
115|7|The Business of Tracking
115|8|Commercial Tracking
115|10|Tracking Semantics
118|1|Reverb and Compression
118|3|Tracking the Format
118|6|Is Tracking Commercially Viable
119|6|Reverb and Audio Gear
002|5|Interview
004|3|Interviews
005|4|Interviews
006|6|Interviews
007|5|Interviews
008|4|Interviews
011|6|Interviews
013|8|Interview
015|7|Claim
015|8|SV
016|4|Populus
017|4|AmusiC
018|5|Lord Pegasus
019|6|Quarex
022|2|Jase
026|4|Faces in the Crowd
027|2|Faces in the Crowd
028|1|Faces in the Crowd
029|3|Interview with Smeghead
029|4|Esper Division
030|8|Interview with Ender
030|9|Paganus
031|5|Interview with Luv Kohli
031|6|Vicious
031|7|Fred
032|9|Complaints
034|1|Interview with Deus Ex
034|2|Song Reviews
035|4|Interview with Loki
040|7|Interview with Blackwolf
040|8|Interview with Zalt
041|4|Interview with Mick Rippon
041|5|Interview with Shawn
042|6|Interview with Balrog
043|5|Interview with Pariah
044|10|Interview with Acidfrog
050|9|Interview with VadimVS
052|2|Interview with Daedalus
052|3|Interview with Ganja Man
054|4|Interview with Saxy
054|5|Interview with Quantam Porcupine
054|6|Interview with Scirocco
054|7|Interview with Injekted and Subhuman
055|4|Interview with Clef
060|1|Interview with Rage
060|2|Faces in the Crowd
062|10|Interview with Vegas
063|3|Interview with Ryan
066|5|Interview with Liam the Lemming
067|3|Interview with U4IA
087|7|Interview with Perisoft
090|2|Interview with Cosmic/RR
103|4|Interview with Mikmak
111|4|Interview with Khyron
119|5|Interview with Mental Floss""".split('\n')]
H1 = re.compile(r'^\s*/?-{1,3}\s*\[\s*(?:(\d+)[.)]\s*)?([^\]]+?)\s*\]')
H2 = re.compile(r'===\[\s*([^\]]+?)\s*\]===')
def norm(s): return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()
for issue, num, title in targets:
    f = f'{RAW}/TRAXWEEK.{issue}'
    lines = open(f, encoding='cp437', errors='replace').read().split('\n')
    heads = []
    for i, l in enumerate(lines):
        m = H1.match(l)
        if m: heads.append((i, m.group(1), m.group(2))); continue
        m = H2.search(l)
        if m: heads.append((i, None, m.group(1)))
    # skip the contents block: only headers after the first section header following a [Contents]
    cand = [h for h in heads if norm(title) in norm(h[2]) and (h[1] is None or h[1] == num)]
    if not cand: print('NOT FOUND', issue, num, title); continue
    h = cand[-1] if len(cand) > 1 and 'contents' in ''.join(lines[:cand[0][0]]).lower() else cand[0]
    # pick the last candidate that is not inside the contents list (contents entries lack the header dashes anyway)
    idx = heads.index(h)
    end = heads[idx+1][0] if idx+1 < len(heads) else len(lines)
    body = '\n'.join(lines[h[0]:end]).rstrip()
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    name = f'tw{issue}-{num}-{slug}.txt'
    open(f'{OUT}/{name}', 'w').write(body)
    print(f'{name}: {len(body.split())} words, lines {h[0]}-{end}')
