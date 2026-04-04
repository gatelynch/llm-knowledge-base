# 自訂指南

## 語言

系統預設以英文作為結構語言（資料夾名稱、段落標題），但你可以調整輸出語言。

### 步驟 1：在 `CLAUDE.md` 設定你的語言

```yaml
- **Language**: 繁體中文
```

### 步驟 2：自訂段落標題

在 `CLAUDE.md` 中，修改編譯規格裡的段落標題。例如，繁體中文可以這樣設定：

| English (default) | 繁體中文 | 日本語 |
|-------------------|---------|--------|
| Core Conclusion | 核心結論 | 核心的結論 |
| Key Evidence | 關鍵證據 | 主要な証拠 |
| Open Questions | 疑點 | 未解決の疑問 |
| Key Terms | 術語 | 重要用語 |
| My Claims | 我的主張 | 私の主張 |
| Practice Experience | 實踐經驗 | 実践経験 |
| My Practice | 我的實踐 | 私の実践 |
| External Perspectives | 外部觀點 | 外部の視点 |
| Tensions & Gaps | 張力與缺口 | 緊張と課題 |

`/compile` 和 `/health-check` 會遵循你在 `CLAUDE.md` 中定義的段落標題。

## 領域

### 新增 `artifacts/` 子資料夾

範本預設只提供 `artifacts/projects/`。你可以依照自己的領域新增子資料夾：

**如果你是老師：**
```
artifacts/
├── lessons/
├── essays/
├── presentations/
└── projects/
```

**如果你是研究者：**
```
artifacts/
├── papers/
├── talks/
├── grant-proposals/
└── projects/
```

**如果你是開發者：**
```
artifacts/
├── blog-posts/
├── documentation/
├── talks/
└── projects/
```

### 新增 `raw/` 子資料夾

你也可以為特定輸入來源，在 `raw/` 下新增更多子資料夾。只要同步更新 `/compile` 指令中的 origin 對應，告訴 LLM 這些新資料夾屬於 `origin: external` 還是 `origin: self` 即可。

## 標籤

標籤應該和你的 vault 語言一致。專有名詞保留原文（例如 `Claude Code`、`Obsidian`），一般概念則翻成你選擇的語言。

## 寫作風格

如果你的領域有特定的寫作風格，可以在 `CLAUDE.md` 加上一個 `## Writing Style` 區段。這會影響 LLM 撰寫摘要與概念條目的方式。

## 額外指令

目前內建的三個指令（`/compile`、`/health-check`、`/thinking-partner`）涵蓋了核心工作流程。你也可以依照自己的需求，在 `.claude/commands/` 裡加入更多指令。如何建立自訂指令，請參考 [Claude Code 文件](https://docs.anthropic.com/en/docs/claude-code/tutorials#create-slash-commands)。
