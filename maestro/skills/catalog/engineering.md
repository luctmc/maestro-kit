# Engineering
name | source | use when | do NOT use when | conflict/preference
Source codes and global choice rules: see ../CATALOG.md

ask-matt | MP | Ask which skill or flow fits your situation | - | -
chief-of-staff | MP | Pursue a long-running goal in a single session by… | in-progress/deprecated set: experimental | -
claude-handoff | MP | Hand the current conversation off to a fresh backg… | in-progress/deprecated set: experimental | not for workers (HANDOFF.md)
code-review | MP | Review the changes since a fixed point (commit, br… | - | PREFERRED for code review (Maestro rule); overlaps native /code-review + code-review plugin
codebase-design | MP | Shared vocabulary for designing deep modules | - | -
diagnosing-bugs | MP | Diagnosis loop for hard bugs and performance regre… | - | prefer SP systematic-debugging
domain-modeling | MP | Build and sharpen a project's domain model | - | -
git-guardrails-claude-code | MP | Set up Claude Code hooks to block dangerous git co… | - | -
grill-me | MP | A relentless interview to sharpen a plan or design… | - | dup of grilling; pick one
grill-with-docs | MP | A relentless interview to sharpen a plan or design… | - | overlaps grilling
grilling | MP | Grill the user relentlessly about a plan, decision… | - | -
handoff | MP | Compact the current conversation into a handoff do… | - | do NOT use for workers: use HANDOFF.md
implement | MP | Implement a piece of work based on a spec or set o… | - | prefer Maestro delegation
implement-spec | MP | Implement the result of /to-spec and /to-tickets i… | - | -
improve-codebase-architecture | MP | Scan a codebase for deepening opportunities, prese… | - | -
loop-me | MP | Grill me about specs for the workflows I want to b… | in-progress/deprecated set: experimental | -
migrate-to-shoehorn | MP | Migrate test files from `as` type assertions to @t… | - | -
pr | MP | Use when writing a PR body. | - | -
prototype | MP | Build a throwaway prototype to answer a design que… | - | overlaps EK prototype (UI); use EK for UI
research | MP | Investigate a question against high-trust primary… | - | -
retro | MP | Conduct a retrospective on a coding session. | - | -
scaffold-exercises | MP | Create exercise directory structures with sections… | - | -
setup-matt-pocock-skills | MP | Configure this repo for the engineering skills: se… | - | -
setup-pre-commit | MP | Set up Husky pre-commit hooks with lint-staged (Pr… | - | -
setup-ts-deep-modules | MP | Wire dependency-cruiser into a TypeScript repo so… | in-progress/deprecated set: experimental | -
tdd | MP | Test-driven development | - | prefer SP test-driven-development
teach | MP | Teach the user a new skill or concept, within this… | - | -
to-questionnaire | MP | Turn a decision you can't fully answer into a ques… | - | -
to-spec | MP | Turn the current conversation into a spec and publ… | - | -
to-tickets | MP | Break a plan, spec, or the current conversation in… | - | -
triage | MP | Move issues and external PRs through a state machi… | - | -
wait-what | MP | Stop | - | -
wayfinder | MP | Plan a huge chunk of work (more than one agent ses… | - | -
wizard | MP | Generate an interactive bash wizard that walks a h… | - | -
writing-beats | MP | Writing, exploit; assemble raw material into a jou… | in-progress/deprecated set: experimental | -
writing-for-agents | MP | Writing documents for agents | - | -
writing-fragments | MP | Writing, explore: mine raw fragments, no structure… | in-progress/deprecated set: experimental | -
writing-shape | MP | Writing, exploit: shape raw material into an artic… | in-progress/deprecated set: experimental | -
csharp-lsp | claude-plugins-official (LSP) | C# code intelligence | binary not installed yet -> inert | -
pyright-lsp | claude-plugins-official (LSP) | Python type checking | binary not installed yet -> inert | -
typescript-lsp | claude-plugins-official (LSP) | TS/JS code intelligence | binary not installed yet -> inert | -
code-review | claude-plugins-official/code-review | automated PR review with agents | duplicate-name risk with native/MP | PR multi-agent review; MP code-review preferred
