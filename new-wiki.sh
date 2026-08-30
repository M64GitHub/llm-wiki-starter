#!/usr/bin/env bash
# Create a new LLM wiki from template/.
#   ./new-wiki.sh <target-dir> ["Wiki Name"]
# Copies the template, fills in {{WIKI_NAME}} / {{WIKI_SLUG}} / {{DATE}}, runs git init.
# The first Claude Code session in the new folder runs KICKOFF.md (the interview) automatically.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
target="${1:-}"
if [ -z "$target" ]; then echo "usage: $0 <target-dir> [\"Wiki Name\"]" >&2; exit 2; fi
if [ -e "$target" ] && [ -n "$(ls -A "$target" 2>/dev/null)" ]; then echo "error: $target exists and is not empty" >&2; exit 1; fi
slug="$(basename "$target")"
name="${2:-}"
if [ -z "$name" ]; then
  # folder name -> Title Case, hyphens to spaces, "-wiki" suffix kept as "Wiki"
  name="$(echo "$slug" | tr '-' ' ' | awk '{for(i=1;i<=NF;i++){$i=toupper(substr($i,1,1)) substr($i,2)}}1')"
fi
date="$(date +%Y-%m-%d)"
mkdir -p "$target"
cp -R "$here/template/." "$target/"
# fill placeholders in text files only
find "$target" -type f \( -name '*.md' -o -name '*.json' -o -name '*.py' -o -name '*.txt' \) -print0 |
  xargs -0 perl -pi -e "s/\\{\\{WIKI_NAME\\}\\}/$(printf '%s' "$name" | sed 's/[\/&]/\\&/g')/g; s/\\{\\{WIKI_SLUG\\}\\}/$(printf '%s' "$slug" | sed 's/[\/&]/\\&/g')/g; s/\\{\\{DATE\\}\\}/$date/g"
chmod +x "$target/tools/"*.py 2>/dev/null || true
# keep empty folders in git
for d in raw inbox wiki/summaries wiki/techniques wiki/concepts wiki/entities; do
  [ -d "$target/$d" ] && [ -z "$(ls -A "$target/$d")" ] && touch "$target/$d/.gitkeep"
done
if [ ! -d "$target/.git" ]; then (cd "$target" && git init -q); fi
cat <<MSG

created $target  ("$name")

next:
  cd $target
  claude            # the first session finds KICKOFF.md and runs the setup interview
or, from this repo, tell Claude Code:  new wiki $target
MSG
