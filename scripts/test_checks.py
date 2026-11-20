#!/usr/bin/env python3
"""檢查節點的自我測試：確認數字比對該擋的會擋、該過的會過。
這些案例來自 run 02 之後人工看 evidence 時發現的誤判。
用法：python3 scripts/test_checks.py
"""
import sys

from common import RAW, contains_number, normalize_for_search, numbers_in, split_frontmatter

raw = normalize_for_search(split_frontmatter((RAW / "01-quantum-computing.md").read_text(encoding="utf-8"))[1])
CASES = [
    ("2019 年 Google 用 53 個量子位元", False),   # 原文是 54
    ("2019 年 Google 用 54 個量子位元", True),
    ("需要 300 萬個實體量子位元", True),          # 原文是 3 million
    ("需要 400 萬個實體量子位元", False),
    ("超級電腦要算 10,000 年", True),             # 千分位逗號
    ("一半機率得到 $|11⟩$", True),               # ket 標籤不算數字
    ("版本號 1386685712", False),                 # 只出現在 raw 標頭，不能拿來比對
]
bad = 0
for text, expect in CASES:
    nums = numbers_in(text)
    ok = all(contains_number(raw, n) for n in nums)
    good = ok == expect
    bad += not good
    print("ok  " if good else "BUG ", f"預期{'通過' if expect else '擋下'}：{text}")
print(f"test_checks：{len(CASES) - bad}/{len(CASES)} 通過")
sys.exit(1 if bad else 0)
