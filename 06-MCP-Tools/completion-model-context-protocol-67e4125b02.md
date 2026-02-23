---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:38Z"
source_url: "https://modelcontextprotocol.io/specification/draft/server/utilities/completion"
title: "Completion - Model Context Protocol"
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

Completion

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

  - [](/specification/draft/server/utilities/completion)
    Completion
  - [](/specification/draft/server/utilities/logging)
    Logging
  - [](/specification/draft/server/utilities/pagination)
    Pagination

- [](/specification/draft/schema)
  Schema Reference

On this page

- [User Interaction Model](#user-interaction-model)
- [Capabilities](#capabilities)
- [Protocol Messages](#protocol-messages)
- [Requesting Completions](#requesting-completions)
- [Reference Types](#reference-types)
- [Completion Results](#completion-results)
- [Message Flow](#message-flow)
- [Data Types](#data-types)
- [CompleteRequest](#completerequest)
- [CompleteResult](#completeresult)
- [Error Handling](#error-handling)
- [Implementation Considerations](#implementation-considerations)
- [Security](#security)

Utilities

# Completion

Copy page

Copy page

**Protocol Revision**: draft

The Model Context Protocol (MCP) provides a standardized way for servers to offer autocompletion suggestions for the arguments of prompts and resource templates. When users are filling in argument values for a specific prompt (identified by name) or resource template (identified by URI), servers can provide contextual suggestions.

## 

[​](#user-interaction-model)

User Interaction Model

Completion in MCP is designed to support interactive user experiences similar to IDE code completion. For example, applications may show completion suggestions in a dropdown or popup menu as users type, with the ability to filter and select from available options. However, implementations are free to expose completion through any interface pattern that suits their needs—the protocol itself does not mandate any specific user interaction model.

## 

[​](#capabilities)

Capabilities

Servers that support completions **MUST** declare the `completions` capability:

Copy

``` shiki
{
  "capabilities": {
    "completions": {}
  }
}
```

## 

[​](#protocol-messages)

Protocol Messages

### 

[​](#requesting-completions)

Requesting Completions

To get completion suggestions, clients send a `completion/complete` request specifying what is being completed through a reference type: **Request:**

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "completion/complete",
  "params": {
    "ref": {
      "type": "ref/prompt",
      "name": "code_review"
    },
    "argument": {
      "name": "language",
      "value": "py"
    }
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
    "completion": {
      "values": ["python", "pytorch", "pyside"],
      "total": 10,
      "hasMore": true
    }
  }
}
```

For prompts or URI templates with multiple arguments, clients should include previous completions in the `context.arguments` object to provide context for subsequent requests. **Request:**

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "completion/complete",
  "params": {
    "ref": {
      "type": "ref/prompt",
      "name": "code_review"
    },
    "argument": {
      "name": "framework",
      "value": "fla"
    },
    "context": {
      "arguments": {
        "language": "python"
      }
    }
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
    "completion": {
      "values": ["flask"],
      "total": 1,
      "hasMore": false
    }
  }
}
```

### 

[​](#reference-types)

Reference Types

The protocol supports two types of completion references:

| Type | Description | Example |
|----|----|----|
| `ref/prompt` | References a prompt by name | `{"type": "ref/prompt", "name": "code_review"}` |
| `ref/resource` | References a resource URI | `{"type": "ref/resource", "uri": "file:///{path}"}` |

### 

[​](#completion-results)

Completion Results

Servers return an array of completion values ranked by relevance, with:

- Maximum 100 items per response
- Optional total number of available matches
- Boolean indicating if additional results exist

## 

[​](#message-flow)

Message Flow

## 

[​](#data-types)

Data Types

### 

[​](#completerequest)

CompleteRequest

- `ref`: A `PromptReference` or `ResourceReference`
- `argument`: Object containing:
  - `name`: Argument name
  - `value`: Current value
- `context`: Object containing:
  - `arguments`: A mapping of already-resolved argument names to their values.

### 

[​](#completeresult)

CompleteResult

- `completion`: Object containing:
  - `values`: Array of suggestions (max 100)
  - `total`: Optional total matches
  - `hasMore`: Additional results flag

## 

[​](#error-handling)

Error Handling

Servers **SHOULD** return standard JSON-RPC errors for common failure cases:

- Method not found: `-32601` (Capability not supported)
- Invalid prompt name: `-32602` (Invalid params)
- Missing required arguments: `-32602` (Invalid params)
- Internal errors: `-32603` (Internal error)

## 

[​](#implementation-considerations)

Implementation Considerations

1.  Servers **SHOULD**:
    - Return suggestions sorted by relevance
    - Implement fuzzy matching where appropriate
    - Rate limit completion requests
    - Validate all inputs
2.  Clients **SHOULD**:
    - Debounce rapid completion requests
    - Cache completion results where appropriate
    - Handle missing or partial results gracefully

## 

[​](#security)

Security

Implementations **MUST**:

- Validate all completion inputs
- Implement appropriate rate limiting
- Control access to sensitive suggestions
- Prevent completion-based information disclosure

Was this page helpful?

Yes

No

[Tools](/specification/draft/server/tools)[Logging](/specification/draft/server/utilities/logging)

[github](https://github.com/modelcontextprotocol)
