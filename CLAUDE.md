# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A Chinese-language Markdown handbook (《人类紧急求生与健康指南》) covering first aid, disaster response, wilderness survival, farming/husbandry, metallurgy, and improvised pharmaceuticals. There is no code, build system, linter, or test suite — all work is writing and editing Markdown that renders on GitHub. Write all content in Simplified Chinese, matching the existing tone.

## Structure

- `README.md` — top-level entry point: table of contents for the six parts, a quick-lookup table (`快速索引`) of deep links into chapters, recommended reading order, disclaimer, and emergency phone numbers.
- `docs/NN-<主题>/` — one directory per part (`01-日常疾病和伤害` … `06-制药技术`). Each contains a `README.md` that indexes its chapters, plus chapter files named `NN-<标题>.md`. Some parts start at `00-基础…` for foundational material; others start at `01-`.

Adding or renaming a chapter means updating three places: the chapter file itself, its part's `README.md`, and the part's bullet list in the root `README.md` (and the quick-lookup table if relevant).

## Linking conventions

- Links use relative paths with the literal Chinese file/directory names (e.g. `../04-动植物培育/04-药用植物.md`).
- Anchor links rely on GitHub's heading slugs, so the fragment must match the full heading text exactly (e.g. `## 烫伤与烧伤` → `#烫伤与烧伤`). When renaming a heading, grep for links targeting it.

## Chapter style

The style differs by when a part was written; follow the conventions of the part you are editing:

- Parts 01–02 (and `03-野外生存/00-基础生存技能.md`) open with a `## 目录` of in-page anchor links and use numbered step lists under `##`/`###` headings.
- Parts 05–06 open with a `>` tagline and a prominent `⚠️` warning section, use numbered `## 一、…` / `### 1.1 …` headings, fenced code blocks for step-by-step procedures, checklists (`- [ ]`), difficulty/risk tables with ⭐/☠️ ratings, and end with a `## 相关章节` section of ⏮️/⏭️/🔗 cross-links followed by a bolded closing line.
- Safety framing is a deliberate part of the content: medical chapters direct readers to professional care, and the pharmaceutical/metallurgy parts stress that procedures are for civilization-collapse scenarios only. Preserve these warnings when editing, and keep dangerous-procedure content at the educational level of the existing chapters.

## Contributing workflow

Per the README: feature branch → commit (commit messages are written in Chinese, e.g. `添加某某内容`) → pull request.
