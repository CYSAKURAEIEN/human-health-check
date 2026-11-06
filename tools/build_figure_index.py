#!/usr/bin/env python3
"""重新生成根 README.md(和英文版 en/README.md)里的"示意图目录"一节。

用法(在仓库根目录): python3 tools/build_figure_index.py
按部分、章节列出每张示意图,图名取自 SVG 的 <title>,链接指向图所在的小节。
英文版用 en/ 下已译好的章节和 en/images/ 的英文图;还没译的章节列中文原文。
新增、删除示意图或改动图所在小节的标题后运行一次;
只改 README 里 START 和 END 两行注释之间的内容,不要手工编辑那一段。
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, 'README.md')
EN_README = os.path.join(ROOT, 'en', 'README.md')
START = '<!-- 示意图目录开始: 由 tools/build_figure_index.py 生成,不要手工编辑 -->'
END = '<!-- 示意图目录结束 -->'
IMG = re.compile(r'!\[[^\]]*\]\((?:\.\./)+(?:docs/)?images/([^)\s]+\.svg)\)')


def slug(h):
    h = h.strip().lower()
    h = re.sub(r'[^\w\- 一-鿿]', '', h)
    return h.replace(' ', '-')


def svg_title(name, en=False):
    p = os.path.join(ROOT, 'en', 'images', name)
    if not (en and os.path.isfile(p)):
        p = os.path.join(ROOT, 'docs', 'images', name)
    s = open(p, encoding='utf-8').read()
    m = re.search(r'<title>(.*?)</title>', s, re.S)
    return re.sub(r'\s+', ' ', m.group(1)).strip() if m else name[:-4]


def figures(path, en=False):
    """返回 (章节标题, [(图名, 锚点, 文件名)]),锚点是图前面最近的标题(GitHub 规则,重名加 -1、-2)。"""
    title, anchor, seen, out, fence = None, '', {}, [], False
    for line in open(os.path.join(ROOT, path), encoding='utf-8').read().split('\n'):
        if line.startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        m = re.match(r'(#{1,6}) (.*)', line)
        if m:
            s = slug(m.group(2))
            if s in seen:
                seen[s] += 1
                s = f'{s}-{seen[s]}'
            else:
                seen[s] = 0
            if title is None and m.group(1) == '#':
                title = m.group(2).strip()
            else:
                anchor = s
            continue
        for name in IMG.findall(line):
            out.append((svg_title(name, en), anchor, name))
    return title or os.path.basename(path)[:-3], out


def en_paths():
    out = {}
    for line in open(os.path.join(ROOT, 'en', 'paths.tsv'), encoding='utf-8'):
        if not line.startswith('#') and line.strip():
            zh, en = line.rstrip('\n').split('\t')
            out[zh] = en
    return out


def build(readme, en=False):
    """en=True 时生成英文版目录: 链接相对 en/README.md,已译的章节用英文版。"""
    parts = dict((d.split('/')[-1], t) for t, d in
                 re.findall(r'^### \[([^\]]+)\]\(((?:\.\./)?docs/[^/)]+)/README\.md\)', readme, re.M))
    zh2en = en_paths() if en else {}
    en_parts = {zh.split('/')[1]: e.split('/')[2] for zh, e in zh2en.items() if zh.startswith('docs/')}
    lines, total, names = [], 0, set()
    for part in sorted(os.listdir(os.path.join(ROOT, 'docs'))):
        d = os.path.join('docs', part)
        key = next((k for k in (en_parts.get(part), part) if k in parts), None)  # 英文版里还没译的部分链接中文原文
        if key is None:
            continue
        rows = []
        for f in sorted(os.listdir(os.path.join(ROOT, d))):
            if not f.endswith('.md') or f == 'README.md':
                continue
            zh = f'{d}/{f}'
            path, link = zh, zh
            if en:
                e = zh2en.get(zh)
                if e and os.path.isfile(os.path.join(ROOT, e)):
                    path, link = e, e[len('en/'):]
                else:
                    link = '../' + zh
            title, figs = figures(path, en)
            if not figs:
                continue
            total += len(figs)
            names.update(f for _, _, f in figs)
            links = ' · '.join(f'[{n}]({link}#{a})' if a else f'[{n}]({link})' for n, a, _ in figs)
            rows.append(f'- **[{title}]({link})**: {links}')
        if rows:
            lines += [f'### {parts[key]}', '', *rows, '']
    if en:
        intro = (f'{len(names)} diagrams in all ({total} placements; a few appear in two related chapters), '
                 'listed by part and chapter; click a name to jump to the section it is in. '
                 'Chapters not yet translated are listed in Chinese.')
    else:
        intro = f'全书共 {len(names)} 张示意图({total} 处,有的图在相关的两章里都出现),按部分和章节排列;点击图名跳到图所在的小节。'
    return [START, '', intro, ''] + lines + [END]


def updated(readme, en=False):
    """返回替换了示意图目录一节后的 README 全文(check_docs.py 也用它检查目录是否最新)。"""
    if START not in readme or END not in readme:
        raise SystemExit('README 里找不到示意图目录的开始/结束标记')
    pre, rest = readme.split(START, 1)
    _, post = rest.split(END, 1)
    return pre + '\n'.join(build(readme, en)) + post


def main():
    for path, en in ((README, False), (EN_README, True)):
        if not os.path.isfile(path):
            continue
        readme = open(path, encoding='utf-8').read()
        new = updated(readme, en)
        if new != readme:
            open(path, 'w', encoding='utf-8').write(new)
        print(os.path.relpath(path, ROOT), '示意图目录已更新' if new != readme else '示意图目录无变化')


if __name__ == '__main__':
    main()
