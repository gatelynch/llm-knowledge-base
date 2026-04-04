---
name: init-llm
description: 'Set up your knowledge base: profile, preferences, and file organization'
argument-hint: ''
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion
---

# Initialize Knowledge Base

Walk a new user through setting up their knowledge base. Gather their profile and preferences, scan for existing files, propose an organization plan, and update CLAUDE.md. Detect the user's language from their answers and respond accordingly.

## Process

### 1. Interview — Who Are You?

Ask the user (in one message, then wait for their response):

> Let's set up your knowledge base. Tell me about yourself:
>
> 1. **Name** — What should I call you?
> 2. **Role** — What do you do? (e.g., teacher, researcher, designer, developer)
> 3. **Language** — What language do you prefer for output? (e.g., English, 繁體中文, 日本語)
> 4. **Domain** — What is this knowledge base centered on? (e.g., AI, education, design, software engineering)

### 2. Interview — How Do You Work?

After receiving answers to Step 1, ask (in one message, then wait):

> Now a few questions about how you like to work:
>
> 1. **Interaction style** — Do you prefer "ask before acting" or "be direct, move fast"?
> 2. **Exploration vs. output** — When you have a new topic, do you prefer deep discussion first (`/thinking-partner` style) or jump straight to generating compiled output (`/compile` style)?
> 3. **Writing style** — Do you have a specific voice or style for your writing? (optional — skip if unsure)
> 4. **Artifact subfolders** — Any subfolders you already know you'll need under `artifacts/`? (e.g., `essays/`, `blog-posts/`, `teaching/`, `talks/`)

### 3. Scan Existing Files

Scan the vault for `.md` files and folders outside the template structure:

- Use Glob to find files in the root directory and any non-template folders
- Template folders to ignore: `raw/`, `wiki/`, `brainstorming/`, `artifacts/`, `attachments/`, `templates/`, `docs/`, `.claude/`, `.git/`
- Identify files that could be moved into `raw/` or `artifacts/`
- Identify existing folders that could map to subfolders of `raw/` or `artifacts/`

If the vault is a fresh clone with no extra files, skip to Step 5.

### 4. Propose Migration Plan

Present the user with a clear plan:

- List each file/folder and where it would be moved (with brief reasoning)
- List new subfolders to be created under `artifacts/` based on their role and domain
- List anything that stays untouched (e.g., `README.md`, `CLAUDE.md`, `docs/`)

Format as a checklist so the user can approve, reject, or modify individual items.

**Do not proceed until the user explicitly approves.**

### 5. Execute

After approval:

1. **Create folders** — Create any new subfolders agreed upon (e.g., `artifacts/essays/`)
2. **Move files** — Move files as agreed using `mv` (never `cp`, to avoid duplicates)
3. **Update CLAUDE.md** — Replace all placeholder values:
   - `[YOUR_NAME]` → user's name
   - `[YOUR_ROLE]` → user's role (with any elaboration from context)
   - `[YOUR_LANGUAGE]` → user's preferred language (appears in both "About You" and "Vault Overview")
   - `[YOUR_DOMAIN]` → user's domain
   - Interaction style line
   - If the user provided a writing style, add a `## Writing Style` section after `## Naming Conventions`
   - Update `## Available Commands` to list all current commands
4. **Create index files** — If `wiki/indexes/All-Sources.md` and `wiki/indexes/All-Concepts.md` don't exist, create them with empty table headers

### 6. Summary & Next Steps

Tell the user what was done (files moved, CLAUDE.md updated, folders created).

Then suggest next steps:

> Your knowledge base is ready. Here's what you can do next:
>
> - Drop a file into `raw/articles/` and run `/compile` to see your first summary
> - Run `/thinking-partner` to start exploring a topic
> - Run `/health-check` any time to check the state of your wiki

## Init Principles

- **Never assume — always ask.** Every decision comes from the user's answers, not from defaults
- **Plan before acting.** Show the migration plan and wait for approval before moving any files
- **Use `mv`, not `cp`.** Avoid duplicates when reorganizing
- **Don't touch content.** This command organizes files and updates CLAUDE.md — it never edits the user's notes or articles
- **Detect language from conversation.** Since CLAUDE.md isn't configured yet, infer the response language from how the user answers
