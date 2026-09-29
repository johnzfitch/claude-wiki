---
title: "Tool search tool - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:23Z"
tags: ["api", "mcp", "prompting", "search"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Ftool-use%2Ftool-search-tool)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](../Other/get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](../Other/manage-claude-authentication.md)

Building with Claude

[Features overview](../Guides/build-with-claude-overview.md)[Using the Messages API](../Guides/build-with-claude-working-with-messages.md)[Stop reasons and fallback](../Guides/build-with-claude-handling-stop-reasons.md)[Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md)[Fallback credit](../Guides/build-with-claude-fallback-credit.md)

Model capabilities

[Effort](../Guides/build-with-claude-effort.md)[Task budgets (beta)](../Guides/build-with-claude-task-budgets.md)[Fast mode (research preview)](../Guides/build-with-claude-fast-mode.md)[Structured outputs](../Guides/build-with-claude-structured-outputs.md)[Citations](../Guides/build-with-claude-citations.md)[Streaming Messages](../Guides/build-with-claude-streaming.md)[Batch processing](../Guides/build-with-claude-batch-processing.md)[Search results](../Guides/build-with-claude-search-results.md)[Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](../Guides/build-with-claude-multilingual-support.md)[Embeddings](../Guides/build-with-claude-embeddings.md)

[Thinking](../Guides/build-with-claude-thinking.md)

Tools

[Overview](agents-and-tools-tool-use-overview.md)[How tool use works](agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](agents-and-tools-tool-use-tool-runner.md)[Strict tool use](agents-and-tools-tool-use-strict-tool-use.md)[Server tools](agents-and-tools-tool-use-server-tools.md)[Web search tool](agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](agents-and-tools-tool-use-memory-tool.md)[Bash tool](agents-and-tools-tool-use-bash-tool.md)[Text editor tool](agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](agents-and-tools-tool-use-tool-reference.md)[Manage tool context](agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](../Guides/build-with-claude-context-windows.md)[Context editing](../Guides/build-with-claude-context-editing.md)[Prompt caching](../Guides/build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](../Guides/build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](../Guides/build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](../Guides/build-with-claude-cache-diagnostics.md)[Token counting](../Guides/build-with-claude-token-counting.md)

[Compaction](../Guides/build-with-claude-compaction.md)

Working with files

[Files API](../Guides/build-with-claude-files.md)[PDF support](../Guides/build-with-claude-pdf-support.md)

[Images and vision](../Guides/build-with-claude-vision.md)

Skills

[Overview](agents-and-tools-agent-skills-overview.md)[Quickstart](agents-and-tools-agent-skills-quickstart.md)[Best practices](agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](agents-and-tools-agent-skills-enterprise.md)[Skills in the API](../Guides/build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](agents-and-tools-remote-mcp-servers.md)[MCP connector](agents-and-tools-mcp-connector.md)

[MCP tunnels](agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](../Guides/build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](../Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)[Google Cloud](../Guides/build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md)

[Console](../Other/usage-limits.md)

[Messages](../../01-Getting-Started/intro.md)Tools

# Tool search tool

Copy page



Scale to hundreds or thousands of tools by letting Claude search your tool catalog and load only the tools it needs.

Copy page



The tool search tool lets Claude work with hundreds or thousands of tools by discovering and loading them on demand. Instead of loading all tool definitions into the context window up front, Claude searches your tool catalog (including tool names, descriptions, argument names, and argument descriptions) and loads only the tools it needs.

Loading every tool definition up front causes two problems as a tool library grows:

- **Context bloat:** A typical multiserver setup (GitHub, Slack, Sentry, Grafana, and Splunk) can consume ~55k tokens in definitions before Claude does any work. Tool search typically reduces this by over 85 percent, loading only the 3–5 tools Claude needs for a given request.
- **Tool selection accuracy:** Claude's ability to pick the right tool degrades once you exceed 30–50 available tools. Because tool search loads only a focused set of relevant tools on demand, selection accuracy stays high even across thousands of tools.

For the models that support tool search, see [Model compatibility](#model-compatibility).



For background on the scaling challenges that tool search solves, see [Advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use). Tool search's on-demand loading is also an instance of the broader just-in-time retrieval principle described in [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).

Tool search runs as a server-side tool, but you can also implement your own client-side tool search. See [Custom tool search implementation](#custom-tool-search-implementation) for details.



Share feedback on this feature through the [feedback form](https://forms.gle/MhcGFFwLxuwnWTkYA).



To learn how zero data retention (ZDR) applies to this feature, see [API and data retention](../Other/manage-claude-api-and-data-retention.md).



On Amazon Bedrock, server-side tool search is available only through the [InvokeModel API](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModel_AnthropicClaude_section.html), not the Converse API.



On [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md), server-side tool search works identically to the Claude API. Claude Platform on AWS uses the Anthropic Messages API directly, so there is no InvokeModel or Converse distinction.

## Model compatibility

Both tool search variants are available on the following models:

[TABLE]

Claude Opus 4.1 and earlier models don't support the tool search tool.

## How tool search works

There are two tool search variants:

- **Regex** (`tool_search_tool_regex_20251119`): Claude constructs regex patterns to search for tools.
- **BM25** (`tool_search_tool_bm25_20251119`): Claude uses natural language queries to search for tools.

When you enable the tool search tool:

1.  You include a tool search tool (for example, `tool_search_tool_regex_20251119` or `tool_search_tool_bm25_20251119`) in your `tools` list.
2.  You provide every tool definition in the `tools` array and set `defer_loading: true` on the tools that shouldn't load up front. At least one tool, normally the tool search tool itself, must stay non-deferred.
3.  Initially, Claude's context contains only the tool search tool and any non-deferred tools.
4.  When Claude needs additional tools, it searches using a tool search tool.
5.  The API runs the search and returns the matching tools as `tool_reference` blocks (up to 5 by default; Claude can set a `limit` in its search input).
6.  The API automatically expands these references into full tool definitions.
7.  Claude selects from the discovered tools and calls them.

## Quick start

The following example includes the tool search tool and two deferred tools:

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
    max_tokens=2048,
    messages=[{"role": "user", "content": "What is the weather in San Francisco?"}],
    tools=[
        {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},
        {
            "name": "get_weather",
            "description": "Get the weather at a specific location",
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
            "defer_loading": True,
        },
        {
            "name": "search_files",
            "description": "Search through files in the workspace",
            "input_schema": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "file_types": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["query"],
            },
            "defer_loading": True,
        },
    ],
)

print(response)
```

Claude searches the catalog, discovers `get_weather`, and calls it. The response ends with `stop_reason: "tool_use"`. Execute the discovered tool and return a `tool_result` as in [Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md). [Response format](#response-format) shows the blocks you get back and what to send next.

## Tool definition

The tool search tool has two variants:

JSON



```python
{
  "type": "tool_search_tool_regex_20251119",
  "name": "tool_search_tool_regex"
}
```

JSON



```python
{
  "type": "tool_search_tool_bm25_20251119",
  "name": "tool_search_tool_bm25"
}
```



**Regex variant query format: Python regex, not natural language**

With `tool_search_tool_regex_20251119`, Claude writes Python `re.search()` patterns, not natural language queries. Matching is case-insensitive. Common patterns include the following:

- `"weather"`: matches tool names and descriptions containing "weather"
- `"get_.*_data"`: matches tools such as `get_user_data` and `get_weather_data`
- `"database.*query|query.*database"`: matches either word order

Maximum pattern length: 200 characters



**BM25 variant query format: natural language**

With `tool_search_tool_bm25_20251119`, Claude searches with natural language queries. Maximum query length: 500 characters.

### Deferred tool loading

Mark tools for on-demand loading by adding `defer_loading: true`:

JSON



```python
{
  "name": "get_weather",
  "description": "Get current weather for a location",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": { "type": "string" },
      "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] }
    },
    "required": ["location"]
  },
  "defer_loading": true
}
```

`defer_loading` controls what enters the context window, not what you send in the request:

- You still send every tool's full definition in the `tools` array on every request, including the deferred ones. The API needs them server-side to run the search and expand `tool_reference` blocks.
- Tools without `defer_loading` load into context immediately.
- Tools with `defer_loading: true` load only when Claude discovers them through search.
- Never set `defer_loading: true` on the tool search tool itself.
- Keep your 3–5 most frequently used tools non-deferred so Claude can call them without searching first.

The computer use and browser use toolsets (`computer_toolset_20260801` and `browser_toolset_20260801`) take `defer_loading` per member tool inside the entry's `configs` object, not on the entry itself; a request that sets it at the entry level is rejected. Because a toolset defers and expands as a unit, `defer_loading` must resolve to the same value on every enabled member, and when Claude discovers the toolset through search, every enabled member loads at once. See [Client toolsets](agents-and-tools-tool-use-tool-reference.md#client-toolsets) for the `configs` format.

Both tool search variants (`regex` and `bm25`) search tool names, descriptions, argument names, and argument descriptions.

Internally, the API excludes deferred tools from the system-prompt prefix. When Claude discovers a deferred tool through tool search, the API appends a `tool_reference` block inline in the conversation, then expands it into the full tool definition before passing it to Claude. The prefix is untouched, so prompt caching is preserved. The grammar for [strict mode](agents-and-tools-tool-use-strict-tool-use.md) (the rules that constrain tool-call output to match your schemas) builds from the full toolset, so `defer_loading` and strict mode compose without grammar recompilation.

## Response format

When Claude uses the tool search tool, the response includes the following block types:

JSON



```python
{
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "I'll search for tools to help with the weather information."
    },
    {
      "type": "server_tool_use",
      "id": "srvtoolu_01ABC123",
      "name": "tool_search_tool_regex",
      "input": {
        "pattern": "weather",
        "limit": 10
      }
    },
    {
      "type": "tool_search_tool_result",
      "tool_use_id": "srvtoolu_01ABC123",
      "content": {
        "type": "tool_search_tool_search_result",
        "tool_references": [{ "type": "tool_reference", "tool_name": "get_weather" }]
      }
    },
    {
      "type": "text",
      "text": "I found a weather tool. Let me get the weather for San Francisco."
    },
    {
      "type": "tool_use",
      "id": "toolu_01XYZ789",
      "name": "get_weather",
      "input": { "location": "San Francisco", "unit": "fahrenheit" }
    }
  ],
  "stop_reason": "tool_use"
}
```

### Understanding the response

- **`server_tool_use`:** Claude's call to the tool search tool. The search runs on Anthropic's servers. Never return a `tool_result` for its `srvtoolu_...` ID. The `input` holds the search (`pattern` for the regex variant, `query` for BM25) and may include an optional `limit`, an integer from 1 to 10,000 that caps how many matching tools the search returns (default: 5).
- **`tool_search_tool_result`:** the search results, in a nested `tool_search_tool_search_result` object. Keep it in the message history as is.
- **`tool_references`:** an array of `tool_reference` objects pointing to discovered tools. The API expands these for Claude. You never expand them yourself.
- **`tool_use`:** Claude's call to a discovered tool. Execute it and return a `tool_result` exactly as in standard tool use.

The API automatically expands `tool_reference` blocks into full tool definitions before showing them to Claude. You don't need to handle this expansion yourself, as long as you provide all matching tool definitions in the `tools` parameter.

### Continuing the conversation

On the next request, pass the assistant's content back unchanged, including the `server_tool_use` and `tool_search_tool_result` blocks. Add your `tool_result` for the discovered tool in a user message, and send the same `tools` array: the search tool plus every deferred definition. Don't return a `tool_result` for the `srvtoolu_...` ID: the API rejects the request. The API expands `tool_reference` blocks throughout the conversation history, so Claude can reuse discovered tools in later turns without re-searching. A search that matches nothing returns a `tool_search_tool_search_result` with an empty `tool_references` array, not an error.

## MCP integration

If your tools come from MCP servers through the [MCP connector](agents-and-tools-mcp-connector.md), you don't set `defer_loading` on individual tool definitions. Instead, set it once on the `mcp_toolset` entry's `default_config` for the whole server, or per tool in its `configs`. See [MCP toolset configuration](agents-and-tools-mcp-connector.md#mcp-toolset-configuration).

## Custom tool search implementation

You can implement your own tool search logic (for example, using embeddings or semantic search) by returning `tool_reference` blocks from a custom tool. When Claude calls your custom search tool, return a standard `tool_result` with `tool_reference` blocks in the content array:

JSON



```python
{
  "type": "tool_result",
  "tool_use_id": "toolu_your_tool_id",
  "content": [{ "type": "tool_reference", "tool_name": "discovered_tool_name" }]
}
```

Every tool referenced must have a corresponding tool definition in the top-level `tools` parameter, normally with `defer_loading: true`. This lets you use search methods the built-in variants don't provide, such as embedding-based retrieval, and the API expands the returned `tool_reference` blocks the same way.



The `tool_search_tool_result` format shown in the [Response format](#response-format) section is the server-side format used internally by Anthropic's built-in tool search. For custom client-side implementations, always use the standard `tool_result` format with `tool_reference` content blocks as shown in the preceding example.

For a complete example using embeddings, see the [tool search with embeddings](https://platform.claude.com/cookbook/tool-use-tool-search-with-embeddings) recipe.

## Error handling



[Tool use examples](agents-and-tools-tool-use-implement-tool-use.md#providing-tool-use-examples) work with tool search: when Claude discovers a deferred tool, the API expands its `input_examples` along with its definition.

### HTTP errors (400 status)

These errors prevent the API from processing the request:

**All tools deferred:**

```python
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "At least one tool must have defer_loading=false. All tools cannot be deferred."
  }
}
```



**Missing tool definition:**

```python
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "Tool reference 'unknown_tool' not found in available tools"
  }
}
```



### Tool result errors (200 status)

When a tool search operation fails during execution, the API returns a 200 response with the error in the body:

JSON



```python
{
  "type": "tool_search_tool_result",
  "tool_use_id": "srvtoolu_01ABC123",
  "content": {
    "type": "tool_search_tool_result_error",
    "error_code": "invalid_tool_input",
    "error_message": "Invalid regular expression pattern: missing ) at position 1"
  }
}
```

The `error_code` field has four possible values:

- `invalid_tool_input`: the search input was invalid, for example a malformed regex pattern or a pattern over the 200-character limit
- `unavailable`: the search couldn't run, for example because it timed out or the service was unavailable
- `too_many_requests`: rate limit exceeded for tool search operations
- `execution_time_exceeded`: the search exceeded its execution time limit

### Common mistakes

### 400 error: all tools are deferred

**Cause:** You set `defer_loading: true` on every tool, including the tool search tool.

**Fix:** Remove `defer_loading` from the tool search tool:

```python
{
  "type": "tool_search_tool_regex_20251119",
  "name": "tool_search_tool_regex"
}
```



### 400 error: missing tool definition

**Cause:** A `tool_reference` points to a tool not in your `tools` array.

**Fix:** Ensure every tool that could be discovered has a complete definition:

```python
{
  "name": "my_tool",
  "description": "Full description here",
  "input_schema": {
    "type": "object"
  },
  "defer_loading": true
}
```



### Claude doesn't find expected tools

**Cause:** The regex pattern doesn't match the tool's name, description, argument names, or argument descriptions.

**Debugging steps:**

1.  Check tool name, description, argument names, and argument descriptions. Claude searches all of these fields.
2.  Test your pattern: `import re; re.search(r"your_pattern", "tool_name", re.IGNORECASE)`.
3.  Matching is case-insensitive, so casing differences aren't the problem.
4.  Claude uses broad patterns such as `".*weather.*"`, not exact matches.

**Tip:** Add common keywords to tool descriptions to improve discoverability.

## Prompt caching

To learn how `defer_loading` preserves prompt caching, see [Tool use with prompt caching](agents-and-tools-tool-use-tool-use-with-prompt-caching.md).

A tool with `defer_loading: true` can't also carry `cache_control`: the API returns a 400. Put the cache breakpoint on a non-deferred tool.

## Streaming

With streaming enabled, you'll receive tool search events as part of the stream:

```python
event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "tool_search_tool_regex"}}

// Search pattern streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"pattern\":\"weather\"}"}}

// Pause while search executes

// Search results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "tool_search_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": {"type": "tool_search_tool_search_result", "tool_references": [{"type": "tool_reference", "tool_name": "get_weather"}]}}}

// Claude continues with discovered tools
```



## Batch requests

You can include the tool search tool in the [Messages Batches API](../Guides/build-with-claude-batch-processing.md).

## Limits and best practices

### Limits

- **Maximum deferred tools:** 10,000 tools with `defer_loading: true` per request
- **Search results:** each search returns up to 5 matching tools by default; Claude can set `limit` in its search input to any integer from 1 to 10,000
- **Pattern and query length:** maximum 200 characters for regex patterns and 500 characters for BM25 queries
- **Model support:** see [Model compatibility](#model-compatibility)

### When to use tool search

Use tool search when any of the following apply:

- You have 10 or more tools available.
- Your tool definitions consume more than 10k tokens.
- Tool selection accuracy drops as your toolset grows.
- You aggregate multiple MCP servers (200+ tools).
- Your tool library grows over time.

Standard tool calling, without tool search, is a better fit when you have fewer than 10 tools, every tool is used in every request, or your tool definitions are small (less than 100 tokens total).

### Optimization tips

- Keep your 3–5 most frequently used tools non-deferred.
- Write clear, descriptive tool names and descriptions.
- Use consistent namespacing in tool names: prefix by service or resource (for example, `github_`, `slack_`) so one search matches the whole group.
- Use keywords in descriptions that match how users describe tasks.
- Add a system prompt section describing available tool categories: "You can search for tools to interact with Slack, GitHub, and Jira."
- Monitor which tools Claude discovers to refine your descriptions.

## Usage

Tool search isn't metered as a separate server tool. The response's `usage.server_tool_use` object has no tool search field, and the tool definitions that search loads into context count as input tokens like any other tool definition.

## Next steps



[Memory tool](agents-and-tools-tool-use-memory-tool.md)

Let Claude store and retrieve information across conversations by implementing the memory tool's file operations in your application.



[Tool reference](agents-and-tools-tool-use-tool-reference.md)

Directory of Anthropic-provided tools and reference for optional tool definition properties.



[MCP connector](agents-and-tools-mcp-connector.md)

Configure MCP toolsets with deferred loading.



[Tool use with prompt caching](agents-and-tools-tool-use-tool-use-with-prompt-caching.md)

Cache tool definitions across turns and understand what invalidates your cache.



[Define tools](agents-and-tools-tool-use-implement-tool-use.md)

Specify tool schemas, write effective descriptions, and control when Claude calls your tools.
