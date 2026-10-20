#!/usr/bin/env python3
"""把全书合并成一个可离线阅读、可打印的 HTML 文件。

用法(在仓库根目录): python3 tools/build_offline.py [输出文件]
依赖: pandoc(2.x 或以上)。生成的文件用浏览器打开即可阅读;
用 tools/build_pdf.py 打印成带版本页脚的 PDF。
正文最前面加一页"版本信息"(仓库地址、源文件提交、生成时间),
同样的信息也写进 meta 标签、HTML 注释和一行看不见的白色小字,供日后查证。
"""
import datetime, html, os, re, subprocess, sys, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'dist', '人类紧急求生与健康指南.html')
DEFAULT_REPO = 'https://github.com/CYSAKURAEIEN/human-health-check'
CST = datetime.timezone(datetime.timedelta(hours=8))


def git(*args):
    try:
        return subprocess.run(['git', '-C', ROOT, *args], check=True, capture_output=True, text=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ''


def build_info():
    """版本信息: 仓库地址、源文件提交、生成时间。写进正文、页脚、隐藏文字和 meta 标签,供日后查证。"""
    server, repo = os.environ.get('GITHUB_SERVER_URL'), os.environ.get('GITHUB_REPOSITORY')
    url = f'{server}/{repo}' if server and repo else DEFAULT_REPO
    sha = git('rev-parse', 'HEAD') or 'unknown'
    commit_time = git('log', '-1', '--format=%cI')
    dirty = bool(git('status', '--porcelain'))
    now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)
    local = now.astimezone(CST)
    commit_local = (datetime.datetime.fromisoformat(commit_time).astimezone(CST).strftime('%Y-%m-%d %H:%M')
                    if commit_time else '未知')
    return {
        'url': url,
        'sha': sha,
        'short': sha[:7],
        'dirty': dirty,
        'version': f'{local:%Y.%m.%d}-{sha[:7]}' + ('-dirty' if dirty else ''),
        'built': f'{local:%Y-%m-%d %H:%M} (UTC+8)',
        'built_utc': now.isoformat().replace('+00:00', 'Z'),
        'commit_time': f'{commit_local} (UTC+8)',
    }


def colophon(info):
    """正文最前面的版本页。"""
    e = html.escape
    dirty = '<br><strong>注意: 生成时仓库有未提交的修改,内容可能与该提交不完全一致。</strong>' if info['dirty'] else ''
    return f'''<section class="colophon" id="版本信息">
<h1>版本信息</h1>
<table>
<tr><th>书名</th><td>人类紧急求生与健康指南(离线版)</td></tr>
<tr><th>版本号</th><td><code>{e(info['version'])}</code></td></tr>
<tr><th>生成时间</th><td>{e(info['built'])} / {e(info['built_utc'])}</td></tr>
<tr><th>源文件提交</th><td><code>{e(info['sha'])}</code>(提交于 {e(info['commit_time'])})</td></tr>
<tr><th>仓库地址</th><td><a href="{e(info['url'])}">{e(info['url'])}</a></td></tr>
<tr><th>该版本原文</th><td><a href="{e(info['url'])}/tree/{e(info['sha'])}">{e(info['url'])}/tree/{e(info['sha'])}</a></td></tr>
</table>
<p>查证方法: 在仓库里打开"该版本原文"链接,或运行 <code>git show {e(info['short'])}</code>,
可以看到生成本文件时所用的全部原文和提交时间。每页页脚都印有版本号;
手册内容会不断修订,使用前请尽量对照仓库里的最新版本。{dirty}</p>
<p class="hidden-mark">{e(stamp_text(info))}</p>
</section>
'''


def stamp_text(info):
    return f"人类紧急求生与健康指南 | {info['url']} | commit {info['sha']} | built {info['built_utc']} | version {info['version']}"



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
.colophon td,.colophon th{text-align:left}
.colophon th{white-space:nowrap}
.colophon code{word-break:break-all}
.hidden-mark{color:#fff;font-size:1px;line-height:1px;margin:0;user-select:all}
.doc{border-top:3px double #bbb;margin-top:2em}
#top{position:fixed;right:1em;bottom:1em;background:#c33;color:#fff;padding:.4em .7em;border-radius:4px;text-decoration:none}
@media print{#top{display:none}.doc{page-break-before:always}pre,table,blockquote{page-break-inside:avoid}
  a{color:#222;text-decoration:none}body{max-width:none;padding:0}
  .colophon{page-break-after:always}
}
"""


def main():
    order = list(files_in_order())
    ids = {p: file_id(p) for p in order}
    parts = [render(p, ids) for p in order]
    info = build_info()
    e = html.escape
    os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
                f'<title>人类紧急求生与健康指南(离线版) {e(info["version"])}</title>\n'
                f'<meta name="author" content="{e(info["url"])}">\n'
                f'<meta name="build-version" content="{e(info["version"])}">\n'
                f'<meta name="build-time" content="{e(info["built_utc"])}">\n'
                f'<meta name="source-commit" content="{e(info["sha"])}">\n'
                f'<meta name="source-repository" content="{e(info["url"])}">\n'
                f'<!-- {e(stamp_text(info))} -->\n'
                f'<style>{CSS}</style>\n</head>\n<body>\n'
                f'<a id="top" href="#{ids["README.md"]}">目录</a>\n'
                + colophon(info))
        f.writelines(parts)
        f.write('</body>\n</html>\n')
    print(f'{len(order)} 个文件 → {OUT} ({os.path.getsize(OUT) // 1024} KB), 版本 {info["version"]}')


if __name__ == '__main__':
    main()
