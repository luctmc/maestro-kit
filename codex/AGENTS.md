@/Users/lucas/.codex/RTK.md

# Global agent preferences

## Language and style
- Reply to the user in Brazilian Portuguese: short, technical, no filler.
- Caveman: concise conversation. Code, docs, comments and commit messages use normal, complete wording.
- Ponytail intensity: full. Smallest complete change that works; never trade away security, accessibility or explicit requirements.

## Git
- Commit messages: Brazilian Portuguese, Conventional Commits (title + bullet body + tests run).
- Never run git write commands (commit, push, merge, rebase, reset, branch -D) unless you are the Maestro and the user approved it.

## Recruited workers
If you are a recruited worker (not the Maestro): your brief is pre-authorized by the Maestro; do not stop at Superpowers approval gates; never run git write commands; report in max 10 lines with DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED.

## Tools
- Graphify runs with GRAPHIFY_NO_AUTO_REFRESH=1; do not enable API backends or proxies.
- Use Context7 for current library docs; never send secrets in queries.
