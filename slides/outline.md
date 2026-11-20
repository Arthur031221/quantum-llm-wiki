<!-- layout: title -->
<!-- sources: quantum-computer -->
# 量子電腦是什麼？

給完全沒學過量子力學的人的入門簡報

<p class="subtitle">內容全部來自本專案的量子計算 LLM Wiki・每張投影片右下角都標了 wiki 來源</p>

---

<!-- sources: quantum-computer -->
## 今天的學習目標

看完這份簡報，你應該能夠：

1. 說出量子位元和一般位元差在哪裡
2. 用自己的話解釋疊加、測量、糾纏
3. 看懂一個兩步驟的量子電路
4. 說明 Shor 演算法為什麼讓密碼學家緊張
5. 知道量子電腦現在卡在哪裡

---

<!-- sources: quantum-computer, qubit -->
## 從位元說起

<div class="cols">
<div class="card">

### 古典位元

- 只能是 0 或 1
- 讀取時不會改變它
- 電晶體的電壓高低就是一個位元

</div>
<div class="card accent">

### 量子位元（qubit）

- 可以處在 0 和 1 的疊加
- 一測量就會被改變
- 電子自旋、光子偏振都能當量子位元

</div>
</div>

量子電腦用量子態表示和處理資訊，基本單位就是量子位元。

---

<!-- sources: qubit, superposition-and-measurement -->
## 疊加：兩個振幅

一個量子位元的狀態寫成

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \qquad |\alpha|^2 + |\beta|^2 = 1$$

- $\alpha$、$\beta$ 叫機率振幅，可以是負數，也可以是複數
- 兩個都不是 0，量子位元就處在疊加
- 通俗說法是「同時是 0 也是 1」，正式的意思是兩個振幅都不為零
- 古典位元就是 $\alpha$ 或 $\beta$ 其中一個等於 0 的特例

---

<!-- sources: superposition-and-measurement -->
## 測量：機率是振幅的平方

測量 $\alpha|0\rangle + \beta|1\rangle$ 時（Born 規則）：

- 得到 0 的機率是 $|\alpha|^2$，之後狀態變成 $|0\rangle$
- 得到 1 的機率是 $|\beta|^2$，之後狀態變成 $|1\rangle$
- 測量後原本的疊加就沒了，所以測量不可逆

<div class="example">例子：測量 $\tfrac{1}{\sqrt2}|0\rangle + \tfrac{1}{\sqrt2}|1\rangle$，$|\tfrac{1}{\sqrt2}|^2 = \tfrac12$，得到 0 和 1 的機率各一半。</div>

---

<!-- sources: superposition-and-measurement, quantum-algorithms -->
## 振幅可以互相抵消：干涉

- 機率一定是正的，振幅可以是負的
- 正負振幅相加會抵消，這叫破壞性干涉
- $|+\rangle$ 和 $|-\rangle$ 直接測量看起來一樣，都是一半一半，只差一個正負號；經過 Hadamard 閘後會得到不同結果
- 量子演算法的做法：安排操作，讓錯誤答案的振幅互相抵消，正確答案的振幅變大

---

<!-- sources: qubit, quantum-computer -->
## 多個量子位元：每多一個，維度加倍

| 量子位元數 | 需要記錄的振幅數 |
|---|---|
| 1 | 2 |
| 2 | 4（$\lvert 00\rangle, \lvert 01\rangle, \lvert 10\rangle, \lvert 11\rangle$） |
| n | $2^n$ |
| 100 | $2^{100}$ |

用古典電腦記下 100 個量子位元的狀態，要存 $2^{100}$ 個數。這就是古典電腦很難模擬量子電腦的原因。

---

<!-- sources: entanglement -->
## 量子糾纏

兩個量子位元的 Bell 態：

$$|\Phi^+\rangle = \frac{1}{\sqrt2}\left(|00\rangle + |11\rangle\right)$$

- 測量時一半機率得到 00、一半得到 11，不會出現 01 或 10
- Alice 和 Bob 各拿一個，分開再遠，兩人的結果也一定相同
- 但 Alice 控制不了自己測到什麼，所以糾纏不能拿來超光速傳訊
- 1964 年 Bell 提出可檢驗的不等式，實驗結果違反它；2022 年諾貝爾物理獎頒給相關實驗

---

<!-- sources: quantum-gates -->
## 量子邏輯閘：作用在量子位元上的矩陣

<div class="cols">
<div class="card">

### X 閘（量子 NOT）

$$X = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$$

把 $|0\rangle$ 和 $|1\rangle$ 互換

</div>
<div class="card">

### Hadamard 閘（H）

$$H = \frac{1}{\sqrt2}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$$

把 $|0\rangle$ 變成等量疊加 $|+\rangle$

</div>
</div>

量子閘都是么正矩陣，一定可逆。測量不可逆，所以測量不算量子閘。

---

<!-- sources: quantum-gates, entanglement -->
## 第一個量子電路：做出糾纏

<div class="circuit">
<div class="wire"><span class="q">q₀ = |0⟩</span><span class="gate">H</span><span class="ctrl">●</span><span class="end">─</span></div>
<div class="wire"><span class="q">q₁ = |0⟩</span><span class="gap"></span><span class="tgt">⊕</span><span class="end">─</span></div>
</div>

1. 開始：$|00\rangle$
2. 對 q₀ 做 H：$\frac{1}{\sqrt2}(|00\rangle + |10\rangle)$
3. CNOT（q₀ 是 1 才翻轉 q₁）：$|10\rangle$ 變成 $|11\rangle$
4. 結果：$\frac{1}{\sqrt2}(|00\rangle + |11\rangle)$，就是上一張的 Bell 態

---

<!-- sources: quantum-algorithms -->
## 量子電腦會同時試所有答案嗎？

- 把輸入準備成疊加，輸出的確同時包含所有輸入的結果，這叫量子平行
- 可是最後一測量，只會拿到一個值
- 加速要靠干涉：放大正確答案、抵消錯誤答案
- Grover 搜尋：n 個項目裡找一個，古典約 n 次，量子約 $\sqrt n$ 次
- Shor 分解整數：比已知最好的古典演算法快很多

---

<!-- sources: shor-algorithm -->
## Shor 演算法：為什麼密碼學家緊張

- RSA 加密靠的是「大整數很難分解」
- 1994 年 Peter Shor 提出量子演算法，能在多項式時間內分解整數
- 只要量子電腦夠大、雜訊夠小，就能破解 RSA 和 Diffie–Hellman
- 只有「找週期」這一步需要量子電腦，其他步驟用古典電腦
- 現在：2001 年 IBM 用 7 個量子位元把 15 分解成 3 × 5，之後也只分解過 21 這種小數字
- 對策：後量子密碼學（PQC），NIST 正在制定標準

---

<!-- sources: decoherence-and-error-correction -->
## 最大的難題：退相干

- 量子位元跟環境互動，量子資訊就流到環境裡，疊加和糾纏跟著消失
- 每個操作都要在退相干之前做完，有些機器要冷卻到 20 mK
- 宇宙射線也可能在幾毫秒內破壞量子態
- 對策是量子錯誤更正：用很多實體量子位元保護一個邏輯量子位元，例如 Shor code 用 9 個
- 代價：分解 2,048 位元的整數，估計要 300 萬個實體量子位元、5 個月

<p class="note">比喻：相干性沒有消失，就像摩擦把能量變成熱，它混進了環境裡。</p>

---

<!-- sources: quantum-computer, shor-algorithm -->
## 量子電腦現在到哪裡了？

- 到 2023 年，所有實際應用上古典電腦仍然比較強
- 2019 年 Google 宣稱用 54 個量子位元達成量子霸權，說超級電腦要算 10,000 年；IBM 反駁說約 2.5 天就能算完
- 量子霸權實驗挑的問題不一定有用，比較像科學里程碑
- 現在是 NISQ（有雜訊的中等規模）時代，下一步是可以容錯的大型量子電腦
- 最有希望的應用：量子模擬（化學、材料）

---

<!-- sources: qubit, superposition-and-measurement, entanglement, quantum-gates -->
## 小測驗

<details><summary>1. 一個量子位元是 $\tfrac{1}{\sqrt2}|0\rangle - \tfrac{1}{\sqrt2}|1\rangle$，測量得到 1 的機率是多少？</summary>機率是振幅的平方：$|-\tfrac{1}{\sqrt2}|^2 = \tfrac12$。負號不影響機率，但會影響干涉。</details>

<details><summary>2. 3 個量子位元的狀態需要幾個振幅來描述？</summary>$2^3 = 8$ 個。每多一個量子位元，數量加倍。</details>

<details><summary>3. Alice 和 Bob 共享 Bell 態，Alice 測到 0。Bob 會測到什麼？他們能用這個方法傳訊息嗎？</summary>Bob 一定測到 0。但 Alice 沒辦法決定自己測到 0 還是 1，Bob 單看自己的結果只是隨機的 0 和 1，所以不能傳訊息。</details>

<details><summary>4. 為什麼測量不算量子邏輯閘？</summary>量子閘是么正矩陣，一定可逆；測量會讓狀態崩塌，原本的疊加資訊消失，不可逆。</details>

---

<!-- sources: qubit, superposition-and-measurement, entanglement, quantum-gates, shor-algorithm, decoherence-and-error-correction -->
## 重點整理

1. 量子位元可以處在 $|0\rangle$、$|1\rangle$ 的疊加，n 個量子位元要 $2^n$ 個振幅描述
2. 測量依 Born 規則隨機得到結果，機率是振幅的平方，測量後疊加消失
3. 糾纏讓測量結果完全相關，但不能超光速傳訊
4. 量子閘是可逆的矩陣；H 加 CNOT 就能做出糾纏
5. 加速來自干涉；Shor 演算法威脅 RSA，但需要的量子位元遠超過現有機器
6. 退相干是最大難題，錯誤更正有效但代價很高

---

<!-- sources: quantum-computer, qubit, superposition-and-measurement, entanglement, quantum-gates, quantum-algorithms, shor-algorithm, decoherence-and-error-correction -->
## 參考資料

這份簡報只使用下列 wiki 頁面，wiki 頁面整理自 6 篇英文維基百科條目（CC BY-SA 4.0）。

- [量子電腦](wiki.html#quantum-computer)、[量子位元](wiki.html#qubit)、[疊加與測量](wiki.html#superposition-and-measurement)、[量子糾纏](wiki.html#entanglement)
- [量子邏輯閘](wiki.html#quantum-gates)、[量子演算法與加速](wiki.html#quantum-algorithms)、[Shor 演算法](wiki.html#shor-algorithm)、[退相干與錯誤更正](wiki.html#decoherence-and-error-correction)
- 原始來源：Quantum computing、Qubit、Quantum entanglement、Quantum logic gate、Shor's algorithm、Quantum decoherence
- 流程與檢查紀錄：[workflow.html](workflow.html)
