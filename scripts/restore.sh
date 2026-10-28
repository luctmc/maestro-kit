#!/usr/bin/env bash
# Restore the Maestro kit into $HOME.
# Backs up every file or folder it is about to replace to ~/.maestro-kit-backups/<timestamp>/, then copies the kit files in.
# Does not install plugins or skills (see PLUGINS.md) and does not touch ~/.maestro/backups.
# Notes: codex/config.toml has no hook-trust hashes (approve hooks again in /hooks) and keeps absolute /Users/lucas paths; review it on another machine.
set -euo pipefail

KIT="$(cd "$(dirname "$0")/.." && pwd)"
BK="$HOME/.maestro-kit-backups/$(date +%Y%m%d-%H%M%S)"

# put <kit-relative source> <absolute destination>
put() {
  local src="$KIT/$1" dest="$2"
  if [ -e "$dest" ]; then
    mkdir -p "$BK$(dirname "$dest")"
    if [ -d "$dest" ]; then
      rsync -a --exclude 'backups/' "$dest/" "$BK$dest/"
    else
      cp -p "$dest" "$BK$dest"
    fi
  fi
  mkdir -p "$(dirname "$dest")"
  if [ -d "$src" ]; then
    mkdir -p "$dest"
    rsync -a "$src/" "$dest/"
  else
    cp "$src" "$dest"
  fi
  echo "restored $dest"
}

put maestro "$HOME/.maestro"
# Runtime docs the roles read (teams, gates, playbooks, role texts for pasting): ~/.maestro/maestri
put maestri "$HOME/.maestro/maestri"
put claude/settings.json "$HOME/.claude/settings.json"
put claude/CLAUDE.md "$HOME/.claude/CLAUDE.md"
put claude/RTK.md "$HOME/.claude/RTK.md"
put codex/AGENTS.md "$HOME/.codex/AGENTS.md"
put codex/RTK.md "$HOME/.codex/RTK.md"
put codex/rules "$HOME/.codex/rules"
put codex/hooks.json "$HOME/.codex/hooks.json"
put codex/config.toml "$HOME/.codex/config.toml"
put git/gitconfig "$HOME/.gitconfig"
put git/gitconfig-work "$HOME/.gitconfig-work"
put git/gitconfig-personal "$HOME/.gitconfig-personal"
put config/caveman/config.json "$HOME/.config/caveman/config.json"

# RTK config (carries the git diff/log/status/maestri exclusions). macOS path only.
# shortcut: Linux and Windows keep RTK config elsewhere; add those paths when the kit is restored there.
if [ "$(uname -s)" = "Darwin" ]; then
  put rtk/config.toml "$HOME/Library/Application Support/rtk/config.toml"
  put rtk/filters.toml "$HOME/Library/Application Support/rtk/filters.toml"
else
  echo "skipped rtk/*.toml: not macOS; copy them to this OS's RTK config folder by hand (see rtk/)"
fi

# ~/.zshrc is personal: only append the Graphify line when it is missing.
LINE="$(cat "$KIT/shell/graphify.zsh")"
if ! grep -qxF "$LINE" "$HOME/.zshrc" 2>/dev/null; then
  if [ -e "$HOME/.zshrc" ]; then
    mkdir -p "$BK$HOME"
    cp -p "$HOME/.zshrc" "$BK$HOME/.zshrc"
  fi
  printf '%s\n' "$LINE" >> "$HOME/.zshrc"
  echo "appended Graphify line to $HOME/.zshrc"
fi

echo "Backup of replaced files: $BK (absent if nothing existed)"
echo "Next: recreate presets/roles/accounts from maestri/ and install plugins from PLUGINS.md."
echo "skills/design-excellence is NOT installed by this script: copy it to ~/.claude/skills and ~/.agents/skills only after owner approval."
