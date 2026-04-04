# 工作流程

這份文件抽出與模型供應商無關的操作規格。`CLAUDE.md` 與 `AGENTS.md` 都應該引用這裡，而不是各自維護一份不同版本的流程描述。

## Origin 對應

依照路徑判斷 `origin`：

- `raw/articles/` → `external`
- `raw/books/` → `external`
- `raw/podcasts/` → `external`
- `raw/papers/` → `external`
- `raw/notes/` → `self`
- `raw/projects/` → `self`
- `artifacts/` 下所有檔案 → `self`

## Compile

目標：把 `raw/` 與 `artifacts/` 的新內容編譯成 `wiki/` 裡的摘要、概念與索引。

### 步驟

1. 決定處理範圍
2. 找出尚未編譯的新檔案
3. 依路徑判斷 `origin`
4. 為每個來源生成摘要，寫入 `wiki/summaries/`
5. 從摘要中提取概念，建立或更新 `wiki/concepts/`
6. 更新 `wiki/indexes/All-Sources.md`
7. 如果出現新概念，更新 `wiki/indexes/All-Concepts.md`

### 摘要格式

- `origin: external`：核心結論 → 關鍵證據 → 疑點 → 術語
- `origin: self`：我的主張 → 實踐經驗 → 未解問題 → 與研究的對照

### 原則

- 不修改 `raw/` 或 `artifacts/` 原始內容
- 每份摘要都必須保留 `source`
- 概念條目優先分開「我的實踐」與「外部觀點」
- 只有在 2 份以上摘要都涉及同一概念時，才建立獨立概念條目

## Thinking Partner

目標：協助使用者探索複雜問題，而不是急著得出答案。

### 步驟

1. 理解主題或困惑
2. 搜尋 vault 中的相關材料
3. 提出 3 到 5 個釐清問題
4. 追蹤對話中浮現的洞見、關聯與未解問題
5. 在適當時總結目前輪廓

### 原則

- 先問再答
- 優先幫助使用者澄清與深化
- 避免過早收斂成單一答案

## Write Partner

目標：在使用者正式寫作之前，先整理已有材料、反例、張力與開放問題。

### 步驟

1. 理解要寫的主題或草稿
2. 搜尋 `wiki/` 中的摘要與概念
3. 搜尋 `artifacts/` 中相關的既有作品與實踐紀錄
4. 找出支持觀點、反例、矛盾與尚未解決的問題
5. 產出一份可用來動筆的探索整理

## Braindump

目標：把一次對話沉澱成可以重用的知識素材。

### 輸出位置

- 問答記錄、探索過程、草稿片段都存到 `brainstorming/chat/`

### 原則

- 優先保留推理脈絡，而不只是結論
- 讓後續的 `compile` 或寫作能重用這些內容

## Health Check

目標：檢查 `wiki/` 的一致性、完整性與連結品質。

### 檢查方向

- 是否有摘要缺少必要段落
- 是否有概念條目缺少來源或交叉引用
- 是否有索引未更新
- 是否存在孤立概念或重複概念
- 是否有摘要與概念之間的連結斷裂

### 輸出位置

- 將檢查結果寫入 `brainstorming/health/`
