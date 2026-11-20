繳交標題：清大 111022201 物理26 李騏維 量子計算 LLM Wiki 教學簡報

---

【LLM Wiki 主題與簡短介紹】
主題是「量子計算入門」。我從英文維基百科抓了 6 篇條目當原始資料（Quantum computing、Qubit、Quantum entanglement、Quantum logic gate、Shor's algorithm、Quantum decoherence），每篇先寫一份討論紀錄，再整理成 8 個 wiki 概念頁：量子電腦、量子位元、疊加與測量、量子糾纏、量子邏輯閘、量子演算法與加速、Shor 演算法、退相干與錯誤更正。每頁都列出用到的來源，數字和說法都核對過原文。

【LLM Wiki 連結】
Wiki 網頁：https://arthur031221.github.io/quantum-llm-wiki/wiki.html
GitHub：https://github.com/Arthur031221/quantum-llm-wiki （raw/、discussions/、wiki/ 三層都在裡面，規則寫在 CLAUDE.md）

【教學 HTML 簡報連結】
https://arthur031221.github.io/quantum-llm-wiki/slides.html
共 17 張，對象是沒學過量子力學的人。結構是學習目標、概念（位元、疊加、測量、干涉、糾纏、量子閘、第一個量子電路、演算法、Shor、退相干、現況）、小測驗、重點整理、參考資料。每張投影片右下角都標了 wiki 來源，點了就會跳到那一頁；wiki 頁面也會列出哪幾張投影片用到它。

【loop / graph 設計】
完整說明與流程圖：https://arthur031221.github.io/quantum-llm-wiki/workflow.html
最終版本（graph v3）：
test_checks → fetch → discuss → ingest → lint_wiki → review_claims → plan_outline → check_outline → build_slides → check_build

- fetch：腳本從維基百科抓純文字，存成唯讀的 raw。
- discuss：每篇來源先寫討論紀錄（重點、要寫進哪頁、疑點），沒討論過的來源不准進 wiki，lint_wiki 會擋。
- ingest：寫 wiki 頁面。
- lint_wiki：檢查格式、連結、index，並確認 wiki 裡每個大於 10 的數字都能在原文找到，同時列出出處給人看。
- review_claims：LLM 逐頁回原文核對沒有數字的說法。審查紀錄必須比 wiki 新，wiki 改過就要重審。
- plan_outline：只讀 wiki 寫簡報大綱，每張標註 wiki 來源。
- check_outline：檢查教學結構、來源標註、每張不超過 6 點、投影片數字能在 wiki 找到。
- build_slides、check_build：產生 slides.html，檢查張數和連結。
- test_checks：最前面先測試檢查器本身。

會重複執行的地方：ingest ↔ lint_wiki ↔ review_claims、plan_outline ↔ check_outline、build_slides ↔ check_build 三個迴圈，哪個檢查失敗就回到前面的生成節點重做。同一節點連續失敗 3 次就停下來交給人判斷。
這樣設計是因為每一層只讀上一層，錯誤在哪一層發生就在哪一層擋，失敗時也清楚該回到哪裡改。

【一次實際執行的結果與檢查紀錄】
一共跑了 9 次，每次的紀錄都在 runs/：
- run 01（v1）失敗：封面寫了「20 分鐘」，wiki 沒有這個數字，是 LLM 在寫大綱時自己加的。
- run 02（v1）通過，但 v1 只拿投影片比對 wiki，從沒檢查 wiki 本身。
- run 03（v2）失敗：新加的檢查器自我測試裡，有一個案例是我寫錯的。
- run 04（v2）通過。
- run 05（v3）停在 review_claims，接著審查找到 5 處超出來源的說法（例如「AND 閘不可逆」來源沒寫、「most scalable」被寫成「最好的」）。
- run 06、run 07（v3）修正後通過。
- run 08（v3）失敗：修飾文字時改了 4 句 wiki，審查紀錄變得比 wiki 舊，review_claims 擋下來，證明「wiki 改過就要重審」的規則有效。
- run 09（v3）重審那 4 句後通過，是最後發布的版本：10 個節點全部通過，test_checks 7/7。
紀錄連結：https://github.com/Arthur031221/quantum-llm-wiki/tree/main/runs

【反思】
最常出錯的節點是 ingest。它出的 5 個問題都是句子讀起來對、但來源沒寫，或把原文的程度詞換得更強，而且都沒有數字，所以格式和數字檢查都看不出來。寫大綱的 plan_outline 也出過一次同樣性質的錯（封面的「20 分鐘」）。

另一個意外是檢查器本身。lint_wiki 第一次跑就說通過，但我逐條看數字的出處，發現「300 萬」對到的是「300-digit primes」，正確的出處是「3 million qubits」；raw 標頭的日期和 |11⟩ 這種狀態標籤也被拿去比對。只看「通過」兩個字，我會以為 wiki 沒問題。

檢查往前移的地方：
1. 數字核對從最後的投影片檢查，往前移到 ingest 之後（lint_wiki），wiki 的錯不會再一路被抄進投影片。
2. 說法核對（review_claims）放在 ingest 之後、寫大綱之前。
3. 投影片內容檢查移到建置之前（check_outline）。
4. 最前面加上 test_checks，先確認檢查器沒壞再相信它的結果。

workflow 因此從 v1 改到 v3。v1 把檢查全放在最後，前面的錯會被複製下去，到最後反而看起來有根據。v2 把數字檢查放到錯誤發生的那一層，也修好了檢查器。v3 補上數字以外的說法核對，因為 ingest 最常犯的正是這種錯。
還沒解決的是：review_claims 是 LLM 審自己寫的內容，換一個模型或請人審會更可靠。
