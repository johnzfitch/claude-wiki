---
title: "Agent SDK reference - Python - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/agent-sdk/python"
category: "09-Agents-Patterns"
fetched_at: "2026-08-02T05:38:43Z"
tags: ["agents", "claude-code", "python", "sdk"]
---

## On this page

- [Installation](#installation)
- [Choosing between query() and ClaudeSDKClient](#choosing-between-query-and-claudesdkclient)
  - [Quick comparison](#quick-comparison)
  - [When to use query() (one-off tasks)](#when-to-use-query-one-off-tasks)
  - [When to use ClaudeSDKClient (continuous conversation)](#when-to-use-claudesdkclient-continuous-conversation)
- [Functions](#functions)
  - [query()](#query)
  - [Parameters](#parameters)
  - [Returns](#returns)
  - [Example - With options](#example-with-options)
  - [tool()](#tool)
  - [Parameters](#parameters-2)
  - [Input schema options](#input-schema-options)
  - [Returns](#returns-2)
  - [Example](#example)
  - [ToolAnnotations](#toolannotations)
  - [create_sdk_mcp_server()](#create_sdk_mcp_server)
  - [Parameters](#parameters-3)
  - [Returns](#returns-3)
  - [Example](#example-2)
  - [list_sessions()](#list_sessions)
  - [Parameters](#parameters-4)
  - [Return type: SDKSessionInfo](#return-type-sdksessioninfo)
  - [Example](#example-3)
  - [get_session_messages()](#get_session_messages)
  - [Parameters](#parameters-5)
  - [Return type: SessionMessage](#return-type-sessionmessage)
  - [Example](#example-4)
  - [get_session_info()](#get_session_info)
  - [Parameters](#parameters-6)
  - [Example](#example-5)
  - [rename_session()](#rename_session)
  - [Parameters](#parameters-7)
  - [Example](#example-6)
  - [tag_session()](#tag_session)
  - [Parameters](#parameters-8)
  - [Example](#example-7)
- [Classes](#classes)
  - [ClaudeSDKClient](#claudesdkclient)
  - [Key Features](#key-features)
  - [Methods](#methods)
  - [Context Manager Support](#context-manager-support)
  - [Example - Continuing a conversation](#example-continuing-a-conversation)
  - [Example - Streaming input with ClaudeSDKClient](#example-streaming-input-with-claudesdkclient)
  - [Example - Using interrupts](#example-using-interrupts)
  - [Example - Advanced permission control](#example-advanced-permission-control)
- [Types](#types)
  - [SdkMcpTool](#sdkmcptool)
  - [Transport](#transport)
  - [ClaudeAgentOptions](#claudeagentoptions)
  - [Handle slow or stalled API responses](#handle-slow-or-stalled-api-responses)
  - [OutputFormat](#outputformat)
  - [SystemPromptPreset](#systempromptpreset)
  - [SystemPromptFile](#systempromptfile)
  - [SettingSource](#settingsource)
  - [Default behavior](#default-behavior)
  - [Why use setting_sources](#why-use-setting_sources)
  - [Settings precedence](#settings-precedence)
  - [AgentDefinition](#agentdefinition)
  - [PermissionMode](#permissionmode)
  - [EffortLevel](#effortlevel)
  - [CanUseTool](#canusetool)
  - [ToolPermissionContext](#toolpermissioncontext)
  - [PermissionResult](#permissionresult)
  - [PermissionResultAllow](#permissionresultallow)
  - [PermissionResultDeny](#permissionresultdeny)
  - [PermissionUpdate](#permissionupdate)
  - [PermissionRuleValue](#permissionrulevalue)
  - [ToolsPreset](#toolspreset)
  - [ThinkingConfig](#thinkingconfig)
  - [TaskBudget](#taskbudget)
  - [SdkBeta](#sdkbeta)
  - [McpSdkServerConfig](#mcpsdkserverconfig)
  - [McpServerConfig](#mcpserverconfig)
  - [McpStdioServerConfig](#mcpstdioserverconfig)
  - [McpSSEServerConfig](#mcpsseserverconfig)
  - [McpHttpServerConfig](#mcphttpserverconfig)
  - [McpServerStatusConfig](#mcpserverstatusconfig)
  - [McpStatusResponse](#mcpstatusresponse)
  - [McpServerStatus](#mcpserverstatus)
  - [SdkPluginConfig](#sdkpluginconfig)
- [Message Types](#message-types)
  - [Message](#message)
  - [UserMessage](#usermessage)
  - [AssistantMessage](#assistantmessage)
  - [AssistantMessageError](#assistantmessageerror)
  - [SystemMessage](#systemmessage)
  - [ResultMessage](#resultmessage)
  - [StreamEvent](#streamevent)
  - [RateLimitEvent](#ratelimitevent)
  - [RateLimitInfo](#ratelimitinfo)
  - [TaskStartedMessage](#taskstartedmessage)
  - [TaskUsage](#taskusage)
  - [TaskProgressMessage](#taskprogressmessage)
  - [TaskNotificationMessage](#tasknotificationmessage)
- [Content Block Types](#content-block-types)
  - [ContentBlock](#contentblock)
  - [TextBlock](#textblock)
  - [ThinkingBlock](#thinkingblock)
  - [ToolUseBlock](#tooluseblock)
  - [ToolResultBlock](#toolresultblock)
- [Error Types](#error-types)
  - [ClaudeSDKError](#claudesdkerror)
  - [CLINotFoundError](#clinotfounderror)
  - [CLIConnectionError](#cliconnectionerror)
  - [ProcessError](#processerror)
  - [CLIJSONDecodeError](#clijsondecodeerror)
- [Hook Types](#hook-types)
  - [HookEvent](#hookevent)
  - [HookCallback](#hookcallback)
  - [HookContext](#hookcontext)
  - [HookMatcher](#hookmatcher)
  - [HookInput](#hookinput)
  - [BaseHookInput](#basehookinput)
  - [PreToolUseHookInput](#pretoolusehookinput)
  - [PostToolUseHookInput](#posttoolusehookinput)
  - [PostToolUseFailureHookInput](#posttoolusefailurehookinput)
  - [UserPromptSubmitHookInput](#userpromptsubmithookinput)
  - [StopHookInput](#stophookinput)
  - [SubagentStopHookInput](#subagentstophookinput)
  - [PreCompactHookInput](#precompacthookinput)
  - [NotificationHookInput](#notificationhookinput)
  - [SubagentStartHookInput](#subagentstarthookinput)
  - [PermissionRequestHookInput](#permissionrequesthookinput)
  - [HookJSONOutput](#hookjsonoutput)
  - [SyncHookJSONOutput](#synchookjsonoutput)
  - [HookSpecificOutput](#hookspecificoutput)
  - [AsyncHookJSONOutput](#asynchookjsonoutput)
  - [Hook Usage Example](#hook-usage-example)
- [Tool Input/Output Types](#tool-input%2Foutput-types)
  - [Agent](#agent)
  - [AskUserQuestion](#askuserquestion)
  - [Bash](#bash)
  - [Monitor](#monitor)
  - [Edit](#edit)
  - [Read](#read)
  - [Write](#write)
  - [Glob](#glob)
  - [Grep](#grep)
  - [NotebookEdit](#notebookedit)
  - [WebFetch](#webfetch)
  - [WebSearch](#websearch)
  - [TodoWrite](#todowrite)
  - [TaskCreate](#taskcreate)
  - [TaskUpdate](#taskupdate)
  - [TaskGet](#taskget)
  - [TaskList](#tasklist)
  - [TaskOutput](#taskoutput)
  - [TaskStop](#taskstop)
  - [ExitPlanMode](#exitplanmode)
  - [ListMcpResources](#listmcpresources)
  - [ReadMcpResource](#readmcpresource)
- [Advanced Features with ClaudeSDKClient](#advanced-features-with-claudesdkclient)
  - [Building a Continuous Conversation Interface](#building-a-continuous-conversation-interface)
  - [Using Hooks for Behavior Modification](#using-hooks-for-behavior-modification)
  - [Real-time Progress Monitoring](#real-time-progress-monitoring)
- [Example Usage](#example-usage)
  - [Basic file operations (using query)](#basic-file-operations-using-query)
  - [Error handling](#error-handling)
  - [Streaming mode with client](#streaming-mode-with-client)
  - [Using custom tools with ClaudeSDKClient](#using-custom-tools-with-claudesdkclient)
- [Sandbox Configuration](#sandbox-configuration)
  - [SandboxSettings](#sandboxsettings)
  - [Example usage](#example-usage-2)
  - [SandboxNetworkConfig](#sandboxnetworkconfig)
  - [SandboxIgnoreViolations](#sandboxignoreviolations)
  - [Permissions Fallback for Unsandboxed Commands](#permissions-fallback-for-unsandboxed-commands)
- [See also](#see-also)

SDK references

# Agent SDK reference - Python

Copy pageCopy page

Complete API reference for the Python Agent SDK, including all functions, types, and classes.

Copy pageCopy page


[​](#installation)

Installation

Install the package into a virtual environment. On recent Debian, Ubuntu, and Homebrew Python installs, running `pip install` against system Python fails with `error: externally-managed-environment`.

```python
python3 -m venv .venv
source .venv/bin/activate
pip install claude-agent-sdk
```

For uv, Windows PowerShell, and API key setup, see [Setup in the Agent SDK quickstart](/docs/en/agent-sdk/quickstart#setup).


[​](#choosing-between-query-and-claudesdkclient)

Choosing between `query()` and `ClaudeSDKClient`

The Python SDK provides two ways to interact with Claude Code:


[​](#quick-comparison)

Quick comparison

| Feature             | `query()`                                      | `ClaudeSDKClient`                  |
|:--------------------|:-----------------------------------------------|:-----------------------------------|
| **Session**         | Creates a new session by default               | Reuses same session                |
| **Conversation**    | Single exchange                                | Multiple exchanges in same context |
| **Connection**      | Managed automatically                          | Manual control                     |
| **Streaming Input** | ✅ Supported                                   | ✅ Supported                       |
| **Interrupts**      | ❌ Not supported                               | ✅ Supported                       |
| **Hooks**           | ✅ Supported                                   | ✅ Supported                       |
| **Custom Tools**    | ✅ Supported                                   | ✅ Supported                       |
| **Continue Chat**   | Manual via `continue_conversation` or `resume` | ✅ Automatic                       |
| **Use Case**        | One-off tasks                                  | Continuous conversations           |


[​](#when-to-use-query-one-off-tasks)

When to use `query()` (one-off tasks)

**Best for:**

- One-off questions where you don’t need conversation history
- Independent tasks that don’t require context from previous exchanges
- Simple automation scripts
- When you want a fresh start each time


[​](#when-to-use-claudesdkclient-continuous-conversation)

When to use `ClaudeSDKClient` (continuous conversation)

**Best for:**

- **Continuing conversations** - When you need Claude to remember context
- **Follow-up questions** - Building on previous responses
- **Interactive applications** - Chat interfaces, REPLs
- **Response-driven logic** - When next action depends on Claude’s response
- **Session control** - Managing conversation lifecycle explicitly


[​](#functions)

Functions

Signature blocks and bare `async for` / `async with` fragments on this page are illustrative. To run them, wrap the body in `async def main(): ...` and call `asyncio.run(main())`.


[​](#query)

`query()`

Creates a new session for each interaction with Claude Code by default. Returns an async iterator that yields messages as they arrive. Each call to `query()` starts fresh with no memory of previous interactions unless you pass `continue_conversation=True` or `resume` in [`ClaudeAgentOptions`](#claudeagentoptions). See [Sessions](/docs/en/agent-sdk/sessions).

```python
async def query(
    *,
    prompt: str | AsyncIterable[dict[str, Any]],
    options: ClaudeAgentOptions | None = None,
    transport: Transport | None = None
) -> AsyncIterator[Message]
```


[​](#parameters)

Parameters

| Parameter   | Type                        | Description                                                                |
|:------------|:----------------------------|:---------------------------------------------------------------------------|
| `prompt`    | `str | AsyncIterable[dict]` | The input prompt as a string or async iterable for streaming mode          |
| `options`   | `ClaudeAgentOptions | None` | Optional configuration object (defaults to `ClaudeAgentOptions()` if None) |
| `transport` | `Transport | None`          | Optional custom transport for communicating with the CLI process           |


[​](#returns)

Returns

Returns an `AsyncIterator[Message]` that yields messages from the conversation.


[​](#example-with-options)

Example - With options

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions


async def main():
    options = ClaudeAgentOptions(
        system_prompt="You are an expert Python developer",
        permission_mode="acceptEdits",
    )

    async for message in query(prompt="Create a Python web server", options=options):
        print(message)


asyncio.run(main())
```


[​](#tool)

`tool()`

Decorator for defining MCP tools with type safety.

```python
def tool(
    name: str,
    description: str,
    input_schema: type | dict[str, Any],
    annotations: ToolAnnotations | None = None
) -> Callable[[Callable[[Any], Awaitable[dict[str, Any]]]], SdkMcpTool[Any]]
```


[​](#parameters-2)

Parameters

| Parameter      | Type                                           | Description                                                         |
|:---------------|:-----------------------------------------------|:--------------------------------------------------------------------|
| `name`         | `str`                                          | Unique identifier for the tool                                      |
| `description`  | `str`                                          | Human-readable description of what the tool does                    |
| `input_schema` | `type | dict[str, Any]`                        | Schema defining the tool’s input parameters (see below)             |
| `annotations`  | [`ToolAnnotations`](#toolannotations)` | None` | Optional MCP tool annotations providing behavioral hints to clients |


[​](#input-schema-options)

Input schema options

1.  **Simple type mapping** (recommended):

    ``` shiki
    {"text": str, "count": int, "enabled": bool}
    ```
2.  **JSON Schema format** (for complex validation):

    ``` shiki
    {
        "type": "object",
        "properties": {
            "text": {"type": "string"},
            "count": {"type": "integer", "minimum": 0},
        },
        "required": ["text"],
    }
    ```


[​](#returns-2)

Returns

A decorator function that wraps the tool implementation and returns an `SdkMcpTool` instance.


[​](#example)

Example

```python
from claude_agent_sdk import tool
from typing import Any


@tool("greet", "Greet a user", {"name": str})
async def greet(args: dict[str, Any]) -> dict[str, Any]:
    return {"content": [{"type": "text", "text": f"Hello, {args['name']}!"}]}
```


[​](#toolannotations)

`ToolAnnotations`

Re-exported from `mcp.types` (also available as `from claude_agent_sdk import ToolAnnotations`). All fields are optional hints; clients should not rely on them for security decisions.

| Field             | Type          | Default | Description                                                                                                                                          |
|:------------------|:--------------|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `title`           | `str | None`  | `None`  | Human-readable title for the tool                                                                                                                    |
| `readOnlyHint`    | `bool | None` | `False` | If `True`, the tool does not modify its environment                                                                                                  |
| `destructiveHint` | `bool | None` | `True`  | If `True`, the tool may perform destructive updates (only meaningful when `readOnlyHint` is `False`)                                                 |
| `idempotentHint`  | `bool | None` | `False` | If `True`, repeated calls with the same arguments have no additional effect (only meaningful when `readOnlyHint` is `False`)                         |
| `openWorldHint`   | `bool | None` | `True`  | If `True`, the tool interacts with external entities (for example, web search). If `False`, the tool’s domain is closed (for example, a memory tool) |

```python
from claude_agent_sdk import tool, ToolAnnotations
from typing import Any


@tool(
    "search",
    "Search the web",
    {"query": str},
    annotations=ToolAnnotations(readOnlyHint=True, openWorldHint=True),
)
async def search(args: dict[str, Any]) -> dict[str, Any]:
    return {"content": [{"type": "text", "text": f"Results for: {args['query']}"}]}
```


[​](#create_sdk_mcp_server)

`create_sdk_mcp_server()`

Create an in-process MCP server that runs within your Python application.

```python
def create_sdk_mcp_server(
    name: str,
    version: str = "1.0.0",
    tools: list[SdkMcpTool[Any]] | None = None
) -> McpSdkServerConfig
```


[​](#parameters-3)

Parameters

| Parameter | Type                           | Default   | Description                                           |
|:----------|:-------------------------------|:----------|:------------------------------------------------------|
| `name`    | `str`                          | \-        | Unique identifier for the server                      |
| `version` | `str`                          | `"1.0.0"` | Server version string                                 |
| `tools`   | `list[SdkMcpTool[Any]] | None` | `None`    | List of tool functions created with `@tool` decorator |


[​](#returns-3)

Returns

Returns an `McpSdkServerConfig` object that can be passed to `ClaudeAgentOptions.mcp_servers`.


[​](#example-2)

Example

```python
from claude_agent_sdk import tool, create_sdk_mcp_server, ClaudeAgentOptions


@tool("add", "Add two numbers", {"a": float, "b": float})
async def add(args):
    return {"content": [{"type": "text", "text": f"Sum: {args['a'] + args['b']}"}]}


@tool("multiply", "Multiply two numbers", {"a": float, "b": float})
async def multiply(args):
    return {"content": [{"type": "text", "text": f"Product: {args['a'] * args['b']}"}]}


calculator = create_sdk_mcp_server(
    name="calculator",
    version="2.0.0",
    tools=[add, multiply],  # Pass decorated functions
)

# Use with Claude
options = ClaudeAgentOptions(
    mcp_servers={"calc": calculator},
    allowed_tools=["mcp__calc__add", "mcp__calc__multiply"],
)
```


[​](#list_sessions)

`list_sessions()`

Lists past sessions with metadata. Filter by project directory or list sessions across all projects. Synchronous; returns immediately.

```python
def list_sessions(
    directory: str | None = None,
    limit: int | None = None,
    offset: int = 0,
    include_worktrees: bool = True
) -> list[SDKSessionInfo]
```


[​](#parameters-4)

Parameters

| Parameter           | Type         | Default | Description                                                                                      |
|:--------------------|:-------------|:--------|:-------------------------------------------------------------------------------------------------|
| `directory`         | `str | None` | `None`  | Directory to list sessions for. When omitted, returns sessions across all projects               |
| `limit`             | `int | None` | `None`  | Maximum number of sessions to return                                                             |
| `offset`            | `int`        | `0`     | Number of sessions to skip from the start of the sorted results. Use with `limit` for pagination |
| `include_worktrees` | `bool`       | `True`  | When `directory` is inside a git repository, include sessions from all worktree paths            |


[​](#return-type-sdksessioninfo)

Return type: `SDKSessionInfo`

| Property        | Type         | Description                                                          |
|:----------------|:-------------|:---------------------------------------------------------------------|
| `session_id`    | `str`        | Unique session identifier                                            |
| `summary`       | `str`        | Display title: custom title, auto-generated summary, or first prompt |
| `last_modified` | `int`        | Last modified time in milliseconds since epoch                       |
| `file_size`     | `int | None` | Session file size in bytes (`None` for remote storage backends)      |
| `custom_title`  | `str | None` | User-set session title                                               |
| `first_prompt`  | `str | None` | First meaningful user prompt in the session                          |
| `git_branch`    | `str | None` | Git branch at the end of the session                                 |
| `cwd`           | `str | None` | Working directory for the session                                    |
| `tag`           | `str | None` | User-set session tag (see [`tag_session()`](#tag_session))           |
| `created_at`    | `int | None` | Session creation time in milliseconds since epoch                    |


[​](#example-3)

Example

Print the 10 most recent sessions for a project. Results are sorted by `last_modified` descending, so the first item is the newest. Omit `directory` to search across all projects.

```python
from claude_agent_sdk import list_sessions

for session in list_sessions(directory="/path/to/project", limit=10):
    print(f"{session.summary} ({session.session_id})")
```


[​](#get_session_messages)

`get_session_messages()`

Retrieves messages from a past session. Synchronous; returns immediately.

```python
def get_session_messages(
    session_id: str,
    directory: str | None = None,
    limit: int | None = None,
    offset: int = 0
) -> list[SessionMessage]
```


[​](#parameters-5)

Parameters

| Parameter    | Type         | Default  | Description                                                       |
|:-------------|:-------------|:---------|:------------------------------------------------------------------|
| `session_id` | `str`        | required | The session ID to retrieve messages for                           |
| `directory`  | `str | None` | `None`   | Project directory to look in. When omitted, searches all projects |
| `limit`      | `int | None` | `None`   | Maximum number of messages to return                              |
| `offset`     | `int`        | `0`      | Number of messages to skip from the start                         |


[​](#return-type-sessionmessage)

Return type: `SessionMessage`

| Property             | Type                           | Description               |
|:---------------------|:-------------------------------|:--------------------------|
| `type`               | `Literal["user", "assistant"]` | Message role              |
| `uuid`               | `str`                          | Unique message identifier |
| `session_id`         | `str`                          | Session identifier        |
| `message`            | `Any`                          | Raw message content       |
| `parent_tool_use_id` | `None`                         | Reserved for future use   |


[​](#example-4)

Example

```python
from claude_agent_sdk import list_sessions, get_session_messages

sessions = list_sessions(limit=1)
if sessions:
    messages = get_session_messages(sessions[0].session_id)
    for msg in messages:
        print(f"[{msg.type}] {msg.uuid}")
```


[​](#get_session_info)

`get_session_info()`

Reads metadata for a single session by ID without scanning the full project directory. Synchronous; returns immediately.

```python
def get_session_info(
    session_id: str,
    directory: str | None = None,
) -> SDKSessionInfo | None
```


[​](#parameters-6)

Parameters

| Parameter    | Type         | Default  | Description                                                            |
|:-------------|:-------------|:---------|:-----------------------------------------------------------------------|
| `session_id` | `str`        | required | UUID of the session to look up                                         |
| `directory`  | `str | None` | `None`   | Project directory path. When omitted, searches all project directories |

Returns [`SDKSessionInfo`](#return-type-sdksessioninfo), or `None` if the session is not found.


[​](#example-5)

Example

Look up a single session’s metadata without scanning the project directory. Useful when you already have a session ID from a previous run.

```python
from claude_agent_sdk import get_session_info

info = get_session_info("550e8400-e29b-41d4-a716-446655440000")
if info:
    print(f"{info.summary} (branch: {info.git_branch}, tag: {info.tag})")
```


[​](#rename_session)

`rename_session()`

Renames a session by appending a custom-title entry. Repeated calls are safe; the most recent title wins. Synchronous.

```python
def rename_session(
    session_id: str,
    title: str,
    directory: str | None = None,
) -> None
```


[​](#parameters-7)

Parameters

| Parameter    | Type         | Default  | Description                                                            |
|:-------------|:-------------|:---------|:-----------------------------------------------------------------------|
| `session_id` | `str`        | required | UUID of the session to rename                                          |
| `title`      | `str`        | required | New title. Must be non-empty after stripping whitespace                |
| `directory`  | `str | None` | `None`   | Project directory path. When omitted, searches all project directories |

Raises `ValueError` if `session_id` is not a valid UUID or `title` is empty; `FileNotFoundError` if the session cannot be found.


[​](#example-6)

Example

Rename the most recent session so it’s easier to find later. The new title appears in [`SDKSessionInfo.custom_title`](#return-type-sdksessioninfo) on subsequent reads.

```python
from claude_agent_sdk import list_sessions, rename_session

sessions = list_sessions(directory="/path/to/project", limit=1)
if sessions:
    rename_session(sessions[0].session_id, "Refactor auth module")
```


[​](#tag_session)

`tag_session()`

Tags a session. Pass `None` to clear the tag. Repeated calls are safe; the most recent tag wins. Synchronous.

```python
def tag_session(
    session_id: str,
    tag: str | None,
    directory: str | None = None,
) -> None
```


[​](#parameters-8)

Parameters

| Parameter    | Type         | Default  | Description                                                            |
|:-------------|:-------------|:---------|:-----------------------------------------------------------------------|
| `session_id` | `str`        | required | UUID of the session to tag                                             |
| `tag`        | `str | None` | required | Tag string, or `None` to clear. Unicode-sanitized before storing       |
| `directory`  | `str | None` | `None`   | Project directory path. When omitted, searches all project directories |

Raises `ValueError` if `session_id` is not a valid UUID or `tag` is empty after sanitization; `FileNotFoundError` if the session cannot be found.


[​](#example-7)

Example

Tag a session, then filter by that tag on a later read. Pass `None` to clear an existing tag.

```python
from claude_agent_sdk import list_sessions, tag_session

# Tag the most recent session
sessions = list_sessions(directory="/path/to/project", limit=1)
if sessions:
    tag_session(sessions[0].session_id, "needs-review")

# Later: find all sessions with that tag
for session in list_sessions(directory="/path/to/project"):
    if session.tag == "needs-review":
        print(session.summary)
```


[​](#classes)

Classes


[​](#claudesdkclient)

`ClaudeSDKClient`

**Maintains a conversation session across multiple exchanges.** This is the Python equivalent of how the TypeScript SDK’s `query()` function works internally - it creates a client object that can continue conversations.


[​](#key-features)

Key Features

- **Session continuity**: Maintains conversation context across multiple `query()` calls
- **Same conversation**: The session retains previous messages
- **Interrupt support**: Can stop execution mid-task
- **Explicit lifecycle**: You control when the session starts and ends
- **Response-driven flow**: Can react to responses and send follow-ups
- **Custom tools and hooks**: Supports custom tools (created with `@tool` decorator) and hooks

```python
class ClaudeSDKClient:
    def __init__(self, options: ClaudeAgentOptions | None = None, transport: Transport | None = None)
    async def connect(self, prompt: str | AsyncIterable[dict] | None = None) -> None
    async def query(self, prompt: str | AsyncIterable[dict], session_id: str = "default") -> None
    async def receive_messages(self) -> AsyncIterator[Message]
    async def receive_response(self) -> AsyncIterator[Message]
    async def interrupt(self) -> None
    async def set_permission_mode(self, mode: str) -> None
    async def set_model(self, model: str | None = None) -> None
    async def rewind_files(self, user_message_id: str) -> None
    async def get_mcp_status(self) -> McpStatusResponse
    async def reconnect_mcp_server(self, server_name: str) -> None
    async def toggle_mcp_server(self, server_name: str, enabled: bool) -> None
    async def stop_task(self, task_id: str) -> None
    async def get_server_info(self) -> dict[str, Any] | None
    async def disconnect(self) -> None
```


[​](#methods)

Methods

| Method                                    | Description                                                                                                                                                            |
|:------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `__init__(options)`                       | Initialize the client with optional configuration                                                                                                                      |
| `connect(prompt)`                         | Connect to Claude with an optional initial prompt or message stream                                                                                                    |
| `query(prompt, session_id)`               | Send a new request in streaming mode                                                                                                                                   |
| `receive_messages()`                      | Receive all messages from Claude as an async iterator                                                                                                                  |
| `receive_response()`                      | Receive messages until and including a ResultMessage                                                                                                                   |
| `interrupt()`                             | Send interrupt signal (only works in streaming mode)                                                                                                                   |
| `set_permission_mode(mode)`               | Change the permission mode for the current session                                                                                                                     |
| `set_model(model)`                        | Change the model for the current session. Pass `None` to reset to default                                                                                              |
| `rewind_files(user_message_id)`           | Restore files to their state at the specified user message. Requires `enable_file_checkpointing=True`. See [File checkpointing](/docs/en/agent-sdk/file-checkpointing) |
| `get_mcp_status()`                        | Get the status of all configured MCP servers. Returns [`McpStatusResponse`](#mcpstatusresponse)                                                                        |
| `reconnect_mcp_server(server_name)`       | Retry connecting to an MCP server that failed or was disconnected                                                                                                      |
| `toggle_mcp_server(server_name, enabled)` | Enable or disable an MCP server mid-session. Disabling removes its tools                                                                                               |
| `stop_task(task_id)`                      | Stop a running background task. A [`TaskNotificationMessage`](#tasknotificationmessage) with status `"stopped"` follows in the message stream                          |
| `get_server_info()`                       | Get server information including session ID and capabilities                                                                                                           |
| `disconnect()`                            | Disconnect from Claude                                                                                                                                                 |


[​](#context-manager-support)

Context Manager Support

The client can be used as an async context manager for automatic connection management:

```python
import asyncio
from claude_agent_sdk import ClaudeSDKClient


async def main():
    async with ClaudeSDKClient() as client:
        await client.query("Hello Claude")
        async for message in client.receive_response():
            print(message)


asyncio.run(main())
```

> **Important:** When iterating over messages, avoid using `break` to exit early as this can cause asyncio cleanup issues. Instead, let the iteration complete naturally or use flags to track when you’ve found what you need.


[​](#example-continuing-a-conversation)

Example - Continuing a conversation

```python
import asyncio
from claude_agent_sdk import ClaudeSDKClient, AssistantMessage, TextBlock, ResultMessage


async def main():
    async with ClaudeSDKClient() as client:
        # First question
        await client.query("What's the capital of France?")

        # Process response
        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        print(f"Claude: {block.text}")

        # Follow-up question - the session retains the previous context
        await client.query("What's the population of that city?")

        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        print(f"Claude: {block.text}")

        # Another follow-up - still in the same conversation
        await client.query("What are some famous landmarks there?")

        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        print(f"Claude: {block.text}")


asyncio.run(main())
```


[​](#example-streaming-input-with-claudesdkclient)

Example - Streaming input with ClaudeSDKClient

```python
import asyncio
from claude_agent_sdk import ClaudeSDKClient


async def message_stream():
    """Generate messages dynamically."""
    yield {
        "type": "user",
        "message": {"role": "user", "content": "Analyze the following data:"},
    }
    await asyncio.sleep(0.5)
    yield {
        "type": "user",
        "message": {"role": "user", "content": "Temperature: 25°C, Humidity: 60%"},
    }
    await asyncio.sleep(0.5)
    yield {
        "type": "user",
        "message": {"role": "user", "content": "What patterns do you see?"},
    }


async def main():
    async with ClaudeSDKClient() as client:
        # Stream input to Claude
        await client.query(message_stream())

        # Process response
        async for message in client.receive_response():
            print(message)

        # Follow-up in same session
        await client.query("Should we be concerned about these readings?")

        async for message in client.receive_response():
            print(message)


asyncio.run(main())
```


[​](#example-using-interrupts)

Example - Using interrupts

```python
import asyncio
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, ResultMessage


async def interruptible_task():
    options = ClaudeAgentOptions(allowed_tools=["Bash"], permission_mode="acceptEdits")

    async with ClaudeSDKClient(options=options) as client:
        # Start a long-running task
        await client.query("Count from 1 to 100 slowly, using the bash sleep command")

        # Let it run for a bit
        await asyncio.sleep(2)

        # Interrupt the task
        await client.interrupt()
        print("Task interrupted!")

        # Drain the interrupted task's messages (including its ResultMessage)
        async for message in client.receive_response():
            if isinstance(message, ResultMessage):
                print(f"Interrupted task: terminal_reason={message.terminal_reason!r}")
                # terminal_reason is "aborted_streaming" or "aborted_tools"
                # for interrupted turns

        # Send a new command
        await client.query("Just say hello instead")

        # Now receive the new response
        async for message in client.receive_response():
            if isinstance(message, ResultMessage) and message.subtype == "success":
                print(f"New result: {message.result}")


asyncio.run(interruptible_task())
```

**Buffer behavior after interrupt:** `interrupt()` sends a stop signal but does not clear the message buffer. Messages already produced by the interrupted task, including its `ResultMessage`, remain in the stream. You must drain them with `receive_response()` before reading the response to a new query. If you send a new query immediately after `interrupt()` and call `receive_response()` only once, you’ll receive the interrupted task’s messages, not the new query’s response.


[​](#example-advanced-permission-control)

Example - Advanced permission control

```python
import asyncio
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions
from claude_agent_sdk.types import (
    PermissionResultAllow,
    PermissionResultDeny,
    ToolPermissionContext,
)


async def custom_permission_handler(
    tool_name: str, input_data: dict, context: ToolPermissionContext
) -> PermissionResultAllow | PermissionResultDeny:
    """Custom logic for tool permissions."""

    # Block writes to system directories
    if tool_name == "Write" and input_data.get("file_path", "").startswith("/system/"):
        return PermissionResultDeny(
            message="System directory write not allowed", interrupt=True
        )

    # Redirect sensitive file operations
    if tool_name in ["Write", "Edit"] and "config" in input_data.get("file_path", ""):
        safe_path = f"./sandbox/{input_data['file_path']}"
        return PermissionResultAllow(
            updated_input={**input_data, "file_path": safe_path}
        )

    # Allow everything else
    return PermissionResultAllow(updated_input=input_data)


async def main():
    # Don't also list the gated tools in allowed_tools: allow rules approve calls before can_use_tool runs
    options = ClaudeAgentOptions(can_use_tool=custom_permission_handler)

    async with ClaudeSDKClient(options=options) as client:
        await client.query("Update the system config file")

        async for message in client.receive_response():
            # Will use sandbox path instead
            print(message)


asyncio.run(main())
```


[​](#types)

Types

**`@dataclass` vs `TypedDict`:** This SDK uses two kinds of types. Classes decorated with `@dataclass` (such as `ResultMessage`, `AgentDefinition`, `TextBlock`) are object instances at runtime and support attribute access: `msg.result`. Classes defined with `TypedDict` (such as `ThinkingConfigEnabled`, `McpStdioServerConfig`, `SyncHookJSONOutput`) are **plain dicts at runtime** and require key access: `config["budget_tokens"]`, not `config.budget_tokens`. The `ClassName(field=value)` call syntax works for both, but only dataclasses produce objects with attributes.


[​](#sdkmcptool)

`SdkMcpTool`

Definition for an SDK MCP tool created with the `@tool` decorator.

```python
@dataclass
class SdkMcpTool(Generic[T]):
    name: str
    description: str
    input_schema: type[T] | dict[str, Any]
    handler: Callable[[T], Awaitable[dict[str, Any]]]
    annotations: ToolAnnotations | None = None
```

| Property       | Type                                       | Description                                                                                                |
|:---------------|:-------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| `name`         | `str`                                      | Unique identifier for the tool                                                                             |
| `description`  | `str`                                      | Human-readable description                                                                                 |
| `input_schema` | `type[T] | dict[str, Any]`                 | Schema for input validation                                                                                |
| `handler`      | `Callable[[T], Awaitable[dict[str, Any]]]` | Async function that handles tool execution                                                                 |
| `annotations`  | `ToolAnnotations | None`                   | Optional MCP tool annotations (e.g., `readOnlyHint`, `destructiveHint`, `openWorldHint`). From `mcp.types` |


[​](#transport)

`Transport`

Abstract base class for custom transport implementations. Use this to communicate with the Claude process over a custom channel (for example, a remote connection instead of a local subprocess).

This is a low-level internal API. The interface may change in future releases. Custom implementations must be updated to match any interface changes.

```python
from abc import ABC, abstractmethod
from collections.abc import AsyncIterator
from typing import Any


class Transport(ABC):
    @abstractmethod
    async def connect(self) -> None: ...

    @abstractmethod
    async def write(self, data: str) -> None: ...

    @abstractmethod
    def read_messages(self) -> AsyncIterator[dict[str, Any]]: ...

    @abstractmethod
    async def close(self) -> None: ...

    @abstractmethod
    def is_ready(self) -> bool: ...

    @abstractmethod
    async def end_input(self) -> None: ...
```

| Method            | Description                                                                 |
|:------------------|:----------------------------------------------------------------------------|
| `connect()`       | Connect the transport and prepare for communication                         |
| `write(data)`     | Write raw data (JSON + newline) to the transport                            |
| `read_messages()` | Async iterator that yields parsed JSON messages                             |
| `close()`         | Close the connection and clean up resources                                 |
| `is_ready()`      | Returns `True` if the transport can send and receive                        |
| `end_input()`     | Close the input stream (for example, close stdin for subprocess transports) |

Import: `from claude_agent_sdk import Transport`


[​](#claudeagentoptions)

`ClaudeAgentOptions`

Configuration dataclass for Claude Code queries.

```python
@dataclass
class ClaudeAgentOptions:
    tools: list[str] | ToolsPreset | None = None
    allowed_tools: list[str] = field(default_factory=list)
    system_prompt: str | SystemPromptPreset | SystemPromptFile | None = None
    mcp_servers: dict[str, McpServerConfig] | str | Path = field(default_factory=dict)
    strict_mcp_config: bool = False
    permission_mode: PermissionMode | None = None
    continue_conversation: bool = False
    resume: str | None = None
    session_id: str | None = None
    max_turns: int | None = None
    max_budget_usd: float | None = None
    disallowed_tools: list[str] = field(default_factory=list)
    model: str | None = None
    fallback_model: str | None = None
    betas: list[SdkBeta] = field(default_factory=list)
    output_format: dict[str, Any] | None = None
    permission_prompt_tool_name: str | None = None
    cwd: str | Path | None = None
    cli_path: str | Path | None = None
    settings: str | None = None
    add_dirs: list[str | Path] = field(default_factory=list)
    env: dict[str, str] = field(default_factory=dict)
    extra_args: dict[str, str | None] = field(default_factory=dict)
    max_buffer_size: int | None = None
    debug_stderr: Any = sys.stderr  # Deprecated
    stderr: Callable[[str], None] | None = None
    can_use_tool: CanUseTool | None = None
    hooks: dict[HookEvent, list[HookMatcher]] | None = None
    user: str | None = None
    include_partial_messages: bool = False
    include_hook_events: bool = False
    fork_session: bool = False
    agents: dict[str, AgentDefinition] | None = None
    setting_sources: list[SettingSource] | None = None
    skills: list[str] | Literal["all"] | None = None
    sandbox: SandboxSettings | None = None
    plugins: list[SdkPluginConfig] = field(default_factory=list)
    max_thinking_tokens: int | None = None  # Deprecated: use thinking instead
    thinking: ThinkingConfig | None = None
    effort: EffortLevel | None = None
    enable_file_checkpointing: bool = False
    session_store: SessionStore | None = None
    session_store_flush: SessionStoreFlushMode = "batched"
    load_timeout_ms: int = 60_000
    task_budget: TaskBudget | None = None
```

| Property                      | Type                                                                                      | Default                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:------------------------------|:------------------------------------------------------------------------------------------|:-----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `tools`                       | `list[str] | ToolsPreset | None`                                                          | `None`                             | Tools configuration. Use `{"type": "preset", "preset": "claude_code"}` for Claude Code’s default tools                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `allowed_tools`               | `list[str]`                                                                               | `[]`                               | Tools to auto-approve without prompting. This does not restrict Claude to only these tools; unlisted tools fall through to `permission_mode` and `can_use_tool`. Use `disallowed_tools` to block tools. See [Permissions](/docs/en/agent-sdk/permissions#allow-and-deny-rules)                                                                                                                                                                                                                                                                                                                                      |
| `system_prompt`               | `str | SystemPromptPreset | SystemPromptFile | None`                                      | `None`                             | System prompt configuration. Pass a string for a custom prompt, `{"type": "preset", "preset": "claude_code"}` for Claude Code’s system prompt with optional `"append"`, or `{"type": "file", "path": "..."}` to load a large prompt from disk. See [`SystemPromptPreset`](#systempromptpreset) and [`SystemPromptFile`](#systempromptfile)                                                                                                                                                                                                                                                                          |
| `mcp_servers`                 | `dict[str, McpServerConfig] | str | Path`                                                 | `{}`                               | MCP server configurations or path to config file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `strict_mcp_config`           | `bool`                                                                                    | `False`                            | When `True`, use only the servers passed in `mcp_servers` and ignore project `.mcp.json`, user settings, plugin-provided MCP servers, and [claude.ai connectors](/docs/en/mcp#use-mcp-servers-from-claude-ai). Maps to the CLI `--strict-mcp-config` flag                                                                                                                                                                                                                                                                                                                                                           |
| `permission_mode`             | `PermissionMode | None`                                                                   | `None`                             | Permission mode for tool usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `continue_conversation`       | `bool`                                                                                    | `False`                            | Continue the most recent conversation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `resume`                      | `str | None`                                                                              | `None`                             | Session ID to resume                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `session_id`                  | `str | None`                                                                              | `None`                             | Use a specific session ID instead of an auto-generated one. Must be a valid UUID. Can’t be combined with `continue_conversation` or `resume` unless `fork_session` is also set                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `max_turns`                   | `int | None`                                                                              | `None`                             | Maximum agentic turns (tool-use round trips)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `max_budget_usd`              | `float | None`                                                                            | `None`                             | Stop the query when the client-side cost estimate reaches this USD value. Compared against the same estimate as `total_cost_usd`; see [Track cost and usage](/docs/en/agent-sdk/cost-tracking) for accuracy caveats                                                                                                                                                                                                                                                                                                                                                                                                 |
| `disallowed_tools`            | `list[str]`                                                                               | `[]`                               | Tools to deny. A bare name such as `"Bash"` removes the tool from Claude’s context. A scoped rule such as `"Bash(rm *)"` leaves the tool available and denies matching calls in every permission mode, including `bypassPermissions`. See [Permissions](/docs/en/agent-sdk/permissions#allow-and-deny-rules)                                                                                                                                                                                                                                                                                                        |
| `enable_file_checkpointing`   | `bool`                                                                                    | `False`                            | Enable file change tracking for rewinding. See [File checkpointing](/docs/en/agent-sdk/file-checkpointing)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `model`                       | `str | None`                                                                              | `None`                             | Claude model alias or full model name. See [accepted values and provider-specific IDs](/docs/en/model-config#available-models)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `fallback_model`              | `str | None`                                                                              | `None`                             | Fallback model to use if the primary model fails                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `betas`                       | `list[SdkBeta]`                                                                           | `[]`                               | Beta features to enable. See [`SdkBeta`](#sdkbeta) for available options                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `output_format`               | `dict[str, Any] | None`                                                                   | `None`                             | Output format for structured responses (e.g., `{"type": "json_schema", "schema": {...}}`). See [Structured outputs](/docs/en/agent-sdk/structured-outputs) for details                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `permission_prompt_tool_name` | `str | None`                                                                              | `None`                             | MCP tool name for permission prompts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `cwd`                         | `str | Path | None`                                                                       | `None`                             | Current working directory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `cli_path`                    | `str | Path | None`                                                                       | `None`                             | Custom path to the Claude Code CLI executable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `settings`                    | `str | None`                                                                              | `None`                             | Path to settings file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `add_dirs`                    | `list[str | Path]`                                                                        | `[]`                               | Additional directories Claude can access                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `env`                         | `dict[str, str]`                                                                          | `{}`                               | Environment variables merged on top of the inherited process environment. See [Environment variables](/docs/en/env-vars) for variables the underlying CLI reads, and [Handle slow or stalled API responses](#handle-slow-or-stalled-api-responses) for timeout-related variables                                                                                                                                                                                                                                                                                                                                    |
| `extra_args`                  | `dict[str, str | None]`                                                                   | `{}`                               | Additional CLI arguments to pass directly to the CLI                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `max_buffer_size`             | `int | None`                                                                              | `None`                             | Maximum bytes when buffering CLI stdout                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `debug_stderr`                | `Any`                                                                                     | `sys.stderr`                       | *Deprecated* - File-like object for debug output. Use `stderr` callback instead                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `stderr`                      | `Callable[[str], None] | None`                                                            | `None`                             | Callback function for stderr output from CLI                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `can_use_tool`                | [`CanUseTool`](#canusetool) ` | None`                                                     | `None`                             | Tool permission callback, invoked only when the [permission flow](/docs/en/agent-sdk/permissions#how-permissions-are-evaluated) falls through to a prompt. Not invoked for calls auto-approved by `allowed_tools`, allow rules, or `permission_mode`. `AskUserQuestion`, connector tools [your organization set to `ask`](/docs/en/mcp#organization-controls-on-connector-tools), and MCP tools marked [`requiresUserInteraction`](/docs/en/mcp#require-approval-for-a-specific-tool) reach it even if you’ve allowed them; in `dontAsk` mode these are denied instead. See [`CanUseTool`](#canusetool) for details |
| `hooks`                       | `dict[HookEvent, list[HookMatcher]] | None`                                               | `None`                             | Hook configurations for intercepting events                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `user`                        | `str | None`                                                                              | `None`                             | User identifier                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `include_partial_messages`    | `bool`                                                                                    | `False`                            | Include partial message streaming events. When enabled, [`StreamEvent`](#streamevent) messages are yielded                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `include_hook_events`         | `bool`                                                                                    | `False`                            | Include hook lifecycle events in the message stream as `HookEventMessage` objects                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `fork_session`                | `bool`                                                                                    | `False`                            | When resuming with `resume`, fork to a new session ID instead of continuing the original session                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `agents`                      | `dict[str, AgentDefinition] | None`                                                       | `None`                             | Programmatically defined subagents                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `plugins`                     | `list[SdkPluginConfig]`                                                                   | `[]`                               | Load custom plugins from local paths. See [Plugins](/docs/en/agent-sdk/plugins) for details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `sandbox`                     | [`SandboxSettings`](#sandboxsettings) ` | None`                                           | `None`                             | Configure sandbox behavior programmatically. See [Sandbox settings](#sandboxsettings) for details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `setting_sources`             | `list[SettingSource] | None`                                                              | `None` (CLI defaults: all sources) | Control which filesystem settings to load. Pass `[]` to disable user, project, and local settings. Endpoint-managed policy loads regardless; server-managed settings are fetched when the session authenticates with an organization credential on an [eligible configuration](/docs/en/server-managed-settings#platform-availability). See [Use Claude Code features](/docs/en/agent-sdk/claude-code-features#what-settingsources-does-not-control)                                                                                                                                                                |
| `skills`                      | `list[str] | Literal["all"] | None`                                                       | `None`                             | Skills available to the session. Pass `"all"` to enable every discovered skill, or a list of skill names. When set, the SDK adds the Skill tool to `allowed_tools` automatically. If you also pass `tools`, include `"Skill"` in that list. See [Skills](/docs/en/agent-sdk/skills)                                                                                                                                                                                                                                                                                                                                 |
| `max_thinking_tokens`         | `int | None`                                                                              | `None`                             | *Deprecated* - Maximum tokens for thinking blocks. Use `thinking` instead                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `thinking`                    | [`ThinkingConfig`](#thinkingconfig) ` | None`                                             | `None`                             | Controls extended thinking behavior. Takes precedence over `max_thinking_tokens`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `effort`                      | [`EffortLevel`](#effortlevel) ` | None`                                                   | `None`                             | Effort level for thinking depth. See [adjust the effort level](/docs/en/model-config#adjust-effort-level)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `session_store`               | [`SessionStore`](/docs/en/agent-sdk/session-storage#the-sessionstore-interface) ` | None` | `None`                             | Mirror session transcripts to an external backend so any host can resume them. See [Persist sessions to external storage](/docs/en/agent-sdk/session-storage)                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `session_store_flush`         | `Literal["batched", "eager"]`                                                             | `"batched"`                        | When to flush mirrored transcript entries to `session_store`. `"batched"` flushes once per turn or when the buffer fills; `"eager"` triggers a background flush after every frame. Ignored when `session_store` is `None`                                                                                                                                                                                                                                                                                                                                                                                           |
| `load_timeout_ms`             | `int`                                                                                     | `60000`                            | Per-call timeout for `session_store.load()` and `list_subkeys()` during resume materialization, in milliseconds                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `task_budget`                 | `TaskBudget | None`                                                                       | `None`                             | API-side token budget. Sent as `output_config.task_budget` with the `task-budgets-2026-03-13` beta header. Pass `{"total": <int>}`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |


[​](#handle-slow-or-stalled-api-responses)

Handle slow or stalled API responses

The CLI subprocess reads several environment variables that control API timeouts and stall detection. Pass them through `ClaudeAgentOptions.env`:

```python
from claude_agent_sdk import ClaudeAgentOptions

options = ClaudeAgentOptions(
    env={
        "API_TIMEOUT_MS": "120000",
        "CLAUDE_CODE_MAX_RETRIES": "2",
        "CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS": "120000",
    },
)
```

- `API_TIMEOUT_MS`: per-request timeout on the Anthropic client, in milliseconds. Default `600000`. Applies to the main loop and all subagents.
- `CLAUDE_CODE_MAX_RETRIES`: maximum API retries. Default `10`, capped at `15`. Each retry gets its own `API_TIMEOUT_MS` window, so worst-case wall time is roughly `API_TIMEOUT_MS × (CLAUDE_CODE_MAX_RETRIES + 1)` plus backoff. For unattended runs that need to wait through longer outages, set `CLAUDE_CODE_RETRY_WATCHDOG=1`: it retries capacity errors indefinitely, and as of Claude Code v2.1.199 raises the default for other transient errors to `300` and removes the cap on this variable.
- `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS`: stall watchdog for subagents launched with `run_in_background`. Default `600000`. Resets on each stream event; on stall it aborts the subagent, marks the task failed, and surfaces the error to the parent with any partial result. Does not apply to synchronous subagents.
- `CLAUDE_ENABLE_STREAM_WATCHDOG` with `CLAUDE_STREAM_IDLE_TIMEOUT_MS`: aborts the request when headers have arrived but the response body stops streaming. The watchdog is on by default for all providers; set `CLAUDE_ENABLE_STREAM_WATCHDOG=0` to disable it. `CLAUDE_STREAM_IDLE_TIMEOUT_MS` defaults to `300000` and is clamped to that minimum. After the abort, Claude Code retries the request at most once, and only before Claude has started a block of text or a tool call in the response; once Claude has completed a block of text or a tool call, Claude Code keeps the completed output, appends an [incomplete-response notice](/docs/en/errors#the-response-above-may-be-incomplete) instead of retrying, and still runs any completed tool call.


[​](#outputformat)

`OutputFormat`

Configuration for structured output validation. Pass this as a `dict` to the `output_format` field on `ClaudeAgentOptions`:

```python
# Expected dict shape for output_format
{
    "type": "json_schema",
    "schema": {...},  # Your JSON Schema definition
}
```

| Field    | Required | Description                                        |
|:---------|:---------|:---------------------------------------------------|
| `type`   | Yes      | Must be `"json_schema"` for JSON Schema validation |
| `schema` | Yes      | JSON Schema definition for output validation       |


[​](#systempromptpreset)

`SystemPromptPreset`

Configuration for using Claude Code’s preset system prompt with optional additions.

```python
class SystemPromptPreset(TypedDict):
    type: Literal["preset"]
    preset: Literal["claude_code"]
    append: NotRequired[str]
    exclude_dynamic_sections: NotRequired[bool]
```

| Field                      | Required | Description                                                                                                                                                                                                                                                                                                                       |
|:---------------------------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`                     | Yes      | Must be `"preset"` to use a preset system prompt                                                                                                                                                                                                                                                                                  |
| `preset`                   | Yes      | Must be `"claude_code"` to use Claude Code’s system prompt                                                                                                                                                                                                                                                                        |
| `append`                   | No       | Additional instructions to append to the preset system prompt                                                                                                                                                                                                                                                                     |
| `exclude_dynamic_sections` | No       | Move per-session context such as working directory, the git-repo flag, and auto-memory paths from the system prompt into the first user message. Improves prompt-cache reuse across users and machines. See [Modify system prompts](/docs/en/agent-sdk/modifying-system-prompts#improve-prompt-caching-across-users-and-machines) |


[​](#systempromptfile)

`SystemPromptFile`

Configuration for loading a custom system prompt from a file instead of passing it as a string. The SDK maps this to the CLI [`--system-prompt-file`](/docs/en/cli-reference#system-prompt-flags) flag. Use the file form when the prompt is large: the SDK passes a string `system_prompt` on the CLI subprocess argv, which is subject to OS command-line length limits before the SDK sends any API request. On Linux a single argument longer than roughly 128 KB fails at process spawn with `Argument list too long`. On Windows the whole command line is capped at roughly 32 KB, so the string form fails at a lower threshold.

```python
class SystemPromptFile(TypedDict):
    type: Literal["file"]
    path: str
```

| Field  | Required | Description                                   |
|:-------|:---------|:----------------------------------------------|
| `type` | Yes      | Must be `"file"` to load the prompt from disk |
| `path` | Yes      | Path to a file containing the system prompt   |


[​](#settingsource)

`SettingSource`

Controls which filesystem-based configuration sources the SDK loads settings from.

```python
SettingSource = Literal["user", "project", "local"]
```

| Value       | Description                                                               | Location                      |
|:------------|:--------------------------------------------------------------------------|:------------------------------|
| `"user"`    | Global user settings                                                      | `~/.claude/settings.json`     |
| `"project"` | Shared project settings (version controlled)                              | `.claude/settings.json`       |
| `"local"`   | Local project settings, gitignored when Claude Code saves a setting to it | `.claude/settings.local.json` |


[​](#default-behavior)

Default behavior

When `setting_sources` is omitted or `None`, `query()` loads the same filesystem settings as the Claude Code CLI: user, project, and local. Endpoint-managed policy is loaded in all cases; server-managed settings are fetched when the session authenticates with an organization credential on an [eligible configuration](/docs/en/server-managed-settings#platform-availability). See [What settingSources does not control](/docs/en/agent-sdk/claude-code-features#what-settingsources-does-not-control) for inputs that are read regardless of this option, and how to disable them.


[​](#why-use-setting_sources)

Why use setting_sources

**Disable filesystem settings:**

```python
# Do not load user, project, or local settings from disk
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions


async def main():
    async for message in query(
        prompt="Analyze this code",
        options=ClaudeAgentOptions(
            setting_sources=[]
        ),
    ):
        print(message)


asyncio.run(main())
```

In Python SDK 0.1.59 and earlier, an empty list was treated the same as omitting the option, so `setting_sources=[]` did not disable filesystem settings. Upgrade to a newer release if you need an empty list to take effect. The TypeScript SDK is not affected.

**Load all filesystem settings explicitly:**

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions


async def main():
    async for message in query(
        prompt="Analyze this code",
        options=ClaudeAgentOptions(
            setting_sources=["user", "project", "local"]
        ),
    ):
        print(message)


asyncio.run(main())
```

**Load only specific setting sources:**

```python
# Load only project settings, ignore user and local
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions


async def main():
    async for message in query(
        prompt="Run CI checks",
        options=ClaudeAgentOptions(
            setting_sources=["project"]  # Only .claude/settings.json
        ),
    ):
        print(message)


asyncio.run(main())
```

**Testing and CI environments:**

```python
# Ensure consistent behavior in CI by excluding local settings
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions


async def main():
    async for message in query(
        prompt="Run tests",
        options=ClaudeAgentOptions(
            setting_sources=["project"],  # Only team-shared settings
            permission_mode="bypassPermissions",
        ),
    ):
        print(message)


asyncio.run(main())
```

**SDK-only applications:**

```python
# Define everything programmatically.
# Pass [] to opt out of filesystem setting sources.
import asyncio
from claude_agent_sdk import AgentDefinition, ClaudeAgentOptions, query


async def main():
    async for message in query(
        prompt="Review this PR",
        options=ClaudeAgentOptions(
            setting_sources=[],
            agents={
                "code-reviewer": AgentDefinition(
                    description="Reviews code changes",
                    prompt="You are a code reviewer. Report issues in the diff.",
                ),
            },
            allowed_tools=["Read", "Grep", "Glob"],
        ),
    ):
        print(message)


asyncio.run(main())
```

**Loading CLAUDE.md project instructions:**

```python
# Load project settings to include CLAUDE.md files
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions


async def main():
    async for message in query(
        prompt="Add a new feature following project conventions",
        options=ClaudeAgentOptions(
            system_prompt={
                "type": "preset",
                "preset": "claude_code",  # Use Claude Code's system prompt
            },
            setting_sources=["project"],  # Loads CLAUDE.md from project
            allowed_tools=["Read", "Write", "Edit"],
        ),
    ):
        print(message)


asyncio.run(main())
```


[​](#settings-precedence)

Settings precedence

When multiple sources are loaded, settings are merged with this precedence (highest to lowest):

1.  Local settings (`.claude/settings.local.json`)
2.  Project settings (`.claude/settings.json`)
3.  User settings (`~/.claude/settings.json`)

Programmatic options such as `agents` and `allowed_tools` override user, project, and local filesystem settings. Managed policy settings take precedence over programmatic options.


[​](#agentdefinition)

`AgentDefinition`

Configuration for a subagent defined programmatically.

```python
@dataclass
class AgentDefinition:
    description: str
    prompt: str
    tools: list[str] | None = None
    disallowedTools: list[str] | None = None
    model: str | None = None
    skills: list[str] | None = None
    memory: Literal["user", "project", "local"] | None = None
    mcpServers: list[str | dict[str, Any]] | None = None
    initialPrompt: str | None = None
    maxTurns: int | None = None
    background: bool | None = None
    effort: EffortLevel | int | None = None
    permissionMode: PermissionMode | None = None
```

| Field             | Required | Description                                                                                                                                                                                                                      |
|:------------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `description`     | Yes      | Natural language description of when to use this agent                                                                                                                                                                           |
| `prompt`          | Yes      | The agent’s system prompt                                                                                                                                                                                                        |
| `tools`           | No       | Array of allowed tool names. If omitted, inherits every [tool available to subagents](/docs/en/sub-agents#available-tools)                                                                                                       |
| `disallowedTools` | No       | Array of tool names to remove from the agent’s tool set. MCP server-level patterns are also accepted: `mcp__server` or `mcp__server__*` removes every tool from that server, and `mcp__*` removes every MCP tool from any server |
| `model`           | No       | Model override for this agent. Accepts an alias such as `"sonnet"`, `"opus"`, `"haiku"`, or `"inherit"`, or a full model ID. If omitted, uses the main model                                                                     |
| `skills`          | No       | List of skill names to preload into the agent’s context at startup. Unlisted skills remain invocable through the Skill tool                                                                                                      |
| `memory`          | No       | Memory source for this agent: `"user"`, `"project"`, or `"local"`                                                                                                                                                                |
| `mcpServers`      | No       | MCP servers available to this agent. Each entry is a server name or an inline `{name: config}` dict                                                                                                                              |
| `initialPrompt`   | No       | Auto-submitted as the first user turn when this agent runs as the main thread agent                                                                                                                                              |
| `maxTurns`        | No       | Maximum number of agentic turns before the agent stops                                                                                                                                                                           |
| `background`      | No       | Run this agent as a non-blocking background task when invoked                                                                                                                                                                    |
| `effort`          | No       | Reasoning effort level for this agent. Accepts a named level or an integer. See [`EffortLevel`](#effortlevel)                                                                                                                    |
| `permissionMode`  | No       | Permission mode for tool execution within this agent. See [`PermissionMode`](#permissionmode)                                                                                                                                    |

`AgentDefinition` field names use camelCase, such as `disallowedTools`, `permissionMode`, and `maxTurns`. These names map directly to the wire format shared with the TypeScript SDK. This differs from `ClaudeAgentOptions`, which uses Python snake_case for the equivalent top-level fields such as `disallowed_tools` and `permission_mode`. Because `AgentDefinition` is a dataclass, passing a snake_case keyword raises a `TypeError` at construction time.


[​](#permissionmode)

`PermissionMode`

Permission modes for controlling tool execution.

```python
PermissionMode = Literal[
    "default",  # Standard permission behavior
    "acceptEdits",  # Auto-accept file edits
    "plan",  # Planning mode - explore without editing
    "dontAsk",  # Deny anything not pre-approved instead of prompting
    "bypassPermissions",  # Bypass permission checks; explicit ask rules still prompt (use with caution)
    "auto",  # Model classifier approves or denies permission prompts
]
```


[​](#effortlevel)

`EffortLevel`

Effort levels for guiding thinking depth.

```python
EffortLevel = Literal[
    "low",  # Minimal thinking, fastest responses
    "medium",  # Moderate thinking
    "high",  # Deep reasoning
    "xhigh",  # Extended reasoning; falls back to "high" on models that don't support it
    "max",  # Maximum effort
]
```


[​](#canusetool)

`CanUseTool`

Type alias for tool permission callback functions.

```python
CanUseTool = Callable[
    [str, dict[str, Any], ToolPermissionContext], Awaitable[PermissionResult]
]
```

The callback receives:

- `tool_name`: Name of the tool being called
- `input_data`: The tool’s input parameters
- `context`: A `ToolPermissionContext` with additional information

Returns a `PermissionResult` (either `PermissionResultAllow` or `PermissionResultDeny`). The callback is the SDK replacement for the interactive permission prompt: it’s invoked only when the [permission evaluation flow](/docs/en/agent-sdk/permissions#how-permissions-are-evaluated) resolves to a prompt. Tool calls already approved by an `allowed_tools` entry, a settings allow rule, or the permission mode, such as `acceptEdits` or `bypassPermissions`, never invoke it. To gate every tool call, use a [`PreToolUse` hook](/docs/en/agent-sdk/hooks) instead. `AskUserQuestion`, MCP tools marked [`requiresUserInteraction`](/docs/en/mcp#require-approval-for-a-specific-tool), and connector tools [your organization set to `ask`](/docs/en/mcp#organization-controls-on-connector-tools) reach the callback even when an allow rule matches. In `dontAsk` mode these calls are denied instead, without invoking the callback.


[​](#toolpermissioncontext)

`ToolPermissionContext`

Context information passed to tool permission callbacks.

```python
@dataclass
class ToolPermissionContext:
    signal: Any | None = None  # Future: abort signal support
    suggestions: list[PermissionUpdate] = field(default_factory=list)
    tool_use_id: str | None = None
    agent_id: str | None = None
    blocked_path: str | None = None
    decision_reason: str | None = None
    title: str | None = None
    display_name: str | None = None
    description: str | None = None
```

| Field             | Type                     | Description                                                                                                                                                                                                                                 |
|:------------------|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `signal`          | `Any | None`             | Reserved for future abort signal support                                                                                                                                                                                                    |
| `suggestions`     | `list[PermissionUpdate]` | Permission update suggestions from the CLI. Bash prompts include a suggestion with the `localSettings` destination, so returning it in `updated_permissions` writes the rule to `.claude/settings.local.json` and persists across sessions. |
| `tool_use_id`     | `str | None`             | Identifier of the specific tool call this prompt is for. Always populated when delivered to `can_use_tool`                                                                                                                                  |
| `agent_id`        | `str | None`             | Sub-agent ID when the call originates from a subagent; `None` for the main agent                                                                                                                                                            |
| `blocked_path`    | `str | None`             | File path that triggered the permission request, when applicable. For example, when a Bash command tries to access a path outside allowed directories                                                                                       |
| `decision_reason` | `str | None`             | Reason this permission request was triggered. Forwarded from a PreToolUse hook’s `permissionDecisionReason` when the hook returned `"ask"`                                                                                                  |
| `title`           | `str | None`             | Full permission prompt sentence, such as `Claude wants to read foo.txt`. Use as the primary prompt text when present                                                                                                                        |
| `display_name`    | `str | None`             | Short noun phrase for the tool action, such as `Read file`, suitable for button labels                                                                                                                                                      |
| `description`     | `str | None`             | Human-readable subtitle for the permission UI                                                                                                                                                                                               |


[​](#permissionresult)

`PermissionResult`

Union type for permission callback results.

```python
PermissionResult = PermissionResultAllow | PermissionResultDeny
```


[​](#permissionresultallow)

`PermissionResultAllow`

Result indicating the tool call should be allowed.

```python
@dataclass
class PermissionResultAllow:
    behavior: Literal["allow"] = "allow"
    updated_input: dict[str, Any] | None = None
    updated_permissions: list[PermissionUpdate] | None = None
```

| Field                 | Type                            | Default   | Description                               |
|:----------------------|:--------------------------------|:----------|:------------------------------------------|
| `behavior`            | `Literal["allow"]`              | `"allow"` | Must be “allow”                           |
| `updated_input`       | `dict[str, Any] | None`         | `None`    | Modified input to use instead of original |
| `updated_permissions` | `list[PermissionUpdate] | None` | `None`    | Permission updates to apply               |


[​](#permissionresultdeny)

`PermissionResultDeny`

Result indicating the tool call should be denied.

```python
@dataclass
class PermissionResultDeny:
    behavior: Literal["deny"] = "deny"
    message: str = ""
    interrupt: bool = False
```

| Field       | Type              | Default  | Description                                |
|:------------|:------------------|:---------|:-------------------------------------------|
| `behavior`  | `Literal["deny"]` | `"deny"` | Must be “deny”                             |
| `message`   | `str`             | `""`     | Message explaining why the tool was denied |
| `interrupt` | `bool`            | `False`  | Whether to interrupt the current execution |


[​](#permissionupdate)

`PermissionUpdate`

Configuration for updating permissions programmatically.

```python
@dataclass
class PermissionUpdate:
    type: Literal[
        "addRules",
        "replaceRules",
        "removeRules",
        "setMode",
        "addDirectories",
        "removeDirectories",
    ]
    rules: list[PermissionRuleValue] | None = None
    behavior: Literal["allow", "deny", "ask"] | None = None
    mode: PermissionMode | None = None
    directories: list[str] | None = None
    destination: (
        Literal["userSettings", "projectSettings", "localSettings", "session"] | None
    ) = None
```

| Field         | Type                                     | Description                                     |
|:--------------|:-----------------------------------------|:------------------------------------------------|
| `type`        | `Literal[...]`                           | The type of permission update operation         |
| `rules`       | `list[PermissionRuleValue] | None`       | Rules for add/replace/remove operations         |
| `behavior`    | `Literal["allow", "deny", "ask"] | None` | Behavior for rule-based operations              |
| `mode`        | `PermissionMode | None`                  | Mode for setMode operation                      |
| `directories` | `list[str] | None`                       | Directories for add/remove directory operations |
| `destination` | `Literal[...] | None`                    | Where to apply the permission update            |


[​](#permissionrulevalue)

`PermissionRuleValue`

A rule to add, replace, or remove in a permission update.

```python
@dataclass
class PermissionRuleValue:
    tool_name: str
    rule_content: str | None = None
```


[​](#toolspreset)

`ToolsPreset`

Preset tools configuration for using Claude Code’s default tool set.

```python
class ToolsPreset(TypedDict):
    type: Literal["preset"]
    preset: Literal["claude_code"]
```


[​](#thinkingconfig)

`ThinkingConfig`

Controls extended thinking behavior. A union of three configurations:

```python
ThinkingDisplay = Literal["summarized", "omitted"]


class ThinkingConfigAdaptive(TypedDict):
    type: Literal["adaptive"]
    display: NotRequired[ThinkingDisplay]


class ThinkingConfigEnabled(TypedDict):
    type: Literal["enabled"]
    budget_tokens: int
    display: NotRequired[ThinkingDisplay]


class ThinkingConfigDisabled(TypedDict):
    type: Literal["disabled"]


ThinkingConfig = ThinkingConfigAdaptive | ThinkingConfigEnabled | ThinkingConfigDisabled
```

| Variant    | Fields                             | Description                                  |
|:-----------|:-----------------------------------|:---------------------------------------------|
| `adaptive` | `type`, `display`                  | Claude adaptively decides when to think      |
| `enabled`  | `type`, `budget_tokens`, `display` | Enable thinking with a specific token budget |
| `disabled` | `type`                             | Disable thinking                             |

The optional `display` field controls whether thinking text is returned `"summarized"` or `"omitted"`. On Claude Opus 4.7 and later, the API default is `"omitted"`, so set `"summarized"` to receive thinking content in [`ThinkingBlock`](#thinkingblock) outputs. Claude Code doesn’t send `display` to Amazon Bedrock or Google Cloud’s Agent Platform, so on those providers Opus 4.7 and later return empty `ThinkingBlock` outputs even when you set `display` to `"summarized"`. Because these are `TypedDict` classes, they’re plain dicts at runtime. Either construct them as dict literals or call the class like a constructor; both produce a `dict`. Access fields with `config["budget_tokens"]`, not `config.budget_tokens`:

```python
from claude_agent_sdk import ClaudeAgentOptions, ThinkingConfigEnabled

# Option 1: dict literal (recommended, no import needed)
options = ClaudeAgentOptions(thinking={"type": "enabled", "budget_tokens": 20000})

# Option 2: constructor-style (returns a plain dict)
config = ThinkingConfigEnabled(type="enabled", budget_tokens=20000)
print(config["budget_tokens"])  # 20000
# config.budget_tokens would raise AttributeError
```


[​](#taskbudget)

`TaskBudget`

API-side task budget in tokens, used with the `task_budget` field in `ClaudeAgentOptions`.

```python
class TaskBudget(TypedDict):
    total: int
```

| Field   | Type  | Description                     |
|:--------|:------|:--------------------------------|
| `total` | `int` | Total token budget for the task |

Because this is a `TypedDict`, pass it as a plain dict, such as `ClaudeAgentOptions(task_budget={"total": 50000})`.


[​](#sdkbeta)

`SdkBeta`

Literal type for SDK beta features.

```python
SdkBeta = Literal["context-1m-2025-08-07"]
```

Use with the `betas` field in `ClaudeAgentOptions` to enable beta features.

The `context-1m-2025-08-07` beta is retired as of April 30, 2026. Passing this header with Claude Sonnet 4.5 or Sonnet 4 has no effect, and requests that exceed the standard 200k-token context window return an error. To use a 1M-token context window, migrate to [Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.6, Claude Opus 4.7, or Claude Opus 4.8](https://platform.claude.com/docs/en/about-claude/models/overview), which include 1M context at standard pricing with no beta header required.


[​](#mcpsdkserverconfig)

`McpSdkServerConfig`

Configuration for SDK MCP servers created with `create_sdk_mcp_server()`.

```python
class McpSdkServerConfig(TypedDict):
    type: Literal["sdk"]
    name: str
    instance: Any  # MCP Server instance
```


[​](#mcpserverconfig)

`McpServerConfig`

Union type for MCP server configurations.

```python
McpServerConfig = (
    McpStdioServerConfig | McpSSEServerConfig | McpHttpServerConfig | McpSdkServerConfig
)
```


[​](#mcpstdioserverconfig)

`McpStdioServerConfig`

```python
class McpStdioServerConfig(TypedDict):
    type: NotRequired[Literal["stdio"]]  # Optional for backwards compatibility
    command: str
    args: NotRequired[list[str]]
    env: NotRequired[dict[str, str]]
```


[​](#mcpsseserverconfig)

`McpSSEServerConfig`

```python
class McpSSEServerConfig(TypedDict):
    type: Literal["sse"]
    url: str
    headers: NotRequired[dict[str, str]]
```


[​](#mcphttpserverconfig)

`McpHttpServerConfig`

```python
class McpHttpServerConfig(TypedDict):
    type: Literal["http"]
    url: str
    headers: NotRequired[dict[str, str]]
```


[​](#mcpserverstatusconfig)

`McpServerStatusConfig`

The configuration of an MCP server as reported by [`get_mcp_status()`](#methods). This is the union of all [`McpServerConfig`](#mcpserverconfig) transport variants plus an output-only `claudeai-proxy` variant for servers proxied through claude.ai.

```python
McpServerStatusConfig = (
    McpStdioServerConfig
    | McpSSEServerConfig
    | McpHttpServerConfig
    | McpSdkServerConfigStatus
    | McpClaudeAIProxyServerConfig
)
```

`McpSdkServerConfigStatus` is the serializable form of [`McpSdkServerConfig`](#mcpsdkserverconfig) with only `type` (`"sdk"`) and `name` (`str`) fields; the in-process `instance` is omitted. `McpClaudeAIProxyServerConfig` has `type` (`"claudeai-proxy"`), `url` (`str`), and `id` (`str`) fields.


[​](#mcpstatusresponse)

`McpStatusResponse`

Response from [`ClaudeSDKClient.get_mcp_status()`](#methods). Wraps the list of server statuses under the `mcpServers` key.

```python
class McpStatusResponse(TypedDict):
    mcpServers: list[McpServerStatus]
```


[​](#mcpserverstatus)

`McpServerStatus`

Status of a connected MCP server, contained in [`McpStatusResponse`](#mcpstatusresponse).

```python
class McpServerStatus(TypedDict):
    name: str
    status: McpServerConnectionStatus  # "connected" | "failed" | "needs-auth" | "pending" | "disabled"
    serverInfo: NotRequired[McpServerInfo]
    error: NotRequired[str]
    config: NotRequired[McpServerStatusConfig]
    scope: NotRequired[str]
    tools: NotRequired[list[McpToolInfo]]
```

| Field        | Type                                                         | Description                                                                                                                                                                   |
|:-------------|:-------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`       | `str`                                                        | Server name                                                                                                                                                                   |
| `status`     | `str`                                                        | One of `"connected"`, `"failed"`, `"needs-auth"`, `"pending"`, or `"disabled"`                                                                                                |
| `serverInfo` | `dict` (optional)                                            | Server name and version (`{"name": str, "version": str}`)                                                                                                                     |
| `error`      | `str` (optional)                                             | Error message if the server failed to connect                                                                                                                                 |
| `config`     | [`McpServerStatusConfig`](#mcpserverstatusconfig) (optional) | Server configuration. Same shape as [`McpServerConfig`](#mcpserverconfig) (stdio, SSE, HTTP, or SDK), plus a `claudeai-proxy` variant for servers connected through claude.ai |
| `scope`      | `str` (optional)                                             | Configuration scope                                                                                                                                                           |
| `tools`      | `list` (optional)                                            | Tools provided by this server, each with `name`, `description`, and `annotations` fields                                                                                      |


[​](#sdkpluginconfig)

`SdkPluginConfig`

Configuration for loading plugins in the SDK.

```python
class SdkPluginConfig(TypedDict):
    type: Literal["local"]
    path: str
```

| Field  | Type               | Description                                                |
|:-------|:-------------------|:-----------------------------------------------------------|
| `type` | `Literal["local"]` | Must be `"local"` (only local plugins currently supported) |
| `path` | `str`              | Absolute or relative path to the plugin directory          |

**Example:**

```python
plugins = [
    {"type": "local", "path": "./my-plugin"},
    {"type": "local", "path": "/absolute/path/to/plugin"},
]
```

For complete information on creating and using plugins, see [Plugins](/docs/en/agent-sdk/plugins).


[​](#message-types)

Message Types


[​](#message)

`Message`

Union type of all possible messages.

```python
Message = (
    UserMessage
    | AssistantMessage
    | SystemMessage
    | ResultMessage
    | StreamEvent
    | RateLimitEvent
)
```


[​](#usermessage)

`UserMessage`

User input message.

```python
@dataclass
class UserMessage:
    content: str | list[ContentBlock]
    uuid: str | None = None
    parent_tool_use_id: str | None = None
    tool_use_result: dict[str, Any] | None = None
```

| Field                | Type                       | Description                                           |
|:---------------------|:---------------------------|:------------------------------------------------------|
| `content`            | `str | list[ContentBlock]` | Message content as text or content blocks             |
| `uuid`               | `str | None`               | Unique message identifier                             |
| `parent_tool_use_id` | `str | None`               | Tool use ID if this message is a tool result response |
| `tool_use_result`    | `dict[str, Any] | None`    | Tool result data if applicable                        |


[​](#assistantmessage)

`AssistantMessage`

Assistant response message with content blocks.

```python
@dataclass
class AssistantMessage:
    content: list[ContentBlock]
    model: str
    parent_tool_use_id: str | None = None
    error: AssistantMessageError | None = None
    usage: dict[str, Any] | None = None
    message_id: str | None = None
    stop_reason: str | None = None
    session_id: str | None = None
    uuid: str | None = None
```

| Field                | Type                                                        | Description                                                                    |
|:---------------------|:------------------------------------------------------------|:-------------------------------------------------------------------------------|
| `content`            | `list[ContentBlock]`                                        | List of content blocks in the response                                         |
| `model`              | `str`                                                       | Model that generated the response                                              |
| `parent_tool_use_id` | `str | None`                                                | Tool use ID if this is a nested response                                       |
| `error`              | [`AssistantMessageError`](#assistantmessageerror) ` | None` | Error type if the response encountered an error                                |
| `usage`              | `dict[str, Any] | None`                                     | Per-message token usage (same keys as [`ResultMessage.usage`](#resultmessage)) |
| `message_id`         | `str | None`                                                | API message ID. Multiple messages from one turn share the same ID              |
| `stop_reason`        | `str | None`                                                | Stop reason from the API (e.g. `end_turn`, `tool_use`)                         |
| `session_id`         | `str | None`                                                | ID of the session this message belongs to                                      |
| `uuid`               | `str | None`                                                | Unique message identifier within the session transcript                        |


[​](#assistantmessageerror)

`AssistantMessageError`

Possible error types for assistant messages.

```python
AssistantMessageError = Literal[
    "authentication_failed",
    "billing_error",
    "rate_limit",
    "invalid_request",
    "server_error",
    "unknown",
]
```

The underlying CLI process can emit error types this Literal doesn’t list, such as `max_output_tokens`. The SDK passes the value through unmodified, so treat strings outside this list the way you treat `unknown`. The TypeScript [`SDKAssistantMessageError`](/docs/en/agent-sdk/typescript#sdkassistantmessage) type lists the full set of values the CLI can emit.


[​](#systemmessage)

`SystemMessage`

System message with metadata.

```python
@dataclass
class SystemMessage:
    subtype: str
    data: dict[str, Any]
```


[​](#resultmessage)

`ResultMessage`

Final result message with cost and usage information.

```python
@dataclass
class ResultMessage:
    subtype: str
    duration_ms: int
    duration_api_ms: int
    is_error: bool
    num_turns: int
    session_id: str
    stop_reason: str | None = None
    total_cost_usd: float | None = None
    usage: dict[str, Any] | None = None
    result: str | None = None
    structured_output: Any = None
    model_usage: dict[str, ModelUsage] | None = None
    permission_denials: list[Any] | None = None
    deferred_tool_use: DeferredToolUse | None = None
    errors: list[str] | None = None
    api_error_status: int | None = None
    uuid: str | None = None
    terminal_reason: str | None = None
```

The `subtype` field determines which other fields are populated. It is one of `"success"`, `"error_during_execution"`, `"error_max_turns"`, `"error_max_budget_usd"`, or `"error_max_structured_output_retries"`. The Python dataclass flattens all variants into one shape, so fields that don’t apply to the returned subtype are `None`. Several fields carry diagnostic detail about how the conversation ended:

- `is_error`: `True` when the conversation ended in an error state. Always `True` on the `error_*` subtypes. On `subtype="success"` it is `True` when the final model request failed, meaning the agent loop completed but the last API call returned an error.
- `api_error_status`: the HTTP status code of the terminating API error. `None` when the turn ended without one. Populated only on `subtype="success"`.
- `result`: text of the final assistant message on `subtype="success"`, or `None` on the `error_*` subtypes. When `subtype="success"` and `is_error=True`, this holds the API error string if one is available but can be empty, so check `api_error_status` and the preceding `AssistantMessage` content for detail.
- `errors`: loop-level error strings such as the max-turns message. Populated only on the `error_*` subtypes.
- `terminal_reason`: why the query loop ended, such as `"completed"`, `"max_turns"`, `"api_error"`, `"aborted_streaming"`, or `"aborted_tools"`. A value of `"aborted_streaming"` or `"aborted_tools"` means the turn was aborted before completing. Common causes are [`interrupt()`](#claudesdkclient) and a permission callback returning [`PermissionResultDeny`](#permissionresultdeny) with `interrupt=True`. `None` on CLI versions that predate the field, on results that bypassed the query loop such as local slash commands, or on synthesized error results emitted when the session fails fatally. Mirrors the TypeScript SDK’s [`SDKResultMessage.terminal_reason`](/docs/en/agent-sdk/typescript#sdkresultmessage), which lists the full set of values.

The `usage` dict contains the following keys when present:

| Key                           | Type  | Description                                                                                                                                                                                        |
|-------------------------------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `input_tokens`                | `int` | Input tokens consumed by the top-level agent loop. [Subagent tokens aren’t included](/docs/en/agent-sdk/cost-tracking#get-the-total-cost-of-a-query); use `model_usage` for whole-tree accounting. |
| `output_tokens`               | `int` | Output tokens generated by the top-level agent loop. Subagent tokens aren’t included.                                                                                                              |
| `cache_creation_input_tokens` | `int` | Tokens used to create new cache entries.                                                                                                                                                           |
| `cache_read_input_tokens`     | `int` | Tokens read from existing cache entries.                                                                                                                                                           |

The `model_usage` dict maps model names to per-model usage. Each value is a `ModelUsage` TypedDict whose keys use camelCase, because the value is passed through unmodified from the underlying CLI process. Import via `from claude_agent_sdk.types import ModelUsage`. The keys are:

| Key                        | Type    | Description                                                                                                                                                              |
|----------------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `inputTokens`              | `int`   | Input tokens for this model.                                                                                                                                             |
| `outputTokens`             | `int`   | Output tokens for this model.                                                                                                                                            |
| `cacheReadInputTokens`     | `int`   | Cache read tokens for this model.                                                                                                                                        |
| `cacheCreationInputTokens` | `int`   | Cache creation tokens for this model.                                                                                                                                    |
| `webSearchRequests`        | `int`   | Web search requests made by this model.                                                                                                                                  |
| `costUSD`                  | `float` | Estimated cost in USD for this model, computed client-side. See [Track cost and usage](/docs/en/agent-sdk/cost-tracking) for billing caveats.                            |
| `contextWindow`            | `int`   | Context window size for this model.                                                                                                                                      |
| `maxOutputTokens`          | `int`   | Maximum output token limit for this model.                                                                                                                               |
| `canonicalModel`           | `str`   | Canonical model ID used for the pricing lookup. May differ from the raw model string the entry is keyed by, such as a provider-specific ID or alias. Not always present. |
| `provider`                 | `str`   | API provider that served this model, such as `firstParty`, `bedrock`, `vertex`, `foundry`, `anthropicAws`, `mantle`, or `gateway`. Not always present.                   |


[​](#streamevent)

`StreamEvent`

Stream event for partial message updates during streaming. Only received when `include_partial_messages=True` in `ClaudeAgentOptions`. Import via `from claude_agent_sdk.types import StreamEvent`.

```python
@dataclass
class StreamEvent:
    uuid: str
    session_id: str
    event: dict[str, Any]  # The raw Claude API stream event
    parent_tool_use_id: str | None = None
```

| Field                | Type             | Description                                                                                                                                                         |
|:---------------------|:-----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `uuid`               | `str`            | Unique identifier for this event                                                                                                                                    |
| `session_id`         | `str`            | Session identifier                                                                                                                                                  |
| `event`              | `dict[str, Any]` | The raw Claude API stream event data                                                                                                                                |
| `parent_tool_use_id` | `str | None`     | Always `None`. Stream events are emitted for the main session only. For subagent attribution, use complete messages such as [`AssistantMessage`](#assistantmessage) |


[​](#ratelimitevent)

`RateLimitEvent`

Emitted when rate limit status changes (for example, from `"allowed"` to `"allowed_warning"`). Use this to warn users before they hit a hard limit, or to back off when status is `"rejected"`.

```python
@dataclass
class RateLimitEvent:
    rate_limit_info: RateLimitInfo
    uuid: str
    session_id: str
```

| Field             | Type                              | Description              |
|:------------------|:----------------------------------|:-------------------------|
| `rate_limit_info` | [`RateLimitInfo`](#ratelimitinfo) | Current rate limit state |
| `uuid`            | `str`                             | Unique event identifier  |
| `session_id`      | `str`                             | Session identifier       |


[​](#ratelimitinfo)

`RateLimitInfo`

Rate limit state carried by [`RateLimitEvent`](#ratelimitevent).

```python
RateLimitStatus = Literal["allowed", "allowed_warning", "rejected"]
RateLimitType = Literal[
    "five_hour", "seven_day", "seven_day_opus", "seven_day_sonnet", "overage"
]


@dataclass
class RateLimitInfo:
    status: RateLimitStatus
    resets_at: int | None = None
    rate_limit_type: RateLimitType | None = None
    utilization: float | None = None
    overage_status: RateLimitStatus | None = None
    overage_resets_at: int | None = None
    overage_disabled_reason: str | None = None
    raw: dict[str, Any] = field(default_factory=dict)
```

| Field                     | Type                     | Description                                                                                           |
|:--------------------------|:-------------------------|:------------------------------------------------------------------------------------------------------|
| `status`                  | `RateLimitStatus`        | Current status. `"allowed_warning"` means approaching the limit; `"rejected"` means the limit was hit |
| `resets_at`               | `int | None`             | Unix timestamp when the rate limit window resets                                                      |
| `rate_limit_type`         | `RateLimitType | None`   | Which rate limit window applies                                                                       |
| `utilization`             | `float | None`           | Fraction of the rate limit consumed (0.0 to 1.0)                                                      |
| `overage_status`          | `RateLimitStatus | None` | Status of pay-as-you-go overage usage, if applicable                                                  |
| `overage_resets_at`       | `int | None`             | Unix timestamp when the overage window resets                                                         |
| `overage_disabled_reason` | `str | None`             | Why overage is unavailable, if status is `"rejected"`                                                 |
| `raw`                     | `dict[str, Any]`         | Full raw dict from the CLI, including fields not modeled above                                        |


[​](#taskstartedmessage)

`TaskStartedMessage`

Emitted when a background task starts. A background task is anything tracked outside the main turn: a backgrounded Bash command, a [Monitor](#monitor) watch, a subagent spawned via the Agent tool, or a remote agent. The `task_type` field tells you which. This naming is unrelated to the `Task`-to-`Agent` tool rename.

```python
@dataclass
class TaskStartedMessage(SystemMessage):
    task_id: str
    description: str
    uuid: str
    session_id: str
    tool_use_id: str | None = None
    task_type: str | None = None
```

| Field         | Type         | Description                                                                                                                 |
|:--------------|:-------------|:----------------------------------------------------------------------------------------------------------------------------|
| `task_id`     | `str`        | Unique identifier for the task                                                                                              |
| `description` | `str`        | Description of the task                                                                                                     |
| `uuid`        | `str`        | Unique message identifier                                                                                                   |
| `session_id`  | `str`        | Session identifier                                                                                                          |
| `tool_use_id` | `str | None` | Associated tool use ID                                                                                                      |
| `task_type`   | `str | None` | Which kind of background task: `"local_bash"` for background Bash and Monitor watches, `"local_agent"`, or `"remote_agent"` |


[​](#taskusage)

`TaskUsage`

Token and timing data for a background task.

```python
class TaskUsage(TypedDict):
    total_tokens: int
    tool_uses: int
    duration_ms: int
```


[​](#taskprogressmessage)

`TaskProgressMessage`

Emitted periodically with progress updates for a running background task.

```python
@dataclass
class TaskProgressMessage(SystemMessage):
    task_id: str
    description: str
    usage: TaskUsage
    uuid: str
    session_id: str
    tool_use_id: str | None = None
    last_tool_name: str | None = None
```

| Field            | Type         | Description                         |
|:-----------------|:-------------|:------------------------------------|
| `task_id`        | `str`        | Unique identifier for the task      |
| `description`    | `str`        | Current status description          |
| `usage`          | `TaskUsage`  | Token usage for this task so far    |
| `uuid`           | `str`        | Unique message identifier           |
| `session_id`     | `str`        | Session identifier                  |
| `tool_use_id`    | `str | None` | Associated tool use ID              |
| `last_tool_name` | `str | None` | Name of the last tool the task used |


[​](#tasknotificationmessage)

`TaskNotificationMessage`

Emitted when a background task completes, fails, or is stopped. Background tasks include `run_in_background` Bash commands, Monitor watches, and background subagents.

```python
@dataclass
class TaskNotificationMessage(SystemMessage):
    task_id: str
    status: TaskNotificationStatus  # "completed" | "failed" | "stopped"
    output_file: str
    summary: str
    uuid: str
    session_id: str
    tool_use_id: str | None = None
    usage: TaskUsage | None = None
```

| Field         | Type                     | Description                                      |
|:--------------|:-------------------------|:-------------------------------------------------|
| `task_id`     | `str`                    | Unique identifier for the task                   |
| `status`      | `TaskNotificationStatus` | One of `"completed"`, `"failed"`, or `"stopped"` |
| `output_file` | `str`                    | Path to the task output file                     |
| `summary`     | `str`                    | Summary of the task result                       |
| `uuid`        | `str`                    | Unique message identifier                        |
| `session_id`  | `str`                    | Session identifier                               |
| `tool_use_id` | `str | None`             | Associated tool use ID                           |
| `usage`       | `TaskUsage | None`       | Final token usage for the task                   |


[​](#content-block-types)

Content Block Types


[​](#contentblock)

`ContentBlock`

Union type of all content blocks.

```python
ContentBlock = TextBlock | ThinkingBlock | ToolUseBlock | ToolResultBlock
```


[​](#textblock)

`TextBlock`

Text content block.

```python
@dataclass
class TextBlock:
    text: str
```


[​](#thinkingblock)

`ThinkingBlock`

Thinking content block (for models with thinking capability).

```python
@dataclass
class ThinkingBlock:
    thinking: str
    signature: str
```


[​](#tooluseblock)

`ToolUseBlock`

Tool use request block.

```python
@dataclass
class ToolUseBlock:
    id: str
    name: str
    input: dict[str, Any]
```


[​](#toolresultblock)

`ToolResultBlock`

Tool execution result block.

```python
@dataclass
class ToolResultBlock:
    tool_use_id: str
    content: str | list[dict[str, Any]] | None = None
    is_error: bool | None = None
```


[​](#error-types)

Error Types


[​](#claudesdkerror)

`ClaudeSDKError`

Base exception class for all SDK errors.

```python
class ClaudeSDKError(Exception):
    """Base error for Claude SDK."""
```

When a single-shot `query()` ends with an error result, for example a turn-limit error, the SDK raises a plain `Exception` after yielding the final result message, not a `ClaudeSDKError` subclass.


[​](#clinotfounderror)

`CLINotFoundError`

Raised when Claude Code CLI is not installed or not found.

```python
class CLINotFoundError(CLIConnectionError):
    def __init__(
        self, message: str = "Claude Code not found", cli_path: str | None = None
    ):
        """
        Args:
            message: Error message (default: "Claude Code not found")
            cli_path: Optional path to the CLI that was not found
        """
```


[​](#cliconnectionerror)

`CLIConnectionError`

Raised when connection to Claude Code fails.

```python
class CLIConnectionError(ClaudeSDKError):
    """Failed to connect to Claude Code."""
```


[​](#processerror)

`ProcessError`

Raised when the Claude Code process fails.

```python
class ProcessError(ClaudeSDKError):
    def __init__(
        self, message: str, exit_code: int | None = None, stderr: str | None = None
    ):
        self.exit_code = exit_code
        self.stderr = stderr
```


[​](#clijsondecodeerror)

`CLIJSONDecodeError`

Raised when JSON parsing fails.

```python
class CLIJSONDecodeError(ClaudeSDKError):
    def __init__(self, line: str, original_error: Exception):
        """
        Args:
            line: The line that failed to parse
            original_error: The original JSON decode exception
        """
        self.line = line
        self.original_error = original_error
```


[​](#hook-types)

Hook Types

For a comprehensive guide on using hooks with examples and common patterns, see the [Hooks guide](/docs/en/agent-sdk/hooks).


[​](#hookevent)

`HookEvent`

Supported hook event types.

```python
HookEvent = Literal[
    "PreToolUse",  # Called before tool execution
    "PostToolUse",  # Called after tool execution
    "PostToolUseFailure",  # Called when a tool execution fails
    "UserPromptSubmit",  # Called when user submits a prompt
    "Stop",  # Called when stopping execution
    "SubagentStop",  # Called when a subagent stops
    "PreCompact",  # Called before message compaction
    "Notification",  # Called for notification events
    "SubagentStart",  # Called when a subagent starts
    "PermissionRequest",  # Called when a permission decision is needed
]
```

The TypeScript SDK supports additional hook events not yet available in Python. See the [hook availability table](/docs/en/agent-sdk/hooks#available-hooks) for per-SDK support.


[​](#hookcallback)

`HookCallback`

Type definition for hook callback functions.

```python
HookCallback = Callable[[HookInput, str | None, HookContext], Awaitable[HookJSONOutput]]
```

Parameters:

- `input`: Strongly-typed hook input with discriminated unions based on `hook_event_name` (see [`HookInput`](#hookinput))
- `tool_use_id`: Optional tool use identifier (for tool-related hooks)
- `context`: Hook context with additional information

Returns a [`HookJSONOutput`](#hookjsonoutput) that may contain:

- `decision`: `"block"` to block the action
- `systemMessage`: warning message shown to the user
- `hookSpecificOutput`: Hook-specific output data


[​](#hookcontext)

`HookContext`

Context information passed to hook callbacks.

```python
class HookContext(TypedDict):
    signal: Any | None  # Future: abort signal support
```


[​](#hookmatcher)

`HookMatcher`

Configuration for matching hooks to specific events or tools.

```python
@dataclass
class HookMatcher:
    matcher: str | None = (
        None  # Tool name or pattern to match (e.g., "Bash", "Write|Edit")
    )
    hooks: list[HookCallback] = field(
        default_factory=list
    )  # List of callbacks to execute
    timeout: float | None = (
        None  # Timeout in seconds. When omitted, the per-event default applies:
        # 600 for most events, 30 for UserPromptSubmit
    )
```


[​](#hookinput)

`HookInput`

Union type of all hook input types. The actual type depends on the `hook_event_name` field.

```python
HookInput = (
    PreToolUseHookInput
    | PostToolUseHookInput
    | PostToolUseFailureHookInput
    | UserPromptSubmitHookInput
    | StopHookInput
    | SubagentStopHookInput
    | PreCompactHookInput
    | NotificationHookInput
    | SubagentStartHookInput
    | PermissionRequestHookInput
)
```


[​](#basehookinput)

`BaseHookInput`

Base fields present in all hook input types.

```python
class BaseHookInput(TypedDict):
    session_id: str
    transcript_path: str
    cwd: str
    permission_mode: NotRequired[str]
```

| Field             | Type             | Description                         |
|:------------------|:-----------------|:------------------------------------|
| `session_id`      | `str`            | Current session identifier          |
| `transcript_path` | `str`            | Path to the session transcript file |
| `cwd`             | `str`            | Current working directory           |
| `permission_mode` | `str` (optional) | Current permission mode             |


[​](#pretoolusehookinput)

`PreToolUseHookInput`

Input data for `PreToolUse` hook events.

```python
class PreToolUseHookInput(BaseHookInput):
    hook_event_name: Literal["PreToolUse"]
    tool_name: str
    tool_input: dict[str, Any]
    tool_use_id: str
    agent_id: NotRequired[str]
    agent_type: NotRequired[str]
```

| Field             | Type                    | Description                                                        |
|:------------------|:------------------------|:-------------------------------------------------------------------|
| `hook_event_name` | `Literal["PreToolUse"]` | Always “PreToolUse”                                                |
| `tool_name`       | `str`                   | Name of the tool about to be executed                              |
| `tool_input`      | `dict[str, Any]`        | Input parameters for the tool                                      |
| `tool_use_id`     | `str`                   | Unique identifier for this tool use                                |
| `agent_id`        | `str` (optional)        | Subagent identifier, present when the hook fires inside a subagent |
| `agent_type`      | `str` (optional)        | Subagent type, present when the hook fires inside a subagent       |


[​](#posttoolusehookinput)

`PostToolUseHookInput`

Input data for `PostToolUse` hook events.

```python
class PostToolUseHookInput(BaseHookInput):
    hook_event_name: Literal["PostToolUse"]
    tool_name: str
    tool_input: dict[str, Any]
    tool_response: Any
    tool_use_id: str
    agent_id: NotRequired[str]
    agent_type: NotRequired[str]
```

| Field             | Type                     | Description                                                        |
|:------------------|:-------------------------|:-------------------------------------------------------------------|
| `hook_event_name` | `Literal["PostToolUse"]` | Always “PostToolUse”                                               |
| `tool_name`       | `str`                    | Name of the tool that was executed                                 |
| `tool_input`      | `dict[str, Any]`         | Input parameters that were used                                    |
| `tool_response`   | `Any`                    | Response from the tool execution                                   |
| `tool_use_id`     | `str`                    | Unique identifier for this tool use                                |
| `agent_id`        | `str` (optional)         | Subagent identifier, present when the hook fires inside a subagent |
| `agent_type`      | `str` (optional)         | Subagent type, present when the hook fires inside a subagent       |


[​](#posttoolusefailurehookinput)

`PostToolUseFailureHookInput`

Input data for `PostToolUseFailure` hook events. Called when a tool execution fails.

```python
class PostToolUseFailureHookInput(BaseHookInput):
    hook_event_name: Literal["PostToolUseFailure"]
    tool_name: str
    tool_input: dict[str, Any]
    tool_use_id: str
    error: str
    is_interrupt: NotRequired[bool]
    agent_id: NotRequired[str]
    agent_type: NotRequired[str]
```

| Field             | Type                            | Description                                                        |
|:------------------|:--------------------------------|:-------------------------------------------------------------------|
| `hook_event_name` | `Literal["PostToolUseFailure"]` | Always “PostToolUseFailure”                                        |
| `tool_name`       | `str`                           | Name of the tool that failed                                       |
| `tool_input`      | `dict[str, Any]`                | Input parameters that were used                                    |
| `tool_use_id`     | `str`                           | Unique identifier for this tool use                                |
| `error`           | `str`                           | Error message from the failed execution                            |
| `is_interrupt`    | `bool` (optional)               | Whether the failure was caused by an interrupt                     |
| `agent_id`        | `str` (optional)                | Subagent identifier, present when the hook fires inside a subagent |
| `agent_type`      | `str` (optional)                | Subagent type, present when the hook fires inside a subagent       |


[​](#userpromptsubmithookinput)

`UserPromptSubmitHookInput`

Input data for `UserPromptSubmit` hook events.

```python
class UserPromptSubmitHookInput(BaseHookInput):
    hook_event_name: Literal["UserPromptSubmit"]
    prompt: str
```

| Field             | Type                          | Description                 |
|:------------------|:------------------------------|:----------------------------|
| `hook_event_name` | `Literal["UserPromptSubmit"]` | Always “UserPromptSubmit”   |
| `prompt`          | `str`                         | The user’s submitted prompt |


[​](#stophookinput)

`StopHookInput`

Input data for `Stop` hook events.

```python
class StopHookInput(BaseHookInput):
    hook_event_name: Literal["Stop"]
    stop_hook_active: bool
```

| Field              | Type              | Description                     |
|:-------------------|:------------------|:--------------------------------|
| `hook_event_name`  | `Literal["Stop"]` | Always “Stop”                   |
| `stop_hook_active` | `bool`            | Whether the stop hook is active |


[​](#subagentstophookinput)

`SubagentStopHookInput`

Input data for `SubagentStop` hook events.

```python
class SubagentStopHookInput(BaseHookInput):
    hook_event_name: Literal["SubagentStop"]
    stop_hook_active: bool
    agent_id: str
    agent_transcript_path: str
    agent_type: str
```

| Field                   | Type                      | Description                            |
|:------------------------|:--------------------------|:---------------------------------------|
| `hook_event_name`       | `Literal["SubagentStop"]` | Always “SubagentStop”                  |
| `stop_hook_active`      | `bool`                    | Whether the stop hook is active        |
| `agent_id`              | `str`                     | Unique identifier for the subagent     |
| `agent_transcript_path` | `str`                     | Path to the subagent’s transcript file |
| `agent_type`            | `str`                     | Type of the subagent                   |


[​](#precompacthookinput)

`PreCompactHookInput`

Input data for `PreCompact` hook events.

```python
class PreCompactHookInput(BaseHookInput):
    hook_event_name: Literal["PreCompact"]
    trigger: Literal["manual", "auto"]
    custom_instructions: str | None
```

| Field                 | Type                        | Description                        |
|:----------------------|:----------------------------|:-----------------------------------|
| `hook_event_name`     | `Literal["PreCompact"]`     | Always “PreCompact”                |
| `trigger`             | `Literal["manual", "auto"]` | What triggered the compaction      |
| `custom_instructions` | `str | None`                | Custom instructions for compaction |


[​](#notificationhookinput)

`NotificationHookInput`

Input data for `Notification` hook events.

```python
class NotificationHookInput(BaseHookInput):
    hook_event_name: Literal["Notification"]
    message: str
    title: NotRequired[str]
    notification_type: str
```

| Field               | Type                      | Description                  |
|:--------------------|:--------------------------|:-----------------------------|
| `hook_event_name`   | `Literal["Notification"]` | Always “Notification”        |
| `message`           | `str`                     | Notification message content |
| `title`             | `str` (optional)          | Notification title           |
| `notification_type` | `str`                     | Type of notification         |


[​](#subagentstarthookinput)

`SubagentStartHookInput`

Input data for `SubagentStart` hook events.

```python
class SubagentStartHookInput(BaseHookInput):
    hook_event_name: Literal["SubagentStart"]
    agent_id: str
    agent_type: str
```

| Field             | Type                       | Description                        |
|:------------------|:---------------------------|:-----------------------------------|
| `hook_event_name` | `Literal["SubagentStart"]` | Always “SubagentStart”             |
| `agent_id`        | `str`                      | Unique identifier for the subagent |
| `agent_type`      | `str`                      | Type of the subagent               |


[​](#permissionrequesthookinput)

`PermissionRequestHookInput`

Input data for `PermissionRequest` hook events. Allows hooks to handle permission decisions programmatically.

```python
class PermissionRequestHookInput(BaseHookInput):
    hook_event_name: Literal["PermissionRequest"]
    tool_name: str
    tool_input: dict[str, Any]
    permission_suggestions: NotRequired[list[Any]]
    agent_id: NotRequired[str]
    agent_type: NotRequired[str]
```

| Field                    | Type                           | Description                                                        |
|:-------------------------|:-------------------------------|:-------------------------------------------------------------------|
| `hook_event_name`        | `Literal["PermissionRequest"]` | Always “PermissionRequest”                                         |
| `tool_name`              | `str`                          | Name of the tool requesting permission                             |
| `tool_input`             | `dict[str, Any]`               | Input parameters for the tool                                      |
| `permission_suggestions` | `list[Any]` (optional)         | Suggested permission updates from the CLI                          |
| `agent_id`               | `str` (optional)               | Subagent identifier, present when the hook fires inside a subagent |
| `agent_type`             | `str` (optional)               | Subagent type, present when the hook fires inside a subagent       |


[​](#hookjsonoutput)

`HookJSONOutput`

Union type for hook callback return values.

```python
HookJSONOutput = AsyncHookJSONOutput | SyncHookJSONOutput
```


[​](#synchookjsonoutput)

`SyncHookJSONOutput`

Synchronous hook output with control and decision fields.

```python
class SyncHookJSONOutput(TypedDict):
    # Control fields
    continue_: NotRequired[bool]  # Whether to proceed (default: True)
    suppressOutput: NotRequired[bool]  # Hide stdout from transcript
    stopReason: NotRequired[str]  # Message when continue is False

    # Decision fields
    decision: NotRequired[Literal["block"]]
    systemMessage: NotRequired[str]  # Warning message for user
    reason: NotRequired[str]  # Feedback for Claude

    # Hook-specific output
    hookSpecificOutput: NotRequired[HookSpecificOutput]
```

Use `continue_` (with underscore) in Python code. It is automatically converted to `continue` when sent to the CLI.


[​](#hookspecificoutput)

`HookSpecificOutput`

A `TypedDict` containing the hook event name and event-specific fields. The shape depends on the `hookEventName` value. For full details on available fields per hook event, see [Control execution with hooks](/docs/en/agent-sdk/hooks#outputs). A discriminated union of event-specific output types. The `hookEventName` field determines which fields are valid.

```python
class PreToolUseHookSpecificOutput(TypedDict):
    hookEventName: Literal["PreToolUse"]
    permissionDecision: NotRequired[Literal["allow", "deny", "ask", "defer"]]
    permissionDecisionReason: NotRequired[str]
    updatedInput: NotRequired[dict[str, Any]]
    additionalContext: NotRequired[str]


class PostToolUseHookSpecificOutput(TypedDict):
    hookEventName: Literal["PostToolUse"]
    additionalContext: NotRequired[str]
    updatedToolOutput: NotRequired[Any]
    updatedMCPToolOutput: NotRequired[Any]  # Deprecated: use updatedToolOutput, which works for all tools


class PostToolUseFailureHookSpecificOutput(TypedDict):
    hookEventName: Literal["PostToolUseFailure"]
    additionalContext: NotRequired[str]


class UserPromptSubmitHookSpecificOutput(TypedDict):
    hookEventName: Literal["UserPromptSubmit"]
    additionalContext: NotRequired[str]


class NotificationHookSpecificOutput(TypedDict):
    hookEventName: Literal["Notification"]
    additionalContext: NotRequired[str]


class SubagentStartHookSpecificOutput(TypedDict):
    hookEventName: Literal["SubagentStart"]
    additionalContext: NotRequired[str]


class PermissionRequestHookSpecificOutput(TypedDict):
    hookEventName: Literal["PermissionRequest"]
    decision: dict[str, Any]


HookSpecificOutput = (
    PreToolUseHookSpecificOutput
    | PostToolUseHookSpecificOutput
    | PostToolUseFailureHookSpecificOutput
    | UserPromptSubmitHookSpecificOutput
    | NotificationHookSpecificOutput
    | SubagentStartHookSpecificOutput
    | PermissionRequestHookSpecificOutput
)
```


[​](#asynchookjsonoutput)

`AsyncHookJSONOutput`

Async hook output that defers hook execution.

```python
class AsyncHookJSONOutput(TypedDict):
    async_: Literal[True]  # Set to True to defer execution
    asyncTimeout: NotRequired[int]  # Timeout in milliseconds
```

Use `async_` (with underscore) in Python code. It is automatically converted to `async` when sent to the CLI.


[​](#hook-usage-example)

Hook Usage Example

This example registers two hooks: one that blocks dangerous bash commands like `rm -rf /`, and another that logs all tool usage for auditing. The security hook only runs on Bash commands (via the `matcher`), while the logging hook runs on all tools.

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, HookMatcher, HookContext
from typing import Any


async def validate_bash_command(
    input_data: dict[str, Any], tool_use_id: str | None, context: HookContext
) -> dict[str, Any]:
    """Validate and potentially block dangerous bash commands."""
    if input_data["tool_name"] == "Bash":
        command = input_data["tool_input"].get("command", "")
        if "rm -rf /" in command:
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": "Dangerous command blocked",
                }
            }
    return {}


async def log_tool_use(
    input_data: dict[str, Any], tool_use_id: str | None, context: HookContext
) -> dict[str, Any]:
    """Log all tool usage for auditing."""
    print(f"Tool used: {input_data.get('tool_name')}")
    return {}


options = ClaudeAgentOptions(
    hooks={
        "PreToolUse": [
            HookMatcher(
                matcher="Bash", hooks=[validate_bash_command], timeout=120
            ),  # 2 min for validation
            HookMatcher(
                hooks=[log_tool_use]
            ),  # Applies to all tools (per-event default timeout)
        ],
        "PostToolUse": [HookMatcher(hooks=[log_tool_use])],
    }
)

async def main():
    async for message in query(prompt="Analyze this codebase", options=options):
        print(message)


asyncio.run(main())
```


[​](#tool-input/output-types)

Tool Input/Output Types

Documentation of input/output schemas for all built-in Claude Code tools. While the Python SDK doesn’t export these as types, they represent the structure of tool inputs and outputs in messages.


[​](#agent)

Agent

**Tool name:** `Agent`. The previous name `Task` is still accepted as an alias, and the `tools` list in the init [`SystemMessage`](#systemmessage) reports this tool as `Task` for backward compatibility. **Input:**

```python
{
    "description": str,  # A short (3-5 word) description of the task
    "prompt": str,  # The task for the agent to perform
    "subagent_type": str | None,  # The type of specialized agent to use
    "model": "sonnet" | "opus" | "haiku" | "fable" | None,  # Model override for this agent
    "run_in_background": bool | None,  # Agents run in the background by default; set to False to run synchronously
    "name": str | None,  # Name for the spawned agent
    "team_name": str | None,  # Deprecated; ignored
    "mode": "acceptEdits" | "auto" | "bypassPermissions" | "default" | "dontAsk" | "plan" | None,  # Deprecated; ignored. Subagents inherit the parent session's permission mode; agent-definition frontmatter may override it
    "isolation": "worktree" | "remote" | None,  # Isolation mode for the agent's changes
}
```

Launches a new agent to handle complex, multi-step tasks autonomously. **Output (status: `"completed"`):**

```python
{
    "status": "completed",
    "agentId": str,  # ID of the agent that ran
    "agentType": str | None,  # The subagent type that handled the task
    "content": [  # Result content blocks
        {
            "type": "text",
            "text": str,
            "citations": list | None,
        }
    ],
    "resolvedModel": str | None,  # Model the subagent started on
    "modelsUsed": list[str] | None,  # Models used in order, with consecutive repeats collapsed
    "totalToolUseCount": int,  # Number of tool calls the agent made
    "totalDurationMs": int,  # Execution duration in milliseconds
    "totalTokens": int,  # Total tokens used
    "usage": {  # Token usage statistics
        "input_tokens": int,
        "output_tokens": int,
        "cache_creation_input_tokens": int | None,
        "cache_read_input_tokens": int | None,
        "server_tool_use": {"web_search_requests": int, "web_fetch_requests": int} | None,
        "service_tier": str | None,
        "cache_creation": {"ephemeral_1h_input_tokens": int, "ephemeral_5m_input_tokens": int} | None,
        "inference_geo": str | None,
        "speed": str | None,
        "iterations": Any | None,
    },
    "toolStats": {  # Aggregate tool activity for the run
        "readCount": int,
        "searchCount": int,
        "bashCount": int,
        "editFileCount": int,
        "linesAdded": int,
        "linesRemoved": int,
        "otherToolCount": int,
        "frameCount": int | None,
    } | None,
    "prompt": str,  # The prompt the agent ran
    "worktreePath": str | None,  # Present for worktree-isolated runs
    "worktreeBranch": str | None,  # Present for worktree-isolated runs
}
```

**Output (status: `"async_launched"`):**

```python
{
    "status": "async_launched",
    "isAsync": bool | None,  # True on background launches
    "agentId": str,  # ID of the launched agent
    "description": str,  # The task description
    "resolvedModel": str | None,  # Model in use at the backgrounding transition
    "modelsUsed": list[str] | None,  # Models used before backgrounding, in order, with consecutive repeats collapsed
    "prompt": str,  # The prompt the agent runs
    "outputFile": str,  # File path where the agent's output is written
    "canReadOutputFile": bool | None,  # Whether the output file can be read directly
}
```

**Output (status: `"remote_launched"`):**

```python
{
    "status": "remote_launched",
    "taskId": str,  # ID of the remote task
    "sessionUrl": str,  # Link to the remote cloud session
    "description": str,  # The task description
    "prompt": str,  # The prompt the agent runs
    "outputFile": str,  # File path where the agent's output is written
}
```

Returns the result from the subagent. The output is discriminated on the `status` field: `"completed"` for finished tasks, `"async_launched"` for background tasks, and `"remote_launched"` for tasks Claude Code dispatched to a remote cloud session, where `sessionUrl` links to that session and `taskId` identifies it. Worktree-isolated runs include `worktreePath` and `worktreeBranch` on the `completed` variant. On the `completed` variant, `resolvedModel` names the model the subagent started on, which can differ from the requested `model` input when [`availableModels`](/docs/en/model-config#restrict-model-selection) or another override applies. This field requires Claude Code v2.1.174 or later. On the `async_launched` variant, `resolvedModel` names the model in use when the agent moved to the background, so a swap that happened before backgrounding is reflected there. The `modelsUsed` field on both variants lists the models used in order, with consecutive repeats collapsed; it’s set only when the model was swapped mid-run. `modelsUsed` and the backgrounding-time `resolvedModel` behavior require Claude Code v2.1.212 or later.


[​](#askuserquestion)

AskUserQuestion

**Tool name:** `AskUserQuestion` Asks the user clarifying questions during execution. See [Handle approvals and user input](/docs/en/agent-sdk/user-input#handle-clarifying-questions) for usage details. **Input:**

```python
{
    "questions": [  # Questions to ask the user (1-4 questions)
        {
            "question": str,  # The complete question to ask the user
            "header": str,  # Very short label displayed as a chip/tag (max 12 chars)
            "options": [  # The available choices (2-4 options)
                {
                    "label": str,  # Display text for this option (1-5 words)
                    "description": str,  # Explanation of what this option means
                    "preview": str | None,  # Preview content rendered when the option is focused
                }
            ],
            "multiSelect": bool,  # Set to true to allow multiple selections
        }
    ],
    "answers": dict[str, str] | None,
    # User answers populated by the permission system. Multi-select
    # answers are a comma-joined string of the selected labels; a
    # list of labels is accepted on input and coerced to that form
    "annotations": dict[str, dict] | None,
    # Per-question annotations from the user, keyed by question text.
    # Each value can carry "preview" (the selected option's preview
    # content) and "notes" (free-text notes on the selection)
    "metadata": dict | None,  # Analytics metadata, such as {"source": "remember"}; not displayed to the user
}
```

**Output:**

```python
{
    "questions": [  # The questions that were asked
        {
            "question": str,
            "header": str,
            "options": [{"label": str, "description": str, "preview": str | None}],
            "multiSelect": bool,
        }
    ],
    "answers": dict[str, str],  # Maps question text to answer string
    # Multi-select answers are comma-separated
    "response": str | None,
    # Freeform reply typed instead of answering the questions; when set,
    # Claude receives "The user responded: ..." in place of the answer list
    "annotations": dict[str, dict] | None,  # Per-question "preview" and "notes" from the user's selections
    "afkTimeoutMs": int | None,  # Set when the dialog auto-resolved after this many milliseconds of user inactivity; absent when the user answered
}
```


[​](#bash)

Bash

**Tool name:** `Bash` **Input:**

```python
{
    "command": str,  # The command to execute
    "timeout": int | None,  # Optional timeout in milliseconds (max 600000; higher values are clamped to the max)
    "description": str | None,  # Clear, concise description (5-10 words)
    "run_in_background": bool | None,  # Set to true to run in background
}
```

**Output:**

```python
{
    "output": str,  # Combined stdout and stderr output
    "exitCode": int,  # Exit code of the command
    "killed": bool | None,  # Whether command was killed due to timeout
    "shellId": str | None,  # Shell ID for background processes
}
```


[​](#monitor)

Monitor

**Tool name:** `Monitor` Runs a background source and delivers each event to Claude so it can react without polling: `command` runs a script and emits one event per stdout line, and `ws` opens a WebSocket and emits one event per text frame. Provide exactly one of `command` or `ws`. When Monitor runs a command, it follows the same permission rules as Bash; a WebSocket watch prompts for approval separately. The `ws` source requires Claude Code v2.1.195 or later. See the [Monitor tool reference](/docs/en/tools-reference#monitor-tool) for behavior and provider availability. **Input:**

```python
{
    "command": str | None,  # Shell script; each stdout line is an event, exit ends the watch
    "ws": dict | None,  # WebSocket source: {"url": str, "protocols": list[str] | None}; each text frame is an event
    "description": str,  # Short description shown in notifications
    "timeout_ms": int | None,  # Kill after this deadline (default 300000, max 3600000)
    "persistent": bool | None,  # Run for the lifetime of the session; stop with TaskStop
}
```

**Output:**

```python
{
    "taskId": str,  # ID of the background monitor task
    "timeoutMs": int,  # Timeout deadline in milliseconds (0 when persistent)
    "persistent": bool | None,  # True when running until TaskStop or session end
}
```


[​](#edit)

Edit

**Tool name:** `Edit` **Input:**

```python
{
    "file_path": str,  # The absolute path to the file to modify
    "old_string": str,  # The text to replace
    "new_string": str,  # The text to replace it with
    "replace_all": bool | None,  # Replace all occurrences (default False)
}
```

**Output:**

```python
{
    "message": str,  # Confirmation message
    "replacements": int,  # Number of replacements made
    "file_path": str,  # File path that was edited
}
```


[​](#read)

Read

**Tool name:** `Read` **Input:**

```python
{
    "file_path": str,  # The absolute path to the file to read
    "offset": int | None,  # The line number to start reading from
    "limit": int | None,  # The number of lines to read
}
```

**Output (Text files):**

```python
{
    "content": str,  # File contents with line numbers
    "total_lines": int,  # Total number of lines in file
    "lines_returned": int,  # Lines actually returned
}
```

**Output (Images):**

```python
{
    "image": str,  # Base64 encoded image data
    "mime_type": str,  # Image MIME type
    "file_size": int,  # File size in bytes
}
```


[​](#write)

Write

**Tool name:** `Write` **Input:**

```python
{
    "file_path": str,  # The absolute path to the file to write
    "content": str,  # The content to write to the file
}
```

**Output:**

```python
{
    "message": str,  # Success message
    "bytes_written": int,  # Number of bytes written
    "file_path": str,  # File path that was written
}
```


[​](#glob)

Glob

**Tool name:** `Glob` **Input:**

```python
{
    "pattern": str,  # The glob pattern to match files against
    "path": str | None,  # The directory to search in (defaults to cwd)
}
```

**Output:**

```python
{
    "matches": list[str],  # Array of matching file paths
    "count": int,  # Number of matches found
    "search_path": str,  # Search directory used
}
```


[​](#grep)

Grep

**Tool name:** `Grep` **Input:**

```python
{
    "pattern": str,  # The regular expression pattern
    "path": str | None,  # File or directory to search in
    "glob": str | None,  # Glob pattern to filter files
    "type": str | None,  # File type to search
    "output_mode": str | None,  # "content", "files_with_matches", or "count"
    "-i": bool | None,  # Case insensitive search
    "-n": bool | None,  # Show line numbers
    "-B": int | None,  # Lines to show before each match
    "-A": int | None,  # Lines to show after each match
    "-C": int | None,  # Lines to show before and after
    "head_limit": int | None,  # Limit output to first N lines/entries
    "multiline": bool | None,  # Enable multiline mode
}
```

**Output (content mode):**

```python
{
    "matches": [
        {
            "file": str,
            "line_number": int | None,
            "line": str,
            "before_context": list[str] | None,
            "after_context": list[str] | None,
        }
    ],
    "total_matches": int,
}
```

**Output (files_with_matches mode):**

```python
{
    "files": list[str],  # Files containing matches
    "count": int,  # Number of files with matches
}
```


[​](#notebookedit)

NotebookEdit

**Tool name:** `NotebookEdit` **Input:**

```python
{
    "notebook_path": str,  # Absolute path to the Jupyter notebook
    "cell_id": str | None,  # The ID of the cell to edit
    "new_source": str,  # The new source for the cell
    "cell_type": "code" | "markdown" | None,  # The type of the cell
    "edit_mode": "replace" | "insert" | "delete" | None,  # Edit operation type
}
```

**Output:**

```python
{
    "message": str,  # Success message
    "edit_type": "replaced" | "inserted" | "deleted",  # Type of edit performed
    "cell_id": str | None,  # Cell ID that was affected
    "total_cells": int,  # Total cells in notebook after edit
}
```


[​](#webfetch)

WebFetch

**Tool name:** `WebFetch` **Input:**

```python
{
    "url": str,  # The URL to fetch content from
    "prompt": str,  # The prompt to run on the fetched content
}
```

**Output:**

```python
{
    "bytes": int,  # Size of the fetched content in bytes
    "code": int,  # HTTP response code
    "codeText": str,  # HTTP response code text
    "result": str,  # Processed result from applying the prompt to the content
    "durationMs": int,  # Time to fetch and process the content, in milliseconds
    "url": str,  # URL that was fetched
}
```


[​](#websearch)

WebSearch

**Tool name:** `WebSearch` **Input:**

```python
{
    "query": str,  # The search query to use
    "allowed_domains": list[str] | None,  # Only include results from these domains
    "blocked_domains": list[str] | None,  # Never include results from these domains
}
```

**Output:**

```python
{
    "query": str,  # The search query
    "results": list[str | {"tool_use_id": str, "content": list[{"title": str, "url": str}]}],
    "durationSeconds": float,  # Search duration in seconds
}
```


[​](#todowrite)

TodoWrite

**Tool name:** `TodoWrite`

As of Claude Code v2.1.142, `TodoWrite` is disabled by default. Use `TaskCreate`, `TaskGet`, `TaskUpdate`, and `TaskList` instead. See [Migrate to Task tools](/docs/en/agent-sdk/todo-tracking#migrate-to-task-tools) to update your monitoring code, or set `CLAUDE_CODE_ENABLE_TASKS=0` to revert to `TodoWrite`.

**Input:**

```python
{
    "todos": [
        {
            "content": str,  # The task description
            "status": "pending" | "in_progress" | "completed",  # Task status
            "activeForm": str,  # Active form of the description
        }
    ]
}
```

**Output:**

```python
{
    "message": str,  # Success message
    "stats": {"total": int, "pending": int, "in_progress": int, "completed": int},
}
```


[​](#taskcreate)

TaskCreate

**Tool name:** `TaskCreate` **Input:**

```python
{
    "subject": str,  # Short task title
    "description": str,  # Detailed task body
    "activeForm": str | None,  # Present-tense label shown while in progress
    "metadata": dict | None,  # Arbitrary caller metadata
}
```

**Output:**

```python
{
    "task": {"id": str, "subject": str},  # Created task with assigned ID
}
```


[​](#taskupdate)

TaskUpdate

**Tool name:** `TaskUpdate` **Input:**

```python
{
    "taskId": str,  # ID of the task to patch
    "status": Literal["pending", "in_progress", "completed", "deleted"] | None,
    "subject": str | None,
    "description": str | None,
    "activeForm": str | None,
    "addBlocks": list[str] | None,  # Task IDs this task now blocks
    "addBlockedBy": list[str] | None,  # Task IDs that now block this task
    "owner": str | None,
    "metadata": dict | None,
}
```

**Output:**

```python
{
    "success": bool,
    "taskId": str,
    "updatedFields": list[str],  # Names of fields that changed
    "error": str | None,
    "statusChange": {"from": str, "to": str} | None,
}
```


[​](#taskget)

TaskGet

**Tool name:** `TaskGet` **Input:**

```python
{
    "taskId": str,  # ID of the task to read
}
```

**Output:**

```python
{
    "task": {
        "id": str,
        "subject": str,
        "description": str,
        "status": Literal["pending", "in_progress", "completed"],
        "blocks": list[str],
        "blockedBy": list[str],
    } | None,  # None when the ID is not found
}
```


[​](#tasklist)

TaskList

**Tool name:** `TaskList` **Input:**

```python
{}
```

**Output:**

```python
{
    "tasks": [
        {
            "id": str,
            "subject": str,
            "status": Literal["pending", "in_progress", "completed"],
            "owner": str | None,
            "blockedBy": list[str],
        }
    ],
}
```


[​](#taskoutput)

TaskOutput

**Tool name:** `TaskOutput`. The previous name `BashOutput` is still accepted as an alias.

`TaskOutput` is deprecated; prefer `Read` on the task’s output file path. Deprecated since Claude Code v2.1.83. The schemas below remain valid for hooks and permission handlers that encounter the tool.

**Input:**

```python
{
    "task_id": str,  # The task ID to get output from
    "block": bool,  # Whether to wait for completion (default True)
    "timeout": int,  # Max wait time in ms (default 30000)
}
```

**Output:**

```python
{
    "retrieval_status": "success" | "timeout" | "not_ready",  # Whether the output was retrieved
    "task": dict | None,  # Task details: task_id, task_type, status, description, output, plus type-specific fields such as exitCode
}
```


[​](#taskstop)

TaskStop

**Tool name:** `TaskStop`. The previous names `KillShell` and `KillBash` are still accepted as aliases. **Input:**

```python
{
    "task_id": str | None,  # The ID of the background task to stop
    "shell_id": str | None,  # Deprecated: use task_id instead
}
```

**Output:**

```python
{
    "message": str,  # Status message about the operation
    "task_id": str,  # The ID of the task that was stopped
    "task_type": str,  # The type of the task that was stopped
    "command": str | None,  # The command or description of the stopped task
}
```


[​](#exitplanmode)

ExitPlanMode

**Tool name:** `ExitPlanMode` **Input:**

```python
{
    "plan": str  # The plan to run by the user for approval
}
```

**Output:**

```python
{
    "message": str,  # Confirmation message
    "approved": bool | None,  # Whether user approved the plan
}
```


[​](#listmcpresources)

ListMcpResources

**Tool name:** `ListMcpResourcesTool` **Input:**

```python
{
    "server": str | None  # Optional server name to filter resources by
}
```

**Output:**

```python
{
    "resources": [
        {
            "uri": str,
            "name": str,
            "description": str | None,
            "mimeType": str | None,
            "server": str,
        }
    ],
    "total": int,
}
```


[​](#readmcpresource)

ReadMcpResource

**Tool name:** `ReadMcpResourceTool` **Input:**

```python
{
    "server": str,  # The MCP server name
    "uri": str,  # The resource URI to read
}
```

**Output:**

```python
{
    "contents": [
        {"uri": str, "mimeType": str | None, "text": str | None, "blob": str | None}
    ],
    "server": str,
}
```


[​](#advanced-features-with-claudesdkclient)

Advanced Features with ClaudeSDKClient


[​](#building-a-continuous-conversation-interface)

Building a Continuous Conversation Interface

```python
from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    AssistantMessage,
    TextBlock,
)
import asyncio


class ConversationSession:
    """Maintains a single conversation session with Claude."""

    def __init__(self, options: ClaudeAgentOptions | None = None):
        self.client = ClaudeSDKClient(options)
        self.turn_count = 0

    async def start(self):
        await self.client.connect()
        print("Starting conversation session. Claude will remember context.")
        print(
            "Commands: 'exit' to quit, 'interrupt' to stop current task, 'new' for new session"
        )

        while True:
            user_input = input(f"\n[Turn {self.turn_count + 1}] You: ")

            if user_input.lower() == "exit":
                break
            elif user_input.lower() == "interrupt":
                await self.client.interrupt()
                print("Task interrupted!")
                continue
            elif user_input.lower() == "new":
                # Disconnect and reconnect for a fresh session
                await self.client.disconnect()
                await self.client.connect()
                self.turn_count = 0
                print("Started new conversation session (previous context cleared)")
                continue

            # Send message - the session retains all previous messages
            await self.client.query(user_input)
            self.turn_count += 1

            # Process response
            print(f"[Turn {self.turn_count}] Claude: ", end="")
            async for message in self.client.receive_response():
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            print(block.text, end="")
            print()  # New line after response

        await self.client.disconnect()
        print(f"Conversation ended after {self.turn_count} turns.")


async def main():
    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Write", "Bash"], permission_mode="acceptEdits"
    )
    session = ConversationSession(options)
    await session.start()


# Example conversation:
# Turn 1 - You: "Create a file called hello.py"
# Turn 1 - Claude: "I'll create a hello.py file for you..."
# Turn 2 - You: "What's in that file?"
# Turn 2 - Claude: "The hello.py file I just created contains..." (remembers!)
# Turn 3 - You: "Add a main function to it"
# Turn 3 - Claude: "I'll add a main function to hello.py..." (knows which file!)

asyncio.run(main())
```


[​](#using-hooks-for-behavior-modification)

Using Hooks for Behavior Modification

```python
from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    HookMatcher,
    HookContext,
)
import asyncio
from typing import Any


async def pre_tool_logger(
    input_data: dict[str, Any], tool_use_id: str | None, context: HookContext
) -> dict[str, Any]:
    """Log all tool usage before execution."""
    tool_name = input_data.get("tool_name", "unknown")
    print(f"[PRE-TOOL] About to use: {tool_name}")

    # You can modify or block the tool execution here
    if tool_name == "Bash" and "rm -rf" in str(input_data.get("tool_input", {})):
        return {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": "Dangerous command blocked",
            }
        }
    return {}


async def post_tool_logger(
    input_data: dict[str, Any], tool_use_id: str | None, context: HookContext
) -> dict[str, Any]:
    """Log results after tool execution."""
    tool_name = input_data.get("tool_name", "unknown")
    print(f"[POST-TOOL] Completed: {tool_name}")
    return {}


async def user_prompt_modifier(
    input_data: dict[str, Any], tool_use_id: str | None, context: HookContext
) -> dict[str, Any]:
    """Add context to user prompts."""
    original_prompt = input_data.get("prompt", "")

    # Add a timestamp as additional context for Claude to see
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": f"[Submitted at {timestamp}] Original prompt: {original_prompt}",
        }
    }


async def main():
    options = ClaudeAgentOptions(
        hooks={
            "PreToolUse": [
                HookMatcher(hooks=[pre_tool_logger]),
                HookMatcher(matcher="Bash", hooks=[pre_tool_logger]),
            ],
            "PostToolUse": [HookMatcher(hooks=[post_tool_logger])],
            "UserPromptSubmit": [HookMatcher(hooks=[user_prompt_modifier])],
        },
        allowed_tools=["Read", "Write", "Bash"],
    )

    async with ClaudeSDKClient(options=options) as client:
        await client.query("List files in current directory")

        async for message in client.receive_response():
            # Hooks will automatically log tool usage
            pass


asyncio.run(main())
```


[​](#real-time-progress-monitoring)

Real-time Progress Monitoring

```python
from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    AssistantMessage,
    ToolUseBlock,
    ToolResultBlock,
    TextBlock,
)
import asyncio


async def monitor_progress():
    options = ClaudeAgentOptions(
        allowed_tools=["Write", "Bash"], permission_mode="acceptEdits"
    )

    async with ClaudeSDKClient(options=options) as client:
        await client.query("Create 5 Python files with different sorting algorithms")

        # Monitor progress in real-time
        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, ToolUseBlock):
                        if block.name == "Write":
                            file_path = block.input.get("file_path", "")
                            print(f"Creating: {file_path}")
                    elif isinstance(block, ToolResultBlock):
                        print("Completed tool execution")
                    elif isinstance(block, TextBlock):
                        print(f"Claude says: {block.text[:100]}...")

        print("Task completed!")


asyncio.run(monitor_progress())
```


[​](#example-usage)

Example Usage


[​](#basic-file-operations-using-query)

Basic file operations (using query)

```python
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ToolUseBlock
import asyncio


async def create_project():
    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Write", "Bash"],
        permission_mode="acceptEdits",
    )

    async for message in query(
        prompt="Create a Python project structure with setup.py", options=options
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, ToolUseBlock):
                    print(f"Using tool: {block.name}")


asyncio.run(create_project())
```


[​](#error-handling)

Error handling

```python
import asyncio

from claude_agent_sdk import query, CLINotFoundError, ProcessError, CLIJSONDecodeError


async def main():
    try:
        async for message in query(prompt="Hello"):
            print(message)
    except CLINotFoundError:
        print(
            "Claude Code CLI not found. Try reinstalling: pip install --force-reinstall claude-agent-sdk"
        )
    except ProcessError as e:
        print(f"Process failed with exit code: {e.exit_code}")
    except CLIJSONDecodeError as e:
        print(f"Failed to parse response: {e}")
    # A single-shot query() raises a plain Exception after yielding an error result
    except Exception as e:
        print(f"Query ended with an error result: {e}")


asyncio.run(main())
```


[​](#streaming-mode-with-client)

Streaming mode with client

```python
from claude_agent_sdk import ClaudeSDKClient
import asyncio


async def interactive_session():
    async with ClaudeSDKClient() as client:
        # Send initial message
        await client.query("What's the weather like?")

        # Process responses
        async for msg in client.receive_response():
            print(msg)

        # Send follow-up
        await client.query("Tell me more about that")

        # Process follow-up response
        async for msg in client.receive_response():
            print(msg)


asyncio.run(interactive_session())
```


[​](#using-custom-tools-with-claudesdkclient)

Using custom tools with ClaudeSDKClient

```python
from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    tool,
    create_sdk_mcp_server,
    AssistantMessage,
    TextBlock,
)
import asyncio
from typing import Any


# Define custom tools with @tool decorator
@tool("calculate", "Perform mathematical calculations", {"expression": str})
async def calculate(args: dict[str, Any]) -> dict[str, Any]:
    try:
        result = eval(args["expression"], {"__builtins__": {}})
        return {"content": [{"type": "text", "text": f"Result: {result}"}]}
    except Exception as e:
        return {
            "content": [{"type": "text", "text": f"Error: {str(e)}"}],
            "is_error": True,
        }


@tool("get_time", "Get current time", {})
async def get_time(args: dict[str, Any]) -> dict[str, Any]:
    from datetime import datetime

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"content": [{"type": "text", "text": f"Current time: {current_time}"}]}


async def main():
    # Create SDK MCP server with custom tools
    my_server = create_sdk_mcp_server(
        name="utilities", version="1.0.0", tools=[calculate, get_time]
    )

    # Configure options with the server
    options = ClaudeAgentOptions(
        mcp_servers={"utils": my_server},
        allowed_tools=["mcp__utils__calculate", "mcp__utils__get_time"],
    )

    # Use ClaudeSDKClient for interactive tool usage
    async with ClaudeSDKClient(options=options) as client:
        await client.query("What's 123 * 456?")

        # Process calculation response
        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        print(f"Calculation: {block.text}")

        # Follow up with time query
        await client.query("What time is it now?")

        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    if isinstance(block, TextBlock):
                        print(f"Time: {block.text}")


asyncio.run(main())
```


[​](#sandbox-configuration)

Sandbox Configuration


[​](#sandboxsettings)

`SandboxSettings`

Configuration for sandbox behavior. Use this to enable command sandboxing and configure network restrictions programmatically.

```python
class SandboxSettings(TypedDict, total=False):
    enabled: bool
    autoAllowBashIfSandboxed: bool
    excludedCommands: list[str]
    allowUnsandboxedCommands: bool
    network: SandboxNetworkConfig
    ignoreViolations: SandboxIgnoreViolations
    enableWeakerNestedSandbox: bool
```

| Property                    | Type                                                  | Default | Description                                                                                                                                                                                                                             |
|:----------------------------|:------------------------------------------------------|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `enabled`                   | `bool`                                                | `False` | Enable sandbox mode for command execution                                                                                                                                                                                               |
| `autoAllowBashIfSandboxed`  | `bool`                                                | `True`  | Auto-approve bash commands when sandbox is enabled                                                                                                                                                                                      |
| `excludedCommands`          | `list[str]`                                           | `[]`    | Commands that always bypass sandbox restrictions (e.g., `["docker"]`). These run unsandboxed automatically without model involvement                                                                                                    |
| `allowUnsandboxedCommands`  | `bool`                                                | `True`  | Allow the model to request running commands outside the sandbox. When `True`, the model can set `dangerouslyDisableSandbox` in tool input, which falls back to the [permissions system](#permissions-fallback-for-unsandboxed-commands) |
| `network`                   | [`SandboxNetworkConfig`](#sandboxnetworkconfig)       | `None`  | Network-specific sandbox configuration                                                                                                                                                                                                  |
| `ignoreViolations`          | [`SandboxIgnoreViolations`](#sandboxignoreviolations) | `None`  | Configure which sandbox violations to ignore                                                                                                                                                                                            |
| `enableWeakerNestedSandbox` | `bool`                                                | `False` | Enable a weaker nested sandbox for compatibility                                                                                                                                                                                        |

The sandbox depends on platform support and, on Linux, tools like `bubblewrap` and `socat`. By default, when `enabled` is `True` but the sandbox can’t start, commands run unsandboxed with a warning on stderr. This default differs from the TypeScript SDK, where `failIfUnavailable` defaults to `true`.Set `"failIfUnavailable": True` in your sandbox settings to stop instead. The key isn’t declared on `SandboxSettings` yet, but the SDK forwards it to Claude Code, which honors it. `query()` then reports a `ResultMessage` with `subtype="error_during_execution"` and the reason in `errors`. Because this is a single-shot `query()` call, the SDK raises after yielding that error result, so wrap the loop in a try block to continue past it. See [Handle the result](/docs/en/agent-sdk/agent-loop#handle-the-result) for the error contract.


[​](#example-usage-2)

Example usage

```python
import asyncio

from claude_agent_sdk import query, ClaudeAgentOptions

sandbox_settings = {
    "enabled": True,
    "autoAllowBashIfSandboxed": True,
    "failIfUnavailable": True,
    "network": {"allowLocalBinding": True},
}


async def main():
    try:
        async for message in query(
            prompt="Build and test my project",
            options=ClaudeAgentOptions(sandbox=sandbox_settings),
        ):
            print(message)
    except Exception as error:
        # A single-shot query() raises after yielding an error result,
        # such as when failIfUnavailable is set and the sandbox can't start.
        print(f"Session ended with an error: {error}")


asyncio.run(main())
```

**Unix socket security**: The `allowUnixSockets` option can grant access to powerful system services. For example, allowing `/var/run/docker.sock` effectively grants full host system access through the Docker API, bypassing sandbox isolation. Only allow Unix sockets that are strictly necessary and understand the security implications of each.


[​](#sandboxnetworkconfig)

`SandboxNetworkConfig`

Network-specific configuration for sandbox mode. These settings apply to sandboxed Bash commands when `enabled` is `True` in the parent [`SandboxSettings`](#sandboxsettings). They do not restrict the WebFetch tool, which uses [permission rules](/docs/en/permissions#webfetch) instead.

```python
class SandboxNetworkConfig(TypedDict, total=False):
    allowedDomains: list[str]
    deniedDomains: list[str]
    allowManagedDomainsOnly: bool
    allowUnixSockets: list[str]
    allowAllUnixSockets: bool
    allowLocalBinding: bool
    allowMachLookup: list[str]
    httpProxyPort: int
    socksProxyPort: int
```

| Property                  | Type        | Default | Description                                                                                                                                            |
|:--------------------------|:------------|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `allowedDomains`          | `list[str]` | `[]`    | Domain names that sandboxed processes can access                                                                                                       |
| `deniedDomains`           | `list[str]` | `[]`    | Domain names that sandboxed processes cannot access. Takes precedence over `allowedDomains`                                                            |
| `allowManagedDomainsOnly` | `bool`      | `False` | Managed-settings only: when set in managed settings, ignore `allowedDomains` from non-managed settings sources. Has no effect when set via SDK options |
| `allowUnixSockets`        | `list[str]` | `[]`    | Unix socket paths that processes can access (e.g., Docker socket)                                                                                      |
| `allowAllUnixSockets`     | `bool`      | `False` | Allow access to all Unix sockets                                                                                                                       |
| `allowLocalBinding`       | `bool`      | `False` | Allow processes to bind to local ports (e.g., for dev servers)                                                                                         |
| `allowMachLookup`         | `list[str]` | `[]`    | macOS only: XPC/Mach service names to allow. Supports a trailing wildcard                                                                              |
| `httpProxyPort`           | `int`       | `None`  | HTTP proxy port for network requests                                                                                                                   |
| `socksProxyPort`          | `int`       | `None`  | SOCKS proxy port for network requests                                                                                                                  |

The built-in sandbox proxy enforces the network allowlist based on the requested hostname and does not terminate or inspect TLS traffic, so techniques such as [domain fronting](https://en.wikipedia.org/wiki/Domain_fronting) can potentially bypass it. See [Sandboxing security limitations](/docs/en/sandboxing#security-limitations) for details and [Secure deployment](/docs/en/agent-sdk/secure-deployment#traffic-forwarding) for configuring a TLS-terminating proxy.


[​](#sandboxignoreviolations)

`SandboxIgnoreViolations`

Configuration for ignoring specific sandbox violations.

```python
class SandboxIgnoreViolations(TypedDict, total=False):
    file: list[str]
    network: list[str]
```

| Property  | Type        | Default | Description                                 |
|:----------|:------------|:--------|:--------------------------------------------|
| `file`    | `list[str]` | `[]`    | File path patterns to ignore violations for |
| `network` | `list[str]` | `[]`    | Network patterns to ignore violations for   |


[​](#permissions-fallback-for-unsandboxed-commands)

Permissions Fallback for Unsandboxed Commands

When `allowUnsandboxedCommands` is enabled, the model can request to run commands outside the sandbox by setting `dangerouslyDisableSandbox: True` in the tool input. These requests fall back to the existing permissions system, meaning your `can_use_tool` handler will be invoked, allowing you to implement custom authorization logic.

**`excludedCommands` vs `allowUnsandboxedCommands`:**

- `excludedCommands`: A static list of commands that always bypass the sandbox automatically (e.g., `["docker"]`). The model has no control over this.
- `allowUnsandboxedCommands`: Lets the model decide at runtime whether to request unsandboxed execution by setting `dangerouslyDisableSandbox: True` in the tool input.

```python
import asyncio
from claude_agent_sdk import (
    query,
    ClaudeAgentOptions,
    HookMatcher,
    PermissionResultAllow,
    PermissionResultDeny,
    ToolPermissionContext,
)


def is_command_authorized(command: str | None) -> bool:
    # Replace with your own authorization logic
    return False


async def can_use_tool(
    tool: str, input: dict, context: ToolPermissionContext
) -> PermissionResultAllow | PermissionResultDeny:
    # Check if the model is requesting to bypass the sandbox
    if tool == "Bash" and input.get("dangerouslyDisableSandbox"):
        # The model is requesting to run this command outside the sandbox
        print(f"Unsandboxed command requested: {input.get('command')}")

        if is_command_authorized(input.get("command")):
            return PermissionResultAllow()
        return PermissionResultDeny(
            message="Command not authorized for unsandboxed execution"
        )
    return PermissionResultAllow()


# Required: dummy hook keeps the stream open for can_use_tool
async def dummy_hook(input_data, tool_use_id, context):
    return {"continue_": True}


async def prompt_stream():
    yield {
        "type": "user",
        "message": {"role": "user", "content": "Deploy my application"},
    }


async def main():
    async for message in query(
        prompt=prompt_stream(),
        options=ClaudeAgentOptions(
            sandbox={
                "enabled": True,
                "allowUnsandboxedCommands": True,  # Model can request unsandboxed execution
            },
            permission_mode="default",
            can_use_tool=can_use_tool,
            hooks={"PreToolUse": [HookMatcher(matcher=None, hooks=[dummy_hook])]},
        ),
    ):
        print(message)


asyncio.run(main())
```

This pattern enables you to:

- **Audit model requests**: Log when the model requests unsandboxed execution
- **Implement allowlists**: Only permit specific commands to run unsandboxed
- **Add approval workflows**: Require explicit authorization for privileged operations

Commands running with `dangerouslyDisableSandbox: True` have full system access. Ensure your `can_use_tool` handler validates these requests carefully.If `permission_mode` is set to `bypassPermissions` and `allow_unsandboxed_commands` is enabled, the model can autonomously execute commands outside the sandbox without approval prompts (an explicit [`ask` rule](/docs/en/agent-sdk/permissions#how-permissions-are-evaluated) still forces one). Review enterprise hardening guidance before enabling this combination.


[​](#see-also)

See also

- [SDK overview](/docs/en/agent-sdk/overview) - General SDK concepts
- [TypeScript SDK reference](/docs/en/agent-sdk/typescript) - TypeScript SDK documentation
- [CLI reference](/docs/en/cli-reference) - Command-line interface
- [Common workflows](/docs/en/common-workflows) - Step-by-step guides
