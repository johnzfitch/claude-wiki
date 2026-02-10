---
category: "05-Agent-SDK"
fetched_at: "2026-02-07T10:04:39Z"
source_url: "https://platform.claude.com/docs/en/agent-sdk/hooks"
title: "Intercept and control agent behavior with hooks - Claude API Docs"
---

Guides

# Intercept and control agent behavior with hooks

Copy page

Intercept and customize agent behavior at key execution points with hooks

Copy page

Hooks let you intercept agent execution at key points to add validation, logging, security controls, or custom logic. With hooks, you can:

- **Block dangerous operations** before they execute, like destructive shell commands or unauthorized file access
- **Log and audit** every tool call for compliance, debugging, or analytics
- **Transform inputs and outputs** to sanitize data, inject credentials, or redirect file paths
- **Require human approval** for sensitive actions like database writes or API calls
- **Track session lifecycle** to manage state, clean up resources, or send notifications

A hook has two parts:

1.  **The callback function**: the logic that runs when the hook fires
2.  **The hook configuration**: tells the SDK which event to hook into (like `PreToolUse`) and which tools to match

The following example blocks the agent from modifying `.env` files. First, define a callback that checks the file path, then pass it to `query()` to run before any Write or Edit tool call:

Python

``` shiki
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, HookMatcher

# Define a hook callback that receives tool call details
async def protect_env_files(input_data, tool_use_id, context):
    # Extract the file path from the tool's input arguments
    file_path = input_data['tool_input'].get('file_path', '')
    file_name = file_path.split('/')[-1]

    # Block the operation if targeting a .env file
    if file_name == '.env':
        return {
            'hookSpecificOutput': {
                'hookEventName': input_data['hook_event_name'],
                'permissionDecision': 'deny',
                'permissionDecisionReason': 'Cannot modify .env files'
            }
        }

    # Return empty object to allow the operation
    return {}

async def main():
    async for message in query(
        prompt="Update the database configuration",
        options=ClaudeAgentOptions(
            hooks={
                # Register the hook for PreToolUse events
                # The matcher filters to only Write and Edit tool calls
                'PreToolUse': [HookMatcher(matcher='Write|Edit', hooks=[protect_env_files])]
            }
        )
    ):
        print(message)

asyncio.run(main())
```

This is a `PreToolUse` hook. It runs before the tool executes and can block or allow operations based on your logic. The rest of this guide covers all available hooks, their configuration options, and patterns for common use cases.

## 

Available hooks

The SDK provides hooks for different stages of agent execution. Some hooks are available in both SDKs, while others are TypeScript-only because the Python SDK doesn't support them.

| Hook Event | Python SDK | TypeScript SDK | What triggers it | Example use case |
|----|----|----|----|----|
| `PreToolUse` | Yes | Yes | Tool call request (can block or modify) | Block dangerous shell commands |
| `PostToolUse` | Yes | Yes | Tool execution result | Log all file changes to audit trail |
| `PostToolUseFailure` | No | Yes | Tool execution failure | Handle or log tool errors |
| `UserPromptSubmit` | Yes | Yes | User prompt submission | Inject additional context into prompts |
| `Stop` | Yes | Yes | Agent execution stop | Save session state before exit |
| `SubagentStart` | No | Yes | Subagent initialization | Track parallel task spawning |
| `SubagentStop` | Yes | Yes | Subagent completion | Aggregate results from parallel tasks |
| `PreCompact` | Yes | Yes | Conversation compaction request | Archive full transcript before summarizing |
| `PermissionRequest` | No | Yes | Permission dialog would be displayed | Custom permission handling |
| `SessionStart` | No | Yes | Session initialization | Initialize logging and telemetry |
| `SessionEnd` | No | Yes | Session termination | Clean up temporary resources |
| `Notification` | No | Yes | Agent status messages | Send agent status updates to Slack or PagerDuty |

## 

Common use cases

Hooks are flexible enough to handle many different scenarios. Here are some of the most common patterns organized by category.

Security

Security

Logging

Logging

Tool interception

Tool interception

Authorization

Authorization

- Block dangerous commands (like `rm -rf /`, destructive SQL)
- Validate file paths before write operations
- Enforce allowlists/blocklists for tool usage

## 

Configure hooks

To configure a hook for your agent, pass the hook in the `options.hooks` parameter when calling `query()`:

Python

``` shiki
async for message in query(
    prompt="Your prompt",
    options=ClaudeAgentOptions(
        hooks={
            'PreToolUse': [HookMatcher(matcher='Bash', hooks=[my_callback])]
        }
    )
):
    print(message)
```

The `hooks` option is a dictionary (Python) or object (TypeScript) where:

- **Keys** are [hook event names](#available-hooks) (e.g., `'PreToolUse'`, `'PostToolUse'`, `'Stop'`)
- **Values** are arrays of [matchers](#matchers), each containing an optional filter pattern and your [callback functions](#callback-function-inputs)

Your hook callback functions receive [input data](#input-data) about the event and return a [response](#callback-outputs) so the agent knows to allow, block, or modify the operation.

### 

Matchers

Use matchers to filter which tools trigger your callbacks:

| Option | Type | Default | Description |
|----|----|----|----|
| `matcher` | `string` | `undefined` | Regex pattern to match tool names. Built-in tools include `Bash`, `Read`, `Write`, `Edit`, `Glob`, `Grep`, `WebFetch`, `Task`, and others. MCP tools use the pattern `mcp__<server>__<action>`. |
| `hooks` | `HookCallback[]` | \- | Required. Array of callback functions to execute when the pattern matches |
| `timeout` | `number` | `60` | Timeout in seconds; increase for hooks that make external API calls |

Use the `matcher` pattern to target specific tools whenever possible. A matcher with `'Bash'` only runs for Bash commands, while omitting the pattern runs your callbacks for every tool call. Note that matchers only filter by **tool name**, not by file paths or other arguments—to filter by file path, check `tool_input.file_path` inside your callback.

Matchers only apply to tool-based hooks (`PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`). For lifecycle hooks like `Stop`, `SessionStart`, and `Notification`, matchers are ignored and the hook fires for all events of that type.

**Discovering tool names:** Check the `tools` array in the initial system message when your session starts, or add a hook without a matcher to log all tool calls.

**MCP tool naming:** MCP tools always start with `mcp__` followed by the server name and action: `mcp__<server>__<action>`. For example, if you configure a server named `playwright`, its tools will be named `mcp__playwright__browser_screenshot`, `mcp__playwright__browser_click`, etc. The server name comes from the key you use in the `mcpServers` configuration.

This example uses a matcher to run a hook only for file-modifying tools when the `PreToolUse` event fires:

Python

``` shiki
options = ClaudeAgentOptions(
    hooks={
        'PreToolUse': [
            HookMatcher(matcher='Write|Edit', hooks=[validate_file_path])
        ]
    }
)
```

### 

Callback function inputs

Every hook callback receives three arguments:

1.  **Input data** (`dict` / `HookInput`): Event details. See [input data](#input-data) for fields
2.  **Tool use ID** (`str | None` / `string | null`): Correlate `PreToolUse` and `PostToolUse` events
3.  **Context** (`HookContext`): In TypeScript, contains a `signal` property (`AbortSignal`) for cancellation. Pass this to async operations like `fetch()` so they automatically cancel if the hook times out. In Python, this argument is reserved for future use.

### 

Input data

The first argument to your hook callback contains information about the event. Field names are identical across SDKs (both use snake_case).

**Common fields** present in all hook types:

| Field | Type | Description |
|----|----|----|
| `hook_event_name` | `string` | The hook type (`PreToolUse`, `PostToolUse`, etc.) |
| `session_id` | `string` | Current session identifier |
| `transcript_path` | `string` | Path to the conversation transcript |
| `cwd` | `string` | Current working directory |

**Hook-specific fields** vary by hook type. Items marked ^(TS) are only available in the TypeScript SDK:

| Field | Type | Description | Hooks |
|----|----|----|----|
| `tool_name` | `string` | Name of the tool being called | PreToolUse, PostToolUse, PostToolUseFailure^(TS), PermissionRequest^(TS) |
| `tool_input` | `object` | Arguments passed to the tool | PreToolUse, PostToolUse, PostToolUseFailure^(TS), PermissionRequest^(TS) |
| `tool_response` | `any` | Result returned from tool execution | PostToolUse |
| `error` | `string` | Error message from tool execution failure | PostToolUseFailure^(TS) |
| `is_interrupt` | `boolean` | Whether the failure was caused by an interrupt | PostToolUseFailure^(TS) |
| `prompt` | `string` | The user's prompt text | UserPromptSubmit |
| `stop_hook_active` | `boolean` | Whether a stop hook is currently processing | Stop, SubagentStop |
| `agent_id` | `string` | Unique identifier for the subagent | SubagentStart^(TS), SubagentStop^(TS) |
| `agent_type` | `string` | Type/role of the subagent | SubagentStart^(TS) |
| `agent_transcript_path` | `string` | Path to the subagent's conversation transcript | SubagentStop^(TS) |
| `trigger` | `string` | What triggered compaction: `manual` or `auto` | PreCompact |
| `custom_instructions` | `string` | Custom instructions provided for compaction | PreCompact |
| `permission_suggestions` | `array` | Suggested permission updates for the tool | PermissionRequest^(TS) |
| `source` | `string` | How the session started: `startup`, `resume`, `clear`, or `compact` | SessionStart^(TS) |
| `reason` | `string` | Why the session ended: `clear`, `logout`, `prompt_input_exit`, `bypass_permissions_disabled`, or `other` | SessionEnd^(TS) |
| `message` | `string` | Status message from the agent | Notification^(TS) |
| `notification_type` | `string` | Type of notification: `permission_prompt`, `idle_prompt`, `auth_success`, or `elicitation_dialog` | Notification^(TS) |
| `title` | `string` | Optional title set by the agent | Notification^(TS) |

The code below defines a hook callback that uses `tool_name` and `tool_input` to log details about each tool call:

Python

``` shiki
async def log_tool_calls(input_data, tool_use_id, context):
    if input_data['hook_event_name'] == 'PreToolUse':
        print(f"Tool: {input_data['tool_name']}")
        print(f"Input: {input_data['tool_input']}")
    return {}
```

### 

Callback outputs

Your callback function returns an object that tells the SDK how to proceed. Return an empty object `{}` to allow the operation without changes. To block, modify, or add context to the operation, return an object with a `hookSpecificOutput` field containing your decision.

**Top-level fields** (outside `hookSpecificOutput`):

| Field | Type | Description |
|----|----|----|
| `continue` | `boolean` | Whether the agent should continue after this hook (default: `true`) |
| `stopReason` | `string` | Message shown when `continue` is `false` |
| `suppressOutput` | `boolean` | Hide stdout from the transcript (default: `false`) |
| `systemMessage` | `string` | Message injected into the conversation for Claude to see |

**Fields inside `hookSpecificOutput`**:

| Field | Type | Hooks | Description |
|----|----|----|----|
| `hookEventName` | `string` | All | Required. Use `input.hook_event_name` to match the current event |
| `permissionDecision` | `'allow'` \| `'deny'` \| `'ask'` | PreToolUse | Controls whether the tool executes |
| `permissionDecisionReason` | `string` | PreToolUse | Explanation shown to Claude for the decision |
| `updatedInput` | `object` | PreToolUse | Modified tool input (requires `permissionDecision: 'allow'`) |
| `additionalContext` | `string` | PreToolUse, PostToolUse, UserPromptSubmit, SessionStart^(TS), SubagentStart^(TS) | Context added to the conversation |

This example blocks write operations to the `/etc` directory while injecting a system message to remind Claude about safe file practices:

Python

``` shiki
async def block_etc_writes(input_data, tool_use_id, context):
    file_path = input_data['tool_input'].get('file_path', '')

    if file_path.startswith('/etc'):
        return {
            # Top-level field: inject guidance into the conversation
            'systemMessage': 'Remember: system directories like /etc are protected.',
            # hookSpecificOutput: block the operation
            'hookSpecificOutput': {
                'hookEventName': input_data['hook_event_name'],
                'permissionDecision': 'deny',
                'permissionDecisionReason': 'Writing to /etc is not allowed'
            }
        }
    return {}
```

#### 

Permission decision flow

When multiple hooks or permission rules apply, the SDK evaluates them in this order:

1.  **Deny** rules are checked first (any match = immediate denial).
2.  **Ask** rules are checked second.
3.  **Allow** rules are checked third.
4.  **Default to Ask** if nothing matches.

If any hook returns `deny`, the operation is blocked—other hooks returning `allow` won't override it.

#### 

Block a tool

Return a deny decision to prevent tool execution:

Python

``` shiki
async def block_dangerous_commands(input_data, tool_use_id, context):
    if input_data['hook_event_name'] != 'PreToolUse':
        return {}

    command = input_data['tool_input'].get('command', '')

    if 'rm -rf /' in command:
        return {
            'hookSpecificOutput': {
                'hookEventName': input_data['hook_event_name'],
                'permissionDecision': 'deny',
                'permissionDecisionReason': 'Dangerous command blocked: rm -rf /'
            }
        }
    return {}
```

#### 

Modify tool input

Return updated input to change what the tool receives:

Python

``` shiki
async def redirect_to_sandbox(input_data, tool_use_id, context):
    if input_data['hook_event_name'] != 'PreToolUse':
        return {}

    if input_data['tool_name'] == 'Write':
        original_path = input_data['tool_input'].get('file_path', '')
        return {
            'hookSpecificOutput': {
                'hookEventName': input_data['hook_event_name'],
                'permissionDecision': 'allow',
                'updatedInput': {
                    **input_data['tool_input'],
                    'file_path': f'/sandbox{original_path}'
                }
            }
        }
    return {}
```

When using `updatedInput`, you must also include `permissionDecision`. Always return a new object rather than mutating the original `tool_input`.

#### 

Add a system message

Inject context into the conversation:

Python

``` shiki
async def add_security_reminder(input_data, tool_use_id, context):
    return {
        'systemMessage': 'Remember to follow security best practices.'
    }
```

#### 

Auto-approve specific tools

Bypass permission prompts for trusted tools. This is useful when you want certain operations to run without user confirmation:

Python

``` shiki
async def auto_approve_read_only(input_data, tool_use_id, context):
    if input_data['hook_event_name'] != 'PreToolUse':
        return {}

    read_only_tools = ['Read', 'Glob', 'Grep', 'LS']
    if input_data['tool_name'] in read_only_tools:
        return {
            'hookSpecificOutput': {
                'hookEventName': input_data['hook_event_name'],
                'permissionDecision': 'allow',
                'permissionDecisionReason': 'Read-only tool auto-approved'
            }
        }
    return {}
```

The `permissionDecision` field accepts three values: `'allow'` (auto-approve), `'deny'` (block), or `'ask'` (prompt for confirmation).

## 

Handle advanced scenarios

These patterns help you build more sophisticated hook systems for complex use cases.

### 

Chaining multiple hooks

Hooks execute in the order they appear in the array. Keep each hook focused on a single responsibility and chain multiple hooks for complex logic. This example runs all four hooks for every tool call (no matcher specified):

Python

``` shiki
options = ClaudeAgentOptions(
    hooks={
        'PreToolUse': [
            HookMatcher(hooks=[rate_limiter]),        # First: check rate limits
            HookMatcher(hooks=[authorization_check]), # Second: verify permissions
            HookMatcher(hooks=[input_sanitizer]),     # Third: sanitize inputs
            HookMatcher(hooks=[audit_logger])         # Last: log the action
        ]
    }
)
```

### 

Tool-specific matchers with regex

Use regex patterns to match multiple tools:

Python

``` shiki
options = ClaudeAgentOptions(
    hooks={
        'PreToolUse': [
            # Match file modification tools
            HookMatcher(matcher='Write|Edit|Delete', hooks=[file_security_hook]),

            # Match all MCP tools
            HookMatcher(matcher='^mcp__', hooks=[mcp_audit_hook]),

            # Match everything (no matcher)
            HookMatcher(hooks=[global_logger])
        ]
    }
)
```

Matchers only match **tool names**, not file paths or other arguments. To filter by file path, check `tool_input.file_path` inside your hook callback.

### 

Tracking subagent activity

Use `SubagentStop` hooks to monitor subagent completion. The `tool_use_id` helps correlate parent agent calls with their subagents:

Python

``` shiki
async def subagent_tracker(input_data, tool_use_id, context):
    if input_data['hook_event_name'] == 'SubagentStop':
        print(f"[SUBAGENT] Completed")
        print(f"  Tool use ID: {tool_use_id}")
        print(f"  Stop hook active: {input_data.get('stop_hook_active')}")
    return {}

options = ClaudeAgentOptions(
    hooks={
        'SubagentStop': [HookMatcher(hooks=[subagent_tracker])]
    }
)
```

### 

Async operations in hooks

Hooks can perform async operations like HTTP requests. Handle errors gracefully by catching exceptions instead of throwing them. In TypeScript, pass the `signal` to `fetch()` so the request cancels if the hook times out:

Python

``` shiki
import aiohttp
from datetime import datetime

async def webhook_notifier(input_data, tool_use_id, context):
    if input_data['hook_event_name'] != 'PostToolUse':
        return {}

    try:
        async with aiohttp.ClientSession() as session:
            await session.post(
                'https://api.example.com/webhook',
                json={
                    'tool': input_data['tool_name'],
                    'timestamp': datetime.now().isoformat()
                }
            )
    except Exception as e:
        print(f'Webhook request failed: {e}')

    return {}
```

### 

Sending notifications (TypeScript only)

Use `Notification` hooks to receive status updates from the agent and forward them to external services like Slack or monitoring dashboards:

TypeScript

``` shiki
import { query, HookCallback, NotificationHookInput } from "@anthropic-ai/claude-agent-sdk";

const notificationHandler: HookCallback = async (input, toolUseID, { signal }) => {
  const notification = input as NotificationHookInput;

  await fetch('https://hooks.slack.com/services/YOUR/WEBHOOK/URL', {
    method: 'POST',
    body: JSON.stringify({
      text: `Agent status: ${notification.message}`
    }),
    signal
  });

  return {};
};

for await (const message of query({
  prompt: "Analyze this codebase",
  options: {
    hooks: {
      Notification: [{ hooks: [notificationHandler] }]
    }
  }
})) {
  console.log(message);
}
```

## 

Fix common issues

This section covers common issues and how to resolve them.

### 

Hook not firing

- Verify the hook event name is correct and case-sensitive (`PreToolUse`, not `preToolUse`)
- Check that your matcher pattern matches the tool name exactly
- Ensure the hook is under the correct event type in `options.hooks`
- For `SubagentStop`, `Stop`, `SessionStart`, `SessionEnd`, and `Notification` hooks, matchers are ignored. These hooks fire for all events of that type.
- Hooks may not fire when the agent hits the [`max_turns`](/docs/en/agent-sdk/python#configuration-options) limit because the session ends before hooks can execute

### 

Matcher not filtering as expected

Matchers only match **tool names**, not file paths or other arguments. To filter by file path, check `tool_input.file_path` inside your hook:

``` shiki
const myHook: HookCallback = async (input, toolUseID, { signal }) => {
  const preInput = input as PreToolUseHookInput;
  const filePath = preInput.tool_input?.file_path as string;
  if (!filePath?.endsWith('.md')) return {};  // Skip non-markdown files
  // Process markdown files...
};
```

### 

Hook timeout

- Increase the `timeout` value in the `HookMatcher` configuration
- Use the `AbortSignal` from the third callback argument to handle cancellation gracefully in TypeScript

### 

Tool blocked unexpectedly

- Check all `PreToolUse` hooks for `permissionDecision: 'deny'` returns
- Add logging to your hooks to see what `permissionDecisionReason` they're returning
- Verify matcher patterns aren't too broad (an empty matcher matches all tools)

### 

Modified input not applied

- Ensure `updatedInput` is inside `hookSpecificOutput`, not at the top level:

  ``` shiki
  return {
    hookSpecificOutput: {
      hookEventName: input.hook_event_name,
      permissionDecision: 'allow',
      updatedInput: { command: 'new command' }
    }
  };
  ```

- You must also return `permissionDecision: 'allow'` for the input modification to take effect

- Include `hookEventName` in `hookSpecificOutput` to identify which hook type the output is for

### 

Session hooks not available

`SessionStart`, `SessionEnd`, and `Notification` hooks are only available in the TypeScript SDK. The Python SDK does not support these events due to setup limitations.

### 

Subagent permission prompts multiplying

When spawning multiple subagents, each one may request permissions separately. Subagents do not automatically inherit parent agent permissions. To avoid repeated prompts, use `PreToolUse` hooks to auto-approve specific tools, or configure permission rules that apply to subagent sessions.

### 

Recursive hook loops with subagents

A `UserPromptSubmit` hook that spawns subagents can create infinite loops if those subagents trigger the same hook. To prevent this:

- Check for a subagent indicator in the hook input before spawning
- Use the `parent_tool_use_id` field to detect if you're already in a subagent context
- Scope hooks to only run for the top-level agent session

### 

systemMessage not appearing in output

The `systemMessage` field adds context to the conversation that the model sees, but it may not appear in all SDK output modes. If you need to surface hook decisions to your application, log them separately or use a dedicated output channel.

## 

Learn more

- [Permissions](/docs/en/agent-sdk/permissions): control what your agent can do
- [Custom Tools](/docs/en/agent-sdk/custom-tools): build tools to extend agent capabilities
- [TypeScript SDK Reference](/docs/en/agent-sdk/typescript)
- [Python SDK Reference](/docs/en/agent-sdk/python)

Was this page helpful?

- 

- [Available hooks](#available-hooks)

- [Common use cases](#common-use-cases)

- [Configure hooks](#configure-hooks)

- [Matchers](#matchers)

- [Callback function inputs](#callback-function-inputs)

- [Input data](#input-data)

- [Callback outputs](#callback-outputs)

- [Handle advanced scenarios](#handle-advanced-scenarios)

- [Chaining multiple hooks](#chaining-multiple-hooks)

- [Tool-specific matchers with regex](#tool-specific-matchers-with-regex)

- [Tracking subagent activity](#tracking-subagent-activity)

- [Async operations in hooks](#async-operations-in-hooks)

- [Sending notifications (TypeScript only)](#sending-notifications-type-script-only)

- [Fix common issues](#fix-common-issues)

- [Hook not firing](#hook-not-firing)

- [Matcher not filtering as expected](#matcher-not-filtering-as-expected)

- [Hook timeout](#hook-timeout)

- [Tool blocked unexpectedly](#tool-blocked-unexpectedly)

- [Modified input not applied](#modified-input-not-applied)

- [Session hooks not available](#session-hooks-not-available)

- [Subagent permission prompts multiplying](#subagent-permission-prompts-multiplying)

- [Recursive hook loops with subagents](#recursive-hook-loops-with-subagents)

- [systemMessage not appearing in output](#system-message-not-appearing-in-output)

- [Learn more](#learn-more)

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
