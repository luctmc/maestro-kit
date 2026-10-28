# Design and UI
name | source | use when | do NOT use when | conflict/preference
Source codes and global choice rules: see ../CATALOG.md
Team: Design Director (Opus 5.5) leads; playbook = ~/.maestro/maestri/design-playbook.md. Entries marked [M] are implemented by Motion Director only.

design-excellence | kit | Core design doctrine: hierarchy, type, spacing, color/depth, effects, Apple-grade polish, anti-slop, rubric; load first for any premium UI | XS fixes inside an existing system | PREFERRED core; kit-owned (skills/design-excellence), no scripts, no network
frontend-design | AN | Any new visual direction or redesign: AI-default calibration list, token plan reviewed against brief, copy rules | pure bug fix inside an existing system | PREFERRED; pair with design-excellence and oc-showcase
oc-showcase | Overclock | Numeric UI doctrine (type ratios, density px, elevation, concentric radius), swap/squint/signature/token tests, pre-delivery checklist | marketing-only art pieces | PREFERRED for product UI and QA checklist; its links to oc-site-premium/oc-design-dna are not installed, ignore them
oc-copywriting | Overclock | Page copy, headlines, CTAs, offer angle before wireframe | UI strings inside an existing product voice | Copywriter seat; DD approves hero/CTA
canvas-design | AN | Key art, posters, OG images, direction boards (static PNG/PDF) | UI code | see images.md; raster photos via $imagegen
animate | EK | [M] Build an animation from scratch | design team work | Motion Director only
animate-expo | EK | [M] RN/Expo animations | design team work | Motion Director only
animation-performance | EK | [M] Frame budget for animations | design team work | Motion Director only
animation-vocabulary | EK | Reverse-lookup glossary that turns a vague description of a we… | - | -
apple-design | EK | Gesture-driven, native-feel, materials, optical type sizing | standard marketing pages | situational; 23 KB, load only when brief needs it
ask-sonner | EK | Guide to Sonner, the React toast library — install and wire up… | - | -
break-ui | EK | G8 QA: worst-case data on content-heavy components (explicit /break-ui) | static art | QA seat
emil-design-eng | EK | G9 polish and design-engineer QA; Before/After/Why table | concept phase (27 KB) | polish pass only
find-animation-opportunities | EK | [M] Find places that should animate | design team work | Motion Director only
improve-animations | EK | [M] Motion code audit | design team work | Motion Director only
mobile-native | EK | Make a web app feel native on a phone — the small CSS and meta… | - | -
pick-ui-library | EK | Library choice for build-out (explicit /pick-ui-library) | when project already has the library | design engineer
prototype | EK | G3 directions and S-size variants on named axes (explicit /prototype) | whole pages in one run | PREFERRED over MP prototype for visual variants
review-animations | EK | [M] Motion review | design team work | Motion Director only
write-swift | EK | How to write modern Swift well — modeling with value types, Sw… | - | -
motion-background | IA/motion-design | [M] animated background | static gradient (design-excellence effect E05) | Motion Director only
60fps-animation | IA/web-animation | [M] fix janky animation | design team work | Motion Director; prefer EK animation-performance
accessible-animation | IA/web-animation | [M] reduced-motion implementation | - | Motion Director; Design checks intent only
ascii-animation | IA/web-animation | [M] ASCII animation | - | Motion Director only
glassmorphism | IA/web-animation | Static glass panels when VISUAL-BRIEF selects glass (design-excellence effects E08/E09) | glass not in brief | glass motion parts [M]
gsap-web | IA/web-animation | [M] scroll animation, ScrollTrigger | design team work | Motion Director only
lottie-animation | IA/web-animation | [M] Lottie | design team work | Motion Director only
micro-interaction | IA/web-animation | [M] hover/press/toggle motion | design team work | Motion Director; prefer EK animate
page-transition-animation | IA/web-animation | [M] route transitions, View Transitions | design team work | Motion Director only
svg-animation | IA/web-animation | [M] SVG animation | design team work | Motion Director only

## Pending owner approval (not installed; do not invoke until installed at the pin)
taste-skill (design-taste-frontend) | Leonxlnx/taste-skill tag v2.1.5 = 12af471f627f866411b4bd785b19646d3672784c | direction library + real-browser inspector | copy skills/taste-skill at the pin, never install.sh; no picsum in final builds
impeccable | pbakaus/impeccable tag skill-v4.8.0 = 414603bf14c7a344edb466bb1f85690c77ce8b7d | 24 design commands + detector | skill folder only (no plugin hooks); IMPECCABLE_NO_TELEMETRY=1 DO_NOT_TRACK=1 IMPECCABLE_API_URL=http://127.0.0.1:9; never live mode
apple-hig | justinwetch/HIGAgentSkills 2206ff935b4affa9ad249a5399a3e8e29f5f6edd | Apple-platform native missions | skill folder only; never run the crawl scripts
oklch-skill | jakubkrehel/oklch-skill 0e81f040e16d48fcc61d3e1b7ea548542371321f | palette generation, APCA/WCAG, gamut | instruction-only
