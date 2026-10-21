# Methodology and orchestration
name | source | use when | do NOT use when | conflict/preference
Source codes and global choice rules: see ../CATALOG.md

cavecrew | CV | caveman subagent crew | - | -
caveman | CV | terse chat replies (default mode) | code/docs/commits (normal wording required) | -
caveman-commit | CV | terse commit msg | - | caveman-commit: ONLY if commit msg stays pt-BR Conventional (Maestro rule wins)
caveman-compress | CV | compress prose/memory files | - | -
caveman-discover | CV | find caveman opportunities | - | -
caveman-evidence-review | CV | review claims vs evidence tersely | - | -
caveman-explore | CV | terse codebase exploration | - | -
caveman-help | CV | how caveman works | - | -
caveman-learn | CV | learn from session into rules | - | -
caveman-manage | CV | manage caveman config | - | -
caveman-optimize | CV | optimize token usage | - | -
caveman-review | CV | terse code review | - | -
caveman-setup | CV | configure caveman | - | -
caveman-stats | CV | token savings stats | - | -
investigate-first | CV | look before editing | - | -
lean-build | CV | minimal build steps | - | -
megacave | CV | extreme terse mode | code/docs/commits (normal wording required) | -
migration | CV | migration checklist, terse | - | -
safe-refactor | CV | refactor with safety checks | - | -
surgical-patch | CV | minimal diff fix | - | -
ultracave | CV | very terse mode | code/docs/commits (normal wording required) | -
verify-and-stop | CV | verify then stop, no extras | - | -
maestri | Maestri | Send messages to connected AI agents on the Maestri canvas a… | outside a Maestri workspace | Maestro-only unless brief says otherwise
maestri-chat | Maestri | Applies only to messages carrying a Maestri Chat header, eve… | outside a Maestri workspace | Maestro-only unless brief says otherwise
maestri-manager | Maestri | Create and connect agent terminals on the Maestri canvas, ma… | outside a Maestri workspace | Maestro-only unless brief says otherwise
maestri-portal | Maestri | Use a browser portal on the Maestri canvas to navigate the w… | outside a Maestri workspace | Maestro-only unless brief says otherwise
maestri-portal-devices | Maestri | Drive an iOS simulator, Android emulator, or physical Androi… | outside a Maestri workspace | Maestro-only unless brief says otherwise
maestri-routines | Maestri | Manage scheduled routines on the Maestri canvas (recurring c… | outside a Maestri workspace | Maestro-only unless brief says otherwise
maestri-workspace | Maestri | Create new Maestri workspaces and floors from the command li… | outside a Maestri workspace | Maestro-only unless brief says otherwise
oc-blackbox | Overclock | Find the root cause before proposing any fix: read the error… | plain Maestri missions | prefer SP/MP equivalents; use only if brief names it
oc-builder | Overclock | Executor role for an Overclock worker pane: take one concret… | plain Maestri missions | prefer SP/MP equivalents; use only if brief names it
oc-conveyor | Overclock | Reviewer role for an Overclock worker pane: audit a diff or… | plain Maestri missions | prefer SP/MP equivalents; use only if brief names it
oc-copywriting | Overclock | Write the words for a deliverable — the offer AND the struct… | plain Maestri missions | prefer SP/MP equivalents; use only if brief names it
oc-guide | Overclock | What Overclock is and how to use all of it, explained to the… | plain Maestri missions | prefer SP/MP equivalents; use only if brief names it
oc-mcp | Overclock | How to act on Overclock through its MCP (the `overclock` ser… | plain Maestri missions | prefer SP/MP equivalents; use only if brief names it
oc-pilot | Overclock | Pilot role for an Overclock mission: think the activities an… | plain Maestri missions | prefer SP/MP equivalents; use only if brief names it
oc-route | Overclock | Write an implementation plan from a spec or requirements bef… | plain Maestri missions | prefer SP/MP equivalents; use only if brief names it
oc-scout | Overclock | Researcher role for an Overclock worker pane: investigate th… | plain Maestri missions | prefer SP/MP equivalents; use only if brief names it
oc-showcase | Overclock | UI/UX rules for building, reviewing or fixing product interf… | plain Maestri missions | prefer SP/MP equivalents; use only if brief names it
oc-stamp | Overclock | Evidence before any claim of done, fixed, passing or shipped… | plain Maestri missions | prefer SP/MP equivalents; use only if brief names it
ponytail | PT | smallest complete change (full intensity default) | security/a11y/explicit requirements | -
ponytail-audit | PT | find over-engineering in code | - | -
ponytail-debt | PT | list simplification debt | - | -
ponytail-gain | PT | show lines/complexity saved | - | -
ponytail-help | PT | how ponytail works | - | -
ponytail-review | PT | review a diff for needless code | - | -
qa-fix-protocol | QA lab | Protocolo do resolvedor de QA — poll no contrato TASK/items/… | plain Maestri missions | prefer SP/MP equivalents; use only if brief names it
brainstorming | SP | design/spec before building new features | trivial edits (L0) | PREFERRED over oc-route for planning (Maestro only; workers skip gates)
diagnosing-superpowers | SP | debug why Superpowers skills misfire | - | -
dispatching-parallel-agents | SP | 2+ independent tasks, disjoint files | - | -
executing-plans | SP | run a written plan task by task | no plan exists | -
finishing-a-development-branch | SP | wrap up a branch (tests, merge/PR options) | workers (git write is Maestro-only) | -
receiving-code-review | SP | act on review feedback with verification | - | -
requesting-code-review | SP | ask for review after a task/feature | - | review itself: mattpocock code-review
subagent-driven-development | SP | execute plan via fresh subagent per task | Maestri workers (use Maestro waves) | -
systematic-debugging | SP | any bug/failing test: root cause first | - | PREFERRED for debugging
test-driven-development | SP | new feature/bugfix, test first | - | PREFERRED for TDD
using-git-worktrees | SP | isolate work in a git worktree | Maestri floors do this; workers never run git write | -
using-superpowers | SP | bootstrap: how to find/use skills | - | -
verification-before-completion | SP | before claiming done/fixed/passing | - | PREFERRED over oc-stamp
writing-plans | SP | spec ready, need a step-by-step plan | - | PREFERRED for plans
writing-skills | SP | author/test new skills | - | -
skill-creator | claude-plugins-official | create/improve/measure skills | routine tasks | -
