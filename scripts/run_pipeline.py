#!/usr/bin/env python3
"""依照 graph 跑一次完整流程，並把每個節點的結果寫成 runs/run-NN-<graph>.md。

graph v1：fetch → discuss → ingest → plan_outline → build_slides → check_slides（所有檢查集中在最後）
graph v2：test_checks → fetch → discuss → ingest → lint_wiki → plan_outline → check_outline → build_slides → check_build
graph v3：v2 再加上 lint_wiki 之後的 review_claims（LLM 逐頁核對沒有數字的說法）

LLM 節點（discuss、ingest、review_claims、plan_outline）由 Claude Code 依 CLAUDE.md 執行，這支腳本只確認它們的產物存在。
腳本節點失敗時，流程停下來，紀錄裡會寫出要回到哪一個節點重做。

用法：python3 scripts/run_pipeline.py v2 [--note "這次改了什麼"]
"""
import subprocess
import sys
import time
from datetime import datetime

from common import DISCUSS, OUTLINE, ROOT, WIKI, raw_ids

PY = sys.executable


def script(cmd):
    def run():
        p = subprocess.run([PY, *cmd], cwd=ROOT / "scripts", capture_output=True, text=True)
        return p.returncode == 0, (p.stdout + p.stderr).strip()
    return run


def artifact(check):
    def run():
        ok, msg = check()
        return ok, msg
    return run


def discuss_done():
    missing = [r for r in raw_ids() if not (DISCUSS / f"{r}.md").exists()]
    return (not missing, "缺少討論紀錄：" + ", ".join(missing) if missing
            else f"{len(raw_ids())} 篇來源都有討論紀錄")


def ingest_done():
    pages = [p for p in WIKI.glob("*.md") if p.stem not in ("index", "log")]
    ok = bool(pages) and (WIKI / "index.md").exists() and (WIKI / "log.md").exists()
    return ok, f"wiki 頁面 {len(pages)} 個，index.md 與 log.md {'存在' if ok else '缺少'}"


REVIEW = ROOT / "runs" / "review-claims.md"


def review_done():
    """review_claims 的紀錄必須存在、結論是通過，而且比每個 wiki 頁面都新（wiki 改過就要重新審）。"""
    if not REVIEW.exists():
        return False, "缺少 runs/review-claims.md：還沒有逐頁核對說法"
    newest = max(p.stat().st_mtime for p in WIKI.glob("*.md") if p.stem != "log")
    if REVIEW.stat().st_mtime < newest:
        return False, "wiki 在審查之後又改過，review-claims.md 已過期"
    if "結論：通過" not in REVIEW.read_text(encoding="utf-8"):
        return False, "review-claims.md 的結論不是「通過」"
    return True, "review-claims.md 存在、比 wiki 新、結論為通過"


def outline_done():
    return OUTLINE.exists(), "slides/outline.md " + ("存在" if OUTLINE.exists() else "不存在")


# (節點名稱, 類型, 執行函式, 失敗時要回到的節點)
NODES = {
    "fetch":        ("腳本", script(["fetch_sources.py"]), "fetch"),
    "discuss":      ("LLM", artifact(discuss_done), "discuss"),
    "ingest":       ("LLM", artifact(ingest_done), "ingest"),
    "test_checks":  ("腳本", script(["test_checks.py"]), "test_checks"),
    "lint_wiki":    ("腳本", script(["lint_wiki.py", "--evidence"]), "ingest"),
    "review_claims": ("LLM", artifact(review_done), "ingest"),
    "plan_outline": ("LLM", artifact(outline_done), "plan_outline"),
    "check_outline": ("腳本", script(["check_slides.py", "outline"]), "plan_outline"),
    "build_slides": ("腳本", script(["build_slides.py"]), "build_slides"),
    "check_build":  ("腳本", script(["check_slides.py", "build"]), "build_slides"),
    "check_slides": ("腳本", script(["check_slides.py", "all"]), "plan_outline"),
}

GRAPHS = {
    "v1": ["fetch", "discuss", "ingest", "plan_outline", "build_slides", "check_slides"],
    "v2": ["test_checks", "fetch", "discuss", "ingest", "lint_wiki", "plan_outline", "check_outline",
           "build_slides", "check_build"],
    "v3": ["test_checks", "fetch", "discuss", "ingest", "lint_wiki", "review_claims", "plan_outline",
           "check_outline", "build_slides", "check_build"],
}


def main():
    graph = sys.argv[1] if len(sys.argv) > 1 else "v2"
    note = sys.argv[sys.argv.index("--note") + 1] if "--note" in sys.argv else ""
    runs = ROOT / "runs"
    n = len(list(runs.glob("run-*.md"))) + 1
    out = runs / f"run-{n:02d}-{graph}.md"

    lines = [f"# Run {n:02d}（graph {graph}）", "",
             f"- 時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
             f"- 節點順序：{' → '.join(GRAPHS[graph])}"]
    if note:
        lines.append(f"- 這次的變更：{note}")
    lines += ["", "| # | 節點 | 類型 | 結果 | 耗時 |", "|---|---|---|---|---|"]
    details, result = [], "通過"
    for i, name in enumerate(GRAPHS[graph], 1):
        kind, fn, back = NODES[name]
        t = time.time()
        ok, msg = fn()
        lines.append(f"| {i} | {name} | {kind} | {'通過' if ok else '失敗'} | {time.time() - t:.2f}s |")
        details += [f"### {i}. {name}", "", "```", msg or "(無輸出)", "```", ""]
        print(f"[{'ok' if ok else 'FAIL'}] {name}")
        if not ok:
            result = f"失敗，停在 {name}，回到節點 {back} 重做"
            break
    lines += ["", f"**結果：{result}**", "", "## 各節點輸出", ""] + details
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"結果：{result}\n紀錄：runs/{out.name}")
    sys.exit(0 if result == "通過" else 1)


if __name__ == "__main__":
    main()
