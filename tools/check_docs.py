#!/usr/bin/env python3
"""检查全书 Markdown: 断链、锚点、代码块、单位写法、药名索引是否最新。

用法(在仓库根目录): python3 tools/check_docs.py
有问题时逐条列出并以非零状态退出;.github/workflows/check.yml 在每个 PR 上运行它。

检查项:
1. 站内链接指向的文件存在,#锚点与目标文件的标题一致(按 GitHub 的标题锚点规则)
2. 代码块(```)成对出现,代码块里没有 Markdown 链接(GitHub 不渲染,离线版也会失效)
3. 数值单位用国际符号: 不写"5米""3公斤",符号和数字之间留空格(写"5 m"不写"5m"),见 CLAUDE.md
4. docs/10-中药材识别与采集/10-药名索引.md 与脚本生成结果一致(需要 pypinyin;没装则跳过)
5. docs/images/ 里的 SVG: 有白色背景和 <title>,不含脚本、外部引用,单个不超过 100 KB
"""
import os
import re
import subprocess
import sys
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 允许出现中文单位名称的文件(换算表、历史单位)
UNIT_EXEMPT = {
    'TODO.md',
    'docs/08-基础科学知识/00-度量衡与科学方法.md',
    'docs/08-基础科学知识/09-计量基准的重建.md',
}
# 数字后面紧跟这些中文单位名称时报错;后一项是"不算单位"的后续字(如"米饭""克服")
CN_UNITS = [
    ('毫米', ''), ('厘米', ''), ('千米', ''), ('公里', ''), ('平方米', ''), ('立方米', ''),
    ('毫升', ''), ('千克', ''), ('公斤', ''), ('毫克', ''), ('微克', ''), ('千瓦时', ''),
    ('千瓦', ''), ('伏特', ''), ('安培', ''), ('千卡', ''), ('大卡', ''), ('千帕', ''), ('公顷', ''),
    ('米', '饭粒酒糠粥汤醋粉面德'), ('升', '高温级起空华降'), ('克', '力隆服制'), ('吨', '位'),
]
ASCII_UNITS = r'mm|cm|km|kg|mg|mL|ml|kWh|Wh|Ah|kW|mA|kJ|MJ|kcal|kPa|MPa|GPa|mSv|Hz|mol|ha|m|L|g|t|W|V|A|J|N'
NUM = r'(?<![0-9A-Za-z.])\d+(?:\.\d+)?'


def md_files():
    out = [f for f in subprocess.run(['git', '-C', ROOT, 'ls-files', '-z', '*.md'], capture_output=True,
                                     text=True).stdout.split('\0') if f]
    if not out:  # 不在 git 仓库里时退回到遍历目录
        out = [os.path.relpath(os.path.join(d, f), ROOT) for d, _, fs in os.walk(ROOT)
               if '/.git' not in d and '/dist' not in d for f in fs if f.endswith('.md')]
    return sorted(out)


def slug(h):
    h = h.strip().lower()
    h = re.sub(r'[^\w\- 一-鿿]', '', h)
    return h.replace(' ', '-')


def lines_outside_code(text):
    """逐行返回 (行号, 行, 是否在代码块里)。"""
    fence = False
    for i, line in enumerate(text.split('\n'), 1):
        if line.startswith('```'):
            fence = not fence
            yield i, line, True
            continue
        yield i, line, fence


def collect_anchors(files):
    anchors = {}
    for f in files:
        seen, a = {}, set()
        for _, line, code in lines_outside_code(open(os.path.join(ROOT, f), encoding='utf-8').read()):
            m = None if code else re.match(r'#{1,6} (.*)', line)
            if m:
                s = slug(m.group(1))
                if s in seen:
                    seen[s] += 1
                    s = f'{s}-{seen[s]}'
                else:
                    seen[s] = 0
                a.add(s)
        anchors[os.path.normpath(f)] = a
    return anchors


def check_links_and_code(files, errors):
    anchors = collect_anchors(files)
    for f in files:
        text = open(os.path.join(ROOT, f), encoding='utf-8').read()
        if sum(1 for line in text.split('\n') if line.startswith('```')) % 2:
            errors.append(f'{f}: 代码块 ``` 没有成对闭合')
        for i, line, code in lines_outside_code(text):
            for m in re.finditer(r'\]\(([^)\s]+)\)', re.sub(r'`[^`]*`', '', line)):  # 行内代码里的示例不算
                target = m.group(1)
                if code:
                    if not line.startswith('```'):
                        errors.append(f'{f}:{i}: 代码块里有链接 {target}')
                    continue
                if re.match(r'^[a-z]+:', target):
                    continue
                path, _, frag = target.partition('#')
                full = os.path.normpath(os.path.join(os.path.dirname(f), urllib.parse.unquote(path))) if path \
                    else os.path.normpath(f)
                if not os.path.exists(os.path.join(ROOT, full)):
                    errors.append(f'{f}:{i}: 链接的文件不存在 {target}')
                elif frag and full.endswith('.md') and urllib.parse.unquote(frag) not in anchors.get(full, ()):
                    errors.append(f'{f}:{i}: 锚点不存在 {target}')


def check_units(files, errors):
    cn = [(re.compile(NUM + re.escape(u) + (f'(?![{neg}])' if neg else '')), u) for u, neg in CN_UNITS]
    tight = re.compile(NUM + r'(' + ASCII_UNITS + r')(?![A-Za-z0-9级])')
    for f in files:
        if f in UNIT_EXEMPT:
            continue
        for i, line, code in lines_outside_code(open(os.path.join(ROOT, f), encoding='utf-8').read()):
            plain = re.sub(r'\]\([^)]*\)|`[^`]*`|https?://\S+', '', line)  # 不检查链接地址和行内代码
            for rx, u in cn:
                for m in rx.finditer(plain):
                    errors.append(f'{f}:{i}: 单位用符号,不写"{m.group(0)}"')
            for m in re.finditer(r'(?<![A-Za-z])ml\b', plain):
                errors.append(f'{f}:{i}: 毫升写作 mL,不写 ml')
            for m in tight.finditer(plain):
                errors.append(f'{f}:{i}: 数字和单位符号之间要空格: "{m.group(0)}"')


def check_svgs(errors):
    d = os.path.join(ROOT, 'docs', 'images')
    if not os.path.isdir(d):
        return
    for f in sorted(os.listdir(d)):
        if not f.endswith('.svg'):
            continue
        rel = f'docs/images/{f}'
        s = open(os.path.join(d, f), encoding='utf-8').read()
        if os.path.getsize(os.path.join(d, f)) > 100 * 1024:
            errors.append(f'{rel}: 超过 100 KB')
        if re.search(r'<script|<foreignObject|\bon\w+="|(?:xlink:)?href="(?!#)', s, re.I):
            errors.append(f'{rel}: 不能含脚本、事件属性或外部引用')
        if not re.search(r'<rect[^>]*fill="#fff(?:fff)?"', s, re.I):
            errors.append(f'{rel}: 缺少白色背景(深色模式下看不清)')
        if '<title>' not in s:
            errors.append(f'{rel}: 缺少 <title>')


def check_herb_index(errors):
    try:
        import pypinyin  # noqa: F401
    except ImportError:
        print('提示: 没有安装 pypinyin,跳过药名索引检查')
        return
    idx = os.path.join(ROOT, 'docs', '10-中药材识别与采集', '10-药名索引.md')
    before = open(idx, encoding='utf-8').read()
    subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'build_herb_index.py')], check=True,
                   capture_output=True)
    after = open(idx, encoding='utf-8').read()
    if after != before:
        open(idx, 'w', encoding='utf-8').write(before)  # 只检查,不改文件
        errors.append('docs/10-中药材识别与采集/10-药名索引.md 不是最新的: 请运行 python3 tools/build_herb_index.py')


def main():
    files = md_files()
    errors = []
    check_links_and_code(files, errors)
    check_units(files, errors)
    check_svgs(errors)
    check_herb_index(errors)
    for e in errors:
        print(e)
    print(f'检查了 {len(files)} 个文件,发现 {len(errors)} 个问题')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
