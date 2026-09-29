---
title: "Debugging - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/docs/draft/tools/debugging"
category: "06-MCP-Tools/General"
fetched_at: "2026-08-02T05:39:25Z"
tags: ["mcp"]
---

## On this page

- [Debugging tools overview](#debugging-tools-overview)
- [Implementing logging](#implementing-logging)
  - [Server-side logging](#server-side-logging)
- [Common issues](#common-issues)
  - [Working directory](#working-directory)
  - [Environment variables](#environment-variables)
  - [Server startup](#server-startup)
  - [Connection problems](#connection-problems)
- [Debugging in Claude Desktop](#debugging-in-claude-desktop)
  - [Checking server status](#checking-server-status)
  - [Viewing logs](#viewing-logs)
  - [Using Chrome DevTools](#using-chrome-devtools)
- [Debugging workflow](#debugging-workflow)
  - [Development cycle](#development-cycle)
  - [Testing changes](#testing-changes)
- [Best practices](#best-practices)
  - [Logging strategy](#logging-strategy)
  - [Security considerations](#security-considerations)
- [Getting help](#getting-help)
- [Next steps](#next-steps)

Developer tools

# Debugging

Copy pageCopy page

A comprehensive guide to debugging Model Context Protocol (MCP) integrations

Copy pageCopy page

Effective debugging is essential when developing MCP servers or integrating them with applications. This guide covers the debugging tools and approaches available in the MCP ecosystem.


[​](#debugging-tools-overview)

Debugging tools overview

MCP provides several tools for debugging at different levels:

1.  **[MCP Inspector](2026-07-28-tools-inspector.md)**: interactive, transport-agnostic testing UI. Connect to stdio or Streamable HTTP servers, invoke [tools](https://modelcontextprotocol.io/specification/latest/server/tools), [prompts](https://modelcontextprotocol.io/specification/latest/server/prompts), and [resources](https://modelcontextprotocol.io/specification/latest/server/resources), and watch the notification stream. This should be your first stop.
2.  **Server logging**: structured logs to stderr (stdio transport) or via [OpenTelemetry](https://opentelemetry.io/) (all transports). [Logging](../Spec/2026-07-28-server-utilities-logging.md) over the protocol (`notifications/message`) is deprecated as of protocol version `2026-07-28`.
3.  **Client developer tools**: most MCP clients expose logs and connection state. See [Debugging in Claude Desktop](#debugging-in-claude-desktop) below for one example, or consult your client’s documentation.


[​](#implementing-logging)

Implementing logging


[​](#server-side-logging)

Server-side logging

When building a server that uses the local [stdio transport](../Spec/2026-07-28-basic-transports-stdio.md), all messages logged to stderr (standard error) will be captured by the host application automatically.

Local MCP servers should not log messages to stdout (standard out), as this will interfere with protocol operation.

For servers using the [Streamable HTTP transport](../Spec/draft-basic-transports-streamable-http.md), stderr is not captured by the client. Use your own server-side log aggregation or [OpenTelemetry](https://opentelemetry.io/) for logs, and standard HTTP tooling (curl, browser DevTools Network panel) to inspect requests and SSE streams.

The `notifications/message` mechanism below is deprecated as of protocol version `2026-07-28`. It remains available during the deprecation window.

For all [transports](https://modelcontextprotocol.io/specification/latest/basic/transports), record what the server is doing as it runs:

Python

TypeScript

```python
import logging

from mcp.server import MCPServer

logger = logging.getLogger(__name__)

mcp = MCPServer("reports")


@mcp.tool()
async def fetch_report(report_id: str) -> str:
    """Fetch a report by id."""
    logger.info("Fetching report %s", report_id)
    return f"Report {report_id} is ready."
```

```python
await server.sendLoggingMessage({
  level: "info",
  data: "Server started successfully",
});
```

MCP defines eight [RFC 5424 severity levels](https://modelcontextprotocol.io/specification/latest/server/utilities/logging#log-levels) (`debug` through `emergency`). Clients opt in to log messages per request by setting the [`io.modelcontextprotocol/logLevel`](../Spec/2026-07-28-server-utilities-logging.md#per-request-log-level) field in the request’s `_meta`. Servers must not send `notifications/message` for requests that omit this field. Important events to log:

- Startup steps
- Resource access
- Tool execution
- Error conditions
- Performance metrics


[​](#common-issues)

Common issues

The examples below use Claude Desktop’s [`claude_desktop_config.json`](draft-develop-connect-local-servers.md); the same principles apply to any stdio-based MCP client.


[​](#working-directory)

Working directory

When an MCP client launches a stdio server:

- The working directory for servers launched via the client’s config may be undefined (like `/` on macOS) since the client could be started from anywhere
- Always use absolute paths in your configuration and `.env` files to ensure reliable operation
- For testing servers directly via command line, the working directory will be where you run the command

For example in `claude_desktop_config.json`, use:

```python
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/username/data"
      ]
    }
  }
}
```

Instead of relative paths like `./data`


[​](#environment-variables)

Environment variables

MCP servers launched over stdio inherit only a limited subset of environment variables automatically (the exact set is platform-dependent). To override the default variables or provide your own, you can specify an `env` key in `claude_desktop_config.json`:

```python
{
  "mcpServers": {
    "myserver": {
      "command": "mcp-server-myapp",
      "env": {
        "MYAPP_API_KEY": "some_key"
      }
    }
  }
}
```


[​](#server-startup)

Server startup

Common startup problems:

1.  **Path Issues**
    - Incorrect server executable path
    - Missing required files
    - Permission problems
    - Try using an absolute path for `command`
2.  **Configuration Errors**
    - Invalid JSON syntax
    - Missing required fields
    - Type mismatches
3.  **Environment Problems**
    - Missing environment variables
    - Incorrect variable values
    - Permission restrictions


[​](#connection-problems)

Connection problems

When servers fail to connect:

1.  Check client logs
2.  Verify server process is running
3.  Test standalone with [Inspector](2026-07-28-tools-inspector.md)
4.  Verify [protocol compatibility](draft-learn-versioning.md#negotiation): call [`server/discover`](../Spec/2026-07-28-server-discover.md) to see which protocol versions the server supports. An `UnsupportedProtocolVersionError` (`-32022`) lists the server’s supported versions in its `data` field
5.  Check the [per-request `_meta` fields](https://modelcontextprotocol.io/specification/draft/basic/index#meta): every request must carry `io.modelcontextprotocol/protocolVersion` and `io.modelcontextprotocol/clientCapabilities`, and clients should also include `io.modelcontextprotocol/clientInfo`. A request missing either required field is rejected with error `-32602` (Invalid params), the same code returned for many other malformed inputs. If the server needs a capability the request’s `clientCapabilities` did not declare, such as [elicitation](../Spec/2026-07-28-client-elicitation.md), it returns a `MissingRequiredClientCapabilityError` (`-32021`) naming the missing capabilities. Inspect the request’s `_meta` and the [`server/discover`](../Spec/2026-07-28-server-discover.md) response to verify both sides declared what you expect


[​](#debugging-in-claude-desktop)

Debugging in Claude Desktop

Claude Desktop is one of many MCP clients. It is available on macOS and Windows.


[​](#checking-server-status)

Checking server status

Click the “Add files, connectors, and more” plus icon in the chat input, then hover over the **Connectors** menu to see connected servers and available tools.


[​](#viewing-logs)

Viewing logs

Log files are written to:

- macOS: `~/Library/Logs/Claude`
- Windows: `%APPDATA%\Claude\logs`

macOS

Windows

```python
tail -n 20 -F ~/Library/Logs/Claude/mcp*.log
```

```python
type "$env:AppData\Claude\logs\mcp*.log"
```

The logs capture:

- Server connection events
- Configuration issues
- Runtime errors
- Message exchanges


[​](#using-chrome-devtools)

Using Chrome DevTools

Access Chrome’s developer tools inside Claude Desktop to investigate client-side errors:

1.  Create a `developer_settings.json` file with `allowDevTools` set to true:

macOS

Windows

```python
echo '{"allowDevTools": true}' > ~/Library/Application\ Support/Claude/developer_settings.json
```

```python
'{"allowDevTools": true}' | Set-Content "$env:AppData\Claude\developer_settings.json"
```

2.  Open DevTools: `Command-Option-I` (macOS) or `Ctrl+Alt+I` (Windows)

Note: You’ll see two DevTools windows:

- Main content window
- App title bar window

Use the Console panel to inspect client-side errors. Use the Network panel to inspect:

- Message payloads
- Connection timing


[​](#debugging-workflow)

Debugging workflow


[​](#development-cycle)

Development cycle

1.  Initial Development
    - Use [Inspector](2026-07-28-tools-inspector.md) for basic testing
    - Implement core functionality
    - Add logging points
2.  Integration Testing
    - Test in your target MCP client
    - Monitor logs
    - Check error handling


[​](#testing-changes)

Testing changes

To test changes efficiently:

- **Configuration changes**: Restart the MCP client
- **Server code changes**: Restart the client (for Claude Desktop, fully quit and reopen; closing the window is not enough)
- **Quick iteration**: Use [Inspector](2026-07-28-tools-inspector.md) during development


[​](#best-practices)

Best practices


[​](#logging-strategy)

Logging strategy

1.  **Structured Logging**
    - Use consistent formats
    - Include context
    - Add timestamps
    - Track request IDs
2.  **Error Handling**
    - Log stack traces
    - Include error context
    - Track error patterns
    - Monitor recovery
3.  **Performance Tracking**
    - Log operation timing
    - Monitor resource usage
    - Track message sizes
    - Measure latency


[​](#security-considerations)

Security considerations

When debugging:

1.  **Sensitive Data**
    - Sanitize logs
    - Protect credentials
    - Mask personal information
2.  **Access Control**
    - Verify permissions
    - Check authentication
    - Monitor access patterns

For a full treatment of MCP attack vectors and mitigations, see [Security Best Practices](draft-tutorials-security-security-best-practices.md).


[​](#getting-help)

Getting help

When encountering issues:

1.  **First Steps**
    - Check server logs
    - Test with [Inspector](2026-07-28-tools-inspector.md)
    - Review configuration
    - Verify environment
2.  **Support Channels**
    - [GitHub issues](https://github.com/modelcontextprotocol/modelcontextprotocol/issues)
    - [GitHub discussions](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions)
3.  **Providing Information**
    - Log excerpts
    - Configuration files
    - Steps to reproduce
    - Environment details


[​](#next-steps)

Next steps

## MCP Inspector

Learn to use the MCP Inspector

## Build an MCP server

Walk through building a server from scratch

## Connect local servers

Full claude_desktop_config.json reference and troubleshooting
