#!/usr/bin/env python3
# Rebuild inbox/traxweekly-toc.md from raw/traxweekly/, keeping summary links of a previous TOC.
# Usage: python3 tools/triage-traxweekly.py raw/traxweekly inbox/traxweekly-toc.md
import re, os, sys, glob
d = sys.argv[1]
files = sorted(glob.glob(os.path.join(d, 'TRAXWEEK.*'))) + [os.path.join(d,'TW.025')] + sorted(glob.glob(os.path.join(d, 'TW-ART*')))
STAR = re.compile(r'\b(tutorial|tips?|hints?|how ?to|technique|guide|lesson|theory|chord|sampl|effects?|arrang|composition|composing|melod|harmon|drum|bass|mix(ing)?|pann|volume|loop|instrument|envelope|vibrato|portamento|filter|delay|echo|reverb|percussion|beat|rhythm|tempo|structure|song ?writing|seminar|advice|beginner|newbie|learn|midi|s3m|impulse|scream ?tracker|fast ?tracker|ft2|st3|it ?tip|chip|realism|ripping|recording|tracking|tracker survey|sound (design|quality)|frequenc|equali[sz]|compress|stereo|mastering)\b', re.I)
SKIP = re.compile(r'distribution|subscrib|staff|contribution|group members|closing|disclaimer|advertis|top 100|charts?$', re.I)
FLAG = [('interview', re.compile(r'interview|faces in the crowd|spotlight', re.I)),
        ('review', re.compile(r'review', re.I)),
        ('compo', re.compile(r'compo\b|competition|contest', re.I)),
        ('column', re.compile(r'column', re.I)),
        ('letter', re.compile(r'letter|feedback|mail', re.I))]
CAT = re.compile(r'^(letters?(\s*/\s*comments)?( and feedback)?|comments|general articles|articles|faces in the crowd|group columns|columns|competitions?|advertisements?|advertisement|trax.?culture|closing|interviews?|reviews?|editorial|news|features?|tutorials?|misc(ellaneous)?|the scene|scene news|charts)\b', re.I)
ART = re.compile(r'[\s_|\\/:~.\-<>]+')
rows = []; stats = {}
DATES = {}
try:
    for m in re.finditer(r'(TRAXWEEK\.\w+|TW\.\d+|TW-ART\d\.TXT)\s*\([\d.]+ kB\)\s*([^\n]+)', open(os.path.join(d,'archive-index.txt')).read()):
        DATES[m.group(1)] = m.group(2).strip()
except FileNotFoundError: pass
def clean_title(t): return re.sub(r'[\s.]+$', '', re.sub(r'^[\s.\-]+', '', t)).strip()
for f in files:
    name = os.path.basename(f)
    if not os.path.exists(f): continue
    txt = open(f, encoding='cp437', errors='replace').read()
    lines = txt.split('\n')
    m = re.search(r'Release date:\s*([^|\n]+?)\s*(?:\||$)', txt, re.I | re.M)
    date = DATES.get(name) or (m.group(1).strip() if m else '')
    # locate contents block
    start = None
    for i, l in enumerate(lines[:200] if not name.startswith('TW-ART') else []):
        if re.search(r'\[\s*contents\s*\]|^\*\*\* contents', l, re.I): start = i; break
    entries = []
    cat = ''
    if start is not None:
        for l in lines[start+1:start+90]:
            s = l.rstrip()
            if re.match(r'^\s*/?-{2,}\s*\[', s) or re.match(r'^\s*/-', s) or re.match(r'^\s*-\[\s*\d', s) or re.match(r'^\*\*\* ', s):
                break
            if not s.strip(): continue
            am = re.search(r'(?<![\w#])(\d{1,2})[.)]\s+(.+?)(?:\.{3,}\s*(.*)|\s+-\s+(.*)|\s*\((.*)\)\s*)?$', s)
            um = re.search(r'([A-Za-z"\'#].*?)\.{4,}\s*(\S.*)$', s)
            if am and clean_title(am.group(2)):
                title = clean_title(am.group(2)); author = clean_title(am.group(3) or am.group(4) or am.group(5) or '')
                entries.append((am.group(1), title, author, cat))
            elif um:
                title = clean_title(um.group(1)); author = clean_title(um.group(2))
                entries.append((str(len(entries)+1), title, author, cat))
            else:
                tail = ART.sub(' ', s).strip()
                tail = re.sub(r'\b[sS][tT][zZ]!?\b|\bsE\b|\bww\b', '', tail).strip()
                if tail and CAT.match(tail): cat = CAT.match(tail).group(0).title()
    else:
        # standalone article files: use *** section markers or first title-ish line
        subj = re.search(r'^Subject:\s*(.*)$', txt, re.M)
        entries.append(('1', (subj.group(1).strip() if subj else 'standalone file') + ' (standalone file, ASCII-art logos)', '', 'standalone'))
    for num, title, author, cat in entries:
        flags = []
        if STAR.search(title): flags.append('★')
        for fl, rx in FLAG:
            if rx.search(title) or rx.search(cat): flags.append(fl)
        if SKIP.search(title) or SKIP.search(cat): flags = ['skip']
        rows.append((name, date, cat, num, title, author, ' '.join(flags)))
    stats[name] = len(entries)
# dedupe identical rows and keep existing summary links from a previous TOC
seen=set(); dedup=[]
for r in rows:
    k=(r[0], r[3], r[4].lower())
    if k in seen: continue
    seen.add(k); dedup.append(r)
rows=dedup
prev={}
if os.path.exists(sys.argv[2]):
    for line in open(sys.argv[2]):
        c=[x.strip() for x in line.strip().strip('|').split(' | ')]
        if len(c)>=8 and c[0].startswith(('TRAXWEEK','TW')) and c[7]: prev[(c[0],c[3],c[4].lower())]=c[7]
zero = [k for k, v in stats.items() if v == 0]
print('files:', len(stats), 'articles:', len(rows), 'zero-article files:', zero)
print('★ flagged:', sum(1 for r in rows if '★' in r[6]))
out = ['# TraxWeekly — table of contents (triage)', '',
       "Source: `raw/traxweekly/` (mirror of https://resources.openmpt.org/traxweekly/). One line per article as listed in each issue's contents section. Generated 2026-08-30 by a script over the issue files (`triage traxweekly` regenerates it); flags are keyword guesses on the *title* only and need a skim before ingest. Ingested articles get a `[[s-tw…]]` link in the last column.",
       '', 'Flags: `★` = title suggests practical know-how (tips, technique, theory, samples, composing…); `interview`, `review`, `compo`, `column`, `letter` = article kind guessed from title/category; `skip` = boilerplate (distribution, subscribing, staff, ads).',
       '', f'Files: {len(stats)} · articles listed: {len(rows)} · ★ candidates: {sum(1 for r in rows if "★" in r[6])}', '',
       '| issue | date | category | # | title | author | flags | summary |', '|---|---|---|---|---|---|---|---|']
for r in rows:
    out.append('| ' + ' | '.join(x.replace('|', '\\|') for x in r) + ' | ' + prev.get((r[0], r[3], r[4].lower()), '') + ' |')
open(sys.argv[2], 'w').write('\n'.join(out) + '\n')
