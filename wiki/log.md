# Wiki 時間紀錄

每次 ingest、lint、修正都在最後面加一筆。

## 2026-11-20 fetch

- 依 `sources.json` 從英文維基百科抓 6 篇條目的純文字，存進 `raw/`。
- 發現純文字抽取會吃掉上標、根號和分數線（例如 $2^n$ 變成「2n」、$1/\sqrt2$ 變成「12」），已記在各篇討論紀錄，寫 wiki 時手動還原。

## 2026-11-20 discuss

- 6 篇來源各寫一份討論紀錄（`discussions/`），決定建立 8 個概念頁，以及每頁要用哪些來源。

## 2026-11-20 ingest

- 新增 8 頁：quantum-computer、qubit、superposition-and-measurement、entanglement、quantum-gates、quantum-algorithms、shor-algorithm、decoherence-and-error-correction。
- 建立 index.md。
- 表格裡的數學式改用 `\lvert ... \rangle`，因為 `|` 會被 Markdown 當成表格分隔線。

## 2026-11-20 run 01（graph v1）

- check_slides 失敗：封面寫了「20 分鐘」，這是簡報長度的估計，wiki 裡沒有這個數字。
- 問題出在 plan_outline：LLM 自己加了 wiki 以外的內容。改成「入門簡報」，不寫時間。

## 2026-11-20 run 02（graph v1）

- 全部通過。可是 v1 只拿投影片去比對 wiki，wiki 本身有沒有忠於 raw 完全沒檢查。

## 2026-11-20 第一次執行 lint_wiki

- 結果通過，但加上 `--evidence` 逐條看「每個數字在原文哪裡找到」之後，發現檢查本身有三個漏洞：
  - 「300 萬」對到原文的「300-digit primes」，正確的出處是「3 million physical qubits」。說法剛好是對的，但檢查是因為巧合才通過。
  - raw 檔標頭的抓取日期、版本時間戳也被拿來比對，「20」「11」「2026」都先對到標頭。
  - |11⟩ 這類 ket 標籤被當成數字。
- 修正：比對前去掉 raw 標頭、忽略 ket 標籤、「萬」「億」換算後依序比對 million、完整數字。換算後「3,000,000」又先撞到 Sycamore 的「3,000,000 times faster」，所以改成先比對 million 這種比較具體的寫法。
- 新增 `scripts/test_checks.py`，把這些誤判寫成測試案例。
- 流程改成 graph v2：lint_wiki 移到 ingest 後面，而且一律輸出 evidence 供人工確認；投影片檢查拆成建置前（check_outline）和建置後（check_build）。

## 2026-11-20 run 03（graph v2）

- 停在 test_checks：測試案例「fetched: 2026-11-20」本身寫錯了。原文本文有「as of 2026」和「20 millikelvin」，這個案例本來就應該通過。改用只出現在標頭的版本號 1386685712 當案例。

## 2026-11-20 run 05（graph v3）與 review_claims

- 新增 review_claims 節點：數字檢查抓不到沒有數字的說法，所以 lint_wiki 通過後，由 LLM 逐頁對照 raw 核對每個說法。
- run 05 停在 review_claims（還沒有審查紀錄），符合預期。
- 審查找到 5 處說法超出來源，已修正，詳見 `runs/review-claims.md`：
  - quantum-gates：「例如 AND 不可逆」，來源只提到 AND 和 Toffoli 閘的關係，刪掉例子。
  - superposition-and-measurement：「測量問題到現在仍有爭論」，來源只說這叫測量問題，刪掉「仍有爭論」。
  - superposition-and-measurement：「環境像在測量量子位元」，這個說法出自 03、06，但這頁的 sources 沒有列它們。改寫成 01 支持的說法。
  - shor-algorithm：「最好的」古典演算法，原文是 most scalable，改成「擴展性最好的」。
  - qubit：「Schumacher 在 1995 年的論文裡提出」，原文是「一般認為是他創的，在致謝裡提到是和 Wootters 開玩笑想出來的」，照原文改寫。

## 2026-11-20 文字修飾與 run 08、09（graph v3）

- 用 humanizer、stop-slop 的規則修飾全部文字，wiki 有 4 句改寫（quantum-computer 2 句、decoherence-and-error-correction 2 句），內容不變。
- run 08 停在 review_claims：wiki 在審查之後改過，審查紀錄過期。這是 v3 的設計目的，照規則重新核對改寫的 4 句後再跑 run 09。
