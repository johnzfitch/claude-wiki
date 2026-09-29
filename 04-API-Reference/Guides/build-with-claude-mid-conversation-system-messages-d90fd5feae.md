---
title: "Mid-conversation system messages and tool changes - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:23Z"
tags: ["api", "prompting"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fmid-conversation-system-messages)





SearchCtrlK

First steps

[Intro to Claude](/docs/en/intro)[Get your API key](/docs/en/get-api-key)[Quickstart](/docs/en/get-started)[Authentication](/docs/en/manage-claude/authentication)

Building with Claude

[Features overview](/docs/en/build-with-claude/overview)[Using the Messages API](/docs/en/build-with-claude/working-with-messages)[Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons)[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)[Fallback credit](/docs/en/build-with-claude/fallback-credit)

Model capabilities

[Effort](/docs/en/build-with-claude/effort)[Task budgets (beta)](/docs/en/build-with-claude/task-budgets)[Fast mode (research preview)](/docs/en/build-with-claude/fast-mode)[Structured outputs](/docs/en/build-with-claude/structured-outputs)[Citations](/docs/en/build-with-claude/citations)[Streaming Messages](/docs/en/build-with-claude/streaming)[Batch processing](/docs/en/build-with-claude/batch-processing)[Search results](/docs/en/build-with-claude/search-results)[Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)[Multilingual support](/docs/en/build-with-claude/multilingual-support)[Embeddings](/docs/en/build-with-claude/embeddings)

[Thinking](/docs/en/build-with-claude/thinking)

Tools

[Overview](/docs/en/agents-and-tools/tool-use/overview)[How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works)[Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[Define tools](/docs/en/agents-and-tools/tool-use/define-tools)[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)[Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use)[Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner)[Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)[Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)[Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)[Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)[Browser use tool](/docs/en/agents-and-tools/tool-use/browser-use-tool)[Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Tool infrastructure

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)[Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context)[Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations)[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)

Context management

[Context windows](/docs/en/build-with-claude/context-windows)[Context editing](/docs/en/build-with-claude/context-editing)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)[Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example)[Cache diagnostics](/docs/en/build-with-claude/cache-diagnostics)[Token counting](/docs/en/build-with-claude/token-counting)

[Compaction](/docs/en/build-with-claude/compaction)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

[Images and vision](/docs/en/build-with-claude/vision)

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Quickstart](/docs/en/agents-and-tools/agent-skills/quickstart)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)[Skills in the API](/docs/en/build-with-claude/skills-guide)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)[MCP connector](/docs/en/agents-and-tools/mcp-connector)

[MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

[Console](/)

[Messages](/docs/en/intro)Context management

# Mid-conversation system messages and tool changes

Copy page



Change system instructions or tool availability partway through a conversation without invalidating the cached prefix that came before them.

Copy page





To learn how zero data retention (ZDR) applies to this feature, see [API and data retention](/docs/en/manage-claude/api-and-data-retention).

System instructions normally live in the top-level `system` field, ahead of every message in the conversation. That position is great for [prompt caching](/docs/en/build-with-claude/prompt-caching): the system prompt is part of the stable prefix, so subsequent turns hit the cache. It is a poor position for instructions you only discover you need partway through a session, because editing the top-level `system` field changes the very beginning of the prompt and invalidates the cache for everything that follows.

Mid-conversation system messages close that gap. You append a `{"role": "system"}` message at the point in the conversation where the new instruction becomes relevant, instead of editing the top-level `system` field. The cached prefix stays the same, so the next request still reads it from cache, and the new instruction is still applied as a system instruction rather than as ordinary user text.



Mid-conversation system messages are available on the Claude API, [Claude in Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock), and [Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai).

This feature is available on Claude Fable 5.1, [Claude Mythos 5.1](https://anthropic.com/glasswing), Claude Fable 5, [Claude Mythos 5](https://anthropic.com/glasswing), Claude Opus 5.5, Claude Opus 4.8, and Claude Opus 5. No beta header is required for mid-conversation system messages. This feature is not available on Claude Sonnet 5. Use the top-level `system` field there instead.

[Mid-conversation tool changes](#mid-conversation-tool-changes) are in beta on the same models. On the Claude API, send the `inline-tools-2026-09-15` beta header, which also covers [defining a tool inside a `tool_addition` block](#define-tools-in-a-message-beta). [Adding an MCP server that way](#add-an-mcp-server-mid-conversation-beta) needs a second beta header, `mcp-client-2026-09-15`, which is available on the Claude API. The `mid-conversation-tool-changes-2026-07-01` header works for changes that name a tool by reference, on the Claude API, Amazon Bedrock, and Google Cloud.

[Turn-scoped system messages](#turn-scoped-system-messages) (`clear_at`) are in beta and require the `mid-conversation-system-clear-at-2026-08-21` beta header, on the same models and platforms as mid-conversation system messages.

## Mid-conversation tool changes

The `tools` array sits even earlier in the hashed request prefix than the top-level `system` field, so editing it invalidates the [prompt cache](/docs/en/build-with-claude/prompt-caching) for the entire conversation. Mid-conversation tool changes are the tools counterpart to mid-conversation system messages. Instead of fixing the tool list for the lifetime of the conversation, you change which tools are offered to the model between turns: declare the full tool set in `tools` up front, then use `tool_addition` and `tool_removal` blocks to offer a tool to the model, or withdraw it, from a specific point in the conversation onward. The `tools` array itself never changes, so the cached prefix stays intact. Mid-conversation tool changes are in beta and use the `inline-tools-2026-09-15` beta header on the Claude API.

`tool_addition` and `tool_removal` are content blocks in the `content` array of a `role: "system"` message, and they can be mixed with `text` blocks in the same message. The message follows the placement rules for any mid-conversation system message, with one extra restriction after a paused turn (see [Limitations](#limitations)), and the change applies from that point in the conversation onward. Each block's `tool` field references a tool rather than defining one: `{"type": "tool_reference", "name": "..."}` names a tool declared in the request's `tools` array, and [MCP connector](/docs/en/agents-and-tools/mcp-connector) tools can be referenced individually with `mcp_tool_reference` (`server_name` and `name`) or as a whole toolset with `mcp_toolset_reference` (`server_name`). Referencing a name that is not declared in `tools` returns a 400 error (on the Claude API, with `error.details.error_code` set to `tool_reference_unresolved`). A `tool_addition` block can instead [carry the tool's full definition](#define-tools-in-a-message-beta), which the `mid-conversation-tool-changes-2026-07-01` header doesn't support.

Every tool declared in `tools` is offered to the model from the start of the conversation unless it is declared with `defer_loading: true`, which keeps it withheld until a `tool_addition` block surfaces it. `tool_addition` also re-offers a tool that an earlier `tool_removal` withdrew.

The following request declares `get_weather` in `tools`, then withdraws it after the first user turn with a `tool_removal` block. The request sends the `inline-tools-2026-09-15` beta header.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    betas=["inline-tools-2026-09-15"],
    # The full tool set is declared up front and never changes, so the
    # cached prefix stays intact.
    tools=[
        {
            "name": "get_weather",
            "description": "Get the current weather for a location.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"},
                },
                "required": ["location"],
            },
        },
    ],
    messages=[
        {
            "role": "user",
            "content": "Say OK.",
        },
        # Withdraw get_weather from this point onward. The block references
        # the tool by name instead of editing `tools`, so earlier turns stay
        # byte-identical and the cache still hits.
        {
            "role": "system",
            "content": [
                {
                    "type": "tool_removal",
                    "tool": {"type": "tool_reference", "name": "get_weather"},
                },
            ],
        },
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
```

### Define tools in a message (beta)

With the `inline-tools-2026-09-15` beta header, a `tool_addition` block can define a tool by value, carrying its full definition, instead of naming it by reference. This lets you introduce a tool that is unknown at the start of the conversation, or whose schema changes later, by appending a `role: "system"` message. The `tools` array and every earlier message stay exactly as sent, so the prompt cache still hits and only the appended message is processed as new input. The one exception, a `tools` array with no non-deferred tool, is covered in the rules below. The header also covers adding and removing tools by reference, so you don't need to send `mid-conversation-tool-changes-2026-07-01` as well.

Wrap the definition in a `tool` object of type `tool_definition`. The `definition` is a `tools` entry, such as a custom tool or an Anthropic-defined client or server tool, with its usual configuration, including `cache_control` and `defer_loading`. During the beta, some tool types (the computer use tool among them) can't be defined in a message yet and return a 400 error that says so; declare those in `tools` and add them by reference. For example, to define a custom tool mid-conversation:

```python
{
  "role": "system",
  "content": [
    {
      "type": "tool_addition",
      "tool": {
        "type": "tool_definition",
        "definition": {
          "name": "db_query",
          "description": "Run a read-only SQL query against the analytics database.",
          "input_schema": {
            "type": "object",
            "properties": { "sql": { "type": "string" } },
            "required": ["sql"]
          }
        }
      }
    }
  ]
}
```



From that position onward, the model can call the tool the same way it calls a tool declared in `tools`. Sending an identical definition again changes nothing, so a client can safely resend it, for example on a retry.

The following request keeps `get_weather` in `tools` and defines `db_query` after the first user turn:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    betas=["inline-tools-2026-09-15"],
    # Keep at least one non-deferred tool in `tools`, so a tool defined
    # later doesn't change the start of the rendered prompt.
    tools=[
        {
            "name": "get_weather",
            "description": "Get the current weather for a location.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"},
                },
                "required": ["location"],
            },
        },
    ],
    messages=[
        {"role": "user", "content": "How many orders shipped yesterday?"},
        # Define db_query by value from this point onward. `tools` and the
        # earlier messages stay exactly as sent, so the cache still hits.
        {
            "role": "system",
            "content": [
                {
                    "type": "tool_addition",
                    "tool": {
                        "type": "tool_definition",
                        "definition": {
                            "name": "db_query",
                            "description": "Run a read-only SQL query against the analytics database.",
                            "input_schema": {
                                "type": "object",
                                "properties": {"sql": {"type": "string"}},
                                "required": ["sql"],
                            },
                        },
                    },
                },
            ],
        },
    ],
)

for block in response.content:
    if block.type == "tool_use":
        print(block.name, block.input)
```

The response's `content` includes a `tool_use` block for the new tool, for example:

```python
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835lq9",
  "name": "db_query",
  "input": {
    "sql": "SELECT COUNT(*) FROM orders WHERE shipped_at::date = CURRENT_DATE - 1"
  }
}
```



To change a tool's schema, or to move a server tool to a newer version, send a different definition under the same name. The new definition replaces the earlier one from that position onward. A definition that reuses the name of a different type of tool returns a 400 error with `error.details.error_code` set to `tool_name_conflict`. A newer version of the same tool doesn't count as a different type. `tool_removal` still takes a reference, and a removed tool can be defined or re-offered again later.

A few rules follow from where the definition renders:

- **Declare what you know up front.** A tool you know about at the first request belongs in `tools`, with `defer_loading: true` and a later `tool_addition` reference if the model shouldn't see it yet. Define by value only what is unknown at the first request or changes later.
- **Keep at least one non-deferred tool in `tools`.** A conversation whose `tools` array has no non-deferred tool is accepted, but the first tool it defines by value changes the start of the rendered prompt, which costs one full cache miss on that request. A [tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool) counts as non-deferred.
- **Dated tool types keep their own beta headers.** If a server tool you define by value requires its own beta header, send that header on every later request in the conversation.
- **`cache_control` goes on the block or in the definition, not both,** and counts toward the request's breakpoint limit. A deferred definition can't carry `cache_control`.

A request returns a 400 error with `error.details.error_code` set to `available_tools_limit_exceeded` when any of these limits is exceeded:

- More than 10,000 deferred tools are available after any message.
- More than 10,000 tools defined after the first user message are available after any message.
- The tool definitions sent after the first user message that are still available after any message total more than 4 MB (4,194,304 bytes).
- The rendered tool text is larger than 4 MB (4,194,304 bytes).

### Add an MCP server mid-conversation (beta)

To add an [MCP connector](/docs/en/agents-and-tools/mcp-connector) server partway through a conversation, send the `mcp-client-2026-09-15` beta header along with `inline-tools-2026-09-15`. The `definition` in a `tool_addition` block can then be an `mcp_toolset`, so the server's tools become available without editing `tools`. List the server's connection details in `mcp_servers` as usual, then append the toolset where the server became available:

```python
{
  "role": "system",
  "content": [
    {
      "type": "tool_addition",
      "tool": {
        "type": "tool_definition",
        "definition": { "type": "mcp_toolset", "mcp_server_name": "calendar" }
      }
    }
  ]
}
```



The `mcp_toolset` object is the same one you would put in `tools`, including `default_config` and `configs`. A `tool_addition` block never holds a server URL or token. Those stay in `mcp_servers`.

The following request keeps `get_weather` in `tools`, lists the calendar server in `mcp_servers`, and adds the server's toolset after the first user turn:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    betas=["inline-tools-2026-09-15", "mcp-client-2026-09-15"],
    mcp_servers=[
        {
            "type": "url",
            "url": "https://mcp.example.com/calendar",
            "name": "calendar",
            "authorization_token": "YOUR_TOKEN",
        },
    ],
    tools=[
        {
            "name": "get_weather",
            "description": "Get the current weather for a location.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"},
                },
                "required": ["location"],
            },
        },
    ],
    messages=[
        {"role": "user", "content": "What's on my calendar tomorrow?"},
        # Make the calendar server's tools available from this point onward.
        # The block names the server; it never holds a URL or token.
        {
            "role": "system",
            "content": [
                {
                    "type": "tool_addition",
                    "tool": {
                        "type": "tool_definition",
                        "definition": {
                            "type": "mcp_toolset",
                            "mcp_server_name": "calendar",
                        },
                    },
                },
            ],
        },
    ],
)

# The response starts with an mcp_tool_listing block for the calendar server,
# so check each block's type instead of reading content[0].
for block in response.content:
    match block.type:
        case "mcp_tool_listing":
            print(block.mcp_server_name, [tool.name for tool in block.tools])
        case "text":
            print(block.text)
```

With `mcp-client-2026-09-15`, a response for which the API fetched a server's tool list starts with an `mcp_tool_listing` block, one for each server it fetched. If your code reads `content[0]`, skip these blocks. Send the assistant message back unchanged, this block included, and keep sending `mcp-client-2026-09-15` on every request that carries it. Later requests then use the recorded list instead of asking the server again. To pin a toolset yourself, copy that list into the `mcp_toolset`'s `tools` field, as described in [Pin an MCP server's tool list](/docs/en/agents-and-tools/mcp-connector#pin-mcp-tool-list).

`mcp-client-2026-09-15` includes everything `mcp-client-2025-11-20` does, so you don't need to send both. These features are available on the Claude API. Requests that use the MCP connector keep its [data retention](/docs/en/agents-and-tools/mcp-connector#data-retention) terms.

## When to use a mid-conversation system message

[Prompt caching](/docs/en/build-with-claude/prompt-caching) hashes the request prefix in order: `tools`, then `system`, then `messages`. A cache hit requires the prefix to match a recent request exactly, byte for byte, up to the cache breakpoint.

That ordering means the top-level `system` field sits near the very start of the hashed prefix. Any change to it, even appending a sentence, produces a different hash, and the request misses the cache for the system prompt and every cached message after it.

Mid-conversation system messages let you add the instruction at the **end** of the message history instead. Everything before the new instruction is unchanged, so the existing cache entry still matches, and only the new message is processed as fresh input.

A few situations where this matters:

- **Mid-session policy or persona changes.** A long agentic session needs a new constraint ("from now on, write all SQL as parameterized queries") after dozens of cached turns. Adding it to the top-level `system` field would re-process the entire history.
- **Per-turn context that must be authoritative.** You want to inject a freshness note, a session deadline, or a tool-availability change with system-level weight, and it changes too often to live in the cached prefix.
- **Per-turn reminders that shouldn't pile up.** A harness nudges the model after each batch of tool results ("request independent reads together", "the user hasn't heard from you in a while") and wants the model to see only the newest copy. A [turn-scoped system message](#turn-scoped-system-messages) renders for one turn and then costs nothing, without deleting anything from the history.
- **State changes your application observes.** Your application notices something Claude should treat as an operator-level fact: files changed on disk, the user toggled an auto-approve setting, available tools changed, or the remaining token budget dropped below a threshold.
- **User input that should not interrupt an agentic loop.** A user types a follow-up while Claude is still executing tools for the previous request. Relaying it as a system message after the next tool result lets Claude fold the new input into the work it is already doing, instead of treating it as a fresh request to switch to. See [Placement after tool results](#placement-after-tool-results).
- **Mode switches that grant standing permissions.** A session-level mode can use a mid-conversation system message to grant standing consent to an expensive capability, such as automatically launching multiagent workflows, with a short refresher every several turns and an exit notice when the mode is turned off. For a worked example, see [Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example).

In all of these cases you could put the instruction in a regular `user` message, and Claude does follow instructions that arrive in user turns. The difference is priority: a `user` message is treated as coming from the end user, while a `system` message is treated as coming from you, the application operator. When the two conflict, system instructions take precedence, so use the `system` role for operator-level facts and constraints that should hold even if the end user asks for something different. A mid-conversation system message keeps that operator-level priority without paying the cache-miss cost of editing the top-level `system` field.

## How it works

Add a message with `"role": "system"` to the `messages` array. Use a plain string or content blocks for `content`, the same as a `user` or `assistant` turn. The instruction applies from that point in the conversation onward. When instructions conflict, later system messages take precedence over earlier ones, and mid-conversation system messages take precedence over the top-level `system` field for the turns that follow them.

You can still set the top-level `system` field for instructions that should apply to the entire conversation. Reserve mid-conversation system messages for instructions that only become relevant later, or that you want to add without invalidating the cached prefix.

A `role: "system"` message can also carry `output_config.effort` to change the [effort](/docs/en/build-with-claude/effort) level from the next `user` turn on. This is in beta on Claude Fable 5.1, Claude Mythos 5.1, Claude Opus 5.5, and Claude Opus 5 on the Claude API and Google Cloud, and requires the `mid-conversation-output-config-2026-07-01` beta header. See [Per-message effort](/docs/en/build-with-claude/effort#change-effort-mid-conversation-beta).

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    # Automatic prompt caching: each request caches the conversation so far,
    # and the next request reads the unchanged prefix from cache.
    cache_control={"type": "ephemeral"},
    system="You are a code review assistant. Be concise.",
    messages=[
        {
            "role": "user",
            "content": "Review process() in utils.py for performance issues.",
        },
        {
            "role": "assistant",
            "content": "The list comprehension is fine for small inputs. For large inputs, consider a generator to avoid materializing the full list.",
        },
        {
            "role": "user",
            "content": "Now review the calling code that invokes process().",
        },
        # The reviewer realizes mid-session that all suggestions must
        # also pass the team's strict typing policy. Appending the
        # instruction here keeps earlier turns byte-identical, so the
        # prefix cached by the previous request is still read from cache.
        {
            "role": "system",
            "content": "From now on, every suggestion must include explicit type annotations.",
        },
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
```

This example enables [automatic caching](/docs/en/build-with-claude/prompt-caching#automatic-caching) with the top-level `cache_control` field. Prompt caching is opt-in: if a request has no `cache_control` field (automatic or an [explicit breakpoint](/docs/en/build-with-claude/prompt-caching#explicit-cache-breakpoints)), nothing is cached and every request pays the regular input token price for the full conversation. With caching enabled, appending the system message leaves the already-cached turns unchanged, so the request that carries the new instruction still reads them from cache instead of processing them again. Caching also requires the conversation to meet the [minimum cacheable prompt length](/docs/en/build-with-claude/prompt-caching#cache-limitations); an example as short as this one falls below it, so `cache_creation_input_tokens` and `cache_read_input_tokens` stay at 0 until the conversation grows.

A mid-conversation system message must immediately follow a `user` turn (or an `assistant` turn ending in a server tool result), and must either be the last entry in `messages` or be immediately followed by an `assistant` turn. A `user` message that carries `tool_result` blocks counts: in an agentic loop you can place the system message right after the tool results, before Claude's next turn. Any other position, including between an `assistant` `tool_use` block and the `tool_result` that answers it, returns a 400 error.

### Placement after tool results

In an [agentic loop](/docs/en/agents-and-tools/tool-use/overview), the system message goes after the `user` message that delivers the tool results. This is also where your application can relay input that the user typed while Claude was working, so the new context is absorbed without restarting the turn:

```python
[
  { "role": "user", "content": "Run the test suite and fix any failures." },
  {
    "role": "assistant",
    "content": [{ "type": "tool_use", "id": "toolu_01", "name": "run_tests", "input": {} }]
  },
  {
    "role": "user",
    "content": [
      { "type": "tool_result", "tool_use_id": "toolu_01", "content": "12 passed, 0 failed" }
    ]
  },
  {
    "role": "system",
    "content": "The user sent the following message while you were working: also update the changelog before you finish."
  }
]
```



Phrase the system content as context rather than as a command that overrides the user. State the fact ("new input arrived from the user: X", "the remaining token budget is now Y") and let Claude act on it. Claude is trained to resist instructions that appear to work against the user, and that protection still applies to the system role, so language such as "ignore what the user said" is less effective than stating what changed.

This pattern is for relaying input from the conversation's own end user. Do not use it to pass tool output, retrieved documents, or other third-party content; keep that content in `tool_result` blocks (see [Limitations](#limitations)).

### Turn-scoped system messages

To scope a `role: "system"` message to the current turn, set its `clear_at` field. It takes one of two values:

- `"never"` (the default): the message renders at its position on every request that includes it. Omitting the field is identical.
- `"next_user_message"`: the message is **turn-scoped**. Its text renders only while no `role: "user"` message comes after it in `messages`. A user message that carries only `tool_result` blocks counts as a user message here. Once a later user message exists, the message is **cleared**: it stays in the array but renders nothing and costs no input tokens, on that request and every later one.

Turn-scoped system messages are in beta. Include the [beta header](/docs/en/api/beta-headers) `mid-conversation-system-clear-at-2026-08-21`. Without it, `clear_at` is rejected as an unknown field.

```python
{
  "role": "system",
  "clear_at": "next_user_message",
  "content": "First privately list what you need next; then request every item that doesn't depend on another's result in this one response."
}
```



The main use is a per-turn reminder in a tool loop. Append the reminder after the `tool_result` message each time you want the model to see it, and leave every earlier copy where it is. The model sees only the copies that come after the last user message, so the reminder never piles up. Nothing earlier in `messages` changes, so the [prompt cache](/docs/en/build-with-claude/prompt-caching) keeps matching. On Claude Fable 5.1 and Claude Opus 5.5 this also keeps later [thinking blocks valid](/docs/en/build-with-claude/thinking#preserved-in-conversation): deleting an earlier reminder would change the conversation before those blocks and fail the conversation check, while a cleared message stays in the array and leaves that conversation unchanged.

The following request is a later step of an agent loop. `messages[3]` rendered on the earlier request, when it was the last message in the array. Once `messages[5]` (a later user message) exists, `messages[3]` is cleared: the cleared message stays in the array, so the conversation before the thinking block in `messages[4]` is unchanged, but the model no longer sees its text. `messages[6]` and `messages[7]` both render, in order.

```python
{
  "model": "claude-fable-5-1",
  "max_tokens": 16000,
  "messages": [
    { "role": "user", "content": "Fix the failing test." },
    {
      "role": "assistant",
      "content": [
        { "type": "thinking", "thinking": "", "signature": "..." },
        {
          "type": "tool_use",
          "id": "toolu_01",
          "name": "read_file",
          "input": { "path": "test_auth.py" }
        }
      ]
    },
    {
      "role": "user",
      "content": [{ "type": "tool_result", "tool_use_id": "toolu_01", "content": "..." }]
    },
    {
      "role": "system",
      "clear_at": "next_user_message",
      "content": "Request independent reads in one turn."
    },
    {
      "role": "assistant",
      "content": [
        { "type": "thinking", "thinking": "", "signature": "..." },
        {
          "type": "tool_use",
          "id": "toolu_02",
          "name": "read_file",
          "input": { "path": "auth.py" }
        },
        {
          "type": "tool_use",
          "id": "toolu_03",
          "name": "read_file",
          "input": { "path": "tokens.py" }
        }
      ]
    },
    {
      "role": "user",
      "content": [
        { "type": "tool_result", "tool_use_id": "toolu_02", "content": "..." },
        {
          "type": "tool_result",
          "tool_use_id": "toolu_03",
          "content": "...",
          "cache_control": { "type": "ephemeral" }
        }
      ]
    },
    {
      "role": "system",
      "clear_at": "next_user_message",
      "content": "Request independent reads in one turn."
    },
    {
      "role": "system",
      "clear_at": "next_user_message",
      "content": "The shell exited with status 137."
    }
  ]
}
```



Rules for turn-scoped messages:

- **Re-send cleared messages verbatim.** A cleared message is still part of the conversation history. Rebuilding it from current state (a fresh token count, a timestamp), dropping it as redundant, or changing its `clear_at` value is an edit to an earlier message. The prompt cache misses from that point, and on Claude Fable 5.1 and Claude Opus 5.5 every thinking block produced after it fails the [conversation check](/docs/en/build-with-claude/thinking#preserved-in-conversation).
- **Text only.** `content` is one or more `text` blocks (or a string). `tool_addition` and `tool_removal` blocks return a 400 error on a turn-scoped message, and so does `output_config`. Use a separate `role: "system"` message without `clear_at` for those.
- **No `cache_control` on its blocks.** A cleared message is never part of a cache key, so a breakpoint on it could never match. Put the breakpoint on the last block of the preceding user turn instead, as the example does. The top-level [automatic caching](/docs/en/build-with-claude/prompt-caching#automatic-caching) field skips turn-scoped messages when it picks a breakpoint. On the request that clears a message, the reusable cached prefix ends at the user turn before it, so only the one assistant turn between that message and the new user message is reprocessed.
- **Placement rules still apply**, cleared or not. A turn-scoped message must follow a `user` turn (or an `assistant` turn ending in a server tool result) and precede an `assistant` turn or end the array, like any mid-conversation system message. One that ends the array always renders. One followed directly by another `user` message is a 400 error, not a cleared message: put all of a tool round's results in one user message and the reminders after it.
- **Assistant turns don't clear it.** A prefilled or [paused](/docs/en/build-with-claude/handling-stop-reasons#pause-turn) assistant turn after the message, or a server-side tool loop, adds no user message, so the message still renders on that continuation. To keep a reminder in view through a client-side tool loop, append it again after each `tool_result` message.
- **Token counting follows what renders.** A cleared message adds nothing to `usage.input_tokens` or to a [token count](/docs/en/build-with-claude/token-counting).
- **Imported history.** In a transcript you construct in one step (few-shot examples, a migrated conversation), a turn-scoped message that already has an assistant turn and a user message after it is cleared from the first request and never renders. That is the right state for a per-turn reminder you are carrying over. Leave `clear_at` unset only on a message the model should see on every request.

The validation errors are:

```python
messages.3.clear_at: Extra inputs are not permitted
messages.3.clear_at: clear_at is only permitted on role 'system' messages
messages.3.clear_at: Input should be 'next_user_message' or 'never'
messages.3: a turn-scoped system message supports text blocks only (clear_at: 'next_user_message')
messages.3: output_config is not permitted on a turn-scoped system message (clear_at: 'next_user_message')
messages.3.content.0: cache_control is not permitted on a turn-scoped system message (clear_at: 'next_user_message')
```



The first is the error returned without the beta header. On Amazon Bedrock and Google Cloud, pass the beta value as described in [Beta headers](/docs/en/api/beta-headers).

Through the SDKs, set `clear_at` on the `role: "system"` entry in `messages` and send the beta header. The following example appends a turn-scoped reminder after the user turn; on the next request, once a later user message exists, the reminder stays in the array but no longer renders:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-fable-5-1",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "Draft a short status update on the database migration for the team channel.",
        },
        # Turn-scoped reminder: renders for this turn, then clears once a later user message exists.
        {
            "role": "system",
            "clear_at": "next_user_message",
            "content": "The reader is on call: keep this reply under 50 words.",
        },
    ],
    betas=["mid-conversation-system-clear-at-2026-08-21"],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
```

## Combining with prompt caching

Mid-conversation system messages and [prompt caching](/docs/en/build-with-claude/prompt-caching) are designed to be used together:

- **Enable caching explicitly.** Caching only happens when the request includes `cache_control`, either the top-level [automatic caching](/docs/en/build-with-claude/prompt-caching#automatic-caching) field or an [explicit breakpoint](/docs/en/build-with-claude/prompt-caching#explicit-cache-breakpoints) on a content block. A mid-conversation system message does not create a cache entry on its own, and without caching enabled there are no savings to preserve.
- **Cache the stable prefix as usual.** Place `cache_control` on the last block that stays the same across requests, whether that is the end of the top-level `system` field, the end of your tool definitions, or a stable point in the message history.
- **Append the system message after the breakpoint.** Because it comes after the cached prefix, it does not change the prefix hash and the cache still hits.
- **A mid-conversation system message is itself cacheable.** Once it is in the conversation, it becomes part of the stable history. On the next turn you can move your cache breakpoint past it (or rely on [automatic caching](/docs/en/build-with-claude/prompt-caching#automatic-caching) to do so) and the system message is read from cache like any other turn.

Avoid editing or removing a mid-conversation system message that has already been sent. Like any other change to earlier messages, that invalidates the cache from that point forward. On Claude Fable 5.1 and Claude Opus 5.5 it also invalidates the [thinking blocks](/docs/en/build-with-claude/thinking#preserved-in-conversation) in every later assistant turn. For guidance that should apply to one turn only, use a [turn-scoped system message](#turn-scoped-system-messages) and leave it in place. If the instruction needs to evolve, append a new system message rather than rewriting the old one. Consecutive system messages are accepted and treated as a single system section, which follows the same placement rule as a whole.

## Limitations

- **Not for the first message.** A `system` message that carries content cannot be the first entry in `messages`. Use the top-level `system` field for instructions that apply from the very start.
- **Placement is constrained.** A `system` message that carries content (`text`, `tool_addition`, or `tool_removal` blocks) must immediately follow a `user` turn (including a `user` turn that carries `tool_result` blocks) or an `assistant` turn ending in a server tool result, and must precede an `assistant` turn or end the array. It cannot sit between a `tool_use` block and its `tool_result`. Placing it elsewhere returns a 400 error. One exception: `tool_addition` and `tool_removal` blocks are not accepted immediately after a [paused](/docs/en/build-with-claude/handling-stop-reasons#pause-turn) `assistant` turn (one ending in a server tool result), though `text` blocks are; resume the paused turn first, then send the tool change in the next `system` message. A message with empty `content` that only sets [`output_config.effort`](/docs/en/build-with-claude/effort#change-effort-mid-conversation-beta) renders nothing at its position and is accepted anywhere in `messages`, including first or between an `assistant` turn and a `user` turn. Consecutive `system` messages are judged together, so adding a text-carrying message next to an effort-only one makes the whole group follow the content rule.
- **Turn-scoped messages are text-only and re-sent verbatim.** A `clear_at: "next_user_message"` message carries no `tool_addition`, `tool_removal`, `output_config`, or `cache_control`, and once cleared it must stay in `messages` byte-for-byte on later requests. See [Turn-scoped system messages](#turn-scoped-system-messages).
- **Not a place for untrusted content.** Claude treats system content as operator instructions and follows it. Do not place text from outside the conversation, such as raw tool output, retrieved documents, or web content, directly in a system message; doing so gives that text operator-level authority. Keep that data in `tool_result` blocks and continue to follow [Mitigate jailbreaks and prompt injections](/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks).

## Related



[Prompt caching](/docs/en/build-with-claude/prompt-caching)

How caching works, where to place breakpoints, and how to read cache usage fields.



[Cache diagnostics](/docs/en/build-with-claude/cache-diagnostics)

Find out exactly where two requests diverged when a cache hit you expected does not happen.



[Using the Messages API](/docs/en/build-with-claude/working-with-messages)

Message structure, multi-turn conversations, and the `system` field.



[Prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)

Writing effective prompts and system instructions.



[Tool use with Claude](/docs/en/agents-and-tools/tool-use/overview)

How `tool_use` and `tool_result` blocks are structured in the `messages` array.
