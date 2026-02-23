---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:26Z"
source_url: "https://modelcontextprotocol.io/specification/2025-03-26/server/utilities/pagination"
title: "Pagination - Model Context Protocol"
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

Utilities

Pagination

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

  - [](/specification/2025-03-26/server/utilities/completion)
    Completion
  - [](/specification/2025-03-26/server/utilities/logging)
    Logging
  - [](/specification/2025-03-26/server/utilities/pagination)
    Pagination

On this page

- [Pagination Model](#pagination-model)
- [Response Format](#response-format)
- [Request Format](#request-format)
- [Pagination Flow](#pagination-flow)
- [Operations Supporting Pagination](#operations-supporting-pagination)
- [Implementation Guidelines](#implementation-guidelines)
- [Error Handling](#error-handling)

Utilities

# Pagination

Copy page

Copy page

**Protocol Revision**: 2025-03-26

The Model Context Protocol (MCP) supports paginating list operations that may return large result sets. Pagination allows servers to yield results in smaller chunks rather than all at once. Pagination is especially important when connecting to external services over the internet, but also useful for local integrations to avoid performance issues with large data sets.

## 

[​](#pagination-model)

Pagination Model

Pagination in MCP uses an opaque cursor-based approach, instead of numbered pages.

- The **cursor** is an opaque string token, representing a position in the result set
- **Page size** is determined by the server, and clients **MUST NOT** assume a fixed page size

## 

[​](#response-format)

Response Format

Pagination starts when the server sends a **response** that includes:

- The current page of results
- An optional `nextCursor` field if more results exist

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": "123",
  "result": {
    "resources": [...],
    "nextCursor": "eyJwYWdlIjogM30="
  }
}
```

## 

[​](#request-format)

Request Format

After receiving a cursor, the client can *continue* paginating by issuing a request including that cursor:

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "method": "resources/list",
  "params": {
    "cursor": "eyJwYWdlIjogMn0="
  }
}
```

## 

[​](#pagination-flow)

Pagination Flow

## 

[​](#operations-supporting-pagination)

Operations Supporting Pagination

The following MCP operations support pagination:

- `resources/list` - List available resources
- `resources/templates/list` - List resource templates
- `prompts/list` - List available prompts
- `tools/list` - List available tools

## 

[​](#implementation-guidelines)

Implementation Guidelines

1.  Servers **SHOULD**:
    - Provide stable cursors
    - Handle invalid cursors gracefully
2.  Clients **SHOULD**:
    - Treat a missing `nextCursor` as the end of results
    - Support both paginated and non-paginated flows
3.  Clients **MUST** treat cursors as opaque tokens:
    - Don’t make assumptions about cursor format
    - Don’t attempt to parse or modify cursors
    - Don’t persist cursors across sessions

## 

[​](#error-handling)

Error Handling

Invalid cursors **SHOULD** result in an error with code -32602 (Invalid params).

Was this page helpful?

Yes

No

[Logging](/specification/2025-03-26/server/utilities/logging)

[github](https://github.com/modelcontextprotocol)
