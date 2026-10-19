#!/usr/bin/env python3
"""重新生成 docs/10-中药材识别与采集/10-药名索引.md。

用法(在仓库根目录): python3 tools/build_herb_index.py
依赖: pypinyin(pip install pypinyin)。
索引从各章"### N.N 药名"标题和"- **正名(别名)**:"一行整理而来;
第十部分增删品种或改别名后运行一次。
"""
import re, glob, os, sys
from pypinyin import lazy_pinyin

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'docs', '10-中药材识别与采集')
OUT = os.path.join(D, '10-药名索引.md')
HEAD = '# 药名索引\n\n> 不知道一味药在哪一章?按药名拼音首字母查,常见别名也收在里面。\n\n## ⚠️ 使用说明\n\n- **粗体**是各章收录的正名,点击直接跳到条目;`别名 → 正名`表示这个名字是别名,点击跳到正名条目\n- 标 ☠️ 的在[有毒中药与易混淆有毒植物](09-有毒中药与易混淆有毒植物.md)一章,**只写识别和中毒表现,不要自采自用**\n- 同一个别名在不同地方可能指不同的药(例如"沙参"可指北沙参或南沙参),以条目里的基原为准\n- 多音字按药材行业的习惯读音排序(如射干 shè gān)\n- 本索引由各章标题和"正名(别名)"一行整理而成;各章增删品种后运行 `tools/build_herb_index.py` 重新生成,不要手工编辑\n\n'
TAIL = '## 相关章节\n\n- ⏮️ [有毒中药与易混淆有毒植物](09-有毒中药与易混淆有毒植物.md) - 剧毒药材和易混淆有毒植物\n- 🔗 [中药材识别与采集总论](00-总论.md) - 识别、采收、加工、储存的通用方法\n- 🔗 [本部分目录](README.md)\n\n---\n\n**叫不出名字的草,不采;对不上条目的药,不用。**\n'
def slug(h):
    h=h.strip().lower(); h=re.sub(r'[^\w\- 一-鿿]','',h); return h.replace(' ','-')
TITLES={}
entries=[]  # (name, file, anchor, chapter, toxic, aliasof)
SKIP=re.compile(r'汇总|自我检查|总览|名单|意味着|为什么|品种与现状|怎样认出|通用提醒|对照总表')
BAD={'开放的花','花蕾','另一味药','见下','乌头类','朴硝精制品'}
HAN=re.compile(r'^[一-鿿]{2,6}$')
for f in sorted(glob.glob(os.path.join(D,'0[1-9]-*.md'))):
    fn=os.path.basename(f); L=open(f).read().split('\n')
    title=L[0].lstrip('# ').strip(); TITLES[fn]=title
    infence=False; cur=None
    for i,line in enumerate(L):
        if line.startswith('```'): infence=not infence; continue
        if infence: continue
        m=re.match(r'### (\d+)\.(\d+) (.+)',line)
        if not m: continue
        sec,head=m.group(1),m.group(3).strip()
        if SKIP.search(head): continue
        anchor=slug(line[4:])
        toxic=fn.startswith('09')
        if toxic and sec not in ('2','3','4'): continue
        h=head
        if toxic:
            if sec=='3' and '细辛' in h: continue  # 细辛 indexed from 04
            h=h.split(' vs ')[0].split(':')[0]
            h=re.sub(r'生食或多食','',h); h=h.replace('苍耳幼苗和苍耳子','苍耳子')
        aliases=[]
        for p in re.findall(r'[((]([^))]*)[))]',h): aliases+=re.split('[、,]',p)
        h=re.sub(r'[((][^))]*[))]','',h)
        names=[n for n in re.split('[、与]',h) if n]
        # aliases from 正名(别名) line
        for j in range(i+1,min(i+6,len(L))):
            mm=re.match(r'- \*\*正名\(别名\)\*\*: (.*)',L[j])
            if mm:
                for p in re.findall(r'[((]([^))]*)[))]',mm.group(1)): aliases+=re.split('[、,;;]',p)
                break
        for n in names:
            entries.append((n.strip(),fn,anchor,toxic,None))
        main=names[0].strip()
        for a in aliases:
            a=a.strip(); a=re.sub(r'^按性状分','',a)
            if a in BAD: continue
            if HAN.match(a) and a not in names: entries.append((a,fn,anchor,toxic,main))
# dedupe: real names win over aliases
seen={}
for e in entries:
    k=e[0]
    if k in seen and seen[k][4] is None: continue
    if k in seen and e[4] is not None: continue
    seen[k]=e
OVR={'射干':'shegan'}
def key(n): return OVR.get(n,''.join(lazy_pinyin(n)))
groups={}
for n,e in sorted(seen.items(),key=lambda kv:key(kv[0])):
    letter=key(n)[0].upper()
    groups.setdefault(letter,[]).append(e)
out=[]
out.append(' | '.join(f'[{g}](#{g.lower()})' for g in sorted(groups)))
out.append('')
for g in sorted(groups):
    out.append(f'## {g}'); out.append('')
    for n,fn,anc,tox,aof in groups[g]:
        mark=' ☠️' if tox else ''
        if aof: out.append(f'- {n} → [{aof}]({fn}#{anc}){mark}')
        else: out.append(f'- **[{n}]({fn}#{anc})**{mark} · {TITLES[fn]}')
    out.append('')

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(HEAD + '\n'.join(out) + '\n' + TAIL)
print(f'{sum(1 for e in seen.values() if e[4] is None)} 味正名, {len(seen)} 个条目 → {OUT}')
