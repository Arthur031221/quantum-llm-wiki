# 量子計算LLM Wiki的AI專案規則

這份文件寫給在這個專案裡工作的AI助手，例如Claude Code或Codex，動手之前請先讀完。

## 1. 專案在做什麼

這個專案照LLM Wiki的做法，把量子計算入門的資料整理成一份由LLM維護的知識庫，再只用這份知識庫做出給初學者看的教學HTML簡報。

讀者設定成高中或大一程度、沒學過量子力學的人，看完簡報要能說出量子位元、疊加、測量、糾纏和量子閘是什麼，知道Shor演算法為什麼讓人緊張，也知道量子電腦現在卡在哪裡。

資料分成幾層，越往下越接近成品，每一層只能讀上一層。

| 層 | 資料夾 | 誰寫 | 規則 |
|---|---|---|---|
| 原始來源 | `raw/` | `fetch_sources.py` | 抓下來之後唯讀，不准修改 |
| 討論紀錄 | `discussions/` | LLM | 每篇來源一份，寫完才能進wiki |
| 知識庫 | `wiki/` | LLM | 每頁一個概念，所有說法都要能在raw找到 |
| 簡報大綱 | `slides/outline.md` | LLM | 每張投影片只能用wiki的內容 |
| 簡報成品 | `slides.html` | 腳本 | 由大綱建置，不要手改 |

## 2. 檔案結構

```
quantum-llm-wiki/
├── CLAUDE.md              # 本文件
├── WORKFLOW.md            # loop和graph的設計、執行紀錄、反思
├── sources.json           # 要抓的來源清單
├── raw/                   # 原始來源（維基百科純文字，唯讀）和 manifest.json
├── discussions/           # 每篇來源的討論紀錄，檔名與 raw 相同
├── wiki/
│   ├── index.md           # 目錄，列出每一頁和一句話摘要
│   ├── log.md             # 時間紀錄，每次 ingest、lint、修正都記一筆
│   └── <概念>.md          # 概念頁
├── slides/
│   ├── outline.md         # 簡報大綱，LLM 寫
│   └── slide-map.json     # wiki 頁面被哪些投影片引用，腳本產生
├── slides.html            # 簡報成品，腳本產生
├── index.html、wiki.html、workflow.html、assets/   # 網站
├── scripts/               # 流程中的腳本節點
└── runs/                  # 每次執行流程的紀錄，腳本產生
```

## 3. 工作流程

目前用的是graph v3，節點依序是test_checks、fetch、discuss、ingest、lint_wiki、review_claims、plan_outline、check_outline、build_slides和check_build，一次跑完全部節點的指令是`python3 scripts/run_pipeline.py v3 --note "這次改了什麼"`，流程為什麼這樣設計、從v1怎麼改到v3，都寫在`WORKFLOW.md`。

### discuss，先討論再生成

讀完一篇raw來源，先在`discussions/<同檔名>.md`寫討論紀錄，內容固定四段。

1. 這篇在講什麼，兩三句就好
2. 初學者需要的重點，三到六點，每點標出原文在哪一節
3. 要寫進哪些wiki頁面，新增還是更新，放哪些內容
4. 疑點與決定，原文有爭議、太深或抽取時跑掉的地方，以及打算怎麼處理

沒有討論紀錄的來源，不能出現在任何wiki頁面的`sources`裡，`lint_wiki.py`會擋下來。

### ingest，寫wiki

- 一個概念一頁，檔名用英文小寫加連字號，例如`qubit.md`或`shor-algorithm.md`
- 每頁開頭一定要有frontmatter

  ```
  ---
  title: 量子位元
  summary: 一句話摘要
  sources: [02-qubit, 01-quantum-computing]
  ---
  ```

- 內文用繁體中文，專有名詞第一次出現時用敘述帶出英文名稱，數學式用`$...$`和`$$...$$`
- 頁面之間用相對連結互連，例如`[量子糾纏](entanglement.md)`
- 只寫`sources`列出的來源裡有的內容，來源沒寫的數字、年份和人名一律不寫
- 有爭議的說法要寫出誰主張、誰反對，例如Google在2019年的量子霸權聲明
- 新增或改名頁面後同步更新`wiki/index.md`，每次ingest結束在`wiki/log.md`記一筆

### review_claims，核對沒有數字的說法

lint_wiki通過以後，逐頁讀wiki，把每個說法拿回該頁`sources`列出的raw檔找出處，找不到出處的、把原文的程度詞換成更強的詞的、出處在沒列出的來源的，都算問題，要回到ingest修正，結果寫進`runs/review-claims.md`並在結尾寫「結論：通過」，這份紀錄必須比所有wiki頁面新，wiki改過就得重審。

### plan_outline，用wiki寫簡報大綱

- 先讀`wiki/index.md`決定要用哪些頁面，再讀那些頁面，不回頭讀raw，也不用wiki以外的知識
- 投影片之間用單獨一行的`---`分隔，每張都要標註來源

  ```
  <!-- sources: qubit, superposition-and-measurement -->
  ## 投影片標題
  - 重點
  ```

- 教學結構固定，依序是封面`<!-- layout: title -->`、學習目標、概念投影片、小測驗、重點整理和參考資料
- 每張投影片最多六個條列點，可以用比喻，但要寫明是比喻

### 檢查節點

| 腳本 | 檢查什麼 | 失敗時回到 |
|---|---|---|
| `test_checks.py` | 數字比對本身有沒有誤判 | 修檢查器 |
| `lint_wiki.py` | 討論紀錄齊全、frontmatter、連結、index，數字都能在raw找到 | ingest |
| `check_slides.py outline` | 教學結構、來源標註、條列數，數字都能在引用的wiki頁找到 | plan_outline |
| `check_slides.py build` | 投影片張數、來源連結，連到的wiki頁都存在 | build_slides |

同一個節點連續失敗三次就停下來，把問題寫進`wiki/log.md`請使用者判斷。

## 4. 寫作規則

所有敘述文字都照這幾條寫，wiki、討論紀錄、簡報和說明文件都一樣。

- 一個段落裡用逗號串起來，只有段落最後用句號，冒號和斜線少用
- 不用分號、破折號、箭頭、表情符號、勾勾叉叉和刪節號字元
- 中文和英文單字或數字之間不加空白，例如寫「用tools/gen產」和「在2019年」
- 少用括號和【】，能用一句話說清楚就用敘述帶過
- 不在句子中間加粗，不寫「不是A而是B」的對仗句，不寫戲劇性的收尾，也不要為了湊滿三點而多寫
- 不用「值得注意的是」「此外」「總而言之」「至關重要」這類套話
- 數字照來源寫，換單位或換算時在log.md記下怎麼換算

## 5. 不要做的事

- 修改`raw/`裡的檔案
- 手改`slides.html`，要改就改`slides/outline.md`再執行`build_slides.py`
- 在投影片放wiki沒有的內容
- 跳過檢查直接push

## 6. 部署

GitHub Pages發布`main`分支的根目錄，網址是https://arthur031221.github.io/quantum-llm-wiki/ ，所有連結都用相對路徑。
