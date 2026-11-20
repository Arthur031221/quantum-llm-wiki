<!-- layout: title -->
<!-- sources: quantum-computer -->
# 量子電腦是什麼？

給完全沒學過量子力學的人的入門簡報

<p class="subtitle">內容全部來自這個專案的量子計算LLM Wiki，每張投影片右下角都標了出自哪幾頁wiki</p>

---

<!-- sources: quantum-computer -->
## 今天的學習目標

看完這份簡報，你應該能夠

1. 說出量子位元和一般位元差在哪裡
2. 用自己的話解釋疊加、測量和糾纏
3. 看懂一個兩步驟的量子電路
4. 說明Shor演算法為什麼讓密碼學家緊張
5. 知道量子電腦現在卡在哪裡

---

<!-- sources: quantum-computer, qubit -->
## 從位元說起

<div class="cols">
<div class="card">

### 古典位元

- 只能是0或1
- 讀取時不會改變它
- 電晶體的電壓高低就是一個位元

</div>
<div class="card accent">

### 量子位元qubit

- 可以處在0和1的疊加
- 一測量就會被改變
- 電子自旋、光子偏振都能當量子位元

</div>
</div>

量子電腦用量子態表示和處理資訊，量子位元就是它的基本單位。

---

<!-- sources: qubit, superposition-and-measurement -->
## 疊加有兩個振幅

一個量子位元的狀態寫成

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \qquad |\alpha|^2 + |\beta|^2 = 1$$

- $\alpha$和$\beta$叫機率振幅，可以是負數，也可以是複數
- 兩個都不是0，量子位元就處在疊加
- 通俗說法是「同時是0也是1」，正式的意思是兩個振幅都不為零
- 古典位元就是$\alpha$或$\beta$其中一個等於0的特例

---

<!-- sources: superposition-and-measurement -->
## 測量時機率是振幅的平方

照Born規則，測量$\alpha|0\rangle + \beta|1\rangle$時

- 得到0的機率是$|\alpha|^2$，測完狀態變成$|0\rangle$
- 得到1的機率是$|\beta|^2$，測完狀態變成$|1\rangle$
- 測完原本的疊加就沒了，所以測量不可逆

<div class="example">舉個例子，測量$\tfrac{1}{\sqrt2}|0\rangle + \tfrac{1}{\sqrt2}|1\rangle$時，$|\tfrac{1}{\sqrt2}|^2 = \tfrac12$，得到0和1的機率各一半。</div>

---

<!-- sources: superposition-and-measurement, quantum-algorithms -->
## 振幅會互相抵消，這叫干涉

- 機率一定是正的，振幅卻可以是負的
- 正負振幅加在一起會抵消，這叫破壞性干涉
- $|+\rangle$和$|-\rangle$直接測量看起來一樣，都是一半一半，只差一個正負號，經過Hadamard閘以後就會得到不同結果
- 量子演算法就是安排一連串操作，讓錯誤答案的振幅互相抵消，正確答案的振幅變大

---

<!-- sources: qubit, quantum-computer -->
## 每多一個量子位元，維度就加倍

| 量子位元數 | 需要記錄的振幅數 |
|---|---|
| 1 | 2 |
| 2 | 4，分別是$\lvert 00\rangle, \lvert 01\rangle, \lvert 10\rangle, \lvert 11\rangle$ |
| n | $2^n$ |
| 100 | $2^{100}$ |

用古典電腦記下100個量子位元的狀態得存$2^{100}$個數，古典電腦很難模擬量子電腦，原因就在這裡。

---

<!-- sources: entanglement -->
## 量子糾纏

兩個量子位元可以處在這個Bell態

$$|\Phi^+\rangle = \frac{1}{\sqrt2}\left(|00\rangle + |11\rangle\right)$$

- 測量時一半機率得到00，一半得到11，不會出現01或10
- Alice和Bob各拿一個，分開再遠，兩人的結果也一定相同
- 可是Alice控制不了自己會測到什麼，所以糾纏不能拿來超光速傳訊
- 1964年Bell提出可以檢驗的不等式，實驗結果違反了它，2022年的諾貝爾物理獎就頒給相關實驗

---

<!-- sources: quantum-gates -->
## 量子邏輯閘是作用在量子位元上的矩陣

<div class="cols">
<div class="card">

### X閘，量子版的NOT

$$X = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$$

把$|0\rangle$和$|1\rangle$互換

</div>
<div class="card">

### Hadamard閘，通常寫成H

$$H = \frac{1}{\sqrt2}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$$

把$|0\rangle$變成等量疊加$|+\rangle$

</div>
</div>

量子閘都是么正矩陣，一定可逆，測量不可逆，所以測量不算量子閘。

---

<!-- sources: quantum-gates, entanglement -->
## 第一個量子電路，做出糾纏

<div class="circuit">
<div class="wire"><span class="q">q₀ = |0⟩</span><span class="gate">H</span><span class="ctrl">●</span><span class="end"></span></div>
<div class="wire"><span class="q">q₁ = |0⟩</span><span class="gap"></span><span class="tgt">⊕</span><span class="end"></span></div>
</div>

1. 一開始是$|00\rangle$
2. 對q₀做H，變成$\frac{1}{\sqrt2}(|00\rangle + |10\rangle)$
3. 做CNOT，q₀是1時才翻轉q₁，所以$|10\rangle$變成$|11\rangle$
4. 結果是$\frac{1}{\sqrt2}(|00\rangle + |11\rangle)$，正好是上一張的Bell態

---

<!-- sources: quantum-algorithms -->
## 量子電腦會同時試所有答案嗎？

- 把輸入準備成疊加，輸出確實同時包含所有輸入的結果，這叫量子平行
- 可是最後一測量，只會拿到一個值
- 加速要靠干涉，放大正確答案，抵消錯誤答案
- Grover搜尋要在n個項目裡找一個，古典方法大約查n次，量子大約$\sqrt n$次
- Shor分解整數比已知最好的古典演算法快很多

---

<!-- sources: shor-algorithm -->
## Shor演算法為什麼讓密碼學家緊張

- RSA加密靠的是大整數很難分解
- 1994年Peter Shor提出量子演算法，能在多項式時間內分解整數
- 只要量子電腦夠大、雜訊夠小，RSA和Diffie-Hellman都能被破解
- 只有找週期那一步需要量子電腦，其他步驟用古典電腦
- 2001年IBM用7個量子位元把15分解成3 × 5，之後也只分解過21這種小數字
- 對策是後量子密碼學PQC，NIST正在制定標準

---

<!-- sources: decoherence-and-error-correction -->
## 最大的難題是退相干

- 量子位元跟環境互動，量子資訊就流到環境裡，疊加和糾纏跟著消失
- 每個操作都要趕在退相干之前做完，有些機器得冷卻到20 mK
- 宇宙射線也可能在幾毫秒內破壞量子態
- 對策是量子錯誤更正，用很多實體量子位元保護一個邏輯量子位元，像Shor code就用9個
- 代價很高，分解2,048位元的整數估計要300萬個實體量子位元、花5個月

<p class="note">打個比喻，相干性沒有消失，它混進了環境裡，就像摩擦把能量變成熱。</p>

---

<!-- sources: quantum-computer, shor-algorithm -->
## 量子電腦現在到哪裡了？

- 到2023年為止，所有實際應用上都還是古典電腦比較強
- 2019年Google宣稱用54個量子位元達成量子霸權，說超級電腦要算10,000年，IBM反駁說大約2.5天就能算完
- 量子霸權實驗挑的問題不一定有用，比較像科學研究上的進展
- 現在是有雜訊的中等規模量子電腦時代，簡稱NISQ，下一步是可以容錯的大型量子電腦
- 最有希望的應用是化學和材料這類量子模擬

---

<!-- sources: qubit, superposition-and-measurement, entanglement, quantum-gates -->
## 小測驗

<details><summary>1. 一個量子位元是$\tfrac{1}{\sqrt2}|0\rangle - \tfrac{1}{\sqrt2}|1\rangle$，測量得到1的機率是多少？</summary>機率是振幅的平方，$|-\tfrac{1}{\sqrt2}|^2 = \tfrac12$，負號不影響機率，可是會影響干涉。</details>

<details><summary>2. 3個量子位元的狀態需要幾個振幅來描述？</summary>需要$2^3 = 8$個，每多一個量子位元，數量就加倍。</details>

<details><summary>3. Alice和Bob共享Bell態，Alice測到0，Bob會測到什麼？他們能用這個方法傳訊息嗎？</summary>Bob一定測到0，可是Alice沒辦法決定自己測到0還是1，Bob單看自己的結果只是一串隨機的0和1，所以不能傳訊息。</details>

<details><summary>4. 為什麼測量不算量子邏輯閘？</summary>量子閘是么正矩陣，一定可逆，測量會讓狀態崩塌，原本的疊加資訊就消失了，沒辦法倒回去。</details>

---

<!-- sources: qubit, superposition-and-measurement, entanglement, quantum-gates, shor-algorithm, decoherence-and-error-correction -->
## 重點整理

1. 量子位元可以處在$|0\rangle$和$|1\rangle$的疊加，n個量子位元要$2^n$個振幅描述
2. 測量依Born規則隨機得到結果，機率是振幅的平方，測完疊加就消失
3. 糾纏讓測量結果完全相關，但不能拿來超光速傳訊
4. 量子閘是可逆的矩陣，H加CNOT就能做出糾纏
5. 加速來自干涉，Shor演算法威脅RSA，但需要的量子位元遠超過現有的機器
6. 退相干是最大的難題，錯誤更正有效，只是代價很高

---

<!-- sources: quantum-computer, qubit, superposition-and-measurement, entanglement, quantum-gates, quantum-algorithms, shor-algorithm, decoherence-and-error-correction -->
## 參考資料

這份簡報只用了下面這些wiki頁面，它們整理自6篇英文維基百科條目，授權是CC BY-SA 4.0。

- [量子電腦](wiki.html#quantum-computer)、[量子位元](wiki.html#qubit)、[疊加與測量](wiki.html#superposition-and-measurement)、[量子糾纏](wiki.html#entanglement)
- [量子邏輯閘](wiki.html#quantum-gates)、[量子演算法與加速](wiki.html#quantum-algorithms)、[Shor演算法](wiki.html#shor-algorithm)、[退相干與錯誤更正](wiki.html#decoherence-and-error-correction)
- 原始條目是Quantum computing、Qubit、Quantum entanglement、Quantum logic gate、Shor's algorithm和Quantum decoherence
- 流程和檢查紀錄放在[workflow.html](workflow.html)
