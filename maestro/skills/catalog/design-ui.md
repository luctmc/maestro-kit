# Design and UI
name | source | use when | do NOT use when | conflict/preference
Source codes and global choice rules: see ../CATALOG.md

frontend-design | AN | Guidance for distinctive, intentional visual design when build… | - | PREFERRED for new UI visual direction; AN
animate | EK | Build an animation from scratch, making the decisions in the o… | - | PREFERRED for UI animation (Maestro rule)
animate-expo | EK | Build animations in React Native and Expo, making the decision… | - | -
animation-performance | EK | Keep web animations inside the frame budget — animate composit… | - | -
animation-vocabulary | EK | Reverse-lookup glossary that turns a vague description of a we… | - | -
apple-design | EK | Apple's approach to interface design and fluid, physical motio… | - | -
ask-sonner | EK | Guide to Sonner, the React toast library — install and wire up… | - | -
break-ui | EK | Try to break a piece of UI by feeding it worst-case data — lon… | - | -
emil-design-eng | EK | This skill encodes Emil Kowalski's philosophy on UI polish, co… | - | -
find-animation-opportunities | EK | Search a codebase or UI for places that don't animate but shou… | - | -
improve-animations | EK | Survey a codebase's animation and motion code as a senior moti… | - | codebase motion audit
mobile-native | EK | Make a web app feel native on a phone — the small CSS and meta… | - | -
pick-ui-library | EK | Pick the right library for a given frontend task from a curate… | - | -
prototype | EK | Build multiple genuinely different versions of a UI piece you… | - | UI prototypes; overlaps MP prototype
review-animations | EK | Reviews animation and motion code against a high craft bar der… | - | PREFERRED for motion review
write-swift | EK | How to write modern Swift well — modeling with value types, Sw… | - | -
motion-background | IA/motion-design | add an animated background; build a mesh/gradient background | - | -
60fps-animation | IA/web-animation | fix janky CSS animation; make animation 60fps | - | overlaps EK animation-performance (prefer EK)
accessible-animation | IA/web-animation | respect prefers-reduced-motion; honor reduced motion | - | use alongside EK
ascii-animation | IA/web-animation | make an ASCII animation; build a terminal/CLI intro or loader | - | -
glassmorphism | IA/web-animation | add a glassmorphism effect; frosted glass UI | - | -
gsap-web | IA/web-animation | build a scroll animation; add ScrollTrigger | - | -
lottie-animation | IA/web-animation | add a Lottie animation; play a .lottie or .json animation | - | -
micro-interaction | IA/web-animation | add a hover/press effect; animate a toggle or switch | - | overlaps EK animate (prefer EK)
page-transition-animation | IA/web-animation | animate page or route transitions; use the View Transitions AP… | - | -
svg-animation | IA/web-animation | animate an SVG; make a line draw itself on | - | -
