#!/usr/bin/env python3
"""投影片檢查，分成兩段：

  outline：建置前檢查 slides/outline.md
    - 必要的教學結構（封面、學習目標、小測驗、重點整理、參考資料）
    - 每張投影片標註 sources，且指向存在的 wiki 頁面
    - 每張投影片的條列不超過 6 點
    - 數字落地：投影片裡每個 > 10 的數字都要出現在它引用的 wiki 頁面中
  build：建置後檢查 slides.html
    - 投影片張數與大綱相同、每張都有來源連結、連到的 wiki 頁面都存在

用法：python3 scripts/check_slides.py [outline|build|all]
"""
import re
import sys

from common import (ROOT, contains_number, normalize_for_search, numbers_in,
                    parse_outline, wiki_pages)

REQUIRED = ["學習目標", "小測驗", "重點整理", "參考資料"]
MAX_BULLETS = 6


def check_outline():
    errors = []
    slides = parse_outline()
    pages = wiki_pages()
    if not slides or slides[0]["layout"] != "title":
        errors.append("[結構] 第一張必須是封面（<!-- layout: title -->）")
    titles = " ".join(s["title"] for s in slides)
    for word in REQUIRED:
        if word not in titles:
            errors.append(f"[結構] 缺少「{word}」投影片")
    for i, s in enumerate(slides, 1):
        tag = f"第 {i} 張「{s['title']}」"
        if not s["sources"]:
            errors.append(f"[來源] {tag} 沒有 <!-- sources: ... -->")
        for src in s["sources"]:
            if src not in pages:
                errors.append(f"[來源] {tag} 引用不存在的 wiki 頁面 {src}")
        bullets = len(re.findall(r"^\s*(?:-|\d+\.) ", s["body"], re.M))
        if bullets > MAX_BULLETS:
            errors.append(f"[版面] {tag} 有 {bullets} 個條列點，上限 {MAX_BULLETS}")
        haystack = normalize_for_search("\n".join(pages[p][1] for p in s["sources"] if p in pages))
        for num in sorted(numbers_in(s["body"])):
            if not contains_number(haystack, num):
                errors.append(f"[數字] {tag} 的「{num}」在引用的 wiki 頁面 {', '.join(s['sources'])} 中找不到")
    return errors, len(slides)


def check_build():
    errors = []
    out = ROOT / "slides.html"
    if not out.exists():
        return ["[建置] 找不到 slides.html"], 0
    html = out.read_text(encoding="utf-8")
    n_html = len(re.findall(r'<section class="slide', html))
    n_outline = len(parse_outline())
    if n_html != n_outline:
        errors.append(f"[建置] slides.html 有 {n_html} 張，大綱有 {n_outline} 張（可能忘了重新建置）")
    if html.count('class="slide-sources"') != n_html:
        errors.append("[建置] 有投影片沒有顯示來源連結")
    for slug in set(re.findall(r'wiki\.html#([\w-]+)', html)):
        if not (ROOT / "wiki" / f"{slug}.md").exists():
            errors.append(f"[建置] slides.html 連到不存在的 wiki 頁面 {slug}")
    return errors, n_html


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    errs = []
    if mode in ("outline", "all"):
        e, n = check_outline()
        errs += e
        print(f"check_outline：{n} 張投影片，{len(e)} 個問題")
    if mode in ("build", "all"):
        e, n = check_build()
        errs += e
        print(f"check_build：{n} 張投影片，{len(e)} 個問題")
    for e in errs:
        print("  -", e)
    sys.exit(1 if errs else 0)
