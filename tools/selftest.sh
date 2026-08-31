#!/usr/bin/env bash
# Self-test for the starter: create a throwaway wiki from the template, lint it, build its site;
# then, if ../chiptune-wiki exists, build that wiki through the template's generator with the reference wiki.json.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tmp="$(mktemp -d)/selftest-wiki"
trap 'rm -rf "$(dirname "$tmp")"' EXIT
"$here/new-wiki.sh" "$tmp" "Selftest Wiki" >/dev/null
grep -q 'Selftest Wiki' "$tmp/CLAUDE.md" || { echo "FAIL: placeholder not replaced"; exit 1; }
grep -q '{{' "$tmp/CLAUDE.md" "$tmp/wiki.json" "$tmp/README.md" "$tmp/wiki/index.md" "$tmp/wiki/log.md" && { echo "FAIL: leftover placeholders"; exit 1; } || true
# a page with a wanted link and a summary, to exercise the pipeline
cat > "$tmp/wiki/summaries/s-test-source.md" <<'MD'
---
title: "Test source (summary)"
type: summary
source-url: https://example.org/test
author: Test
date: 2026-01-01
created: 2026-01-01
updated: 2026-01-01
---

# Test source

Key claim: the wiki builds.

## Pages touched

[[test-technique]]
MD
# a second summary whose ripple never landed — the unlanded-ripple check must find exactly this one
cat > "$tmp/wiki/summaries/s-test-unlanded.md" <<'MD'
---
title: "Test source, never rippled (summary)"
type: summary
source-url: https://example.org/unlanded
author: Test
date: 2026-01-01
created: 2026-01-01
updated: 2026-01-01
---

# Test source, never rippled

Key claim: a summary can name a page that does not cite it back.

## Pages touched

[[test-technique]]
MD
cat > "$tmp/wiki/techniques/test-technique.md" <<'MD'
---
title: Test technique
type: technique
tags: [test]
sources: [s-test-source]
created: 2026-01-01
updated: 2026-01-01
---

# Test technique

## What it is

A page that cites [[s-test-source]] and links a wanted page [[missing-page]] (unverified).

A markdown link whose label holds inline code: [`code-label`](https://example.org/x) — this
re-enters the inline renderer, so the placeholder list has to be shared (regression guard).

| key | value |
|---|---|
| `A` | 1 |

## Sources

[[s-test-source]]
MD
python3 - "$tmp/wiki/index.md" <<'PY'
import sys; p=sys.argv[1]; s=open(p).read()
s=s.replace("## Techniques\n", "## Techniques\n- [[test-technique]] — test\n").replace("## Summaries (one per ingested source)\n", "## Summaries (one per ingested source)\n- [[s-test-source]]\n- [[s-test-unlanded]]\n")
s=s.replace("ingest a source to fill them:\n", "ingest a source to fill them: [[missing-page]]\n"); open(p,'w').write(s)
PY
echo "== lint (empty wiki + test pages)"
lint_out="$(cd "$tmp" && python3 tools/lint.py --strict)" || { echo "$lint_out"; echo "FAIL: lint --strict"; exit 1; }
echo "$lint_out"
grep -q 'citation drift: 0 pages' <<<"$lint_out" || { echo "FAIL: citation drift should be 0 on the fixture"; exit 1; }
grep -q 'unlanded ripples: 1 across 1' <<<"$lint_out" || { echo "FAIL: the unlanded-ripple fixture was not detected"; exit 1; }
# the optional staleness hook: a wiki-specific tool that rejects --quiet and exits non-zero must
# still be a warning — lint --strict may not inherit its exit code
cat > "$tmp/tools/check-staleness.py" <<'STALE'
import sys
print('staleness: 2 behind'); sys.exit(3)
STALE
stale_out="$(cd "$tmp" && python3 tools/lint.py --strict)" || { echo "$stale_out"; echo "FAIL: check-staleness.py exit code leaked into lint --strict"; exit 1; }
grep -q 'staleness: 2 behind' <<<"$stale_out" || { echo "FAIL: staleness summary not printed"; exit 1; }
rm "$tmp/tools/check-staleness.py"
echo "== build"; (cd "$tmp" && python3 tools/build-site.py --out "$tmp/site" | tail -1)
for f in index.html wiki/test-technique.html wiki/s-test-source.html wanted/missing-page.html graph.html browse.html health.html sources.html search-index.js assets/types.css; do
  [ -f "$tmp/site/$f" ] || { echo "FAIL: missing site/$f"; exit 1; }
done
grep -q 'class="wl wanted"' "$tmp/site/wiki/test-technique.html" || { echo "FAIL: wanted link not rendered"; exit 1; }
grep -q '<a class="ext" href="https://example.org/x"><code>code-label</code></a>' "$tmp/site/wiki/test-technique.html" \
  || { echo "FAIL: markdown link with inline-code label not rendered (nested inline placeholder bug)"; exit 1; }
grep -q 'Selftest Wiki' "$tmp/site/index.html" || { echo "FAIL: site name"; exit 1; }
echo "ok: template wiki lints and builds"
ref="$here/../chiptune-wiki"
if [ -d "$ref/wiki" ]; then
  echo "== reference build: chiptune-wiki through the template generator"
  out="$(dirname "$tmp")/chiptune-site"
  python3 "$here/template/tools/build-site.py" --root "$ref" --config "$here/reference/chiptune-wiki/wiki.json" --out "$out" | tail -1
  [ -f "$out/cheatsheets.html" ] && [ -f "$out/inbox/traxweekly-toc.html" ] || { echo "FAIL: reference features missing"; exit 1; }
  echo "ok: reference wiki builds with cheat sheets and TOC table"
fi
echo "selftest passed"
