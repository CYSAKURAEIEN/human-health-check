#!/usr/bin/env python3
"""英文版(en/)的链接维护和结构检查。

用法(在仓库根目录): python3 tools/en_links.py
- 英文版里指向中文原文的链接,如果那一章已经有英文版,就改成指向英文版,
  锚点按标题的先后位置对应(英文版的标题必须和原文一一对应: 数量、级别、顺序都相同)
- 列出标题结构和原文对不上的英文章节
中文路径和英文路径的对应关系见 en/paths.tsv。check_docs.py 用这里的函数检查英文版。
"""
import os, re, sys, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r'(\]\()([^)\s]+)(\))')


def slug(h):
    h = h.strip().lower()
    h = re.sub(r'[^\w\- 一-鿿]', '', h)
    return h.replace(' ', '-')


def load_paths():
    zh2en = {}
    for line in open(os.path.join(ROOT, 'en', 'paths.tsv'), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        zh, en = line.rstrip('\n').split('\t')
        zh2en[zh] = en
    return zh2en


def headings(path):
    """[(级别, 锚点)],锚点按 GitHub 规则,重名加 -1、-2。"""
    out, seen, fence = [], {}, False
    for line in open(os.path.join(ROOT, path), encoding='utf-8').read().split('\n'):
        if line.startswith('```'):
            fence = not fence
            continue
        m = None if fence else re.match(r'(#{1,6}) (.*)', line)
        if m:
            s = slug(m.group(2))
            if s in seen:
                seen[s] += 1
                s = f'{s}-{seen[s]}'
            else:
                seen[s] = 0
            out.append((len(m.group(1)), s))
    return out


def structure_problems(zh2en):
    """英文版标题的数量、级别、顺序和原文不同的章节。"""
    errs = []
    for zh, en in zh2en.items():
        if not os.path.isfile(os.path.join(ROOT, en)):
            continue
        a, b = [l for l, _ in headings(zh)], [l for l, _ in headings(en)]
        if a != b:
            i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
            errs.append(f'{en}: 标题结构和原文 {zh} 不一致(原文 {len(a)} 个标题,英文版 {len(b)} 个;第 {i + 1} 个开始不同)')
    return errs


def rewrite(en_path, zh2en):
    """把指向已有英文版的中文链接改成英文链接;返回 (新文本, 无法对应的锚点列表)。"""
    text = open(os.path.join(ROOT, en_path), encoding='utf-8').read()
    base = os.path.dirname(en_path)
    problems = []

    def fix(m):
        target = m.group(2)
        if re.match(r'^[a-z]+:', target) or target.startswith('#'):
            return m.group(0)
        path, _, frag = target.partition('#')
        full = os.path.normpath(os.path.join(base, urllib.parse.unquote(path)))
        if os.path.isdir(os.path.join(ROOT, full)):
            full = os.path.join(full, 'README.md')
        en = zh2en.get(full)
        if not en or not os.path.isfile(os.path.join(ROOT, en)):
            return m.group(0)
        new_frag = ''
        if frag:
            zh_slugs = [s for _, s in headings(full)]
            en_slugs = [s for _, s in headings(en)]
            k = zh_slugs.index(urllib.parse.unquote(frag)) if urllib.parse.unquote(frag) in zh_slugs else -1
            if 0 <= k < len(en_slugs) and len(zh_slugs) == len(en_slugs):
                new_frag = '#' + en_slugs[k]
            else:
                problems.append(f'{en_path}: 找不到原文锚点 {target} 对应的英文标题')
                return m.group(0)
        return m.group(1) + os.path.relpath(en, base) + new_frag + m.group(3)

    out, fence = [], False
    for line in text.split('\n'):
        if line.startswith('```'):
            fence = not fence
        out.append(line if fence else LINK.sub(fix, line))
    return '\n'.join(out), problems


def en_files():
    for d, _, fs in os.walk(os.path.join(ROOT, 'en')):
        for f in sorted(fs):
            if f.endswith('.md'):
                yield os.path.relpath(os.path.join(d, f), ROOT)


def stale_links(zh2en):
    """check_docs.py 用: 还指向中文原文、但其实已有英文版的链接。"""
    errs = []
    for p in en_files():
        new, problems = rewrite(p, zh2en)
        if new != open(os.path.join(ROOT, p), encoding='utf-8').read():
            errs.append(f'{p}: 有指向中文原文的链接已有英文版可指: 请运行 python3 tools/en_links.py')
        errs += problems
    return errs


def main():
    zh2en = load_paths()
    changed = 0
    for p in en_files():
        new, problems = rewrite(p, zh2en)
        for e in problems:
            print(e)
        if new != open(os.path.join(ROOT, p), encoding='utf-8').read():
            open(os.path.join(ROOT, p), 'w', encoding='utf-8').write(new)
            changed += 1
    for e in structure_problems(zh2en):
        print(e)
    print(f'改写了 {changed} 个英文文件的链接')


if __name__ == '__main__':
    sys.exit(main())
