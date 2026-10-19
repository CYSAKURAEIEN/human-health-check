#!/usr/bin/env python3
"""把全书合并成一个可离线阅读、可打印的 HTML 文件。

用法(在仓库根目录): python3 tools/build_offline.py [输出文件]
依赖: pandoc(2.x 或以上)。生成的文件用浏览器打开即可阅读,
浏览器"打印 → 另存为 PDF"即可得到 PDF。
"""
import html, os, re, subprocess, sys, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'dist', '人类紧急求生与健康指南.html')


def files_in_order():
    """根 README → 各部分 README → 各章(按文件名排序)。"""
    yield 'README.md'
    for part in sorted(os.listdir(os.path.join(ROOT, 'docs'))):
        d = os.path.join('docs', part)
        if not os.path.isdir(os.path.join(ROOT, d)):
            continue
        yield os.path.join(d, 'README.md')
        for f in sorted(os.listdir(os.path.join(ROOT, d))):
            if f.endswith('.md') and f != 'README.md':
                yield os.path.join(d, f)


def file_id(path):
    return 'f-' + re.sub(r'[^\w一-鿿]+', '-', path[:-3]).strip('-')


def render(path, ids):
    """用 pandoc 把一个 Markdown 文件转成 HTML 片段,给标题 id 加上文件前缀,改写站内链接。"""
    fid = ids[path]
    body = subprocess.run(['pandoc', '-f', 'gfm', '-t', 'html', '--wrap=none', os.path.join(ROOT, path)],
                          check=True, capture_output=True, text=True).stdout
    # pandoc 生成的 id 会保留 emoji 变体选择符(U+FE0F),GitHub 的锚点不保留
    body = re.sub(r'\bid="([^"]*)"', lambda m: f'id="{fid}--{m.group(1).replace(chr(0xFE0F), "")}"', body)

    def fix(m):
        href = html.unescape(m.group(1))
        if re.match(r'^[a-z]+:', href):
            return m.group(0)
        target, _, frag = href.partition('#')
        target = urllib.parse.unquote(target)
        frag = urllib.parse.unquote(frag)
        if target:
            t = os.path.normpath(os.path.join(os.path.dirname(path), target))
            if os.path.isdir(os.path.join(ROOT, t)):
                t = os.path.join(t, 'README.md')
            if t not in ids:  # 指向仓库里非 Markdown 的文件(如 LICENSE)
                return m.group(0)
            tid = ids[t]
        else:
            tid = fid
        new = f'#{tid}--{frag}' if frag else f'#{tid}'
        return f'href="{html.escape(new)}"'

    body = re.sub(r'href="([^"]*)"', fix, body)
    # 离线时外部图片(如许可证徽章)加载不出来,换成替代文字
    body = re.sub(r'<img\s[^>]*src="https?://[^"]*"[^>]*alt="([^"]*)"[^>]*/?>', r'\1', body)
    return f'<section class="doc" id="{fid}">\n<div class="src">{html.escape(path)}</div>\n{body}\n</section>\n'


CSS = """
body{font-family:"Noto Sans CJK SC","Source Han Sans SC","PingFang SC","Microsoft YaHei",sans-serif;
  max-width:52em;margin:0 auto;padding:1em;line-height:1.7;color:#222;background:#fff}
h1{border-bottom:2px solid #c33;padding-bottom:.2em}
h2{border-bottom:1px solid #ddd;padding-bottom:.15em}
table{border-collapse:collapse;margin:.8em 0;font-size:.95em;display:block;overflow-x:auto}
th,td{border:1px solid #ccc;padding:.3em .6em;vertical-align:top}
th{background:#f3f3f3}
pre{background:#f6f6f6;padding:.8em;overflow-x:auto;white-space:pre-wrap;word-break:break-word;border-radius:4px}
code{font-family:"Noto Sans Mono CJK SC",Consolas,monospace;font-size:.92em}
blockquote{border-left:4px solid #c33;margin:.8em 0;padding:.2em 1em;color:#555;background:#fafafa}
a{color:#0b5cad}
.src{font-size:.8em;color:#999;margin-top:2em}
.doc{border-top:3px double #bbb;margin-top:2em}
#top{position:fixed;right:1em;bottom:1em;background:#c33;color:#fff;padding:.4em .7em;border-radius:4px;text-decoration:none}
@media print{#top{display:none}.doc{page-break-before:always}pre,table,blockquote{page-break-inside:avoid}
  a{color:#222;text-decoration:none}body{max-width:none}}
"""


def main():
    order = list(files_in_order())
    ids = {p: file_id(p) for p in order}
    parts = [render(p, ids) for p in order]
    os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
                f'<title>人类紧急求生与健康指南(离线版)</title>\n<style>{CSS}</style>\n</head>\n<body>\n'
                f'<a id="top" href="#{ids["README.md"]}">目录</a>\n')
        f.writelines(parts)
        f.write('</body>\n</html>\n')
    print(f'{len(order)} 个文件 → {OUT} ({os.path.getsize(OUT) // 1024} KB)')


if __name__ == '__main__':
    main()
