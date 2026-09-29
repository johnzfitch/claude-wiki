---
title: "Lifecycle - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle"
category: "06-MCP-Tools/Spec-Archive"
fetched_at: "2026-09-29T06:30:26Z"
tags: ["mcp", "mcp-spec"]
---

## On this page

- [Lifecycle Phases](#lifecycle-phases)
  - [Initialization](#initialization)
  - [Version Negotiation](#version-negotiation)
  - [Capability Negotiation](#capability-negotiation)
  - [Operation](#operation)
  - [Shutdown](#shutdown)
  - [stdio](#stdio)
  - [HTTP](#http)
- [Timeouts](#timeouts)
- [Error Handling](#error-handling)

Base Protocol

# Lifecycle

Copy pageCopy page

Copy pageCopy page

The Model Context Protocol (MCP) defines a rigorous lifecycle for client-server connections that ensures proper capability negotiation and state management.

1.  **Initialization**: Capability negotiation and protocol version agreement
2.  **Operation**: Normal protocol communication
3.  **Shutdown**: Graceful termination of the connection


[​](#lifecycle-phases)

Lifecycle Phases


[​](#initialization)

Initialization

The initialization phase **MUST** be the first interaction between client and server. During this phase, the client and server:

- Establish protocol version compatibility
- Exchange and negotiate capabilities
- Share implementation details

The client **MUST** initiate this phase by sending an `initialize` request containing:

- Protocol version supported
- Client capabilities
- Client implementation information

```python
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2025-11-25",
    "capabilities": {
      "roots": {
        "listChanged": true
      },
      "sampling": {},
      "elicitation": {
        "form": {},
        "url": {}
      },
      "tasks": {
        "requests": {
          "elicitation": {
            "create": {}
          },
          "sampling": {
            "createMessage": {}
          }
        }
      }
    },
    "clientInfo": {
      "name": "ExampleClient",
      "title": "Example Client Display Name",
      "version": "1.0.0",
      "description": "An example MCP client application",
      "icons": [
        {
          "src": "https://example.com/icon.png",
          "mimeType": "image/png",
          "sizes": ["48x48"]
        }
      ],
      "websiteUrl": "https://example.com"
    }
  }
}
```

The server **MUST** respond with its own capabilities and information:

```python
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2025-11-25",
    "capabilities": {
      "logging": {},
      "prompts": {
        "listChanged": true
      },
      "resources": {
        "subscribe": true,
        "listChanged": true
      },
      "tools": {
        "listChanged": true
      },
      "tasks": {
        "list": {},
        "cancel": {},
        "requests": {
          "tools": {
            "call": {}
          }
        }
      }
    },
    "serverInfo": {
      "name": "ExampleServer",
      "title": "Example Server Display Name",
      "version": "1.0.0",
      "description": "An example MCP server providing tools and resources",
      "icons": [
        {
          "src": "https://example.com/server-icon.svg",
          "mimeType": "image/svg+xml",
          "sizes": ["any"]
        }
      ],
      "websiteUrl": "https://example.com/server"
    },
    "instructions": "Optional instructions for the client"
  }
}
```

After successful initialization, the client **MUST** send an `initialized` notification to indicate it is ready to begin normal operations:

```python
{
  "jsonrpc": "2.0",
  "method": "notifications/initialized"
}
```

- The client **SHOULD NOT** send requests other than [pings](2025-11-25-basic-utilities-ping.md) before the server has responded to the `initialize` request.
- The server **SHOULD NOT** send requests other than [pings](2025-11-25-basic-utilities-ping.md) and [logging](2025-03-26-server-utilities-logging.md) before receiving the `initialized` notification.


[​](#version-negotiation)

Version Negotiation

In the `initialize` request, the client **MUST** send a protocol version it supports. This **SHOULD** be the *latest* version supported by the client. If the server supports the requested protocol version, it **MUST** respond with the same version. Otherwise, the server **MUST** respond with another protocol version it supports. This **SHOULD** be the *latest* version supported by the server. If the client does not support the version in the server’s response, it **SHOULD** disconnect.

If using HTTP, the client **MUST** include the `MCP-Protocol-Version: <protocol-version>` HTTP header on all subsequent requests to the MCP server. For details, see [the Protocol Version Header section in Transports](2025-11-25-basic-transports.md#protocol-version-header).


[​](#capability-negotiation)

Capability Negotiation

Client and server capabilities establish which optional protocol features will be available during the session. Key capabilities include:

| Category | Capability     | Description                                                                                   |
|----------|----------------|-----------------------------------------------------------------------------------------------|
| Client   | `roots`        | Ability to provide filesystem [roots](2024-11-05-client-roots.md)                 |
| Client   | `sampling`     | Support for LLM [sampling](2025-11-25-client-sampling.md) requests                |
| Client   | `elicitation`  | Support for server [elicitation](2025-11-25-client-elicitation.md) requests       |
| Client   | `tasks`        | Support for [task-augmented](2025-11-25-basic-utilities-tasks.md) client requests |
| Client   | `experimental` | Describes support for non-standard experimental features                                      |
| Server   | `prompts`      | Offers [prompt templates](2025-11-25-server-prompts.md)                           |
| Server   | `resources`    | Provides readable [resources](2025-11-25-server-resources.md)                     |
| Server   | `tools`        | Exposes callable [tools](2025-11-25-server-tools.md)                              |
| Server   | `logging`      | Emits structured [log messages](2025-03-26-server-utilities-logging.md)           |
| Server   | `completions`  | Supports argument [autocompletion](2025-11-25-server-utilities-completion.md)     |
| Server   | `tasks`        | Support for [task-augmented](2025-11-25-basic-utilities-tasks.md) server requests |
| Server   | `experimental` | Describes support for non-standard experimental features                                      |

Capability objects can describe sub-capabilities like:

- `listChanged`: Support for list change notifications (for prompts, resources, and tools)
- `subscribe`: Support for subscribing to individual items’ changes (resources only)


[​](#operation)

Operation

During the operation phase, the client and server exchange messages according to the negotiated capabilities. Both parties **MUST**:

- Respect the negotiated protocol version
- Only use capabilities that were successfully negotiated


[​](#shutdown)

Shutdown

During the shutdown phase, one side (usually the client) cleanly terminates the protocol connection. No specific shutdown messages are defined—instead, the underlying transport mechanism should be used to signal connection termination:


[​](#stdio)

stdio

For the stdio [transport](2025-11-25-basic-transports.md), the client **SHOULD** initiate shutdown by:

1.  First, closing the input stream to the child process (the server)
2.  Waiting for the server to exit, or sending `SIGTERM` if the server does not exit within a reasonable time
3.  Sending `SIGKILL` if the server does not exit within a reasonable time after `SIGTERM`

The server **MAY** initiate shutdown by closing its output stream to the client and exiting.


[​](#http)

HTTP

For HTTP [transports](2025-11-25-basic-transports.md), shutdown is indicated by closing the associated HTTP connection(s).


[​](#timeouts)

Timeouts

Implementations **SHOULD** establish timeouts for all sent requests, to prevent hung connections and resource exhaustion. When the request has not received a success or error response within the timeout period, the sender **SHOULD** issue a [cancellation notification](2025-11-25-basic-utilities-cancellation.md) for that request and stop waiting for a response. SDKs and other middleware **SHOULD** allow these timeouts to be configured on a per-request basis. Implementations **MAY** choose to reset the timeout clock when receiving a [progress notification](2025-11-25-basic-utilities-progress.md) corresponding to the request, as this implies that work is actually happening. However, implementations **SHOULD** always enforce a maximum timeout, regardless of progress notifications, to limit the impact of a misbehaving client or server.


[​](#error-handling)

Error Handling

Implementations **SHOULD** be prepared to handle these error cases:

- Protocol version mismatch
- Failure to negotiate required capabilities
- Request [timeouts](#timeouts)

Example initialization error:

```python
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32602,
    "message": "Unsupported protocol version",
    "data": {
      "supported": ["2024-11-05"],
      "requested": "1.0.0"
    }
  }
}
```
