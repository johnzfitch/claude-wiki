---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:25Z"
source_url: "https://modelcontextprotocol.io/specification/2025-03-26/server"
title: "Overview - Model Context Protocol"
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

Server Features

Overview

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

Server Features

# Overview

Copy page

Copy page

**Protocol Revision**: 2025-03-26

Servers provide the fundamental building blocks for adding context to language models via MCP. These primitives enable rich interactions between clients, servers, and language models:

- **Prompts**: Pre-defined templates or instructions that guide language model interactions
- **Resources**: Structured data or content that provides additional context to the model
- **Tools**: Executable functions that allow models to perform actions or retrieve information

Each primitive can be summarized in the following control hierarchy:

| Primitive | Control | Description | Example |
|----|----|----|----|
| Prompts | User-controlled | Interactive templates invoked by user choice | Slash commands, menu options |
| Resources | Application-controlled | Contextual data attached and managed by the client | File contents, git history |
| Tools | Model-controlled | Functions exposed to the LLM to take actions | API POST requests, file writing |

Explore these key primitives in more detail below:

[](/specification/2025-03-26/server/prompts)

## Prompts

[](/specification/2025-03-26/server/resources)

## Resources

[](/specification/2025-03-26/server/tools)

## Tools

Was this page helpful?

Yes

No

[Sampling](/specification/2025-03-26/client/sampling)[Prompts](/specification/2025-03-26/server/prompts)

[github](https://github.com/modelcontextprotocol)
