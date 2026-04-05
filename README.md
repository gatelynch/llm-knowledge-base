# LLM 知識庫

以 LLM 編譯驅動的個人知識管理系統。靈感來自 [Andrej Karpathy 的 LLM 知識庫工作流程](https://x.com/karpathy/status/2039805659525644595)——把原始素材與編譯知識分開，讓 LLM 擔任你的圖書館員。

## 問題所在

大多數個人知識系統最終都成了墓地。你收藏文章、做筆記、畫重點——然後再也不去看。**收集**
、**理解**與**輸出**之間的落差，就是埋葬知識的地方。

這個系統透過讓 LLM **編譯**你的原始素材，把它們轉化成結構化、相互連結的知識：摘要、概念條目、索引，同時保持原始來源完好不動，來填補這個落差。

## 架構

```
raw/                    ← 你的圖書館：未經編輯的原始素材
  ├── articles/           收藏的文章
  ├── books/              書籍筆記與畫線
  ├── podcasts/           podcast 逐字稿
  ├── papers/             學術論文
  ├── notes/              你的快速想法
  └── projects/           專案相關素材

wiki/                   ← 你的百科全書：LLM 編譯的知識
  ├── summaries/          每個來源一份摘要
  ├── concepts/           概念條目（交叉引用）
  └── indexes/            All-Sources.md、All-Concepts.md

brainstorming/          ← 你的實驗筆記本：探索與品質管理
  ├── chat/               問答記錄與推理過程
  └── health/             知識庫健康報告

artifacts/              ← 你的發表成果：完成的作品
  └── projects/           你的專案與產出
```

**核心原則**：原始素材是唯讀的。LLM 把它們編譯進 wiki/，但永遠不修改你的原始檔案。

## 快速開始

1. 執行 `/init-llm` 進行互動式設定——它會問你幾個問題，然後幫你設定好一切
2. 把第一篇文章丟進 `raw/articles/`
3. 執行 `/compile`——看著第一份摘要和概念條目出現在 `wiki/` 裡

## Claude 與 Codex

這個 repo 現在同時支援 Claude 與 Codex，但兩者的入口不同：

- `CLAUDE.md`：給 Claude Code 的專用設定
- `.claude/commands/`：給 Claude Code 的 slash commands
- `AGENTS.md`：給 Codex 與其他通用 agent 的操作規則
- `docs/workflows.md`：供應商中立的工作流程定義

如果你用的是 Claude Code，照原本的 `/compile`、`/thinking-partner`、`/write-partner` 等指令操作即可。

如果你用的是 Codex，不需要複製 `.claude/commands/`。讓 Codex 讀 `AGENTS.md`、`docs/architecture.md`、`docs/workflows.md` 與 `docs/examples/`，再執行等價流程就可以。

## 指令

這個系統包含 6 個 Claude Code 斜線指令：

| 指令 | 功能 |
|------|------|
| `/init-llm` | 互動式設定——詢問你的個人資料與偏好、掃描現有檔案、提出整理計畫，並設定 `CLAUDE.md` |
| `/compile` | 讀取 `raw/` 和 `artifacts/`，在 `wiki/summaries/` 生成摘要，提取概念至 `wiki/concepts/`，更新索引 |
| `/health-check` | 掃描 `wiki/` 的一致性問題、完整性缺口與連結性問題，輸出優先排序報告至 `brainstorming/health/` |
| `/thinking-partner` | 協作思考——搜尋 vault 中的相關筆記、提出釐清問題，幫你深度探索複雜問題 |
| `/write-partner` | 寫作探索——找出 vault 中的相關內容、反例與開放問題，幫你在動筆前把想法挖得更深 |
| `/braindump` | 把對話沉澱成可複用的素材——問答記錄、文章草稿，或兩者都要——存至 `brainstorming/chat/` |

## 編譯如何運作

```
1. 你把一個檔案放進 raw/articles/
2. 執行 /compile
3. LLM 讀取檔案，判斷 origin（external vs. self）
4. 在 wiki/summaries/ 生成摘要，包含：
   - 核心結論
   - 關鍵證據
   - 疑點
   - 術語
5. 把在 2 個以上摘要中出現的概念提取至 wiki/concepts/
6. 更新 wiki/indexes/（All-Sources.md、All-Concepts.md）
```

每個概念條目把**你的實踐**與**外部觀點**分開，並有專門的**張力與缺口**段落。這是核心知識價值所在——你的經驗與研究並排存在，矛盾被浮現出來，而不是被掩蓋。

## 一個實際例子

假設你讀到一篇談「AI 怎麼改變學生提問能力」的文章，這套系統會這樣運作：

### 第一步：捕捉

你先把文章存進 `raw/articles/20260404 AI改變學生提問能力.md`。這一步只做收集，不需要先分類、摘要，或決定它跟哪個主題有關。

### 第二步：編譯

等你累積了幾篇相關文章，再執行 `/compile`。系統會：

1. 讀取 `raw/` 裡的新檔案
2. 生成摘要，存到 `wiki/summaries/AI改變學生提問能力.md`，內容包含核心結論、關鍵證據與疑點
3. 提取概念；如果 `wiki/concepts/提問能力.md` 還不存在，就建立一份，若已存在就更新它，把這篇新來源納入
4. 更新索引，讓 `wiki/indexes/All-Sources.md` 多出一筆紀錄

### 第三步：問答

之後某天你想寫一篇文章，使用 `/write-partner`：

> AI 輔助教學到底是增強還是削弱了學生的提問能力？研究怎麼說？我自己的課堂經驗又怎麼說？

系統會：

- 翻 `wiki/summaries/` 找外部研究與相關摘要
- 翻你放在 `artifacts/` 裡的文章、教學記錄或其他實踐素材，找出你自己的經驗
- 使用 `/braindump`把整理過的推理過程與結論存到 `brainstorming/chat/`

### 第四步：產出

你根據這些資料寫出一篇文章，存回 `artifacts/`。下次編譯時，這篇文章也會被摘要；但因為它是你的作品，系統會用偏向「你的主張」與「實踐經驗」的格式來整理，而不只是把它當成外部來源做一般摘要。


## 為什麼我最後變成這樣做

我最早用 Google Docs 寫東西，幾乎沒有結構。後來接觸到第二大腦與 Tiago Forte 的 CODE 方法，我以為問題在於自己還不夠會整理；結果真正耗掉時間的，反而是分類、資料夾、Tag 這些組織工作。等我把系統想清楚，已經沒有力氣讀書、思考，或寫出自己的東西。

NotebookLM 出現之後，我又以為答案會是「不要整理，全部交給 AI」。但很快就發現，沒有可累積的記憶，對話就只是一次次重開的隨性對話。每次都要重新交代自己是誰、在做什麼、之前想過什麼；知識沒有真正沉澱，只是被臨時使用。

所以我把系統換成四層：`raw/` 放原始資料、`wiki/` 放 LLM 編譯後的摘要與概念、`brainstorming/` 放與 AI 的探索紀錄、`artifacts/` 放自己的成品。表面上看起來比以前更嚴謹，但實際上我真正碰的主要只有兩層：把靈感丟進 `raw/notes/`，把完成的文章放進 `artifacts/`。中間的整理、連結、概念提取，交給 AI 去做。

也正是在這一步，我才第一次感受到這種系統的價值。AI 不只是替我做摘要，而是能把不同文章裡反覆出現、卻從來沒有被我並排思考過的概念抽出來，重新編成脈絡。像 High Agency 這類想法，我明明在很多來源都碰過，卻從來沒有自己把它們連在一起。這種跨來源的概念編譯，是我手動很難穩定做到的事。

但換了幾次系統之後，我也慢慢確定：真正的問題從來不只是工具。以前用 PARA，摩擦力來自整理本身；每則筆記都要歸類、命名、搬到對的位置。那很煩，但也逼你重新接觸材料。現在整理交給 AI，摩擦力沒有消失，只是換了形式。它變成對話裡那些你答不上來的問題、那些被指出的矛盾、那些你以為想清楚其實還沒有的地方。以前是一個人安靜地重讀材料，現在是透過對話被迫澄清自己的想法。

所以這個 repo 最後想保留的，不是某一套完美分類法，而是一個比較耐用的知識流：原始靈感持續進入 `raw/`，編譯後的理解沉澱到 `wiki/`，探索過程留在 `brainstorming/`，真正重要的產出落到 `artifacts/`。工具會一直換，流程也會一直改，但只要你的筆記和作品還在，系統就沒有白做。

## 自訂

參閱 [docs/customization.md](docs/customization.md) 了解如何：

- 更改編譯輸出的語言
- 在 `artifacts/` 下新增特定領域的子資料夾
- 自訂摘要和概念條目的段落標題
- 為你的領域調整系統

## 致謝

架構靈感來自 [Andrej Karpathy 的 LLM 知識庫概念](https://x.com/karpathy/status/2039805659525644595)及[Andrej Karpathy 的 想法文件](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)。原始實作與編譯工作流程由 [@gatelynch](https://github.com/gatelynch)與 [@claude](https://github.com/claude) 完成。

## 授權

MIT
