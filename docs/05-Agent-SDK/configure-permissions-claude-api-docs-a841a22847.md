---
category: "05-Agent-SDK"
fetched_at: "2026-02-06T07:09:28Z"
source_url: "https://platform.claude.com/docs/en/agent-sdk/permissions"
title: "Configure permissions - Claude API Docs"
---

Guides

# Configure permissions

Copy page

Control how your agent uses tools with permission modes, hooks, and declarative allow/deny rules.

Copy page

The Claude Agent SDK provides permission controls to manage how Claude uses tools. Use permission modes and rules to define what's allowed automatically, and the [`canUseTool` callback](/docs/en/agent-sdk/user-input) to handle everything else at runtime.

This page covers permission modes and rules. To build interactive approval flows where users approve or deny tool requests at runtime, see [Handle approvals and user input](/docs/en/agent-sdk/user-input).

## 

How permissions are evaluated

When Claude requests a tool, the SDK checks permissions in this order:

1.  1

    Hooks

    Run [hooks](/docs/en/agent-sdk/hooks) first, which can allow, deny, or continue to the next step

2.  2

    Permission rules

    Check rules defined in [settings.json](https://code.claude.com/docs/en/settings#permission-settings) in this order: `deny` rules first (block regardless of other rules), then `allow` rules (permit if matched), then `ask` rules (prompt for approval). These declarative rules let you pre-approve, block, or require approval for specific tools without writing code.

3.  3

    Permission mode

    Apply the active [permission mode](#permission-modes) (`bypassPermissions`, `acceptEdits`, `dontAsk`, etc.)

4.  4

    canUseTool callback

    If not resolved by rules or modes, call your [`canUseTool` callback](/docs/en/agent-sdk/user-input) for a decision

This page focuses on **permission modes** (step 3), the static configuration that controls default behavior. For the other steps:

- **Hooks**: run custom code to allow, deny, or modify tool requests. See [Control execution with hooks](/docs/en/agent-sdk/hooks).
- **Permission rules**: configure declarative allow/deny rules in `settings.json`. See [Permission settings](https://code.claude.com/docs/en/settings#permission-settings).
- **canUseTool callback**: prompt users for approval at runtime. See [Handle approvals and user input](/docs/en/agent-sdk/user-input).

## 

Permission modes

Permission modes provide global control over how Claude uses tools. You can set the permission mode when calling `query()` or change it dynamically during streaming sessions.

### 

Available modes

The SDK supports these permission modes:

| Mode | Description | Tool behavior |
|----|----|----|
| `default` | Standard permission behavior | No auto-approvals; unmatched tools trigger your `canUseTool` callback |
| `acceptEdits` | Auto-accept file edits | File edits and [filesystem operations](#accept-edits-mode-acceptedits) (`mkdir`, `rm`, `mv`, etc.) are automatically approved |
| `bypassPermissions` | Bypass all permission checks | All tools run without permission prompts (use with caution) |
| `plan` | Planning mode | No tool execution; Claude plans without making changes |

**Subagent inheritance**: When using `bypassPermissions`, all subagents inherit this mode and it cannot be overridden. Subagents may have different system prompts and less constrained behavior than your main agent. Enabling `bypassPermissions` grants them full, autonomous system access without any approval prompts.

### 

Set permission mode

You can set the permission mode once when starting a query, or change it dynamically while the session is active.

At query time

At query time

During streaming

During streaming

Pass `permission_mode` (Python) or `permissionMode` (TypeScript) when creating a query. This mode applies for the entire session unless changed dynamically.

Python

``` shiki
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    async for message in query(
        prompt="Help me refactor this code",
        options=ClaudeAgentOptions(
            permission_mode="default",  # Set the mode here
        ),
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())
```

### 

Mode details

#### 

Accept edits mode (`acceptEdits`)

Auto-approves file operations so Claude can edit code without prompting. Other tools (like Bash commands that aren't filesystem operations) still require normal permissions.

**Auto-approved operations:**

- File edits (Edit, Write tools)
- Filesystem commands: `mkdir`, `touch`, `rm`, `mv`, `cp`

**Use when:** you trust Claude's edits and want faster iteration, such as during prototyping or when working in an isolated directory.

#### 

Bypass permissions mode (`bypassPermissions`)

Auto-approves all tool uses without prompts. Hooks still execute and can block operations if needed.

Use with extreme caution. Claude has full system access in this mode. Only use in controlled environments where you trust all possible operations.

#### 

Plan mode (`plan`)

Prevents tool execution entirely. Claude can analyze code and create plans but cannot make changes. Claude may use `AskUserQuestion` to clarify requirements before finalizing the plan. See [Handle approvals and user input](/docs/en/agent-sdk/user-input#handle-clarifying-questions) for handling these prompts.

**Use when:** you want Claude to propose changes without executing them, such as during code review or when you need to approve changes before they're made.

## 

Related resources

For the other steps in the permission evaluation flow:

- [Handle approvals and user input](/docs/en/agent-sdk/user-input): interactive approval prompts and clarifying questions
- [Hooks guide](/docs/en/agent-sdk/hooks): run custom code at key points in the agent lifecycle
- [Permission rules](https://code.claude.com/docs/en/settings#permission-settings): declarative allow/deny rules in `settings.json`

Was this page helpful?

- 

- [How permissions are evaluated](#how-permissions-are-evaluated)

- [Permission modes](#permission-modes)

- [Available modes](#available-modes)

- [Set permission mode](#set-permission-mode)

- [Mode details](#mode-details)

- [Related resources](#related-resources)

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
