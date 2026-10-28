---
name: design-excellence
description: Kit design doctrine for premium UI. Load first when designing, building or critiquing any page, screen or component where visual quality matters. Covers hierarchy, type, spacing, color and depth, static effects, Apple-grade polish, anti-slop checks and the 0–5 rubric. Instruction-only, no scripts, no network.
---

# Design excellence

Bar: work that holds up next to Apple's own pages at 375, 768 and 1440 px, and is still clearly this product.
Hierarchy first, then richness. A beautiful page that fails accessibility fails.

## When to use
- Use for new visual directions, redesigns, premium pages, signature sections, design systems and visual QA.
- Skip for a pure bug fix inside an existing design system with no new visual decision.
- The project's existing design system and the brief's explicit words always win over these defaults.
- Motion: specify intent only (what moves, why, reduced-motion equivalent). The Motion team implements every animation.

## The craft loop
1. Subject first. Find the concept in the product's own world (materials, tools, places, people). Write it in one sentence.
2. Token plan. Fill the token-level visual brief: type scale, grid, spacing, OKLCH palette with contrast table, one depth strategy, effects with parameters, at least 5 rejected defaults.
3. Review the plan against the brief and `references/anti-slop.md`. Revise anything a similar prompt would also produce.
4. Wireframe with real copy. Run the hierarchy checklist in `references/hierarchy.md` on a grey-box render.
5. Build the vertical slice: hero, one representative section and footer.
6. Screenshot at 375, 768 and 1440. Score with `references/rubric.md` from the screenshots, never from code.
7. Fix the lowest criterion first. Every remedy names a concrete value (px, token, ratio, property).
8. Polish pass with `references/polish.md`, then theme the browser surfaces (selection, caret, scrollbars, focus ring).

## Rules that always hold
- One focal element per screen. It wins by size, contrast or isolation.
- One depth strategy across the product: border-only, subtle shadow, layered shadow or surface variation.
- One signature element that only this product would have, visible in at least 3 places.
- Extremes in type contrast: display and body weights at least 300 apart; h1 to body size ratio at least 3 on desktop.
- Body text 16–20 px, measure 45–75 characters, never centered beyond 3 lines.
- Body contrast at least 4.5:1; large text and UI parts at least 3:1.
- Every state designed: default, hover, active, focus-visible, disabled; loading, empty, error and long content for data.
- Effects only with parameters and fallbacks (`references/effects.md`). No effect is a default.
- No placeholder services (picsum, lorem ipsum) in a final build. Logos and marks are hand-written SVG.

## Hard fails (any one fails the work regardless of score)
Body contrast below 4.5:1; horizontal scroll at 375; no visible focus; a critical or serious automated accessibility violation; layout shift visible on load; motion without a reduced-motion path.

## References (read only the one the current step needs)
| File | Read when |
|---|---|
| `references/hierarchy.md` | Wireframe, page structure, squint/swap/signature/token tests |
| `references/type.md` | Choosing faces, building the scale, fluid type, numerals |
| `references/color-depth.md` | Palette, contrast, dark mode, shadows, radii, materials |
| `references/effects.md` | Picking any visual effect (E01–E24, with owner Design or Motion) |
| `references/polish.md` | Final polish pass (P1–P20) |
| `references/anti-slop.md` | Direction review, slice review, render QA |
| `references/rubric.md` | Scoring, thresholds, fix-list format |
| `references/web-interface-guidelines.md` | Code review of accessibility, focus, forms, content handling, performance |
| `references/sources.md` | Checking where a rule comes from ([S#] tags) |

## Evidence
- Score only from screenshots you opened; cite the screenshot path per criterion. No screenshot means NOT_PROVEN.
- Never claim a check, capture or accessibility run happened unless it ran.
