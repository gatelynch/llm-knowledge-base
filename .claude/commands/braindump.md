---
name: braindump
description: 'Distill conversation insights into reusable material'
argument-hint: '[topic name, e.g., "rebuilding a second brain"]'
allowed-tools: Read, Write, Grep, Glob, AskUserQuestion
---

# Conversation Braindump

Distill the current conversation into reusable material, saved to `brainstorming/chat/`. Respond in the language set in CLAUDE.md.

## Process

### 1. Confirm Scope

Ask the user:

> How would you like to capture this conversation?
> 1. **Q&A log** — Record the discussion process, conclusions, and unresolved questions
> 2. **Article draft** — Generate an article outline from the conversation (requires your approval before writing)
> 3. **Both** (saved as separate files)

Wait for the user's answer before proceeding.

### 2. Determine Filename

Format: `brainstorming/chat/YYYYMMDD {Topic}.md`

- If `$ARGUMENTS` is provided, use it as the topic
- If not, extract a topic from the conversation content
- Q&A logs and article drafts get separate filenames, e.g.:
  - `20260404 Rebuilding a Second Brain Q&A.md`
  - `20260404 Rebuilding a Second Brain Draft.md`

### 3. Write Q&A Log

If the user chose option 1 or 3, write using this format:

```yaml
---
question: "The core question of this conversation (one sentence)"
asked_at: YYYY-MM-DD
sources: [[[Related vault files]]]
---
```

#### Content Structure

- **TL;DR**: 2-3 sentences summarizing the most important takeaways
- **Conclusions**: Insights formed during the conversation, organized by topic. Each point should be specific, not a vague summary
- **Evidence**:
  - Counterexamples and tensions surfaced during discussion
  - Supporting material from the vault (with `[[wikilinks]]`)
  - Concrete examples the user provided
- **Uncertainties**: Unresolved questions, open threads, contradictions not yet reconciled

#### Key Rules

- Distinguish "what the user said" from "what the AI proposed" — faithfully preserve the user's own words and positions
- If the user said "I haven't figured this out yet," record it as such — do not fill in answers for them
- Only list vault files in `sources` that were actually referenced or searched during the conversation

### 4. Write Article Draft

If the user chose option 2 or 3:

#### 4a. Propose an Outline First

Based on the conversation, generate a 3-5 section outline. Each section includes:
- Section title
- 1-2 sentences describing what it covers

The outline should follow the writing style in CLAUDE.md (if defined). General defaults:
- Start from a real story -> reversal -> reflective doubt -> end with an open question
- Don't wrap up with "in conclusion"
- Ask questions without answering them

**Show the outline to the user. Do not write until they approve or revise it.**

#### 4b. Write the Draft

After approval, write a full article draft and save to `brainstorming/chat/`.

Draft principles:
- Use the user's own language and examples from the conversation — don't invent new ones
- Don't fabricate stories the user never told
- Questions left open in the conversation should remain open in the draft
- This is a draft in brainstorming/, not a finished piece — the user decides when to move it to artifacts/

## Braindump Principles

- **Ask first, act second**: Never assume which format the user wants
- **Outline requires approval**: Do not write the article draft without the user's explicit go-ahead
- **Stay in brainstorming/**: Never move files to artifacts/ — that's the user's decision
- **Be honest about thin material**: If the conversation is too short or scattered, say so rather than padding the output
