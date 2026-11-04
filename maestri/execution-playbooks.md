# Execution playbooks and quota guard
Adapted from github.com/Kc1t/alethe-orchestrate-skill. Maestri stays the execution surface: these are decision rules for the Maestro, not a second orchestrator. Teams (who) are in teams.md; playbooks say how the work is sequenced. Motion and premium UI keep their own procedures (motion-playbook.md, design-playbook.md); only the quota guard applies to them.

## Pick a playbook (after the team, first match wins)
| Playbook | Use when | Shape | Never when |
| --- | --- | --- | --- |
| direct | Narrow and clear, <=3 files | Maestro or one worker, one gate | Work needs reading >~8k tokens |
| cascade | Mechanical change with an automatic check (rename, codemod, lint fix, migration step) | Cheapest fitting runner first; on check failure retry once with a new brief and the failure note, then one tier up | Check does not exist or is weak |
| scout-then-build | Unfamiliar code, much to read, little to write | Read-only scouts return path:line summaries; Maestro writes the build brief from them; one writer | Scope already known |
| plan-execute | One feature in sequential steps | Strong tier writes the plan file; cheaper builder executes step by step; replan only on a failed gate | Steps are independent (use parallel) |
| parallel-worktrees | Independent modules, disjoint files | One writer per floor, integrate after each validates | Two writers need the same file |
| audit-at-scale | Dozens of similar items (files, endpoints, rules) | Cheap read-only scouts, one slice each, findings need path:line; one synthesizer | Items depend on each other |
| advisor-escalation | Long mechanical task with a few hard calls | Cheap builder runs; it writes NEEDS_CONTEXT at a decision point; Maestro or a stronger advisor answers in the brief; builder resumes | Hard calls are most of the task |
| best-of-n | Hard, high-stakes fix, no clear root cause | 2-3 writers, each on own floor with a different approach; reviewer picks by the proof command; losers discarded with approval | Cheap or reversible fix; quota below 50% |
| review-gate | Finished diff before merge | Fresh reviewer session (never the author), findings with path:line; apply only confirmed ones | Diff is <=20 lines |

Rules:
- Name the playbook in the MISSION.md row (`ID | team | playbook | agent...`). A playbook may change between waves; log "Ruling: <change> - <why>".
- A playbook never lowers a hard lock: motion stays Opus, creative work never goes to a lower tier to save quota, auth/payment/data keep the other-vendor reviewer.
- Waves: finish and accept one wave before starting the next. No unit starts on unaccepted output of another.
- Spend only what the gate needs: skip review-gate on trivial diffs, skip scouts when the files are known.

## Quota guard (before every wave and every `maestri recruit`)
Readings are hypotheses, not proof: Codex usage is in the local Codex session files and `/status`; Claude usage is in `/usage` or `/status`; if a reading is missing or older than ~30 min, mark it `unknown`, never `ok`.
- Low: >=80% of a window used. Stop line: >=95%, or the CLI itself reports the limit.
- Low: prefer the less-used account (accounts.md) or the other vendor for non-locked work; tell the user in 1 line.
- Stop line: do not start workers on that provider. Switch with `maestri recruit --replace "<agent>" --account "<other>"` (worker resumes from its handoff), or ask the user with options: wait for reset (give the time if known), switch account, or run on the other vendor. Never pass the stop line silently.
- Both vendors low and the unit is not locked: run the cheapest fitting tier, or ask. Locked units (Motion, Design Opus) wait or report BLOCKED_MOTION_MODEL / BLOCKED_QUOTA; no silent downgrade.
- best-of-n and parallel-worktrees need spare quota: with any provider low, run one writer.
- Spare quota never justifies a stronger model for a cheap job, and never a weaker one for a creative job.
- Record in MISSION.md: `Quota: claude <pct|unknown>, codex-1 <pct|unknown>, codex-2 <pct|unknown>` before each wave.
