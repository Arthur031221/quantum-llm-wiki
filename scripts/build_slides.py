#!/usr/bin/env python3
"""節點 build_slides：把 slides/outline.md 轉成 slides.html，並輸出 slides/slide-map.json。

slide-map.json 記錄「每個 wiki 頁面被哪幾張投影片引用」，wiki 頁面會用它顯示反向連結。
用法：python3 scripts/build_slides.py
"""
import html
import json

from common import ROOT, md_to_html, parse_outline, wiki_pages

TEMPLATE = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>量子電腦是什麼？｜教學簡報</title>
<meta name="description" content="給初學者的量子計算入門簡報，內容全部來自量子計算 LLM Wiki。">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}]});"></script>
<link rel="stylesheet" href="assets/slides.css">
</head>
<body>
<!-- 這個檔案由 scripts/build_slides.py 產生，請改 slides/outline.md 再重新建置 -->
<div id="deck">
__SLIDES__
</div>
<nav id="controls">
  <a href="index.html" class="home">首頁</a>
  <button id="prev" type="button" aria-label="上一張">‹</button>
  <span id="counter"></span>
  <button id="next" type="button" aria-label="下一張">›</button>
</nav>
<div id="progress"><div></div></div>
<script src="assets/slides.js"></script>
</body>
</html>
"""


def build():
    slides = parse_outline()
    pages = wiki_pages()
    slide_map = {slug: [] for slug in pages}
    parts = []
    for i, s in enumerate(slides, 1):
        links = []
        for src in s["sources"]:
            title = pages[src][0].get("title", src) if src in pages else src
            links.append(f'<a href="wiki.html#{src}">{html.escape(title)}</a>')
            slide_map.setdefault(src, []).append({"n": i, "title": s["title"]})
        parts.append(
            f'<section class="slide layout-{s["layout"]}" data-n="{i}">\n'
            f'<div class="slide-body">\n{md_to_html(s["body"])}\n</div>\n'
            f'<footer class="slide-sources">Wiki 來源：{"、".join(links)}</footer>\n'
            f"</section>"
        )
    (ROOT / "slides.html").write_text(TEMPLATE.replace("__SLIDES__", "\n".join(parts)), encoding="utf-8")
    (ROOT / "slides" / "slide-map.json").write_text(
        json.dumps(slide_map, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"build_slides：產生 slides.html（{len(slides)} 張）與 slides/slide-map.json")


if __name__ == "__main__":
    build()
