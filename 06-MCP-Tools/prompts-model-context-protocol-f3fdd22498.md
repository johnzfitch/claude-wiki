---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:24Z"
source_url: "https://modelcontextprotocol.io/specification/2024-11-05/server/prompts"
title: "Prompts - Model Context Protocol"
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

Server Features

Prompts

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

- [User Interaction Model](#user-interaction-model)
- [Capabilities](#capabilities)
- [Protocol Messages](#protocol-messages)
- [Listing Prompts](#listing-prompts)
- [Getting a Prompt](#getting-a-prompt)
- [List Changed Notification](#list-changed-notification)
- [Message Flow](#message-flow)
- [Data Types](#data-types)
- [Prompt](#prompt)
- [PromptMessage](#promptmessage)
- [Text Content](#text-content)
- [Image Content](#image-content)
- [Embedded Resources](#embedded-resources)
- [Error Handling](#error-handling)
- [Implementation Considerations](#implementation-considerations)
- [Security](#security)

Server Features

# Prompts

Copy page

Copy page

**Protocol Revision**: 2024-11-05

The Model Context Protocol (MCP) provides a standardized way for servers to expose prompt templates to clients. Prompts allow servers to provide structured messages and instructions for interacting with language models. Clients can discover available prompts, retrieve their contents, and provide arguments to customize them.

## 

[​](#user-interaction-model)

User Interaction Model

Prompts are designed to be **user-controlled**, meaning they are exposed from servers to clients with the intention of the user being able to explicitly select them for use. Typically, prompts would be triggered through user-initiated commands in the user interface, which allows users to naturally discover and invoke available prompts. For example, as slash commands: However, implementors are free to expose prompts through any interface pattern that suits their needs—the protocol itself does not mandate any specific user interaction model.

## 

[​](#capabilities)

Capabilities

Servers that support prompts **MUST** declare the `prompts` capability during [initialization](/specification/2024-11-05/basic/lifecycle#initialization):

Copy

``` shiki
{
  "capabilities": {
    "prompts": {
      "listChanged": true
    }
  }
}
```

`listChanged` indicates whether the server will emit notifications when the list of available prompts changes.

## 

[​](#protocol-messages)

Protocol Messages

### 

[​](#listing-prompts)

Listing Prompts

To retrieve available prompts, clients send a `prompts/list` request. This operation supports [pagination](/specification/2024-11-05/server/utilities/pagination). **Request:**

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "prompts/list",
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
    "prompts": [
      {
        "name": "code_review",
        "description": "Asks the LLM to analyze code quality and suggest improvements",
        "arguments": [
          {
            "name": "code",
            "description": "The code to review",
            "required": true
          }
        ]
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}
```

### 

[​](#getting-a-prompt)

Getting a Prompt

To retrieve a specific prompt, clients send a `prompts/get` request. Arguments may be auto-completed through [the completion API](/specification/2024-11-05/server/utilities/completion). **Request:**

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "prompts/get",
  "params": {
    "name": "code_review",
    "arguments": {
      "code": "def hello():\n    print('world')"
    }
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
    "description": "Code review prompt",
    "messages": [
      {
        "role": "user",
        "content": {
          "type": "text",
          "text": "Please review this Python code:\ndef hello():\n    print('world')"
        }
      }
    ]
  }
}
```

### 

[​](#list-changed-notification)

List Changed Notification

When the list of available prompts changes, servers that declared the `listChanged` capability **SHOULD** send a notification:

Copy

``` shiki
{
  "jsonrpc": "2.0",
  "method": "notifications/prompts/list_changed"
}
```

## 

[​](#message-flow)

Message Flow

## 

[​](#data-types)

Data Types

### 

[​](#prompt)

Prompt

A prompt definition includes:

- `name`: Unique identifier for the prompt
- `description`: Optional human-readable description
- `arguments`: Optional list of arguments for customization

### 

[​](#promptmessage)

PromptMessage

Messages in a prompt can contain:

- `role`: Either “user” or “assistant” to indicate the speaker
- `content`: One of the following content types:

#### 

[​](#text-content)

Text Content

Text content represents plain text messages:

Copy

``` shiki
{
  "type": "text",
  "text": "The text content of the message"
}
```

This is the most common content type used for natural language interactions.

#### 

[​](#image-content)

Image Content

Image content allows including visual information in messages:

Copy

``` shiki
{
  "type": "image",
  "data": "base64-encoded-image-data",
  "mimeType": "image/png"
}
```

The image data **MUST** be base64-encoded and include a valid MIME type. This enables multi-modal interactions where visual context is important.

#### 

[​](#embedded-resources)

Embedded Resources

Embedded resources allow referencing server-side resources directly in messages:

Copy

``` shiki
{
  "type": "resource",
  "resource": {
    "uri": "resource://example",
    "mimeType": "text/plain",
    "text": "Resource content"
  }
}
```

Resources can contain either text or binary (blob) data and **MUST** include:

- A valid resource URI
- The appropriate MIME type
- Either text content or base64-encoded blob data

Embedded resources enable prompts to seamlessly incorporate server-managed content like documentation, code samples, or other reference materials directly into the conversation flow.

## 

[​](#error-handling)

Error Handling

Servers **SHOULD** return standard JSON-RPC errors for common failure cases:

- Invalid prompt name: `-32602` (Invalid params)
- Missing required arguments: `-32602` (Invalid params)
- Internal errors: `-32603` (Internal error)

## 

[​](#implementation-considerations)

Implementation Considerations

1.  Servers **SHOULD** validate prompt arguments before processing
2.  Clients **SHOULD** handle pagination for large prompt lists
3.  Both parties **SHOULD** respect capability negotiation

## 

[​](#security)

Security

Implementations **MUST** carefully validate all prompt inputs and outputs to prevent injection attacks or unauthorized access to resources.

Was this page helpful?

Yes

No

[Overview](/specification/2024-11-05/server)[Resources](/specification/2024-11-05/server/resources)

[github](https://github.com/modelcontextprotocol)
