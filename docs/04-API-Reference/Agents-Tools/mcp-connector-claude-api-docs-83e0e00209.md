---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:04:48Z"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/mcp-connector"
title: "MCP connector - Claude API Docs"
---

MCP in the API

# MCP connector

Copy page

Copy page

Claude's Model Context Protocol (MCP) connector feature enables you to connect to remote MCP servers directly from the Messages API without a separate MCP client.

**Current version**: This feature requires the beta header: `"anthropic-beta": "mcp-client-2025-11-20"`

The previous version (`mcp-client-2025-04-04`) is deprecated. See the [deprecated version documentation](#deprecated-version-mcp-client-2025-04-04) below.

## 

Key features

- **Direct API integration**: Connect to MCP servers without implementing an MCP client
- **Tool calling support**: Access MCP tools through the Messages API
- **Flexible tool configuration**: Enable all tools, allowlist specific tools, or denylist unwanted tools
- **Per-tool configuration**: Configure individual tools with custom settings
- **OAuth authentication**: Support for OAuth Bearer tokens for authenticated servers
- **Multiple servers**: Connect to multiple MCP servers in a single request

## 

Limitations

- Of the feature set of the [MCP specification](https://modelcontextprotocol.io/introduction#explore-mcp), only [tool calls](https://modelcontextprotocol.io/docs/concepts/tools) are currently supported.
- The server must be publicly exposed through HTTP (supports both Streamable HTTP and SSE transports). Local STDIO servers cannot be connected directly.
- The MCP connector is currently not supported on Amazon Bedrock and Google Vertex.

## 

Using the MCP connector in the Messages API

The MCP connector uses two components:

1.  **MCP Server Definition** (`mcp_servers` array): Defines server connection details (URL, authentication)
2.  **MCP Toolset** (`tools` array): Configures which tools to enable and how to configure them

### 

Basic example

This example enables all tools from an MCP server with default configuration:

Shell

``` shiki
curl https://api.anthropic.com/v1/messages \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: mcp-client-2025-11-20" \
  -d '{
    "model": "claude-opus-4-6",
    "max_tokens": 1000,
    "messages": [{"role": "user", "content": "What tools do you have available?"}],
    "mcp_servers": [
      {
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse",
        "name": "example-mcp",
        "authorization_token": "YOUR_TOKEN"
      }
    ],
    "tools": [
      {
        "type": "mcp_toolset",
        "mcp_server_name": "example-mcp"
      }
    ]
  }'
```

## 

MCP server configuration

Each MCP server in the `mcp_servers` array defines the connection details:

``` shiki
{
  "type": "url",
  "url": "https://example-server.modelcontextprotocol.io/sse",
  "name": "example-mcp",
  "authorization_token": "YOUR_TOKEN"
}
```

### 

Field descriptions

| Property | Type | Required | Description |
|----|----|----|----|
| `type` | string | Yes | Currently only "url" is supported |
| `url` | string | Yes | The URL of the MCP server. Must start with https:// |
| `name` | string | Yes | A unique identifier for this MCP server. Must be referenced by exactly one MCPToolset in the `tools` array. |
| `authorization_token` | string | No | OAuth authorization token if required by the MCP server. See [MCP specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization). |

## 

MCP toolset configuration

The MCPToolset lives in the `tools` array and configures which tools from the MCP server are enabled and how they should be configured.

### 

Basic structure

``` shiki
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

### 

Field descriptions

| Property | Type | Required | Description |
|----|----|----|----|
| `type` | string | Yes | Must be "mcp_toolset" |
| `mcp_server_name` | string | Yes | Must match a server name defined in the `mcp_servers` array |
| `default_config` | object | No | Default configuration applied to all tools in this set. Individual tool configs in `configs` will override these defaults. |
| `configs` | object | No | Per-tool configuration overrides. Keys are tool names, values are configuration objects. |
| `cache_control` | object | No | Cache breakpoint configuration for this toolset |

### 

Tool configuration options

Each tool (whether configured in `default_config` or in `configs`) supports the following fields:

| Property | Type | Default | Description |
|----|----|----|----|
| `enabled` | boolean | `true` | Whether this tool is enabled |
| `defer_loading` | boolean | `false` | If true, tool description is not sent to the model initially. Used with [Tool Search Tool](/docs/en/agents-and-tools/tool-use/tool-search-tool). |

### 

Configuration merging

Configuration values merge with this precedence (highest to lowest):

1.  Tool-specific settings in `configs`
2.  Set-level `default_config`
3.  System defaults

Example:

``` shiki
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

Results in:

- `search_events`: `enabled: false` (from configs), `defer_loading: true` (from default_config)
- All other tools: `enabled: true` (system default), `defer_loading: true` (from default_config)

## 

Common configuration patterns

### 

Enable all tools with default configuration

The simplest pattern - enable all tools from a server:

``` shiki
{
  "type": "mcp_toolset",
  "mcp_server_name": "google-calendar-mcp",
}
```

### 

Allowlist - Enable only specific tools

Set `enabled: false` as the default, then explicitly enable specific tools:

``` shiki
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

### 

Denylist - Disable specific tools

Enable all tools by default, then explicitly disable unwanted tools:

``` shiki
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

### 

Mixed - Allowlist with per-tool configuration

Combine allowlisting with custom configuration for each tool:

``` shiki
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

In this example:

- `search_events` is enabled with `defer_loading: false`
- `list_events` is enabled with `defer_loading: true` (inherited from default_config)
- All other tools are disabled

## 

Validation rules

The API enforces these validation rules:

- **Server must exist**: The `mcp_server_name` in an MCPToolset must match a server defined in the `mcp_servers` array
- **Server must be used**: Every MCP server defined in `mcp_servers` must be referenced by exactly one MCPToolset
- **Unique toolset per server**: Each MCP server can only be referenced by one MCPToolset
- **Unknown tool names**: If a tool name in `configs` doesn't exist on the MCP server, a backend warning is logged but no error is returned (MCP servers may have dynamic tool availability)

## 

Response content types

When Claude uses MCP tools, the response will include two new content block types:

### 

MCP Tool Use Block

``` shiki
{
  "type": "mcp_tool_use",
  "id": "mcptoolu_014Q35RayjACSWkSj4X2yov1",
  "name": "echo",
  "server_name": "example-mcp",
  "input": { "param1": "value1", "param2": "value2" }
}
```

### 

MCP Tool Result Block

``` shiki
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

## 

Multiple MCP servers

You can connect to multiple MCP servers by including multiple server definitions in `mcp_servers` and a corresponding MCPToolset for each in the `tools` array:

``` shiki
{
  "model": "claude-opus-4-6",
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

## 

Authentication

For MCP servers that require OAuth authentication, you'll need to obtain an access token. The MCP connector beta supports passing an `authorization_token` parameter in the MCP server definition. API consumers are expected to handle the OAuth flow and obtain the access token prior to making the API call, as well as refreshing the token as needed.

### 

Obtaining an access token for testing

The MCP inspector can guide you through the process of obtaining an access token for testing purposes.

1.  Run the inspector with the following command. You need Node.js installed on your machine.

    ``` shiki
    npx @modelcontextprotocol/inspector
    ```

2.  In the sidebar on the left, for "Transport type", select either "SSE" or "Streamable HTTP".

3.  Enter the URL of the MCP server.

4.  In the right area, click on the "Open Auth Settings" button after "Need to configure authentication?".

5.  Click "Quick OAuth Flow" and authorize on the OAuth screen.

6.  Follow the steps in the "OAuth Flow Progress" section of the inspector and click "Continue" until you reach "Authentication complete".

7.  Copy the `access_token` value.

8.  Paste it into the `authorization_token` field in your MCP server configuration.

### 

Using the access token

Once you've obtained an access token using either OAuth flow above, you can use it in your MCP server configuration:

``` shiki
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

For detailed explanations of the OAuth flow, refer to the [Authorization section](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) in the MCP specification.

## 

Client-side MCP helpers (TypeScript)

If you manage your own MCP client connection (for example, with local stdio servers, MCP prompts, or MCP resources), the TypeScript SDK provides helper functions that convert between MCP types and Claude API types. This eliminates manual conversion code when using the [MCP SDK](https://github.com/modelcontextprotocol/typescript-sdk) alongside the Anthropic SDK.

These helpers are currently available in the TypeScript SDK only.

Use the [`mcp_servers` API parameter](#using-the-mcp-connector-in-the-messages-api) when you have remote servers accessible via URL and only need tool support. If you're using the [Agent SDK](/docs/en/agent-sdk/mcp), MCP connections are managed automatically. Use the client-side helpers when you need local servers, prompts, resources, or more control over the connection with the base SDK.

### 

Installation

Install both the Anthropic SDK and the MCP SDK:

``` shiki
npm install @anthropic-ai/sdk @modelcontextprotocol/sdk
```

### 

Available helpers

Import the helpers from the beta namespace:

``` shiki
import {
  mcpTools,
  mcpMessages,
  mcpResourceToContent,
  mcpResourceToFile,
} from '@anthropic-ai/sdk/helpers/beta/mcp';
```

| Helper | Description |
|----|----|
| `mcpTools(tools, mcpClient)` | Converts MCP tools to Claude API tools for use with `client.beta.messages.toolRunner()` |
| `mcpMessages(messages)` | Converts MCP prompt messages to Claude API message format |
| `mcpResourceToContent(resource)` | Converts an MCP resource to a Claude API content block |
| `mcpResourceToFile(resource)` | Converts an MCP resource to a file object for upload |

### 

Use MCP tools

Convert MCP tools for use with the SDK's [tool runner](/docs/en/agents-and-tools/tool-use/implement-tool-use#tool-runner-beta), which handles tool execution automatically:

``` shiki
import Anthropic from '@anthropic-ai/sdk';
import { mcpTools } from '@anthropic-ai/sdk/helpers/beta/mcp';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StdioClientTransport } from '@modelcontextprotocol/sdk/client/stdio.js';

const anthropic = new Anthropic();

// Connect to an MCP server
const transport = new StdioClientTransport({ command: 'mcp-server', args: [] });
const mcpClient = new Client({ name: 'my-client', version: '1.0.0' });
await mcpClient.connect(transport);

// List tools and convert them for the Claude API
const { tools } = await mcpClient.listTools();
const runner = await anthropic.beta.messages.toolRunner({
  model: 'claude-sonnet-4-5',
  max_tokens: 1024,
  messages: [{ role: 'user', content: 'What tools do you have available?' }],
  tools: mcpTools(tools, mcpClient),
});
```

### 

Use MCP prompts

Convert MCP prompt messages into Claude API message format:

``` shiki
import { mcpMessages } from '@anthropic-ai/sdk/helpers/beta/mcp';

const { messages } = await mcpClient.getPrompt({ name: 'my-prompt' });
const response = await anthropic.beta.messages.create({
  model: 'claude-sonnet-4-5',
  max_tokens: 1024,
  messages: mcpMessages(messages),
});
```

### 

Use MCP resources

Convert MCP resources into content blocks to include in messages, or into file objects for upload:

``` shiki
import { mcpResourceToContent, mcpResourceToFile } from '@anthropic-ai/sdk/helpers/beta/mcp';

// As a content block in a message
const resource = await mcpClient.readResource({ uri: 'file:///path/to/doc.txt' });
await anthropic.beta.messages.create({
  model: 'claude-sonnet-4-5',
  max_tokens: 1024,
  messages: [
    {
      role: 'user',
      content: [
        mcpResourceToContent(resource),
        { type: 'text', text: 'Summarize this document' },
      ],
    },
  ],
});

// As a file upload
const fileResource = await mcpClient.readResource({ uri: 'file:///path/to/data.json' });
await anthropic.beta.files.upload({ file: mcpResourceToFile(fileResource) });
```

### 

Error handling

The conversion functions throw `UnsupportedMCPValueError` if an MCP value isn't supported by the Claude API. This can happen with unsupported content types, MIME types, or non-HTTP resource links.

## 

Migration guide

If you're using the deprecated `mcp-client-2025-04-04` beta header, follow this guide to migrate to the new version.

### 

Key changes

1.  **New beta header**: Change from `mcp-client-2025-04-04` to `mcp-client-2025-11-20`
2.  **Tool configuration moved**: Tool configuration now lives in the `tools` array as MCPToolset objects, not in the MCP server definition
3.  **More flexible configuration**: New pattern supports allowlisting, denylisting, and per-tool configuration

### 

Migration steps

**Before (deprecated):**

``` shiki
{
  "model": "claude-opus-4-6",
  "max_tokens": 1000,
  "messages": [...],
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

**After (current):**

``` shiki
{
  "model": "claude-opus-4-6",
  "max_tokens": 1000,
  "messages": [...],
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

### 

Common migration patterns

| Old pattern | New pattern |
|----|----|
| No `tool_configuration` (all tools enabled) | MCPToolset with no `default_config` or `configs` |
| `tool_configuration.enabled: false` | MCPToolset with `default_config.enabled: false` |
| `tool_configuration.allowed_tools: [...]` | MCPToolset with `default_config.enabled: false` and specific tools enabled in `configs` |

## 

Deprecated version: mcp-client-2025-04-04

This version is deprecated. Please migrate to `mcp-client-2025-11-20` using the [migration guide](#migration-guide) above.

The previous version of the MCP connector included tool configuration directly in the MCP server definition:

``` shiki
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

### 

Deprecated field descriptions

| Property | Type | Description |
|----|----|----|
| `tool_configuration` | object | **Deprecated**: Use MCPToolset in the `tools` array instead |
| `tool_configuration.enabled` | boolean | **Deprecated**: Use `default_config.enabled` in MCPToolset |
| `tool_configuration.allowed_tools` | array | **Deprecated**: Use allowlist pattern with `configs` in MCPToolset |

Was this page helpful?

- 

- [Key features](#key-features)

- [Limitations](#limitations)

- [Using the MCP connector in the Messages API](#using-the-mcp-connector-in-the-messages-api)

- [Basic example](#basic-example)

- [MCP server configuration](#mcp-server-configuration)

- [Field descriptions](#field-descriptions)

- [MCP toolset configuration](#mcp-toolset-configuration)

- [Basic structure](#basic-structure)

- [Field descriptions](#field-descriptions-2)

- [Tool configuration options](#tool-configuration-options)

- [Configuration merging](#configuration-merging)

- [Common configuration patterns](#common-configuration-patterns)

- [Enable all tools with default configuration](#enable-all-tools-with-default-configuration)

- [Allowlist - Enable only specific tools](#allowlist-enable-only-specific-tools)

- [Denylist - Disable specific tools](#denylist-disable-specific-tools)

- [Mixed - Allowlist with per-tool configuration](#mixed-allowlist-with-per-tool-configuration)

- [Validation rules](#validation-rules)

- [Response content types](#response-content-types)

- [MCP Tool Use Block](#mcp-tool-use-block)

- [MCP Tool Result Block](#mcp-tool-result-block)

- [Multiple MCP servers](#multiple-mcp-servers)

- [Authentication](#authentication)

- [Obtaining an access token for testing](#obtaining-an-access-token-for-testing)

- [Using the access token](#using-the-access-token)

- [Client-side MCP helpers (TypeScript)](#client-side-mcp-helpers-type-script)

- [Installation](#installation)

- [Available helpers](#available-helpers)

- [Use MCP tools](#use-mcp-tools)

- [Use MCP prompts](#use-mcp-prompts)

- [Use MCP resources](#use-mcp-resources)

- [Error handling](#error-handling)

- [Migration guide](#migration-guide)

- [Key changes](#key-changes)

- [Migration steps](#migration-steps)

- [Common migration patterns](#common-migration-patterns)

- [Deprecated version: mcp-client-2025-04-04](#deprecated-version-mcp-client-2025-04-04)

- [Deprecated field descriptions](#deprecated-field-descriptions)

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
