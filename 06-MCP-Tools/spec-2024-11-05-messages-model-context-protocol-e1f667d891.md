---
category: "06-MCP-Tools"
fetched_at: "2026-03-12T08:19:14Z"
source_url: "https://modelcontextprotocol.io/specification/2024-11-05/basic/messages"
title: "Messages - Model Context Protocol"
---

# Messages


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
