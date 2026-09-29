---
title: "Configure permissions - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/agent-sdk/permissions"
category: "05-Agent-SDK"
fetched_at: "2026-09-28T06:32:57Z"
tags: ["agents", "claude-code", "sdk"]
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

The Claude Agent SDK provides permission controls to manage how Claude uses tools. Use permission modes and rules to define what’s allowed automatically, and the [`canUseTool` callback](agent-sdk-user-input.md) to handle everything else at runtime.


[​](#how-permissions-are-evaluated)

How permissions are evaluated

When Claude requests a tool, the SDK checks permissions in this order:

1

Hooks

Run [hooks](agent-sdk-hooks.md) first. A hook can deny the call outright or pass it on. A hook that returns `allow` does not skip the deny and ask rules below; those are evaluated regardless of the hook result. A `PreToolUse` hook allow also can’t approve an `rm` or `rmdir` removal targeting a [critical path](../02-Claude-Code-CLI/permission-modes.md#critical-paths).

2

Deny rules

Check `deny` rules (from `disallowed_tools` and [settings.json](../02-Claude-Code-CLI/settings-reference.md#permission-settings)). If a deny rule matches, the tool is blocked, even in `bypassPermissions` mode. Bare-name deny rules like `Bash` remove the tool from Claude’s context before this evaluation begins, so only scoped rules like `Bash(rm *)` are checked at this step.

3

Ask rules

Check `ask` rules from [settings.json](../02-Claude-Code-CLI/settings-reference.md#permission-settings). If an ask rule matches, the call falls through to your [`canUseTool` callback](agent-sdk-user-input.md) for confirmation, even in `bypassPermissions` mode.Tools that require user interaction behave the same way: `AskUserQuestion` and MCP tools whose server sets [`_meta["anthropic/requiresUserInteraction"]`](../06-MCP-Tools/General/mcp.md#require-approval-for-a-specific-tool) always fall through to the callback, even when an allow rule matches. In `dontAsk` mode both cases are denied instead, because that mode never prompts. The MCP annotation requires Claude Code v2.1.199 or later.[claude.ai connector](../06-MCP-Tools/General/mcp.md#organization-controls-on-connector-tools) tools your organization has set to `ask` also leave the flow at this step. Every call falls through to the callback, even in `bypassPermissions` mode and even when an allow rule matches. The callback receives the reason `Your organization requires approval for this tool`. In `dontAsk` mode the call is denied instead, because that mode never prompts.

4

Permission mode

Apply the active [permission mode](#permission-modes):

- In `bypassPermissions` mode, Claude Code approves everything that reaches this step except `rm` and `rmdir` removals targeting a [critical path](../02-Claude-Code-CLI/permission-modes.md#critical-paths), which fall through instead.
- In `acceptEdits` mode, Claude Code approves the file operations listed under [Accept edits mode](#accept-edits-mode-acceptedits).
- In `plan` mode, Claude Code sends file-edit and shell-write tools to your `canUseTool` callback regardless of allow rules, so write operations can’t be auto-approved while planning.
- In other modes, the request falls through.

5

Allow rules

Check `allow` rules (from `allowed_tools` and settings.json). If a rule matches, the tool is approved. A call the tool approves on its own is resolved at this step too, with no rule needed: for example a file read inside your working directories or a [read-only Bash command](../02-Claude-Code-CLI/permissions.md#read-only-commands).`rm` and `rmdir` removals targeting a [critical path](../02-Claude-Code-CLI/permission-modes.md#critical-paths) are never approved by an allow rule. Whether they then reach your callback depends on the permission mode: in an Agent SDK session in `auto` mode, for example, Claude Code denies them by default without calling it. The [Critical paths](../02-Claude-Code-CLI/permission-modes.md#critical-paths) mode table lists what each mode does with them.

6

canUseTool callback

If not resolved by any of the above, call your [`canUseTool` callback](agent-sdk-user-input.md) for a decision. In `dontAsk` mode, this step is skipped and the tool is denied.In the TypeScript SDK, if you set [`permissionPrompts: 'none'`](agent-sdk-typescript.md#options), your callback isn’t called at this step. A [`PermissionRequest` hook](../07-Hooks/hooks.md#permissionrequest) still gets a chance to decide, and if it doesn’t, Claude Code denies the call. The option requires Claude Code v2.1.259 or later.

If you pass a `canUseTool` callback in a configuration where the TypeScript SDK expects the evaluation order to auto-approve calls before the callback is consulted, the SDK emits a Node.js process warning once when the query is constructed. The warning’s code is `CLAUDE_SDK_CAN_USE_TOOL_SHADOWED`. Two configurations trigger it:

- `permissionMode: 'bypassPermissions'`, which auto-approves every call that reaches the permission mode step apart from the [actions no mode auto-approves](../02-Claude-Code-CLI/permission-modes.md#actions-no-mode-auto-approves)
- Each bare `allowedTools` entry such as `"Read"`, which auto-approves that whole tool before the callback is consulted, apart from the [actions no mode auto-approves](../02-Claude-Code-CLI/permission-modes.md#actions-no-mode-auto-approves)

Entries with a specifier such as `Bash(ls *)` and the `acceptEdits` mode don’t trigger it, and allow rules coming from settings files aren’t visible to the check. Listen with `process.on('warning', ...)` and match the code to log or suppress it. To gate every tool call regardless of mode and rules, use a [`PreToolUse` hook](agent-sdk-hooks.md) instead. This page focuses on **allow and deny rules** and **permission modes**. For the other steps:

- **Hooks:** run custom code to allow, deny, or modify tool requests. See [Control execution with hooks](agent-sdk-hooks.md).
- **canUseTool callback:** prompt users for approval at runtime, when no earlier step resolves the call. See [Handle approvals and user input](agent-sdk-user-input.md).


[​](#allow-and-deny-rules)

Allow and deny rules

`allowed_tools` and `disallowed_tools` (TypeScript: `allowedTools` / `disallowedTools`) add entries to the allow and deny rule lists in the evaluation flow above. If you name one of the [task-tracking tools](agent-sdk-todo-tracking.md#model-availability) in `allowed_tools`, Claude Code also opts the session in. Any other tool not listed in `allowed_tools` is still available to Claude, and a call to it that needs approval falls through to the permission mode. Deny rules behave differently depending on whether they name a tool or scope a pattern within one.

| Option                            | Effect                                                                                                                                                                                                                                              |
|:----------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `allowed_tools=["Read", "Grep"]`  | `Read` and `Grep` are auto-approved. Other tools not listed here still exist, and calls to them that need approval fall through to the permission mode and `canUseTool`.                                                                            |
| `disallowed_tools=["Bash"]`       | The `Bash` tool definition is removed from the request. Claude does not see the tool and cannot attempt it.                                                                                                                                         |
| `disallowed_tools=["Bash(rm *)"]` | `Bash` stays available. Calls matching `rm *` [as written](../02-Claude-Code-CLI/permissions.md#bash-rule-limits) are denied in every permission mode, including `bypassPermissions`. Other `Bash` calls, including `/bin/rm`, fall through to the permission mode. |
| `disallowed_tools=["*"]`          | Every tool definition is removed from the request. Tool-name globs are supported in deny rules: `"*"` matches every tool and `"mcp__*"` matches every MCP tool across all servers.                                                                  |

Allow rules accept tool-name globs only after a literal `mcp__<server>__` prefix. The server segment must be glob-free so the rule names a specific server you configured: `mcp__puppeteer__*` matches every tool from the `puppeteer` server, and `mcp__github__get_*` matches its `get_` tools. An unanchored entry like `allowed_tools=["*"]` or `allowed_tools=["mcp__*"]` is ignored with a startup warning and does not auto-approve anything. Scoped rules for `Read` and `Edit` take a path pattern. `Edit(path)` rules govern all built-in tools that write files, including `Write` and `NotebookEdit`; a `Write(path)` rule is never matched by the file permission checks. Use `//path` for an absolute filesystem path: a deny rule of `Edit(//secrets/**)` blocks writes anywhere under `/secrets` on disk. With a single leading slash, `Edit(/secrets/**)` anchors at the rule’s source instead. For rules passed through `allowed_tools` or `disallowed_tools`, that means the session’s working directory, so the rule doesn’t block `/secrets` on disk. See [Read and Edit rules](../02-Claude-Code-CLI/permissions.md#read-and-edit) for the four anchor forms and how rules from settings files resolve.

**Auto-approved tools never reach `canUseTool`.** A tool call approved at any earlier step, by `acceptEdits` or `bypassPermissions`, or by an allow rule, skips your `canUseTool` callback, so permission checks you put there are silently bypassed for that tool.An allow rule never auto-approves `AskUserQuestion`, MCP tools marked [`_meta["anthropic/requiresUserInteraction"]`](../06-MCP-Tools/General/mcp.md#require-approval-for-a-specific-tool), connector tools [your organization set to `ask`](../06-MCP-Tools/General/mcp.md#organization-controls-on-connector-tools), or `rm` and `rmdir` removals targeting a [critical path](../02-Claude-Code-CLI/permission-modes.md#critical-paths). In `dontAsk` mode Claude Code denies these calls without invoking the callback. In other modes the first three reach the callback. Depending on the [permission mode](../02-Claude-Code-CLI/permission-modes.md#critical-paths), a critical-path removal reaches the callback too or Claude Code denies it without calling it, as it does by default for an Agent SDK session in `auto` mode.Coverage depends on the entry’s form: a bare name like `Read` or `mcp__github__get_issue` auto-approves every call to that tool apart from the exceptions above, while a scoped rule like `Bash(npm test *)` auto-approves only matching calls, and other `Bash` calls that need approval still fall through to the callback. For checks that must run on every tool call, use a [`PreToolUse` hook](agent-sdk-hooks.md): hooks run before every other step, and a hook deny applies even in `bypassPermissions` mode.

For a locked-down agent, pair `allowedTools` with `permissionMode: "dontAsk"`:

```python
const options = {
  allowedTools: ["Read", "Glob", "Grep"],
  permissionMode: "dontAsk"
};
```

Listed tools are approved, apart from the [actions no mode auto-approves](../02-Claude-Code-CLI/permission-modes.md#actions-no-mode-auto-approves), and every other call that would prompt is denied instead. Calls that need no approval in `default` mode run whether or not you list them, such as [read-only Bash commands](../02-Claude-Code-CLI/permissions.md#read-only-commands), tools like `Agent` that don’t ask before running, and file reads inside your working directories. To put a tool out of Claude’s reach entirely, add its bare name to `disallowedTools`.

**`allowed_tools` does not constrain `bypassPermissions`.** `allowed_tools` pre-approves the tools you list. Other unlisted tools are not matched by any allow rule and fall through to the permission mode, where `bypassPermissions` approves them. Setting `allowed_tools=["Read"]` alongside `permission_mode="bypassPermissions"` still approves every tool, including `Bash`, `Write`, and `Edit`. If you need `bypassPermissions` but want specific tools blocked, use `disallowed_tools`.

You can also configure allow, deny, and ask rules declaratively in `.claude/settings.json`. These rules are read when the `project` setting source is enabled, which it is for default `query()` options. If you set `setting_sources` (TypeScript: `settingSources`) explicitly, include `"project"` for them to apply. See [Permission settings](../02-Claude-Code-CLI/settings-reference.md#permission-settings) for the rule syntax.


[​](#permission-modes)

Permission modes

Permission modes provide global control over how Claude uses tools. You can set the permission mode when calling `query()` or change it dynamically during streaming sessions.


[​](#available-modes)

Available modes

The SDK supports these permission modes:

| Mode                | Description                  | Tool behavior                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:--------------------|:-----------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `default`           | Standard permission behavior | No mode-based auto-approvals; calls that need approval and match no allow rule trigger your `canUseTool` callback                                                                                                                                                                                                                                                                                                                                                                          |
| `dontAsk`           | Deny instead of prompting    | Any call that would otherwise prompt is denied. Calls approved by `allowed_tools` or rules run, and so do calls that need no approval in `default` mode; connector tools [your organization set to `ask`](../06-MCP-Tools/General/mcp.md#organization-controls-on-connector-tools) and tools that require user interaction are denied even if you’ve pre-approved them, as are `rm` and `rmdir` removals targeting a [critical path](../02-Claude-Code-CLI/permission-modes.md#critical-paths). `canUseTool` is never called |
| `acceptEdits`       | Auto-accept file edits       | File edits and [filesystem operations](#accept-edits-mode-acceptedits) (`mkdir`, `rm`, `mv`, etc.) are automatically approved                                                                                                                                                                                                                                                                                                                                                              |
| `bypassPermissions` | Bypass permission checks     | Tools run without permission prompts, except for the [actions no mode auto-approves](../02-Claude-Code-CLI/permission-modes.md#actions-no-mode-auto-approves). Use with caution                                                                                                                                                                                                                                                                                                                            |
| `plan`              | Planning mode                | Claude explores and plans without editing your source files; file edits are never auto-approved and prompt through your `canUseTool` callback                                                                                                                                                                                                                                                                                                                                              |
| `auto`              | Model-classified approvals   | A model classifier approves or denies permission prompts. See [Auto mode](../02-Claude-Code-CLI/permission-modes.md#eliminate-prompts-with-auto-mode) for availability                                                                                                                                                                                                                                                                                                                                     |

**Subagent inheritance:** A subagent runs in the parent session’s permission mode unless you set `permissionMode` on its [`AgentDefinition`](agent-sdk-typescript.md#agentdefinition) and the parent session is in `default`, `dontAsk`, or `plan` mode. Even then, Claude Code never applies a `"bypassPermissions"` value. A subagent runs in `bypassPermissions` mode only when the parent session itself does. The `bypassPermissions` exception requires Claude Code v2.1.267 or later.Subagents may have different system prompts and less constrained behavior than your main agent, so inheriting `bypassPermissions` grants them full, autonomous system access. The [actions no mode auto-approves](../02-Claude-Code-CLI/permission-modes.md#actions-no-mode-auto-approves) still apply.


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

Both apply only to paths inside the working directory or `additionalDirectories`. In `acceptEdits` mode, Claude Code doesn’t auto-approve the request when Claude:

- Works on a path outside that scope
- Writes to a protected path
- Removes a [critical path](../02-Claude-Code-CLI/permission-modes.md#critical-paths) with `rm` or `rmdir`

**Use when:** you trust Claude’s edits and want faster iteration, such as during prototyping or when working in an isolated directory.


[​](#don’t-ask-mode-dontask)

Don’t ask mode (`dontAsk`)

Converts any permission prompt into a denial, without calling `canUseTool`. Tools pre-approved by `allowed_tools`, `settings.json` allow rules, or a hook run as normal, and so do calls that need no approval in `default` mode, such as file reads inside your working directories and calls to `Agent`. Connector tools [your organization set to `ask`](../06-MCP-Tools/General/mcp.md#organization-controls-on-connector-tools), tools that require user interaction, and `rm` and `rmdir` removals targeting a [critical path](../02-Claude-Code-CLI/permission-modes.md#critical-paths) are denied even when an allow rule matches. A `PreToolUse` hook allow doesn’t clear a critical-path removal either. **Use when:** you want a fixed, explicit tool surface for a headless agent and prefer a hard deny over silent reliance on `canUseTool` being absent.


[​](#bypass-permissions-mode-bypasspermissions)

Bypass permissions mode (`bypassPermissions`)

Auto-approves tool uses without prompting, except the cases listed in the warning below. Hooks still execute and can block operations if needed. On Linux and macOS, Claude Code refuses to start in this mode as root or under `sudo` outside a [recognized sandbox](../02-Claude-Code-CLI/permission-modes.md#skip-all-checks-with-bypasspermissions-mode), and the query fails before the first turn.

Use with extreme caution. Claude has full system access in this mode. Only use in controlled environments where you trust all possible operations.`allowed_tools` does not constrain this mode. Every tool is approved, not just the ones you listed. These controls still apply:

- Deny rules, explicit `ask` rules, and hooks are evaluated before the mode check and can still block a tool.
- Connector tools [your organization set to `ask`](../06-MCP-Tools/General/mcp.md#organization-controls-on-connector-tools), tools that require user interaction, and `rm` and `rmdir` removals targeting a [critical path](../02-Claude-Code-CLI/permission-modes.md#critical-paths) still fall through to your `canUseTool` callback.
- The [cross-session messaging safeguards](../02-Claude-Code-CLI/permission-modes.md#skip-all-checks-with-bypasspermissions-mode) still apply.


[​](#plan-mode-plan)

Plan mode (`plan`)

Claude explores the codebase and produces a plan without editing your source files. Read-only tools run as they do in the `default` permission mode. File edits are never auto-approved in plan mode, even when an allow rule matches. They prompt through your `canUseTool` callback instead. On Claude Code v2.1.212 or later, shell commands that modify files, such as `touch` and `rm`, reach your `canUseTool` callback the same way. In the TypeScript SDK, if you set `allowDangerouslySkipPermissions: true` alongside `permissionMode: 'plan'`, file edits and shell commands that modify files still reach your `canUseTool` callback. The option lets you switch to `bypassPermissions` later with `setPermissionMode()`. Claude may use `AskUserQuestion` to clarify requirements before finalizing the plan. See [Handle approvals and user input](agent-sdk-user-input.md#handle-clarifying-questions) for handling these prompts. **Use when:** you want Claude to propose changes without executing them, such as during code review or when you need to approve changes before they’re made.


[​](#related-resources)

Related resources

For the other steps in the permission evaluation flow:

- [Handle approvals and user input](agent-sdk-user-input.md): interactive approval prompts and clarifying questions
- [Hooks guide](agent-sdk-hooks.md): run custom code at key points in the agent lifecycle
- [Permission rules](../02-Claude-Code-CLI/settings-reference.md#permission-settings): declarative allow/deny rules in `settings.json`
