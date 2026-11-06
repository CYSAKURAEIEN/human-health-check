#!/usr/bin/env python3
"""重新生成根 README.md 里的"示意图目录"一节。

用法(在仓库根目录): python3 tools/build_figure_index.py
按部分、章节列出 docs/images/ 里每张示意图,图名取自 SVG 的 <title>,
链接指向图所在的小节。新增、删除示意图或改动图所在小节的标题后运行一次;
只改 README 里 START 和 END 两行注释之间的内容,不要手工编辑那一段。
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, 'README.md')
START = '<!-- 示意图目录开始: 由 tools/build_figure_index.py 生成,不要手工编辑 -->'
END = '<!-- 示意图目录结束 -->'
IMG = re.compile(r'!\[[^\]]*\]\(\.\./images/([^)\s]+\.svg)\)')


def slug(h):
    h = h.strip().lower()
    h = re.sub(r'[^\w\- 一-鿿]', '', h)
    return h.replace(' ', '-')


def svg_title(name):
    s = open(os.path.join(ROOT, 'docs', 'images', name), encoding='utf-8').read()
    m = re.search(r'<title>(.*?)</title>', s, re.S)
    return re.sub(r'\s+', ' ', m.group(1)).strip() if m else name[:-4]


def figures(path):
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
            out.append((svg_title(name), anchor, name))
    return title or os.path.basename(path)[:-3], out


def build():
    readme = open(README, encoding='utf-8').read()
    parts = dict((d, t) for t, d in re.findall(r'^### \[([^\]]+)\]\(docs/([^/)]+)/README\.md\)', readme, re.M))
    lines, total, names = [], 0, set()
    for part in sorted(os.listdir(os.path.join(ROOT, 'docs'))):
        d = os.path.join('docs', part)
        if part not in parts:
            continue
        rows = []
        for f in sorted(os.listdir(os.path.join(ROOT, d))):
            if not f.endswith('.md') or f == 'README.md':
                continue
            path = f'{d}/{f}'
            title, figs = figures(path)
            if not figs:
                continue
            total += len(figs)
            names.update(f for _, _, f in figs)
            links = ' · '.join(f'[{n}]({path}#{a})' if a else f'[{n}]({path})' for n, a, _ in figs)
            rows.append(f'- **[{title}]({path})**: {links}')
        if rows:
            lines += [f'### {parts[part]}', '', *rows, '']
    head = [START, '', f'全书共 {len(names)} 张示意图({total} 处,有的图在相关的两章里都出现),按部分和章节排列;点击图名跳到图所在的小节。', '']
    return head + lines + [END]


def updated(readme):
    """返回替换了示意图目录一节后的 README 全文(check_docs.py 也用它检查目录是否最新)。"""
    if START not in readme or END not in readme:
        raise SystemExit('README.md 里找不到示意图目录的开始/结束标记')
    pre, rest = readme.split(START, 1)
    _, post = rest.split(END, 1)
    return pre + '\n'.join(build()) + post


def main():
    readme = open(README, encoding='utf-8').read()
    new = updated(readme)
    if new != readme:
        open(README, 'w', encoding='utf-8').write(new)
    print('示意图目录已更新' if new != readme else '示意图目录无变化')


if __name__ == '__main__':
    main()
