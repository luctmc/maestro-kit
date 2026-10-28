# Color, contrast and depth

## Palette (OKLCH first, hex fallback)
- Build every color in `oklch()` [S22]: fixed hue per family, lightness steps, chroma at most 0.2 for UI.
- Neutrals: 9–11 steps from L 0.98 to L 0.15, tinted toward the brand hue (chroma 0.005–0.02). No pure gray text on colored backgrounds [S29].
- Brand: 1 accent, at most 1 secondary. Accent chroma 0.12–0.2.
- Semantic: success, warning, danger, each with a text-safe and a fill variant.
- Proportion: about 60/30/10 neutral, secondary, accent. The accent covers about 10% of the surface.
- Trace the palette to the subject's physical world: name at least 3 of 5 key colors after a source (e.g. "kiln brick", "harbor fog").
- Generate hex fallbacks at build time only when a target browser needs them.

## Contrast
| Pair | WCAG 2.2 minimum [S11] |
|---|---|
| Body text on its background | 4.5:1 |
| Large text (≥ 24px, or ≥ 18.66px bold) | 3:1 |
| UI components and focus indicators | 3:1 |

- Put a contrast table in the visual brief: every text/background pair with its ratio.
- APCA is advisory only [S13]: use it to tune thin display weights and dark mode, never to pass something WCAG fails.
- Interactive states increase contrast: hover, active and focus are more prominent than rest.

## Depth (choose ONE strategy for the whole product)
| Strategy | Use when | Key tokens |
|---|---|---|
| Border-only | Dense apps, editorial calm | 1px borders, 2–3 neutral steps |
| Subtle shadow | Product UI with few layers | 1–2 shadow tokens, low alpha |
| Layered shadow | Premium cards and objects that lift | 3–5 stacked shadows (effect E02) [S30] |
| Surface variation | Dark UIs, minimal chrome | Lightness steps per elevation (effect E03) |

- Shadows show elevation; borders show structure.
- Layered shadows: offsets and blurs double per layer, one global light direction, shadow hue is the background hue at lower lightness [S30]. Never animate layered shadows.
- Specular top edge for raised surfaces: `inset 0 1px 0` white at α 0.08–0.15 on dark, 0.6–0.8 on light (effect E07).

## Radius
- Radius on a scale (sm, md, lg).
- Concentric rule: outer radius = inner radius + padding.
- Continuous (squircle) corners only through an SVG mask or CSS `corner-shape` where supported (support UNVERIFIED); fall back to a standard radius.

## Dark mode (tuned, not inverted)
- Elevation by lightness: each level +0.02–0.04 L.
- Borders carry structure: rgba(255,255,255,.06–.12).
- Desaturate semantic colors and lower accent chroma slightly so they do not glow.
- Set `color-scheme: dark` on `<html>` and `<meta name="theme-color">` to the page background.

## Materials (blur, translucency)
- Use a material only where content passes beneath it and hierarchy needs it (apple-design skill §12).
- Glass needs a fallback: at least 0.6 opacity background, an opaque surface under `prefers-reduced-transparency`, and an `@supports` fallback (effect E08).
- List each material use in the visual brief; anything not listed is removed.

## Image separation
- Images on same-tone backgrounds get a 1px inset outline: `rgba(0,0,0,.1)` on light, `rgba(255,255,255,.1)` on dark [S43].
