# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A Chinese-language Markdown handbook (《人类紧急求生与健康指南》) covering first aid, disaster response, wilderness survival, farming/husbandry, metallurgy, improvised pharmaceuticals, and everyday living skills (food preservation, nutrition, sanitation, soap, long-term housing, lighting and energy, textiles and tanning, household electrical safety, woodworking and tool maintenance, water supply, pottery/glass/papermaking, teaching and knowledge preservation, record-keeping and community organisation), and a reference of foundational mathematics, physics, chemistry, biology and medicine for rebuilding technology, plus a more advanced part on engineering and a technology-rebuilding roadmap. There is no code, build system, linter, or test suite — all work is writing and editing Markdown that renders on GitHub. Write all content in Simplified Chinese, matching the existing tone.

## Structure

- `README.md` — top-level entry point: table of contents for the nine parts, a quick-lookup table (`快速索引`) of deep links into chapters, recommended reading order, disclaimer, and emergency phone numbers.
- `docs/NN-<主题>/` — one directory per part (`01-日常疾病和伤害` … `09-进阶科学与工程`). Each contains a `README.md` that indexes its chapters, plus chapter files named `NN-<标题>.md`. Some parts start at `00-基础…` for foundational material; others start at `01-`.
- Part 01's display name is 《急救与家庭健康》; its directory keeps the original name `01-日常疾病和伤害` so existing links don't break. Use the display name in link text and headings, the directory name only in paths.

Adding or renaming a chapter means updating three places: the chapter file itself, its part's `README.md`, and the part's bullet list in the root `README.md` (and the quick-lookup table if relevant).

Parts 01 and 03 group their chapters into themed subsections (01: 急救 / 常见病与长期健康 / 特殊人群; 03: 基础 / 户外安全 / 极端环境 / 长期生存), both in the part `README.md` and in the root `README.md`. File numbers follow the order chapters were written, not these groups, so place a new chapter under the right group in both places. The part 03 README is an index plus short summaries; put substantive content in chapters rather than duplicating it there.

## Keeping READMEs in sync with content

The READMEs do more than index files — they summarize what each chapter teaches, assign difficulty/risk ratings, and lay out learning paths. So **changing a chapter's conclusions silently invalidates its READMEs**, and the result is worse than a stale description: the entry point tells readers to do something the chapter now says not to.

After changing what a chapter concludes or recommends, grep both the root `README.md` and the part's `README.md` for the topic and reconcile:

- Chapter descriptions and bullet lists (e.g. a bullet promising "阿司匹林的制备" after the chapter established it can't be made).
- `学习路线` / `推荐阅读顺序` steps (e.g. a learning path still budgeting "1-3个月" for a procedure that was deleted).
- `难度`/`风险`/成功率 ratings and tables, which are easy to leave pointing at content that no longer dominates the chapter.
- The `最后更新时间` line at the bottom of the root `README.md` and `docs/06-制药技术/README.md`.

## Facts are duplicated across files

The same number or instruction often appears in several places, and the copies drift apart. Examples: rewarming water temperature in both `02-外伤处理.md` and `04-雪地极地求生.md`; the lightning crouch in both `02-气象灾害.md` and `05-山地求生.md`; burn-ointment advice in two part READMEs; emergency phone numbers in the root `README.md`, `docs/01-.../README.md` and `docs/02-.../README.md`; fever thresholds in a chapter and its README.

When changing a specific value or a short piece of advice, grep the whole repo for that value (not just the topic) and update every copy, or the handbook will contradict itself.

## Units

Numeric values use SI unit symbols with a space between number and symbol (`1.5 m`, `500 g`, `220 V`, `kWh`, `mL`), not Chinese unit names. Exceptions: time in running prose stays Chinese (`冲洗15分钟`, `等待3天`) but uses symbols inside formulas, data and compound units (`m/s`, `km/h`); `°C` and `%` attach without a space. 市制/英制 units (斤, 亩, 里, 英寸, 磅…) are converted to SI (per-亩 rates become per-ha, ×15); they appear only in the conversion tables in `08-基础科学知识/00-度量衡与科学方法.md` and the historical-units section of `08-基础科学知识/09-计量基准的重建.md`. Angles use `°`, liquor strength uses `%vol`. The symbol glossary is the `📏 单位符号说明` section of the root `README.md` — add any new symbol there (its last column links to how each unit is reconstructed in `09-计量基准的重建.md`).

## Linking conventions

- Links use relative paths with the literal Chinese file/directory names (e.g. `../04-动植物培育/04-药用植物.md`).
- Anchor links rely on GitHub's heading slugs, so the fragment must match the full heading text exactly (e.g. `## 烫伤与烧伤` → `#烫伤与烧伤`). When renaming a heading, grep for links targeting it.

## Chapter style

The style differs by when a part was written; follow the conventions of the part you are editing:

- Parts 01–02 (and `03-野外生存/00-基础生存技能.md`) open with a `## 目录` of in-page anchor links and use numbered step lists under `##`/`###` headings.
- Parts 05–06 (and parts 08–09) open with a `>` tagline and a prominent `⚠️` warning section, use numbered `## 一、…` / `### 1.1 …` headings, fenced code blocks for step-by-step procedures, checklists (`- [ ]`), difficulty/risk tables with ⭐/☠️ ratings, and end with a `## 相关章节` section of ⏮️/⏭️/🔗 cross-links followed by a bolded closing line.
- Safety framing is a deliberate part of the content: medical chapters direct readers to professional care, and the pharmaceutical/metallurgy parts stress that procedures are for civilization-collapse scenarios only. Preserve these warnings when editing, and keep dangerous-procedure content at the educational level of the existing chapters.

## Contributing workflow

Per the README: feature branch → commit (commit messages are written in Chinese, e.g. `添加某某内容`) → pull request.
