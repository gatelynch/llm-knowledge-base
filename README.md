# LLM Knowledge Base

A personal knowledge management system powered by LLM compilation. Based on [Andrej Karpathy's LLM Knowledge Base workflow](https://x.com/karpathy/status/1908536205968998906) — separating raw materials from compiled knowledge, with an LLM as your librarian.

## The Problem

Most personal knowledge systems become graveyards. You clip articles, take notes, highlight books — then never look at them again. The gap between **collecting** and **understanding** is where knowledge dies.

This system closes that gap by using an LLM to **compile** your raw materials into structured, interconnected knowledge — summaries, concept entries, and indexes — while keeping your original sources untouched.

## Architecture

```
raw/                    ← Your library: unedited source material
  ├── articles/           clipped articles
  ├── books/              book notes & highlights
  ├── podcasts/           podcast transcripts
  ├── papers/             academic papers
  ├── notes/              your quick thoughts
  └── projects/           project-related material

wiki/                   ← Your encyclopedia: LLM-compiled knowledge
  ├── summaries/          one summary per source
  ├── concepts/           concept entries (cross-referenced)
  └── indexes/            All-Sources.md, All-Concepts.md

brainstorming/          ← Your lab notebook: exploration & quality
  ├── chat/               Q&A logs with reasoning
  └── health/             knowledge base health reports

artifacts/              ← Your publications: finished works
  └── projects/           your projects and outputs
```

**Key principle**: Raw materials are read-only. The LLM compiles them into wiki/, but never modifies your originals.

## Quick Start

1. Click **"Use this template"** on GitHub to create your own repo
2. Clone it to your machine
3. Open the folder in [Obsidian](https://obsidian.md)
4. Install [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)
5. Customize `CLAUDE.md` — fill in your name, domain, and language preference
6. Drop your first article into `raw/articles/`
7. Run `/compile` — watch your first summary and concept entries appear in `wiki/`

## Commands

This system includes 6 Claude Code slash commands:

| Command | What it does |
|---------|-------------|
| `/init-llm` | Interactive setup — asks about your profile, preferences, scans existing files, proposes an organization plan, and configures `CLAUDE.md` |
| `/compile` | Reads `raw/` and `artifacts/`, generates summaries in `wiki/summaries/`, extracts concepts to `wiki/concepts/`, updates indexes |
| `/health-check` | Scans `wiki/` for consistency issues, completeness gaps, and connectivity problems. Outputs a prioritized report to `brainstorming/health/` |
| `/thinking-partner` | Collaborative thinking — searches your vault for related notes, asks clarifying questions, helps you explore complex problems |
| `/write-partner` | Writing exploration — surfaces related vault content, counterexamples, and open questions to help you dig deeper before writing |
| `/braindump` | Distills a conversation into reusable material — Q&A logs, article drafts, or both — saved to `brainstorming/chat/` |

## How Compilation Works

```
1. You drop a file into raw/articles/
2. Run /compile
3. The LLM reads the file and determines origin (external vs self)
4. Generates a summary in wiki/summaries/ with:
   - Core Conclusion
   - Key Evidence
   - Open Questions
   - Key Terms
5. Extracts concepts mentioned 2+ times across summaries → wiki/concepts/
6. Updates wiki/indexes/ (All-Sources.md, All-Concepts.md)
```

Each concept entry separates **your practice** from **external perspectives**, with a dedicated section for **tensions & gaps** between the two. This is the core intellectual value — your experience and the research exist side by side, and contradictions are surfaced, not buried.

## Works Without an LLM

The folder structure and Obsidian templates work on their own. You can manually write summaries and concept entries following the formats in `CLAUDE.md`. The Claude Code commands simply automate what you'd otherwise do by hand.

## Customization

See [docs/customization.md](docs/customization.md) for how to:
- Change the language of compilation output
- Add domain-specific subfolders under `artifacts/`
- Customize section headers in summaries and concept entries
- Adapt the system for your field

## Credit

Architecture inspired by [Andrej Karpathy's LLM Knowledge Base concept](https://x.com/karpathy/status/1908536205968998906). Original implementation and compilation workflow by [@gatelynch](https://github.com/gatelynch).

## License

MIT
