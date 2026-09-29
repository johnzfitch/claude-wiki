---
title: "Roots - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/specification/draft/client/roots"
category: "06-MCP-Tools"
fetched_at: "2026-09-29T06:31:06Z"
tags: ["mcp"]
---

## On this page

- [User Interaction Model](#user-interaction-model)
- [Capabilities](#capabilities)
- [Protocol Messages](#protocol-messages)
  - [Listing Roots](#listing-roots)
- [Message Flow](#message-flow)
- [Data Types](#data-types)
  - [Root](#root)
  - [Project Directory](#project-directory)
  - [Multiple Repositories](#multiple-repositories)
- [Error Handling](#error-handling)
- [Security Considerations](#security-considerations)
- [Implementation Guidelines](#implementation-guidelines)

Client Features

# Roots

Copy pageCopy page

Copy pageCopy page

**Deprecated**: The Roots feature is deprecated as of protocol version `2026-07-28` ([SEP-2577](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2577)). Under the [feature lifecycle policy](/community/feature-lifecycle), it remains in the specification for at least twelve months after this revision’s release before it becomes eligible for removal. New implementations **SHOULD NOT** adopt it; existing implementations **SHOULD** migrate to passing directories or files via tool parameters, resource URIs, or server configuration. See the [deprecated features registry](/specification/draft/deprecated).

The Model Context Protocol (MCP) provides a standardized way for clients to expose filesystem “roots” to servers. Roots inform servers about the directories and files the client considers relevant, so that servers can focus their operations accordingly. They are informational guidance rather than an access-control mechanism. The protocol does not enforce that servers stay within roots. Servers can request the list of roots from supporting clients.


[​](#user-interaction-model)

User Interaction Model

Roots in MCP are typically exposed through workspace or project configuration interfaces. For example, implementations could offer a workspace/project picker that allows users to select directories and files the server should have access to. This can be combined with automatic workspace detection from version control systems or project files. However, implementations are free to expose roots through any interface pattern that suits their needs—the protocol itself does not mandate any specific user interaction model.


[​](#capabilities)

Capabilities

Clients that support roots **MUST** declare the `roots` capability in `_meta.io.modelcontextprotocol/clientCapabilities` on each request:

```python
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```


[​](#protocol-messages)

Protocol Messages


[​](#listing-roots)

Listing Roots

To retrieve roots during the processing of a client request, servers send an `InputRequiredResult` containing a `roots/list` request: **Input request (delivered inside [`InputRequiredResult.inputRequests`](/specification/draft/basic/patterns/mrtr#inputrequests)):**

```python
{
  "method": "roots/list"
}
```

**Client result (returned inside `inputResponses` on the retried request):**

```python
{
  "roots": [
    {
      "uri": "file:///home/user/projects/myproject",
      "name": "My Project"
    }
  ]
}
```


[​](#message-flow)

Message Flow


[​](#data-types)

Data Types


[​](#root)

Root

A root definition includes:

- `uri`: Unique identifier for the root. This **MUST** be a `file://` URI in the current specification.
- `name`: Optional human-readable name for display purposes.

Example roots for different use cases:


[​](#project-directory)

Project Directory

```python
{
  "uri": "file:///home/user/projects/myproject",
  "name": "My Project"
}
```


[​](#multiple-repositories)

Multiple Repositories

```python
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


[​](#error-handling)

Error Handling

If an error occurs, the client does not need to replay the initial call with an error message as the server is not waiting for a response with the `InputRequiredResult` pattern.


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


[​](#implementation-guidelines)

Implementation Guidelines

1.  Clients **SHOULD**:
    - Prompt users for consent before exposing roots to servers
    - Provide clear user interfaces for root management
    - Validate root accessibility before exposing
    - Monitor for root changes
2.  Servers **SHOULD**:
    - Check for roots capability before usage
    - Respect root boundaries in operations
    - Cache root information appropriately
