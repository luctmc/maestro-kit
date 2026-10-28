# Design playbook (Design Director reference; read only the section for your current step)

Runtime role: `maestri/roles/design-director.md`. Gate checklist: `maestri/quality-gates.md` (Premium UI gate).
Craft doctrine lives in the kit skill `design-excellence` (kit path `skills/design-excellence/`; once installed, `~/.agents/skills/design-excellence/`). This playbook covers team, process and routing; the skill covers hierarchy, type, color, effects, polish, anti-slop and the rubric. [S#] tags point to `skills/design-excellence/references/sources.md`.

| Step | Read |
|---|---|
| Intake and staffing | §B |
| Gates and templates | §C |
| Scoring and QA | §D, then skill `references/rubric.md` and `references/anti-slop.md` |
| Effects | §E (pointer) |
| Model choice and A/B | §F |

## §B Staffing (dynamic, per request)

Owner rules: no fixed team and no cap on Opus seats for design; the Design Director (DD) composes the team per request and may change it mid-mission; quality over cost for design, but no waste on trivial jobs; read-only scouts run on Haiku (model id verified in the CLI first); the default reviewer is a fresh same-vendor session, the other vendor only for auth, payment, data and L3 work. Motion stays with the Motion team (Opus 5.5 only).

### B1. Seat catalogue (what the DD can staff; none is mandatory)

| Seat | Preset / model / effort | Typical sub-tasks | Notes |
|---|---|---|---|
| DD (lead) | Design Director / Opus 5.5 / high | All class-A sub-tasks, final judgment | Maestro flag on, so it recruits the seats below |
| Opus design seat | Design Director preset + role "Design Director" briefed as "Visual Designer", "Design Engineer" or "Critic" / Opus 5.5 / high | Class A/B work in parallel: second page template, signature section, build-out of visible sections, fresh critic | As many as the plan justifies (B3 rule 4); no cap |
| Fresh critic | Same preset as the author's vendor (Claude → Opus seat), new session with no authoring context | G6/G8 scoring from screenshots + rubric + calibration set | Same-vendor fresh reviewer by default (owner rule) |
| Sonnet seat | Claude Sonnet / Sonnet 5.5 / medium | Class B/C work not visible in key viewports: logic-heavy components, data wiring, copy drafts, IA tables | Takes class-B visible work only with A/B evidence (B5) |
| Codex Sol seat | Codex Sol 1/2 / gpt-6.1-sol / medium | `$imagegen` runs, data-heavy app logic, other-vendor review when the mission touches auth/payment/data or is L3 | Model id "gpt-6.1-sol" not found in a release note (UNVERIFIED) [S26] |
| Haiku scout | Haiku preset (to create; verify id with `claude --model haiku` in the CLI) / low | Read-only: reference measurement extraction, inventory of existing tokens/components, screenshot contact sheets, catalog lookups | Never edits project files |
| Luna runner | Codex Luna 1/2 / gpt-6-luna / low | Dev server, captures at 375/768/1440, `diff` runs, a11y tool runs, exports | Mechanical commands only |
| Tools (no seat) | `$imagegen` (gpt-image-2), Figma MCP, Canva MCP, `canvas-design`, `agent-browser`, `maestri portal` | Assets, editable design files, captures | Choice rules in B3 step 3 |
| Motion Director | Motion Director / Opus 5.5 / high | Every motion beat in VISUAL-BRIEF | Recruited by the Maestro on DD request; separate team |

### B2. Never delegated below Opus (class A, fixed)
Concept and directions; type pairing and scale; palette; hero and signature moment; art-direction prompts for images; logos/brand marks (hand-written SVG); final rubric score and sign-off. These can go to an additional Opus seat, never to Sonnet, Codex, Haiku or Luna.

### B3. Staffing procedure (the DD runs it at intake, writes TEAM.md, re-runs it on every trigger in B4)

Step 1 — Request profile (write 10 lines in TEAM.md)
```
SURFACE MODE: persuade (landing/marketing) | operate (app/dashboard) | read (docs/editorial) | experience (portfolio/showcase)
NOVELTY: refine (keep identity) | extend (new surfaces, same system) | redesign (replace look) | new world (no incumbent)
SCOPE: <n> page templates, <n> sections, <n> components, <n> states
CONTENT: exists | partial | must be written
ASSETS: none | photo | illustration | 3D | icons | logo | key art  (count)
MOTION BEATS: none | <list>  → Motion Director needed yes/no
PLATFORM: web | iOS | Android | multi; DESIGN SYSTEM: none | exists (extend) | locked
VISIBILITY: internal | client-facing | public launch | award ambition
DEADLINE / BUDGET NOTE: <owner constraint or "quality first">
SIZE: XS | S | M | L | XL  (XS = polish inside an existing system → Maestro/Sonnet, DD not recruited)
```
(The four surface modes are adapted from Impeccable's mode split, Apache-2.0 [S29]; they set how much expression vs restraint the rubric rewards.)

Step 2 — Decompose into sub-tasks and classify each
- Class A (taste-defining): direction, type, palette, hero, signature, image art direction, final judgment → Opus only.
- Class B (taste-sensitive execution): build-out of sections visible at first viewport or on key templates, copy, IA, component variants, polish → Opus by default; a cheaper seat only with B5 evidence.
- Class C (mechanical/read-only): captures, measurement extraction, inventories, wiring, data, tests, a11y runs, exports, image generation runs → Haiku scout (read-only), Luna runner (commands), Sonnet/Codex Sol (non-visual code).

Step 3 — Pick seat, model and tool per sub-task (first matching rule wins)
1. Class A → DD; if the DD is the bottleneck (two class-A streams can run in parallel, e.g. two page templates), add an Opus design seat.
2. Class B visible → Opus design seat, unless §F evidence for that task class is VERIFIED-LOCAL and the challenger met the B5 rule → that seat.
3. Class B non-visible (logic, data, state machines) → Sonnet (Claude-only skills needed) or Codex Sol (stack fit, quota).
4. Add a parallel seat only when its work is disjoint in files and ≥ 30 min, or needs a specialty the current seats lack. Parallel builders get separate floors; one writer per file.
5. Read-only fact gathering → Haiku scout. Commands without judgment → Luna runner.
6. Images: raster photo/illustration → `$imagegen` (Codex Sol seat) with DD-written prompt; logos/marks → DD SVG; posters/key art/OG → `canvas-design` (DD) or `$imagegen`; editable layered asset or social set → Canva MCP; owner wants an editable design file or the source of truth is Figma → Figma MCP (load `figma-use` / `figma-generate-design` first).
7. Review: fresh same-vendor critic (Opus seat with no authoring context) for G6/G8; add an other-vendor reviewer only if the mission touches auth, payment or personal data, or is L3.
8. Motion beats → ask the Maestro to recruit Motion Director; the DD never writes animation.
9. More than 3 concurrent recruits → allowed (no cap for design), but notify the owner in one line with the TEAM.md summary (owner rule).

Step 4 — Write TEAM.md (one row per seat)
```
| Seat name | Preset/model/effort | Sub-tasks (ids) | Class | Why this seat (rule #) | Evidence level | Rejected alternative | Exit condition |
```
Example (L job, public launch, 3 templates, 6 images, 2 motion beats): DD (A: direction, tokens, home hero, final score) · Opus "Visual Designer" (A/B: product + pricing templates) · Opus "Design Engineer" (B: visible build-out, polish) · Sonnet (B-non-visible: CMS wiring, forms logic) · Codex Sol (C: 6 `$imagegen` runs) · Haiku scout (C: reference measurements, token inventory) · Luna runner (C: captures, a11y) · fresh Opus critic (G6/G8) · Motion Director (2 beats). Eight concurrent seats → one-line owner notice.

Step 5 — Launch in waves. Wave 1: scouts + DD (G1–G4). Wave 2: builders after slice approval (G6). Wave 3: critic + runner (G8). Dismiss seats at their exit condition.

### B4. Mid-mission change triggers (log every change in TEAM.md: trigger, evidence, old → new)
| Trigger (observable) | Change |
|---|---|
| A rubric criterion stays < 3 on a seat's output after 2 revise loops | Upgrade the seat (Sonnet/Codex → Opus) or change the approach; never a third identical loop |
| Seat output fails ≥ 3 anti-slop items (skill anti-slop.md) at G6/G8 | Reassign that sub-task to an Opus seat; keep the cheaper seat only for class C |
| Scope grows (new template, page or asset set) | Re-run Steps 1–3 for the delta; add a seat if rule 4 holds |
| Critic and DD totals differ by > 5 | Add a second fresh critic (Opus); use the median |
| Account limit reached | `maestri recruit --replace` to the same model on the other account; never downgrade class A/B-visible |
| Owner approves a direction change | Re-run Steps 1–4 for affected sub-tasks; previous VISUAL-BRIEF archived |
| A/B result (F1) published for a task class | Apply its decision on the next sub-task of that class |
| Seat idle > 20 min with no queued sub-task | Dismiss |

### B5. Minimum evidence per choice
| Choice | Minimum evidence before acting |
|---|---|
| Any class-A sub-task on Opus | None (fixed rule) |
| Class-B visible sub-task on a non-Opus seat | VERIFIED-LOCAL A/B (F1) for that task class within 90 days, challenger mean ≥ primary − 1, no criterion ≥ 2 lower, no hard fail |
| Extra parallel seat | TEAM.md row naming disjoint files and ≥ 30 min of work, or a missing specialty |
| Figma / Canva MCP | Owner request, existing Figma source, or a deliverable that must be an editable design file |
| `$imagegen` asset | VISUAL-BRIEF imagery section lists the asset with treatment and rights note |
| Other-vendor reviewer | Mission touches auth/payment/personal data, or classified L3 |
| Downsizing the team | Exit condition met, or seat idle trigger |
| XS classification (no DD) | Change confined to existing tokens/components, no new visual decision |

### B6. Job sizes (guidance for Step 1, not a fixed team)
XS polish inside an existing system → Maestro or Sonnet with `oc-showcase` + `emil-design-eng`, no DD. S one premium component/section → DD alone with `/prototype`. M one premium page → DD + the seats Step 3 yields (typically 2–4). L multi-template site/product redesign → DD + parallel Opus seats per template + class-C helpers. XL brand/new world → L + 2–3 directions approved by the owner before VISUAL-BRIEF.

### B7. Helper brief (DD → helper), brief score ≥ 7/10 per maestri/quality-gates.md

```
ROLE: <QA runner | Design engineer | Critic | Asset generator>  SEAT: <preset> / <effort>
GOAL: <one sentence, observable>
INPUTS: VISUAL-BRIEF.md, <slice URL/path>, <screenshots dir>
OWNED PATHS: <files/dirs>   FORBIDDEN: everything else; no git writes; no motion code
SKILLS TO USE: <exact names or "none">
DELIVERABLE: <file paths> + reply ≤ 10 lines (DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED)
CHECKS: <commands to run, viewports, states>
RETURN: paths only, never inline image dumps or full logs
```

### B8. Token economy rules
- Helpers return file paths and counts; the DD opens only the screenshots it scores (3 viewports per template, plus failing states).
- Use `agent-browser screenshot --if-changed` and `diff screenshot --baseline` on re-runs so unchanged views cost nothing.
- Load `emil-design-eng` (27 KB) and `apple-design` (23 KB) only in polish/QA or when the brief needs gestures; `design-excellence` (kit skill; one reference per step), `frontend-design` (9 KB) and `oc-showcase` (15 KB) are the default set.
- The runtime role file stays ≤ 80 lines; the playbook is read per stage, by section heading.

## §C Workflow, artifacts and gates

All artifacts live in `<project>/.maestri/design/` (not committed unless the Maestro decides). Loop budget: max 3 critique→revise iterations per gate; on the third failure change the approach or escalate to the Maestro with evidence.

| Gate | Stage | Owner | Artifact | Exit criterion |
|---|---|---|---|---|
| G0 | Intake and sizing | Maestro | MISSION.md line: size XS–XL, team, motion yes/no | Size chosen with reason |
| G1 | Audit | DD (+ Luna captures) | AUDIT.md: current screenshots 375/768/1440, token inventory, content inventory, constraints, 3 KEEP + 3 KILL | Screenshots exist on disk; constraints listed |
| G2 | Reference board | DD (+ Luna captures) | REFERENCES.md (template below) | 5–8 references, ≥ 2 from outside the product category, each with one contribution axis |
| G3 | Concept directions | DD | DIRECTIONS.md: 2–3 directions on named axes | Each direction passes the swap test; owner approval for XL or brand departure |
| G4 | Visual brief | DD | VISUAL-BRIEF.md (token-level template below) | Every field filled with a value, not an adjective; anti-defaults section names ≥ 5 rejected defaults |
| G5 | Wireframe / hierarchy | DD or IA seat | WIREFRAME.md: section table + ASCII mobile and desktop + real copy; grey-box screenshot | Hierarchy checklist 10/10 (skill hierarchy.md); squint test on grey-box |
| G6 | Vertical slice | DD codes | Hero + 1 representative content section + footer at 375/768/1440 | Rubric ≥ 40/50 with no criterion < 3; slice becomes the reference implementation |
| G7 | Full build | Design engineers (floors, one writer per file) | Sections/components | Built only from tokens; no new raw hex/px outside tokens; typecheck/build pass |
| G8 | Render QA | Luna captures; Critic scores; a11y run | QA.md: rubric draft + fix list + a11y raw output | No P0; a11y hard gates pass |
| G9 | Polish and sign-off | DD with `emil-design-eng` | POLISH.md: Before/After/Why table; final rubric | Premium thresholds met (§D); PASS / FAIL / NOT_PROVEN per gate |

### C1. REFERENCES.md template (per reference)
```
### R<n> — <site/product name>   URL: <url>   Captured: <screenshot path(s)>
Category: same-domain | cross-domain
Contributes (ONE axis): type | grid/layout | color/light | imagery/art direction | interaction signature | pacing/rhythm | copy/layout pairing
Principle extracted (transferable, 1–2 lines): <e.g. "display type at 14vw cropped by the viewport edge carries the hero; no image">
Measured values: <e.g. h1 ≈ 168px/0.9 lh, body 18/1.6, 12-col 24px gutter, section padding 160px>
Do NOT copy: <assets, exact layout, logo, copy, distinctive illustration style>
Used in: <which section/direction of ours>
```
Rules: never copy assets, full layouts or copy; extract principles and measured values. Measure with `agent-browser eval "getComputedStyle(document.querySelector('h1')).fontSize"` or `maestri portal evaluate`. If browsing is unavailable, state so in REFERENCES.md and mark G2 NOT_PROVEN.

### C2. VISUAL-BRIEF.md template (token level; every field takes a value)
```
CONCEPT: <one sentence>. EMOTION: <2 words with meaning, e.g. "calm authority">. METAPHOR: <physical-world source>
SIGNATURE: <the one element only this product would have> — appears in: <≥ 3 places>
REJECTED DEFAULTS: <≥ 5, each "default → replacement">

TYPE
  Families: display <name, source, license>; text <name>; (mono only if content is code/data)
  Scale: base 16px (mobile) / 18px (≥ 1024); ratio 1.250 (product) | 1.333 (editorial) | 1.5–1.618 (expressive hero only)
  Fluid: clamp() per step between 375 and 1440 viewports (Utopia method); h1 <min>–<max>px
  Leading: display 0.9–1.05; headings 1.1–1.25; body 1.5–1.65 (serif +0.05)
  Tracking: display −0.02 to −0.04em; caps labels +0.06em (only if labels are used at all)
  Measure: body 60–75ch; text-wrap: balance on h1–h3, pretty on paragraphs
  Numerals: tabular-nums for data; oldstyle for editorial body if the face has them
GRID
  Columns: 4 @ 375 / 8 @ 768 / 12 @ 1440; gutter 16 / 24 / 32px; margins 20 / 40 / 80px; max content width <px>
  Breaks: <where the layout intentionally breaks the grid, and why>
SPACING
  Unit 4px; scale 4 8 12 16 24 32 48 64 96 128 160; section padding mobile 64–96, desktop 128–200
  Density map: section → D1 airy | D2 open | D3 standard | D4 dense
COLOR (OKLCH + hex)
  Neutrals: 5–7 steps with L values; brand: 1 accent (+1 secondary max); semantic: success/warn/danger
  Ratios: 60/30/10 neutral/secondary/accent; contrast table: each text/bg pair with WCAG ratio (body ≥ 4.5, large ≥ 3, UI ≥ 3)
  Dark mode: yes/no; elevation by +L steps (2–4%), borders rgba(255,255,255,.06–.12)
DEPTH / LIGHT / TEXTURE
  Depth strategy (ONE): border-only | subtle shadow | layered shadow | surface variation
  Shadow tokens: <layered values>; radius scale: sm/md/lg with concentric rule outer = inner + padding
  Light: <direction, specular edge yes/no>; texture: <grain opacity, pattern>
IMAGERY / ART DIRECTION
  Source: photo | $imagegen | illustration | 3D | type-only; treatment: <duotone/grade/crop rules>; aspect ratios; subject rules
EFFECTS (from design-excellence references/effects.md; name + parameters)
  <E-id, params, where, fallback>
MOTION HANDOFF (Motion team implements)
  Beats: <where, intent, trigger>; reduced-motion behavior: <static equivalent>
RESPONSIVE
  375: <what changes>; 768: <...>; 1440: <...>; touch targets ≥ 44px
ACCEPTANCE
  Rubric target: ≥ 40 (premium) | ≥ 44 (award ambition); viewports 375/768/1440; states list
```

### C3. Hierarchy checklist and C4. Page structure
Both live in the skill: `references/hierarchy.md` (10-item hierarchy checklist, WIREFRAME.md section table with rhythm rules, surface modes, identity tests). Fill the WIREFRAME.md table from there at G5.

### C5. Render QA capture protocol (QA runner, Codex Luna)
```
agent-browser open <url>
for W in 375x812 768x1024 1440x900:   agent-browser set viewport <w> <h>; agent-browser screenshot --full <dir>/<page>-<w>.png
agent-browser media dark            ; repeat 1440 + 375 → <page>-<w>-dark.png   (only if dark mode in brief)
agent-browser media reduced-motion  ; repeat 375 → <page>-375-rm.png
States: hover/focus via `agent-browser snapshot` refs + keyboard Tab walk; record focus order transcript
Re-runs: add --if-changed; compare with `agent-browser diff screenshot --baseline <old>`
Inside the Maestri canvas instead: maestri portal create <url> "QA" --size 375x812; maestri portal resize "QA" 768 1024; maestri portal screenshot "QA"; maestri portal snapshot "QA"
```
Note: `maestri portal check` toggles a checkbox; it is not a capture command. Capture = `snapshot` (a11y tree), `screenshot`, `resize`, `evaluate`.

## §D Rubric and scoring

- Rubric (10 criteria × 0–5), pass thresholds, hard fails, NOT_PROVEN rule and the fix-list format: skill `references/rubric.md`.
- Anti-slop checklist at G3, G6 and G8: skill `references/anti-slop.md`.
- Polish rules P1–P20 at G9: skill `references/polish.md`.
- Scorer independence: G8 draft by a fresh Opus critic seat with no authoring context (same vendor as the author); G9 final by the DD. Totals differ by > 5: add a second fresh critic and use the median (§B4). Other-vendor review only for auth, payment, personal data or L3.

### D2b. Calibration (reduces score drift) [S4]
- Before scoring, the Critic reads `~/.maestro/design-calibration/` (proposed): 3 scored examples (one ~30, one ~40, one ~46) with per-criterion reasons. Until the owner supplies examples, the DD writes them from the first two projects and the owner confirms.
- Awwwards view (informative, for "award ambition" briefs) [S5]: Design 40% = mean(Hierarchy, Typography, Layout, Color, Richness, Polish); Usability 30% = mean(Responsiveness, Accessibility); Creativity 20% = Originality; Content 10% = Cohesion + copy quality judged at G5.

### D2c. Benchmark test ("better than Apple", award-ambition briefs)
At G2 the DD picks the closest apple.com page or product page (same surface mode). The runner captures it at 375/768/1440 with ours. A fresh critic scores both blind with the rubric. PASS = ours ≥ benchmark on ≥ 8 of 10 criteria and never lower by ≥ 2 on any. Apple captures are reference only, never copied (C1 rules).

## §E Effects
The effects library (E01–E24 with technique, start parameters, cost, fallback and owner D/M) is skill `references/effects.md`. VISUAL-BRIEF "EFFECTS" names each chosen effect with its parameters. Owner M items go to the Motion Director through MOTION HANDOFF; the design team never writes animation code.

## §F Model and seat routing per sub-task

Evidence levels: VERIFIED-PUBLIC = public leaderboard result for the same model family on a matching task (note: arena runs use Max/xHigh effort, our presets use medium/high, so transfer is still UNVERIFIED); KIT-RULE = owner constraint; UNVERIFIED = judgment, to be settled by the A/B protocol.

| Sub-task | Primary seat | Challenger for A/B | Evidence | Reason |
|---|---|---|---|---|
| Art direction, concept, critique, sign-off | DD (Opus 5.5 high) | none | KIT-RULE + VERIFIED-PUBLIC: Opus 5.5 #1 WebDev overall 1809, #1 frontend board [S23, S33] | Highest-ranked web/frontend model; owner keeps DD on Opus |
| Hero / signature section code | DD (Opus 5.5 high) | Sonnet 5.5 medium | VERIFIED-PUBLIC: Image-to-WebDev Opus 1749 vs Sonnet 1740 [S34] (small gap) | Taste-critical; gap small, so A/B decides whether Sonnet can draft and Opus revise |
| Wireframe / IA / section table | Sonnet 5.5 medium (L/XL), DD (S/M) | Codex Sol medium | UNVERIFIED | Structured writing task; cheaper seat adequate if DD approves |
| Design-token system (decide) | DD | none | UNVERIFIED | Token values are taste decisions |
| Token implementation + visible build-out (class B) | Opus 5.5 high design seat | Sonnet 5.5 medium, Codex Sol 1/2 medium | VERIFIED-PUBLIC (partial): Sonnet 5.5 #3 vs GPT-6.1 Sol #4 WebDev, 1769 vs 1752 at max effort [S23]; Design Arena 1326 vs 1320, tie [S24] | Quality-first default is Opus (owner rule); Sonnet/Sol near tie with each other but below Opus on WebDev; a cheaper seat takes visible build-out only after F1 shows it within 1 point (B5) |
| Copy | Sonnet 5.5 medium + `oc-copywriting`; DD approves hero/CTA | Opus for hero line only | UNVERIFIED | Copy drives layout; DD approval keeps voice |
| Raster images / key art | Codex Sol + `$imagegen` (gpt-image-2) | Figma `generate_image` / Canva `generate-image` (session tools) | VERIFIED-PUBLIC: gpt-image-2 #3 text-to-image 1381 [S25] | Kit rule; newer gpt-image-2.5 variants are preliminary and not configured |
| Logos / marks / icons | DD hand-written SVG | none | KIT-RULE | Vector, editable, no raster artifacts |
| Posters / OG / direction boards | DD with `canvas-design` | `$imagegen` | UNVERIFIED | Philosophy-led static art |
| Visual QA from screenshots (defects) | Fresh Opus 5.5 critic seat (no authoring context) | Sonnet 5.5 medium fresh session | UNVERIFIED: no public vision-QA benchmark found | Same-vendor fresh reviewer is the owner default; freshness, not vendor, provides independence; DD keeps final score |
| Accessibility audit | Luna low runs tools; Critic triages | — | Tool-based (axe install needs owner approval) | Deterministic checks beat model opinion |
| Screenshot capture, dev server, diff | Codex Luna low | — | KIT-RULE (runners) | Mechanical; cheapest seat (Luna #40 WebDev, not for design) [S23] |
| Editable design file for owner review | Figma MCP (`use_figma`, `get_screenshot`, `search_design_system`) after loading `figma-use` / `figma-generate-design` | Canva for social/brand assets | Session tool list [S28] | Only when the owner wants Figma; code is the source of truth |

### F1. A/B protocol (the way to settle model choice per task class; DD or Maestro runs it)
1. Pick one brief per task class: (a) landing hero + 1 section, (b) dense dashboard panel, (c) content/editorial section. Freeze VISUAL-BRIEF.md, REFERENCES.md and COPY.md so only the model varies.
2. Recruit model A and model B with the identical brief (B7 template), same skills, same time box (30 min), separate floors.
3. Luna runner captures both at 375/768/1440 (C5). Rename outputs to `X-*` / `Y-*` (blind).
4. Two judges score blind with the rubric (skill rubric.md): the DD and a fresh Opus critic seat. Average the two; record per-criterion scores, tokens and wall time.
5. Decision (quality first): a stronger challenger replaces the primary if its mean total ≥ primary + 2 with no hard fail. A cheaper challenger may take that task class only if mean ≥ primary − 1, no criterion ≥ 2 lower and no hard fail (B5). Class A never moves off Opus. Re-run when a model, preset or effort changes, and at most every 90 days per class.
6. Record in `~/.maestro/design-ab/RESULTS.md` (proposed): date, task class, models/effort, scores, cost, decision. Update this routing table's evidence column to "VERIFIED-LOCAL <date>".

