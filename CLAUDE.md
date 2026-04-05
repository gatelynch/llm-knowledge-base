# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

---

## 關於使用者

<!-- 在此填寫你的簡介。範例：台灣的軟體工程師，對個人知識管理充滿熱情，持續探索如何讓學習更有效率。 -->
[YOUR_BIO — 用 1-2 句話描述你是誰、你關心什麼]

## 互動原則

- 使用 [YOUR_LANGUAGE] 跟我對話，請叫我「[YOUR_NAME]」
- 第一性原理：從最根本的角度分析問題，不預設答案
- 提問優先：需求不夠清楚時，主動提問直到沒有疑問，才開始執行
- 直接指出錯誤：尊重事實比照顧感受重要。使用者犯錯時立刻說明，不因感受迴避，這是強硬規則
- 在對任務採取行動之前先告訴我你的計畫。等我允許之後才開始執行

## 寫作風格

<!-- 選填：如果你有特定的寫作風格偏好，在此描述。/init-llm 會協助你填寫。 -->
<!-- 範例結構：
**結構**：從真實故事出發 → 反轉（打破預期）→ 帶著疑惑反思 → 留下沒有答案的問題

**慣用語模式**：
- 用「既⋯⋯又⋯⋯」表達矛盾感受，不輕易下單一結論
- 用「或許」、「可能」保留不確定性
- 問完問題不給答案，讓問題懸著

**避免的 AI 寫作味**：
- 不用「總結來說」、「綜上所述」收尾
- 不在問完問題後立刻給答案
- 不以統計數據為主要說服力
-->

---

## Vault 概覽

這是一個個人知識管理 Vault，內容以 **[YOUR_DOMAIN]** 為核心，以 Obsidian 管理，內容以 **[YOUR_LANGUAGE]** 為主。

**最後設置日期**：[DATE]

## 知識庫架構（raw / wiki / brainstorming / artifacts）

基於 Karpathy 的 LLM Knowledge Base 工作流，把原始資料、編譯產物、思考探索、成品四層分開。

```
vault/
├── raw/                    # 原始資料，只進不改（不管誰寫的，未經編譯加工）
│   ├── articles/           # 文章剪藏（origin: external）
│   ├── books/              # 書籍筆記（origin: external）
│   ├── podcasts/           # 播客轉錄（origin: external）
│   ├── papers/             # 學術論文（origin: external）
│   ├── notes/              # 隨手靈感筆記（origin: self）
│   └── projects/           # 專案相關原始資料（origin: self）
│
├── wiki/                   # 編譯產物，由 LLM 維護，不手動改
│   ├── indexes/            # All-Sources.md, All-Concepts.md
│   ├── concepts/           # 概念條目（交叉引用）
│   ├── summaries/          # 逐篇摘要
│   └── log.md              # 操作紀錄（compile、query、health-check）
│
├── brainstorming/          # 思考與探索
│   ├── chat/               # 問答沉澱（每次複雜提問的結果）
│   └── health/             # /health-check 產出的知識庫品質報告
│
├── artifacts/              # 個人成品與對外產出（origin: self）
│   └── projects/           # 進行中的專案
│   # 依領域自訂子資料夾，如：文章/、教學記錄/、書稿/、簡報/ 等
│
└── attachments/            # 圖片、PDF 等附件
```

## 編譯規範

### 摘要結構（wiki/summaries/）

#### 外部來源（raw/ → wiki/summaries/）

```yaml
---
origin: external
source: "[[YYYYMMDD 標題]]"
compiled: YYYY-MM-DD
tags: [標籤1, 標籤2]
---
# 核心結論
# 關鍵證據
# 疑點
# 術語
```

#### 自有作品（artifacts/ → wiki/summaries/）

```yaml
---
origin: self
source: "[[作品標題]]"
compiled: YYYY-MM-DD
tags: [標籤1, 標籤2]
---
# 我的主張
# 實踐經驗（什麼有效、什麼沒用）
# 未解決的問題
# 跟外部研究的對照
```

### 概念條目（wiki/concepts/）

```yaml
---
concept: 概念名稱
related: [相關概念1, 相關概念2]
updated: YYYY-MM-DD
sources:
  - "[[來源1]]"
---
# 概念名稱

## 定義

## 我的實踐
（從自有作品編譯：怎麼用這個概念、實際上發生了什麼、踩過什麼坑）

## 外部觀點
（從外部來源編譯：研究怎麼說、別人怎麼定義）

## 張力與缺口
（自己的經驗跟外部研究之間的矛盾，或還沒驗證過的部分）

## 例子

## 來源
### 自己的
### 外部的
```

### 問答沉澱（brainstorming/chat/）

```yaml
---
question: "問題"
asked_at: YYYY-MM-DD
sources: [[[摘要1]], [[摘要2]]]
---
# TL;DR
# 結論
# 證據
# 不確定性
```

## 筆記分類

Vault 包含以下類型文件：

1. **原始剪藏**：文章、Podcast、研討會紀錄 → `raw/`
2. **編譯知識**：概念條目、摘要、索引 → `wiki/`
3. **問答輸出**：複雜提問的推理結果 → `brainstorming/chat/`
4. **成品作品**：文章、專案成果與對外產出 → `artifacts/`
5. **隨手靈感**：隨時記下的想法（YYYYMMDD 命名）→ `raw/notes/`

## 核心主題

<!-- 列出你的 3-5 個核心主題。/init-llm 會協助你填寫。範例：
- **個人知識管理**：建立可持續的知識系統與工作流
- **AI 輔助學習**：用 LLM 加速理解與產出
- **寫作方法論**：從靈感到成品的寫作流程
-->

## 命名慣例

- 有日期的筆記：`YYYYMMDD 主題.md`（如 `20250608 Anthropic AI fluency Course.md`）
- 書籍摘要：`書名 - 作者.md`
- 概念條目：`概念名稱.md`
- 進行中的文件可能包含「還在寫」或「未完」標記

## 常用工作流程

### 搜尋內容
- 使用 Grep 在多個筆記中搜尋主題
- 使用 Glob 找特定命名模式的檔案

### 整理筆記（編譯流程）
- 捕捉：新內容放進 `raw/`（文章 → articles/，靈感 → notes/）
- 編譯：累積 5-10 篇後，執行 `/compile` 讓 LLM 讀 raw/ 最新檔案，生成摘要、提取概念、更新索引
- 問答：複雜提問的結果存到 `brainstorming/chat/`，帶推理過程和來源連結
- 定期健康檢查：定期執行 `/health-check` 讓 LLM 掃 wiki/，輸出 `brainstorming/health/` 報告
- 操作紀錄：每次 compile、query、health-check 自動 append 到 `wiki/log.md`
- 使用 `mv`（不用 `cp`）避免重複

### 分析主題
- 跨多份文件找出模式
- 為長文件建立摘要
- 擷取研究筆記中的關鍵概念

## Git 版本控制

- 提交格式：`vault backup: YYYY-MM-DD HH:MM:SS`
- 主要分支：`main`

## 可用指令

```
/init-llm             # 新使用者互動式設定
/compile              # 編譯 raw/ 與 artifacts/ 成 wiki/
/health-check         # 知識庫健康檢查
/thinking-partner     # 協作思考夥伴
/write-partner        # 動筆前的寫作探索
/braindump            # 把對話沉澱成可複用的素材
```

## 重要說明

- 這是個人知識管理 Vault，不是軟體專案
- 沒有建置指令、lint 或測試流程
- 內容以研究與寫作為主
- 進行中的文件請視為草稿處理
- 除非明確要求，保留 [YOUR_LANGUAGE] 內容不翻譯
