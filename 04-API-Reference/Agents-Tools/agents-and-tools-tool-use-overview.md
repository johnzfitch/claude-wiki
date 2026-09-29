---
title: "Tool use with Claude - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:26Z"
tags: ["api"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Ftool-use%2Foverview)

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

# Tool use with Claude

Copy page



Connect Claude to external tools and APIs. See where tools execute, when Claude calls them, and which tool fits your task.

Copy page



Tool use (also called function calling) lets Claude call functions that you define or that Anthropic provides. Claude determines when to call a tool based on the user's request and the tool's description. It then returns a structured call that your application executes (client tools) or that Anthropic executes (server tools).

Here's a minimal example using a server tool, the [Web search tool](agents-and-tools-tool-use-web-search-tool.md), which Anthropic executes for you:

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
    tools=[{"type": "web_search_20260209", "name": "web_search"}],
    messages=[{"role": "user", "content": "What's the latest on the Mars rover?"}],
)
print(response.content)
```

Claude runs the search on Anthropic's infrastructure and returns the cited results in the same response. To have Claude call a function that you define, pass a tool with an `input_schema`, then execute the call when Claude returns a `tool_use` block. [How tool use works](#how-tool-use-works) shows that round trip end to end. Learn more about [defining tools](agents-and-tools-tool-use-implement-tool-use.md) and [handling tool calls](agents-and-tools-tool-use-handle-tool-calls.md).

## How tool use works

Tools differ primarily by where the code executes. **Client tools** (including user-defined tools and tools with Anthropic-defined schemas, such as `bash` and `text_editor`) run in your application. Claude responds with `stop_reason: "tool_use"` and one or more `tool_use` blocks. Your code executes the operation and sends back a `tool_result`. **Server tools** (such as `web_search`, `web_fetch`, `code_execution`, and `tool_search`) run on Anthropic's infrastructure: you see the results directly without handling execution, unless Claude calls the tool in the same group of parallel tool calls as one of your client tools (see [Stop reasons and fallback](../Guides/build-with-claude-handling-stop-reasons.md#tool-use)).

Here's that round trip in full for a client tool. The first request defines a `get_weather` tool, and Claude answers the question by calling it: the response carries a `tool_use` block, your code runs the lookup, and a second request sends the result back in a `tool_result` block so Claude can reply with the answer.

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

tools = [
    {
        "name": "get_weather",
        "description": "Get the current weather for a given location.",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City and state, e.g. San Francisco, CA",
                }
            },
            "required": ["location"],
        },
    }
]
messages = [{"role": "user", "content": "What's the weather in San Francisco?"}]

# Claude replies with a tool_use block naming the tool and its arguments.
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    tools=tools,
    # Ask for at most one tool call per turn.
    tool_choice={"type": "auto", "disable_parallel_tool_use": True},
    messages=messages,
)
tool_use = next(block for block in response.content if block.type == "tool_use")
print(f"Claude called {tool_use.name} with {json.dumps(tool_use.input)}")

# Run the tool, then send the result back in a tool_result block.
weather = "15 degrees Celsius, partly cloudy"  # your weather lookup goes here
messages += [
    {"role": "assistant", "content": response.content},
    {
        "role": "user",
        "content": [
            {"type": "tool_result", "tool_use_id": tool_use.id, "content": weather}
        ],
    },
]
followup = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    tools=tools,
    tool_choice={"type": "auto", "disable_parallel_tool_use": True},
    messages=messages,
)

# Claude uses the result to answer the original question.
final_text = next(block for block in followup.content if block.type == "text")
print(final_text.text)
```

Output



``` block
Claude called get_weather with {"location": "San Francisco, CA"}
The current weather in San Francisco is 15 degrees Celsius with partly cloudy skies.
```

[Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md) covers each step in detail, including result formatting and error signaling; [Parallel tool use](agents-and-tools-tool-use-parallel-tool-use.md) covers responses that call several tools at once. To skip writing this round trip yourself, use [Tool Runner](agents-and-tools-tool-use-tool-runner.md): the SDKs execute your tools and send the results back automatically.

For the full conceptual model including the agentic loop and when to choose each approach, see [How tool use works](agents-and-tools-tool-use-how-tool-use-works.md).

To connect to Model Context Protocol (MCP) servers, see the [MCP connector](agents-and-tools-mcp-connector.md). To build your own MCP client, see the Model Context Protocol guide to [building an MCP client](../../06-MCP-Tools/Tutorials/develop-build-client.md).

## When Claude uses tools

With the default `tool_choice` of `{"type": "auto"}`, Claude determines on each turn whether to call a tool or respond directly. It calls a tool when the request maps to that tool's described capability and the answer isn't already in context. It responds directly for stable knowledge, creative tasks, and conversational turns.

This boundary is steerable through your system prompt. If Claude isn't calling tools when you expect, a light instruction such as `"Use the tools to investigate before responding."` increases tool use. A stronger form such as `"Always call a tool first before responding."` pushes further. Conversely, `"Use your judgment about whether to call a tool or respond directly."` keeps triggering behavior conservative.

To require a tool call rather than rely on prompting, set [`tool_choice`](agents-and-tools-tool-use-implement-tool-use.md#forcing-tool-use).



**Guarantee schema conformance with strict tool use**

Add `strict: true` to your custom tool definitions to ensure Claude's tool calls always match your schema exactly. See [Strict tool use](agents-and-tools-tool-use-strict-tool-use.md).

Each server tool's page describes its own trigger boundary in more detail.

### When required parameters are missing

If the user's prompt doesn't include enough information to fill all the required parameters for a tool, Claude Opus is much more likely to recognize that a parameter is missing and ask for it. Claude Sonnet might ask, especially when prompted to think before outputting a tool request. But it might also infer a reasonable value.

For example, given a `get_weather` tool that requires a `location` parameter, if you ask Claude "What's the weather?" without specifying a location, Claude (particularly Claude Sonnet) might guess values you didn't supply:

JSON



```python
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835lq9",
  "name": "get_weather",
  "input": { "location": "New York, NY", "unit": "fahrenheit" }
}
```

This behavior is not guaranteed, especially for more ambiguous prompts and for less capable models.

## Choose a tool

For `type` strings, versions, and beta headers, see [Tool reference](agents-and-tools-tool-use-tool-reference.md).

### Your own tools

For tools you define, you write the schema and your application executes each call.



[Define tools](agents-and-tools-tool-use-implement-tool-use.md)

Specify tool schemas, write descriptions, and control when Claude calls your tools.

[Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md)

Parse `tool_use` blocks, format `tool_result` responses, and handle errors.

### Anthropic-schema client tools

Anthropic publishes the schema and trains Claude on it. Your application still executes each call and returns the `tool_result`.



[Memory tool](agents-and-tools-tool-use-memory-tool.md)

Store and retrieve information across conversations in files you control.



[Bash tool](agents-and-tools-tool-use-bash-tool.md)

Run shell commands in a persistent session that maintains state.



[Text editor tool](agents-and-tools-tool-use-text-editor-tool.md)

View and modify text files to debug, fix, and improve code.



[Computer use tool](agents-and-tools-tool-use-computer-use-tool.md)

Take screenshots and control the mouse and keyboard in a desktop environment.

[Browser use tool](agents-and-tools-tool-use-browser-use-tool.md)

Navigate, read, and interact with webpages in your own browser environment.

### Server tools

Server tools run on Anthropic's infrastructure, with no handler code in your application. See [Server tools](agents-and-tools-tool-use-server-tools.md) for the mechanics they share.



[Web search tool](agents-and-tools-tool-use-web-search-tool.md)

Search the web for information beyond the knowledge cutoff, with cited sources.



[Web fetch tool](agents-and-tools-tool-use-web-fetch-tool.md)

Retrieve the full content of specified web pages and PDF documents.



[Code execution tool](agents-and-tools-tool-use-code-execution-tool.md)

Run Python and bash code in a sandboxed container to analyze data and generate files.



[Advisor tool](agents-and-tools-tool-use-advisor-tool.md)

Let a faster executor model consult a higher-intelligence advisor model mid-generation.



[Tool search tool](agents-and-tools-tool-use-tool-search-tool.md)

Work with thousands of tools by discovering and loading them on demand.



[MCP connector](agents-and-tools-mcp-connector.md)

Connect to remote MCP servers from the Messages API without a separate MCP client.



[Claude Managed Agents](../Other/managed-agents-overview.md) provides a built-in toolset that Claude uses autonomously within a session. For that toolset and the Managed Agents way to add custom tools, see its [Tools](../Other/managed-agents-tools.md) page.

## Pricing

Tool use requests are priced based on:

1.  The total number of input tokens sent to the model (including in the `tools` parameter)
2.  The number of output tokens generated
3.  For server-side tools, additional usage-based pricing (for example, web search charges per search performed)

Client-side tools are priced the same as any other Claude API request, although server-side tools can incur additional charges based on their specific usage.

The additional tokens from tool use come from:

- The `tools` parameter in API requests (tool names, descriptions, and schemas)
- `tool_use` content blocks in API requests and responses
- `tool_result` content blocks in API requests

When you use `tools`, the API also automatically includes a special system prompt for the model that enables tool use. The number of tool use tokens required for each model is listed in the following table (excluding the additional tokens listed earlier). Note that the table assumes at least 1 tool is provided. If no `tools` are provided, then a tool choice of `none` uses 0 additional system prompt tokens.

[TABLE]

These token counts are added to your normal input and output tokens to calculate the total cost of a request.

See the [Models overview](../../20-Models/about-claude-models-overview.md#latest-models-comparison) table for current per-model prices.

When you send a tool use prompt, like any other API request, the response includes both input and output token counts in the reported `usage` metrics.

Some server tools add usage-based charges on top of tokens: see [Web search tool](agents-and-tools-tool-use-web-search-tool.md#usage-and-pricing) and [Code execution tool](agents-and-tools-tool-use-code-execution-tool.md#usage-and-pricing) for their rates.

## Next steps

[How tool use works](agents-and-tools-tool-use-how-tool-use-works.md)

Understand the tool use loop, where tools execute, and when to use tools instead of prose.



[Tutorial: Build a tool-using agent](agents-and-tools-tool-use-build-a-tool-using-agent.md)

A guided walkthrough from a single tool call to a production-ready agentic loop.



[Tool reference](agents-and-tools-tool-use-tool-reference.md)

Directory of Anthropic-provided tools and reference for optional tool definition properties.
