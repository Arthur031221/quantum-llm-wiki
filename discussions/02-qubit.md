# 討論：Qubit

來源：raw/02-qubit.md（英文維基百科，rev 1385056994）

## 1. 這篇在講什麼

量子位元的定義、數學表示、布洛赫球、對量子位元能做的操作，以及兩個量子位元如何形成糾纏。

## 2. 初學者需要的重點

- 量子位元是量子資訊的基本單位，可以用任何二能階系統實現，例如電子自旋、光子偏振（導言）。
- 古典位元只能是 0 或 1；量子位元可以處在 |0⟩ 和 |1⟩ 的疊加（Comparison with classical bits）。
- 測量會破壞疊加，古典位元被讀取時則不受影響（Comparison with classical bits）。
- n 個量子位元需要 $2^n$ 個複數描述（Comparison with classical bits）。
- 布洛赫球：古典位元只能在北極或南極，純量子態可以是球面上任一點（Bloch sphere representation）。
- 用 CNOT 可以把兩個量子位元做成 Bell 態 $\frac{1}{\sqrt2}(|00⟩+|11⟩)$（Controlled gate to construct the Bell state）。

## 3. 要寫進哪些 wiki 頁面

- 新增 `qubit.md`：定義、與古典位元比較、實體例子、布洛赫球、n 個量子位元。
- 補充 `superposition-and-measurement.md`：測量的不可逆性、測量後振幅改變。
- 補充 `entanglement.md`：Bell 態與 Alice、Bob 的例子。
- 補充 `quantum-gates.md`：CNOT 產生 Bell 態的步驟。

## 4. 疑點與決定

- 原文 Bell 態寫成「12(|00⟩+|11⟩)」，係數是 $1/\sqrt{2}$，抽取時根號和分數線遺失，寫 wiki 時要還原。
- 「量子位元可以同時是 0 和 1」是通俗說法，原文也標明是 popularly expressed。wiki 會寫出這是通俗說法，正式說法是兩個振幅都不為零。
- 混合態、Hopf 座標對初學者太深，只用一句話帶過混合態，不寫座標推導。
