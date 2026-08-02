---
title: "Configure permissions - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/agent-sdk/permissions"
category: "09-Agents-Patterns"
fetched_at: "2026-08-02T05:38:04Z"
tags: ["agents", "claude-code"]
---

## On this page

- [How permissions are evaluated](#how-permissions-are-evaluated)
- [Allow and deny rules](#allow-and-deny-rules)
- [Permission modes](#permission-modes)
  - [Available modes](#available-modes)
  - [Set permission mode](#set-permission-mode)
  - [Mode details](#mode-details)
  - [Accept edits mode (acceptEdits)](#accept-edits-mode-acceptedits)
  - [Don’t ask mode (dontAsk)](#don%E2%80%99t-ask-mode-dontask)
  - [Bypass permissions mode (bypassPermissions)](#bypass-permissions-mode-bypasspermissions)
  - [Plan mode (plan)](#plan-mode-plan)
- [Related resources](#related-resources)

Control and observability

# Configure permissions

Copy pageCopy page

Control how your agent uses tools with permission modes, hooks, and declarative allow/deny rules.

Copy pageCopy page

The Claude Agent SDK provides permission controls to manage how Claude uses tools. Use permission modes and rules to define what’s allowed automatically, and the [`canUseTool` callback](/docs/en/agent-sdk/user-input) to handle everything else at runtime.

This page covers permission modes and rules. To build interactive approval flows where users approve or deny tool requests at runtime, see [Handle approvals and user input](/docs/en/agent-sdk/user-input).


[​](#how-permissions-are-evaluated)

How permissions are evaluated

When Claude requests a tool, the SDK checks permissions in this order:

1

Hooks

Run [hooks](/docs/en/agent-sdk/hooks) first. A hook can deny the call outright or pass it on. A hook that returns `allow` does not skip the deny and ask rules below; those are evaluated regardless of the hook result.

2

Deny rules

Check `deny` rules (from `disallowed_tools` and [settings.json](/docs/en/settings#permission-settings)). If a deny rule matches, the tool is blocked, even in `bypassPermissions` mode. Bare-name deny rules like `Bash` remove the tool from Claude’s context before this evaluation begins, so only scoped rules like `Bash(rm *)` are checked at this step.

3

Ask rules

Check `ask` rules from [settings.json](/docs/en/settings#permission-settings). If an ask rule matches, the call falls through to your [`canUseTool` callback](/docs/en/agent-sdk/user-input) for confirmation, even in `bypassPermissions` mode.Tools that require user interaction behave the same way: `AskUserQuestion` and MCP tools whose server sets [`_meta["anthropic/requiresUserInteraction"]`](/docs/en/mcp#require-approval-for-a-specific-tool) always fall through to the callback, even when an allow rule matches. In `dontAsk` mode both cases are denied instead, because that mode never prompts. The MCP annotation requires Claude Code v2.1.199 or later.[claude.ai connector](/docs/en/mcp#organization-controls-on-connector-tools) tools your organization has set to `ask` also leave the flow at this step. Every call falls through to the callback, even in `bypassPermissions` mode and even when an allow rule matches. The callback receives the reason `Your organization requires approval for this tool`. In `dontAsk` mode the call is denied instead, because that mode never prompts.

4

Permission mode

Apply the active [permission mode](#permission-modes). `bypassPermissions` approves everything that reaches this step. `acceptEdits` approves file operations. `plan` routes file-edit and shell-write tools to your `canUseTool` callback regardless of allow rules, so write operations cannot be auto-approved while planning. Other modes fall through.

5

Allow rules

Check `allow` rules (from `allowed_tools` and settings.json). If a rule matches, the tool is approved.

6

canUseTool callback

If not resolved by any of the above, call your [`canUseTool` callback](/docs/en/agent-sdk/user-input) for a decision. In `dontAsk` mode, this step is skipped and the tool is denied.

As of v2.1.198, if you pass a `canUseTool` callback that this evaluation order can never reach, the TypeScript SDK emits a Node.js process warning once when the query is constructed. The warning’s code is `CLAUDE_SDK_CAN_USE_TOOL_SHADOWED`. Two configurations trigger it:

- `permissionMode: 'bypassPermissions'`, which auto-approves every call that reaches the permission mode step
- Each bare `allowedTools` entry such as `"Read"`, which auto-approves that whole tool before the callback is consulted

Entries with a specifier such as `Bash(ls *)` and the `acceptEdits` mode don’t trigger it, and allow rules coming from settings files aren’t visible to the check. Listen with `process.on('warning', ...)` and match the code to log or suppress it. To gate every tool call regardless of mode and rules, use a [`PreToolUse` hook](/docs/en/agent-sdk/hooks) instead. This page focuses on **allow and deny rules** and **permission modes**. For the other steps:

- **Hooks:** run custom code to allow, deny, or modify tool requests. See [Control execution with hooks](/docs/en/agent-sdk/hooks).
- **canUseTool callback:** prompt users for approval at runtime, when no earlier step resolves the call. See [Handle approvals and user input](/docs/en/agent-sdk/user-input).


[​](#allow-and-deny-rules)

Allow and deny rules

`allowed_tools` and `disallowed_tools` (TypeScript: `allowedTools` / `disallowedTools`) add entries to the allow and deny rule lists in the evaluation flow above. Allow rules only affect approval: a tool not listed in `allowed_tools` is still available to Claude and falls through to the permission mode. Deny rules behave differently depending on whether they name a tool or scope a pattern within one.

| Option                            | Effect                                                                                                                                                                             |
|:----------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `allowed_tools=["Read", "Grep"]`  | `Read` and `Grep` are auto-approved. Tools not listed here still exist and fall through to the permission mode and `canUseTool`.                                                   |
| `disallowed_tools=["Bash"]`       | The `Bash` tool definition is removed from the request. Claude does not see the tool and cannot attempt it.                                                                        |
| `disallowed_tools=["Bash(rm *)"]` | `Bash` stays available. Calls matching `rm *` are denied in every permission mode, including `bypassPermissions`. Other `Bash` calls fall through to the permission mode.          |
| `disallowed_tools=["*"]`          | Every tool definition is removed from the request. Tool-name globs are supported in deny rules: `"*"` matches every tool and `"mcp__*"` matches every MCP tool across all servers. |

Allow rules accept tool-name globs only after a literal `mcp__<server>__` prefix. The server segment must be glob-free so the rule names a specific server you configured: `mcp__puppeteer__*` matches every tool from the `puppeteer` server, and `mcp__github__get_*` matches its `get_` tools. An unanchored entry like `allowed_tools=["*"]` or `allowed_tools=["mcp__*"]` is ignored with a startup warning and does not auto-approve anything. Scoped rules for `Read` and `Edit` take a path pattern. `Edit(path)` rules govern all built-in tools that write files, including `Write` and `NotebookEdit`; a `Write(path)` rule is never matched by the file permission checks. Use `//path` for an absolute filesystem path: a deny rule of `Edit(//secrets/**)` blocks writes anywhere under `/secrets` on disk. With a single leading slash, `Edit(/secrets/**)` anchors at the rule’s source instead. For rules passed through `allowed_tools` or `disallowed_tools`, that means the session’s working directory, so the rule doesn’t block `/secrets` on disk. See [Read and Edit rules](/docs/en/permissions#read-and-edit) for the four anchor forms and how rules from settings files resolve.

**Auto-approved tools never reach `canUseTool`.** A tool call approved at any earlier step, by `acceptEdits` or `bypassPermissions`, or by an allow rule, skips your `canUseTool` callback, so permission checks you put there are silently bypassed for that tool. `AskUserQuestion`, MCP tools marked [`_meta["anthropic/requiresUserInteraction"]`](/docs/en/mcp#require-approval-for-a-specific-tool), and connector tools [your organization set to `ask`](/docs/en/mcp#organization-controls-on-connector-tools) still reach the callback, even when an allow rule matches.Coverage depends on the entry’s form: a bare name like `Read` or `mcp__github__get_issue` auto-approves every call to that tool, while a scoped rule like `Bash(ls *)` auto-approves only matching calls and other `Bash` calls still fall through to the callback. For checks that must run on every tool call, use a [`PreToolUse` hook](/docs/en/agent-sdk/hooks): hooks run before every other step, and a hook deny applies even in `bypassPermissions` mode.

For a locked-down agent, pair `allowedTools` with `permissionMode: "dontAsk"`. Listed tools are approved, apart from the always-prompt tools in the Warning above; anything else is denied outright instead of prompting:

```python
const options = {
  allowedTools: ["Read", "Glob", "Grep"],
  permissionMode: "dontAsk"
};
```

**`allowed_tools` does not constrain `bypassPermissions`.** `allowed_tools` only pre-approves the tools you list. Unlisted tools are not matched by any allow rule and fall through to the permission mode, where `bypassPermissions` approves them. Setting `allowed_tools=["Read"]` alongside `permission_mode="bypassPermissions"` still approves every tool, including `Bash`, `Write`, and `Edit`. If you need `bypassPermissions` but want specific tools blocked, use `disallowed_tools`.

You can also configure allow, deny, and ask rules declaratively in `.claude/settings.json`. These rules are read when the `project` setting source is enabled, which it is for default `query()` options. If you set `setting_sources` (TypeScript: `settingSources`) explicitly, include `"project"` for them to apply. See [Permission settings](/docs/en/settings#permission-settings) for the rule syntax.


[​](#permission-modes)

Permission modes

Permission modes provide global control over how Claude uses tools. You can set the permission mode when calling `query()` or change it dynamically during streaming sessions.


[​](#available-modes)

Available modes

The SDK supports these permission modes:

| Mode                | Description                  | Tool behavior                                                                                                                                                                                                                                                                               |
|:--------------------|:-----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `default`           | Standard permission behavior | No auto-approvals; unmatched tools trigger your `canUseTool` callback                                                                                                                                                                                                                       |
| `dontAsk`           | Deny instead of prompting    | Anything not pre-approved by `allowed_tools` or rules is denied; connector tools [your organization set to `ask`](/docs/en/mcp#organization-controls-on-connector-tools) and tools that require user interaction are denied even if you’ve pre-approved them. `canUseTool` is never called  |
| `acceptEdits`       | Auto-accept file edits       | File edits and [filesystem operations](#accept-edits-mode-acceptedits) (`mkdir`, `rm`, `mv`, etc.) are automatically approved                                                                                                                                                               |
| `bypassPermissions` | Bypass permission checks     | Tools run without permission prompts, except tools matched by an explicit [`ask` rule](#how-permissions-are-evaluated), connector tools [your organization set to `ask`](/docs/en/mcp#organization-controls-on-connector-tools), and tools that require user interaction (use with caution) |
| `plan`              | Planning mode                | Claude explores and plans without editing your source files; file edits are never auto-approved and prompt through your `canUseTool` callback                                                                                                                                               |
| `auto`              | Model-classified approvals   | A model classifier approves or denies permission prompts. See [Auto mode](/docs/en/permission-modes#eliminate-prompts-with-auto-mode) for availability                                                                                                                                      |

**Subagent inheritance:** Subagents inherit the parent session’s permission mode. An [`AgentDefinition`’s `permissionMode`](/docs/en/agent-sdk/typescript#agentdefinition) can override it, except when the parent uses `bypassPermissions`, `acceptEdits`, or `auto`: those modes apply to every subagent and can’t be overridden per subagent.Subagents may have different system prompts and less constrained behavior than your main agent, so inheriting `bypassPermissions` grants them full, autonomous system access. Explicit [`ask` rules](#how-permissions-are-evaluated), connector tools [your organization set to `ask`](/docs/en/mcp#organization-controls-on-connector-tools), and tools that require user interaction still force a prompt.


[​](#set-permission-mode)

Set permission mode

You can set the permission mode once when starting a query, or change it dynamically while the session is active.

- At query time

- During streaming

Pass `permission_mode` (Python) or `permissionMode` (TypeScript) when creating a query. This mode applies for the entire session unless changed dynamically.

Python

TypeScript

```python
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

```python
import { query } from "@anthropic-ai/claude-agent-sdk";

async function main() {
  for await (const message of query({
    prompt: "Help me refactor this code",
    options: {
      permissionMode: "default" // Set the mode here
    }
  })) {
    if ("result" in message) {
      console.log(message.result);
    }
  }
}

main();
```

Call `set_permission_mode()` (Python) or `setPermissionMode()` (TypeScript) to change the mode mid-session. The new mode takes effect immediately for all subsequent tool requests. This lets you start restrictive and loosen permissions as trust builds, for example switching to `acceptEdits` after reviewing Claude’s initial approach.

Python

TypeScript

```python
import asyncio
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions


async def main():
    async with ClaudeSDKClient(
        options=ClaudeAgentOptions(
            permission_mode="default",  # Start in default mode
        )
    ) as client:
        await client.query("Help me refactor this code")

        # Change mode dynamically mid-session
        await client.set_permission_mode("acceptEdits")

        # Process messages with the new permission mode
        async for message in client.receive_response():
            if hasattr(message, "result"):
                print(message.result)


asyncio.run(main())
```

```python
import { query } from "@anthropic-ai/claude-agent-sdk";

async function main() {
  const q = query({
    prompt: "Help me refactor this code",
    options: {
      permissionMode: "default" // Start in default mode
    }
  });

  // Change mode dynamically mid-session
  await q.setPermissionMode("acceptEdits");

  // Process messages with the new permission mode
  for await (const message of q) {
    if ("result" in message) {
      console.log(message.result);
    }
  }
}

main();
```


[​](#mode-details)

Mode details


[​](#accept-edits-mode-acceptedits)

Accept edits mode (`acceptEdits`)

Auto-approves file operations so Claude can edit code without prompting. Other tools (like Bash commands that aren’t filesystem operations) still require normal permissions. **Auto-approved operations:**

- File edits (Edit, Write tools)
- Filesystem commands: `mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, `sed`

Both apply only to paths inside the working directory or `additionalDirectories`. Paths outside that scope and writes to protected paths still prompt. **Use when:** you trust Claude’s edits and want faster iteration, such as during prototyping or when working in an isolated directory.


[​](#don’t-ask-mode-dontask)

Don’t ask mode (`dontAsk`)

Converts any permission prompt into a denial. Tools pre-approved by `allowed_tools`, `settings.json` allow rules, or a hook run as normal. Connector tools [your organization set to `ask`](/docs/en/mcp#organization-controls-on-connector-tools) and tools that require user interaction are denied even when an allow rule matches. Everything else is denied without calling `canUseTool`. **Use when:** you want a fixed, explicit tool surface for a headless agent and prefer a hard deny over silent reliance on `canUseTool` being absent.


[​](#bypass-permissions-mode-bypasspermissions)

Bypass permissions mode (`bypassPermissions`)

Auto-approves all tool uses without prompts. Hooks still execute and can block operations if needed.

Use with extreme caution. Claude has full system access in this mode. Only use in controlled environments where you trust all possible operations.`allowed_tools` does not constrain this mode. Every tool is approved, not just the ones you listed. Deny rules (`disallowed_tools`), explicit `ask` rules, and hooks are evaluated before the mode check and can still block a tool. Connector tools [your organization set to `ask`](/docs/en/mcp#organization-controls-on-connector-tools) and tools that require user interaction still fall through to your `canUseTool` callback.


[​](#plan-mode-plan)

Plan mode (`plan`)

Claude explores the codebase and produces a plan without editing your source files. Read-only tools run as in default mode. File edits are never auto-approved in plan mode, even when an allow rule matches. They prompt through your `canUseTool` callback instead. On Claude Code v2.1.212 or later, shell commands that modify files, such as `touch` and `rm`, reach your `canUseTool` callback the same way. Claude may use `AskUserQuestion` to clarify requirements before finalizing the plan. See [Handle approvals and user input](/docs/en/agent-sdk/user-input#handle-clarifying-questions) for handling these prompts. **Use when:** you want Claude to propose changes without executing them, such as during code review or when you need to approve changes before they’re made.


[​](#related-resources)

Related resources

For the other steps in the permission evaluation flow:

- [Handle approvals and user input](/docs/en/agent-sdk/user-input): interactive approval prompts and clarifying questions
- [Hooks guide](/docs/en/agent-sdk/hooks): run custom code at key points in the agent lifecycle
- [Permission rules](/docs/en/settings#permission-settings): declarative allow/deny rules in `settings.json`
