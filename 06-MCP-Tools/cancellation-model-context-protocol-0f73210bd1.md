---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:30Z"
source_url: "https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/cancellation"
title: "Cancellation - Model Context Protocol"
---

[Skip to main content](#content-area)

[Model Context Protocol home page](/)

Version 2025-11-25 (latest)

Search...

⌘K

- [Blog](https://blog.modelcontextprotocol.io)
- [GitHub](https://github.com/modelcontextprotocol)

Search...

Navigation

Utilities

Cancellation

[Documentation](/docs/getting-started/intro)

[Extensions](/extensions/overview)

[Specification](/specification/2025-11-25)

[Registry](/registry/about)

[Community](/community/contributing)

- [](/specification/2025-11-25)
  Specification

&nbsp;

- [](/specification/2025-11-25/changelog)
  Key Changes

&nbsp;

- [](/specification/2025-11-25/architecture)
  Architecture

##### Base Protocol

- [](/specification/2025-11-25/basic)
  Overview

- [](/specification/2025-11-25/basic/lifecycle)
  Lifecycle

- [](/specification/2025-11-25/basic/transports)
  Transports

- [](/specification/2025-11-25/basic/authorization)
  Authorization

- Utilities

  - [](/specification/2025-11-25/basic/utilities/cancellation)
    Cancellation
  - [](/specification/2025-11-25/basic/utilities/ping)
    Ping
  - [](/specification/2025-11-25/basic/utilities/progress)
    Progress
  - [](/specification/2025-11-25/basic/utilities/tasks)
    Tasks

##### Client Features

- [](/specification/2025-11-25/client/roots)
  Roots
- [](/specification/2025-11-25/client/sampling)
  Sampling
- [](/specification/2025-11-25/client/elicitation)
  Elicitation

##### Server Features

- [](/specification/2025-11-25/server)
  Overview

- [](/specification/2025-11-25/server/prompts)
  Prompts

- [](/specification/2025-11-25/server/resources)
  Resources

- [](/specification/2025-11-25/server/tools)
  Tools

- Utilities

- [](/specification/2025-11-25/schema)
  Schema Reference

On this page

- [Cancellation Flow](#cancellation-flow)
- [Behavior Requirements](#behavior-requirements)
- [Timing Considerations](#timing-considerations)
- [Implementation Notes](#implementation-notes)
- [Error Handling](#error-handling)

Utilities

# Cancellation

Copy page

Copy page

**Protocol Revision**: 2025-11-25

The Model Context Protocol (MCP) supports optional cancellation of in-progress requests through notification messages. Either side can send a cancellation notification to indicate that a previously-issued request should be terminated.

## 

[​](#cancellation-flow)

Cancellation Flow

When a party wants to cancel an in-progress request, it sends a `notifications/cancelled` notification containing:

- The ID of the request to cancel
- An optional reason string that can be logged or displayed

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "method": "notifications/cancelled",
  "params": {
    "requestId": "123",
    "reason": "User requested cancellation"
  }
}
```

## 

[​](#behavior-requirements)

Behavior Requirements

1.  Cancellation notifications **MUST** only reference requests that:
    - Were previously issued in the same direction
    - Are believed to still be in-progress
2.  The `initialize` request **MUST NOT** be cancelled by clients
3.  For [task-augmented requests](./tasks), the `tasks/cancel` request **MUST** be used instead of the `notifications/cancelled` notification. Tasks have their own dedicated cancellation mechanism that returns the final task state.
4.  Receivers of cancellation notifications **SHOULD**:
    - Stop processing the cancelled request
    - Free associated resources
    - Not send a response for the cancelled request
5.  Receivers **MAY** ignore cancellation notifications if:
    - The referenced request is unknown
    - Processing has already completed
    - The request cannot be cancelled
6.  The sender of the cancellation notification **SHOULD** ignore any response to the request that arrives afterward

## 

[​](#timing-considerations)

Timing Considerations

Due to network latency, cancellation notifications may arrive after request processing has completed, and potentially after a response has already been sent. Both parties **MUST** handle these race conditions gracefully:

## 

[​](#implementation-notes)

Implementation Notes

- Both parties **SHOULD** log cancellation reasons for debugging
- Application UIs **SHOULD** indicate when cancellation is requested

## 

[​](#error-handling)

Error Handling

Invalid cancellation notifications **SHOULD** be ignored:

- Unknown request IDs
- Already completed requests
- Malformed notifications

This maintains the “fire and forget” nature of notifications while allowing for race conditions in asynchronous communication.

Was this page helpful?

Yes

No

[Authorization](/specification/2025-11-25/basic/authorization)[Ping](/specification/2025-11-25/basic/utilities/ping)

[github](https://github.com/modelcontextprotocol)
