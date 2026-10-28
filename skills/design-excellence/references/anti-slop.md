# Anti-slop checklist

Run at direction review, slice review and render QA. Any unchecked item needs a one-line justification tied to the brief; the brief's explicit request always wins. [S#] tags point to sources.md.

Type
- [ ] Display face is not Inter, Roboto, Arial, system-ui, Space Grotesk, or the project's previous default, unless the brand mandates it [S2].
- [ ] Weight contrast between display and body ≥ 300 units (e.g. 200 vs 700), not 400 vs 600 [S1].
- [ ] h1 : body size ratio ≥ 3 on desktop [S1]; scale follows the declared ratio.
- [ ] No single accented word in a headline (italic/color swap) [S3].
- [ ] No tracked ALL-CAPS eyebrow above every heading; no "WORD — fragment" labels; no "A · B · C" meta strings; no "→" appended to every link [S3].
- [ ] Monospace only for code/data content.
Color
- [ ] Palette traceable to the subject's physical world (≥ 3 of 5 hex named after a source).
- [ ] No purple/violet→blue gradient on white; no gradient used as decoration only [S2].
- [ ] Not cream #F4F1EA-ish + serif + terracotta #D97757-ish; not near-black + single acid accent, unless chosen on purpose in the directions [S3].
- [ ] Neutrals tinted toward the brand hue; no gray text on colored backgrounds [S29].
- [ ] One accent (max one secondary) at ≈ 10% of surface.
Layout
- [ ] Hero is not centered headline + subline + two buttons + screenshot, unless justified in brief.
- [ ] Not a uniform grid of identical rounded cards with the same radius and rgba(0,0,0,.1) shadow [S3].
- [ ] No cards nested inside cards; no rounded-square icon tile above every heading [S29].
- [ ] Two adjacent sections never share layout pattern and density (hierarchy.md, page structure).
- [ ] Numbered markers (01/02/03) only for true sequences [S3].
- [ ] At least one intentional grid break and one full-bleed moment per page.
Components and depth
- [ ] One depth strategy across the product (color-depth.md).
- [ ] Radius on a scale; concentric radii (outer = inner + padding).
- [ ] Glass only if selected in VISUAL-BRIEF, with ≥ 0.6 opacity fallback and reduced-transparency path.
- [ ] Icons from one set; no emoji as icons (oc-showcase).
- [ ] Every interactive element has default/hover/active/focus-visible/disabled; data views have loading/empty/error.
Copy
- [ ] No lorem ipsum, no "Unlock the power of", "Seamless", "Elevate", "Revolutionize", "Next-gen" (UNVERIFIED as a sourced list; house rule).
- [ ] CTA names the action ("Book a call", "Save changes"), not "Get started"/"Submit" by default [S3].
- [ ] Real numbers and names in proofs; no fake logos or invented testimonials presented as real.
Imagery
- [ ] No generic stock "team at laptop" or abstract 3D blobs; images obey VISUAL-BRIEF treatment (grade, crop, aspect).
- [ ] AI images reviewed for artifacts (hands, text, logos) before use; logos are hand-written SVG.
Motion (Motion team implements; design checks intent)
- [ ] No fade-and-slide-up on every section; no hover lift on every card [S3].
- [ ] No bounce/elastic easing by default [S29]; one orchestrated page-load moment at most.
- [ ] Every motion beat has a reduced-motion static equivalent.
Final tests (hierarchy.md, identity tests)
- [ ] Swap test: replacing fonts and layout with a template changes the identity.
- [ ] Squint test passes at 375 and 1440.
- [ ] Signature test: point to 3 places the signature appears.
- [ ] Token test: token names and values read as THIS product.
