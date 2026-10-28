# Apple-grade polish rules (P1–P20)

Run as the final pass before sign-off. Each rule has a check you can perform on a screenshot or computed style. Sources in brackets; [S#] tags point to sources.md.

| # | Rule | Check |
|---|---|---|
| P1 | Concentric radii: outer = inner + padding [oc-showcase; S43] | Nested rounded elements measured |
| P2 | Optical alignment: icon side ≈ 2px less padding; play/arrow glyphs nudged to visual center [oc-showcase; S43] | Zoomed screenshot |
| P3 | `font-variant-numeric: tabular-nums` on every changing number [S43] | Prices, counters, tables |
| P4 | Display tracking negative (−0.02 to −0.04em, floor −0.04em); small caps text +0.06em [S29; S8] | Computed styles |
| P5 | `text-wrap: balance` h1–h3, `pretty` body [S16, S17] | No orphans in headings at 3 widths |
| P6 | More space above a heading than below it [S29] | Computed margins |
| P7 | Hit area ≥ 44×44px via padding or pseudo-element; never below WCAG 24×24 [S12; S43] | Snapshot bounds |
| P8 | Icon stroke weight matches adjacent text weight; one icon set; no emoji icons [S43; oc-showcase] | Visual |
| P9 | Image outline: 1px inset `rgba(0,0,0,.1)` light / `rgba(255,255,255,.1)` dark to separate images from same-tone backgrounds [S43] | Visual |
| P10 | Shadows for elevation, borders for structure; layered shadows tinted with the background hue [S43; S30] | Token review |
| P11 | Theme browser surfaces: `::selection`, `caret-color`, scrollbars, focus ring, `text-underline-offset`, link underline thickness [S29] | Screenshot of selected text, focus |
| P12 | No layout shift: `aspect-ratio`/width-height on media; font fallback metrics (`size-adjust`) [house rule] | Load capture |
| P13 | Materials (blur/translucency) only where content passes beneath and hierarchy needs it [apple-design §12] | Visual brief lists each use |
| P14 | Every interactive state designed: default/hover/active/focus-visible/disabled; data: loading/empty/error [oc-showcase] | State screenshots |
| P15 | Real content and imagery; no placeholder services (picsum, lorem) in final [S41; house rule] | grep build output |
| P16 | Dark mode tuned, not inverted: desaturated semantics, luminance elevation, borders carry structure [oc-showcase] | Dark captures |
| P17 | Copy names actions; errors name problem and recovery [frontend-design] | Copy review |
| P18 | Font rendering checked on macOS and Windows captures; `-webkit-font-smoothing: antialiased` only for light-on-dark if the brief accepts it [S43; trade-off UNVERIFIED] | Two OS captures if available |
| P19 | Continuous (squircle) corners only via SVG mask or CSS `corner-shape` where supported; support UNVERIFIED, fallback to standard radius | Feature check |
| P20 | Press feedback, transitions and any movement specified for Motion team (e.g. press scale 0.97) — design never ships un-specified motion [emil-design-eng skill] | MOTION HANDOFF lists it |
