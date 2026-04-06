---
allowed-tools: Read, Write, Edit, Bash, Glob
description: '將 EPUB / PDF / DOCX 檔案（或整個資料夾）轉成 Obsidian Markdown'
argument-hint: '<檔案或資料夾路徑，如 mybook.epub、report.pdf、~/Downloads/books/ 或 Facebook 匯出資料夾>'
---

# 轉檔：EPUB / PDF / DOCX / Facebook JSON → Obsidian Markdown

將電子書、報告、文件或社群平台匯出轉成乾淨的 Markdown。

| 來源格式 | 輸出位置 | 媒體位置 |
|----------|---------|---------|
| EPUB / PDF / DOCX | `raw/books/` | `raw/books/assets/` |
| Facebook JSON 匯出 | `raw/notes/social/facebook/` | `raw/notes/social/facebook/assets/` |

## 輸入

`$ARGUMENTS` 為檔案或資料夾路徑。

- **單一檔案**：轉換該檔案（支援 `.epub`、`.pdf`、`.docx`）
- **資料夾（書籍）**：掃描資料夾內所有 `.epub`、`.pdf`、`.docx`，逐一轉換
- **資料夾（Facebook 匯出）**：偵測到 `your_facebook_activity/` 子目錄時，自動走 Facebook 轉換路徑
- 若無提供，問使用者：「請提供要轉換的檔案或資料夾路徑」

---

## 流程

### Step 0：確認環境

檢查必要工具，缺少則安裝或提示使用者：

```bash
pandoc --version 2>&1 | head -1          # EPUB、DOCX 都需要
python3 -c "import fitz; print('OK')"    # PDF 需要 pymupdf
```

- pandoc 未安裝 → 提示：`brew install pandoc`
- pymupdf 未安裝 → 執行：`pip3 install pymupdf`

### Step 1：判斷輸入類型

```bash
# 判斷是檔案還是資料夾
if [ -d "$ARGUMENTS" ]; then
  # 先檢查是否為 Facebook 匯出（含 your_facebook_activity/ 子目錄）
  if [ -d "$ARGUMENTS/your_facebook_activity" ]; then
    echo "FACEBOOK_EXPORT"
  else
    # 一般資料夾：列出所有支援的檔案
    find "$ARGUMENTS" -maxdepth 1 -type f \( -iname "*.epub" -o -iname "*.pdf" -o -iname "*.docx" \)
  fi
else
  # 單一檔案
  file "$ARGUMENTS"
fi
```

- **若偵測到 Facebook 匯出** → 跳至「Facebook JSON 路徑」
- **若為一般資料夾**，列出找到的檔案清單，告訴使用者即將轉換哪些檔案，確認後逐一執行 Step 2-7
- **若為單一檔案** → 依副檔名走對應路徑

### Step 2：提取書名與 metadata

| 格式 | 方法 |
|------|------|
| EPUB | pandoc metadata 或解壓讀 `nav.xhtml` |
| PDF | `fitz.open(path).metadata['title']` |
| DOCX | `pandoc --metadata` 或讀 `docProps/core.xml` |

若提取失敗，用檔名（去副檔名）當書名。

產出檔名：`raw/books/{書名}.md`

### Step 3：轉換

---

#### EPUB 路徑

1. **pandoc 轉換**（`--wrap=none` 避免斷行）：
```bash
pandoc "$FILE" -t markdown --wrap=none --extract-media=raw/books/assets -o raw/books/{書名}_raw.md
```

2. **後處理**：
   - 移除 pandoc 屬性：`{.class}`、`[]{#id}`、`::: div`
   - 移除翻譯外掛殘留（`.immersive-translate-*`、`.notranslate`）
   - 圖片路徑改為相對路徑
   - 中英文間距統一（pangu spacing）
   - `------` → `——`
   - 移除行首殘留 `]` `[`
   - 移除索引頁和廣告頁

3. **圖片**：加書名前綴避免衝突，更新 markdown 路徑

---

#### PDF 路徑

1. **用 pymupdf 提取結構**：
```python
import fitz
doc = fitz.open(filepath)
toc = doc.get_toc()
```

2. **逐頁提取文字**，利用 TOC 建立標題層級：
   - TOC level 1 → `##`，level 2 → `###`，level 3 → `####`

3. **清理**：
   - 偵測並移除重複的頁首頁尾文字
   - 移除頁碼行（獨立數字、含 private use area unicode 的行）
   - 合併斷行（非結構性連續行）
   - 中英文間距統一

4. 移除索引、廣告等無用頁面

---

#### DOCX 路徑

1. **pandoc 轉換**：
```bash
pandoc "$FILE" -t markdown --wrap=none --extract-media=raw/books/assets -o raw/books/{書名}_raw.md
```

2. **後處理**（與 EPUB 類似但通常更乾淨）：
   - 移除 pandoc 屬性標記
   - 圖片路徑改為相對路徑
   - 中英文間距統一
   - 清理多餘空行

3. **圖片**：pandoc `--extract-media` 會自動提取 docx 內嵌圖片

---

### Step 4：加上 Frontmatter

```yaml
---
title: "書名"
origin: external
type: book / report / document
publisher: "出版社"  # 若能提取
year: YYYY           # 若能提取
isbn: "ISBN"         # 若能提取（EPUB/PDF）
---
```

### Step 5：程式碼區塊語法高亮

將 pandoc 輸出的 4-space 縮排程式碼區塊，轉換成帶語言標籤的 fenced code block。

**語言偵測邏輯**（依序判斷）：

| 條件 | 語言標籤 |
|------|----------|
| 開頭是 shell 指令（`npm`、`node`、`pnpm`、`tsc`、`git`、`cd`、`pip`、`python`、`brew` 等） | `bash` |
| 符合 TypeScript 關鍵字（`const`、`let`、`type`、`interface`、`class`、`import`、`export`、`=>`、`: string` 等） | `typescript` |
| 符合 Python 關鍵字（`def`、`import`、`class`、`for`、`if __name__`、`print(`、`#!python` 等） | `python` |
| 符合 JSON 結構（開頭是 `{`、`[`，加上 `"key":` 模式） | `json` |
| 符合 YAML（`key: value` 模式，含 `---`） | `yaml` |
| 符合 HTML/XML（`<html`、`<div`、`<?xml` 等） | `html` |
| 符合 CSS（`.class {`、`#id {`、`@media` 等） | `css` |
| 符合 SQL（`SELECT`、`FROM`、`WHERE`、`INSERT` 等） | `sql` |
| 符合 Go（`func `、`package `、`:=`） | `go` |
| 符合 Rust（`fn `、`let mut`、`impl `、`use `） | `rust` |
| 符合錯誤訊息（`Type `、`Cannot `、`Error:`、`'x' is `、`Argument of type` 等） | （無標籤，純 ` ``` `） |
| 其他 | `typescript`（EPUB/DOCX 技術書預設）或 `text`（非技術文件） |

**實作**：用 Python 逐行掃描，偵測縮排區塊的起止範圍，判斷語言後套用 ` ```lang ` 圍欄。

### Step 6：最終清理

- 移除臨時檔案（`*_raw.md`、解壓的臨時目錄）
- 確認 markdown 語法正確
- 計算行數和圖片數量

### Step 7：回報結果

告知使用者每個檔案的：
- 產出路徑和大小
- 跳過的部分
- 需注意的限制

若為批次模式，最後給一個總覽表：

| 檔案 | 格式 | 產出 | 大小 |
|------|------|------|------|
| book1.epub | EPUB | raw/books/Book1.md | 245 KB |
| report.pdf | PDF | raw/books/Report.md | 872 KB |

---

## 清理規則清單

| 問題 | 處理 |
|------|------|
| pandoc `{.class}` 屬性 | 正則移除 |
| `[]{#anchor}` 空錨點 | 移除 |
| `::: div` 標記 | 移除 |
| 沉浸式翻譯殘留 | 移除 `.immersive-translate-*` |
| 圖片路徑 | 改為相對路徑 `assets/...` |
| 中英文間距 | CJK 與 ASCII 之間加空格 |
| `------` 破折號 | 改為 `——` |
| PDF 頁首頁尾 | 偵測重複文字模式並移除 |
| PDF 頁碼 | 移除獨立數字行及含 PUA unicode 的行 |
| PDF/EPUB 斷行 | 合併非結構性連續行 |
| 多餘空行 | 3+ 行壓縮為 2 行 |
| 4-space 縮排程式碼區塊 | 轉換為帶語言標籤的 fenced code block（見 Step 5） |

---

## Facebook JSON 匯出路徑

當 Step 1 偵測到資料夾內含 `your_facebook_activity/` 子目錄時，走此路徑。

### 背景

Facebook「下載你的資訊」匯出為 JSON 格式，文字使用 latin1-encoded UTF-8（需解碼修正），貼文、媒體、連結分散在不同欄位中。

### 轉換方式

使用 `.claude/scripts/facebook_to_md.py` 腳本：

```bash
python3 .claude/scripts/facebook_to_md.py "$ARGUMENTS" [自訂輸出目錄]
```

輸出目錄預設為 `raw/notes/social/facebook/`。

### 腳本行為

1. **自動尋找**資料夾內的 `your_posts__check_ins__photos_and_videos_1.json`
2. **修正編碼**：`text.encode('latin1').decode('utf-8')` 解決 Facebook JSON 的中文亂碼
3. **過濾**：只轉換有文字內容（`data[].post` 有值）的貼文，純分享/轉貼跳過
4. **命名**：`YYYYMMDD-N 貼文前20字.md`（同日多則用流水號區分）
5. **媒體**：複製對應圖片/影片到 `assets/` 子目錄，MD 中用 `![[assets/檔名]]` 引用
6. **連結**：外部連結列在 `## 連結` 區段
7. **Frontmatter**：
   ```yaml
   ---
   origin: self
   source: facebook
   date: YYYY-MM-DD
   timestamp: 原始 Unix timestamp
   tags: [facebook]
   ---
   ```

### 回報結果

腳本會印出：
- 總貼文數、有文字貼文數
- 建立的 MD 檔數量
- 複製的媒體檔數量
- 輸出路徑

---

## 注意事項

- EPUB 和 DOCX 的轉換品質通常優於 PDF（有結構資訊）
- PDF 不提取圖片，只轉換文字內容
- 批次模式下若某個檔案失敗，跳過它並繼續處理其他檔案，最後回報失敗清單
- 若 `raw/books/` 已有同名 .md 檔案，詢問使用者是否覆蓋
- Facebook 匯出若 `raw/notes/social/facebook/` 已有檔案，會覆蓋同名檔案
- 轉換後建議在 Obsidian 中開啟確認格式
