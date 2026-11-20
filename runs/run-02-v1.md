# Run 02（graph v1）

- 時間：2026-11-20 16:23:02
- 節點順序：fetch → discuss → ingest → plan_outline → build_slides → check_slides
- 這次的變更：修正封面的 20 分鐘

| # | 節點 | 類型 | 結果 | 耗時 |
|---|---|---|---|---|
| 1 | fetch | 腳本 | 通過 | 0.04s |
| 2 | discuss | LLM | 通過 | 0.00s |
| 3 | ingest | LLM | 通過 | 0.00s |
| 4 | plan_outline | LLM | 通過 | 0.00s |
| 5 | build_slides | 腳本 | 通過 | 0.02s |
| 6 | check_slides | 腳本 | 通過 | 0.02s |

**結果：通過**

## 各節點輸出

### 1. fetch

```
skip  01-quantum-computing.md（已存在）
skip  02-qubit.md（已存在）
skip  03-quantum-entanglement.md（已存在）
skip  04-quantum-logic-gate.md（已存在）
skip  05-shors-algorithm.md（已存在）
skip  06-quantum-decoherence.md（已存在）
manifest.json：6 個來源
```

### 2. discuss

```
6 篇來源都有討論紀錄
```

### 3. ingest

```
wiki 頁面 8 個，index.md 與 log.md 存在
```

### 4. plan_outline

```
slides/outline.md 存在
```

### 5. build_slides

```
build_slides：產生 slides.html（17 張）與 slides/slide-map.json
```

### 6. check_slides

```
check_outline：17 張投影片，0 個問題
check_build：17 張投影片，0 個問題
```

