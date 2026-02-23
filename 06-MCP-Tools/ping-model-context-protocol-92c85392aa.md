---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:27Z"
source_url: "https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/ping"
title: "Ping - Model Context Protocol"
---

[Skip to main content](#content-area)

[Model Context Protocol home page](/)

Version 2025-06-18

Search...

⌘K

- [Blog](https://blog.modelcontextprotocol.io)
- [GitHub](https://github.com/modelcontextprotocol)

Search...

Navigation

Utilities

Ping

[Documentation](/docs/getting-started/intro)

[Extensions](/extensions/overview)

[Specification](/specification/2025-11-25)

[Registry](/registry/about)

[Community](/community/contributing)

- [](/specification/2025-06-18)
  Specification

&nbsp;

- [](/specification/2025-06-18/changelog)
  Key Changes

&nbsp;

- [](/specification/2025-06-18/architecture)
  Architecture

##### Base Protocol

- [](/specification/2025-06-18/basic)
  Overview

- [](/specification/2025-06-18/basic/lifecycle)
  Lifecycle

- [](/specification/2025-06-18/basic/transports)
  Transports

- [](/specification/2025-06-18/basic/authorization)
  Authorization

- Utilities

  - [](/specification/2025-06-18/basic/utilities/cancellation)
    Cancellation
  - [](/specification/2025-06-18/basic/utilities/ping)
    Ping
  - [](/specification/2025-06-18/basic/utilities/progress)
    Progress

##### Client Features

- [](/specification/2025-06-18/client/roots)
  Roots
- [](/specification/2025-06-18/client/sampling)
  Sampling
- [](/specification/2025-06-18/client/elicitation)
  Elicitation

##### Server Features

- [](/specification/2025-06-18/server)
  Overview

- [](/specification/2025-06-18/server/prompts)
  Prompts

- [](/specification/2025-06-18/server/resources)
  Resources

- [](/specification/2025-06-18/server/tools)
  Tools

- Utilities

- [](/specification/2025-06-18/schema)
  Schema Reference

On this page

- [Overview](#overview)
- [Message Format](#message-format)
- [Behavior Requirements](#behavior-requirements)
- [Usage Patterns](#usage-patterns)
- [Implementation Considerations](#implementation-considerations)
- [Error Handling](#error-handling)

Utilities

# Ping

Copy page

Copy page

**Protocol Revision**: 2025-06-18

The Model Context Protocol includes an optional ping mechanism that allows either party to verify that their counterpart is still responsive and the connection is alive.

## 

[​](#overview)

Overview

The ping functionality is implemented through a simple request/response pattern. Either the client or server can initiate a ping by sending a `ping` request.

## 

[​](#message-format)

Message Format

A ping request is a standard JSON-RPC request with no parameters:

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": "123",
  "method": "ping"
}
```

## 

[​](#behavior-requirements)

Behavior Requirements

1.  The receiver **MUST** respond promptly with an empty response:

Copy

``` shiki
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

## 

[​](#usage-patterns)

Usage Patterns

## 

[​](#implementation-considerations)

Implementation Considerations

- Implementations **SHOULD** periodically issue pings to detect connection health
- The frequency of pings **SHOULD** be configurable
- Timeouts **SHOULD** be appropriate for the network environment
- Excessive pinging **SHOULD** be avoided to reduce network overhead

## 

[​](#error-handling)

Error Handling

- Timeouts **SHOULD** be treated as connection failures
- Multiple failed pings **MAY** trigger connection reset
- Implementations **SHOULD** log ping failures for diagnostics

Was this page helpful?

Yes

No

[Cancellation](/specification/2025-06-18/basic/utilities/cancellation)[Progress](/specification/2025-06-18/basic/utilities/progress)

[github](https://github.com/modelcontextprotocol)
