# 量子計算 LLM Wiki：AI 專案規則

這份文件寫給在這個專案裡工作的 AI 助手（Claude Code、Codex 等）。動手之前先讀完。

## 1. 專案在做什麼

這個專案依照 LLM Wiki 的做法，把「量子計算入門」的資料整理成一份由 LLM 維護的知識庫，再只用這份知識庫做出一份給初學者看的教學 HTML 簡報。

讀者設定是高中或大一程度、沒學過量子力學的人。簡報看完，讀者要能說出量子位元、疊加、測量、糾纏、量子閘是什麼，知道 Shor 演算法為什麼重要，也知道量子電腦現在卡在哪裡。

資料有三層，越往下越接近成品：

| 層 | 資料夾 | 誰寫 | 規則 |
|---|---|---|---|
| 原始來源 | `raw/` | `fetch_sources.py` | 抓下來之後唯讀，不准修改 |
| 討論紀錄 | `discussions/` | LLM | 每篇來源一份，寫完才能進 wiki |
| 知識庫 | `wiki/` | LLM | 每頁一個概念，所有說法都要能在 raw 找到 |
| 簡報 | `slides/outline.md` → `slides.html` | LLM 寫大綱，腳本建置 | 每張投影片只能用 wiki 的內容 |

## 2. 檔案結構

```
quantum-llm-wiki/
├── CLAUDE.md              # 本文件
├── WORKFLOW.md            # loop / graph 設計、執行紀錄、反思
├── sources.json           # 要抓的來源清單
├── raw/                   # 原始來源（維基百科純文字，唯讀）＋ manifest.json
├── discussions/           # 每篇來源的討論紀錄，檔名與 raw 相同
├── wiki/
│   ├── index.md           # 目錄：列出每一頁和一句話摘要
│   ├── log.md             # 時間紀錄：每次 ingest、lint、修正都記一筆
│   └── <概念>.md          # 概念頁
├── slides/
│   ├── outline.md         # 簡報大綱（LLM 寫）
│   └── slide-map.json     # wiki 頁面被哪些投影片引用（腳本產生）
├── slides.html            # 簡報成品（腳本產生，不要手改）
├── index.html、wiki.html、workflow.html、assets/   # 網站
├── scripts/               # 流程中的腳本節點
└── runs/                  # 每次執行流程的紀錄（腳本產生）
```

## 3. 工作流程（graph v3）

```
test_checks → fetch → discuss → ingest → lint_wiki → review_claims → plan_outline → check_outline → build_slides → check_build
```

一次跑完全部檢查：`python3 scripts/run_pipeline.py v3 --note "這次改了什麼"`。
流程的設計理由，以及從 v1 改到 v3 的經過，寫在 `WORKFLOW.md`。

### discuss：先討論，後生成

讀完一篇 raw 來源後，先在 `discussions/<同檔名>.md` 寫討論紀錄，內容固定四段：

1. 這篇在講什麼（2 到 3 句）
2. 初學者需要的重點（3 到 6 點，每點標出原文在哪一節）
3. 要寫進哪些 wiki 頁面（新增或更新哪一頁、放哪些內容）
4. 疑點與決定（原文有爭議、太深、或抽取時跑掉的地方，以及怎麼處理）

沒有討論紀錄的來源，不能出現在任何 wiki 頁面的 `sources` 裡。`lint_wiki.py` 會擋。

### ingest：寫 wiki

- 一個概念一頁，檔名用英文小寫加連字號，例如 `qubit.md`、`shor-algorithm.md`。
- 每頁開頭必須有 frontmatter：

  ```
  ---
  title: 量子位元
  summary: 一句話摘要
  sources: [02-qubit, 01-quantum-computing]
  ---
  ```

- 內文用繁體中文，專有名詞第一次出現時附英文。數學式用 `$...$` 和 `$$...$$`。
- 頁面之間用相對連結互連，例如 `[量子糾纏](entanglement.md)`。
- 只寫 `sources` 列出的來源裡有的內容。來源沒寫的數字、年份、人名，一律不寫。
- 有爭議的說法要寫出是誰主張、誰反對，例如 Google 2019 年的量子霸權聲明。
- 新增或改名頁面後，同步更新 `wiki/index.md`；每次 ingest 結束在 `wiki/log.md` 加一筆。

### review_claims：核對沒有數字的說法

- lint_wiki 通過後，逐頁讀 wiki，每個說法都回到該頁 `sources` 列出的 raw 檔找出處。
- 找不到出處、把原文的程度詞換成更強的詞、或出處在沒列出的來源，都算問題，回到 ingest 修正。
- 結果寫進 `runs/review-claims.md`，結尾寫「結論：通過」。這份紀錄必須比所有 wiki 頁面新，wiki 改過就要重新審。

### plan_outline：用 wiki 寫簡報大綱

- 先讀 `wiki/index.md` 決定要用哪些頁面，再讀那些頁面。不要回頭讀 raw，也不要用 wiki 以外的知識。
- 投影片之間用單獨一行的 `---` 分隔，每張都要標註來源：

  ```
  <!-- sources: qubit, superposition-and-measurement -->
  ## 投影片標題
  - 重點
  ```

- 教學結構固定：封面（`<!-- layout: title -->`）、學習目標、概念投影片、小測驗、重點整理、參考資料。
- 每張投影片的條列最多 6 點。比喻可以用，但要標明是比喻。

### 檢查節點

| 腳本 | 檢查什麼 | 失敗時回到 |
|---|---|---|
| `test_checks.py` | 數字比對本身沒有誤判 | 修檢查器 |
| `lint_wiki.py` | 討論紀錄齊全、frontmatter、連結、index、數字都能在 raw 找到 | ingest |
| `check_slides.py outline` | 教學結構、來源標註、條列數、數字都能在引用的 wiki 頁找到 | plan_outline |
| `check_slides.py build` | 投影片張數、來源連結、wiki 連結都存在 | build_slides |

同一個節點連續失敗 3 次，就停下來把問題寫進 `wiki/log.md`，請使用者判斷。

## 4. 寫作規則

- 句子短，直接寫事實和推導。
- 不用「不是 A，而是 B」的對比句、破折號（——）和段落結尾的總結金句，段首也不加粗體標籤。
- 數字照來源寫，換單位或換算時在 log.md 記下換算方式。

## 5. 不要做的事

- 修改 `raw/` 裡的檔案。
- 手改 `slides.html`，要改就改 `slides/outline.md` 再執行 `build_slides.py`。
- 在投影片放 wiki 沒有的內容。
- 跳過檢查直接 push。

## 6. 部署

- GitHub Pages 發布 `main` 分支根目錄：https://arthur031221.github.io/quantum-llm-wiki/
- 所有連結用相對路徑。
