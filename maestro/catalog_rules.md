# Skill catalog (Maestro)
Read before routing. Format per line: name | source | use when | do NOT use when | conflict/preference.
Sources: SP=superpowers, PT=ponytail, CV=caveman, MP=mattpocock-skills, EK=emilkowalski/skills, RM=remotion-dev/skills, VM=vibe-motion/skills,
IA/<pack>=iart-ai, AN=anthropics/skills, MB=Barty-Bart/motion-graphics, AZ=azure-skills, GC=google-plugins, DN=dotnet/skills, N8=n8n-mcp-skills.

## Quality-first overlay
- Team selection by task type: ~/.maestro/maestri/teams.md (15 teams). Gates and brief template: ~/.maestro/maestri/quality-gates.md.
- Premium UI: Design Director (Claude Opus 5.5 high) composes its team per request; procedure in ~/.maestro/maestri/design-playbook.md; load design-excellence first.
- Motion/video/UI animation: Motion Director and its helpers, Claude Opus 5.5 only ("Motion Render" at medium effort only for mechanical renders); per-job skill map in ~/.maestro/maestri/motion-playbook.md section G1. Never Codex, Sonnet, Haiku or Luna.
- Skills are not evidence of quality; inspect real rendered results and report NOT_PROVEN when they cannot be seen.

## Choice rules
- Overlap -> debugging: SP systematic-debugging. TDD: SP test-driven-development. Code review: MP code-review. Plans/specs: SP brainstorming + writing-plans. Done-check: SP verification-before-completion. UI animation: EK (animate, review-animations). Motion video: Motion Director decides.
- Remotion (any remotion-* skill, IA remotion-video, VM remotion-*): PERSONAL PROJECTS ONLY. Never in work repos (CIINTEC*).
- Cloud/.NET/n8n plugins are OFF globally. Maestro enables them per project (or before recruiting a worker) only when the mission needs them, and tells the user in one line. Never enable all.
- lower-thirds: keep ONLY the copy from tiktok-video-skills. The lower-thirds-skills pack is not installed (name conflict).
- Skills marked CLONES/FETCHES external code need explicit user OK before invoking.
- 77 motion/design skills are name-only (Claude skillOverrides) and implicit-off (Codex): invoke by /name or $name, name them in the brief under "Skills to use".
- Image creation/editing: Codex $imagegen (gpt-image-2). canvas-design only for static art/posters.
- Workers: Maestro names skills in the brief; workers do not browse this catalog. Workers do not use handoff/claude-handoff skills; they update HANDOFF.md.
- Methodology: Ponytail full + Caveman concise chat; code, docs and commits stay in normal wording.
- Always-on listing cost ~8.2k tok (skill-doctor, upper bound). Cloud on-demand adds: azure ~6.3k, dotnet core ~11.1k, n8n ~4.0k, gcp ~0.8k.
