---
name: compile
description: '編譯 raw/ 與 artifacts/ 成 wiki/（摘要、概念、索引）'
argument-hint: '[資料夾路徑或檔案數量，例如 raw/articles 10 或 artifacts/essays]'
---

# 知識庫編譯

把 raw/（素材）與 artifacts/（你的作品）編譯成結構化知識，存入 wiki/。

## 流程

### 1. 確認編譯範圍

- 如果使用者指定了路徑或數量，就處理那個範圍
- 如果沒有指定，讀取 wiki/indexes/All-Sources.md，與 raw/ 和 artifacts/ 比對，找出**尚未編譯的新檔案**
- 如果新檔案超過 15 個，告知使用者，建議分批處理（每批 10-15 個）

### 2. 判斷來源類型

根據檔案的子資料夾路徑自動判斷 `origin`：

**origin: external**（外部來源——他人撰寫）

- `raw/articles/`
- `raw/books/`
- `raw/podcasts/`
- `raw/papers/`

**origin: self**（自己的——使用者撰寫）

- `raw/notes/`
- `raw/projects/`
- `artifacts/*`

### 3. 讀取每個來源檔案

讀取每個檔案並理解其內容。依日期由新到舊處理。

### 4. 生成摘要（wiki/summaries/）

每個來源產出一份摘要。檔名格式：`YYYYMMDD 簡短標題.md`

#### 外部來源（origin: external）

```yaml
---
origin: external
source: "[[原始檔案名稱]]"
compiled: YYYY-MM-DD
tags: [tag1, tag2]
---

# 標題

## 核心結論
（1-3 句話——最重要的收穫）

## 關鍵證據
（支持結論的具體事實、數據、引述）

## 疑點
（不確定、有爭議或尚未驗證的主張）

## 術語
（這個來源引入的重要術語，附簡短定義）
```

#### 自己的作品（origin: self）

```yaml
---
origin: self
source: "[[你的作品檔名]]"
compiled: YYYY-MM-DD
tags: [tag1, tag2]
---

# 標題

## 我的主張
（這篇作品的核心論點或目標）

## 實踐經驗
（做了什麼、成效如何、實際發生了什麼）

## 未解問題
（寫完或做完後仍懸著的問題）

## 與研究的對照
（你的經驗如何與已知研究吻合或矛盾）
```

### 5. 提取或更新概念（wiki/concepts/）

從摘要中找出概念。檔名格式：`概念名稱.md`

**新概念**：建立條目

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
（從 origin: self 來源整理——如何使用這個概念、發生了什麼、學到什麼）

## 外部觀點
（從 origin: external 來源整理——研究怎麼說、他人如何定義）

## 張力與缺口
（你的經驗與外部研究之間的矛盾，或尚未驗證的地方）

## 例子

## 來源
### 我的
### 外部
```

**現有概念的更新規則**：

- 在 sources 清單中附加新來源
- 依 origin 把新內容路由到對應段落：`origin: self` → 「我的實踐」，`origin: external` → 「外部觀點」
- 如果概念同時有 self 和 external 來源，檢查「張力與缺口」是否需要更新
- 在「例子」中新增新例子
- 更新 `updated` 日期
- 在來源清單中將來源歸類至「我的」或「外部」

### 6. 更新索引（wiki/indexes/）

- **All-Sources.md**：為每個新編譯的來源新增一行（來源、標籤、核心收穫、狀態）
- **All-Concepts.md**：如果有新建概念條目，新增一行（概念、條目連結、定義、相關概念）

### 7. 回報結果

告訴使用者：

- 共編譯了多少個檔案（分 external 與 self）
- 建立了哪些摘要
- 建立或更新了哪些概念
- 索引更新狀態

## 編譯原則

- **不修改 raw/ 或 artifacts/**：素材是唯讀的
- **source 是必填欄位**：每份摘要都必須有 wikilink 指回原始檔案
- **origin 是必填欄位**：external 或 self，從來源路徑自動判斷
- **疑點不能留空**（external）：如果沒有發現問題，寫「這個來源的論點有充分支撐；沒有發現重大疑點」
- **概念需要交叉引用**：只有在 2 個以上摘要中出現的概念才建立獨立條目。單一提及放在摘要的「術語」段落即可
- **檔名不加前綴**：摘要與概念的檔名不加 S-、C- 等前綴
- **概念條目以使用者視角為主**：「我的實踐」在「外部觀點」之前
