# 架構：四層知識系統

## 為什麼是四層？

大多數個人知識系統都有一個致命缺陷：**原始材料與加工後的理解混在同一個地方**。你剪藏一篇文章，也許畫了幾段重點，然後它就和你那些尚未成形的想法並排放在一起。久而久之，一切都糊成一團。

這個系統強制維持明確分層：

```
raw/            → 圖書館         （你收集了什麼）
wiki/           → 百科全書       （LLM整理了什麼）
brainstorming/  → 實驗筆記本     （你正在探索什麼）
artifacts/      → 發表成果       （你產出了什麼）
```

## 第 1 層：`raw/` — 圖書館

**規則：收進來之後就是唯讀。** 一旦檔案進入 `raw/`，就不再編輯。這能保留來源最原始的樣子。

為什麼這很重要：幾個月後你回來編譯摘要時，你需要的是原始版本，而不是一份已經被你用當下視角重寫過的版本。原始材料就是證據，不要動證據。

**依來源類型分的子資料夾：**
- `articles/` — 網路文章、部落格文章、電子報
- `books/` — 書籍筆記、畫線、章節摘要
- `podcasts/` — 逐字稿、單集筆記
- `papers/` — 學術論文、研究報告
- `notes/` — 你的即時想法、隨手記錄的靈感（`origin: self`）
  - `social/` — 社群平台匯入（`facebook/` 等，`origin: self`）
- `projects/` — 與專案相關的原始材料（`origin: self`）

## 第 2 層：`wiki/` — 百科全書

**規則：由 LLM 維護，不手動編輯。** 這是發生編譯的地方。LLM 讀取 `raw/`，並在這裡產生結構化知識。

編譯後會產生三種輸出：

### 摘要（`wiki/summaries/`）
每個來源一份。依照 `origin` 分成兩種格式：
- **External**：Core Conclusion → Key Evidence → Open Questions → Key Terms
- **Self**：My Claims → Practice Experience → Unresolved Questions → Comparison with Research

### 概念（`wiki/concepts/`）
當某個詞在 2 篇以上摘要中出現時，就會長出一篇交叉引用的概念條目。每個概念都會把**你的實踐**和**外部觀點**分開，並有一個專門的「Tensions & Gaps」區段。

這是核心設計決策：你的經驗與研究並排存在，矛盾會被浮現出來，而不是被埋掉。

### 索引（`wiki/indexes/`）
兩份總表：
- **All-Sources.md** — 所有已編譯來源，附上標籤與關鍵收穫
- **All-Concepts.md** — 所有概念條目，附上定義與相關概念

## 第 3 層：`brainstorming/` — 實驗筆記本

**規則：放探索過程，不放打磨完成的作品。** 這是你和 LLM 一起大聲思考的地方。

- `chat/` — 複雜問題的問答紀錄（包含推理、來源與不確定性）
- `health/` — 健康檢查報告，用來追蹤你的 `wiki/` 品質隨時間的變化

## 第 4 層：`artifacts/` — 發表成果

**規則：放你的完成品。** 你寫的文章、教學材料、專案交付物，任何能代表你思考的產出都放在這裡。

這些內容也會像外部來源一樣被編譯進 `wiki/`，但它們的 `origin` 會是 `self`。因此，你的實踐經驗會和外部研究一起進入概念條目。

## 編譯流程

```
raw/articles/new-paper.md
        ↓ /compile
wiki/summaries/20250615 New-Paper.md
        ↓ concept extraction
wiki/concepts/Concept-Name.md  (created or updated)
        ↓ index update
wiki/indexes/All-Sources.md    (new row added)
wiki/indexes/All-Concepts.md   (new row if new concept)
```

## 為什麼 `origin` 很重要

每個來源都會被標記為 `origin: external` 或 `origin: self`。這個區分會影響整個系統：

- **摘要** 會依照 `origin` 使用不同的段落標題
- **概念條目** 會把內容分流到「My Practice」（self）或「External Perspectives」（external）
- **Tensions & Gaps** 只有在兩種來源都存在時才真正有意義

目標不是把所有東西混成單一敘事，而是保留你親身經驗與他人研究之間那種有生產力的張力。
