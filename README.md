# LLM 知識庫

以 LLM 編譯驅動的個人知識管理系統。靈感來自 [Andrej Karpathy 的 LLM 知識庫工作流程](https://x.com/karpathy/status/2039805659525644595)——把原始素材與編譯知識分開，讓 LLM 擔任你的圖書館員。

## 問題所在

大多數個人知識系統最終都成了墓地。你收藏文章、做筆記、畫重點——然後再也不去看。**收集**與**理解**之間的落差，就是知識死去的地方。

這個系統透過讓 LLM **編譯**你的原始素材，把它們轉化成結構化、相互連結的知識——摘要、概念條目、索引——同時保持原始來源完好不動，來填補這個落差。

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

1. 在 GitHub 點 **「Use this template」** 建立你自己的 repo
2. Clone 到本機
3. 用 [Obsidian](https://obsidian.md) 開啟資料夾
4. 安裝 [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)
5. 執行 `/init-llm` 進行互動式設定——它會問你幾個問題，然後幫你設定好一切
6. 把第一篇文章丟進 `raw/articles/`
7. 執行 `/compile`——看著第一份摘要和概念條目出現在 `wiki/` 裡

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

## 不用 LLM 也可以運作

資料夾結構與 Obsidian 範本本身就能獨立運作。你可以按照 `CLAUDE.md` 中的格式手動撰寫摘要和概念條目。Claude Code 指令只是自動化了你原本要手動完成的事。

## 自訂

參閱 [docs/customization.md](docs/customization.md) 了解如何：

- 更改編譯輸出的語言
- 在 `artifacts/` 下新增特定領域的子資料夾
- 自訂摘要和概念條目的段落標題
- 為你的領域調整系統

## 致謝

架構靈感來自 [Andrej Karpathy 的 LLM 知識庫概念](https://x.com/karpathy/status/2039805659525644595)。原始實作與編譯工作流程由 [@gatelynch](https://github.com/gatelynch) 完成。

## 授權

MIT
