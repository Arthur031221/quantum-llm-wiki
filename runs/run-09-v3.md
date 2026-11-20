# Run 09（graph v3）

- 時間：2026-11-20 16:31:02
- 節點順序：test_checks → fetch → discuss → ingest → lint_wiki → review_claims → plan_outline → check_outline → build_slides → check_build
- 這次的變更：重審文字修飾改寫的 4 句後重跑

| # | 節點 | 類型 | 結果 | 耗時 |
|---|---|---|---|---|
| 1 | test_checks | 腳本 | 通過 | 0.03s |
| 2 | fetch | 腳本 | 通過 | 0.03s |
| 3 | discuss | LLM | 通過 | 0.00s |
| 4 | ingest | LLM | 通過 | 0.00s |
| 5 | lint_wiki | 腳本 | 通過 | 0.04s |
| 6 | review_claims | LLM | 通過 | 0.00s |
| 7 | plan_outline | LLM | 通過 | 0.00s |
| 8 | check_outline | 腳本 | 通過 | 0.02s |
| 9 | build_slides | 腳本 | 通過 | 0.02s |
| 10 | check_build | 腳本 | 通過 | 0.02s |

**結果：通過**

## 各節點輸出

### 1. test_checks

```
ok   預期擋下：2019 年 Google 用 53 個量子位元
ok   預期通過：2019 年 Google 用 54 個量子位元
ok   預期通過：需要 300 萬個實體量子位元
ok   預期擋下：需要 400 萬個實體量子位元
ok   預期通過：超級電腦要算 10,000 年
ok   預期通過：一半機率得到 $|11⟩$
ok   預期擋下：版本號 1386685712
test_checks：7/7 通過
```

### 2. fetch

```
skip  01-quantum-computing.md（已存在）
skip  02-qubit.md（已存在）
skip  03-quantum-entanglement.md（已存在）
skip  04-quantum-logic-gate.md（已存在）
skip  05-shors-algorithm.md（已存在）
skip  06-quantum-decoherence.md（已存在）
manifest.json：6 個來源
```

### 3. discuss

```
6 篇來源都有討論紀錄
```

### 4. ingest

```
wiki 頁面 8 個，index.md 與 log.md 存在
```

### 5. lint_wiki

```
wiki/decoherence-and-error-correction.md「20」 ← um computers require their qubits to be cooled to 20 millikelvin (usually using a dilution refrigerato
wiki/decoherence-and-error-correction.md「2020」 ← ic interference. Shielding cosmic rays: In August 2020 scientists reported that ionizing radiation from 
wiki/decoherence-and-error-correction.md「2048」 ← at least 3 million physical qubits would factor a 2048-bit integer in 5 months on a fully error-correcte
wiki/decoherence-and-error-correction.md「300萬」 ← orders of magnitude. Estimates show that at least 3 million physical qubits would factor a 2048-bit integer i
wiki/entanglement.md「11」 ← states and weakly entangled states like |00⟩+0.01|11⟩) and the separable ones (i.e., product states li
wiki/entanglement.md「1203」 ← ing a new quantum entanglement distance record of 1203 km, demonstrating the survival of a two-photon pa
wiki/entanglement.md「1935」 ← information. Such phenomena were the subject of a 1935 paper by Albert Einstein, Boris Podolsky, and Nat
wiki/entanglement.md「1964」 ← hed for decades after his paper was published. In 1964 John S. Bell demonstrated an upper limit, seen in
wiki/entanglement.md「1972」 ← ering work of Stuart Freedman and John Clauser in 1972, and Alain Aspect's experiments in 1982. While Be
wiki/entanglement.md「1982」 ← lauser in 1972, and Alain Aspect's experiments in 1982. While Bell actively discouraged students from pu
wiki/entanglement.md「2017」 ← er—than the interval between the measurements. In 2017, Yin et al. reported setting a new quantum entang
wiki/entanglement.md「2022」 ← e quantum cryptography with entangled photons. In 2022, the Nobel Prize in Physics was awarded to Aspect
wiki/quantum-algorithms.md「128」 ← le security against such an attack to that of AES-128 against classical brute-force search. Post-quantu
wiki/quantum-algorithms.md「2023」 ←  such as the reactions inside a collider. In June 2023, IBM computer scientists reported that a quantum 
wiki/quantum-algorithms.md「256」 ← symmetric key lengths are effectively halved: AES-256 would have comparable security against such an at
wiki/quantum-computer.md「10000」 ←  classical supercomputers would take an estimated 10000 years to complete—a claim subsequently disputed b
wiki/quantum-computer.md「1980」 ← hanics and computer science began to converge. In 1980, Paul Benioff introduced the quantum Turing machi
wiki/quantum-computer.md「1994」 ← irani algorithm in 1993, and Simon's algorithm in 1994. These algorithms did not solve practical problem
wiki/quantum-computer.md「1996」 ← algorithm drew attention to quantum computing. In 1996, Grover's algorithm established a quantum speedup
wiki/quantum-computer.md「1998」 ← puters using trapped ions and superconductors. In 1998, a two-qubit quantum computer demonstrated techni
wiki/quantum-computer.md「2019」 ←  the number of qubits and reduced error rates. In 2019, Google AI and NASA announced that they had achie
wiki/quantum-computer.md「2023」 ←  such as the reactions inside a collider. In June 2023, IBM computer scientists reported that a quantum 
wiki/quantum-computer.md「2024」 ←  decoherence through quantum error correction. In 2024, researchers demonstrated approaches for high thr
wiki/quantum-computer.md「54」 ← d that they had achieved quantum supremacy with a 54-qubit machine, performing a computation that clas
wiki/qubit.md「100」 ← omputer to simulate a quantum one: representing a 100-qubit system requires storing 2100 classical valu
wiki/qubit.md「1995」 ← enjamin Schumacher. In the acknowledgments of his 1995 paper, Schumacher states that the term qubit was 
wiki/shor-algorithm.md「15」 ←  was demonstrated by a group at IBM, who factored 15 into 3×5, using an NMR implementation of a quantu
wiki/shor-algorithm.md「1994」 ←  prime factors of an integer. It was developed in 1994 by the American mathematician Peter Shor. It is o
wiki/shor-algorithm.md「2001」 ← and have only succeeded with small semiprimes. In 2001, Shor's algorithm was demonstrated by a group at 
wiki/shor-algorithm.md「2012」 ← mented Shor's algorithm using photonic qubits. In 2012, the factorization of 15 was performed with solid
wiki/shor-algorithm.md「2016」 ← in 2012, the factorization of 21 was achieved. In 2016, the factorization of 15 was performed again usin
wiki/shor-algorithm.md「2026」 ← hy (PQC).   === Physical implementation === As of 2026, the high error rates of quantum computers and li
wiki/shor-algorithm.md「2048」 ← at least 3 million physical qubits would factor a 2048-bit integer in 5 months on a fully error-correcte
wiki/shor-algorithm.md「21」 ← tate qubits. Later, in 2012, the factorization of 21 was achieved. In 2016, the factorization of 15 wa
wiki/shor-algorithm.md「300」 ←  of a few prime numbers (e.g., the product of two 300-digit primes). By contrast, a quantum computer co
wiki/shor-algorithm.md「300萬」 ← orders of magnitude. Estimates show that at least 3 million physical qubits would factor a 2048-bit integer i
lint_wiki：通過（8 個 wiki 頁面）
```

### 6. review_claims

```
review-claims.md 存在、比 wiki 新、結論為通過
```

### 7. plan_outline

```
slides/outline.md 存在
```

### 8. check_outline

```
check_outline：17 張投影片，0 個問題
```

### 9. build_slides

```
build_slides：產生 slides.html（17 張）與 slides/slide-map.json
```

### 10. check_build

```
check_build：17 張投影片，0 個問題
```

