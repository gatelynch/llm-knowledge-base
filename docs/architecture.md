# Architecture: The Four-Layer Knowledge System

## Why Four Layers?

Most personal knowledge systems have one fatal flaw: **raw materials and processed understanding live in the same place**. You clip an article, maybe highlight a few lines, and it sits next to your own half-formed thoughts. Over time, everything blurs together.

This system enforces a strict separation:

```
raw/            → The library         (what you've collected)
wiki/           → The encyclopedia    (what you've understood)
brainstorming/  → The lab notebook    (what you're exploring)
artifacts/      → The publications    (what you've produced)
```

## Layer 1: raw/ — The Library

**Rule: read-only after capture.** Once a file enters raw/, it never gets edited. This preserves the original source exactly as you found it.

Why this matters: When you compile a summary months later, you want the original — not a version you've already rewritten through your current lens. Raw materials are evidence. Don't tamper with evidence.

**Subfolders by source type:**
- `articles/` — Web articles, blog posts, newsletters
- `books/` — Book notes, highlights, chapter summaries
- `podcasts/` — Transcripts, episode notes
- `papers/` — Academic papers, research reports
- `notes/` — Your quick thoughts, captured ideas (origin: self)
- `projects/` — Project-related raw material (origin: self)

## Layer 2: wiki/ — The Encyclopedia

**Rule: maintained by LLM, not edited manually.** This is where compilation happens. The LLM reads raw/ and produces structured knowledge here.

Three types of compiled output:

### Summaries (wiki/summaries/)
One per source. Two formats based on origin:
- **External**: Core Conclusion → Key Evidence → Open Questions → Key Terms
- **Self**: My Claims → Practice Experience → Unresolved Questions → Comparison with Research

### Concepts (wiki/concepts/)
Cross-referenced entries that emerge when a term appears in 2+ summaries. Each concept separates **your practice** from **external perspectives**, with a dedicated "Tensions & Gaps" section.

This is the core design decision: your experience and the research exist side by side, and contradictions are surfaced, not buried.

### Indexes (wiki/indexes/)
Two master tables:
- **All-Sources.md** — Every compiled source with tags and key takeaway
- **All-Concepts.md** — Every concept entry with definition and related concepts

## Layer 3: brainstorming/ — The Lab Notebook

**Rule: exploration outputs, not polished work.** This is where you think out loud with the LLM.

- `chat/` — Q&A logs from complex queries (with reasoning, sources, and uncertainties)
- `health/` — Health check reports that track the quality of your wiki/ over time

## Layer 4: artifacts/ — The Publications

**Rule: your finished works.** Articles you've written, teaching materials, project deliverables — anything you've produced that represents your thinking.

These get compiled into wiki/ just like external sources, but with `origin: self` — so your practice experience feeds into concept entries alongside external research.

## The Compilation Flow

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

## Why Origin Matters

Every source is tagged as either `origin: external` or `origin: self`. This distinction flows through the entire system:

- **Summaries** use different section headers based on origin
- **Concepts** route content to "My Practice" (self) or "External Perspectives" (external)
- **Tensions & Gaps** only become meaningful when both origins are present

The goal is not to blend everything into a single narrative, but to maintain the productive tension between what you've experienced and what others have found.
