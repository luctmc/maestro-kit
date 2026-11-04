---
name: maestro-setup
description: Maestro only. Set up a project's whole environment in Maestri: workspace, floors, notes, portal, routines, the 4 default skills, the vibe-coding-toolkit setup, plugin profile and verification. Use when the user types /maestro-setup (Claude) or $maestro-setup (Codex), or asks to configure the environment of a project in Maestri.
---
# maestro-setup

Runs only for the Maestro (Maestro mode on). Same procedure on Claude and Codex. Goal: leave one project ready to work, with evidence. Speak Brazilian Portuguese, short. Show the plan, then execute by phases; one question round at most.

## 0. Identify
- Ask only what you cannot discover: project path (default: the directory you were opened for), and base branch. Read `git config user.email`: `luctmc@outlook.com` = personal, `lucas.castro@montreal.com.br` or a CIINTEC* path = work.
- Run `maestri list`, `maestri workspace list`, `maestri floor list`, `maestri preset list` first. Reuse what exists; never duplicate a workspace, floor, note or routine.

## 1. Plan (show before changing anything)
Print a checklist with phases 2-8, marking each: exists | will create | not applicable. Work repos: ask one ok before phase 4 (it rewrites AGENTS.md, CLAUDE.md, docs). Personal: proceed after the plan, and stop at any item marked "needs approval" below.

## 2. Maestri workspace
- No workspace for the path: `maestri workspace create "<Project>" --dir <path> [--group G]` (path must exist). Use `--from "<Source>"` only to clone a layout the user names.
- Floors (skill maestri-workspace): the ground stays for read-only work; create a floor per writer only when a mission needs it (`maestri floor create "<name>" --branch <feature/...>`). Ask the base branch once. Never land or delete a floor without approval.
- Band for the recruited team only when 2+ agents are connected.

## 3. Notes, portal, routines (skills maestri, maestri-portal, maestri-routines)
- WHERE: `maestri note`, `portal` and `routine` attach to the terminal that runs them. If the project is NOT the workspace you run in, recruit or reuse a Maestro in that workspace (`maestri recruit "Maestro <Project>" --preset "Maestro Codex 2" --workspace "<Project>"`, or the Claude "Maestro" preset) and give it a brief file to create the note, portal and routines there. After the Codex terminal opens, send `maestri ask "<name>" --raw '\e'` once to dismiss its startup warning. A Claude Maestro may stop on "trust this folder": tell the user to confirm it, never answer it yourself. Afterwards run `maestri list` here and confirm nothing was left behind; delete strays only if the user asks.
- Note "MISSION" (connected): request, base branch, commands (install, dev, test, build, lint), env var NAMES only, `agents: N, reason`, `toolkit: done|declined`, quota line.
- Portal: if the project has a dev URL or a mobile target, create one (`maestri portal create <url> "<Name>" --size 1440x900`; `maestri-portal-devices` for simulators). No dev URL yet: mark NOT_PROVEN for visual checks.
- Routines: offer only what fits (CI check, quota check, long render). Create with `maestri routine create`, after the user agrees.

## 4. Project foundation (all pinned, project-local)
- Default skills: run `~/Documents/GitHub/maestro-kit/scripts/install-project-skills.sh <project>`; confirm `.agents/skills/{alethe,unslop,emil-design-eng,animate,review-animations}` and the links in `.claude/skills`. Never the alethe plugin or its hook.
- Toolkit: no `docs/setup.md` = run `docs/prompts/12-existing-project-setup.md` (new Next.js project: prompt 11) from `~/Documents/GitHub/vibe-coding-toolkit` with a fresh worker; accept only with docs/setup.md and its coverage matrix. Never `git pull` the toolkit without approval.
- Project hygiene: Context7 config and `.graphifyignore` per the toolkit templates; tokens and credentials never copied.

## 5. Plugin profile (needs approval to enable)
Pick from `~/.maestro/profiles.md` by stack (web-ts, dotnet, python, azure, gcp, n8n). Enable only what the project uses, in `<project>/.claude/settings.local.json` (personal) or `settings.json` (shared). Say it in one line, with the token cost. Remotion skills: personal projects only.

## 6. Toolchain
Detect the package manager and runtime; install dependencies and missing language servers (typescript-language-server, csharp-ls, pyright) only if the stack needs them. Run install, build, lint and tests once and record the exact commands and results in MISSION. Failing baseline = report it, do not fix it here.

## 7. Verify (evidence per item: PASS | FAIL | NOT_PROVEN)
Workspace exists; floors listed; MISSION note readable by `maestri note read`; skills present in `.agents/skills` and `.claude/skills`; docs/setup.md updated; baseline commands run; portal opens the dev URL (screenshot) when one exists.

## 8. Close
Reply in max 10 lines: what exists now, what was created, what is NOT_PROVEN, and what needs the user (approvals, credentials, logins). Git: never commit or push without explicit approval; show `git config user.email` before asking.

## Hard rules
- Never install or enable anything outside the default skills, the toolkit and the chosen plugin profile without approval; always pin versions or commits.
- Never delete files, branches, floors or unpreserved changes. Never print secrets; names only.
- Recruit a worker only per the trigger test in `~/.maestro/maestri/teams.md`.
