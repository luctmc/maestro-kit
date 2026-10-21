import os, re, glob, json
H = os.path.expanduser('~')
AG = H + '/.agents/skills'
PC = H + '/.claude/plugins/cache'
step3 = set(json.load(open(H + '/.maestro/step3-skills.json')))

def fm(path):
    s = open(path, errors='ignore').read()
    m = re.match(r'---\n(.*?)\n---', s, re.S)
    b = m.group(1) if m else ''
    n = re.search(r'^name:\s*(.+)$', b, re.M)
    d = re.search(r'^description:\s*(>[-|]?\s*\n(?:[ \t]+.*\n?)+|.+)$', b, re.M)
    desc = re.sub(r'\s+', ' ', d.group(1).lstrip('>|- \n')).strip().strip('"') if d else ''
    return (n.group(1).strip().strip('"\'') if n else os.path.basename(os.path.dirname(path))), desc

def use(desc, n=70):
    d = re.sub(r'^This skill should be used when the user asks (anything about |to )?', '', desc)
    q = re.findall(r'"([^"]{3,40})"', desc)
    if len(q) >= 2 and 'should be used' in desc:
        d = '; '.join(q[:2])
    d = re.split(r'(?<=[a-z\)])\. ', d)[0]
    d = d.replace('|', '/')
    return (d[:n].rstrip(' ,;') + ('…' if len(d) > n else ''))

# category -> list of (name, source, use, not, pref)
cats = {k: [] for k in ['methodology', 'engineering', 'cloud', 'motion', 'design', 'images']}
def add(cat, name, src, desc, nots='-', pref='-', usetxt=None, n=70):
    cats[cat].append((name, src, usetxt or use(desc, n), nots, pref))

def scan(root, pat):
    for p in sorted(glob.glob(root + pat)):
        yield os.path.basename(os.path.dirname(p)), fm(p)[1], p

# lock sources for global skills
lock = json.load(open(H + '/.agents/.skill-lock.json')); lk = lock.get('skills', lock)
def gsrc(name):
    v = lk.get(name, {}); s = v.get('source', '') if isinstance(v, dict) else ''
    return {'emilkowalski/skills': 'EK', 'remotion-dev/skills': 'RM', 'vibe-motion/skills': 'VM', 'anthropics/skills': 'AN',
            'Barty-Bart/motion-graphics': 'MB', 'oil-oil/oil-motion': 'oil', 'echris6/motion-video-kit': 'echris6'}.get(s, 'IA/' + s.split('/')[-1].replace('-skills', '') if s.startswith('iart-ai') else (s or 'local'))

# ---------------- methodology ----------------
SP = {'brainstorming': 'design/spec before building new features', 'diagnosing-superpowers': 'debug why Superpowers skills misfire',
 'dispatching-parallel-agents': '2+ independent tasks, disjoint files', 'executing-plans': 'run a written plan task by task',
 'finishing-a-development-branch': 'wrap up a branch (tests, merge/PR options)', 'receiving-code-review': 'act on review feedback with verification',
 'requesting-code-review': 'ask for review after a task/feature', 'subagent-driven-development': 'execute plan via fresh subagent per task',
 'systematic-debugging': 'any bug/failing test: root cause first', 'test-driven-development': 'new feature/bugfix, test first',
 'using-git-worktrees': 'isolate work in a git worktree', 'using-superpowers': 'bootstrap: how to find/use skills',
 'verification-before-completion': 'before claiming done/fixed/passing', 'writing-plans': 'spec ready, need a step-by-step plan', 'writing-skills': 'author/test new skills'}
SPN = {'brainstorming': 'trivial edits (L0)', 'executing-plans': 'no plan exists', 'subagent-driven-development': 'Maestri workers (use Maestro waves)',
 'using-git-worktrees': 'Maestri floors do this; workers never run git write', 'finishing-a-development-branch': 'workers (git write is Maestro-only)'}
SPP = {'systematic-debugging': 'PREFERRED for debugging', 'test-driven-development': 'PREFERRED for TDD', 'brainstorming': 'PREFERRED over oc-route for planning (Maestro only; workers skip gates)',
 'writing-plans': 'PREFERRED for plans', 'verification-before-completion': 'PREFERRED over oc-stamp', 'requesting-code-review': 'review itself: mattpocock code-review'}
for n in SP: add('methodology', n, 'SP', '', SPN.get(n, '-'), SPP.get(n, '-'), SP[n])
PT = {'ponytail': 'smallest complete change (full intensity default)', 'ponytail-audit': 'find over-engineering in code', 'ponytail-debt': 'list simplification debt',
 'ponytail-gain': 'show lines/complexity saved', 'ponytail-help': 'how ponytail works', 'ponytail-review': 'review a diff for needless code'}
for n in PT: add('methodology', n, 'PT', '', 'security/a11y/explicit requirements' if n == 'ponytail' else '-', '-', PT[n])
CV = {'caveman': 'terse chat replies (default mode)', 'cavecrew': 'caveman subagent crew', 'caveman-commit': 'terse commit msg', 'caveman-compress': 'compress prose/memory files',
 'caveman-discover': 'find caveman opportunities', 'caveman-evidence-review': 'review claims vs evidence tersely', 'caveman-explore': 'terse codebase exploration',
 'caveman-help': 'how caveman works', 'caveman-learn': 'learn from session into rules', 'caveman-manage': 'manage caveman config', 'caveman-optimize': 'optimize token usage',
 'caveman-review': 'terse code review', 'caveman-setup': 'configure caveman', 'caveman-stats': 'token savings stats', 'investigate-first': 'look before editing',
 'lean-build': 'minimal build steps', 'megacave': 'extreme terse mode', 'migration': 'migration checklist, terse', 'safe-refactor': 'refactor with safety checks',
 'surgical-patch': 'minimal diff fix', 'ultracave': 'very terse mode', 'verify-and-stop': 'verify then stop, no extras'}
for n in CV:
    nots = 'code/docs/commits (normal wording required)' if n in ('caveman', 'ultracave', 'megacave') else '-'
    pref = 'caveman-commit: ONLY if commit msg stays pt-BR Conventional (Maestro rule wins)' if n == 'caveman-commit' else '-'
    add('methodology', n, 'CV', '', nots, pref, CV[n])
add('methodology', 'skill-creator', 'claude-plugins-official', '', 'routine tasks', '-', 'create/improve/measure skills')

for n, d, p in scan(AG, '/*/SKILL.md'):
    if n in step3: continue
    if n.startswith('maestri'):
        add('methodology', n, 'Maestri', d, 'outside a Maestri workspace', 'Maestro-only unless brief says otherwise', n=60)
    elif n.startswith('oc-') or n == 'qa-fix-protocol':
        add('methodology', n, 'Overclock' if n.startswith('oc-') else 'QA lab', d, 'plain Maestri missions', 'prefer SP/MP equivalents; use only if brief names it', n=60)

# ---------------- engineering ----------------
MP = {}
for n, d, p in scan(PC + '/mattpocock/mattpocock-skills', '/*/skills/*/*/SKILL.md'):
    MP[n] = d
MPP = {'code-review': 'PREFERRED for code review (Maestro rule); overlaps native /code-review + code-review plugin', 'tdd': 'prefer SP test-driven-development',
 'diagnosing-bugs': 'prefer SP systematic-debugging', 'prototype': 'overlaps EK prototype (UI); use EK for UI', 'handoff': 'do NOT use for workers: use HANDOFF.md',
 'claude-handoff': 'not for workers (HANDOFF.md)', 'implement': 'prefer Maestro delegation', 'grill-me': 'dup of grilling; pick one', 'grill-with-docs': 'overlaps grilling'}
for n in sorted(MP):
    add('engineering', n, 'MP', MP[n], 'in-progress/deprecated set: experimental' if n in ('chief-of-staff', 'claude-handoff', 'loop-me', 'setup-ts-deep-modules', 'writing-beats', 'writing-fragments', 'writing-shape') else '-', MPP.get(n, '-'), n=50)
add('engineering', 'code-review', 'claude-plugins-official/code-review', '', 'duplicate-name risk with native/MP', 'PR multi-agent review; MP code-review preferred', 'automated PR review with agents')
for n, desc in [('typescript-lsp', 'TS/JS code intelligence'), ('csharp-lsp', 'C# code intelligence'), ('pyright-lsp', 'Python type checking')]:
    add('engineering', n, 'claude-plugins-official (LSP)', '', 'binary not installed yet -> inert', '-', desc)

# ---------------- cloud (OFF by default) ----------------
def cloud(plugin_glob, src, nots):
    for n, d, p in scan(PC, plugin_glob):
        add('cloud', n, src, d, nots, '-', n=44)
cloud('/azure-skills/azure/*/skills/*/SKILL.md', 'AZ', 'non-Azure projects')
cloud('/google-plugins/google-cloud-developer/*/skills/*/SKILL.md', 'GC', 'non-GCP; MCP needs API key')
for plug in ['dotnet', 'dotnet-test', 'dotnet-aspnetcore', 'dotnet-diag', 'dotnet-data', 'dotnet-upgrade']:
    cloud(f'/dotnet-agent-skills/{plug}/*/skills/*/SKILL.md', f'DN/{plug}', 'non-.NET projects')
cloud('/n8n-mcp-skills/n8n-mcp-skills/*/skills/*/SKILL.md', 'N8', 'non-n8n; hooks cannot be split')

# ---------------- motion / design / images (standalone global) ----------------
RMN = 'WORK projects: PERSONAL PROJECTS ONLY'
design_names = {'animate', 'animate-expo', 'animation-performance', 'animation-vocabulary', 'apple-design', 'ask-sonner', 'break-ui', 'emil-design-eng',
 'find-animation-opportunities', 'improve-animations', 'mobile-native', 'pick-ui-library', 'prototype', 'review-animations', 'write-swift',
 'frontend-design', 'glassmorphism', 'micro-interaction', 'page-transition-animation', 'accessible-animation', '60fps-animation', 'gsap-web',
 'lottie-animation', 'svg-animation', 'motion-background', 'ascii-animation'}
image_names = {'canvas-design'}
ovr = {
 'animate': (' - ', 'PREFERRED for UI animation (Maestro rule)'), 'review-animations': ('-', 'PREFERRED for motion review'),
 'improve-animations': ('-', 'codebase motion audit'), 'prototype': ('-', 'UI prototypes; overlaps MP prototype'),
 '60fps-animation': ('-', 'overlaps EK animation-performance (prefer EK)'), 'micro-interaction': ('-', 'overlaps EK animate (prefer EK)'),
 'accessible-animation': ('-', 'use alongside EK'), 'frontend-design': ('-', 'PREFERRED for new UI visual direction; AN'),
 'canvas-design': ('code/UI; use for static art/poster', 'for AI image gen use Codex $imagegen (gpt-image-2)'),
 'lower-thirds': ('-', 'ONLY copy kept: from tiktok-video-skills; lower-thirds-skills pack NOT installed (name conflict)'),
 'remotion-video': (RMN, 'IA copy; overlaps RM remotion-best-practices'), 'explainer-default': ('-', 'MB pack; overlaps IA explainer-video'),
 'explainer-engaging': ('-', 'MB pack; overlaps IA explainer-video'), 'explainer-high-energy': ('-', 'MB pack'),
 'sound-effects': ('-', 'audio pass for motion videos'), 'object-separation': ('-', 'video segmentation (SAM 2), local'),
 'reverse-engineer-anything': ('-', 'local skill'),
 'explainer-video': ('-', 'overlaps MB explainer-*; Motion Director chooses'),
 'motion-art-direction': ('-', 'Motion Director: creative judgment layer'),
 'caption-animation': (RMN + ' if Remotion-based', '-'),
}
EXT = {'3d-chladni-render', 'claude-typer', 'fisheye-motion', 'wechat-2d-render', 'procedural-fish-render', 'ruler-progress-render', 'threejs-earth-render'}
for n, d, p in scan(AG, '/*/SKILL.md'):
    if n not in step3 and n not in ('reverse-engineer-anything', 'business-motion-film', 'explainer-default', 'explainer-engaging', 'explainer-high-energy', 'motion-broll', 'object-separation', 'oil-motion', 'sound-effects'):
        continue
    src = gsrc(n); nots, pref = ovr.get(n, ('-', '-'))
    nots = nots.strip()
    if n.startswith('remotion-') and src == 'RM':
        nots, pref = RMN, 'Remotion family; router: remotion-best-practices'
    if src == 'VM' and n.startswith('remotion-'):
        nots, pref = RMN, 'VM variant'
    if n in EXT:
        nots = (nots + '; ' if nots != '-' else '') + 'CLONES/FETCHES external code: needs user OK'
    if src == 'VM' and 'Remotion' in d and RMN not in nots:
        nots = (nots + '; ' if nots != '-' else '') + RMN
    cat = 'images' if n in image_names else ('design' if n in design_names else 'motion')
    nm = 62
    if re.search(r'[一-鿿]', d):
        en = re.split(r'[一-鿿]', d)[0].strip(' .,(')
        d = en if len(en) > 15 else ('(CN skill) ' + n.replace('-', ' '))
    add(cat, n, src, d, nots, pref, n=nm)

titles = {'methodology': 'Methodology and orchestration', 'engineering': 'Engineering', 'cloud': 'Cloud and platform (plugins OFF by default)',
          'motion': 'Motion and video', 'design': 'Design and UI', 'images': 'Images'}
files = {'methodology': 'methodology.md', 'engineering': 'engineering.md', 'cloud': 'cloud.md', 'motion': 'motion.md', 'design': 'design-ui.md', 'images': 'images.md'}
when = {'methodology': 'Superpowers, Ponytail, Caveman, skill-creator, Maestri/Overclock/QA workflow. For process, debugging, planning, verification, orchestration.',
 'engineering': 'mattpocock-skills, code-review, LSP plugins. For coding missions: specs, tickets, TDD, review, architecture.',
 'cloud': 'Azure, Google Cloud, .NET, n8n (plugins OFF). Read ONLY for a matching platform; then enable the plugin and tell the user.',
 'motion': 'Remotion, vibe-motion, iart-ai, explainers, captions, video. For motion/video missions. Remotion = personal projects only.',
 'design': 'Emil Kowalski, frontend-design, UI animation, glass, GSAP, Lottie, SVG. For UI/UX and web-animation missions.',
 'images': 'canvas-design (static art). Image creation/editing itself uses Codex $imagegen.'}
head = open(H + '/.maestro/catalog_rules.md').read()
cd = H + '/.maestro/skills/catalog'
os.makedirs(cd, exist_ok=True)
total = 0
order = ['methodology', 'engineering', 'cloud', 'motion', 'design', 'images']
for k in order:
    out = [f'# {titles[k]}', 'name | source | use when | do NOT use when | conflict/preference', 'Source codes and global choice rules: see ../CATALOG.md', '']
    for name, src, u, nots, pref in sorted(cats[k], key=lambda x: (x[1], x[0])):
        out.append(f'{name} | {src} | {u} | {nots} | {pref}'); total += 1
    open(f'{cd}/{files[k]}', 'w').write('\n'.join(out) + '\n')
idx = [head.rstrip('\n'), '', '## Categories (read this index + ONLY the category file(s) the mission needs)']
for k in order:
    idx.append(f'- {titles[k]} ({len(cats[k])}): ~/.maestro/skills/catalog/{files[k]} - {when[k]}')
idx += ['', '## Who reads what',
        '- Maestro: this index, then only the category file(s) matching the mission (usually methodology + engineering; cloud only for a matching platform).',
        '- Motion Director: this index, motion.md and design-ui.md (images.md if the mission has stills).',
        '- Workers: read nothing here; the Maestro names the skills in the brief.']
open(H + '/.maestro/skills/CATALOG.md', 'w').write('\n'.join(idx) + '\n')
print('entries', total)
