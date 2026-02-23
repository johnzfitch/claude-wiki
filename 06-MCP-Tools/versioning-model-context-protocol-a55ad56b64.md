---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:38Z"
source_url: "https://modelcontextprotocol.io/specification/versioning"
title: "Versioning - Model Context Protocol"
---

[Skip to main content](#content-area)

[Model Context Protocol home page](/)

Search...

⌘K

- [Blog](https://blog.modelcontextprotocol.io)
- [GitHub](https://github.com/modelcontextprotocol)

Search...

Navigation

About MCP

Versioning

[Documentation](/docs/getting-started/intro)

[Extensions](/extensions/overview)

[Specification](/specification/2025-11-25)

[Registry](/registry/about)

[Community](/community/contributing)

##### Get started

- [](/docs/getting-started/intro)
  What is MCP?

##### About MCP

- [](/docs/learn/architecture)
  Architecture
- [](/docs/learn/server-concepts)
  Servers
- [](/docs/learn/client-concepts)
  Clients
- [](/specification/versioning)
  Versioning

##### Develop with MCP

- [](/docs/develop/connect-local-servers)
  Connect to local MCP servers

- [](/docs/develop/connect-remote-servers)
  Connect to remote MCP Servers

- [](/docs/develop/build-server)
  Build an MCP server

- [](/docs/develop/build-client)
  Build an MCP client

- [](/docs/sdk)
  SDKs

- Security

##### Developer tools

- [](/docs/tools/inspector)
  MCP Inspector

On this page

- [Revisions](#revisions)
- [Negotiation](#negotiation)

About MCP

# Versioning

Copy page

Copy page

The Model Context Protocol uses string-based version identifiers following the format `YYYY-MM-DD`, to indicate the last date backwards incompatible changes were made.

The protocol version will *not* be incremented when the protocol is updated, as long as the changes maintain backwards compatibility. This allows for incremental improvements while preserving interoperability.

## 

[​](#revisions)

Revisions

Revisions may be marked as:

- **Draft**: in-progress specifications, not yet ready for consumption.
- **Current**: the current protocol version, which is ready for use and may continue to receive backwards compatible changes.
- **Final**: past, complete specifications that will not be changed.

The **current** protocol version is [**2025-11-25**](/specification/2025-11-25).

## 

[​](#negotiation)

Negotiation

Version negotiation happens during [initialization](/specification/latest/basic/lifecycle#initialization). Clients and servers **MAY** support multiple protocol versions simultaneously, but they **MUST** agree on a single version to use for the session. The protocol provides appropriate error handling if version negotiation fails, allowing clients to gracefully terminate connections when they cannot find a version compatible with the server.

Was this page helpful?

Yes

No

[Clients](/docs/learn/client-concepts)[Connect to local MCP servers](/docs/develop/connect-local-servers)

[github](https://github.com/modelcontextprotocol)
