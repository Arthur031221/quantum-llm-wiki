# 討論：Quantum logic gate

來源：raw/04-quantum-logic-gate.md（英文維基百科，rev 1376542851）

## 1. 這篇在講什麼

量子邏輯閘的定義與矩陣表示、常見的閘（Pauli、Hadamard、CNOT、Toffoli）、通用閘組，以及為什麼測量不算量子閘。

## 2. 初學者需要的重點

- 量子閘是量子電路的積木，作用在少數幾個量子位元上（導言）。
- 量子閘是么正矩陣，一定可逆；很多古典邏輯閘不可逆（導言）。
- X 閘是量子版的 NOT，把 |0⟩ 和 |1⟩ 互換（Pauli gates）。
- Hadamard 閘把 |0⟩ 變成等量疊加 $(|0⟩+|1⟩)/\sqrt2$（Hadamard gate）。
- CNOT：第一個量子位元是 |1⟩ 時才翻轉第二個（Controlled gates）。
- 測量不可逆，所以不是量子閘；測量依 Born 規則隨機投影到某個基底態（Measurement）。

## 3. 要寫進哪些 wiki 頁面

- 新增 `quantum-gates.md`：閘是什麼、可逆性、X／H／CNOT、通用閘組、簡單電路（H 加 CNOT 做出 Bell 態）。
- 補充 `superposition-and-measurement.md`：Born 規則、測量後狀態崩塌、所有結果機率總和為 1。

## 4. 疑點與決定

- 原文矩陣在純文字裡被壓成「[0110]」這種樣子，寫 wiki 時要重寫成 2×2 矩陣。
- Toffoli 閘、Solovay–Kitaev 定理只寫一句（Toffoli 證明量子電路能做所有古典運算），不展開。
- Hadamard 矩陣原文的「12」是 $1/\sqrt2$，同樣要還原。
