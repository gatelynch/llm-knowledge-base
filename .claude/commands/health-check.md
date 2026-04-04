---
name: health-check
description: 'Knowledge base health check (consistency, completeness, connectivity)'
argument-hint: ''
---

# Knowledge Base Health Check

Periodically scan wiki/ for quality issues — inconsistencies, gaps, and isolated nodes — and produce an actionable repair report.

## Process

### 1. Scan All wiki/ Files

- Read all concept entries in wiki/concepts/
- Read all summaries in wiki/summaries/
- Read wiki/indexes/All-Sources.md and All-Concepts.md

### 2. Consistency Check

Check each of the following:

**Terminology Conflicts**
- Does the same term have contradictory definitions across different concept entries or summaries?
- Example: "RAG" defined as "Retrieval-Augmented Generation" in one entry but as "vector database search" in another

**Bidirectional Related Links**
- If Concept A lists B in its `related` field, check if B also lists A
- List all one-way links

**Naming Consistency**
- Are tags and concept names consistent across files?
- Common issues: variant spellings, inconsistent capitalization, synonyms used interchangeably

**Frontmatter Format**
- Do all sources use wikilink format `"[[xxx]]"`?
- Do all summaries have an `origin` field?
- Do all concept entries have an `updated` date?

### 3. Completeness Check

**Empty Concept Sections**
- Check whether each concept has empty or placeholder-only content in:
  - My Practice
  - External Perspectives
  - Tensions & Gaps
  - Examples
  - Sources (Mine / External)

**Potential New Concepts**
- Scan the "Key Terms" sections across all summaries
- Find terms mentioned in 2+ summaries that don't yet have a standalone concept entry
- List candidate concepts with occurrence count and sources

**Index Sync**
- Compare sources listed in All-Sources.md vs actual files in wiki/summaries/
- Find ghost entries (in index but file missing)
- Find unindexed files (file exists but not in index)

**Uncompiled Sources**
- Count .md files in raw/ and artifacts/ that don't appear in All-Sources.md
- Break down by subfolder

### 4. Connectivity Check

**Orphan Summaries**
- Which wiki/summaries/ files are not referenced by any wiki/concepts/ entry's sources?
- These summaries may contain concepts worth extracting

**Single-Source Concepts**
- Which wiki/concepts/ entries have only 1 source?
- Single-source concepts are fragile — suggest finding more supporting sources

**Missing Link Suggestions**
- Based on content similarity between concept entries, suggest `related` links that should exist but don't
- Based on tag co-occurrence across summaries, suggest potentially related concepts

### 5. Generate Report

Output to `brainstorming/health/YYYYMMDD Health-Check.md`

```yaml
---
date: YYYY-MM-DD
scope: wiki/
stats:
  concepts: N
  summaries: N
  uncompiled: N
---
```

Report structure:

```markdown
# Knowledge Base Health Check — YYYY-MM-DD

## Overview
(Concept count, summary count, uncompiled count, changes since last check)

## Consistency Issues
(Each issue with specific filenames and suggested fix)

## Completeness Gaps
(Empty sections, candidate new concepts, index sync issues)

## Connectivity Suggestions
(Orphan summaries, single-source concepts, suggested new links)

## Recommended Actions (by priority)
1. 🔴 Must fix: Consistency issues (cause confusion)
2. 🟡 Should fix: Completeness gaps (worth filling but not urgent)
3. 🟢 Nice to have: Connectivity improvements (enrichment)
```

### 6. Report Results

Tell the user:
- Total issue count (across three dimensions)
- Top 3 items to prioritize
- Report file path

## Check Principles

- **Read-only**: Health check only produces reports, never modifies wiki/ files directly
- **Actionable specifics**: Every issue must include a suggested fix, not vague advice
- **Compare with previous**: If brainstorming/health/ contains a prior report, compare changes (issues added/resolved)
- **No duplicate reporting**: The same issue should not appear in multiple sections
