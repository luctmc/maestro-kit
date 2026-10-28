# Teams — Maestro runtime catalog
Pick the row by TASK TYPE. Recruit only if the trigger test in roles/maestro.md passes. Presets/accounts: presets.md. Gates and brief template: quality-gates.md.
Tier: S <=15k tok, M ~15-80k, L >80k (estimates, not measured). Max live agents = recruits + native subagents.
"Opus" = preset Motion Director or Design Director (claude-opus-5-5 high).

## Rules for every team
- Depth 2: Maestro -> lead -> helper. Only a lead whose preset has the Maestro flag on (Design Director, Motion Director) spawns helpers; helpers never spawn. One writer per file, own floor per writer.
- Brief by pointer (quality-gates.md template, score >=7). Handoff file + max 10-line reply.
- Helper classes: scout (read-only: native Explore, or a Haiku preset after verifying its model id in the CLI), writer (floor + owned paths), reviewer (fresh session, never the author; same vendor by default, other vendor only for auth, payment, personal data and L3), runner (Codex Luna, verbatim commands; never in motion).
- Helper break-even: spawn only if the task needs >~8k tokens of reads/output or runs in parallel on disjoint files.
- No helper runs git writes.

## 1 Trivial fix
Signals: one file, <=20 lines, typo/rename/config, questions. Lead: Maestro itself. Gate: Code (run one check). Tier S. Recruits: 0.

## 2 Backend / data / API
Signals: endpoint, schema, query, auth, service, integration.
Lead: Builder, Codex Sol (less-used account). Helpers: scout; fresh Sonnet reviewer if 2+ modules; auth/payment/data: reviewer from the other vendor.
Skills: superpowers:test-driven-development, mattpocock-skills:code-review. Gate: Code (+ security for auth). Tier M. Max 2.
Plugin: dotnet profile only for CIINTEC .NET.

## 3 Functional UI
Signals: form, table, state, routing, screen bug, no redesign.
Lead: Builder, Claude Sonnet. Helpers: scout; visual checker (Sonnet) at 375 and 1440.
Skills: frontend-design, break-ui, oc-showcase. Gate: Code + one real render. Tier M. Max 2.

## 4 Premium UI / design
Signals: redesign, rebrand, landing, premium, award, wow, new product UI.
Lead: Design Director (Opus). It analyses the request and composes the team per sub-task (Claude Opus/Sonnet, Codex Sol/Luna, image or Figma/Canva tools) and may change it mid-mission. No fixed team, no cap on Opus seats; quality over cost, no waste on trivial jobs. Procedure: design-playbook.md.
Typical seats: Reference Scout (read-only), Prototype Builder (approved artboards only, no motion), Visual Critic (fresh session, screenshots only).
Skills: frontend-design, emil-design-eng, apple-design, prototype, break-ui, colorize, oc-copywriting. Gate: Premium UI. Tier L. Max 3 recruits unless the user is told.
Animation inside it goes to team 5.

## 5 Motion
Signals: animation, scroll choreography, transitions, GSAP, Lottie, kinetic type, hero sequence, any animation beyond CSS hover.
Lead: Motion Director (Opus), NO substitute. Procedure: motion-playbook.md.
Helpers, Opus 5.5 only: Motion Helper preset (high: Engineer, Critic, Scout), Motion Render preset (medium: Render Operator, only for mechanical renders/captures/exports from commands an Opus-high author wrote; spawn only if the batch blocks >~15 min).
Nothing but Opus writes animation source, timing, easing or keyframes. Never Codex, Sonnet, Haiku or Luna, not even for a render command.
Skills: motion-art-direction, shot-composition, animation-principles, animation-performance, accessible-animation, review-animations, gsap-web. Gate: Motion. Tier L. Max 3.

## 6 Video / brand film
Signals: video, reel, launch film, ad, promo, explainer, clip edit.
Lead: Motion Director (Opus). Helpers: as team 5 + Image Builder (Codex $imagegen) for stills only.
Skills: business-motion-film OR brand-launch-video-star, motion-art-direction, shot-composition, beat-sync-editing, sound-effects. Remotion only in personal projects.
Gate: Motion. Tier L. Max 3.

## 7 Images
Signals: logo, poster, illustration, asset image.
Lead: Image Builder, Codex Sol with $imagegen (gpt-image-2). Logos/marks: hand-written SVG by Claude Sonnet, never raster.
Skills: canvas-design (static art only). Gate: viewed render. Tier S-M. Max 1; 3 generation rounds, then show the user.

## 8 QA / testing
Signals: test, QA, find bugs, coverage, regression, E2E.
Lead: QA Lead, Claude Sonnet. Helpers: visual explorer, runner (Codex Luna).
Skills: qa-fix-protocol (fixers), break-ui. Gate: Code + findings with path:line. Tier M. Max 2.

## 9 DevOps / cloud
Signals: deploy, CI, pipeline, Docker, Azure, GCP, infra, env vars.
Lead: Ops Builder, Codex Sol; runner Codex Luna. Enable the azure or gcp profile first and tell the user in 1 line.
Skills: azure-prepare -> azure-validate -> azure-deploy; azure-diagnostics for prod. Gate: Ops (dry run + rollback noted). Tier M. Max 1.

## 10 Research / investigation
Signals: how does, compare, which library, map the code, audit (read-only).
Lead: Maestro with native Explore subagents; Claude Sonnet high only if ambiguous. Up to 3 scouts on disjoint questions.
Skills: mattpocock-skills:research, caveman:caveman-explore. Gate: Read-only (path:line). Tier S-M.

## 11 Docs
Signals: README, guide, changelog, document this.
Lead: Writer, Claude Sonnet. Skills: ponytail:ponytail. Gate: Code (commands/links run). Tier S. Max 1.

## 12 Debugging
Signals: error text, stack trace, broken, flaky, failing test.
Lead: Debugger, Claude Sonnet high (Codex Sol if stack is Codex-native or quota low). Helper: read-only tracer.
Skills: superpowers:systematic-debugging, mattpocock-skills:diagnosing-bugs, oc-stamp. 3 failed fixes = stop, report the coupling.
Gate: Code (red -> green). Tier M. Max 1 writer + 1 tracer.

## 13 Refactor
Signals: refactor, clean up, split, rename across, dedupe, no behavior change.
Lead: Refactorer, Codex Sol. Helpers: scout; reviewer for behavior preservation.
Skills: caveman:safe-refactor, superpowers:test-driven-development. Gate: Code (tests green before AND after). Tier M. Max 2.

## 14 Security review
Signals: security, vulnerability, auth review, secrets, OWASP, pre-release audit.
Lead: Security Reviewer, Claude Sonnet high. Auth/payment/data: second reviewer from Codex Sol; add skeptic (default REJECTED).
Skills: security-review, ponytail:ponytail-audit, mattpocock-skills:code-review. Gate: Read-only + skeptic. Tier M-L. Max 2.

## 15 Migration
Signals: schema change, framework/major dependency upgrade, data move, API versioning.
Lead: Migration Lead, Codex Sol builds; Claude Sonnet high reviews rollback. Serial steps, 1 writer.
Skills: caveman:migration, superpowers:writing-plans, oc-stamp. Gate: Code + Ops (rollback proven). Tier L.

## Mixed requests
Split by type, then order: design (4) -> build (2/3) -> motion (5) -> QA (8). Motion work never moves to another team even if the rest does.
