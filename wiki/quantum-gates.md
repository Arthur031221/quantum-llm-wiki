---
title: 量子邏輯閘
summary: 作用在量子位元上的可逆操作，用么正矩陣表示，是量子電路的積木。
sources: [04-quantum-logic-gate, 01-quantum-computing, 02-qubit]
---

# 量子邏輯閘（Quantum logic gate）

量子邏輯閘（簡稱量子閘）是量子電路的積木，作用在一個或少數幾個[量子位元](qubit.md)上，角色就像數位電路裡的古典邏輯閘。

## 量子閘就是矩陣

量子態是向量，量子閘是矩陣，套用一個閘就是做矩陣乘法。作用在 n 個量子位元上的閘是 $2^n \times 2^n$ 的么正矩陣（unitary matrix）。

么正矩陣一定有反矩陣，所以量子閘都是可逆的。很多古典邏輯閘不可逆，這是兩者的一個差別。可逆的 Toffoli 閘能做出所有布林函數，而且有量子版本，所以古典電路能做的運算，量子電路都能做。

## 常見的單一量子位元閘

X 閘（Pauli-X）是量子版的 NOT，把 $|0⟩$ 和 $|1⟩$ 互換：

$$X = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \qquad X|0⟩ = |1⟩, \quad X|1⟩ = |0⟩$$

Z 閘保持 $|0⟩$ 不變，把 $|1⟩$ 變成 $-|1⟩$，所以叫相位翻轉（phase-flip）。

Hadamard 閘（H）把基底態變成等量疊加：

$$H = \frac{1}{\sqrt2}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}, \qquad H|0⟩ = |+⟩, \quad H|1⟩ = |-⟩$$

$|+⟩$、$|-⟩$ 的定義見[疊加與測量](superposition-and-measurement.md)。

## 兩個量子位元的閘：CNOT

CNOT（controlled NOT）有一個控制位元和一個目標位元。控制位元是 $|1⟩$ 時，翻轉目標位元；控制位元是 $|0⟩$ 時，什麼都不做：

| 輸入 | 輸出 |
|---|---|
| $\lvert 00\rangle$ | $\lvert 00\rangle$ |
| $\lvert 01\rangle$ | $\lvert 01\rangle$ |
| $\lvert 10\rangle$ | $\lvert 11\rangle$ |
| $\lvert 11\rangle$ | $\lvert 10\rangle$ |

## 第一個量子電路：做出 Bell 態

1. 兩個量子位元都從 $|0⟩$ 開始：$|00⟩$。
2. 對第一個量子位元做 H：得到 $\frac{1}{\sqrt2}(|00⟩ + |10⟩)$。
3. 以第一個為控制、第二個為目標做 CNOT：$|10⟩$ 變成 $|11⟩$，結果是 $\frac{1}{\sqrt2}(|00⟩ + |11⟩)$。

這就是[量子糾纏](entanglement.md)頁的 Bell 態 $|\Phi^+⟩$。

## 通用閘組

一組閘如果能組合出（或任意逼近）量子電腦上的所有操作，就叫通用閘組。例如 {CNOT, H, S} 再加上 T 閘，或 Toffoli 閘加 Hadamard 閘。

## 測量不是量子閘

測量會讓狀態崩塌到某個結果，不可逆，所以不算量子閘。量子電路通常把測量放在最後，詳見[疊加與測量](superposition-and-measurement.md)。

## 真實硬體

理想的量子閘是精確的，但真實硬體有誤差，每做一個閘都會帶進一點錯誤，量子態的保真度會隨時間下降（見[退相干與錯誤更正](decoherence-and-error-correction.md)）。
