# Quality gates — evidence before completion

These gates apply to orchestrated work. The model's self-assessment is not evidence. Report PASS, FAIL or NOT_PROVEN for each relevant gate.

## Routing gate
- Before spawning workers: scope, complexity, capability needs, dependencies, exact model, effort, skills verified installed, resource/quota constraints, allowed files, reviewer, and acceptance checks.
- Never assign creative quality ownership purely by cheapest provider, vendor rotation, or spare capacity.
- Brief score (Alethe-inspired): goal 0–3; checkable deliverable 0–3; owned paths 0–2; constraints 0–2. Minimum 7/10 before delegation.
- For independent concurrent builders: separate floors/files and integrate only after validation. The Maestro owns git.

## Code gate
- Tests for changed behavior; typecheck/lint/build where available; relevant error and empty states; no secrets; no regressions; accessibility/security/performance checks as warranted.
- Reviewer independent of the author. Every finding has path/line, scenario, severity and fix. A failed check requires a changed approach or evidence, not the same prompt again.
- A change to tests that weakens coverage is a finding, not a passing gate.

## Premium UI gate
- ART DIRECTION: purposeful concept, documented brand treatment, type scale, grid, spacing, color/contrast, visual priority, cohesive assets and editorial hierarchy.
- ORIGINALITY: distinguishable composition and signatures; do not treat a component library's default appearance as the finished design. Forbidden generic defaults are specified for the project, not as universal bans.
- RESPONSIVENESS: inspect real rendered views at representative mobile (375px), tablet (768px) and desktop (1440px) widths where browser access is available.
- STATES: inspect loading, empty, error, long-content, focus, hover, keyboard navigation and reduced-motion as relevant.
- MOTION: only Opus 5.5 authors meaningful animations; verify scroll interactions, sequences, easing, responsiveness, performance and prefers-reduced-motion.
- EVIDENCE: link screenshot/artifact for each key viewport and critical state. If tools cannot show a rendered UI, label visual QA NOT_PROVEN, not PASS.
- Visual reviewer critiques actual render, not just code. Fix large hierarchy or polish defects before declaring complete.

## Motion gate — Opus only
- Verified active model Opus 5.5 high for creative direction, storyboard, all animation implementation, frame review and correction.
- Real style-frame preview, timeline/storyboard fidelity, correct timing/typography/scene transitions, no flicker/jitter/broken masking, sound synchronization, export metadata and appropriate reduced-motion behavior.
- Opus reviews exported result and records concrete timestamps/screenshots; no delegated creative or motion coding to other models.
- No actual preview = NOT_PROVEN. Wrong model = FAIL/BLOCKED_MOTION_MODEL.

## Acceptance contract
Each delegated unit must contain: owner/model/effort, objective, owned and forbidden paths, input references, skills to actually invoke, observable deliverable, commands/checks, visual review when relevant, dependencies, handoff and allowed fallback. A PASS requires evidence for every applicable criterion; otherwise FAIL or NOT_PROVEN.
