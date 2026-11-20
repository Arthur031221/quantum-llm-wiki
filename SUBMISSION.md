繳交標題：清大 111022201 物理26 李騏維 量子計算LLM Wiki教學簡報

---

LLM Wiki主題與簡介

我選的主題是量子計算入門，從英文維基百科抓了6篇條目當原始資料，分別是Quantum computing、Qubit、Quantum entanglement、Quantum logic gate、Shor's algorithm和Quantum decoherence，每篇先寫一份討論紀錄，再整理成8個wiki概念頁，包括量子電腦、量子位元、疊加與測量、量子糾纏、量子邏輯閘、量子演算法與加速、Shor演算法，以及退相干與錯誤更正，每頁都列出用到的來源，數字和說法也都核對過原文。

LLM Wiki連結

Wiki網頁在 https://arthur031221.github.io/quantum-llm-wiki/wiki.html ，GitHub在 https://github.com/Arthur031221/quantum-llm-wiki ，raw、discussions和wiki三層資料都在裡面，給AI看的規則寫在CLAUDE.md。

教學HTML簡報連結

https://arthur031221.github.io/quantum-llm-wiki/slides.html

簡報一共17張，對象是沒學過量子力學的人，從學習目標開始，接著講位元、疊加、測量、干涉、糾纏、量子閘、第一個量子電路、演算法、Shor、退相干和現況，最後是小測驗、重點整理和參考資料，每張投影片右下角都標了出自哪幾頁wiki，點下去就跳到那一頁，wiki頁面也會反過來列出哪幾張投影片用到它。

loop和graph的設計

完整說明和流程圖在 https://arthur031221.github.io/quantum-llm-wiki/workflow.html ，最後的版本是graph v3，節點依序是test_checks、fetch、discuss、ingest、lint_wiki、review_claims、plan_outline、check_outline、build_slides和check_build。

fetch用腳本從維基百科抓純文字，存成唯讀的raw，discuss替每篇來源寫討論紀錄，寫下重點、要放進哪一頁和有疑問的地方，沒討論過的來源不能進wiki，lint_wiki會擋下來。

ingest負責寫wiki頁面，lint_wiki接著檢查格式、連結和目錄，並確認wiki裡每個大於10的數字都能在原文找到，同時列出出處給人看，review_claims再由LLM逐頁回原文核對沒有數字的說法，審查紀錄必須比wiki新，wiki改過就得重審。

plan_outline只讀wiki寫簡報大綱，每張都標註wiki來源，check_outline檢查教學結構、來源標註、每張不超過六點，以及投影片的數字能不能在wiki找到，build_slides產生slides.html，check_build再檢查張數和連結，最前面的test_checks則是先測試檢查器本身。

會重複執行的地方有三個迴圈，分別是ingest、lint_wiki和review_claims，plan_outline和check_outline，以及build_slides和check_build，哪個檢查沒過就回到前面的生成節點重做，同一個節點連續失敗三次就停下來交給人判斷。

這樣設計是因為每一層只讀上一層，錯誤在哪一層發生就在哪一層擋，失敗時也清楚該回到哪裡改。

一次實際執行的結果與檢查紀錄

流程一共跑了11次，每次的紀錄都在 https://github.com/Arthur031221/quantum-llm-wiki/tree/main/runs 。

- run 01用graph v1，沒過，封面寫了「20分鐘」，wiki沒有這個數字，是LLM寫大綱時自己加的
- run 02用v1，通過了，可是v1只拿投影片比對wiki，從來沒檢查wiki本身
- run 03用v2，沒過，新加的檢查器自我測試裡有一個案例是我寫錯的
- run 04用v2，通過
- run 05用v3，停在review_claims，接著審查找到5處超出來源的說法，像「AND閘不可逆」來源沒寫，「most scalable」被寫成「最好的」
- run 06和run 07用v3，修正後通過
- run 08用v3，沒過，修飾文字時改了4句wiki，審查紀錄變得比wiki舊，review_claims把它擋下來，「wiki改過就要重審」這條規則確實有用
- run 09用v3，重審那4句後通過
- run 10用v3，照新的寫作規則改寫全部文字，順便修好數字緊貼中文時被略過的問題，重審後10個節點全部通過
- run 11用v3，把段落中間的句號改成逗號或分段，只動標點，重審後通過，這是最後發布的版本

反思

最常出錯的節點是ingest，它出的5個問題都是句子讀起來對，來源卻沒寫，或是把原文的程度詞換得更強，而且都沒有數字，格式和數字檢查都看不出來，寫大綱的plan_outline也出過一次同樣性質的錯，就是封面的「20分鐘」。

另一個意外是檢查器本身，lint_wiki第一次跑就說通過，我逐條看數字的出處，才發現「300萬」對到的是「300-digit primes」，正確的出處是「3 million qubits」，raw標頭的日期和|11⟩這種狀態標籤也被拿去比對。

後來把中文和數字之間的空白拿掉，「在2019年」這種數字又被比對規則靜靜略過，只看通過兩個字，我會以為wiki沒問題。

檢查往前移了好幾處，數字核對從最後的投影片檢查移到ingest之後，也就是lint_wiki，wiki的錯不會再一路被抄進投影片，說法核對review_claims放在ingest之後、寫大綱之前，投影片內容的檢查移到建置之前，最前面再加上test_checks，先確認檢查器沒壞，再相信它的結果。

workflow也因此從v1改到v3，v1把檢查全放在最後，前面的錯會被複製下去，到最後反而看起來有根據，v2把數字檢查放到錯誤發生的那一層，也修好了檢查器，v3補上數字以外的說法核對，因為ingest最常犯的就是這種錯。

還沒解決的是review_claims由LLM審自己寫的內容，換一個模型或請人來審會更可靠。
