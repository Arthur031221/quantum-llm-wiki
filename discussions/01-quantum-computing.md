# 討論：Quantum computing

來源：raw/01-quantum-computing.md（英文維基百科，rev 1386685712）

## 1. 這篇在講什麼

量子電腦的總覽條目。從量子位元、疊加、干涉講到演算法、加密、硬體困難和目前的實際狀況，範圍最廣，適合當整份 wiki 的主幹。

## 2. 初學者需要的重點

- 量子電腦用量子態表示和處理資訊，運用疊加、干涉、糾纏（導言）。
- 一個量子位元的狀態是 α|0⟩+β|1⟩，測量得到 0 的機率是 |α|²，且 |α|²+|β|²=1（Quantum information）。
- 每多一個量子位元，狀態空間維度加倍；n 個量子位元是 2^n 維，模擬 100 個量子位元要存 2^100 個數（Quantum information）。
- 「同時算所有輸入」只是直覺說法，最後測量只拿到一個值，演算法還要靠干涉放大正確答案的機率（導言、Quantum parallelism）。
- Shor 演算法（1994）能有效分解整數，威脅 RSA；Grover 演算法（1996）對無結構搜尋有平方加速（History、Algorithms）。
- 現況：到 2023 年，所有實際應用上古典電腦仍然比較強；2019 年 Google 宣稱達成量子霸權，IBM 提出反駁（Engineering、Quantum supremacy）。

## 3. 要寫進哪些 wiki 頁面

- 新增 `quantum-computer.md`：定義、用到的三個現象、發展簡史、現況與爭議。
- 新增 `quantum-algorithms.md`：量子平行的誤解、干涉放大、Shor 與 Grover 的加速種類、量子模擬。
- 提供 `qubit.md`、`superposition-and-measurement.md`、`decoherence-and-error-correction.md` 的補充內容。

## 4. 疑點與決定

- 抽取純文字時上標不見了：原文的「2n」是 $2^n$、「2100」是 $2^{100}$、「10−3」是 $10^{-3}$。寫 wiki 時要還原成數學式，不能照抄成 2100。
- 量子霸權的數字有爭議（Google 說超級電腦要 10,000 年，IBM 說約 2.5 天），兩邊都要寫出來，不能只寫一邊。
- Grover 沒有獨立的來源頁，只用這篇的內容，寫到「平方加速」為止，不展開演算法細節。
- 2025 到 2026 年的硬體新聞（冷卻劑、模組化架構）對初學者太細，先不寫。
