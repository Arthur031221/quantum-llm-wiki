# review_claims：wiki 說法逐頁核對

- 節點：review_claims（LLM）
- 時間：2026-11-20，run 05 之後
- 方法：逐頁讀 wiki，每個沒有數字的說法都回到該頁 `sources` 列出的 raw 檔找出處（數字已由 lint_wiki 比對，這裡不重複）。找不到出處、或出處在別的來源但這頁沒列的，都算問題。

## 各頁結果

| 頁面 | 問題數 | 處理 |
|---|---|---|
| quantum-computer | 0 | |
| qubit | 1 | Schumacher 命名的說法不精確，照原文改寫 |
| superposition-and-measurement | 2 | 「仍有爭論」來源沒寫，刪除；「環境像在測量」出自未列出的來源，改寫 |
| entanglement | 0 | |
| quantum-gates | 1 | 「例如 AND 不可逆」來源沒寫，刪除例子 |
| quantum-algorithms | 0 | |
| shor-algorithm | 1 | 「最好的」古典演算法改成原文的「擴展性最好的」 |
| decoherence-and-error-correction | 0 | |
| 合計 | 5 | 全部已修正 |

## 觀察

- 5 個問題都出在 ingest：LLM 會順手補上自己知道、而且大致正確的說法（AND 不可逆、測量問題有爭論），或把原文的程度詞換成更強的詞（most scalable 寫成「最好的」）。
- 這些說法都沒有數字，所以 lint_wiki 全部放行。
- 其中一個問題（環境像在測量）的內容在別的來源裡找得到，錯在這頁的 sources 沒列那篇。這種「來源標錯頁」的問題，數字比對也抓不到。

結論：通過（5 個問題已在 wiki 中修正）

## 重審（run 08 之後）

文字修飾改了 4 句 wiki，逐句回原文確認：

| 頁面 | 改寫後的句子 | 出處 | 結果 |
|---|---|---|---|
| quantum-computer | 古典電腦裡的半導體也靠量子效應運作 | 01 Quantum information processing：semiconductors … may rely on quantum behavior | 通過 |
| quantum-computer | 做法是設計演算法，讓干涉放大正確答案的機率 | 01 導言：wave interference effects amplify the probability of the desired measurement result | 通過 |
| decoherence-and-error-correction | 相干性並沒有消失，它混進了環境中大量的自由度 | 06 Concept：coherence is not lost but rather mixed with many more degrees of freedom in the environment | 通過 |
| decoherence-and-error-correction | 所以 Shor 演算法目前還威脅不到真實使用的加密 | 01 Decoherence：分解 2,048 位元整數至少要 3 million 實體量子位元；01 導言：not yet practical for real-world applications | 通過 |

結論：通過（重審 4 句，沒有新問題）
