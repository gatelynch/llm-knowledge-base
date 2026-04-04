# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this knowledge base.

---

## About You

<!-- Customize this section. Tell your LLM who you are and how you work. -->

- **Name**: [YOUR_NAME]
- **Role**: [YOUR_ROLE — e.g., "teacher", "researcher", "designer"]
- **Language**: [YOUR_LANGUAGE — e.g., "English", "繁體中文", "日本語"]
- **Interaction style**: [e.g., "Ask before acting", "Be direct about errors", "First-principles thinking"]

## Vault Overview

This is a personal knowledge management vault. Content is centered on **[YOUR_DOMAIN]** and managed with Obsidian. The primary language is **[YOUR_LANGUAGE]**.

## Knowledge Base Architecture (raw / wiki / brainstorming / artifacts)

Based on Karpathy's LLM Knowledge Base workflow — separating raw materials, compiled knowledge, exploration, and finished works into four layers.

```
vault/
├── raw/                    # Raw materials — read-only, never edited after capture
│   ├── articles/           # Clipped articles (origin: external)
│   ├── books/              # Book notes (origin: external)
│   ├── podcasts/           # Podcast transcripts (origin: external)
│   ├── papers/             # Academic papers (origin: external)
│   ├── notes/              # Quick personal notes (origin: self)
│   └── projects/           # Project-related raw material (origin: self)
│
├── wiki/                   # Compiled knowledge — maintained by LLM, not edited manually
│   ├── indexes/            # All-Sources.md, All-Concepts.md
│   ├── concepts/           # Concept entries (cross-referenced)
│   └── summaries/          # Per-source summaries
│
├── brainstorming/          # Thinking & exploration
│   ├── chat/               # Q&A logs (complex queries with reasoning)
│   └── health/             # Health check reports (consistency, completeness, connectivity)
│
├── artifacts/              # Finished works & personal output (origin: self)
│   └── projects/           # Active projects
│   # Add your own subfolders: essays/, teaching/, blog/, etc.
│
├── attachments/            # Images, PDFs, etc.
└── templates/              # Obsidian templates
```

## Compilation Specs

### Summary Structure (wiki/summaries/)

#### External Sources (raw/ → wiki/summaries/)

```yaml
---
origin: external
source: "[[Original File Name]]"
compiled: YYYY-MM-DD
tags: [tag1, tag2]
---

# Title

## Core Conclusion
(1-3 sentences — the most important takeaway)

## Key Evidence
(Specific facts, data, quotes supporting the conclusion)

## Open Questions
(Uncertain, controversial, or unverified claims)

## Key Terms
(Important terms introduced in this source, with brief definitions)
```

#### Self-Authored Works (artifacts/ → wiki/summaries/)

```yaml
---
origin: self
source: "[[Your Work File Name]]"
compiled: YYYY-MM-DD
tags: [tag1, tag2]
---

# Title

## My Claims
(Core argument or goal of this piece)

## Practice Experience
(What worked, what didn't, what actually happened)

## Unresolved Questions
(Questions that remain open after writing or doing this)

## Comparison with Research
(How your experience aligns with or contradicts known research)
```

### Concept Entries (wiki/concepts/)

```yaml
---
concept: Concept Name
related: [Related Concept 1, Related Concept 2]
updated: YYYY-MM-DD
sources:
  - "[[Source 1]]"
---

# Concept Name

## Definition

## My Practice
(Compiled from origin: self sources — how you use this concept, what happened, what you learned)

## External Perspectives
(Compiled from origin: external sources — what research says, how others define it)

## Tensions & Gaps
(Contradictions between your experience and external research, or things not yet verified)

## Examples

## Sources
### Mine
### External
```

### Q&A Logs (brainstorming/chat/)

```yaml
---
question: "The question"
asked_at: YYYY-MM-DD
sources: [[[Summary 1]], [[Summary 2]]]
---

# TL;DR
# Conclusions
# Evidence
# Uncertainties
```

## Note Categories

1. **Raw clips**: Articles, podcasts, papers → `raw/`
2. **Compiled knowledge**: Concept entries, summaries, indexes → `wiki/`
3. **Q&A output**: Complex query results with reasoning → `brainstorming/chat/`
4. **Finished works**: Your articles, projects, output → `artifacts/`
5. **Quick thoughts**: Ideas captured on the fly (YYYYMMDD naming) → `raw/notes/`

## Naming Conventions

- Dated notes: `YYYYMMDD Topic.md` (e.g., `20250608 Anthropic AI Fluency Course.md`)
- Book summaries: `Book Title - Author.md`
- Concept entries: `Concept Name.md`

## Standard Workflows

### Capturing Content
- New external content goes into `raw/` (articles → articles/, ideas → notes/)
- New personal works go into `artifacts/`

### Compiling Knowledge
- After accumulating 5-10 new files, run `/compile`
- The LLM reads new files in raw/ and artifacts/, generates summaries, extracts concepts, updates indexes
- Use `mv` (not `cp`) when reorganizing to avoid duplicates

### Exploring Topics
- Run `/thinking-partner` for deep exploration of a topic
- Q&A results are saved to `brainstorming/chat/` with reasoning and source links

### Quality Maintenance
- Run `/health-check` periodically to scan wiki/ for issues
- Reports go to `brainstorming/health/`

## 可用指令

```
/init-llm             # 新使用者互動式設定
/compile              # 編譯 raw/ 與 artifacts/ 成 wiki/
/health-check         # 知識庫健康檢查
/thinking-partner     # 協作思考夥伴
/write-partner        # 動筆前的寫作探索
/braindump            # 把對話沉澱成可複用的素材
```
