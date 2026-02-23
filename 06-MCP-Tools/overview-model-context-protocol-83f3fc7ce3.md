---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:24Z"
source_url: "https://modelcontextprotocol.io/specification/2025-03-26/basic"
title: "Overview - Model Context Protocol"
---

[Skip to main content](#content-area)

[Model Context Protocol home page](/)

Version 2025-03-26

Search...

⌘K

- [Blog](https://blog.modelcontextprotocol.io)
- [GitHub](https://github.com/modelcontextprotocol)

Search...

Navigation

Base Protocol

Overview

[Documentation](/docs/getting-started/intro)

[Extensions](/extensions/overview)

[Specification](/specification/2025-11-25)

[Registry](/registry/about)

[Community](/community/contributing)

- [](/specification/2025-03-26)
  Specification

&nbsp;

- [](/specification/2025-03-26/changelog)
  Key Changes

&nbsp;

- [](/specification/2025-03-26/architecture)
  Architecture

##### Base Protocol

- [](/specification/2025-03-26/basic)
  Overview

- [](/specification/2025-03-26/basic/lifecycle)
  Lifecycle

- [](/specification/2025-03-26/basic/transports)
  Transports

- [](/specification/2025-03-26/basic/authorization)
  Authorization

- Utilities

##### Client Features

- [](/specification/2025-03-26/client/roots)
  Roots
- [](/specification/2025-03-26/client/sampling)
  Sampling

##### Server Features

- [](/specification/2025-03-26/server)
  Overview

- [](/specification/2025-03-26/server/prompts)
  Prompts

- [](/specification/2025-03-26/server/resources)
  Resources

- [](/specification/2025-03-26/server/tools)
  Tools

- Utilities

On this page

- [Messages](#messages)
- [Requests](#requests)
- [Responses](#responses)
- [Notifications](#notifications)
- [Batching](#batching)
- [Auth](#auth)
- [Schema](#schema)

Base Protocol

# Overview

Copy page

Copy page

**Protocol Revision**: 2025-03-26

The Model Context Protocol consists of several key components that work together:

- **Base Protocol**: Core JSON-RPC message types
- **Lifecycle Management**: Connection initialization, capability negotiation, and session control
- **Server Features**: Resources, prompts, and tools exposed by servers
- **Client Features**: Sampling and root directory lists provided by clients
- **Utilities**: Cross-cutting concerns like logging and argument completion

All implementations **MUST** support the base protocol and lifecycle management components. Other components **MAY** be implemented based on the specific needs of the application. These protocol layers establish clear separation of concerns while enabling rich interactions between clients and servers. The modular design allows implementations to support exactly the features they need.

## 

[​](#messages)

Messages

All messages between MCP clients and servers **MUST** follow the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) specification. The protocol defines these types of messages:

### 

[​](#requests)

Requests

Requests are sent from the client to the server or vice versa, to initiate an operation.

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

### 

[​](#responses)

Responses

Responses are sent in reply to requests, containing the result or error of the operation.

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
- **Responses** are further sub-categorized as either **successful results** or **errors**. Either a `result` or an `error` **MUST** be set. A response **MUST NOT** set both.
- Results **MAY** follow any JSON object structure, while errors **MUST** include an error code and message at minimum.
- Error codes **MUST** be integers.

### 

[​](#notifications)

Notifications

Notifications are sent from the client to the server or vice versa, as a one-way message. The receiver **MUST NOT** send a response.

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

### 

[​](#batching)

Batching

JSON-RPC also defines a means to [batch multiple requests and notifications](https://www.jsonrpc.org/specification#batch), by sending them in an array. MCP implementations **MAY** support sending JSON-RPC batches, but **MUST** support receiving JSON-RPC batches.

## 

[​](#auth)

Auth

MCP provides an [Authorization](/specification/2025-03-26/basic/authorization) framework for use with HTTP. Implementations using an HTTP-based transport **SHOULD** conform to this specification, whereas implementations using STDIO transport **SHOULD NOT** follow this specification, and instead retrieve credentials from the environment. Additionally, clients and servers **MAY** negotiate their own custom authentication and authorization strategies. For further discussions and contributions to the evolution of MCP’s auth mechanisms, join us in [GitHub Discussions](https://github.com/modelcontextprotocol/specification/discussions) to help shape the future of the protocol!

## 

[​](#schema)

Schema

The full specification of the protocol is defined as a [TypeScript schema](https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.ts). This is the source of truth for all protocol messages and structures. There is also a [JSON Schema](https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-03-26/schema.json), which is automatically generated from the TypeScript source of truth, for use with various automated tooling.

Was this page helpful?

Yes

No

[Architecture](/specification/2025-03-26/architecture/index)[Lifecycle](/specification/2025-03-26/basic/lifecycle)

[github](https://github.com/modelcontextprotocol)
