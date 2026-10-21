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
| Motion Director | `claude --dangerously-skip-permissions --model claude-opus-5-5 --effort high` | - | [x] |
