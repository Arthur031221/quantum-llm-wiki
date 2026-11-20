# 討論Qubit

來源是raw/02-qubit.md，英文維基百科版本1385056994。

## 1. 這篇在講什麼

講量子位元的定義和數學表示、布洛赫球、對量子位元能做哪些操作，最後講兩個量子位元怎麼形成糾纏。

## 2. 初學者需要的重點

- 量子位元是量子資訊的基本單位，任何二能階系統都能拿來實現，像電子自旋或光子偏振，出自導言
- 古典位元只能是0或1，量子位元可以處在|0⟩和|1⟩的疊加，出自Comparison with classical bits
- 測量會破壞疊加，古典位元被讀取時則不受影響，同一節
- n個量子位元需要$2^n$個複數才描述得完，同一節
- 在布洛赫球上，古典位元只能待在北極或南極，純量子態可以是球面上任何一點，出自Bloch sphere representation
- 用CNOT可以把兩個量子位元做成Bell態$\frac{1}{\sqrt2}(|00⟩+|11⟩)$，出自Controlled gate to construct the Bell state

## 3. 要寫進哪些wiki頁面

- 新增`qubit.md`，寫定義、和古典位元的比較、實體例子、布洛赫球和多個量子位元
- 補充`superposition-and-measurement.md`，寫測量為什麼不可逆，以及測量後振幅怎麼變
- 補充`entanglement.md`，放Bell態和Alice、Bob的例子
- 補充`quantum-gates.md`，寫CNOT怎麼做出Bell態

## 4. 疑點與決定

- 原文的Bell態被抽成「12(|00⟩+|11⟩)」，係數應該是$1/\sqrt{2}$，根號和分數線在抽取時掉了，寫wiki時要還原
- 「量子位元可以同時是0和1」是通俗說法，原文也註明是popularly expressed，wiki會交代這是通俗說法，正式的意思是兩個振幅都不為零
- 混合態和Hopf座標對初學者太深，混合態只用一句話帶過，座標推導不寫
