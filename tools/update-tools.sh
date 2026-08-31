#!/usr/bin/env bash
# Push the template's tools (viewer generator, assets, lint, extractors) into an existing wiki.
#   tools/update-tools.sh <wiki-dir> [--dry-run]
# Never touches wiki.json, CLAUDE.md or pages. Shows a diff summary; with --dry-run only shows it.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
wiki="${1:-}"; dry="${2:-}"
if [ -z "$wiki" ] || [ ! -d "$wiki/wiki" ]; then echo "usage: $0 <wiki-dir> [--dry-run]  (a folder with wiki/ inside)" >&2; exit 2; fi
src="$here/template/tools"; dst="$wiki/tools"
mkdir -p "$dst/site-assets"
changed=0
while IFS= read -r -d '' f; do
  rel="${f#$src/}"
  if [ ! -e "$dst/$rel" ]; then echo "new:      tools/$rel"; changed=1
  elif ! cmp -s "$f" "$dst/$rel"; then echo "changed:  tools/$rel ($(diff "$dst/$rel" "$f" | grep -c '^[<>]') lines)"; changed=1
  fi
  if [ "$dry" != "--dry-run" ]; then mkdir -p "$(dirname "$dst/$rel")"; cp "$f" "$dst/$rel"; fi
done < <(find "$src" -type f -not -path '*/__pycache__/*' -not -name '*.pyc' -print0)
[ "$changed" = 0 ] && echo "tools already up to date"
[ "$dry" = "--dry-run" ] && echo "(dry run — nothing copied)"
if [ "$dry" != "--dry-run" ] && [ ! -f "$wiki/wiki.json" ]; then
  echo "note: $wiki has no wiki.json — the tools use defaults (technique/concept/entity/summary). Copy template/wiki.json and adapt it."
fi
