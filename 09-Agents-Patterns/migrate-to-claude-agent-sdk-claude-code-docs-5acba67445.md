---
title: "Migrate to Claude Agent SDK - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/agent-sdk/migration-guide"
category: "09-Agents-Patterns"
fetched_at: "2026-08-02T05:38:04Z"
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
- [Why the Rename?](#why-the-rename)
- [Getting Help](#getting-help)
- [Next Steps](#next-steps)

SDK references

# Migrate to Claude Agent SDK

Copy pageCopy page

Guide for migrating the Claude Code TypeScript and Python SDKs to the Claude Agent SDK

Copy pageCopy page


[​](#overview)

Overview

The Claude Code SDK has been renamed to the **Claude Agent SDK** and its documentation has been reorganized. This change reflects the SDK’s broader capabilities for building AI agents beyond just coding tasks.


[​](#what’s-changed)

What’s Changed

| Aspect                     | Old                         | New                              |
|:---------------------------|:----------------------------|:---------------------------------|
| **Package Name (TS/JS)**   | `@anthropic-ai/claude-code` | `@anthropic-ai/claude-agent-sdk` |
| **Python Package**         | `claude-code-sdk`           | `claude-agent-sdk`               |
| **Documentation Location** | Claude Code docs            | API Guide → Agent SDK section    |

**Documentation Changes:** The Agent SDK documentation has moved from the Claude Code docs to the API Guide under a dedicated [Agent SDK](/docs/en/agent-sdk/overview) section. The Claude Code docs now focus on the CLI tool and automation features.


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

**4. Update package.json dependencies:** If you have the package listed in your `package.json`, update it: Before:

```python
{
  "dependencies": {
    "@anthropic-ai/claude-code": "^0.0.42"
  }
}
```

After:

```python
{
  "dependencies": {
    "@anthropic-ai/claude-agent-sdk": "^0.3.0"
  }
}
```

**5. Review [breaking changes](#breaking-changes)** Make any code changes needed to complete the migration.


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

**3. Update your imports:** Change all imports from `claude_code_sdk` to `claude_agent_sdk`:

```python
# Before
from claude_code_sdk import query, ClaudeCodeOptions

# After
from claude_agent_sdk import query, ClaudeAgentOptions
```

**4. Update type names:** Change `ClaudeCodeOptions` to `ClaudeAgentOptions`:

```python
# Before
from claude_code_sdk import query, ClaudeCodeOptions

options = ClaudeCodeOptions(model="claude-opus-4-7")

# After
from claude_agent_sdk import query, ClaudeAgentOptions

options = ClaudeAgentOptions(model="claude-opus-4-7")
```

**5. Review [breaking changes](#breaking-changes)** Make any code changes needed to complete the migration.


[​](#breaking-changes)

Breaking changes

To improve isolation and explicit configuration, Claude Agent SDK v0.1.0 introduces breaking changes for users migrating from Claude Code SDK. Review this section carefully before migrating.


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

**Why this changed:** The type name now matches the “Claude Agent SDK” branding and provides consistency across the SDK’s naming conventions.


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

**Why this changed:** Provides better control and isolation for SDK applications. You can now build agents with custom behavior without inheriting Claude Code’s CLI-focused instructions.


[​](#settings-sources-default)

Settings sources default

This default was briefly changed in v0.1.0 and then reverted, so no migration action is needed. **Current behavior:** Omitting `settingSources` on `query()` loads user, project, and local filesystem settings, matching the CLI. This includes `~/.claude/settings.json`, `.claude/settings.json`, `.claude/settings.local.json`, CLAUDE.md files, and custom commands. To run isolated from filesystem settings, pass an empty array:

TypeScript

Python

```python
import { query } from "@anthropic-ai/claude-agent-sdk";

const isolatedResult = query({
  prompt: "Hello",
  options: {
    settingSources: [] // No filesystem settings loaded
  }
});

// Or load only specific sources:
const projectOnlyResult = query({
  prompt: "Hello",
  options: {
    settingSources: ["project"] // Only project settings
  }
});
```

```python
from claude_agent_sdk import query, ClaudeAgentOptions
import asyncio


async def main():
    async for message in query(
        prompt="Hello",
        options=ClaudeAgentOptions(setting_sources=[]),  # No filesystem settings loaded
    ):
        print(message)

    # Or load only specific sources:
    async for message in query(
        prompt="Hello",
        options=ClaudeAgentOptions(
            setting_sources=["project"]  # Only project settings
        ),
    ):
        print(message)


asyncio.run(main())
```

Isolation is especially important for CI/CD pipelines, deployed applications, test environments, and multi-tenant systems where local customizations should not leak in.

SDK v0.1.0 briefly defaulted to no settings loaded; this was reverted in subsequent releases. Python SDK 0.1.59 and earlier treated an empty list the same as omitting the option, so upgrade before relying on `setting_sources=[]`. See [What settingSources does not control](/docs/en/agent-sdk/claude-code-features#what-settingsources-does-not-control) for inputs that are read even when `settingSources` is `[]`.


[​](#why-the-rename)

Why the Rename?

The Claude Code SDK was originally designed for coding tasks, but it has evolved into a powerful framework for building all types of AI agents. The new name “Claude Agent SDK” better reflects its capabilities:

- Building business agents (legal assistants, finance advisors, customer support)
- Creating specialized coding agents (SRE bots, security reviewers, code review agents)
- Developing custom agents for any domain with tool use, MCP integration, and more


[​](#getting-help)

Getting Help

If you encounter any issues during migration: **For TypeScript/JavaScript:**

1.  Check that all imports are updated to use `@anthropic-ai/claude-agent-sdk`
2.  Verify your package.json has the new package name
3.  Run `npm install` to ensure dependencies are updated

**For Python:**

1.  Check that all imports are updated to use `claude_agent_sdk`
2.  Verify your requirements.txt or pyproject.toml has the new package name
3.  Run `pip install claude-agent-sdk` to ensure the package is installed


[​](#next-steps)

Next Steps

- Explore the [Agent SDK Overview](/docs/en/agent-sdk/overview) to learn about available features
- Check out the [TypeScript SDK Reference](/docs/en/agent-sdk/typescript) for detailed API documentation
- Review the [Python SDK Reference](/docs/en/agent-sdk/python) for Python-specific documentation
- Learn about [Custom Tools](/docs/en/agent-sdk/custom-tools) and [MCP Integration](/docs/en/agent-sdk/mcp)
