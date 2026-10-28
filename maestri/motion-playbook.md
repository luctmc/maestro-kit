# Motion playbook (reference — load the section you need, not the whole file)
Sections: B1 roles · B2 spawn + effort rule · B3 presets, recruit commands + render brief · B4 helper brief · B5 Design/Motion ownership · C0 stack + capture commands + fix loop · C1–C6 job workflows · D motion tokens · D10 Apple-grade polish checklist · E recipes R01–R28 · F rubric · F2 calibration benchmarks · G1 skill loading map.
Numbers in section D override any skill. Runtime roles: maestri/roles/motion-director.md, motion-helper.md, motion-render.md. Gate: maestri/quality-gates.md (Motion gate). Skill catalog: maestro/skills/catalog/motion.md.
Legend: `[L]` verified on the owner's machine (2026-10-28). `[W]` verified on the web (sources at the end). `[H]` heuristic chosen by this playbook (craft decision, not a sourced fact). `UNVERIFIED` = check before relying on it.

---

## B. Team and helper policy

### B1. Roles (all Claude Opus 5.5)

| Role | Preset | Effort | Owns (writes) | Never does |
|---|---|---|---|---|
| Motion Director (lead) | `Motion Director` (Maestro flag ON) | high | `MOTION-BRIEF.md`, `STORYBOARD.md`, `motion/tokens.(css\|ts)`, final `MOTION-QA.md` verdict, integration of helper output | grade its own build as final; recruit non-Opus helpers for motion |
| Motion Engineer (role `Motion Helper`, mode Engineer) | `Motion Helper` (Maestro OFF) | high | the scene/component files assigned in its brief only (e.g. `src/motion/hero.ts`, `film/scenes/s03.html`) | change storyboard, tokens or another engineer's files |
| Motion Critic (role `Motion Helper`, mode Critic) | `Motion Helper` (Maestro OFF) | high | `qa/rN/MOTION-QA-rN.md`, frames it extracts | edit source; read builder reasoning |
| Sound/Rhythm (films with audio only; role `Motion Helper`, mode Sound) | `Motion Helper` (Maestro OFF) | high | `audio/*`, cue sheet | move picture cuts without Director approval |
| Motion Render Operator (role `Motion Render`) | `Motion Render` (Maestro OFF) | **medium** | `out/**`, `qa/rN/captures/**` (renders, exports, captures, contact sheets, ffprobe/loudness logs) | author or change any command, parameter, source file, storyboard or score; judge quality |

Why no separate "Motion Designer/storyboard" helper: storyboard is the creative contract; splitting it from the Director adds a handoff and loses intent.
Why a medium-effort render operator (owner decision, 2026-10-28): long finals (motion-blur renders take 20–60 min per the `explainer-*` skills), multi-format exports and 3-viewport capture batches block the Director's context while adding no judgement. The operator stays Claude Opus 5.5 (model lock intact); medium effort is allowed **only** because every command it runs is authored verbatim by an Opus-high author. Any decision (fps, crf, crop, timing, which frames to sample) is made upstream and written into its brief. No Codex, Sonnet, Haiku or Luna anywhere in motion.

### B2. When to spawn a helper (token break-even) `[H]`
A recruited Opus helper pays a fixed start-up: role text + brief + 2–3 skills + reading the storyboard and tokens ≈ 20–30k input tokens (estimate from file sizes: role ~1k, skills 6–12 KB each, playbook sections ~8k). Rules:
1. **Critic: always** spawn a fresh one per review round on anything beyond a single micro-interaction. Independence is the value, not speed.
2. **Engineer:** spawn only when there are **≥ 2 independent units with disjoint files** (scenes, sections, components) **and** each unit is ≥ ~45 min of work, or when the Director's own context is above ~60% and the remaining unit is self-contained. Otherwise the Director builds it.
3. **Never** spawn a helper for: a single component, token tweaks, a re-render, a fix list under 5 items.
4. **Concurrency:** max 3 helpers at once (kit rule); a 4th requires telling the owner.
5. **Helpers cannot recruit** (preset Maestro flag OFF). Only the Director (flag ON) recruits.
6. **Re-use before recruit:** `maestri list` first; continue an existing helper with `maestri ask` when its context still holds the scene.
7. **Effort rule (owner decision):**
   | Work | Preset | Effort |
   |---|---|---|
   | concept, storyboard, tokens, animation code, fixes, edit decisions, critique/scoring | `Motion Director` / `Motion Helper` | high |
   | running renders, exports, transcodes, captures, contact sheets, ffprobe/loudness/frozen-time **from a command list written by an Opus-high author** | `Motion Render` | medium |
   | anything else, or any doubt | `Motion Helper` | high |
   A Render Operator spawn pays off only when the batch blocks the Director for **> ~15 min** of wall time (final with motion blur, ≥ 3 formats/aspects, 3-viewport scroll captures of a long page). Shorter batches: the Director runs them itself with `run_in_background`. If a render fails or a capture looks wrong, the operator reports the exact error/path and stops; it never edits source or changes parameters (only an identical retry is allowed).

### B3. Exact preset and recruit commands
```bash
# one-time setup (owner runs or approves)
maestri preset create "Motion Helper" --command "claude --dangerously-skip-permissions --model claude-opus-5-5 --effort high" --maestro off
maestri preset create "Motion Render" --command "claude --dangerously-skip-permissions --model claude-opus-5-5 --effort medium" --maestro off
# paste maestri/roles/motion-helper.md and maestri/roles/motion-render.md whole into Maestri → Agentes → Responsabilidades as roles "Motion Helper" and "Motion Render"

# per mission (Director runs)
maestri list
maestri recruit "mx-eng-1" --preset "Motion Helper" --role "Motion Helper"       # brief says "Mode: Engineer"
maestri recruit "mx-critic-r1" --preset "Motion Helper" --role "Motion Helper"   # fresh per round; brief says "Mode: Critic"
maestri recruit "mx-render-1" --preset "Motion Render" --role "Motion Render"    # only per B2 rule 7
```
Render Operator brief (the only brief allowed for the medium preset; every line is filled by an Opus-high author):
```markdown
# Render brief: <batch id>
Model/effort: claude-opus-5-5 / medium (Motion Render). First reply line: model confirmation.
Commands (run exactly, in order; do not edit):
1. <command>   → expected output <path>
2. <command>   → expected output <path>
Verify after each: file exists, `ffprobe` line matches <codec/size/fps/duration>.
On any error or mismatch: stop, report command #, exact error line, paths. Identical retry once allowed.
Owned paths: out/<batch>/**, qa/<round>/captures/**. Do not open or edit source, STORYBOARD.md, tokens.
Report max 10 lines: DONE | BLOCKED + paths + ffprobe lines. No git writes. No quality opinions.
```
Model IDs must still be validated in the installed CLI before first use (kit rule). If `claude-opus-5-5` is unavailable, the helper returns `BLOCKED_MOTION_MODEL`.

### B4. Helper brief template (copy-paste; scores ≥ 7/10 on the kit brief score)
```markdown
# Brief: <unit id> — <one-line goal>
Mode: Engineer | Critic | Sound. Owner/model/effort: <helper name> / claude-opus-5-5 / high. First line of your reply: model confirmation.
Goal: <what the viewer/user must perceive, one sentence>
Contract (immutable): STORYBOARD.md rows <S03–S05>; tokens motion/tokens.css; recipes <R03, R11>.
Values: section D of maestri/motion-playbook.md overrides any value inside a skill.
Owned paths (write only these): <list>
Forbidden paths: everything else, especially STORYBOARD.md, tokens, other scenes.
Skills to use: <2–4 exact names>; read ~/.agents/skills/review-animations/STANDARDS.md before finishing (do not invoke; it is model-disabled).
Deliverable: <files> + stills at t=<list> via `node render.mjs … --stills` (or capture script C0.2) at qa/<unit>/.
Checks you must run: <commands from C0>; report frame paths, not opinions.
Done = all rows implemented at storyboard timings ±1 frame, stills inspected by you, no console errors.
Report: max 10 lines, DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED, paths. Update HANDOFF.md. No git writes.
```

### B5. Design Director ↔ Motion Director on a premium site
Both are Opus 5.5 high, so collaboration never violates the lock. The risk is the **third party**: Sonnet/Codex builders implementing non-motion parts.

| Artifact / file | Owner | Other director's right |
|---|---|---|
| `VISUAL-BRIEF.md` (concept, type, grid, palette, layout) | Design Director | Motion comments in a `## Motion notes` section |
| `MOTION-BRIEF.md`, `STORYBOARD.md` (scroll map / transitions) | Motion Director | Design approves that layout states match artboards |
| Design tokens (`tokens.css`: color, type, space) | Design Director | read-only |
| Motion tokens (`motion/tokens.css` or `.ts`) | Motion Director | read-only |
| Static components / page markup | Design Director or delegated builder | Motion may only add `data-motion="<recipe-id>"` hooks via a request list |
| All animation code: `src/motion/**`, `*.motion.(ts\|tsx\|css)`, ScrollTrigger/Lenis setup, View Transition CSS, keyframes | Motion Director / Motion Engineer | Design reviews the render |
| Final visual sign-off | Design Director (static) + Motion Director (motion) | each can block |

Sequence: Design vertical slice (static, 3 viewports) → Motion scroll map on that slice (STORYBOARD rows per section with recipe IDs) → joint approval → parallel build (Design/builders static, Motion animation in its own files) → Motion Critic round on recorded scroll + Design visual QA → fixes → both PASS.

Lock enforcement for non-Opus builders (copy into their briefs): "You write zero animation code: no `transition`, `@keyframes`, `animation`, `gsap`, `motion.`/`framer-motion`, `animate(`, `ScrollTrigger`, `view-transition`. Add `data-motion` hooks only." Gate check run by the Maestro before merge:
```bash
rg -n "transition|@keyframes|animation:|gsap|framer-motion|from ['\"]motion|\.animate\(|ScrollTrigger|view-transition" <files owned by non-Opus builders>
# must return nothing (hover colour transitions excepted only if listed in MOTION-BRIEF)
```

---

## C. Workflow per job type

### C0. Shared stack rule, capture pipeline and fix loop

**C0.1 Stack rule (decide before concept)** `[L][W]`
```bash
git config user.email; git remote -v; basename "$PWD"
cat package.json 2>/dev/null | python3 -c "import json,sys;d=json.load(sys.stdin);print({**d.get('dependencies',{}),**d.get('devDependencies',{})})"
ls LICENSE* CONTRIBUTING* .maestri/ 2>/dev/null
```
- Work project = email `lucas.castro@montreal.com.br`, or folder `CIINTEC*` (kit rule `e2f1dd3`), or repo policy says so. **Never Remotion.** Reason: Remotion requires a paid Company License for organisations of 4+ people — https://www.remotion.dev/docs/license/faq, https://remotion.dev/license.
- Personal project (`luctmc@outlook.com`): Remotion allowed in addition.
- Web, cheapest first (from `animate`, EK): CSS transition → `@starting-style` → CSS animation / scroll-driven CSS → WAAPI → Motion (motion.dev) for springs, layout, exit, gestures (React) → GSAP (+ScrollTrigger, SplitText, Flip) for timelines and scroll choreography → Lenis only if the brief asks for smooth scroll → Three.js/R3F only for spatial content → Rive/Lottie only when a designer supplies the file. Extend existing repo deps; never add a second library for the same job.
- Video in work projects: HTML + GSAP paused timeline + `window.seek(t)` → Playwright → ffmpeg (renderer = `render.mjs` from `~/.agents/skills/explainer-engaging/SKILL.md`, copied into the project). Motion Canvas only if the repo already uses it. HyperFrames (HeyGen, HTML+GSAP→MP4, open-sourced 2026-04-17) is a strong alternative but **not installed** — candidate in I1.

**C0.2 Capture-and-review pipeline (exact commands)**
Installed `[L]`: `ffmpeg`/`ffprobe` 9.0.2, `node` 26.10, `agent-browser` 0.39.1, Playwright Chromium 1248 cache, `maestri portal`. Not installed: ImageMagick, gifski, Python Playwright, Python ≥ 3.10.
Project-local install needed once (`npm i -D playwright` — the npx cache holds an alpha, do not rely on it).

(a) Deterministic stills of a film or seekable page (any frame, any order):
```bash
node render.mjs film.html qa/r1/sheet.png --stills 0.5,1.2,2.0,3.4,5.1,7.0   # one time per storyboard row + every transition midpoint
node render.mjs film.html qa/r1/draft.mp4 30 1 4                            # draft: 30fps, no blur, 4 workers
node render.mjs film.html out/final.mp4 60 8 8                              # final: 60fps, 8 subframes motion blur
```
(b) Web motion that is time-driven (CSS/WAAPI/GSAP non-scroll): freeze and step time in the page instead of trusting real-time playback.
```js
// qa/step.mjs — node qa/step.mjs http://localhost:5173 "#hero" 0,100,200,300,450,700
import { chromium } from 'playwright';
const [url, sel = 'body', ts = '0,100,200,400,800'] = process.argv.slice(2);
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1440, height: 900 } });
await p.clock.install();                         // fakes Date, timers, requestAnimationFrame (playwright.dev/docs/clock)
await p.goto(url); await p.evaluate(() => document.fonts.ready);
let last = 0;
for (const t of ts.split(',').map(Number)) {
  await p.clock.runFor(t - last); last = t;      // advances JS-driven animation (GSAP ticker, rAF)
  await p.evaluate(ms => document.getAnimations().forEach(a => { a.pause(); a.currentTime = ms; }), t); // CSS/WAAPI
  await p.locator(sel).screenshot({ path: `qa/step-${String(t).padStart(5, '0')}.png` });
}
await b.close();
```
`page.clock.install()`/`runFor()` semantics: https://playwright.dev/docs/clock `[W]`. Whether every library honours the fake rAF is library-specific — verify on the first frame pair (UNVERIFIED for Lenis and R3F; for those use (c)).

(c) Scroll choreography: sample scroll positions, not time.
```js
// qa/scroll.mjs — node qa/scroll.mjs http://localhost:5173 1440 900 40
import { chromium } from 'playwright';
const [url, w = 1440, h = 900, n = 40] = process.argv.slice(2);
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: +w, height: +h } });
await p.goto(url); await p.evaluate(() => document.fonts.ready);
const max = await p.evaluate(() => document.documentElement.scrollHeight - innerHeight);
for (let i = 0; i <= n; i++) {
  const y = Math.round(max * i / n);
  await p.evaluate(y => { window.lenis ? window.lenis.scrollTo(y, { immediate: true }) : scrollTo(0, y);
                          window.ScrollTrigger?.update(); }, y);
  await p.waitForTimeout(350);                   // let scrub smoothing settle; set scrub:true (not a number) in QA builds
  await p.screenshot({ path: `qa/scroll-${w}-${String(i).padStart(3, '0')}.png` });
}
await b.close();
```
Then contact sheet (ffmpeg only, no ImageMagick):
```bash
ffmpeg -v error -y -framerate 1 -i qa/scroll-1440-%03d.png -vf "scale=480:-1,tile=6x7:padding=4:color=gray" -frames:v 1 qa/scroll-1440-sheet.png
```
Run at 1440×900, 768×1024, 390×844.

(d) Real-time recording (feel, jank, scrub smoothing) — agent-browser:
```bash
agent-browser open http://localhost:5173
agent-browser set viewport 1440 900
agent-browser record start qa/r1/scroll.webm
agent-browser scroll down 600; agent-browser wait 800; agent-browser scroll down 600; agent-browser wait 800   # repeat to the end
agent-browser record stop
ffmpeg -v error -y -i qa/r1/scroll.webm -vf "fps=4,scale=480:-1,tile=6x6" -frames:v 1 qa/r1/scroll-rt-sheet.png
```
In the Maestri canvas use `maestri portal resize "Portal" 390 844` + `maestri portal scroll …` + `maestri portal screenshot "Portal"` for spot checks the owner can watch.

(e) Dense transition window (1/30 s around each cut or transition, per the Gauntlet):
```bash
ffmpeg -v error -y -ss 4.8 -t 0.6 -i out/final.mp4 -vf "fps=30,scale=360:-1,tile=6x3" -frames:v 1 qa/r1/t04_8.png
```
(f) Frozen time, loudness, metadata (scripts from `business-motion-film`):
```bash
S=~/.agents/skills/business-motion-film/scripts
bash $S/frozen-time.sh out/final.mp4 0.35       # near-frozen seconds; target < 5% of runtime outside planned holds
bash $S/loudness.sh out/final.mp4               # -14 LUFS punchy / ~-16 LUFS calm; true peak <= -1 dBFS (business-motion-film quality-bar.md); <= -4 dBFS when the sound-effects pipeline mixes
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt,duration -of compact out/final.mp4
```
(g) Reduced motion and performance:
```bash
agent-browser set media reduced-motion          # then re-run (c) at 1440 and inspect
agent-browser trace start; agent-browser scroll down 3000; agent-browser trace stop qa/r1/trace.json
```
In-page long-frame probe (Chromium only; LoAF = frame > 50 ms — https://developer.mozilla.org/en-US/docs/Web/API/Performance_API/Long_animation_frame_timing):
```js
new PerformanceObserver(l => l.getEntries().forEach(e => console.log('LoAF', Math.round(e.duration), e.scripts?.[0]?.sourceURL)))
  .observe({ type: 'long-animation-frame', buffered: true });
```

**C0.3 Fix loop (all job types)**
Round = build → capture (C0.2) → fresh Critic scores with rubric F → Director picks the top 3–5 defects by severity → fix → new Critic verifies item by item (FIXED / PARTLY / STILL) + regressions. **Cap: 4 rounds** (Gauntlet data: 3–5 rounds reach diminishing returns). After round 4 with any criterion < 3: stop, report `DONE_WITH_CONCERNS` with the open defect list; do not loop silently.

### C1. Web scroll hero / scroll story
- Inputs: VISUAL-BRIEF static slice at 3 viewports, copy, assets (SVG/3D/image sequences), performance target device.
- Concept: 2 directions only if new identity; each = one sentence + scroll map + 1 signature recipe (e.g. "R01 pinned story + R03 mask lines" vs "R16 product rotation + R08 depth parallax").
- Storyboard format (scroll map):
```markdown
| Section | Trigger start → end (scroll %) | Pin? | Hero element / recipe | Support / recipe | Easing token | Reduced-motion fallback |
| S1 hero | 0 → 100vh | no | headline R03 (load) | nav R17 | --ease-out-expo | fade 200ms |
| S2 story | top top → +=300% | yes | product R16 scrub | captions R03 per step | scrub: none (linear) | static frames + text |
```
- Build: tokens first; one ScrollTrigger timeline per pinned section; `gsap.matchMedia()` branches for `(prefers-reduced-motion: reduce)` and `(max-width: 767px)`; `ScrollTrigger.refresh()` after fonts/images load.
- Capture: C0.2 (c) at 3 widths + (d) real-time + (g) reduced-motion + LoAF.
- Delivery: source files, `MOTION-QA.md` with sheets, perf numbers, reduced-motion sheet.

### C2. Page transitions
- Inputs: router type (MPA, Next App Router, SPA), list of route pairs, shared elements.
- Concept: pick one transition family for the site (Material's pattern choice is a good rule: shared-axis for sibling navigation, container transform for list→detail, fade-through for unrelated pages — https://material.io/design/motion/the-motion-system.html `[W]`).
- Storyboard: table route A → route B, shared element names, duration, direction.
- Stack: MPA same-origin → cross-document View Transitions `@view-transition { navigation: auto; }` (Chrome/Edge 126+, Safari 18.2+, Firefox not supported per Chrome docs — https://developer.chrome.com/docs/web-platform/view-transitions `[W]`); SPA → `document.startViewTransition`; Next App Router → `page-transition-animation` skill (template.tsx + AnimatePresence or View Transitions). Unsupported browsers get an instant swap (no polyfill).
- Capture: (b) stepped at 0/60/120/180/240/320 ms during navigation; check both directions (back navigation reverses direction).
- Delivery: CSS/TS + QA sheet per route pair.

### C3. Micro-interactions
- Inputs: component list, interaction frequency per component.
- Concept: none (frequency gate from `animate` decides). No style frames.
- Storyboard: one line per component: trigger, purpose word, properties, token, interruption rule.
- Stack: CSS transitions / `@starting-style` first; Motion springs only for gesture/drag.
- Capture: (b) stepped frames at 0/50/100/150/200 ms + hover gating check at 390 px (touch).
- Review: Critic reads `review-animations` SKILL.md + STANDARDS.md and outputs its required "Before | After | Why" table + Block/Approve.
- Delivery: diff + table.

### C4. Brand film / explainer
- Inputs: BRIEF (`business-motion-film` step 1 template), length, aspect ratios, brand assets, truth constraints, music licence.
- Concept: 2 directions as one-paragraph treatments + tone cell (`motion-art-direction` matrix) + 3 signature transformations.
- Storyboard format:
```markdown
| # | In–Out (s) | Frames @60 | What the viewer sees | Job of the beat | Hero / recipe | Transition out + carried element | Audio cue |
| 1 | 0.00–1.20 | 0–72 | logo mark draws | brand | R20 | mark scales into S2 headline dot (R19) | riser start |
```
12–15 compositions per 30 s; lead subject fills 60–85% of the usable frame in feature beats (from `business-motion-film`).
- Stack: C0.1 video rule. One root GSAP timeline, scenes as labelled sub-timelines, `window.seek(t)` pure.
- Style frames: `render.mjs --stills` at 3 key times before building the rest.
- Capture: (a) stills per row, draft MP4, (e) per transition, (f) frozen/loudness/ffprobe.
- Delivery: master MP4 1080p60 H.264 yuv420p, poster frame, contact sheet, source HTML, Gauntlet ledger.

### C5. Animated carousel / social
- Inputs: platform, slide count, aspect (4:5 1080×1350 or 9:16 1080×1920), autoplay or swipe.
- Concept: one carried element across slides (continuity across swipes), cover slide hook.
- Storyboard: per slide: hold time (reading time `[H]`: 0.35 s per word + 0.6 s), entrance recipe, exit.
- Stack: same seek-renderer; export per-slide MP4 (≤ 60 s each; check platform limits — UNVERIFIED per platform, check at delivery) or one 9:16 MP4.
- Safe areas `[H]`: keep text inside the central 80% width and away from the top 14% and bottom 20% of 9:16 frames (platform UI overlays; exact zones vary by app — UNVERIFIED).
- Capture: (a) stills at each slide's mid-hold; (e) every slide boundary.

### C6. Logo animation
- Inputs: SVG master (outlined paths), brand rules (clear space, min size), sound or silent.
- Concept: 2 builds that reveal the logo's **construction idea**, not a generic effect.
- Storyboard: 2–4 s, rows at frame level.
- Stack: SVG + GSAP (DrawSVG/MorphSVG are free — Webflow source above) or CSS `pathLength`; video via seek-renderer; web via inline SVG.
- Capture: (a) every 6 frames for the whole sting + final hold frame at 100% and at 64 px tall (legibility).
- Delivery: MP4 (with/without alpha: ProRes 4444 `.mov` when alpha is needed: `ffmpeg -i frames/%05d.png -c:v prores_ks -profile:v 4444 -pix_fmt yuva444p10le logo.mov`), web SVG/JS, poster PNG.

---

## D. Motion language spec (default tokens)

One spec for everything. A project may override **once**, in `MOTION-BRIEF.md`, with reason. Values chosen to agree with `animate` (EK) for UI and with `motion-art-direction` hierarchy rules for films; conflicts in A5 resolved as stated.

### D1. Easing (cubic-bezier) — 4 curves, 2 used in ~90% of moves
| Token | Value | Use | Source |
|---|---|---|---|
| `--ease-out` | `cubic-bezier(0.23, 1, 0.32, 1)` | all UI enters/exits, hovers that move | `animate` (EK) `[L]` |
| `--ease-out-expo` | `cubic-bezier(0.16, 1, 0.3, 1)` | marketing reveals, hero landings, film entrances | most frequent curve in installed skills (16 hits) `[L]` |
| `--ease-in-out` | `cubic-bezier(0.77, 0, 0.175, 1)` | element moving/morphing while on screen, camera moves | `animate` (EK) `[L]` |
| `--ease-exit` | `cubic-bezier(0.7, 0, 0.84, 0)` | film only: accelerating exit of an element leaving frame | installed skills (expo-in) `[L]` |
| `--ease-drawer` | `cubic-bezier(0.32, 0.72, 0, 1)` | drawers/sheets only | `animate` (EK) `[L]` |
| `linear` | — | scrub, marquee, progress, spinners | — |
Forbidden: `ease-in` on UI; bare `ease-in-out`/`ease`; `cubic-bezier(0.4,0,0.2,1)`; overshoot curves except the Playful personality (`cubic-bezier(0.34,1.56,0.64,1)`, bounce ≤ 10%).
GSAP mapping `[H]`: register exact curves once with CustomEase (free) and use the names in every tween (recipes in E use these names):
```js
gsap.registerPlugin(CustomEase);
CustomEase.create('out', '0.23,1,0.32,1'); CustomEase.create('out-expo', '0.16,1,0.3,1');
CustomEase.create('in-out', '0.77,0,0.175,1'); CustomEase.create('exit', '0.7,0,0.84,0');
```
Do not approximate with `power3.out`/`expo.out`.

### D2. Duration scale
| Token | ms | Use |
|---|---|---|
| `--dur-0` | 0 | keyboard-triggered, 100+/day actions |
| `--dur-1` | 120 | press feedback, toggles |
| `--dur-2` | 180 | tooltips, small popovers, hover moves |
| `--dur-3` | 240 | dropdowns, tabs indicator, list item enter |
| `--dur-4` | 320 | modals, drawers (enter); page transitions |
| `--dur-5` | 480 | marketing section reveals |
| `--dur-6` | 720 | hero entrance, film element entrances |
| `--dur-7` | 1100 | film hero moves, camera pushes |
Rules: UI ≤ `--dur-4` (≤ 300 ms target per EK); exits = 70% of the matching enter `[H]`; films use multiples of a base unit = `--dur-5` at 60 fps (≈ 29 frames) `[H]`.

### D3. Springs (Motion / motion.dev)
| Token | Config | Use |
|---|---|---|
| `spring.ui` | `{ type: "spring", visualDuration: 0.3, bounce: 0 }` | layout, shared element in UI |
| `spring.alive` | `{ type: "spring", visualDuration: 0.45, bounce: 0.15 }` | cards, playful elements |
| `spring.gesture` | `{ type: "spring", duration: 0.5, bounce: 0.2 }` | drag release, swipe dismiss (EK) |
`visualDuration` overrides `duration`; `bounce` default 0.25; setting stiffness/damping/mass overrides both — https://motion.dev/motion/transition/ `[W]`. Bounce cap 0.3; 0 for finance/serious content.

### D4. Stagger
| Group | Step | Cap |
|---|---|---|
| characters | 18 ms | total ≤ 500 ms; else split by words |
| words | 45 ms | ≤ 12 words per staggered line |
| lines | 90 ms | — |
| list items / cards | 50 ms | total ≤ 300 ms (EK 30–80 ms range); items beyond 6 enter together |
| film: support after hero | 100 ms lag | support starts after hero is ≥ 60% complete |

### D5. Distance, scale, blur, depth
- UI enter translate 8–12 px; section reveal 24–40 px; hero 64–96 px or full mask (`yPercent: 100` inside an overflow-hidden line).
- Scale from 0.96 (UI), 0.92 (cards), 0.85 (hero); never 0.
- Bridge blur 4–8 px max, only during crossfades.
- Parallax layer ratios: background 0.25, mid 0.6, foreground 1.0, overlay 1.12; max 3 moving layers per viewport.
- Rotation: UI 0°; type 0–4°; 3D object scroll rotation ≤ 180° per viewport height scrolled.

### D6. Choreography rules
1. One hero per frame/viewport. Support travel ≤ 60% of hero travel, starts ≥ 1 stagger step later.
2. Exits before entrances; overlap ≤ 30% of the exit.
3. One axis per scene (all vertical or all horizontal); direction reverses only to mean "back".
4. Every transition carries something from the previous scene (shape, colour or direction) — kept from the installed role, made checkable: the storyboard column "carried element" must be non-empty.
5. Films: land → hold 0.3–0.6 s → accelerating exit. Never move text the viewer is still reading.
6. One "wow" moment per piece (from `motion-art-direction`).
7. Texture/ambient: loops ≥ 8 s, opacity change ≤ 10%, never behind body text.

### D7. Hierarchy of attention
Order of reveal = reading order: headline → key visual → supporting copy → CTA → chrome. CTA never animates in later than 1.2 s after its section enters. Navigation and data the user reads never move for style (EK `animate` "function" rule).

### D8. Performance budgets
- Animate `transform`, `opacity`, `clip-path` only (`filter: blur` only on ≤ 2 elements simultaneously) — https://web.dev/articles/animations-guide `[W]`.
- `will-change` added just before animation and removed after; never in global CSS (web.dev guidance: sparingly) `[W]`.
- 0 long animation frames > 50 ms during scroll/interaction on the target desktop; ≤ 2 on a throttled (4× CPU) run `[H]`.
- Animation must not change layout: CLS contribution 0.
- Motion JS budget ≤ 70 KB gzip for all motion libraries combined `[H]`; lazy-load Three.js only for sections that use it.
- Canvas/WebGL: DPR capped at 2; pause render loop when offscreen (IntersectionObserver) and when `document.hidden`.
- Video frames: 1080p60 H.264 `yuv420p` CRF 16–18 for masters; social exports per platform.

### D9. Reduced motion (ships with the animation)
- `prefers-reduced-motion: reduce` ⇒ remove translate/scale/rotate/parallax/pin-scrub/smooth-scroll; keep opacity and colour changes ≤ 200 ms; show final states. Lenis disabled; ScrollTrigger pins replaced by static stacked sections.
- Autoplaying motion > 5 s running next to other content needs a visible pause control (WCAG 2.2.2 Level A) — https://www.w3.org/WAI/WCAG21/Understanding/pause-stop-hide `[W]`. Interaction-triggered motion must be disableable (WCAG 2.3.3 AAA, met via reduced-motion) — https://dequeuniversity.com/resources/wcag2.1/2.3.3-animations-from-interactions `[W]`.
- Never convey information only through motion (Apple HIG) — https://developer.apple.com/design/human-interface-guidelines/motion `[W]`.
- Hover motion gated by `@media (hover: hover) and (pointer: fine)` (EK).
- No flashing > 3 per second anywhere (WCAG 2.3.1) `[H]` standard requirement.

Token file (copy into `motion/tokens.css`):
```css
:root{
  --ease-out:cubic-bezier(.23,1,.32,1); --ease-out-expo:cubic-bezier(.16,1,.3,1);
  --ease-in-out:cubic-bezier(.77,0,.175,1); --ease-exit:cubic-bezier(.7,0,.84,0); --ease-drawer:cubic-bezier(.32,.72,0,1);
  --dur-1:120ms; --dur-2:180ms; --dur-3:240ms; --dur-4:320ms; --dur-5:480ms; --dur-6:720ms; --dur-7:1100ms;
  --stagger-char:18ms; --stagger-word:45ms; --stagger-line:90ms; --stagger-item:50ms;
  --dist-ui:10px; --dist-section:32px; --dist-hero:80px; --scale-ui:.96; --scale-card:.92;
}
@media (prefers-reduced-motion: reduce){ :root{ --dist-ui:0px; --dist-section:0px; --dist-hero:0px; --scale-ui:1; --scale-card:1; } }
```

### D10. Apple-grade motion polish checklist (run before every Critic round)
Source: `apple-design` skill (EK, installed), which distils Apple WWDC18 "Designing Fluid Interfaces" (talk confirmed via https://github.com/nathangitter/fluid-interfaces `[W]`; Apple URL/session number 803 UNVERIFIED) — plus `review-animations` STANDARDS.md and the `business-motion-film` quality bar `[L]`. Each item is binary; one "no" blocks PASS on rubric criterion 6 (Polish).
1. **Response ≤ 1 frame.** Visual change on `pointerdown`, not `click` (`:active { transform: scale(.97); transition: transform 100ms var(--ease-out) }`). Measure: stepped capture (C0.2 b) at 16.7 ms steps after the press.
2. **1:1 tracking.** Drags follow the pointer every frame, keep the grab offset, use `setPointerCapture`; no animation only at gesture end.
3. **Interruptible from the presentation value.** Reversing mid-flight starts from the on-screen value; jump between consecutive frames at the reversal ≤ 2 px. Input is never locked during a transition.
4. **Springs for anything touchable.** Default critically damped (`bounce: 0`); bounce 0.15–0.2 only after a momentum gesture. Apple values: reposition damping 1.0 / response 0.4; drawer/sheet 0.8 / 0.3.
5. **Velocity handoff + projection.** Release velocity feeds the spring; snap target chosen from `project(v) = (v/1000)·0.998/(1−0.998)` (exponential decay, as `apple-design` gives it), not from the release point.
6. **Boundaries resist.** Over-drag rubber-bands; no hard stop, no free overshoot.
7. **Symmetric paths, anchored origins.** Exit along the entry path; popovers scale from the trigger; mirrored easing on reversible transitions.
8. **Clean landings.** The last 3 frames of every move differ by < 0.5 px (no creep, no 1-frame pop). Final state is `transform: none` / no `will-change`, so text renders crisp after landing.
9. **No dead frames in crossfades.** Through every crossfade the combined content stays legible: no frame where both layers are below ~50% opacity over an empty background; no text over text (check every frame of the crossfade, not just settled frames). `[H]` threshold.
10. **Frame 0 and the last frame are finished compositions** (films, loops, carousels; loop seam `seek(duration) == seek(0)`).
11. **Restraint.** Exactly one signature moment; everything else is quieter than the content.
12. **Reduced motion is designed**, not broken: the reduced capture tells the same story with fades and final states.
13. **Feel checks done and logged:** 0.25× playback (DevTools Animations panel or stepped capture), frame-by-frame through each transition, gestures on a real device, second look after a break (`review-animations` STANDARDS.md "Debugging").

---

## E. Recipe library (28 signature moves)

Format: ID · name — when · stack · parameters · skeleton · failure modes. Skeletons are minimal; values come from D.

**R01 · Pinned scroll story** — one product/idea explained in 3–5 steps while the section stays fixed. GSAP ScrollTrigger.
```js
const tl = gsap.timeline({ scrollTrigger: { trigger: '#story', start: 'top top', end: '+=300%', pin: true, scrub: true, anticipatePin: 1, invalidateOnRefresh: true } });
tl.to('.step-1', { autoAlpha: 0, y: -32 }).from('.step-2', { autoAlpha: 0, y: 32 }, '<0.2') /* … */;
```
Params: end = +=100% per step; scrub `true` (or 0.5 s smoothing with Lenis off). Fails: pin jump on fast scroll (use `anticipatePin: 1` — gsap.com docs `[W]`), wrong lengths after font load (call `ScrollTrigger.refresh()` after `document.fonts.ready`), mobile address-bar resize (`ScrollTrigger.config({ ignoreMobileResize: true })`).

**R02 · Horizontal pinned track** — gallery/timeline. Same as R01 with `tl.to(track, { x: () => -(track.scrollWidth - innerWidth), ease: 'none' })`. Fails: vertical text unreadable while moving (pause steps with snap `1/(n-1)`), keyboard users can't reach items (provide focusable list).

**R03 · Mask line reveal** — headlines, statements. GSAP SplitText (free).
```js
const s = SplitText.create('.h1', { type: 'lines', mask: 'lines' });
gsap.from(s.lines, { yPercent: 100, duration: .72, ease: 'out-expo', stagger: .09 });
```
Fails: split before fonts load (wrap in `document.fonts.ready`), re-split on resize (use SplitText `autoSplit` + `onSplit`), screen readers reading fragments (SplitText 3.13 adds aria handling per Webflow note `[W]`; verify).

**R04 · Clip-path image reveal** — imagery entering. `clip-path: inset(100% 0 0 0)` → `inset(0)`, `--dur-6`, `--ease-out-expo`, image inside scales 1.12 → 1 over the same time. Fails: clip on element with border-radius (animate `inset(… round 16px)`), Safari repaint on huge images (limit to ≤ 2 simultaneous).

**R05 · Shared-element (same document)** — list → detail in an SPA.
```js
el.style.viewTransitionName = 'card-42';
document.startViewTransition(() => render(detail));
```
CSS: `::view-transition-group(card-42){ animation-duration: 320ms; animation-timing-function: var(--ease-in-out); }`. Fails: duplicate names (each must be unique on the page), text distortion during size morph (crossfade `::view-transition-old/new` contents, or keep text outside the group).

**R06 · Cross-document transition** — MPA/static site. `@view-transition { navigation: auto; }` on both pages + named shared elements. Fallback: instant. Fails: different origin (no transition), long page loads (transition waits; keep pages fast).

**R07 · FLIP layout change** — filter/sort/reorder grid. GSAP Flip or Motion `layout`. `Flip.getState(items); reorder(); Flip.from(state, { duration: .32, ease: 'in-out', absolute: true, stagger: .02 })`. Fails: images stretching (`scale: false` for content or animate wrappers), focus lost after reorder.

**R08 · Depth parallax** — layered hero. CSS scroll-driven where supported, else ScrollTrigger.
```css
@supports (animation-timeline: view()) {
  .layer-bg { animation: drift linear both; animation-timeline: view(); animation-range: cover; }
  @keyframes drift { from { transform: translateY(-8%) } to { transform: translateY(8%) } }
}
```
Ratios from D5. `view()` is not Baseline (MDN) — https://developer.mozilla.org/docs/Web/CSS/animation-timeline/view `[W]`: final state must be the default without support. Fails: more than 3 moving layers (noise), parallax on text (motion sickness), forgetting reduced-motion.

**R09 · Scroll progress / reveal in pure CSS** — reading progress bar, simple reveals. `animation-timeline: scroll(root)` for progress; `view()` + `animation-range: entry 0% entry 60%` for reveals. Fails: same support caveat as R08.

**R10 · Magnetic button** — premium CTA on desktop.
```js
const xTo = gsap.quickTo(btn, 'x', { duration: .4, ease: 'out' }), yTo = gsap.quickTo(btn, 'y', { duration: .4, ease: 'out' });
btn.addEventListener('pointermove', e => { const r = btn.getBoundingClientRect(); xTo((e.clientX - r.left - r.width / 2) * .3); yTo((e.clientY - r.top - r.height / 2) * .3); });
btn.addEventListener('pointerleave', () => { xTo(0); yTo(0); });
```
Strength 0.2–0.35, only `(hover:hover) and (pointer:fine)`. Fails: target moves away from cursor and misses clicks (cap travel 12 px), used on every button (only 1 CTA per view).

**R11 · Cursor follower / label cursor** — portfolios, galleries. `quickTo` x/y on a fixed element, 0.35–0.5 s. Fails: hiding the native cursor (never), lag on low-end (disable below 60 fps measured).

**R12 · Number counter** — stats. `gsap.to(obj, { v: target, duration: 1.1, ease: 'out-expo', snap: { v: 1 }, onUpdate: () => el.textContent = fmt.format(obj.v) })`, `font-variant-numeric: tabular-nums`, `Intl.NumberFormat('pt-BR')`. Fails: width jitter (tabular nums + fixed min-width), screen readers announcing every tick (`aria-live` off; put the final value in `aria-label`).

**R13 · Marquee** — logos, ticker. CSS: two copies of the content, `@keyframes { to { transform: translateX(-50%) } }`, `linear`, 30–60 s per loop. Pause on hover/focus; stop under reduced motion; provide pause control if > 5 s and next to content (WCAG 2.2.2). Fails: gap jump at loop (copies must be identical width), text marquees (unreadable).

**R14 · SVG path draw** — diagrams, signatures, logo lines. `<path pathLength="1" style="stroke-dasharray:1;stroke-dashoffset:1">` → offset 0, `--dur-6`, `--ease-in-out`. Fails: non-scaling strokes on responsive SVG (`vector-effect: non-scaling-stroke` only if intended), paths with fills drawing as strokes (separate fill fade after draw).

**R15 · Gradient / shader background** — brand atmosphere. Option A CSS: `@property --a { syntax:'<angle>'; inherits:false; initial-value:0deg }` + conic/radial gradients animated over ≥ 12 s. Option B WebGL fragment shader (single full-screen quad, DPR ≤ 1.5 for backgrounds, pause offscreen). Fails: the "generic gradient blob" anti-pattern (only if the brief asks for atmosphere; tie colours to brand), banding (add 1–2% noise), battery drain (pause when hidden).

**R16 · 3D object scroll rotation** — product hero. R3F/Three: progress from ScrollTrigger → `rotation.y = damp(current, progress * Math.PI, 6, dt)`. Lights fixed; camera pitch 15–35°. Fails: top-down camera turning objects into slabs (Gauntlet: limit pitch), first-load pop (show poster image until GL ready), mobile heat (lower DPR, fewer lights). Alternative: R23 image sequence when the model is not available.

**R17 · Staggered entrance** — lists, nav, cards. CSS `@starting-style { opacity:0; transform: translateY(var(--dist-ui)) }` + `transition-delay: calc(var(--i) * var(--stagger-item))`. Fails: everything at once (no stagger), stagger > 300 ms total (cap 6 items).

**R18 · Kinetic headline (film)** — statements in films. Words: `yPercent:110 → 0`, `rotate: 4 → 0`, word stagger 45 ms, `--ease-out-expo` 0.72 s; hold 0.3–0.6 s; exit `yPercent:-110` with `--ease-exit` 0.4 s. Fails: text overlapping text mid-crossfade (outgoing leaves before incoming enters — Gauntlet), > 7 words on screen in 9:16.

**R19 · Match cut / carried element** — every film transition. Last frame of scene A and first frame of scene B share an object at identical pixel coordinates (Gauntlet rule); then B moves it. Fails: 1–12 px jumps (compute positions from the same layout function), z-order flips.

**R20 · Logo build** — stinger. Sequence: stroke draw (R14) 0.6 s → fill fade 0.2 s → wordmark mask reveal (R03) 0.5 s → hold 1.0 s. Fails: generic "everything scales up with glow"; logo distortion (never non-uniform scale a brand mark).

**R21 · Data bar / chart grow** — stats, explainers. Bars `scaleY: 0.001 → 1` from bottom origin, stagger 50 ms, values via R12, axis first. Fails: animating before labels are readable, misleading partial states in screenshots (final state is default).

**R22 · Sticky card stack** — features, testimonials. Each card `position: sticky; top: 10vh`; previous card scales 1 → 0.94 and dims to 0.6 as the next arrives (ScrollTrigger scrub or `view()` timeline). Fails: content hidden under stacked cards for keyboard users (all content in DOM order and focusable).

**R23 · Image-sequence scrub** — product rotation/assembly without real-time 3D. Pre-rendered frames (WebP/AVIF, 60–120 frames) drawn to canvas by scroll progress. Fails: network weight (≤ 3 MB total target `[H]`, lazy-load after first paint), blurry on retina (size frames for DPR 2 of the canvas box).

**R24 · Hover tilt card** — galleries, pricing. Pointer position → `rotateX/rotateY` ±6° with `spring.alive`, perspective 800 px, glare layer opacity ≤ 0.15. Pointer-fine only. Fails: tilt on touch (gate), text blurring under 3D (keep text layer at translateZ(0) and small angles).

**R25 · Drawer / toast / modal** — UI chrome. Use `~/.agents/skills/animate/RECIPES.md` exactly (EK); toasts with transitions not keyframes. Fails: listed in EK "Never Ship" table.

**R26 · Beat-cut montage (film)** — energetic sections. Cuts on beats from the music grid (`sound-effects` beat check or `beat-sync-editing` technique); 4–8 frames of motion before each cut; never cut mid-read. Fails: cuts drifting off-beat after tempo change, flashing > 3/s.

**R27 · Zoom-through transition** — moving from overview to detail in films/sites. Scale an element of scene A (a window, a dot, a letter counter) to fill the frame, then scene B is revealed inside it. `--ease-in-out`, 0.6–0.9 s. Fails: raster pixelation (vector or high-res source), motion sickness on web (reduced-motion: crossfade).

**R28 · Skeleton → content morph** — loading states. Crossfade skeleton to content with 4 px blur bridge, 240 ms, no layout shift (same box sizes). Fails: content jumping (reserve sizes), shimmer running forever (stop after load; shimmer is ambient, ≥ 1.2 s period).

---

## F. Motion rubric (Critic and Director)

Score each criterion 0–5 on the actual renders/captures. Anchors:

| # | Criterion | 1 | 3 | 5 |
|---|---|---|---|---|
| 1 | Intent | motion with no nameable purpose | every move has a purpose word; some decoration | every move serves the brief; one clear signature; restraint visible |
| 2 | Timing & easing | default/mixed curves, sluggish UI | tokens used, some off-scale values | all values from D; holds and accelerations feel deliberate at 0.25× and 1× |
| 3 | Choreography | everything at once or random order | hero/support order mostly right | one hero per frame, lead-follow, exits before entrances, one axis per scene |
| 4 | Typography legibility | text moves while being read / clipped | readable at 1×; minor collisions | every line readable at mid-hold, inside safe areas, at 390 px and 64 px logo size |
| 5 | Continuity | hard jumps, no carried element | carried element in most transitions | every transition carries shape/colour/direction; pixel-exact match cuts |
| 6 | Polish | flicker, pops, broken masks | no defects at 1×; small pops at frame level | clean frame-by-frame in dense transition windows; no frozen time outside planned holds |
| 7 | Performance | jank visible, layout properties animated | compositor-only; occasional long frame | 0 LoAF > 50 ms on target; CLS 0; video metadata correct |
| 8 | Accessibility | no reduced-motion path | reduced-motion exists but loses information | reduced-motion sheet complete; pause controls; no motion-only information; hover gated |

**Thresholds:** PASS = every criterion ≥ 3 **and** mean ≥ 4.0 **and** criteria 1, 2 and 8 ≥ 4. Any criterion ≤ 1 = FAIL. Otherwise FAIL with the defect list.

**NOT_PROVEN rules:** any criterion whose evidence was not actually viewed is scored `NP`, not a number. Specifically: no frames/sheet = criteria 2–6 NP; no reduced-motion capture = 8 NP; no trace or LoAF probe = 7 NP; no audio listen/loudness measure (films) = add "audio NP". Any NP on criteria 1, 2 or 8 ⇒ overall NOT_PROVEN. The critic must list the exact file paths it viewed.

**Defect report format (one line each, sorted by severity):**
```
D-07 | P1 | 00:04.12 (f247@60) | S03→S04 wipe | headline split into "Sur|face" by wipe edge | outgoing title exits before wipe; incoming enters after | qa/r2/t04_0.png
D-08 | P2 | scroll 42% @1440 | S2 pinned | caption 2 visible under caption 1 for ~6% scroll | add 0.1 gap between step tweens | qa/r2/scroll-1440-017.png
```
Severity: P0 = broken/inaccessible/wrong brand or claim; P1 = visible defect at 1× speed; P2 = visible only frame-by-frame or at one viewport; P3 = taste.
Verification rounds mark each previous defect `FIXED | PARTLY | STILL` and list new regressions.

### F2. Calibration: three benchmarks Opus must match
Purpose: replace "looks good to me" with a side-by-side measurement against reference-quality work. The Director captures the reference **with the same pipeline (C0.2)** once per project type, writes the numbers to `calibration/<benchmark>.md` (URL, capture date, viewport, values), and the Critic scores our build against those numbers. References are studied for mechanism and measurements only; no assets, layouts or copy are reused.
Pass rule `[H]`: pacing metrics within ±20% of the reference (or a written reason in MOTION-BRIEF.md); defect metrics (jumps, LoAF, collisions, frozen time) equal to or better than the reference. A build that fails F2 caps rubric criteria 2 and 6 at 3.

**CB1 — Web scroll story: an Apple product page (current flagship page at capture time).**
Why: canonical pinned/sticky scroll storytelling with canvas image-sequence scrubbing; the technique is documented in the CSS-Tricks article "Let's Make One of Those Fancy Scrolling Animations Used on Apple Product Pages" (Jurn van Wissen, 2020; AirPods Pro hero example) — https://css-tricks.com/author/jurnvanwissen/ `[W]`. The specific page and its numbers change over time, so they are measured, not assumed (no Apple values are claimed here).
Capture: C0.2 (c) at 1440×900 and 390×844 with n = 80 samples; (d) real-time recording of one pinned section; (g) reduced-motion and LoAF probe.
Measure and record:
| Metric | How |
|---|---|
| Scroll distance per idea (vh per pinned step) | sample index where caption N appears → disappears |
| Readable-hold distance for each caption (vh where text is static and fully opaque) | consecutive identical caption crops in the scroll sheet |
| Moving elements per viewport (max) | count elements that change between adjacent samples |
| Image-sequence smoothness (px of scroll per frame change) | frames of the canvas per 100 vh |
| Long animation frames during the recorded scroll | LoAF probe count > 50 ms |
| Reduced-motion behaviour | reduced sheet: what remains, what becomes static |

**CB2 — UI interaction: Vaul (drawer) and Sonner (toasts) by Emil Kowalski, plus Apple's "Designing Fluid Interfaces" behaviours.**
Why: open-source, inspectable references for the exact EK bar this spec adopts (`--ease-drawer` is the Ionic/iOS curve used in that family; STANDARDS.md notes Sonner/Vaul positioning) `[L]`; WWDC18 "Designing Fluid Interfaces" defines response, interruption and velocity handoff (session number UNVERIFIED). Demo URLs are the projects' own sites (find them from their GitHub READMEs at capture time; not hard-coded here — UNVERIFIED current URLs).
Capture: C0.2 (b) stepped at 16.7 ms from the trigger for open, close, and a reversal at 50% progress; drag release via Playwright `mouse.down/move/up` with known velocity.
Measure and record:
| Metric | How |
|---|---|
| Response latency (frames from pointerdown to first visual change) | first stepped frame with pixel change |
| Onset → settle time (ms) for open/close | first and last frame with change > 0.5 px |
| Overshoot (px) and settle oscillations | max position beyond target in stepped frames |
| Reversal discontinuity (px between consecutive frames at interrupt) | stepped frames around the reversal |
| Release velocity continuity (px/frame before vs after release) | positions at frames −2…+2 around `mouse.up` |
| Toast stack stagger and exit path | stepped frames with 3 toasts |

**CB3 — Brand/launch film: the `business-motion-film` quality bar applied to a reference film chosen in the brief.**
Why: the only installed benchmark with measured, client-validated targets (`references/quality-bar.md`, `gauntlet.md`) `[L]`. The reference film (owner-supplied or a public launch film named in MOTION-BRIEF.md) is measured with the same scripts so our cut is compared like for like.
Capture: `contact-sheet.sh` every 0.25 s, dense 1/30 s windows at each cut, `frozen-time.sh`, `loudness.sh`, `ffprobe`.
Measure and record (targets from quality-bar.md unless the reference is stricter):
| Metric | Target |
|---|---|
| Frozen time | ≤ ~1 s per 30 s; no single hold > 0.6 s except the final CTA |
| Distinct compositions | 12–15 per 30 s; scale varies (macro/wide/overhead/UI close-up/type) |
| Cuts on beat | every cut within ±1 frame of the beat grid |
| Loudness / dynamics | −14 LUFS punchy or ~−16 calm; true peak ≤ −1 dBFS; LRA ≥ ~3 LU for energetic scores |
| Text | 0 collisions on every crossfade frame; CTA readable at phone size ≥ 1.5 s; WCAG AA on settled text |
| Frame 0 | finished composition |
| Determinism | same frame from two seek orders = identical pixels (`cmp` on two PNGs) |

Shared motion-timing probe (for CB1 recordings; for precise UI timing prefer CB2's stepped capture, since real-time recording frame rate is not guaranteed — check with `ffprobe`):
```bash
# prints intervals where the cropped region is moving: start-end (ms)
ffmpeg -hide_banner -i qa/rec.webm -vf "crop=600:400:420:250,format=gray,tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG" -an -f null - 2>&1 \
 | grep -oE "pts_time:[0-9.]+|YAVG=[0-9.]+" | paste - - | awk -F'[: =\t]' '{t=$2; m=($4>0.2); if(m&&!on){on=1;s=t} if(!m&&on){on=0;printf "motion %.3f-%.3f (%.0f ms)\n",s,t,(t-s)*1000}}'
```
`[H]` threshold 0.2 YAVG; tune once per capture (static region must print nothing). Verified in this session on a synthetic 60 fps clip with one 500 ms move: output `motion 1.017-1.517 (500 ms)`.

---

## G. Skill loading map

All names verified installed in `~/.claude/skills` → `~/.agents/skills` `[L]`. "Read" = load the file with Read because the skill is model-disabled (`disable-model-invocation: true`). Order matters: direction first, technique second, review last.

### G1. Per job type
| Job | Director loads | Engineer loads | Critic loads |
|---|---|---|---|
| Web scroll hero / story | `motion-art-direction`, `gsap-web` | `gsap-web`, `animation-performance` | Read `review-animations` (+STANDARDS.md), `accessible-animation` |
| Page transitions | `page-transition-animation` | `page-transition-animation`, `animate` | Read `review-animations` |
| Micro-interactions | `animate` (+ RECIPES.md) | `animate` | Read `review-animations` |
| Brand film / explainer | `business-motion-film`, `motion-art-direction`, `shot-composition` | one renderer template: `explainer-engaging` (one-take), `explainer-high-energy` (promo) or `explainer-default` (product demo); `kinetic-typography` for type scenes | `business-motion-film` (references/gauntlet.md, critic-prompts.md, quality-bar.md only) |
| Animated carousel / social | `motion-art-direction`, `shot-composition` | `kinetic-typography`, renderer template as above | `business-motion-film` quality-bar.md |
| Logo animation | `logo-animation`, `motion-art-direction` | `svg-animation` | Read `review-animations` STANDARDS.md (cohesion, easing) |
| Films with audio | + `sound-effects` (needs Python ≥ 3.10 venv) | — | loudness via `business-motion-film/scripts/loudness.sh` |
| Personal projects with Remotion | + `remotion-best-practices` (router) | + the routed `remotion-*` skill | same |
| iOS-feel / native-feel UI | + `apple-design` | + `animate-expo` (React Native only) | — |

Use only on explicit need: `animation-vocabulary` (when the owner describes an effect vaguely), `emil-design-eng` (broad UI polish pass with Design Director), `improve-animations` / `find-animation-opportunities` (codebase audit), `color-motion`, `motion-background` (only when the brief asks for atmosphere), `lottie-animation` (designer supplies Lottie), `diagram-animation`, `chart-animation`, `animated-infographic` (data pieces; their Remotion build paths are personal-only).

---

Sources (web): https://webflow.com/updates/gsap-becomes-free · https://github.com/greensock/gsap-skills · https://www.remotion.dev/docs/license/faq · https://remotion.dev/license · https://playwright.dev/docs/clock · https://developer.chrome.com/docs/web-platform/view-transitions · https://developer.mozilla.org/docs/Web/CSS/animation-timeline/view · https://motion.dev/motion/transition/ · https://web.dev/articles/animations-guide · https://web.dev/articles/animations-and-performance · https://developer.mozilla.org/en-US/docs/Web/API/Performance_API/Long_animation_frame_timing · https://developer.apple.com/design/human-interface-guidelines/motion · https://www.w3.org/WAI/WCAG21/Understanding/pause-stop-hide · https://dequeuniversity.com/resources/wcag2.1/2.3.3-animations-from-interactions · https://material.io/design/motion/the-motion-system.html · https://uxmag.com/articles/creating-usability-with-motion-the-ux-in-motion-manifesto · https://motioncanvas.io/docs/rendering/video · https://github.com/iart-ai/motion-skills · https://awesome.ecosyste.ms/projects/github.com%2Femilkowalski%2Fskills · https://github.com/lottiefiles/motion-design-skill · https://cdn.jsdelivr.net/npm/lenis@1.3.23/README.md · https://gsap.com/docs/v3/Plugins/ScrollTrigger/ · https://css-tricks.com/author/jurnvanwissen/ · https://github.com/nathangitter/fluid-interfaces
UNVERIFIED items: WWDC18 session number, current Vaul/Sonner demo URLs, exact Material 3 token values (official page is JS-rendered and could not be fetched; not used in D), Firefox View Transitions status (sources disagree), Safari version for scroll-driven animations (sources disagree; D treats `view()` as progressive enhancement), SplitText aria behaviour, HyperFrames licence, social platform safe-zone sizes.
