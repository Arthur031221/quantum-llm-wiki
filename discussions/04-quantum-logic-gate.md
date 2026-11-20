# 討論Quantum logic gate

來源是raw/04-quantum-logic-gate.md，英文維基百科版本1376542851。

## 1. 這篇在講什麼

講量子邏輯閘的定義和矩陣表示，介紹Pauli、Hadamard、CNOT和Toffoli這些常見的閘，再談通用閘組，最後說明測量為什麼不算量子閘。

## 2. 初學者需要的重點

- 量子閘是量子電路的積木，作用在少數幾個量子位元上，出自導言
- 量子閘是么正矩陣，一定可逆，很多古典邏輯閘卻不可逆，同樣出自導言
- X閘是量子版的NOT，會把|0⟩和|1⟩互換，出自Pauli gates
- Hadamard閘把|0⟩變成等量疊加$(|0⟩+|1⟩)/\sqrt2$，出自Hadamard gate
- CNOT只在第一個量子位元是|1⟩時翻轉第二個，出自Controlled gates
- 測量不可逆，所以不算量子閘，它會依Born規則隨機投影到某個基底態，出自Measurement

## 3. 要寫進哪些wiki頁面

- 新增`quantum-gates.md`，寫閘是什麼、為什麼可逆、X和H和CNOT三種閘、通用閘組，再放一個用H加CNOT做出Bell態的簡單電路
- 補充`superposition-and-measurement.md`，寫Born規則、測量後狀態崩塌，以及所有結果的機率加起來是1

## 4. 疑點與決定

- 矩陣在純文字裡被壓成「[0110]」這種樣子，寫wiki時要重新排成2×2矩陣
- Toffoli閘和Solovay-Kitaev定理只寫一句，提到Toffoli代表量子電路能做所有古典運算就好，不展開
- Hadamard矩陣原文的「12」是$1/\sqrt2$，一樣要還原
