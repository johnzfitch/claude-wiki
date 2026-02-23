---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:34Z"
source_url: "https://modelcontextprotocol.io/specification/draft/basic/utilities/progress"
title: "Progress - Model Context Protocol"
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

Progress

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

- [Progress Flow](#progress-flow)
- [Behavior Requirements](#behavior-requirements)
- [Implementation Notes](#implementation-notes)

Utilities

# Progress

Copy page

Copy page

**Protocol Revision**: draft

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
- An optional “message” value

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "method": "notifications/progress",
  "params": {
    "progressToken": "abc123",
    "progress": 50,
    "total": 100,
    "message": "Reticulating splines..."
  }
}
```

- The `progress` value **MUST** increase with each notification, even if the total is unknown.
- The `progress` and the `total` values **MAY** be floating point.
- The `message` field **SHOULD** provide relevant human readable progress information.

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
3.  For [task-augmented requests](./tasks), the `progressToken` provided in the original request **MUST** continue to be used for progress notifications throughout the task’s lifetime, even after the `CreateTaskResult` has been returned. The progress token remains valid and associated with the task until the task reaches a terminal status.
    - Progress notifications for tasks **MUST** use the same `progressToken` that was provided in the initial task-augmented request
    - Progress notifications for tasks **MUST** stop after the task reaches a terminal status (`completed`, `failed`, or `cancelled`)

## 

[​](#implementation-notes)

Implementation Notes

- Senders and receivers **SHOULD** track active progress tokens
- Both parties **SHOULD** implement rate limiting to prevent flooding
- Progress notifications **MUST** stop after completion

Was this page helpful?

Yes

No

[Ping](/specification/draft/basic/utilities/ping)[Tasks](/specification/draft/basic/utilities/tasks)

[github](https://github.com/modelcontextprotocol)
