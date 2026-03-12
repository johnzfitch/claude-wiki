---
category: "06-MCP-Tools"
fetched_at: "2026-03-12T08:19:15Z"
source_url: "https://modelcontextprotocol.io/specification/2024-11-05/server/resources"
title: "Resources - Model Context Protocol"
---

# Resources


The Model Context Protocol (MCP) provides a standardized way for servers to expose resources to clients. Resources allow servers to share data that provides context to language models, such as files, database schemas, or application-specific information. Each resource is uniquely identified by a [URI](https://datatracker.ietf.org/doc/html/rfc3986).

## 

[​](#user-interaction-model)

User Interaction Model

Resources in MCP are designed to be **application-driven**, with host applications determining how to incorporate context based on their needs. For example, applications could:

- Expose resources through UI elements for explicit selection, in a tree or list view
- Allow the user to search through and filter available resources
- Implement automatic context inclusion, based on heuristics or the AI model’s selection

However, implementations are free to expose resources through any interface pattern that suits their needs—the protocol itself does not mandate any specific user interaction model.

## 

[​](#capabilities)

Capabilities

Servers that support resources **MUST** declare the `resources` capability:

Copy

``` shiki
{
  "capabilities": {
    "resources": {
      "subscribe": true,
      "listChanged": true
    }
  }
}
```

The capability supports two optional features:

- `subscribe`: whether the client can subscribe to be notified of changes to individual resources.
- `listChanged`: whether the server will emit notifications when the list of available resources changes.

Both `subscribe` and `listChanged` are optional—servers can support neither, either, or both:

Copy

``` shiki
{
  "capabilities": {
    "resources": {} // Neither feature supported
  }
}
```

Copy

``` shiki
{
  "capabilities": {
    "resources": {
      "subscribe": true // Only subscriptions supported
    }
  }
}
```

Copy

``` shiki
{
  "capabilities": {
    "resources": {
      "listChanged": true // Only list change notifications supported
    }
  }
}
```

## 

[​](#protocol-messages)

Protocol Messages

### 

[​](#listing-resources)

Listing Resources

To discover available resources, clients send a `resources/list` request. This operation supports [pagination](/specification/2024-11-05/server/utilities/pagination). **Request:**

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "resources/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}
```

**Response:**

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "resources": [
      {
        "uri": "file:///project/src/main.rs",
        "name": "main.rs",
        "description": "Primary application entry point",
        "mimeType": "text/x-rust"
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```

### 

[​](#reading-resources)

Reading Resources

To retrieve resource contents, clients send a `resources/read` request: **Request:**

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "resources/read",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}
```

**Response:**

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "contents": [
      {
        "uri": "file:///project/src/main.rs",
        "mimeType": "text/x-rust",
        "text": "fn main() {\n    println!(\"Hello world!\");\n}"
      }
    ]
  }
}
```

### 

[​](#resource-templates)

Resource Templates

Resource templates allow servers to expose parameterized resources using [URI templates](https://datatracker.ietf.org/doc/html/rfc6570). Arguments may be auto-completed through [the completion API](/specification/2024-11-05/server/utilities/completion). This operation supports [pagination](/specification/2024-11-05/server/utilities/pagination). **Request:**

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "resources/templates/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}
```

**Response:**

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "resourceTemplates": [
      {
        "uriTemplate": "file:///{path}",
        "name": "Project Files",
        "description": "Access files in the project directory",
        "mimeType": "application/octet-stream"
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```

### 

[​](#list-changed-notification)

List Changed Notification

When the list of available resources changes, servers that declared the `listChanged` capability **SHOULD** send a notification:

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/list_changed"
}
```

### 

[​](#subscriptions)

Subscriptions

The protocol supports optional subscriptions to resource changes. Clients can subscribe to specific resources and receive notifications when they change: **Subscribe Request:**

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "resources/subscribe",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}
```

**Update Notification:**

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/updated",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}
```

## 

[​](#message-flow)

Message Flow

## 

[​](#data-types)

Data Types

### 

[​](#resource)

Resource

A resource definition includes:

- `uri`: Unique identifier for the resource
- `name`: Human-readable name
- `description`: Optional description
- `mimeType`: Optional MIME type

### 

[​](#resource-contents)

Resource Contents

Resources can contain either text or binary data:

#### 

[​](#text-content)

Text Content

Copy

``` shiki
{
  "uri": "file:///example.txt",
  "mimeType": "text/plain",
  "text": "Resource content"
}
```

#### 

[​](#binary-content)

Binary Content

Copy

``` shiki
{
  "uri": "file:///example.png",
  "mimeType": "image/png",
  "blob": "base64-encoded-data"
}
```

## 

[​](#common-uri-schemes)

Common URI Schemes

The protocol defines several standard URI schemes. This list not exhaustive—implementations are always free to use additional, custom URI schemes.

### 

[​](#https//)

https://

Used to represent a resource available on the web. Servers **SHOULD** use this scheme only when the client is able to fetch and load the resource directly from the web on its own—that is, it doesn’t need to read the resource via the MCP server. For other use cases, servers **SHOULD** prefer to use another URI scheme, or define a custom one, even if the server will itself be downloading resource contents over the internet.

### 

[​](#file//)

file://

Used to identify resources that behave like a filesystem. However, the resources do not need to map to an actual physical filesystem. MCP servers **MAY** identify file:// resources with an [XDG MIME type](https://specifications.freedesktop.org/shared-mime-info-spec/0.14/ar01s02.html#id-1.3.14), like `inode/directory`, to represent non-regular files (such as directories) that don’t otherwise have a standard MIME type.

### 

[​](#git//)

git://

Git version control integration.

## 

[​](#error-handling)

Error Handling

Servers **SHOULD** return standard JSON-RPC errors for common failure cases:

- Resource not found: `-32002`
- Internal errors: `-32603`

Example error:

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": 5,
  "error": {
    "code": -32002,
    "message": "Resource not found",
    "data": {
      "uri": "file:///nonexistent.txt"
    }
  }
}
```

## 

[​](#security-considerations)

Security Considerations

1.  Servers **MUST** validate all resource URIs
2.  Access controls **SHOULD** be implemented for sensitive resources
3.  Binary data **MUST** be properly encoded
4.  Resource permissions **SHOULD** be checked before operations
