---
title: 量子邏輯閘
summary: 作用在量子位元上的可逆操作，用么正矩陣表示，是量子電路的積木。
sources: [04-quantum-logic-gate, 01-quantum-computing, 02-qubit]
---

# 量子邏輯閘

量子邏輯閘簡稱量子閘，是量子電路的積木，作用在一個或少數幾個[量子位元](qubit.md)上，角色就像數位電路裡的古典邏輯閘。

## 量子閘就是矩陣

量子態是向量，量子閘是矩陣，套用一個閘就等於做一次矩陣乘法，作用在n個量子位元上的閘是$2^n \times 2^n$的么正矩陣。

么正矩陣一定有反矩陣，所以量子閘全都可逆，很多古典邏輯閘卻不可逆，這是兩邊的一個差別，可逆的Toffoli閘能做出所有布林函數，而且有量子版本，所以古典電路能做的運算，量子電路也都做得到。

## 常見的單一量子位元閘

X閘又叫Pauli-X，是量子版的NOT，會把$|0⟩$和$|1⟩$互換。

$$X = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \qquad X|0⟩ = |1⟩, \quad X|1⟩ = |0⟩$$

Z閘讓$|0⟩$保持不變，把$|1⟩$變成$-|1⟩$，所以又叫相位翻轉。

Hadamard閘通常寫成H，會把基底態變成等量疊加，$|+⟩$和$|-⟩$的定義在[疊加與測量](superposition-and-measurement.md)那頁。

$$H = \frac{1}{\sqrt2}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}, \qquad H|0⟩ = |+⟩, \quad H|1⟩ = |-⟩$$

## 兩個量子位元的閘CNOT

CNOT是controlled NOT的縮寫，有一個控制位元和一個目標位元，控制位元是$|1⟩$時翻轉目標位元，是$|0⟩$時什麼都不做。

| 輸入 | 輸出 |
|---|---|
| $\lvert 00\rangle$ | $\lvert 00\rangle$ |
| $\lvert 01\rangle$ | $\lvert 01\rangle$ |
| $\lvert 10\rangle$ | $\lvert 11\rangle$ |
| $\lvert 11\rangle$ | $\lvert 10\rangle$ |

## 第一個量子電路，做出Bell態

1. 兩個量子位元都從$|0⟩$開始，合起來是$|00⟩$
2. 對第一個量子位元做H，得到$\frac{1}{\sqrt2}(|00⟩ + |10⟩)$
3. 以第一個當控制、第二個當目標做CNOT，$|10⟩$變成$|11⟩$，結果是$\frac{1}{\sqrt2}(|00⟩ + |11⟩)$

最後得到的就是[量子糾纏](entanglement.md)那頁的Bell態$|\Phi^+⟩$。

## 通用閘組

一組閘如果能組合出量子電腦上的所有操作，或是能任意逼近它們，就叫通用閘組，例如CNOT、H、S再加上T閘，或是Toffoli閘加Hadamard閘。

## 測量不算量子閘

測量會讓狀態崩塌到某個結果，沒辦法倒回去，所以不算量子閘，量子電路通常把測量放在最後，詳細的說明在[疊加與測量](superposition-and-measurement.md)那頁。

## 真實硬體

理想的量子閘是精確的，真實硬體卻有誤差，每做一個閘都會帶進一點錯誤，量子態的保真度也會隨時間下降，相關內容在[退相干與錯誤更正](decoherence-and-error-correction.md)那頁。
