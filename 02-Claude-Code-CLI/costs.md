---
title: "Manage costs effectively"
source_url: "https://code.claude.com/docs/en/costs.md"
category: "02-Claude-Code-CLI"
fetched_at: "2026-04-08"
tags: ["claude-code"]
---

# Manage costs effectively

Track token usage, set team spend limits, and reduce Claude Code costs with context management, model selection, extended thinking settings, and preprocessing hooks.

Claude Code consumes tokens for each interaction. The average cost is $6 per developer per day, with daily costs remaining below $12 for 90% of users. On average, Claude Code costs ~$100-200/developer per month with Sonnet 4.6.

## Track your costs

### Using the `/cost` command

> The `/cost` command shows API token usage and is intended for API users. Claude Max and Pro subscribers have usage included in their subscription, so `/cost` data isn't relevant for billing purposes. Subscribers can use `/stats` to view usage patterns.

```
Total cost:            $0.55
Total duration (API):  6m 19.7s
Total duration (wall): 6h 33m 10.2s
Total code changes:    0 lines added, 0 lines removed
```

## Managing costs for teams

Set workspace spend limits on the total Claude Code workspace spend. Admins can view cost and usage reporting in the Console.

### Rate limit recommendations

| Team size     | TPM per user | RPM per user |
| ------------- | ------------ | ------------ |
| 1-5 users     | 200k-300k    | 5-7          |
| 5-20 users    | 100k-150k    | 2.5-3.5      |
| 20-50 users   | 50k-75k      | 1.25-1.75    |
| 50-100 users  | 25k-35k      | 0.62-0.87    |
| 100-500 users | 15k-20k      | 0.37-0.47    |
| 500+ users    | 10k-15k      | 0.25-0.35    |

### Agent team token costs

Agent teams spawn multiple Claude Code instances. Token usage scales with the number of active teammates.

- Use Sonnet for teammates
- Keep teams small (3-5)
- Keep spawn prompts focused
- Clean up teams when done

## Reduce token usage

### Manage context proactively

- Use `/clear` between tasks
- Use `/compact Focus on code samples and API usage` for custom compaction
- Customize compaction in CLAUDE.md

### Choose the right model

Sonnet handles most coding tasks well and costs less than Opus. Reserve Opus for complex architectural decisions. Use `/model` to switch mid-session.

### Reduce MCP server overhead

MCP tool definitions are deferred by default. Run `/context` to see what's consuming space. Prefer CLI tools (`gh`, `aws`) when available. Disable unused servers via `/mcp`.

### Install code intelligence plugins

Code intelligence plugins give Claude precise symbol navigation, reducing unnecessary file reads.

### Move instructions from CLAUDE.md to skills

Skills load on-demand only when invoked. Keep CLAUDE.md under 200 lines.

### Adjust extended thinking

Extended thinking is enabled by default. For simpler tasks, reduce with `/effort`, disable in `/config`, or lower the budget with `MAX_THINKING_TOKENS=8000`.

### Delegate verbose operations to subagents

Running tests, fetching docs, or processing logs can consume context. Delegate to subagents so verbose output stays in the subagent's context.

### Write specific prompts

Vague requests trigger broad scanning. Specific requests let Claude work efficiently with minimal file reads.

### Work efficiently on complex tasks

- Use plan mode (Shift+Tab) for complex tasks
- Course-correct early with Escape
- Give verification targets (test cases, screenshots)
- Test incrementally

## Background token usage

Claude Code uses tokens for background functionality even when idle:

- Conversation summarization for `claude --resume`
- Command processing for status checks

Typically under $0.04 per session.

## See Also

- [Agent teams](../09-Agents-Patterns/agent-teams.md)
- [Subagents](../09-Agents-Patterns/create-custom-subagents-claude-code-docs-7dc93e85c0.md)
- [Model configuration](model-config-ca429e15da.md)
