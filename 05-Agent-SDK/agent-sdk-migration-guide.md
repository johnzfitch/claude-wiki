---
title: "Migrate to Claude Agent SDK - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/agent-sdk/migration-guide"
category: "05-Agent-SDK"
fetched_at: "2026-09-05T06:27:26Z"
tags: ["agents", "claude-code", "sdk"]
---

## On this page

- [Overview](#overview)
- [What’s Changed](#what%E2%80%99s-changed)
- [Migration Steps](#migration-steps)
  - [For TypeScript/JavaScript Projects](#for-typescript%2Fjavascript-projects)
  - [For Python Projects](#for-python-projects)
- [Breaking changes](#breaking-changes)
  - [Python: ClaudeCodeOptions renamed to ClaudeAgentOptions](#python-claudecodeoptions-renamed-to-claudeagentoptions)
  - [System prompt no longer default](#system-prompt-no-longer-default)
  - [Settings sources default](#settings-sources-default)
- [Next Steps](#next-steps)

Agent SDK

# Migrate to Claude Agent SDK

Copy pageCopy page

Guide for migrating the Claude Code TypeScript and Python SDKs to the Claude Agent SDK

Copy pageCopy page


[​](#overview)

Overview

The Claude Code SDK has been renamed to the **Claude Agent SDK** and its documentation has been reorganized. This change reflects the SDK’s broader capabilities for building AI agents beyond just coding tasks. Migrating from the OpenAI Agents SDK instead? The [OpenAI Agents SDK migration recipe](https://platform.claude.com/cookbook/claude-agent-sdk-04-migrating-from-openai-agents-sdk) maps each primitive onto the Claude Agent SDK through a single worked example.


[​](#what’s-changed)

What’s Changed

| Aspect                     | Old                         | New                                                                           |
|:---------------------------|:----------------------------|:------------------------------------------------------------------------------|
| **Package Name (TS/JS)**   | `@anthropic-ai/claude-code` | `@anthropic-ai/claude-agent-sdk`                                              |
| **Python Package**         | `claude-code-sdk`           | `claude-agent-sdk`                                                            |
| **Documentation Location** | Claude Code docs            | Claude Code docs → dedicated [Agent SDK](agent-sdk-overview.md) section |


[​](#migration-steps)

Migration Steps


[​](#for-typescript/javascript-projects)

For TypeScript/JavaScript Projects

**1. Uninstall the old package:**

```python
npm uninstall @anthropic-ai/claude-code
```

**2. Install the new package:**

```python
npm install @anthropic-ai/claude-agent-sdk
```

**3. Update your imports:** Change all imports from `@anthropic-ai/claude-code` to `@anthropic-ai/claude-agent-sdk`:

```python
// Before
import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-code";

// After
import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-agent-sdk";
```

**4. Update package.json:** If `@anthropic-ai/claude-code` is still listed in your `package.json`, replace it with `@anthropic-ai/claude-agent-sdk` and update the version range as well, for example from `"^0.0.42"` to `"^0.3.0"`. **5. Review [breaking changes](#breaking-changes)** Make any code changes needed to complete the migration.


[​](#for-python-projects)

For Python Projects

**1. Uninstall the old package:**

```python
pip uninstall -y claude-code-sdk
```

If the old package isn’t installed, pip prints `WARNING: Skipping claude-code-sdk as it is not installed.` That’s expected and you can continue to the next step. **2. Install the new package:**

```python
pip install claude-agent-sdk
```

If `claude-code-sdk` is listed in your `requirements.txt` or `pyproject.toml`, replace it with `claude-agent-sdk`. **3. Update your imports:** Change all imports from `claude_code_sdk` to `claude_agent_sdk`:

```python
# Before
from claude_code_sdk import query, ClaudeCodeOptions

# After
from claude_agent_sdk import query, ClaudeAgentOptions
```

**4. Review [breaking changes](#breaking-changes)** Make any code changes needed to complete the migration.


[​](#breaking-changes)

Breaking changes

To improve isolation and explicit configuration, Claude Agent SDK v0.1.0 introduces breaking changes for users migrating from Claude Code SDK.


[​](#python-claudecodeoptions-renamed-to-claudeagentoptions)

Python: ClaudeCodeOptions renamed to ClaudeAgentOptions

**What changed:** The Python SDK type `ClaudeCodeOptions` has been renamed to `ClaudeAgentOptions`. **Migration:**

```python
# BEFORE (claude-code-sdk)
from claude_code_sdk import query, ClaudeCodeOptions

options = ClaudeCodeOptions(model="claude-opus-4-7", permission_mode="acceptEdits")

# AFTER (claude-agent-sdk)
from claude_agent_sdk import query, ClaudeAgentOptions

options = ClaudeAgentOptions(model="claude-opus-4-7", permission_mode="acceptEdits")
```


[​](#system-prompt-no-longer-default)

System prompt no longer default

**What changed:** The SDK no longer uses Claude Code’s system prompt by default. **Migration:**

TypeScript

Python

```python
import { query } from "@anthropic-ai/claude-agent-sdk";

// BEFORE (v0.0.x) - Used Claude Code's system prompt by default
const before = query({ prompt: "Hello" });

// AFTER (v0.1.0) - Uses minimal system prompt by default
// To get the old behavior, explicitly request Claude Code's preset:
const presetResult = query({
  prompt: "Hello",
  options: {
    systemPrompt: { type: "preset", preset: "claude_code" }
  }
});

// Or use a custom system prompt:
const customResult = query({
  prompt: "Hello",
  options: {
    systemPrompt: "You are a helpful coding assistant"
  }
});
```

```python
from claude_agent_sdk import query, ClaudeAgentOptions
import asyncio


async def main():
    # BEFORE (v0.0.x) - Used Claude Code's system prompt by default
    async for message in query(prompt="Hello"):
        print(message)

    # AFTER (v0.1.0) - Uses minimal system prompt by default
    # To get the old behavior, explicitly request Claude Code's preset:
    async for message in query(
        prompt="Hello",
        options=ClaudeAgentOptions(
            system_prompt={"type": "preset", "preset": "claude_code"}  # Use the preset
        ),
    ):
        print(message)

    # Or use a custom system prompt:
    async for message in query(
        prompt="Hello",
        options=ClaudeAgentOptions(system_prompt="You are a helpful coding assistant"),
    ):
        print(message)


asyncio.run(main())
```


[​](#settings-sources-default)

Settings sources default

This default was briefly changed in v0.1.0 to load no filesystem settings and then reverted, so no migration action is needed. **Current behavior:** Omitting `settingSources` on `query()` loads user, project, and local filesystem settings, matching the CLI. This includes `~/.claude/settings.json`, `.claude/settings.json`, `.claude/settings.local.json`, CLAUDE.md files, and custom commands. To run isolated from filesystem settings, pass `settingSources: []`, or `setting_sources=[]` in Python. See [Control filesystem settings with settingSources](agent-sdk-claude-code-features.md#control-filesystem-settings-with-settingsources) for what each source loads. Isolation is especially important for CI/CD pipelines, deployed applications, test environments, and multi-tenant systems where local customizations should not leak in.

Python SDK 0.1.59 and earlier treated an empty list the same as omitting the option, so upgrade before relying on `setting_sources=[]`. See [What settingSources does not control](agent-sdk-claude-code-features.md#what-settingsources-does-not-control) for inputs that are read even when `settingSources` is `[]`.


[​](#next-steps)

Next Steps

- Explore the [Agent SDK Overview](agent-sdk-overview.md) to learn about available features
- Check out the [TypeScript SDK Reference](agent-sdk-typescript.md) for detailed API documentation
- Review the [Python SDK Reference](agent-sdk-python.md) for Python-specific documentation
- Learn about [Custom Tools](agent-sdk-custom-tools.md) and [MCP Integration](agent-sdk-mcp.md)
