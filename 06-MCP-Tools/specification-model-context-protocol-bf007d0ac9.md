---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:35Z"
source_url: "https://modelcontextprotocol.io/specification/draft"
title: "Specification - Model Context Protocol"
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

Specification

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

- [](/specification/draft/schema)
  Schema Reference

On this page

- [Overview](#overview)
- [Key Details](#key-details)
- [Base Protocol](#base-protocol)
- [Features](#features)
- [Additional Utilities](#additional-utilities)
- [Security and Trust & Safety](#security-and-trust-%26-safety)
- [Key Principles](#key-principles)
- [Implementation Guidelines](#implementation-guidelines)
- [Learn More](#learn-more)

# Specification

Copy page

Copy page

[Model Context Protocol](https://modelcontextprotocol.io) (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and tools. Whether you’re building an AI-powered IDE, enhancing a chat interface, or creating custom AI workflows, MCP provides a standardized way to connect LLMs with the context they need. This specification defines the authoritative protocol requirements, based on the TypeScript schema in [schema.ts](https://github.com/modelcontextprotocol/specification/blob/main/schema/draft/schema.ts). For implementation guides and examples, visit [modelcontextprotocol.io](https://modelcontextprotocol.io). The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “NOT RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in [BCP 14](https://datatracker.ietf.org/doc/html/bcp14) \[[RFC2119](https://datatracker.ietf.org/doc/html/rfc2119)\] \[[RFC8174](https://datatracker.ietf.org/doc/html/rfc8174)\] when, and only when, they appear in all capitals, as shown here.

## 

[​](#overview)

Overview

MCP provides a standardized way for applications to:

- Share contextual information with language models
- Expose tools and capabilities to AI systems
- Build composable integrations and workflows

The protocol uses [JSON-RPC](https://www.jsonrpc.org/) 2.0 messages to establish communication between:

- **Hosts**: LLM applications that initiate connections
- **Clients**: Connectors within the host application
- **Servers**: Services that provide context and capabilities

MCP takes some inspiration from the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/), which standardizes how to add support for programming languages across a whole ecosystem of development tools. In a similar way, MCP standardizes how to integrate additional context and tools into the ecosystem of AI applications.

## 

[​](#key-details)

Key Details

### 

[​](#base-protocol)

Base Protocol

- [JSON-RPC](https://www.jsonrpc.org/) message format
- Stateful connections
- Server and client capability negotiation

### 

[​](#features)

Features

Servers offer any of the following features to clients:

- **Resources**: Context and data, for the user or the AI model to use
- **Prompts**: Templated messages and workflows for users
- **Tools**: Functions for the AI model to execute

Clients may offer the following features to servers:

- **Sampling**: Server-initiated agentic behaviors and recursive LLM interactions
- **Roots**: Server-initiated inquiries into URI or filesystem boundaries to operate in
- **Elicitation**: Server-initiated requests for additional information from users

### 

[​](#additional-utilities)

Additional Utilities

- Configuration
- Progress tracking
- Cancellation
- Error reporting
- Logging

## 

[​](#security-and-trust-&-safety)

Security and Trust & Safety

The Model Context Protocol enables powerful capabilities through arbitrary data access and code execution paths. With this power comes important security and trust considerations that all implementors must carefully address.

### 

[​](#key-principles)

Key Principles

1.  **User Consent and Control**
    - Users must explicitly consent to and understand all data access and operations
    - Users must retain control over what data is shared and what actions are taken
    - Implementors should provide clear UIs for reviewing and authorizing activities
2.  **Data Privacy**
    - Hosts must obtain explicit user consent before exposing user data to servers
    - Hosts must not transmit resource data elsewhere without user consent
    - User data should be protected with appropriate access controls
3.  **Tool Safety**
    - Tools represent arbitrary code execution and must be treated with appropriate caution.
      - In particular, descriptions of tool behavior such as annotations should be considered untrusted, unless obtained from a trusted server.
    - Hosts must obtain explicit user consent before invoking any tool
    - Users should understand what each tool does before authorizing its use
4.  **LLM Sampling Controls**
    - Users must explicitly approve any LLM sampling requests
    - Users should control:
      - Whether sampling occurs at all
      - The actual prompt that will be sent
      - What results the server can see
    - The protocol intentionally limits server visibility into prompts

### 

[​](#implementation-guidelines)

Implementation Guidelines

While MCP itself cannot enforce these security principles at the protocol level, implementors **SHOULD**:

1.  Build robust consent and authorization flows into their applications
2.  Provide clear documentation of security implications
3.  Implement appropriate access controls and data protections
4.  Follow security best practices in their integrations
5.  Consider privacy implications in their feature designs

## 

[​](#learn-more)

Learn More

Explore the detailed specification for each protocol component:

[](/specification/draft/architecture)

## Architecture

[](/specification/draft/basic)

## Base Protocol

[](/specification/draft/server)

## Server Features

[](/specification/draft/client)

## Client Features

[](/community/contributing)

## Contributing

Was this page helpful?

Yes

No

[Key Changes](/specification/draft/changelog)

[github](https://github.com/modelcontextprotocol)
