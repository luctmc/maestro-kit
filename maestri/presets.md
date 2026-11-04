# Maestri presets

Recreate with `maestri preset create "<name>" --command "<command>" [--account "<account>"]` and `maestri preset set "<name>" --maestro on|off`.
Account names only; see accounts.md.

| Preset | Command | Account | Maestro |
|---|---|---|---|
| Claude Code | `claude --dangerously-skip-permissions` | - | [ ] |
| Codex | `codex --dangerously-bypass-approvals-and-sandbox` | Padrão | [ ] |
| Shell | (none: plain shell) | - | [ ] |
| Maestro | `claude --dangerously-skip-permissions --model sonnet --effort medium` | - | [x] |
| Claude Sonnet | `claude --dangerously-skip-permissions --model sonnet --effort medium` | - | [ ] |
| Codex Sol 1 | `codex --yolo -m gpt-6.1-sol -c model_reasoning_effort=medium` | Padrão | [ ] |
| Codex Sol 2 | `codex --yolo -m gpt-6.1-sol -c model_reasoning_effort=medium` | Codex 2 | [ ] |
| Codex Luna 1 | `codex --yolo -m gpt-6-luna -c model_reasoning_effort=low` | Padrão | [ ] |
| Codex Luna 2 | `codex --yolo -m gpt-6-luna -c model_reasoning_effort=low` | Codex 2 | [ ] |
| Maestro Codex 1 | `codex --yolo -m gpt-6.1-sol -c model_reasoning_effort=medium` | Padrão | [x] |
| Maestro Codex 2 | `codex --yolo -m gpt-6.1-sol -c model_reasoning_effort=medium` | Codex 2 | [x] |
| Motion Director | `claude --dangerously-skip-permissions --model claude-opus-5-5 --effort high` | - | [x] |
| Motion Helper | `claude --dangerously-skip-permissions --model claude-opus-5-5 --effort high` | - | [ ] |
| Motion Render | `claude --dangerously-skip-permissions --model claude-opus-5-5 --effort medium` | - | [ ] |
| Design Director | `claude --dangerously-skip-permissions --model claude-opus-5-5 --effort high` | - | [x] |

Model IDs must be validated in the installed CLI before use. Motion is exclusively Claude Opus 5.5: Motion Director (Maestro ON) and Motion Helper (modes Engineer, Critic, Sound) at high; Motion Render at medium ONLY for mechanical renders/captures/exports from commands written by an Opus-high author. Helpers have Maestro OFF and cannot recruit. No Codex, Sonnet, Haiku or Luna in motion. Role texts: maestri/roles/motion-director.md, motion-helper.md, motion-render.md; usage rules in maestri/motion-playbook.md (B2, B3).

Maestro parity: Maestro (Claude), Maestro Codex 1 and Maestro Codex 2 use the same role text (Maestri writes it as CLAUDE.md and AGENTS.md), the same ~/.maestro/maestri/ files and the same skill policy. Codex accounts share ~/.codex (config.toml, AGENTS.md, skills, plugins); only the login differs. Hard model locks (motion and design on Claude Opus 5.5) apply to all three.
