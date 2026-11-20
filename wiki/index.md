# 量子計算 LLM Wiki 目錄

給初學者的量子計算知識庫。每頁都整理自 `raw/` 的維基百科來源，來源列在每頁開頭。建議閱讀順序由上到下。

## 基礎概念

- [量子電腦](quantum-computer.md)：用量子態表示和處理資訊的電腦，目前仍在實驗階段。
- [量子位元](qubit.md)：量子資訊的基本單位，可以處在 |0⟩ 和 |1⟩ 的疊加。
- [疊加與測量](superposition-and-measurement.md)：量子位元可以處在疊加，測量時依 Born 規則隨機得到一個結果。
- [量子糾纏](entanglement.md)：多個粒子的量子態無法分開描述，測量結果可以完全相關，但不能拿來超光速傳訊。

## 怎麼計算

- [量子邏輯閘](quantum-gates.md)：作用在量子位元上的可逆操作，用么正矩陣表示，是量子電路的積木。
- [量子演算法與加速](quantum-algorithms.md)：量子演算法靠干涉放大正確答案；Shor 有超多項式加速，Grover 有平方加速。
- [Shor 演算法](shor-algorithm.md)：1994 年提出的量子整數分解演算法，理論上能破解 RSA，但目前的硬體還差很遠。

## 難題

- [退相干與錯誤更正](decoherence-and-error-correction.md)：量子位元和環境互動會失去量子特性，這是量子電腦最大的難題；錯誤更正能對抗它，但代價很高。

## 來源

| id | 條目 |
|---|---|
| 01-quantum-computing | Quantum computing |
| 02-qubit | Qubit |
| 03-quantum-entanglement | Quantum entanglement |
| 04-quantum-logic-gate | Quantum logic gate |
| 05-shors-algorithm | Shor's algorithm |
| 06-quantum-decoherence | Quantum decoherence |
