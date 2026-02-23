---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:21Z"
source_url: "https://modelcontextprotocol.io/extensions/client-matrix"
title: "Extension Support Matrix - Model Context Protocol"
---

[Skip to main content](#content-area)

[Model Context Protocol home page](/)

Search...

⌘K

- [Blog](https://blog.modelcontextprotocol.io)
- [GitHub](https://github.com/modelcontextprotocol)

Search...

Navigation

Extension Support Matrix

[Documentation](/docs/getting-started/intro)

[Extensions](/extensions/overview)

[Specification](/specification/2025-11-25)

[Registry](/registry/about)

[Community](/community/contributing)

- [](/extensions/overview)
  Extensions Overview

&nbsp;

- [](/extensions/client-matrix)
  Extension Support Matrix

##### MCP Apps

- [](/extensions/apps/overview)
  MCP Apps
- [](/extensions/apps/build)
  Build an MCP App

##### Authorization Extensions

- [](/extensions/auth/overview)
  Authorization Extensions
- [](/extensions/auth/oauth-client-credentials)
  OAuth Client Credentials
- [](/extensions/auth/enterprise-managed-authorization)
  Enterprise-Managed Authorization

On this page

- [Extension overview](#extension-overview)
- [Support matrix](#support-matrix)
- [Adding extension support to your client](#adding-extension-support-to-your-client)

# Extension Support Matrix

Copy page

Which MCP clients implement which official extensions

Copy page

This matrix shows which MCP clients support each [official extension](/extensions/overview). Extensions are always opt-in — a client only uses an extension if both client and server declare support during the [initialization handshake](/extensions/overview#negotiation).

This list is maintained by the community. If you notice any inaccuracies or would like to add or update information, please [submit a pull request](https://github.com/modelcontextprotocol/modelcontextprotocol/pulls).

## 

[​](#extension-overview)

Extension overview

| Extension | Identifier | Description |
|----|----|----|
| [MCP Apps](/extensions/apps/overview) | `io.modelcontextprotocol/ui` | Interactive HTML interfaces rendered inline in the conversation |
| [OAuth Client Credentials](/extensions/auth/oauth-client-credentials) | `io.modelcontextprotocol/oauth-client-credentials` | Machine-to-machine auth without interactive user login |
| [Enterprise-Managed Authorization](/extensions/auth/enterprise-managed-authorization) | `io.modelcontextprotocol/enterprise-managed-authorization` | Centralized access control via enterprise IdP |

## 

[​](#support-matrix)

Support matrix

| Client | [MCP Apps](/extensions/apps/overview) | [OAuth Client Credentials](/extensions/auth/oauth-client-credentials) | [Enterprise Auth](/extensions/auth/enterprise-managed-authorization) |
|----|:--:|:--:|:--:|
| [Claude (web)](https://claude.ai) |  |  |  |
| [Claude Desktop](https://claude.ai/download) |  |  |  |
| [VS Code GitHub Copilot](https://code.visualstudio.com/) |  |  |  |
| [Goose](https://block.github.io/goose/) |  |  |  |
| [Postman](https://postman.com) |  |  |  |
| [MCPJam](https://www.mcpjam.com/) |  |  |  |

Auth extension support (OAuth Client Credentials and Enterprise-Managed Authorization) is tracked separately from the core MCP authorization features (DCR, CIMD) shown on the [clients page](/clients). Check each extension’s specification and the [ext-auth repository](https://github.com/modelcontextprotocol/ext-auth) for the latest implementation status.

## 

[​](#adding-extension-support-to-your-client)

Adding extension support to your client

If you’re building an MCP client and want to implement extension support:

1.  Review the extension specification (e.g., in the [ext-auth](https://github.com/modelcontextprotocol/ext-auth) or [ext-apps](https://github.com/modelcontextprotocol/ext-apps) repository)
2.  Declare support in the `extensions` field of your `initialize` capabilities
3.  Implement the extension’s protocol requirements
4.  Submit a pull request to update this matrix

See [Extensions Overview](/extensions/overview#negotiation) for details on the capability negotiation mechanism.

Was this page helpful?

Yes

No

[Extensions Overview](/extensions/overview)[MCP Apps](/extensions/apps/overview)

[github](https://github.com/modelcontextprotocol)
