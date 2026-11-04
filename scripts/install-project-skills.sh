#!/usr/bin/env bash
# Installs the 4 default skill sources into ONE project, pinned by commit.
# Usage: scripts/install-project-skills.sh /path/to/project
# Writes <project>/.agents/skills/<name> and relative links in <project>/.claude/skills/.
# Nothing global is touched. Re-run to update after bumping a SHA below (see maestro/vendor/TOOLKIT.lock).
set -euo pipefail

PROJECT="${1:?usage: $0 /path/to/project}"
[ -d "$PROJECT" ] || { echo "not a directory: $PROJECT" >&2; exit 1; }

# repo | pinned commit | skill paths inside the repo (space separated)
SOURCES=(
  "Kc1t/alethe-orchestrate-skill|5b8cd47675cc7353c0e1b21fc4a1795e7128c492|skills/alethe"
  "heydamir/unslop|a6f121eee5f29c2f74976b75456feae8b66afb3a|skills/unslop"
  "emilkowalski/skills|f1090bec277140d02ed202440185ad9d02ac1490|skills/emil-design-eng skills/animate skills/review-animations"
)
# soumatheusgomes/vibe-coding-toolkit (21b71b68679c11184f49c23168852014bf6dde8b) is docs/templates, not a skill:
# apply it to the project with its docs/prompts/12-existing-project-setup.md (or 11 for a new Next.js project).

TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
mkdir -p "$PROJECT/.agents/skills" "$PROJECT/.claude/skills"

for entry in "${SOURCES[@]}"; do
  IFS='|' read -r repo sha paths <<<"$entry"
  dir="$TMP/${repo//\//_}"
  git init -q "$dir"
  git -C "$dir" fetch -q --depth 1 "https://github.com/$repo.git" "$sha"
  git -C "$dir" checkout -q FETCH_HEAD
  for p in $paths; do
    name="$(basename "$p")"
    [ -f "$dir/$p/SKILL.md" ] || { echo "missing $repo/$p/SKILL.md" >&2; exit 1; }
    rm -rf "$PROJECT/.agents/skills/$name"
    cp -R "$dir/$p" "$PROJECT/.agents/skills/$name"
    ln -sfn "../../.agents/skills/$name" "$PROJECT/.claude/skills/$name"
    echo "ok $name <- $repo@${sha:0:7}"
  done
done
