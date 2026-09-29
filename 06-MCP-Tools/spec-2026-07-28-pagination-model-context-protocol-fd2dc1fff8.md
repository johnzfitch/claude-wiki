---
title: "Pagination - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination"
category: "06-MCP-Tools"
fetched_at: "2026-09-29T06:30:30Z"
tags: ["mcp"]
---

## On this page

- [Pagination Model](#pagination-model)
- [Response Format](#response-format)
- [Request Format](#request-format)
- [Pagination Flow](#pagination-flow)
- [Operations Supporting Pagination](#operations-supporting-pagination)
- [Implementation Guidelines](#implementation-guidelines)
- [Error Handling](#error-handling)

Utilities

# Pagination

Copy pageCopy page

Copy pageCopy page

The Model Context Protocol (MCP) supports paginating list operations that may return large result sets. Pagination allows servers to yield results in smaller chunks rather than all at once. Pagination is especially important when connecting to external services over the internet, but also useful for local integrations to avoid performance issues with large data sets.

For brevity, the request examples on this page omit the `_meta` request metadata (`io.modelcontextprotocol/protocolVersion`, `io.modelcontextprotocol/clientInfo`, and `io.modelcontextprotocol/clientCapabilities`). Every request **MUST** include the required `_meta` fields; see [`_meta`](/specification/2026-07-28/basic/index#meta).


[​](#pagination-model)

Pagination Model

Pagination in MCP uses an opaque cursor-based approach, instead of numbered pages.

- The **cursor** is an opaque string token, representing a position in the result set
- **Page size** is determined by the server, and clients **MUST NOT** assume a fixed page size


[​](#response-format)

Response Format

Pagination starts when the server sends a **response** that includes:

- The current page of results
- An optional `nextCursor` field if more results exist

```python
{
  "jsonrpc": "2.0",
  "id": "123",
  "result": {
    "resultType": "complete",
    "resources": [...],
    "nextCursor": "eyJwYWdlIjogM30=",
    "ttlMs": 300000,
    "cacheScope": "public"
  }
}
```


[​](#request-format)

Request Format

After receiving a cursor, the client can *continue* paginating by issuing a request including that cursor:

```python
{
  "jsonrpc": "2.0",
  "id": "124",
  "method": "resources/list",
  "params": {
    "cursor": "eyJwYWdlIjogMn0="
  }
}
```


[​](#pagination-flow)

Pagination Flow


[​](#operations-supporting-pagination)

Operations Supporting Pagination

The following MCP operations support pagination:

- `resources/list` - List available resources
- `resources/templates/list` - List resource templates
- `prompts/list` - List available prompts
- `tools/list` - List available tools


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
    - Don’t make any determination based on cursor value other than whether a non-null value was provided (e.g. an empty string is a valid cursor and thus **MUST NOT** be treated as the end of results)


[​](#error-handling)

Error Handling

Invalid cursors **SHOULD** result in an error with code -32602 (Invalid params).
