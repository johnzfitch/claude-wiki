---
category: "02-Claude-Code-CLI"
fetched_at: "2026-03-14T10:17:06Z"
source_url: "https://code.claude.com/docs/en/output-styles"
title: "Output styles - Claude Code Docs"
---

# Output styles


Adapt Claude Code for uses beyond software engineering


Output styles allow you to use Claude Code as any type of agent while keeping its core capabilities, such as running local scripts, reading/writing files, and tracking TODOs.

## 

[​](#built-in-output-styles)

Built-in output styles

Claude Code’s **Default** output style is the existing system prompt, designed to help you complete software engineering tasks efficiently. There are two additional built-in output styles focused on teaching you the codebase and how Claude operates:

- **Explanatory**: Provides educational “Insights” in between helping you complete software engineering tasks. Helps you understand implementation choices and codebase patterns.
- **Learning**: Collaborative, learn-by-doing mode where Claude will not only share “Insights” while coding, but also ask you to contribute small, strategic pieces of code yourself. Claude Code will add `TODO(human)` markers in your code for you to implement.

## 

[​](#how-output-styles-work)

How output styles work

Output styles directly modify Claude Code’s system prompt.

- All output styles exclude instructions for efficient output (such as responding concisely).
- Custom output styles exclude instructions for coding (such as verifying code with tests), unless `keep-coding-instructions` is true.
- All output styles have their own custom instructions added to the end of the system prompt.
- All output styles trigger reminders for Claude to adhere to the output style instructions during the conversation.

## 

[​](#change-your-output-style)

Change your output style

Run `/config` and select **Output style** to pick a style from a menu. Your selection is saved to `.claude/settings.local.json` at the [local project level](/docs/en/settings). To set a style without the menu, edit the `outputStyle` field directly in a settings file:

Report incorrect code

Copy


``` shiki
{
  "outputStyle": "Explanatory"
}
```

Because the output style is set in the system prompt at session start, changes take effect the next time you start a new session. This keeps the system prompt stable throughout a conversation so prompt caching can reduce latency and cost.

## 

[​](#create-a-custom-output-style)

Create a custom output style

Custom output styles are Markdown files with frontmatter and the text that will be added to the system prompt:

Report incorrect code

Copy


``` shiki
---
name: My Custom Style
description:
  A brief description of what this style does, to be displayed to the user
---

# Custom Style Instructions

You are an interactive CLI tool that helps users with software engineering
tasks. [Your custom instructions here...]

## Specific Behaviors

[Define how the assistant should behave in this style...]
```

You can save these files at the user level (`~/.claude/output-styles`) or project level (`.claude/output-styles`).

### 

[​](#frontmatter)

Frontmatter

Output style files support frontmatter for specifying metadata:

| Frontmatter | Purpose | Default |
|:---|:---|:---|
| `name` | Name of the output style, if not the file name | Inherits from file name |
| `description` | Description of the output style, shown in the `/config` picker | None |
| `keep-coding-instructions` | Whether to keep the parts of Claude Code’s system prompt related to coding. | false |

## 

[​](#comparisons-to-related-features)

Comparisons to related features

### 

[​](#output-styles-vs-claude-md-vs-—append-system-prompt)

Output Styles vs. CLAUDE.md vs. —append-system-prompt

Output styles completely “turn off” the parts of Claude Code’s default system prompt specific to software engineering. Neither CLAUDE.md nor `--append-system-prompt` edit Claude Code’s default system prompt. CLAUDE.md adds the contents as a user message *following* Claude Code’s default system prompt. `--append-system-prompt` appends the content to the system prompt.

### 

[​](#output-styles-vs-agents)

Output Styles vs. [Agents](/docs/en/sub-agents)

Output styles directly affect the main agent loop and only affect the system prompt. Agents are invoked to handle specific tasks and can include additional settings like the model to use, the tools they have available, and some context about when to use the agent.

### 

[​](#output-styles-vs-skills)

Output Styles vs. [Skills](/docs/en/skills)

Output styles modify how Claude responds (formatting, tone, structure) and are always active once selected. Skills are task-specific prompts that you invoke with `/skill-name` or that Claude loads automatically when relevant. Use output styles for consistent formatting preferences; use skills for reusable workflows and tasks.
