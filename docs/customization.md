# Customization Guide

## Language

The system defaults to English for structure (folder names, section headers) but you can change the output language.

### Step 1: Set your language in CLAUDE.md

```yaml
- **Language**: 繁體中文
```

### Step 2: Customize section headers

In `CLAUDE.md`, change the section headers in the compilation specs. For example, for Traditional Chinese:

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

The `/compile` and `/health-check` commands follow whatever section headers you define in CLAUDE.md.

## Domain

### Adding artifact subfolders

The template ships with just `artifacts/projects/`. Add subfolders that match your domain:

**For a teacher:**
```
artifacts/
├── lessons/
├── essays/
├── presentations/
└── projects/
```

**For a researcher:**
```
artifacts/
├── papers/
├── talks/
├── grant-proposals/
└── projects/
```

**For a developer:**
```
artifacts/
├── blog-posts/
├── documentation/
├── talks/
└── projects/
```

### Adding raw/ subfolders

You can add more subfolders to raw/ for your specific input sources. Just update the origin mapping in the `/compile` command to tell the LLM whether new subfolders are `origin: external` or `origin: self`.

## Tags

Tags should match your vault's language. Use proper nouns in their original form (e.g., "Claude Code", "Obsidian") and translate general concepts to your chosen language.

## Writing Style

If you have a specific writing style for your domain, add a `## Writing Style` section to CLAUDE.md. This will influence how the LLM writes summaries and concept entries.

## Additional Commands

The three included commands (/compile, /health-check, /thinking-partner) cover the core workflow. You can add more commands to `.claude/commands/` for your specific needs. See the [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/tutorials#create-slash-commands) for how to create custom commands.
