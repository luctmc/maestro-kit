# Hierarchy and page structure

## Hierarchy checklist (wireframe and render QA; each item pass/fail)
1. One named focal element per viewport-height screen; it wins by size, contrast or isolation, and the brief says which.
2. Squint test (blurred screenshot, e.g. 8px Gaussian) still shows reading order: focal, then supporting, then action.
3. At most 3 visible levels of text emphasis per section, each using at least 2 levers (size, weight, color).
4. Exactly one primary action per screen; secondary actions visibly quieter.
5. Headings scale by the declared ratio; no two adjacent steps closer than 1.2×.
6. Related items closer than unrelated items (internal spacing smaller than external spacing, ratio at least 1:2).
7. Grouping by space and weight before borders and boxes; no element's border is the first thing the eye lands on.
8. Body text at least 16px on mobile, measure 45–75ch, never centered beyond 3 lines.
9. Long content, empty and error states keep the same hierarchy (check with worst-case data, e.g. the `break-ui` skill).
10. Mobile is a re-composition, not a shrink: the focal element is still first and above the fold at 375×667.

## Page structure and storytelling (WIREFRAME.md)
Fill one row per section.

Rhythm rules:
- Never two consecutive sections with the same layout pattern or the same density.
- After every two D3/D4 sections, place a D1/D2 "breath".
- Alternate contained and full-bleed at least once per three sections.
- Exactly one signature moment above 50% scroll depth and one echo of it near the end.
- The CTA appears at the hook, after proof, and at the coda.

Density: D1 airy, D2 open, D3 standard, D4 dense.

| # | Role | Job (one sentence the visitor should take away) | Layout pattern | Density | Bleed | Focal element | Copy source | Motion beat (handoff) |
|---|---|---|---|---|---|---|---|---|
| 1 | Hook | | | D1/D2 | full | | COPY.md §1 | |
| 2 | Proof / credibility | | | D3 | contained | | | |
| 3 | Tension (problem / why now) | | | D2 | | | | |
| 4 | Mechanism (how it works) | | | D3/D4 | | | | |
| 5 | Showcase (product or work up close) | | | D1 | full | | | |
| 6 | Depth (details, specs, features) | | | D4 | contained | | | |
| 7 | Social proof | | | D2/D3 | | | | |
| 8 | Objection / FAQ | | | D3 | contained | | | |
| 9 | Offer / CTA | | | D1 | | | | |
| 10 | Coda / footer | | | D3 | | | | |

Section roles are a menu, not a mandatory order; a portfolio may be Hook, Showcase ×3, Coda.
Layout pattern vocabulary: split asymmetric (7/5, 8/4), full-bleed media, type-as-image, sticky-aside narrative, staggered or broken grid, horizontal sequence, index/list, single statement, data/specimen table, gallery masonry.

## Surface modes (set how much expression the work earns)
- persuade: landing and marketing pages; expression high, one signature moment.
- operate: apps and dashboards; restraint, density and state coverage first.
- read: docs and editorial; measure, rhythm and typographic detail first.
- experience: portfolios and showcases; expression highest, usability floor unchanged.
(Mode split adapted from Impeccable, Apache-2.0 [S29].)

## Identity tests (direction review, slice review, render QA)
- Swap test: replacing the fonts and layout with a template changes the identity. If nothing is lost, the design has no identity.
- Squint test: reading order survives at 375 and 1440.
- Signature test: point to 3 places the signature appears.
- Token test: token names and values read as this product, not as a generic kit.
(Tests adapted from oc-showcase and interface-design, MIT [S47].)
