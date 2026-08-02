---
title: "Messages - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/specification/2024-11-05/basic/messages"
category: "06-MCP-Tools"
fetched_at: "2026-08-02T05:38:46Z"
tags: ["mcp"]
---

## On this page

- [Requests](#requests)
- [Responses](#responses)
- [Notifications](#notifications)

Base Protocol

# Messages

Copy pageCopy page

Copy pageCopy page

All messages in MCP **MUST** follow the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) specification. The protocol defines three types of messages:


[​](#requests)

Requests

Requests are sent from the client to the server or vice versa.

```python
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


[​](#responses)

Responses

Responses are sent in reply to requests.

```python
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


[​](#notifications)

Notifications

Notifications are sent from the client to the server or vice versa. They do not expect a response.

```python
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

- Notifications **MUST NOT** include an ID.
