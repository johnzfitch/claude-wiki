---
title: "MCP connector - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/mcp-connector"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:17Z"
tags: ["api", "authentication", "cli", "mcp"]
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Fmcp-connector)

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

[Messages](/docs/en/intro)MCP

# MCP connector

Copy page



Connect to remote MCP servers directly from the Messages API without an MCP client, and allowlist, denylist, or configure individual tools.

Copy page



MCP connector

[Beta](/docs/en/build-with-claude/overview#feature-availability)

[Beta header](/docs/en/api/beta-headers)

mcp-client-2025-11-20

[ZDR](/docs/en/manage-claude/api-and-data-retention)

Not eligible

Claude's Model Context Protocol (MCP) connector feature enables you to connect to remote MCP servers directly from the Messages API without a separate MCP client.



The previous version of this feature (`mcp-client-2025-04-04`) is deprecated. See [Deprecated version: mcp-client-2025-04-04](#deprecated-version-mcp-client-2025-04-04).

## Key features

- **Direct API integration:** Connect to MCP servers without implementing an MCP client
- **Tool calling support:** Access MCP tools through the Messages API
- **Flexible tool configuration:** Enable all tools, allowlist specific tools, or denylist unwanted tools
- **Per-tool configuration:** Configure individual tools with custom settings
- **OAuth authentication:** Support for OAuth Bearer tokens for authenticated servers
- **Multiple servers:** Connect to multiple MCP servers in a single request

## When Claude uses MCP tools

Once an MCP server is connected, Claude calls its tools when the user's request maps to a tool's described capability, either explicitly ("search Jira for open bugs") or implicitly ("what's blocking the release?" with a Jira server attached).

Claude does **not** call an MCP tool for general knowledge questions about a connected service. Asking "how do Notion databases work?" with a Notion server attached is answered directly; asking "what's in my Projects database?" triggers the tool.

You can steer how readily Claude calls MCP tools through your system prompt. See [When Claude uses tools](/docs/en/agents-and-tools/tool-use/overview#when-claude-uses-tools) for general guidance and example phrasings.

## Limitations

- Of the feature set of the [MCP specification](https://modelcontextprotocol.io/introduction#explore-mcp), only [tool calls](https://modelcontextprotocol.io/docs/concepts/tools) are currently supported.
- The server must be publicly exposed through HTTP (supports both Streamable HTTP and SSE transports). Local STDIO servers cannot be connected directly.

## Using the MCP connector in the Messages API

The MCP connector uses two components:

1.  **MCP server definition** (`mcp_servers` array): Defines server connection details (URL, authentication)
2.  **MCP toolset** (`tools` array): Configures which tools to enable and how to configure them

### Basic example

This example enables all tools from an MCP server with default configuration:

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
    max_tokens=1000,
    messages=[{"role": "user", "content": "What tools do you have available?"}],
    mcp_servers=[
        {
            "type": "url",
            "url": "https://example-server.modelcontextprotocol.io/sse",
            "name": "example-mcp",
            "authorization_token": "YOUR_TOKEN",
        }
    ],
    tools=[{"type": "mcp_toolset", "mcp_server_name": "example-mcp"}],
    betas=["mcp-client-2025-11-20"],
)

print(response)
```

## MCP server configuration

Each MCP server in the `mcp_servers` array defines the connection details:

```python
{
  "type": "url",
  "url": "https://example-server.modelcontextprotocol.io/sse",
  "name": "example-mcp",
  "authorization_token": "YOUR_TOKEN"
}
```



### Field descriptions

| Property              | Type   | Required | Description                                                                                                                                                                                                                                          |
|-----------------------|--------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`                | string | Yes      | Currently only "url" is supported.                                                                                                                                                                                                                   |
| `url`                 | string | Yes      | The URL of the MCP server. Must start with https://.                                                                                                                                                                                                 |
| `name`                | string | Yes      | A unique identifier for this MCP server. Must be referenced by exactly one MCPToolset in the `tools` array.                                                                                                                                          |
| `authorization_token` | string | No       | OAuth authorization token if required by the MCP server. See [Authentication](#authentication) for how to obtain one, or the [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) for protocol details. |

## MCP toolset configuration

The MCPToolset lives in the `tools` array and configures which tools from the MCP server are enabled and how they should be configured.

### Basic structure

```python
{
  "type": "mcp_toolset",
  "mcp_server_name": "example-mcp",
  "default_config": {
    "enabled": true,
    "defer_loading": false
  },
  "configs": {
    "specific_tool_name": {
      "enabled": true,
      "defer_loading": true
    }
  }
}
```



### Field descriptions

| Property          | Type   | Required | Description                                                                                                           |
|-------------------|--------|----------|-----------------------------------------------------------------------------------------------------------------------|
| `type`            | string | Yes      | Must be "mcp_toolset".                                                                                                |
| `mcp_server_name` | string | Yes      | Must match a server name defined in the `mcp_servers` array.                                                          |
| `default_config`  | object | No       | Default configuration applied to all tools in this set. Individual tool configs in `configs` override these defaults. |
| `configs`         | object | No       | Per-tool configuration overrides. Keys are tool names, values are configuration objects.                              |
| `cache_control`   | object | No       | [Prompt caching](/docs/en/build-with-claude/prompt-caching) cache breakpoint configuration for this toolset.          |

With the `mcp-client-2026-09-15` beta header, an MCPToolset also accepts `tools`, a pinned copy of the server's tool list. See [Pin an MCP server's tool list](#pin-mcp-tool-list).

### Tool configuration options

Each tool (whether configured in `default_config` or in `configs`) supports the following fields:

| Property        | Type    | Default | Description                                                                                                                                      |
|-----------------|---------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `enabled`       | boolean | `true`  | Whether this tool is enabled.                                                                                                                    |
| `defer_loading` | boolean | `false` | If true, tool description is not sent to the model initially. Used with [Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool). |

For the full directory of Anthropic-provided tools and optional properties such as `defer_loading`, see the [Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference). To search across large tool sets, see [Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool).

### Configuration merging

Configuration values merge with this precedence (highest to lowest):

1.  Tool-specific settings in `configs`
2.  Set-level `default_config`
3.  System defaults

Example:

```python
{
  "type": "mcp_toolset",
  "mcp_server_name": "google-calendar-mcp",
  "default_config": {
    "defer_loading": true
  },
  "configs": {
    "search_events": {
      "enabled": false
    }
  }
}
```



Results in:

- `search_events`: `enabled: false` (from configs), `defer_loading: true` (from default_config)
- All other tools: `enabled: true` (system default), `defer_loading: true` (from default_config)

## Common configuration patterns

### Enable all tools with default configuration

The simplest pattern: enable all tools from a server:

```python
{
  "type": "mcp_toolset",
  "mcp_server_name": "google-calendar-mcp"
}
```



### Allowlist: enable only specific tools

Set `enabled: false` as the default, then explicitly enable specific tools:

```python
{
  "type": "mcp_toolset",
  "mcp_server_name": "google-calendar-mcp",
  "default_config": {
    "enabled": false
  },
  "configs": {
    "search_events": {
      "enabled": true
    },
    "create_event": {
      "enabled": true
    }
  }
}
```



### Denylist: disable specific tools

Enable all tools by default, then explicitly disable unwanted tools. Denylisting write or destructive tools is recommended when building read-only assistants, or when you want a human confirmation step before state changes:

```python
{
  "type": "mcp_toolset",
  "mcp_server_name": "google-calendar-mcp",
  "configs": {
    "delete_all_events": {
      "enabled": false
    },
    "share_calendar_publicly": {
      "enabled": false
    }
  }
}
```



### Mixed: allowlist with per-tool configuration

Combine allowlisting with custom configuration for each tool:

```python
{
  "type": "mcp_toolset",
  "mcp_server_name": "google-calendar-mcp",
  "default_config": {
    "enabled": false,
    "defer_loading": true
  },
  "configs": {
    "search_events": {
      "enabled": true,
      "defer_loading": false
    },
    "list_events": {
      "enabled": true
    }
  }
}
```



In this example:

- `search_events` is enabled with `defer_loading: false`
- `list_events` is enabled with `defer_loading: true` (inherited from default_config)
- All other tools are disabled

## Validation rules

The API enforces these validation rules:

- **Server must exist:** The `mcp_server_name` in an MCPToolset must match a server defined in the `mcp_servers` array
- **Server must be used:** Every MCP server defined in `mcp_servers` must be referenced by exactly one MCPToolset
- **Unique toolset per server:** Each MCP server can only be referenced by one MCPToolset
- **Unknown tool names:** If a tool name in `configs` doesn't exist on the MCP server, a backend warning is logged but no error is returned (MCP servers may have dynamic tool availability)

## Response content types

When Claude uses MCP tools, the response includes two new content block types:

### MCP tool use block

```python
{
  "type": "mcp_tool_use",
  "id": "mcptoolu_014Q35RayjACSWkSj4X2yov1",
  "name": "echo",
  "server_name": "example-mcp",
  "input": { "param1": "value1", "param2": "value2" }
}
```



### MCP tool result block

```python
{
  "type": "mcp_tool_result",
  "tool_use_id": "mcptoolu_014Q35RayjACSWkSj4X2yov1",
  "is_error": false,
  "content": [
    {
      "type": "text",
      "text": "Hello"
    }
  ]
}
```



## Pin an MCP server's tool list (beta)

An MCP server can change its tools at any time. The `mcp-client-2026-09-15` beta header records the tool list each server returns and lets you pin it, so a server that changes its tools doesn't change what Claude sees partway through a conversation. It includes everything `mcp-client-2025-11-20` does, so send it in place of that header. It's available on the Claude API.

When the API asks an MCP server for its tools while producing a response, the response starts with an `mcp_tool_listing` block for that server, one block for each server it asked:

```python
{
  "type": "mcp_tool_listing",
  "mcp_server_name": "example-mcp",
  "tools": [
    {
      "name": "echo",
      "description": "Returns the text it receives.",
      "input_schema": {
        "type": "object",
        "properties": { "text": { "type": "string" } },
        "required": ["text"]
      }
    }
  ]
}
```



If your code reads `content[0]`, skip these blocks. Send the assistant message back unchanged, `mcp_tool_listing` blocks included, and keep sending `mcp-client-2026-09-15` on every request that carries one. Later requests then use the recorded list for that server instead of asking it again.

To pin a list yourself, copy a block's `tools` into the `tools` field of that server's MCPToolset. The API then doesn't ask the server for its tools, and the toolset's tools are exactly those entries, with `default_config` and `configs` applied:

```python
{
  "type": "mcp_toolset",
  "mcp_server_name": "example-mcp",
  "tools": [
    {
      "name": "echo",
      "description": "Returns the text it receives.",
      "input_schema": {
        "type": "object",
        "properties": { "text": { "type": "string" } },
        "required": ["text"]
      }
    }
  ]
}
```



Each entry in `tools` holds the tool's `name` as the server lists it (without the server name), its `description`, and its `input_schema`.

The following example sends one request with an unpinned toolset, copies the returned list into the toolset's `tools` field, and sends the request again. The second response has no `mcp_tool_listing` block, because the API doesn't ask the server:

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
from anthropic.types.beta import (
    BetaMessageParam,
    BetaRequestMCPServerURLDefinitionParam,
)

client = anthropic.Anthropic()

mcp_servers: list[BetaRequestMCPServerURLDefinitionParam] = [
    {
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse",
        "name": "example-mcp",
        "authorization_token": "YOUR_TOKEN",
    },
]
messages: list[BetaMessageParam] = [
    {"role": "user", "content": "What tools do you have available?"},
]

# First request: the toolset isn't pinned, so the API asks the server for
# its tools and the response starts with an mcp_tool_listing block.
first = client.beta.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    betas=["mcp-client-2026-09-15"],
    mcp_servers=mcp_servers,
    tools=[{"type": "mcp_toolset", "mcp_server_name": "example-mcp"}],
    messages=messages,
)

listing = next(block for block in first.content if block.type == "mcp_tool_listing")
print([tool.name for tool in listing.tools])

# Pin the list: copy the block's tools into the toolset. The API uses
# exactly these entries and doesn't ask the server again.
second = client.beta.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    betas=["mcp-client-2026-09-15"],
    mcp_servers=mcp_servers,
    tools=[
        {
            "type": "mcp_toolset",
            "mcp_server_name": "example-mcp",
            "tools": [
                {
                    "name": tool.name,
                    "description": tool.description,
                    "input_schema": tool.input_schema,
                }
                for tool in listing.tools
            ],
        },
    ],
    messages=messages,
)

# With a pinned toolset, the response has no mcp_tool_listing block.
print([block.type for block in second.content])
```

With the `inline-tools-2026-09-15` beta header as well, you can add an MCP server partway through a conversation. See [Add an MCP server mid-conversation](/docs/en/build-with-claude/mid-conversation-system-messages#add-an-mcp-server-mid-conversation-beta).

## Multiple MCP servers

You can connect to multiple MCP servers by including multiple server definitions in `mcp_servers` and a corresponding MCPToolset for each in the `tools` array:

```python
{
  "model": "claude-opus-5-5",
  "max_tokens": 1000,
  "messages": [
    {
      "role": "user",
      "content": "Use tools from both mcp-server-1 and mcp-server-2 to complete this task"
    }
  ],
  "mcp_servers": [
    {
      "type": "url",
      "url": "https://mcp.example1.com/sse",
      "name": "mcp-server-1",
      "authorization_token": "TOKEN1"
    },
    {
      "type": "url",
      "url": "https://mcp.example2.com/sse",
      "name": "mcp-server-2",
      "authorization_token": "TOKEN2"
    }
  ],
  "tools": [
    {
      "type": "mcp_toolset",
      "mcp_server_name": "mcp-server-1"
    },
    {
      "type": "mcp_toolset",
      "mcp_server_name": "mcp-server-2",
      "default_config": {
        "defer_loading": true
      }
    }
  ]
}
```



With many tools available, Claude selects based on tool names and descriptions. Clear, specific tool descriptions improve selection accuracy. For large tool sets (dozens of tools across several servers), consider enabling [`defer_loading`](#tool-configuration-options) with the [Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool) so only relevant tools are surfaced per query.

## Authentication

For MCP servers that require OAuth authentication, you'll need to obtain an access token. The MCP connector beta supports passing an `authorization_token` parameter in the MCP server definition. API consumers are expected to handle the OAuth flow and obtain the access token prior to making the API call, and to refresh the token as needed.

### Obtaining an access token for testing

The MCP inspector can guide you through the process of obtaining an access token for testing purposes.

1.  Run the inspector with the following command. You need Node.js installed on your machine.

    ``` shiki
    npx @modelcontextprotocol/inspector
    ```

    

2.  In the sidebar on the left, for **Transport type**, select either **SSE** or **Streamable HTTP**.

3.  Enter the URL of the MCP server.

4.  In the right area, click **Open Auth Settings** after **Need to configure authentication?**.

5.  Click **Quick OAuth Flow** and authorize on the OAuth screen.

6.  Follow the steps in the **OAuth Flow Progress** section of the inspector and click **Continue** until you reach **Authentication complete**.

7.  Copy the `access_token` value.

8.  Paste it into the `authorization_token` field in your MCP server configuration.

### Using the access token

Once you've obtained an access token using either of the preceding OAuth flows, you can use it in your MCP server configuration:

```python
{
  "mcp_servers": [
    {
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse",
      "name": "authenticated-server",
      "authorization_token": "YOUR_ACCESS_TOKEN_HERE"
    }
  ]
}
```



For detailed explanations of the OAuth flow, refer to the [Authorization section](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) in the MCP specification.

## Client-side MCP helpers

If you manage your own MCP client connection (for example, with local stdio servers, MCP prompts, or MCP resources), the SDKs provide helper functions that convert between MCP types and Claude API types. This eliminates manual conversion code when using an MCP SDK for your language (for example, the [TypeScript MCP SDK](https://github.com/modelcontextprotocol/typescript-sdk)) alongside the Anthropic SDK.



Use the [`mcp_servers` API parameter](#using-the-mcp-connector-in-the-messages-api) when you have remote servers accessible by URL and only need tool support. Use the client-side helpers when you need local servers, prompts, resources, or more control over the connection with the base SDK.

### Installation

Install both the Anthropic SDK and the MCP SDK:

Python

TypeScript

C#

Go

Java

PHP

Ruby

The MCP helpers are included in the `mcp` extra, which requires Python 3.10 or later:

```python
pip install "anthropic[mcp]"
```



### Available helpers

Import the helpers for your language:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
from anthropic.lib.tools.mcp import (
    async_mcp_tool,
    mcp_message,
    mcp_resource_to_content,
    mcp_resource_to_file,
)
```

Helper names and exact signatures follow each language's conventions; this table shows the TypeScript forms:

| Helper                           | Description                                                                             |
|----------------------------------|-----------------------------------------------------------------------------------------|
| `mcpTools(tools, mcpClient)`     | Converts MCP tools to Claude API tools for use with `client.beta.messages.toolRunner()` |
| `mcpMessages(messages)`          | Converts MCP prompt messages to Claude API message format                               |
| `mcpResourceToContent(resource)` | Converts an MCP resource to a Claude API content block                                  |
| `mcpResourceToFile(resource)`    | Converts an MCP resource to a file object for upload                                    |

### Use MCP tools

Convert MCP tools for use with the SDK's [tool runner](/docs/en/agents-and-tools/tool-use/tool-runner), which handles tool execution automatically:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
from anthropic.lib.tools.mcp import async_mcp_tool
from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client

client = AsyncAnthropic()


async def main() -> None:
    # Connect to an MCP server
    server_params = StdioServerParameters(command="mcp-server")
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as mcp_client:
            await mcp_client.initialize()

            # List tools and convert them for the Claude API
            tools_result = await mcp_client.list_tools()
            runner = client.beta.messages.tool_runner(
                model="claude-opus-5-5",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": "What tools do you have available?"},
                ],
                tools=[async_mcp_tool(tool, mcp_client) for tool in tools_result.tools],
            )

            final_message = await runner.until_done()
            print(final_message)


asyncio.run(main())
```

### Use MCP prompts

Convert MCP prompt messages into Claude API message format:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
from anthropic.lib.tools.mcp import mcp_message

prompt = await mcp_client.get_prompt(name="my-prompt")
response = await client.beta.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[mcp_message(message) for message in prompt.messages],
)

print(response)
```

### Use MCP resources

Convert MCP resources into content blocks to include in messages, or into file objects for upload:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
from anthropic.lib.tools.mcp import (
    mcp_resource_to_content,
    mcp_resource_to_file,
)

# As a content block in a message
resource = await mcp_client.read_resource(uri="file:///path/to/doc.txt")
response = await client.beta.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                mcp_resource_to_content(resource),
                {"type": "text", "text": "Summarize this document"},
            ],
        }
    ],
)
print(response)

# As a file upload
file_resource = await mcp_client.read_resource(
    uri="file:///path/to/data.json",
)
uploaded = await client.files.upload(
    file=mcp_resource_to_file(file_resource),
)
print(uploaded.id)
```

### Error handling

The conversion functions fail with `UnsupportedMCPValueError` if an MCP value isn't supported by the Claude API (thrown, or in Go returned as an error). This can happen with unsupported content types, MIME types, or resource links (resolve resource links with your MCP client before converting).

## Batch requests

You can include `mcp_servers` in [Message Batches API](/docs/en/build-with-claude/batch-processing) requests. MCP tool calls through the Batches API are priced the same as those in regular Messages API requests.

## Data retention

The MCP connector is not covered by ZDR arrangements. Data exchanged with MCP servers, including tool definitions and execution results, is retained according to Anthropic's standard data retention policy.

For ZDR eligibility across all features, see [API and data retention](/docs/en/manage-claude/api-and-data-retention).

## Migration guide

If you're using the deprecated `mcp-client-2025-04-04` beta header, follow this guide to migrate to the new version.

### Key changes

1.  **New beta header:** Change from `mcp-client-2025-04-04` to `mcp-client-2025-11-20`
2.  **Tool configuration moved:** Tool configuration now lives in the `tools` array as MCPToolset objects, not in the MCP server definition
3.  **More flexible configuration:** New pattern supports allowlisting, denylisting, and per-tool configuration

### Migration steps

**Before (deprecated):**

```python
{
  "model": "claude-opus-5-5",
  "max_tokens": 1000,
  "messages": [
    // ...
  ],
  "mcp_servers": [
    {
      "type": "url",
      "url": "https://mcp.example.com/sse",
      "name": "example-mcp",
      "authorization_token": "YOUR_TOKEN",
      "tool_configuration": {
        "enabled": true,
        "allowed_tools": ["tool1", "tool2"]
      }
    }
  ]
}
```



**After (current):**

```python
{
  "model": "claude-opus-5-5",
  "max_tokens": 1000,
  "messages": [
    // ...
  ],
  "mcp_servers": [
    {
      "type": "url",
      "url": "https://mcp.example.com/sse",
      "name": "example-mcp",
      "authorization_token": "YOUR_TOKEN"
    }
  ],
  "tools": [
    {
      "type": "mcp_toolset",
      "mcp_server_name": "example-mcp",
      "default_config": {
        "enabled": false
      },
      "configs": {
        "tool1": {
          "enabled": true
        },
        "tool2": {
          "enabled": true
        }
      }
    }
  ]
}
```



### Common migration patterns

| Old pattern                                 | New pattern                                                                             |
|---------------------------------------------|-----------------------------------------------------------------------------------------|
| No `tool_configuration` (all tools enabled) | MCPToolset with no `default_config` or `configs`                                        |
| `tool_configuration.enabled: false`         | MCPToolset with `default_config.enabled: false`                                         |
| `tool_configuration.allowed_tools: [...]`   | MCPToolset with `default_config.enabled: false` and specific tools enabled in `configs` |

## Deprecated version: mcp-client-2025-04-04



This version is deprecated. Migrate to `mcp-client-2025-11-20` using the preceding [migration guide](#migration-guide).

The previous version of the MCP connector included tool configuration directly in the MCP server definition:

```python
{
  "mcp_servers": [
    {
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse",
      "name": "example-mcp",
      "authorization_token": "YOUR_TOKEN",
      "tool_configuration": {
        "enabled": true,
        "allowed_tools": ["example_tool_1", "example_tool_2"]
      }
    }
  ]
}
```



### Deprecated field descriptions

| Property                           | Type    | Description                                                        |
|------------------------------------|---------|--------------------------------------------------------------------|
| `tool_configuration`               | object  | **Deprecated:** Use MCPToolset in the `tools` array instead        |
| `tool_configuration.enabled`       | boolean | **Deprecated:** Use `default_config.enabled` in MCPToolset         |
| `tool_configuration.allowed_tools` | array   | **Deprecated:** Use allowlist pattern with `configs` in MCPToolset |

## Compatibility

Supported platforms  
- Claude APIBeta
- Claude Platform on AWSBeta
- Microsoft FoundryBeta
