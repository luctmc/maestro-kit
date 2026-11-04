#!/usr/bin/env bash
# Applies the kit's skill policy AFTER the skills are installed (README, "Caminho A", step 4).
# Codex/agents: allow_implicit_invocation: false for the situational skills (keeps an existing agents/openai.yaml).
# Disables oc-guide, oc-mcp, oc-pilot, oc-scout, oc-conveyor by moving them to skills-disabled-kit next to the skills folder.
# Claude name-only overrides come from claude/settings.json (restore.sh), not from this script.
# Safe to re-run; missing skills are skipped. Needs bash (Git Bash or WSL on Windows).
set -euo pipefail

SITUATIONAL=(oc-blackbox oc-builder oc-copywriting oc-route oc-showcase oc-stamp qa-fix-protocol unslop)
DISABLED=(oc-guide oc-mcp oc-pilot oc-scout oc-conveyor)

for root in "$HOME/.codex/skills" "$HOME/.agents/skills"; do
  [ -d "$root" ] || { echo "skip $root (absent)"; continue; }
  for s in "${DISABLED[@]}"; do
    if [ -d "$root/$s" ]; then
      mkdir -p "$(dirname "$root")/skills-disabled-kit"
      mv "$root/$s" "$(dirname "$root")/skills-disabled-kit/$s"
      echo "disabled $root/$s"
    fi
  done
  for s in "${SITUATIONAL[@]}"; do
    [ -d "$root/$s" ] || continue
    if [ ! -f "$root/$s/agents/openai.yaml" ]; then
      mkdir -p "$root/$s/agents"
      printf 'policy:\n  allow_implicit_invocation: false\n' > "$root/$s/agents/openai.yaml"
      echo "implicit off $root/$s"
    fi
  done
done
