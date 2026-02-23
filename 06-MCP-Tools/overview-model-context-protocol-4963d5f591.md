---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:37Z"
source_url: "https://modelcontextprotocol.io/specification/draft/server"
title: "Overview - Model Context Protocol"
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

Server Features

Overview

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

Server Features

# Overview

Copy page

Copy page

**Protocol Revision**: draft

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

[](/specification/draft/server/prompts)

## Prompts

[](/specification/draft/server/resources)

## Resources

[](/specification/draft/server/tools)

## Tools

Was this page helpful?

Yes

No

[Elicitation](/specification/draft/client/elicitation)[Prompts](/specification/draft/server/prompts)

[github](https://github.com/modelcontextprotocol)
