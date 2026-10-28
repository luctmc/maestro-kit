# Typography

Type carries the identity. Decide it before color.

## Faces
- Pair one display face with one text face. Add monospace only when the content is code or data.
- Display face is not Inter, Roboto, Arial, system-ui, Space Grotesk, or the project's previous default, unless the brand mandates it [S2].
- Record name, source and license for each face in the visual brief. Never ship a face without a web license.
- Pairing works through contrast on one axis (serif vs sans, condensed vs wide, geometric vs humanist) and kinship on another (x-height, proportions, era).

## Extremes rule
- Weight contrast between display and body at least 300 units (e.g. 200 vs 700), not 400 vs 600 [S1].
- h1 to body size ratio at least 3 on desktop [S1].
- Variable fonts: use `wght`, `opsz` and `wdth` axes as hierarchy levers (effect E14).

## Scale
- Base 16px on mobile, 18px from 1024px.
- Ratio 1.250 for product UI, 1.333 for editorial, 1.5–1.618 only for an expressive hero.
- Fluid steps with `clamp()` between the 375 and 1440 viewports (Utopia method [S10]). Default from Utopia: base 18→20px, ratio 1.2→1.25 between 360 and 1240px.
- No two adjacent heading steps closer than 1.2×.

## Leading, tracking, measure
| Text | Leading | Tracking |
|---|---|---|
| Display | 0.9–1.05 | −0.02 to −0.04em (floor −0.04em) |
| Headings | 1.1–1.25 | −0.01 to −0.02em |
| Body | 1.5–1.65 (serif +0.05) | 0 |
| Small caps or caps labels | — | +0.06em (only if labels are used at all) |

- Body measure 60–75ch (45–75ch hard range) [S8].
- `text-wrap: balance` on h1–h3; `text-wrap: pretty` on paragraphs [S16, S17]. `balance` applies to at most 6 lines in Chromium; `pretty` is slower, so use it on body text only.
- More space above a heading than below it.

## Numerals and glyphs
- `font-variant-numeric: tabular-nums` on every number that changes or sits in a column.
- Oldstyle figures for editorial body when the face has them.
- Use `…` not `...`; curly quotes; non-breaking spaces in `10&nbsp;MB` and brand names.

## Loading and rendering
- Preload critical fonts (`<link rel="preload" as="font">`) with `font-display: swap`.
- Prevent layout shift with fallback metrics (`size-adjust`, `ascent-override`) tuned to the web font.
- Check rendering on macOS and Windows captures when available. Use `-webkit-font-smoothing: antialiased` only for light text on dark backgrounds, and only if the brief accepts the thinner look (trade-off UNVERIFIED).

## Display type as image
- Oversized headline cropped by the viewport edge (effect E16): up to 18–22vw, leading 0.85–0.95, tracking −0.03 to −0.05em.
- At 375 no clipped word may change meaning; the full text stays available to assistive technology.

## Bans (see anti-slop.md for the full list)
- No single accented word in a headline (italic or color swap) [S3].
- No tracked ALL-CAPS eyebrow above every heading [S3].
