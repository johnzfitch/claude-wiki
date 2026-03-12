---
category: "05-Agent-SDK"
fetched_at: "2026-03-12T08:16:10Z"
source_url: "https://platform.claude.com/docs/en/agent-sdk/permissions"
title: "Configure permissions - Claude API Docs"
---

# Configure permissions


Control how your agent uses tools with permission modes, hooks, and declarative allow/deny rules.


The Claude Agent SDK provides permission controls to manage how Claude uses tools. Use permission modes and rules to define what's allowed automatically, and the [`canUseTool` callback](/docs/en/agent-sdk/user-input) to handle everything else at runtime.

This page covers permission modes and rules. To build interactive approval flows where users approve or deny tool requests at runtime, see [Handle approvals and user input](/docs/en/agent-sdk/user-input).

## 

How permissions are evaluated

When Claude requests a tool, the SDK checks permissions in this order:

1.  1

    Hooks

    Run [hooks](/docs/en/agent-sdk/hooks) first, which can allow, deny, or continue to the next step

2.  2

    Deny rules

    Check `deny` rules (from `disallowed_tools` and [settings.json](https://code.claude.com/docs/en/settings#permission-settings)). If a deny rule matches, the tool is blocked, even in `bypassPermissions` mode.

3.  3

    Permission mode

    Apply the active [permission mode](#permission-modes). `bypassPermissions` approves everything that reaches this step. `acceptEdits` approves file operations. Other modes fall through.

4.  4

    Allow rules

    Check `allow` rules (from `allowed_tools` and settings.json). If a rule matches, the tool is approved.

5.  5

    canUseTool callback

    If not resolved by any of the above, call your [`canUseTool` callback](/docs/en/agent-sdk/user-input) for a decision. In `dontAsk` mode, this step is skipped and the tool is denied.

This page focuses on **allow and deny rules** and **permission modes**. For the other steps:

- **Hooks:** run custom code to allow, deny, or modify tool requests. See [Control execution with hooks](/docs/en/agent-sdk/hooks).
- **canUseTool callback:** prompt users for approval at runtime. See [Handle approvals and user input](/docs/en/agent-sdk/user-input).

## 

Allow and deny rules

`allowed_tools` and `disallowed_tools` (TypeScript: `allowedTools` / `disallowedTools`) add entries to the allow and deny rule lists in the evaluation flow above. They control whether a tool call is approved, not whether the tool is available to Claude.

| Option | Effect |
|----|----|
| `allowed_tools=["Read", "Grep"]` | `Read` and `Grep` are auto-approved. Tools not listed here still exist and fall through to the permission mode and `canUseTool`. |
| `disallowed_tools=["Bash"]` | `Bash` is always denied. Deny rules are checked first and hold in every permission mode, including `bypassPermissions`. |

For a locked-down agent, pair `allowedTools` with `permissionMode: "dontAsk"` (TypeScript only). Listed tools are approved; anything else is denied outright instead of prompting:

``` shiki
const options = {
  allowedTools: ["Read", "Glob", "Grep"],
  permissionMode: "dontAsk"
};
```

In Python, `dontAsk` is not yet available as a permission mode. Without it, Claude may still attempt to call tools not in `allowed_tools`. The call is rejected at runtime, but Claude wastes a turn discovering this. For tighter control in Python, use `disallowed_tools` to explicitly block tools you don't want Claude to attempt.

**`allowed_tools` does not constrain `bypassPermissions`.** `allowed_tools` only pre-approves the tools you list. Unlisted tools are not matched by any allow rule and fall through to the permission mode, where `bypassPermissions` approves them. Setting `allowed_tools=["Read"]` alongside `permission_mode="bypassPermissions"` still approves every tool, including `Bash`, `Write`, and `Edit`. If you need `bypassPermissions` but want specific tools blocked, use `disallowed_tools`.

You can also configure allow, deny, and ask rules declaratively in `.claude/settings.json`. The SDK does not load filesystem settings by default, so you must set `setting_sources=["project"]` (TypeScript: `settingSources: ["project"]`) in your options for these rules to apply. See [Permission settings](https://code.claude.com/docs/en/settings#permission-settings) for the rule syntax.

## 

Permission modes

Permission modes provide global control over how Claude uses tools. You can set the permission mode when calling `query()` or change it dynamically during streaming sessions.

### 

Available modes

The SDK supports these permission modes:

| Mode | Description | Tool behavior |
|----|----|----|
| `default` | Standard permission behavior | No auto-approvals; unmatched tools trigger your `canUseTool` callback |
| `dontAsk` (TypeScript only) | Deny instead of prompting | Anything not pre-approved by `allowed_tools` or rules is denied; `canUseTool` is never called |
| `acceptEdits` | Auto-accept file edits | File edits and [filesystem operations](#accept-edits-mode-acceptedits) (`mkdir`, `rm`, `mv`, etc.) are automatically approved |
| `bypassPermissions` | Bypass all permission checks | All tools run without permission prompts (use with caution) |
| `plan` | Planning mode | No tool execution; Claude plans without making changes |

**Subagent inheritance:** When using `bypassPermissions`, all subagents inherit this mode and it cannot be overridden. Subagents may have different system prompts and less constrained behavior than your main agent. Enabling `bypassPermissions` grants them full, autonomous system access without any approval prompts.

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

Don't ask mode (`dontAsk`, TypeScript only)

Converts any permission prompt into a denial. Tools pre-approved by `allowed_tools`, `settings.json` allow rules, or a hook run as normal. Everything else is denied without calling `canUseTool`.

**Use when:** you want a fixed, explicit tool surface for a headless agent and prefer a hard deny over silent reliance on `canUseTool` being absent.

`dontAsk` is available in the TypeScript SDK only. In Python, there is no exact equivalent. Use `disallowed_tools` to explicitly block tools you don't want Claude to use.

#### 

Bypass permissions mode (`bypassPermissions`)

Auto-approves all tool uses without prompts. Hooks still execute and can block operations if needed.

Use with extreme caution. Claude has full system access in this mode. Only use in controlled environments where you trust all possible operations.

`allowed_tools` does not constrain this mode. Every tool is approved, not just the ones you listed. Deny rules (`disallowed_tools`), explicit `ask` rules, and hooks are evaluated before the mode check and can still block a tool.

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
