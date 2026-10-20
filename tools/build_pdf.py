#!/usr/bin/env python3
"""把 build_offline.py 生成的 HTML 打印成 PDF,并加上可查证的版本标记。

用法(在仓库根目录): python3 tools/build_pdf.py dist/human-health-guide.html dist/human-health-guide.pdf
依赖: playwright(及其 Chromium)、pypdf。可用环境变量 CHROME_PATH 指定浏览器。

版本信息取自 HTML 里的 meta 标签(仓库地址、源文件提交、生成时间、版本号),写在三处:
- 明显的: 每页页脚印出仓库地址、版本号和页码;正文最前面的"版本信息"页(由 build_offline.py 生成)
- 隐藏的: 每页页脚下方一行白色 1px 文字(看不见,但能被搜索和复制);PDF 文档属性(作者、主题、关键词和自定义字段)
"""
import html
import os
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter


def read_meta(path):
    with open(path, encoding='utf-8') as f:
        head = f.read(8192)
    get = lambda name: html.unescape((re.search(rf'<meta name="{name}" content="([^"]*)">', head) or [None, ''])[1])
    return {k: get(k) for k in ('build-version', 'build-time', 'source-commit', 'source-repository')}


def footer(info):
    e = html.escape
    visible = (f'{e(info["source-repository"])} · 版本 {e(info["build-version"])} · '
               '第 <span class="pageNumber"></span> / <span class="totalPages"></span> 页')
    hidden = (f'人类紧急求生与健康指南 | {e(info["source-repository"])} | commit {e(info["source-commit"])} | '
              f'built {e(info["build-time"])} | version {e(info["build-version"])}')
    return ('<div style="width:100%;text-align:center;font-size:8px;color:#888;'
            'font-family:\'Noto Sans CJK SC\',sans-serif">'
            f'{visible}<div style="color:#fff;font-size:1px;line-height:1px">{hidden}</div></div>')


def main():
    src, out = sys.argv[1], sys.argv[2]
    info = read_meta(src)
    tmp = out + '.tmp'
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=os.environ.get('CHROME_PATH') or None)
        page = browser.new_page()
        page.goto(pathlib.Path(src).resolve().as_uri(), wait_until='load', timeout=0)
        page.pdf(path=tmp, format='A4', print_background=True, display_header_footer=True,
                 header_template='<span></span>', footer_template=footer(info),
                 margin={'top': '14mm', 'bottom': '16mm', 'left': '12mm', 'right': '12mm'})
        browser.close()

    writer = PdfWriter(clone_from=PdfReader(tmp))
    writer.add_metadata({
        '/Title': f'人类紧急求生与健康指南(离线版) {info["build-version"]}',
        '/Author': info['source-repository'],
        '/Subject': f'由 {info["source-repository"]} 的提交 {info["source-commit"]} 于 {info["build-time"]} 生成',
        '/Keywords': f'version={info["build-version"]}; commit={info["source-commit"]}; built={info["build-time"]}',
        '/Creator': 'tools/build_offline.py + tools/build_pdf.py',
        '/BuildVersion': info['build-version'],
        '/SourceCommit': info['source-commit'],
        '/SourceRepository': info['source-repository'],
        '/BuildTime': info['build-time'],
    })
    with open(out, 'wb') as f:
        writer.write(f)
    os.remove(tmp)
    print(f'{out}: {len(writer.pages)} 页, 版本 {info["build-version"]}')


if __name__ == '__main__':
    main()
