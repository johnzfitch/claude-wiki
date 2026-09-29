---
title: "Ping - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/ping"
category: "06-MCP-Tools"
fetched_at: "2026-09-29T06:30:58Z"
tags: ["mcp"]
---

## On this page

- [Overview](#overview)
- [Message Format](#message-format)
- [Behavior Requirements](#behavior-requirements)
- [Usage Patterns](#usage-patterns)
- [Implementation Considerations](#implementation-considerations)
- [Error Handling](#error-handling)

Utilities

# Ping

Copy pageCopy page

Copy pageCopy page

The Model Context Protocol includes an optional ping mechanism that allows either party to verify that their counterpart is still responsive and the connection is alive.


[​](#overview)

Overview

The ping functionality is implemented through a simple request/response pattern. Either the client or server can initiate a ping by sending a `ping` request.


[​](#message-format)

Message Format

A ping request is a standard JSON-RPC request with no parameters:

```python
{
  "jsonrpc": "2.0",
  "id": "123",
  "method": "ping"
}
```


[​](#behavior-requirements)

Behavior Requirements

1.  The receiver **MUST** respond promptly with an empty response:

```python
{
  "jsonrpc": "2.0",
  "id": "123",
  "result": {}
}
```

2.  If no response is received within a reasonable timeout period, the sender **MAY**:
    - Consider the connection stale
    - Terminate the connection
    - Attempt reconnection procedures


[​](#usage-patterns)

Usage Patterns


[​](#implementation-considerations)

Implementation Considerations

- Implementations **SHOULD** periodically issue pings to detect connection health
- The frequency of pings **SHOULD** be configurable
- Timeouts **SHOULD** be appropriate for the network environment
- Excessive pinging **SHOULD** be avoided to reduce network overhead


[​](#error-handling)

Error Handling

- Timeouts **SHOULD** be treated as connection failures
- Multiple failed pings **MAY** trigger connection reset
- Implementations **SHOULD** log ping failures for diagnostics
