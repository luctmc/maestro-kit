# Quality gates — evidence before completion

These gates apply to orchestrated work. The model's self-assessment is not evidence. Report PASS, FAIL or NOT_PROVEN for each relevant gate.

## Routing gate
- Before spawning workers: trigger test passed (teams.md), `maestri list` checked, agents count and reason written, exact model/effort, skills verified installed, allowed files, reviewer, acceptance checks.
- Never assign creative quality ownership purely by cheapest provider, vendor rotation, or spare capacity.
- Brief score (Alethe briefs.md): goal 0-3, expected result 0-3, scope 0-2, constraints 0-2 (0 missing, 1 vague, 2 clear, 3 testable/checkable; scope 2 = owned AND forbidden paths; constraints 2 = repo rules and limits). Minimum 7/10, goal and result >=2. Below 7: read more or ask the user.
- Brief is a file at <ground>/.maestri/briefs/<ID>.md; the prompt is only its absolute path. Handoff at <ground>/.maestri/handoffs/<ID>.md.
- For independent concurrent builders: separate floors/files and integrate only after validation. The Maestro owns git.

## Code gate
- Tests for changed behavior; typecheck/lint/build where available; relevant error and empty states; no secrets; no regressions; accessibility/security/performance checks as warranted.
- Reviewer independent of the author (fresh session; other vendor only for auth, payment, personal data and L3). Every finding has path/line, scenario, severity and fix. A failed check requires a changed approach or evidence, not the same prompt again.
- A change to tests that weakens coverage is a finding, not a passing gate. Read test changes first.

## Premium UI gate
Procedure: maestri/design-playbook.md (staffing, gates, rubric). Scores come from screenshots, never from code.
- STAFFING: TEAM.md exists before recruiting; every seat names sub-task class, rule and evidence; creative class A seats run on Opus 5.5 only.
- ARTIFACTS: VISUAL-BRIEF.md is token-level (type ratio, grid, spacing scale, OKLCH palette with contrast table, one depth strategy, effects with parameters, at least 5 rejected defaults). Missing values = FAIL.
- SLICE FIRST: hero + 1 section + footer at 375/768/1440 scored >= 40/50 before build-out.
- RUBRIC: 0-5 x 10 (hierarchy, typography, layout, color/contrast, richness, originality, cohesion, responsiveness, accessibility, polish). PASS >= 40, none < 3, hierarchy/typography/accessibility >= 4. Award / "better than Apple": >= 44, originality/richness/polish >= 4, benchmark test won on >= 8/10 criteria.
- HARD FAIL: body contrast < 4.5:1; horizontal scroll at 375; no visible focus; critical/serious automated a11y violation; visible layout shift; motion without a reduced-motion path.
- ANTI-SLOP: the playbook checklist at G3, G6, G8; each unchecked item justified by the brief.
- INDEPENDENCE: draft scores by a fresh same-vendor critic with no authoring context; final by the Design Director; > 5-point gap -> second fresh critic, median. Other vendor only for auth/payment/personal data or L3.
- STATES: default/hover/active/focus-visible/disabled; loading/empty/error/long-content; dark mode if in brief; reduced motion.
- EVIDENCE: screenshot path per viewport, state and rubric criterion; fix list with concrete remedies. No rendered evidence = NOT_PROVEN.
- MOTION: implemented and verified only by Motion Director (Opus 5.5); this gate checks that each motion beat has a reduced-motion equivalent.

## Motion gate — Opus only
Procedure: maestri/motion-playbook.md.
- MODEL: every motion author and critic confirmed claude-opus-5-5 high; Render Operators confirmed claude-opus-5-5 medium and ran only commands written by an Opus-high author (first reply line + render brief on file). Any other model or effort touching motion = FAIL. Unavailable = BLOCKED_MOTION_MODEL.
- POLISH + CALIBRATION: polish checklist all yes; the calibration benchmark for the job type measured with the same pipeline and within its pass rule.
- LOCK CHECK: files owned by non-Opus builders contain no animation code (rg command in motion-playbook).
- CONTRACT: STORYBOARD.md approved; every row has a recipe ID and carried element; values from the playbook tokens.
- EVIDENCE: capture artifacts cited by path: stills per storyboard row, dense windows per transition, scroll sheets at 1440/768/390 for web, reduced-motion sheet, LoAF/trace for web, frozen-time + loudness + ffprobe for video. Real style-frame preview required.
- INDEPENDENT REVIEW: a fresh Motion Critic (not the builder) scored the playbook rubric. PASS = all criteria >= 3, mean >= 4.0, intent/timing/accessibility >= 4.
- NOT_PROVEN: any rubric criterion without viewed evidence; NOT_PROVEN on intent, timing or accessibility makes the gate NOT_PROVEN.
- LOOP: max 4 review rounds; open defects listed with timecode/frame lines at the end.

## Read-only gate
- Every finding has path:line plus a reproduction or trace. A finding without a location is rejected.

## Ops gate
- Dry run or validate step shown, rollback path written, no production change without explicit user approval.

## Acceptance and rescue
- Accept from evidence: re-run the proof command, open the screenshots, check `git diff --name-only` is inside owned paths. PASS | FAIL | NOT_PROVEN per criterion; one FAIL or NOT_PROVEN blocks acceptance.
- Rescue: Failure note in the brief (`retry-of <ID>`); rescue 1 only with a specific correctable cause: same worker, or fresh worker one tier up (never down; Opus teams change approach, not model); rescue 2 only with new evidence and smaller scope; then stop and tell the user. Never resend the same brief to the same model. Quota exhaustion is not a rescue: use `maestri recruit --replace --account`.
- Validator verdict ends `VERDICT: PASS | FAIL | NOT_PROVEN` and `NOT CHECKED: <list or none>`; validators run in a new session, never the author's.
- Skeptic/validator (default REJECTED) for security, migration and L3 completions.

## Acceptance contract
Each delegated unit must contain: owner/model/effort, objective, owned and forbidden paths, input references, skills to actually invoke, observable deliverable, commands/checks, visual review when relevant, dependencies, handoff and allowed fallback. A PASS requires evidence for every applicable criterion; otherwise FAIL or NOT_PROVEN.

## Brief template
```
# BRIEF <ID> — <title>
Team: <row name>   Lead/worker: <role>   Model/preset: <exact preset>   Effort: <low|medium|high>
Handoff path: <GROUND>/.maestri/handoffs/<ID>.md   Floor: <name or ground>   Agents allowed: <N>

## Goal (0-3)
<where this unit fits in the whole task; the outcome the owner sees; non-goals.>
## Expected result (0-3)
<observable artifact(s). Proof: exact commands with expected result, or viewports/states to screenshot.>
## Scope (0-2)
Owns: <paths>. Must not touch: <paths>.
## Constraints (0-2)
<repo rules and limits: no git writes; Motion lock; Remotion personal only; evidence format (375/768/1440 screenshots, red->green test, frame timestamps).>

## Context pointers
<absolute paths to specs, prior handoffs, design tokens. No pasted dossiers.>

## Skills to use (max 3, exact names, verified installed)
<name, name>

## Return
Write the handoff file: Outcome, Changed files (paths), Checks (command + exit code, or screenshot paths), Failures, Risks, Not checked. Do not delegate, spawn subagents or run git writes. Last two lines of your reply: `STATUS: DONE|DONE_WITH_CONCERNS|BLOCKED|NEEDS_CONTEXT` and `SUMMARY: <one line + handoff path>`. Max 10 lines.
```
Prompt to the worker: `Brief: <absolute path>. Read it, execute it, write the handoff to the path inside it. Reply max 10 lines.`
