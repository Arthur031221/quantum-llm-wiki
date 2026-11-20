# Wiki時間紀錄

每次ingest、lint或修正都在最後面記一筆。

## 2026-11-20 fetch

依`sources.json`從英文維基百科抓了6篇條目的純文字，存進`raw/`，抓下來才發現純文字抽取會吃掉上標、根號和分數線，像$2^n$變成「2n」，$1/\sqrt2$變成「12」，這些都記在各篇的討論紀錄裡，寫wiki時再手動還原。

## 2026-11-20 discuss

6篇來源各寫了一份討論紀錄，放在`discussions/`，決定建立8個概念頁，也決定好每頁要用哪些來源。

## 2026-11-20 ingest

新增quantum-computer、qubit、superposition-and-measurement、entanglement、quantum-gates、quantum-algorithms、shor-algorithm和decoherence-and-error-correction這8頁，建立index.md。

表格裡的數學式改用`\lvert ... \rangle`，因為`|`會被Markdown當成表格的分隔線。

## 2026-11-20 run 01，graph v1

check_slides沒過，封面寫了「20分鐘」，這是我估的簡報長度，wiki裡沒有這個數字，問題出在plan_outline，LLM自己加了wiki以外的內容，改成「入門簡報」，不寫時間。

## 2026-11-20 run 02，graph v1

全部通過，可是v1只拿投影片去比對wiki，wiki本身有沒有忠於raw，從頭到尾都沒檢查。

## 2026-11-20，第一次執行lint_wiki

結果是通過，但加上`--evidence`逐條看每個數字在原文哪裡找到，才發現檢查本身有三個漏洞。

- 「300萬」對到的是原文的「300-digit primes」，正確的出處是「3 million physical qubits」，說法剛好是對的，檢查卻是因為巧合才通過
- raw檔標頭裡的抓取日期和版本時間戳也被拿去比對，「20」「11」「2026」都先對到了標頭
- |11⟩這類ket標籤被當成數字

修正方式是比對前先去掉raw標頭，忽略ket標籤，遇到「萬」「億」先換算再比對。

換算成3,000,000之後又撞到Sycamore那段的「3,000,000 times faster」，所以改成先比對million這種比較具體的寫法。

這些誤判都寫成`scripts/test_checks.py`裡的測試案例。

流程也改成graph v2，lint_wiki移到ingest後面，而且一律輸出evidence讓人確認，投影片檢查拆成建置前的check_outline和建置後的check_build。

## 2026-11-20 run 03，graph v2

停在test_checks，原因是測試案例「fetched: 2026-11-20」本身寫錯了，原文本文就有「as of 2026」和「20 millikelvin」，這個案例本來就該通過，改用只出現在標頭的版本號1386685712當案例。

## 2026-11-20 run 05與review_claims，graph v3

數字檢查抓不到沒有數字的說法，所以新增review_claims節點，lint_wiki通過以後由LLM逐頁對照raw核對每個說法。

run 05停在review_claims是預期中的事，因為還沒有審查紀錄，審查後找到5處超出來源的說法，都已經修正，細節在`runs/review-claims.md`。

- quantum-gates寫了「例如AND不可逆」，來源只提到AND和Toffoli閘的關係，刪掉這個例子
- superposition-and-measurement寫了「測量問題到現在仍有爭論」，來源只說這叫測量問題，刪掉「仍有爭論」
- superposition-and-measurement寫了「環境像在測量量子位元」，這個說法出自03和06，這頁的sources卻沒列它們，改寫成01支持的說法
- shor-algorithm把原文的most scalable寫成「最好的」，改成「擴展性最好的」
- qubit寫「Schumacher在1995年的論文裡提出」，原文是一般認為是他創的，他在致謝裡提到這個詞是和Wootters開玩笑想出來的，照原文改寫

## 2026-11-20，文字修飾與run 08、09，graph v3

用humanizer和stop-slop的規則修飾全部文字，wiki有4句改寫，quantum-computer和decoherence-and-error-correction各2句，內容不變。

run 08停在review_claims，因為wiki在審查之後改過，審查紀錄過期了，這正是v3要擋的情況，照規則重新核對那4句以後跑run 09才通過。

## 2026-11-20，依新的寫作規則全面改寫

照使用者給的中文寫作規則，把8個概念頁、index和討論紀錄的敘述文字全部改寫，段落內改用逗號串接，拿掉中英文之間的空白，少用括號和冒號，事實、數字和來源都不動。

數字檢查也跟著修正，原本中文字緊貼數字時，例如「在2019年」，數字會被跳過不檢查，現在一樣會抽出來比對，並加進test_checks的案例。

decoherence-and-error-correction把20 mK補上「也就是千分之二十克耳文」，這是單位換算，數值沒變。

## 2026-11-20，段內句號調整

段落中間的句號照寫作規則處理，短段落改成逗號，長段落改成在句號處分段，只動標點，重新審查後跑run 11。
