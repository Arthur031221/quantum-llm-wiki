# review_claims逐頁核對wiki的說法

這是review_claims節點的紀錄，由LLM在run 05之後完成，做法是逐頁讀wiki，把每個沒有數字的說法拿回該頁`sources`列出的raw檔找出處，數字已經由lint_wiki比對過，這裡不重複，找不到出處的，或是出處在別的來源但這頁沒列的，都算問題。

## 第一次審查的結果

| 頁面 | 問題數 | 處理 |
|---|---|---|
| quantum-computer | 0 | |
| qubit | 1 | Schumacher命名的說法不精確，照原文改寫 |
| superposition-and-measurement | 2 | 「仍有爭論」來源沒寫，刪掉，「環境像在測量」出自沒列出的來源，改寫 |
| entanglement | 0 | |
| quantum-gates | 1 | 「例如AND不可逆」來源沒寫，刪掉這個例子 |
| quantum-algorithms | 0 | |
| shor-algorithm | 1 | 「最好的」古典演算法改成原文的「擴展性最好的」 |
| decoherence-and-error-correction | 0 | |
| 合計 | 5 | 全部已修正 |

5個問題全都出在ingest，LLM會順手補上自己知道而且大致正確的說法，像AND不可逆、測量問題有爭論，或是把原文的程度詞換成更強的詞，像把most scalable寫成「最好的」，這些句子都沒有數字，所以lint_wiki全部放行。

其中「環境像在測量」那一句，內容在別的來源找得到，錯在這頁的sources沒列那篇，這種來源標錯頁的問題，數字比對同樣抓不到。

結論：通過，5個問題已在wiki中修正

## 第二次審查，run 08之後

文字修飾改了4句wiki，逐句回原文確認，4句都找得到出處。

| 頁面 | 改寫後的句子 | 原文出處 |
|---|---|---|
| quantum-computer | 古典電腦裡的半導體也靠量子效應運作 | 01的Quantum information processing，semiconductors may rely on quantum behavior |
| quantum-computer | 做法是設計演算法，讓干涉放大正確答案的機率 | 01的導言，wave interference effects amplify the probability of the desired measurement result |
| decoherence-and-error-correction | 相干性並沒有消失，它混進了環境中大量的自由度 | 06的Concept，coherence is not lost but rather mixed with many more degrees of freedom in the environment |
| decoherence-and-error-correction | 所以Shor演算法目前還威脅不到真實使用的加密 | 01的Decoherence估計分解2,048位元整數至少要3 million個實體量子位元，01的導言也說not yet practical for real-world applications |

結論：通過，重審4句，沒有新問題

## 第三次審查，依新寫作規則全面改寫之後

8個概念頁的敘述文字全部重寫過，段落改用逗號串接，拿掉中英文之間的空白，少用括號和冒號。

這次逐頁把新版和舊版對照，確認每個說法、數字和連結都還在，也沒有多出舊版沒有的說法，唯一新增的是decoherence-and-error-correction把20 mK補上一句「也就是千分之二十克耳文」，這是單位換算，數值相同，已經記在log.md。

lint_wiki也重新跑過，36個數字都在原文找得到出處。

| 頁面 | 和舊版比對的結果 |
|---|---|
| quantum-computer | 說法相同，「科學上的里程碑」改寫成「科學研究上的進展，不代表很快就能用」，對應原文的scientific milestones rather than evidence for near-term deployment |
| qubit | 說法相同 |
| superposition-and-measurement | 說法相同 |
| entanglement | 說法相同 |
| quantum-gates | 說法相同 |
| quantum-algorithms | 說法相同 |
| shor-algorithm | 說法相同 |
| decoherence-and-error-correction | 說法相同，多了上面提到的單位換算 |

結論：通過，全面改寫沒有改變任何事實

## 第四次審查，段內句號調整之後

這次只動標點，段落中間的句號，短段落改成逗號，長段落改成在句號處分段，字句沒有增減，說法、數字和連結都和第三次審查時相同，lint_wiki重跑後數字仍然全部找得到出處。

結論：通過，只有標點和分段改變
