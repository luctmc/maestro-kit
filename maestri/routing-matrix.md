# Capability-first routing matrix — Maestro
> Reference only. The Maestro runtime reads maestri/teams.md; this file explains the reasoning.

| Task | Creative owner | Implementation | Independent validator | Gate |
| --- | --- | --- | --- | --- |
| Trivial text/one-line fix | Maestro | Maestro | basic test | code |
| Backend/data/API/auth | Technical Architect (strong capable model) | Codex Sol or Claude Sonnet based on stack/available capability | fresh same-vendor reviewer + tests; other vendor only for auth, payment, data | code/security |
| Functional ordinary UI | Claude Sonnet or a capable UI developer | assigned builder | design check + functional reviewer | UI/code |
| Premium visual identity, landing page, product UI redesign | Design Director, Claude Opus 5.5 high (composes its own team) | Opus for key artboards and critical visuals; bounded Sonnet/Codex for noncreative implementation | fresh critic (screenshots) + Design Director sign-off + technical reviewer | premium UI |
| Rich interactive web motion/scroll experiences | Design Director + Motion Director, both Claude Opus 5.5 high | Motion Director Opus ONLY for all animation source; other builders may implement unrelated business logic | Motion Critic (Opus 5.5 high) + separate technical checks | premium UI/motion |
| Video/brand film/motion graphics/animated carousel | Motion Director Claude Opus 5.5 high | Motion Director Claude Opus 5.5 ONLY | Motion Critic (Opus 5.5 high) + technical render metadata | motion |
| Motion render/export/capture | Motion Director | Motion Director, or Motion Render Operator (Opus 5.5 medium) running commands written by an Opus-high author | Motion Critic (Opus 5.5 high) | motion |
| Mechanical build/test/render command (non-motion) | Existing owner | Codex Luna or CLI tools | task-specific checks | code/render |

Never route creative work to an inferior tier purely because an account has quota. If Opus 5.5 is unavailable, stop that part and disclose rather than silently downgrade. Verify installed model identifiers in the actual CLI before execution; documented presets are hypotheses until checked. The Maestro is a coordinator, not a substitute designer.

## Staffing
- Team by task type: see teams.md (15 rows). Smallest complete team; recruit only by the trigger test in roles/maestro.md.
- Premium UI: Design Director -> prototype/render -> critic -> implementation -> visual QA -> technical QA.
- Motion: Opus authors all animation source; mechanical runners may run Opus-authored commands verbatim, and only on Opus 5.5.
- User-approved branding, art direction and storyboard are immutable contracts until the user approves a change.

## Safeguards (from github.com/Kc1t/alethe-orchestrate-skill and github.com/stablyai/orca)
Bounded briefs scored 7/10, isolated writes, capability routing, quota checks, independent validation (new session), evidence-rich handoffs, rescue only with new context and one tier up, positive proof before retry. Maestri stays the execution surface; no second orchestrator.

## Decision record
One line per delegation in MISSION.md: ID | team | agent/model/effort | brief score | status | evidence path. Add "Ruling: <decision> - <why>" lines for non-obvious choices.
