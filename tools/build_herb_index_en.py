#!/usr/bin/env python3
"""由中文药名索引生成英文版 en/docs/10-chinese-medicinal-herbs/10-herb-name-index.md。

用法(在仓库根目录): python3 tools/build_herb_index_en.py
依赖: pypinyin。先运行 tools/build_herb_index.py 生成中文索引,再运行本脚本。
英文条目名取自英文各章的"### N.N Pinyin (English)"标题,锚点按标题位置对应(见 tools/en_links.py);
别名转成不带声调的拼音,后面保留汉字。英文章节还没有时,条目链接到中文原文。
"""
import os, re, sys

from pypinyin import lazy_pinyin

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.dont_write_bytecode = True
import en_links  # noqa: E402

ZH_DIR = 'docs/10-中药材识别与采集'
ZH = f'{ZH_DIR}/10-药名索引.md'
EN_DIR = 'en/docs/10-chinese-medicinal-herbs'
EN = f'{EN_DIR}/10-herb-name-index.md'
HEAD = '''# Herb Name Index

> Don't know which chapter a herb is in? Look it up by the first letter of its Pinyin name; common alternative names are included.

## ⚠️ How to use

- Names in **bold** are the main entries in the chapters; click to go straight to the entry. `Alternative name → main name` means the name is an alternative; click to go to the main entry
- Herbs marked ☠️ are in the [Toxic Herbs and Poisonous Look-alikes](09-toxic-herbs-and-poisonous-look-alikes.md) chapter, which covers **identification and poisoning signs only: never collect or use them yourself**
- The same alternative name can mean different herbs in different places (for example "Shashen" can mean Beishashen or Nanshashen); go by the source species given in the entry
- Names are sorted by Pinyin; characters with more than one reading follow the usual herb-trade reading (e.g. 射干 is Shegan)
- This index is generated from the chapter headings and the "main name (alternative names)" lines by `tools/build_herb_index_en.py`; do not edit it by hand

'''
TAIL = '''## Related chapters

- ⏮️ [Toxic Herbs and Poisonous Look-alikes](09-toxic-herbs-and-poisonous-look-alikes.md) - highly toxic herbs and poisonous look-alike plants
- 🔗 [General Principles of Identifying and Collecting Chinese Medicinal Herbs](00-general-principles.md) - general methods for identification, harvesting, processing and storage
- 🔗 [Contents of this part](README.md)

---

**If you can't name a plant, don't pick it; if a herb doesn't match its entry, don't use it.**
'''


def pinyin(s):
    return ''.join(lazy_pinyin(s)).capitalize()


class Target:
    """中文链接 file.md#anchor → (英文相对链接, 英文条目名, 英文章名)。"""

    def __init__(self):
        self.zh2en = en_links.load_paths()
        self.cache = {}

    def chapter(self, zh_file):
        if zh_file not in self.cache:
            zh = f'{ZH_DIR}/{zh_file}'
            en = self.zh2en[zh]
            ok = os.path.isfile(os.path.join(ROOT, en))
            info = {'ok': ok, 'en': en, 'zh': zh}
            if ok:
                lines = open(os.path.join(ROOT, en), encoding='utf-8').read().split('\n')
                info['title'] = next(l[2:].strip() for l in lines if l.startswith('# '))
                info['zh_slugs'] = [s for _, s in en_links.headings(zh)]
                info['en_slugs'] = [s for _, s in en_links.headings(en)]
                fence, texts = False, []
                for l in lines:
                    if l.startswith('```'):
                        fence = not fence
                        continue
                    m = None if fence else re.match(r'#{1,6} (.*)', l)
                    if m:
                        texts.append(m.group(1).strip())
                info['texts'] = texts
            self.cache[zh_file] = info
        return self.cache[zh_file]

    def resolve(self, zh_file, anchor, zh_name):
        c = self.chapter(zh_file)
        if not c['ok'] or len(c['zh_slugs']) != len(c['en_slugs']) or anchor not in c['zh_slugs']:
            return f'../../../{c["zh"]}#{anchor}', f'{pinyin(zh_name)}', None
        k = c['zh_slugs'].index(anchor)
        name = re.sub(r'^[\d.]+\s+', '', c['texts'][k]).replace('*', '')
        if re.search(r' vs | and |, ', name):  # 一个标题讲几味药(如"钩吻与金银花"): 只取这味药
            py = pinyin(zh_name)
            m = re.search(rf"(?<![\w']){re.escape(py)} \([^()]*(?:\([^()]*\)[^()]*)*\)", name, re.I)
            name = m.group(0) if m and not re.search(r' and |, ', m.group(0)) else py
        return f'{os.path.basename(c["en"])}#{c["en_slugs"][k]}', name, c['title']


def build():
    t = Target()
    out, body = [HEAD], False
    for line in open(os.path.join(ROOT, ZH), encoding='utf-8').read().split('\n'):
        if line.startswith('[A](#a)'):
            out.append(line + '\n')
            body = True
            continue
        if not body:
            continue
        if line.startswith('## 相关章节'):
            break
        if line.startswith('## '):
            out.append(line + '\n')
            continue
        m = re.match(r'- \*\*\[(.+?)\]\(([^)#]+)#([^)]+)\)\*\*( ☠️)? · .*', line)
        if m:
            link, name, title = t.resolve(m.group(2), m.group(3), m.group(1))
            out.append(f'- **[{name}]({link})** ({m.group(1)}){m.group(4) or ""}'
                       + (f' · {title}' if title else '') + '\n')
            continue
        m = re.match(r'- (.+?) → \[(.+?)\]\(([^)#]+)#([^)]+)\)', line)
        if m:
            link, name, _ = t.resolve(m.group(3), m.group(4), m.group(2))
            out.append(f'- {pinyin(m.group(1))} ({m.group(1)}) → [{name}]({link})\n')
            continue
        out.append(line + '\n' if line else '\n')
    text = ''.join(out).rstrip('\n') + '\n\n' + TAIL
    return re.sub(r'\n{3,}', '\n\n', text)


def main():
    new = build()
    path = os.path.join(ROOT, EN)
    old = open(path, encoding='utf-8').read() if os.path.isfile(path) else None
    if new != old:
        open(path, 'w', encoding='utf-8').write(new)
    print(EN, '已更新' if new != old else '无变化')


if __name__ == '__main__':
    main()
