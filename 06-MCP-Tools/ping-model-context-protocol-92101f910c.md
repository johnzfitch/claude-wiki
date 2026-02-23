---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:34Z"
source_url: "https://modelcontextprotocol.io/specification/draft/basic/utilities/ping"
title: "Ping - Model Context Protocol"
---

[Skip to main content](#content-area)

[Model Context Protocol home page](/)

Draft

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

- [](/specification/draft)
  Specification

&nbsp;

- [](/specification/draft/changelog)
  Key Changes

&nbsp;

- [](/specification/draft/architecture)
  Architecture

##### Base Protocol

- [](/specification/draft/basic)
  Overview

- [](/specification/draft/basic/lifecycle)
  Lifecycle

- [](/specification/draft/basic/transports)
  Transports

- [](/specification/draft/basic/authorization)
  Authorization

- Utilities

  - [](/specification/draft/basic/utilities/cancellation)
    Cancellation
  - [](/specification/draft/basic/utilities/ping)
    Ping
  - [](/specification/draft/basic/utilities/progress)
    Progress
  - [](/specification/draft/basic/utilities/tasks)
    Tasks

##### Client Features

- [](/specification/draft/client/roots)
  Roots
- [](/specification/draft/client/sampling)
  Sampling
- [](/specification/draft/client/elicitation)
  Elicitation

##### Server Features

- [](/specification/draft/server)
  Overview

- [](/specification/draft/server/prompts)
  Prompts

- [](/specification/draft/server/resources)
  Resources

- [](/specification/draft/server/tools)
  Tools

- Utilities

- [](/specification/draft/schema)
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

**Protocol Revision**: draft

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

[Cancellation](/specification/draft/basic/utilities/cancellation)[Progress](/specification/draft/basic/utilities/progress)

[github](https://github.com/modelcontextprotocol)
