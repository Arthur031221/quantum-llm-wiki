#!/usr/bin/env python3
"""節點 fetch：依 sources.json 從英文維基百科抓純文字全文，存成 raw/<id>.md。

raw/ 裡的檔案抓下來後就不再修改（LLM Wiki 的 raw 層是唯讀的）。
已經存在的檔案會跳過，要重抓請先刪除該檔。
用法：python3 scripts/fetch_sources.py
"""
import json
import sys
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://en.wikipedia.org/w/api.php"
UA = "LLM-Wiki-Homework/1.0 (educational project)"


def fetch(title):
    params = {
        "action": "query", "format": "json", "formatversion": "2", "redirects": "1",
        "prop": "extracts|revisions|info", "explaintext": "1", "exsectionformat": "wiki",
        "rvprop": "ids|timestamp", "inprop": "url", "titles": title,
    }
    req = urllib.request.Request(API + "?" + urllib.parse.urlencode(params), headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        page = json.load(r)["query"]["pages"][0]
    return page


def main():
    sources = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
    for s in sources:
        out = ROOT / "raw" / f"{s['id']}.md"
        if out.exists():
            print(f"skip  {out.name}（已存在）")
            continue
        page = fetch(s["title"])
        if "missing" in page or not page.get("extract"):
            print(f"FAIL  {s['title']}：找不到條目", file=sys.stderr)
            sys.exit(1)
        rev = page["revisions"][0]
        header = (
            "---\n"
            f"title: {page['title']}\n"
            f"url: {page['fullurl']}\n"
            f"revision: {rev['revid']} ({rev['timestamp']})\n"
            f"fetched: {date.today().isoformat()}\n"
            "license: CC BY-SA 4.0 (Wikipedia contributors)\n"
            "---\n\n"
        )
        out.write_text(header + page["extract"].strip() + "\n", encoding="utf-8")
        print(f"ok    {out.name}  {len(page['extract']):>6} 字元  rev {rev['revid']}")
    write_manifest()


def write_manifest():
    """把每個 raw 檔的標頭整理成 raw/manifest.json，給 wiki 頁面顯示來源連結用。"""
    manifest = {}
    for p in sorted((ROOT / "raw").glob("*.md")):
        head = p.read_text(encoding="utf-8").split("\n---", 1)[0]
        meta = dict(line.split(": ", 1) for line in head.splitlines()[1:] if ": " in line)
        manifest[p.stem] = meta
    (ROOT / "raw" / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"manifest.json：{len(manifest)} 個來源")


if __name__ == "__main__":
    main()
