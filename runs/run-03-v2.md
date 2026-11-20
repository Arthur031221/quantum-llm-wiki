# Run 03（graph v2）

- 時間：2026-11-20 16:24:47
- 節點順序：test_checks → fetch → discuss → ingest → lint_wiki → plan_outline → check_outline → build_slides → check_build
- 這次的變更：lint_wiki 移到 ingest 之後並輸出 evidence；投影片檢查拆成建置前後；先跑檢查器自我測試

| # | 節點 | 類型 | 結果 | 耗時 |
|---|---|---|---|---|
| 1 | test_checks | 腳本 | 失敗 | 0.02s |

**結果：失敗，停在 test_checks，回到節點 test_checks 重做**

## 各節點輸出

### 1. test_checks

```
ok   預期擋下：2019 年 Google 用 53 個量子位元
ok   預期通過：2019 年 Google 用 54 個量子位元
ok   預期通過：需要 300 萬個實體量子位元
ok   預期擋下：需要 400 萬個實體量子位元
ok   預期通過：超級電腦要算 10,000 年
ok   預期通過：一半機率得到 $|11⟩$
BUG  預期擋下：fetched: 2026-11-20
test_checks：6/7 通過
```

