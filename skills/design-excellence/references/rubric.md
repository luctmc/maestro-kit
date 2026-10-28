# Rubric, thresholds and fix list

## Rubric (score each 0–5 from screenshots at 375/768/1440; cite the screenshot path per score)

| Criterion | 1 (poor) | 3 (competent) | 5 (exceptional) |
|---|---|---|---|
| Hierarchy | No clear focal point; competing elements | Clear focal point on desktop; weaker on mobile | Reading order unmistakable at every viewport; squint test passes |
| Typography | Default/system faces, flat scale | Deliberate pair, consistent scale | Type carries the identity; scale, leading, tracking, measure all tuned; display type used as image |
| Layout & grid | Arbitrary widths, misalignments | Consistent grid, some monotony | Grid is felt and broken on purpose; proportion carries meaning |
| Color & contrast | Muddy or generic palette; contrast failures | Coherent palette; contrast passes | Palette traceable to the subject's world; accent used with discipline; dark mode tuned |
| Richness / depth / effects | Flat or decorative noise | Some depth, applied uniformly | Light, texture and depth create material; effects serve hierarchy; no gratuitous effects |
| Originality | Recognizable template/AI default | Some distinctive choices | Signature visible in ≥ 3 places; swap test fails for a generic replacement |
| Cohesion | Sections look like different sites | Consistent tokens | Every section belongs to one system with intentional variation |
| Responsiveness | Breaks or shrinks at 375 | Works at 3 viewports | Each viewport re-composed; focal element preserved; no horizontal scroll |
| Accessibility | Contrast/focus/semantics failures | Automated checks pass | Keyboard path, focus styling, reduced-motion and screen-reader labels designed, not patched |
| Polish | Misaligned, inconsistent states | States present, minor defects | Concentric radii, optical alignment, tabular numbers, every state designed; no visible defect |

Scores 2 and 4 are in-between anchors.

## Pass thresholds
- Premium PASS: total ≥ 40/50, no criterion < 3, Hierarchy ≥ 4, Typography ≥ 4, Accessibility ≥ 4.
- Award ambition / "better than Apple" PASS: total ≥ 44/50, Originality, Richness and Polish ≥ 4, and a blind benchmark test against the closest apple.com page won on ≥ 8 of 10 criteria (never lower by ≥ 2 on any).
- Hard FAIL regardless of score: body text contrast < 4.5:1 (WCAG 2.x AA); horizontal scroll at 375; missing visible focus; any automated a11y violation of impact "critical" or "serious"; layout shift on load visible in screenshots; motion without a reduced-motion path.
- NOT_PROVEN: any criterion scored without a rendered screenshot.
- Scorer independence: draft scores by a fresh critic session with no authoring context, same vendor as the author; final score by the design lead. If the two totals differ by > 5, the lead writes a one-line reconciliation per criterion with ≥ 2 points gap.

## Mandatory fix-list format (QA and polish reports)

| ID | Sev | Component | Viewport | State | Defect (observable) | Remedy (concrete value) | Evidence |
|---|---|---|---|---|---|---|---|
| F-01 | P0 | Hero CTA | 375 | default | CTA below fold at 375×667 (top at 702px) | Reduce h1 clamp max at 375 to 44px; move CTA above supporting image | qa/home-375.png |
| F-02 | P1 | Feature cards | 1440 | hover | Card lifts 8px and shifts siblings | Use transform translateY(-2px) only; no margin change | qa/home-1440-hover.png |

Severity: P0 blocks release (hard-fail item or hierarchy broken); P1 visible quality defect; P2 polish. A remedy without a concrete value (px, token, ratio, property) is rejected.
