import os,re,sys,glob
# estimate always-on listing cost: tokens ~ chars/4 of "name: description" per skill
def fm(p):
    s=open(p,errors='ignore').read()
    m=re.match(r'---\n(.*?)\n---',s,re.S)
    if not m: return None
    b=m.group(1)
    n=re.search(r'^name:\s*(.+)$',b,re.M)
    d=re.search(r'^description:\s*(>[-|]?\s*\n(?:[ \t]+.*\n?)+|.+)$',b,re.M)
    return (n.group(1).strip() if n else os.path.basename(os.path.dirname(p)), re.sub(r'\s+',' ',d.group(1).lstrip('>|- \n')) if d else '')
root=os.path.expanduser(sys.argv[1] if len(sys.argv)>1 else '~/.agents/skills')
names=set(sys.argv[2:])
tot=cnt=0; tot_name=0
for p in sorted(glob.glob(root+'/*/SKILL.md')):
    r=fm(p)
    if not r: continue
    n,d=r
    if names and os.path.basename(os.path.dirname(p)) not in names: continue
    cnt+=1; tot+=(len(n)+len(d)+4)//4; tot_name+=(len(n)+4)//4
print(f"skills={cnt} full_desc_tokens~{tot} name_only_tokens~{tot_name}")
