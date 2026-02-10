---
category: "05-Agent-SDK"
fetched_at: "2026-02-07T10:04:36Z"
source_url: "https://platform.claude.com/docs/en/agent-sdk/migration-guide"
title: "Migrate to Claude Agent SDK - Claude API Docs"
---

Agent SDK

# Migrate to Claude Agent SDK

Copy page

Guide for migrating the Claude Code TypeScript and Python SDKs to the Claude Agent SDK

Copy page

## 

Overview

The Claude Code SDK has been renamed to the **Claude Agent SDK** and its documentation has been reorganized. This change reflects the SDK's broader capabilities for building AI agents beyond just coding tasks.

## 

What's Changed

| Aspect | Old | New |
|----|----|----|
| **Package Name (TS/JS)** | `@anthropic-ai/claude-code` | `@anthropic-ai/claude-agent-sdk` |
| **Python Package** | `claude-code-sdk` | `claude-agent-sdk` |
| **Documentation Location** | Claude Code docs | API Guide → Agent SDK section |

**Documentation Changes:** The Agent SDK documentation has moved from the Claude Code docs to the API Guide under a dedicated [Agent SDK](/docs/en/agent-sdk/overview) section. The Claude Code docs now focus on the CLI tool and automation features.

## 

Migration Steps

### 

For TypeScript/JavaScript Projects

**1. Uninstall the old package:**

``` shiki
npm uninstall @anthropic-ai/claude-code
```

**2. Install the new package:**

``` shiki
npm install @anthropic-ai/claude-agent-sdk
```

**3. Update your imports:**

Change all imports from `@anthropic-ai/claude-code` to `@anthropic-ai/claude-agent-sdk`:

``` shiki
// Before
import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-code";

// After
import {
  query,
  tool,
  createSdkMcpServer,
} from "@anthropic-ai/claude-agent-sdk";
```

**4. Update package.json dependencies:**

If you have the package listed in your `package.json`, update it:

``` shiki
// Before
{
  "dependencies": {
    "@anthropic-ai/claude-code": "^1.0.0"
  }
}

// After
{
  "dependencies": {
    "@anthropic-ai/claude-agent-sdk": "^0.1.0"
  }
}
```

That's it! No other code changes are required.

### 

For Python Projects

**1. Uninstall the old package:**

``` shiki
pip uninstall claude-code-sdk
```

**2. Install the new package:**

``` shiki
pip install claude-agent-sdk
```

**3. Update your imports:**

Change all imports from `claude_code_sdk` to `claude_agent_sdk`:

``` shiki
# Before
from claude_code_sdk import query, ClaudeCodeOptions

# After
from claude_agent_sdk import query, ClaudeAgentOptions
```

**4. Update type names:**

Change `ClaudeCodeOptions` to `ClaudeAgentOptions`:

``` shiki
# Before
from claude_agent_sdk import query, ClaudeCodeOptions

options = ClaudeCodeOptions(
    model="claude-opus-4-6"
)

# After
from claude_agent_sdk import query, ClaudeAgentOptions

options = ClaudeAgentOptions(
    model="claude-opus-4-6"
)
```

**5. Review [breaking changes](#breaking-changes)**

Make any code changes needed to complete the migration.

## 

Breaking changes

To improve isolation and explicit configuration, Claude Agent SDK v0.1.0 introduces breaking changes for users migrating from Claude Code SDK. Review this section carefully before migrating.

### 

Python: ClaudeCodeOptions renamed to ClaudeAgentOptions

**What changed:** The Python SDK type `ClaudeCodeOptions` has been renamed to `ClaudeAgentOptions`.

**Migration:**

``` shiki
# BEFORE (v0.0.x)
from claude_agent_sdk import query, ClaudeCodeOptions

options = ClaudeCodeOptions(
    model="claude-opus-4-6",
    permission_mode="acceptEdits"
)

# AFTER (v0.1.0)
from claude_agent_sdk import query, ClaudeAgentOptions

options = ClaudeAgentOptions(
    model="claude-opus-4-6",
    permission_mode="acceptEdits"
)
```

**Why this changed:** The type name now matches the "Claude Agent SDK" branding and provides consistency across the SDK's naming conventions.

### 

System prompt no longer default

**What changed:** The SDK no longer uses Claude Code's system prompt by default.

**Migration:**

TypeScript

``` shiki
// BEFORE (v0.0.x) - Used Claude Code's system prompt by default
const result = query({ prompt: "Hello" });

// AFTER (v0.1.0) - Uses minimal system prompt by default
// To get the old behavior, explicitly request Claude Code's preset:
const result = query({
  prompt: "Hello",
  options: {
    systemPrompt: { type: "preset", preset: "claude_code" }
  }
});

// Or use a custom system prompt:
const result = query({
  prompt: "Hello",
  options: {
    systemPrompt: "You are a helpful coding assistant"
  }
});
```

**Why this changed:** Provides better control and isolation for SDK applications. You can now build agents with custom behavior without inheriting Claude Code's CLI-focused instructions.

### 

Settings Sources No Longer Loaded by Default

**What changed:** The SDK no longer reads from filesystem settings (CLAUDE.md, settings.json, slash commands, etc.) by default.

**Migration:**

TypeScript

``` shiki
// BEFORE (v0.0.x) - Loaded all settings automatically
const result = query({ prompt: "Hello" });
// Would read from:
// - ~/.claude/settings.json (user)
// - .claude/settings.json (project)
// - .claude/settings.local.json (local)
// - CLAUDE.md files
// - Custom slash commands

// AFTER (v0.1.0) - No settings loaded by default
// To get the old behavior:
const result = query({
  prompt: "Hello",
  options: {
    settingSources: ["user", "project", "local"]
  }
});

// Or load only specific sources:
const result = query({
  prompt: "Hello",
  options: {
    settingSources: ["project"]  // Only project settings
  }
});
```

**Why this changed:** Ensures SDK applications have predictable behavior independent of local filesystem configurations. This is especially important for:

- **CI/CD environments** - Consistent behavior without local customizations
- **Deployed applications** - No dependency on filesystem settings
- **Testing** - Isolated test environments
- **Multi-tenant systems** - Prevent settings leakage between users

**Backward compatibility:** If your application relied on filesystem settings (custom slash commands, CLAUDE.md instructions, etc.), add `settingSources: ['user', 'project', 'local']` to your options.

## 

Why the Rename?

The Claude Code SDK was originally designed for coding tasks, but it has evolved into a powerful framework for building all types of AI agents. The new name "Claude Agent SDK" better reflects its capabilities:

- Building business agents (legal assistants, finance advisors, customer support)
- Creating specialized coding agents (SRE bots, security reviewers, code review agents)
- Developing custom agents for any domain with tool use, MCP integration, and more

## 

Getting Help

If you encounter any issues during migration:

**For TypeScript/JavaScript:**

1.  Check that all imports are updated to use `@anthropic-ai/claude-agent-sdk`
2.  Verify your package.json has the new package name
3.  Run `npm install` to ensure dependencies are updated

**For Python:**

1.  Check that all imports are updated to use `claude_agent_sdk`
2.  Verify your requirements.txt or pyproject.toml has the new package name
3.  Run `pip install claude-agent-sdk` to ensure the package is installed

## 

Next Steps

- Explore the [Agent SDK Overview](/docs/en/agent-sdk/overview) to learn about available features
- Check out the [TypeScript SDK Reference](/docs/en/agent-sdk/typescript) for detailed API documentation
- Review the [Python SDK Reference](/docs/en/agent-sdk/python) for Python-specific documentation
- Learn about [Custom Tools](/docs/en/agent-sdk/custom-tools) and [MCP Integration](/docs/en/agent-sdk/mcp)

Was this page helpful?

- 

- [Overview](#overview)

- [What's Changed](#whats-changed)

- [Migration Steps](#migration-steps)

- [For TypeScript/JavaScript Projects](#for-type-script-java-script-projects)

- [For Python Projects](#for-python-projects)

- [Breaking changes](#breaking-changes)

- [Python: ClaudeCodeOptions renamed to ClaudeAgentOptions](#python-claude-code-options-renamed-to-claude-agent-options)

- [System prompt no longer default](#system-prompt-no-longer-default)

- [Settings Sources No Longer Loaded by Default](#settings-sources-no-longer-loaded-by-default)

- [Why the Rename?](#why-the-rename)

- [Getting Help](#getting-help)

- [Next Steps](#next-steps)

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
