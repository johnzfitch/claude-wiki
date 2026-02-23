---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:23Z"
source_url: "https://modelcontextprotocol.io/specification/2024-11-05/basic/messages"
title: "Messages - Model Context Protocol"
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

Base Protocol

Messages

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

- [Requests](#requests)
- [Responses](#responses)
- [Notifications](#notifications)

Base Protocol

# Messages

Copy page

Copy page

**Protocol Revision**: 2024-11-05

All messages in MCP **MUST** follow the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) specification. The protocol defines three types of messages:

## 

[​](#requests)

Requests

Requests are sent from the client to the server or vice versa.

Copy

``` shiki
{
  jsonrpc: "2.0";
  id: string | number;
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

- Requests **MUST** include a string or integer ID.
- Unlike base JSON-RPC, the ID **MUST NOT** be `null`.
- The request ID **MUST NOT** have been previously used by the requestor within the same session.

## 

[​](#responses)

Responses

Responses are sent in reply to requests.

Copy

``` shiki
{
  jsonrpc: "2.0";
  id: string | number;
  result?: {
    [key: string]: unknown;
  }
  error?: {
    code: number;
    message: string;
    data?: unknown;
  }
}
```

- Responses **MUST** include the same ID as the request they correspond to.
- Either a `result` or an `error` **MUST** be set. A response **MUST NOT** set both.
- Error codes **MUST** be integers.

## 

[​](#notifications)

Notifications

Notifications are sent from the client to the server or vice versa. They do not expect a response.

Copy

``` shiki
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

- Notifications **MUST NOT** include an ID.

Was this page helpful?

Yes

No

[Lifecycle](/specification/2024-11-05/basic/lifecycle)[Transports](/specification/2024-11-05/basic/transports)

[github](https://github.com/modelcontextprotocol)
