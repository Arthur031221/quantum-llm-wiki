#!/usr/bin/env python3
"""節點 lint_wiki：檢查 wiki 是否符合 CLAUDE.md 的規則。

1. 每個 raw 來源都有對應的討論紀錄（先討論、後生成）
2. 每頁有 title、summary、sources，且 sources 指向存在的 raw 檔
3. 頁面引用的 raw 來源必須先有討論紀錄
4. 頁面之間的連結都存在、index.md 列出每一頁
5. 數字落地：頁面裡每個 > 10 的數字都要出現在它引用的 raw 來源中
用法：python3 scripts/lint_wiki.py   （全部通過時 exit 0）
"""
import re
import sys

from common import (DISCUSS, RAW, WIKI, contains_number, find_number, normalize_for_search,
                    numbers_in, raw_ids, split_frontmatter, wiki_pages)


EVIDENCE = "--evidence" in sys.argv
evidence = []


def lint():
    errors = []
    raws = raw_ids()
    discussed = {p.stem for p in DISCUSS.glob("*.md")}
    for r in raws:
        if r not in discussed:
            errors.append(f"[討論] raw/{r}.md 沒有 discussions/{r}.md")

    pages = wiki_pages()
    index_text = (WIKI / "index.md").read_text(encoding="utf-8") if (WIKI / "index.md").exists() else ""
    if not index_text:
        errors.append("[索引] 缺少 wiki/index.md")
    # 只比對來源本文，標頭裡的日期、版本號不算
    raw_text = {r: normalize_for_search(split_frontmatter((RAW / f"{r}.md").read_text(encoding="utf-8"))[1])
                for r in raws}

    for slug, (meta, body) in pages.items():
        where = f"wiki/{slug}.md"
        for key in ("title", "summary", "sources"):
            if not meta.get(key):
                errors.append(f"[格式] {where} 缺少 frontmatter 欄位 {key}")
        srcs = meta.get("sources") or []
        if isinstance(srcs, str):
            srcs = [srcs]
        for s in srcs:
            if s not in raws:
                errors.append(f"[來源] {where} 引用不存在的來源 {s}")
            elif s not in discussed:
                errors.append(f"[討論] {where} 引用 {s}，但這個來源還沒有討論紀錄")
        for target in re.findall(r"\]\(([\w-]+)\.md\)", body):
            if target not in pages:
                errors.append(f"[連結] {where} 連到不存在的頁面 {target}.md")
        if f"({slug}.md)" not in index_text:
            errors.append(f"[索引] index.md 沒有列出 {slug}.md")
        haystack = "\n".join(raw_text.get(s, "") for s in srcs)
        for num in sorted(numbers_in(body)):
            if not contains_number(haystack, num):
                errors.append(f"[數字] {where} 的「{num}」在引用的來源 {', '.join(srcs)} 中找不到")
            elif EVIDENCE:
                evidence.append(f"{where}「{num}」 ← {snippet(haystack, num)}")
    return errors, len(pages)


def snippet(text, token, width=50):
    m = find_number(text, token)
    return text[max(0, m.start() - width):m.end() + width].replace("\n", " ")


if __name__ == "__main__":
    errs, n = lint()
    if EVIDENCE:
        print("\n".join(evidence))
    if errs:
        print(f"lint_wiki：{len(errs)} 個問題")
        for e in errs:
            print("  -", e)
        sys.exit(1)
    print(f"lint_wiki：通過（{n} 個 wiki 頁面）")
