# AGENTS.md

這份文件提供 Codex 與其他通用 agent 使用這個知識庫架構時的操作規則。

## 先讀這些文件

- `docs/architecture.md`
- `docs/workflows.md`
- `docs/examples/summary-external.md`
- `docs/examples/summary-self.md`
- `docs/examples/concept-entry.md`
- `docs/examples/qa-log.md`

## 核心架構

這是一個四層知識庫：

- `raw/`：原始素材，收進來後不再修改
- `wiki/`：LLM 編譯後的知識，不手動維護
- `brainstorming/`：探索、問答、健康檢查等中間輸出
- `artifacts/`：使用者自己的作品與完成品

## 操作規則

- 不要修改 `raw/` 裡已存在的檔案內容
- 讀取新素材後，將摘要寫入 `wiki/summaries/`
- 只在概念出現在 2 份以上摘要時建立或更新 `wiki/concepts/`
- 將索引寫入 `wiki/indexes/All-Sources.md` 與 `wiki/indexes/All-Concepts.md`
- 將探索式問答與推理紀錄存入 `brainstorming/chat/`
- 將健康檢查報告存入 `brainstorming/health/`
- 將 `artifacts/` 下的內容視為 `origin: self`
- 將 `raw/articles/`、`raw/books/`、`raw/podcasts/`、`raw/papers/` 視為 `origin: external`
- 將 `raw/notes/`、`raw/projects/` 視為 `origin: self`

## 工作流程對應

- `compile`：讀取 `raw/` 與 `artifacts/` 的新檔案，生成摘要、更新概念、更新索引
- `thinking partner`：針對一個複雜主題提出問題、搜尋相關筆記、整理暫時性結論
- `write partner`：為動筆前的寫作做資料蒐集，找出相關內容、反例、張力與未解問題
- `braindump`：把對話沉澱成可重用素材，存到 `brainstorming/chat/`
- `health check`：檢查 `wiki/` 的一致性、完整性與連結性問題

## 與 Claude 相容

- Claude 專用設定仍放在 `CLAUDE.md`
- Claude 專用 slash commands 仍放在 `.claude/commands/`
- 如果你是通用 agent，不要假設 `.claude/commands/` 會自動變成可呼叫命令；請依 `docs/workflows.md` 的行為規格執行等價流程
