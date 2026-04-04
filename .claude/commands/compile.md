---
name: compile
description: 'Compile raw/ and artifacts/ into wiki/ (summaries, concepts, indexes)'
argument-hint: '[folder path or file count, e.g., raw/articles 10 or artifacts/essays]'
---

# Knowledge Base Compilation

Compile raw/ (source material) and artifacts/ (your works) into structured knowledge in wiki/.

## Process

### 1. Determine Compilation Scope

- If the user specifies a path or count, process that scope
- If unspecified, read wiki/indexes/All-Sources.md, compare against raw/ and artifacts/ to find **new uncompiled files**
- If new files exceed 15, inform the user and suggest batching (10-15 per batch)

### 2. Determine Source Type

Automatically determine `origin` based on the file's subfolder path:

**origin: external** (external sources — written by others)
- `raw/articles/`
- `raw/books/`
- `raw/podcasts/`
- `raw/papers/`

**origin: self** (your own — written by the user)
- `raw/notes/`
- `raw/projects/`
- `artifacts/*`

### 3. Read Each Source File

Read each file and understand its content. Process most recent files first (sorted by date).

### 4. Generate Summaries (wiki/summaries/)

Produce one summary per source. Filename format: `YYYYMMDD Short-Title.md`

#### External Sources (origin: external)

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

#### Self-Authored Works (origin: self)

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

### 5. Extract or Update Concepts (wiki/concepts/)

Identify concepts from summaries. Filename format: `Concept Name.md`

- **New concepts**: Create entry

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
(Compiled from origin: self sources — how you use this concept, what happened, lessons learned)

## External Perspectives
(Compiled from origin: external sources — what research says, how others define it)

## Tensions & Gaps
(Contradictions between your experience and external research, or things not yet verified)

## Examples

## Sources
### Mine
### External
```

- **Existing concept update rules**:
  - Append new source to the sources list
  - Route new content to the appropriate section based on origin: `origin: self` → "My Practice", `origin: external` → "External Perspectives"
  - If a concept has both self and external sources, review whether "Tensions & Gaps" needs updating
  - Add new examples to "Examples"
  - Update the `updated` date
  - Route sources to "Mine" or "External" in the sources list

### 6. Update Indexes (wiki/indexes/)

- **All-Sources.md**: Add a row for each newly compiled source (source, tags, key takeaway, status)
- **All-Concepts.md**: If new concept entries were created, add a row (concept, entry link, definition, related concepts)

### 7. Report Results

Tell the user:
- How many files were compiled (broken down by external vs self)
- Which summaries were created
- Which concepts were created or updated
- Index update status

## Compilation Principles

- **Never modify raw/ or artifacts/**: Source materials are read-only
- **source is required**: Every summary must have a wikilink back to the original file
- **origin is required**: external or self, auto-determined from source path
- **Open Questions must not be empty** (external): If no issues found, write "This source's arguments are well-supported; no significant open questions identified"
- **Concepts require cross-references**: Only create a standalone concept entry if it's mentioned in 2+ summaries. Single mentions go in the summary's Key Terms section
- **No filename prefixes**: Don't add S-, C- or similar prefixes to summary or concept filenames
- **User-first perspective in concept entries**: "My Practice" comes before "External Perspectives"
