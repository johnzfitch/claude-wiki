---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:23Z"
source_url: "https://modelcontextprotocol.io/specification/2024-11-05/basic/utilities/progress"
title: "Progress - Model Context Protocol"
---

[Skip to main content](#content-area)

[Model Context Protocol home page](/)

Version 2024-11-05

Search...

⌘K

- [Blog](https://blog.modelcontextprotocol.io)
- [GitHub](https://github.com/modelcontextprotocol)

Search...

Navigation

Utilities

Progress

[Documentation](/docs/getting-started/intro)

[Extensions](/extensions/overview)

[Specification](/specification/2025-11-25)

[Registry](/registry/about)

[Community](/community/contributing)

- [](/specification/2024-11-05)
  Specification

&nbsp;

- [](/specification/2024-11-05/architecture)
  Architecture

##### Base Protocol

- [](/specification/2024-11-05/basic)
  Overview

- [](/specification/2024-11-05/basic/lifecycle)
  Lifecycle

- [](/specification/2024-11-05/basic/messages)
  Messages

- [](/specification/2024-11-05/basic/transports)
  Transports

- Utilities

  - [](/specification/2024-11-05/basic/utilities/cancellation)
    Cancellation
  - [](/specification/2024-11-05/basic/utilities/ping)
    Ping
  - [](/specification/2024-11-05/basic/utilities/progress)
    Progress

##### Client Features

- [](/specification/2024-11-05/client/roots)
  Roots
- [](/specification/2024-11-05/client/sampling)
  Sampling

##### Server Features

- [](/specification/2024-11-05/server)
  Overview

- [](/specification/2024-11-05/server/prompts)
  Prompts

- [](/specification/2024-11-05/server/resources)
  Resources

- [](/specification/2024-11-05/server/tools)
  Tools

- Utilities

On this page

- [Progress Flow](#progress-flow)
- [Behavior Requirements](#behavior-requirements)
- [Implementation Notes](#implementation-notes)

Utilities

# Progress

Copy page

Copy page

**Protocol Revision**: 2024-11-05

The Model Context Protocol (MCP) supports optional progress tracking for long-running operations through notification messages. Either side can send progress notifications to provide updates about operation status.

## 

[​](#progress-flow)

Progress Flow

When a party wants to *receive* progress updates for a request, it includes a `progressToken` in the request metadata.

- Progress tokens **MUST** be a string or integer value
- Progress tokens can be chosen by the sender using any means, but **MUST** be unique across all active requests.

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "some_method",
  "params": {
    "_meta": {
      "progressToken": "abc123"
    }
  }
}
```

The receiver **MAY** then send progress notifications containing:

- The original progress token
- The current progress value so far
- An optional “total” value

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "method": "notifications/progress",
  "params": {
    "progressToken": "abc123",
    "progress": 50,
    "total": 100
  }
}
```

- The `progress` value **MUST** increase with each notification, even if the total is unknown.
- The `progress` and the `total` values **MAY** be floating point.

## 

[​](#behavior-requirements)

Behavior Requirements

1.  Progress notifications **MUST** only reference tokens that:
    - Were provided in an active request
    - Are associated with an in-progress operation
2.  Receivers of progress requests **MAY**:
    - Choose not to send any progress notifications
    - Send notifications at whatever frequency they deem appropriate
    - Omit the total value if unknown

## 

[​](#implementation-notes)

Implementation Notes

- Senders and receivers **SHOULD** track active progress tokens
- Both parties **SHOULD** implement rate limiting to prevent flooding
- Progress notifications **MUST** stop after completion

Was this page helpful?

Yes

No

[Ping](/specification/2024-11-05/basic/utilities/ping)[Roots](/specification/2024-11-05/client/roots)

[github](https://github.com/modelcontextprotocol)
