---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:25Z"
source_url: "https://modelcontextprotocol.io/specification/2025-03-26/changelog"
title: "Key Changes - Model Context Protocol"
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

Key Changes

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

On this page

- [Major changes](#major-changes)
- [Other schema changes](#other-schema-changes)
- [Full changelog](#full-changelog)

# Key Changes

Copy page

Copy page

This document lists changes made to the Model Context Protocol (MCP) specification since the previous revision, [2024-11-05](/specification/2024-11-05).

## 

[​](#major-changes)

Major changes

1.  Added a comprehensive **[authorization framework](/specification/2025-03-26/basic/authorization)** based on OAuth 2.1 (PR [\#133](https://github.com/modelcontextprotocol/specification/pull/133))
2.  Replaced the previous HTTP+SSE transport with a more flexible **[Streamable HTTP transport](/specification/2025-03-26/basic/transports#streamable-http)** (PR [\#206](https://github.com/modelcontextprotocol/specification/pull/206))
3.  Added support for JSON-RPC **[batching](https://www.jsonrpc.org/specification#batch)** (PR [\#228](https://github.com/modelcontextprotocol/specification/pull/228))
4.  Added comprehensive **tool annotations** for better describing tool behavior, like whether it is read-only or destructive (PR [\#185](https://github.com/modelcontextprotocol/specification/pull/185))

## 

[​](#other-schema-changes)

Other schema changes

- Added `message` field to `ProgressNotification` to provide descriptive status updates
- Added support for audio data, joining the existing text and image content types
- Added `completions` capability to explicitly indicate support for argument autocompletion suggestions

See [the updated schema](http://github.com/modelcontextprotocol/specification/tree/main/schema/2025-03-26/schema.ts) for more details.

## 

[​](#full-changelog)

Full changelog

For a complete list of all changes that have been made since the last protocol revision, [see GitHub](https://github.com/modelcontextprotocol/specification/compare/2024-11-05...2025-03-26).

Was this page helpful?

Yes

No

[Specification](/specification/2025-03-26)[Architecture](/specification/2025-03-26/architecture/index)

[github](https://github.com/modelcontextprotocol)
