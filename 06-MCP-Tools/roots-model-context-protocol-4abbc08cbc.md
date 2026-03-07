---
category: "06-MCP-Tools"
fetched_at: "2026-03-07T01:05:17Z"
source_url: "https://modelcontextprotocol.io/specification/2024-11-05/client/roots"
title: "Roots - Model Context Protocol"
---

# Roots


**Protocol Revision**: 2024-11-05

The Model Context Protocol (MCP) provides a standardized way for clients to expose filesystem “roots” to servers. Roots define the boundaries of where servers can operate within the filesystem, allowing them to understand which directories and files they have access to. Servers can request the list of roots from supporting clients and receive notifications when that list changes.

## 

[​](#user-interaction-model)

User Interaction Model

Roots in MCP are typically exposed through workspace or project configuration interfaces. For example, implementations could offer a workspace/project picker that allows users to select directories and files the server should have access to. This can be combined with automatic workspace detection from version control systems or project files. However, implementations are free to expose roots through any interface pattern that suits their needs—the protocol itself does not mandate any specific user interaction model.

## 

[​](#capabilities)

Capabilities

Clients that support roots **MUST** declare the `roots` capability during [initialization](/specification/2024-11-05/basic/lifecycle#initialization):

Copy

``` shiki
{
  "capabilities": {
    "roots": {
      "listChanged": true
    }
  }
}
```

`listChanged` indicates whether the client will emit notifications when the list of roots changes.

## 

[​](#protocol-messages)

Protocol Messages

### 

[​](#listing-roots)

Listing Roots

To retrieve roots, servers send a `roots/list` request: **Request:**

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "roots/list"
}
```

**Response:**

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "roots": [
      {
        "uri": "file:///home/user/projects/myproject",
        "name": "My Project"
      }
    ]
  }
}
```

### 

[​](#root-list-changes)

Root List Changes

When roots change, clients that support `listChanged` **MUST** send a notification:

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "method": "notifications/roots/list_changed"
}
```

## 

[​](#message-flow)

Message Flow

## 

[​](#data-types)

Data Types

### 

[​](#root)

Root

A root definition includes:

- `uri`: Unique identifier for the root. This **MUST** be a `file://` URI in the current specification.
- `name`: Optional human-readable name for display purposes.

Example roots for different use cases:

#### 

[​](#project-directory)

Project Directory

Copy

``` shiki
{
  "uri": "file:///home/user/projects/myproject",
  "name": "My Project"
}
```

#### 

[​](#multiple-repositories)

Multiple Repositories

Copy

``` shiki
[
  {
    "uri": "file:///home/user/repos/frontend",
    "name": "Frontend Repository"
  },
  {
    "uri": "file:///home/user/repos/backend",
    "name": "Backend Repository"
  }
]
```

## 

[​](#error-handling)

Error Handling

Clients **SHOULD** return standard JSON-RPC errors for common failure cases:

- Client does not support roots: `-32601` (Method not found)
- Internal errors: `-32603`

Example error:

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32601,
    "message": "Roots not supported",
    "data": {
      "reason": "Client does not have roots capability"
    }
  }
}
```

## 

[​](#security-considerations)

Security Considerations

1.  Clients **MUST**:
    - Only expose roots with appropriate permissions
    - Validate all root URIs to prevent path traversal
    - Implement proper access controls
    - Monitor root accessibility
2.  Servers **SHOULD**:
    - Handle cases where roots become unavailable
    - Respect root boundaries during operations
    - Validate all paths against provided roots

## 

[​](#implementation-guidelines)

Implementation Guidelines

1.  Clients **SHOULD**:
    - Prompt users for consent before exposing roots to servers
    - Provide clear user interfaces for root management
    - Validate root accessibility before exposing
    - Monitor for root changes
2.  Servers **SHOULD**:
    - Check for roots capability before usage
    - Handle root list changes gracefully
    - Respect root boundaries in operations
    - Cache root information appropriately
