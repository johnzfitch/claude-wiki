---
category: "14-Connectors"
fetched_at: "2026-02-16T21:12:36Z"
source_url: "https://support.claude.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers"
title: "Building custom connectors via remote MCP servers | Claude Help Center"
---

[](/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

Search for articles...

Table of contents

[](#h_18842a1b95)

[](#h_ed638d686b)

[](#h_b0e7505b75)

[All Collections](/en/)

[Connectors](https://support.claude.com/en/collections/15399129-connectors)

Building custom connectors via remote MCP servers

# Building custom connectors via remote MCP servers

Updated this week

Table of contents

[](#h_18842a1b95)

[](#h_ed638d686b)

[](#h_b0e7505b75)

Custom connectors using remote MCP are available on Claude and Claude Desktop for users on Pro, Max, Team, and Enterprise plans.

## Building remote MCP servers

To get started with remote servers, start with the following resources:

- The [auth spec](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization), especially details on [the auth flow for third-party services](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow).

- The remote server examples in the [TypeScript](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/src/examples/server) and [Python](https://github.com/modelcontextprotocol/python-sdk/tree/main/examples/servers) SDKs.

- The client and server auth implementations in the [TypeScript](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/src/server/auth) and [Python](https://github.com/modelcontextprotocol/python-sdk/tree/main/src/mcp) SDKs.

- The official MCP [roadmap](https://modelcontextprotocol.io/development/roadmap) and [draft spec’s changelog](https://modelcontextprotocol.io/specification/draft/changelog) for details on how the protocol will evolve.

Other resources (like [this](https://simplescraper.io/blog/how-to-mcp)) may also be helpful to learn about considerations when building, deploying, and troubleshooting remote servers.

In addition, some [solutions like Cloudflare](https://developers.cloudflare.com/agents/guides/remote-mcp-server/) provide remote MCP server hosting with built-in autoscaling, OAuth token management, and deployment.

## MCP support

### Platforms

- Remote MCP servers are supported on Claude and Claude Desktop for Pro, Max, Team, and Enterprise plans.

  - To configure remote MCP servers for use in Claude Desktop, add them via [Settings \> Connectors](https://claude.ai/settings/connectors). Claude Desktop will not connect to remote servers that are configured directly via *claude_desktop_config.json*.

- As of July, Claude for iOS and Android also support remote MCP servers!

  - Users can use tools, prompts, and resources from remote servers that they’ve already added via [claude.ai](http://claude.ai). Users cannot add new servers directly from Claude Mobile.

### Transport and auth

- Claude supports both SSE- and Streamable HTTP-based remote servers, although support for SSE may be deprecated in the coming months.

- Claude supports both authless and OAuth-based remote servers.

**Auth support**

- Claude supports the [3/26 auth spec](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#1-introduction) and (as of July) the [6/18 auth spec](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization).

- Claude supports [Dynamic Client Registration](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-4-dynamic-client-registration) (DCR).

  - OAuth servers can signal to Claude that a DCR client has been deleted and that Claude should re-register the client by returning an HTTP 401 with an error of invalid_client from the token endpoint, as described in [RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749#section-5.2).

  - As of July, users are also able to specify a custom client ID and client secret when configuring a server that doesn’t support DCR.

- Claude’s OAuth callback URL is [https://claude.ai/api/mcp/auth_callback](https://claude.ai/api/mcp/auth_callback) and its OAuth client name is Claude.

  - This callback URL may change to [https://claude.com/api/mcp/auth_callback](https://claude.com/api/mcp/auth_callback) in the future – if you choose to allowlist MCP client callback URLs, please allowlist this callback URL as well to ensure that your server continues to work with Claude.

- Claude supports token expiry and refresh – servers should support this functionality in order to provide the best experience for users.

See [here](https://docs.anthropic.com/en/api/ip-addresses#ipv4-2) for the IP addresses used by Claude for inbound and outbound connections to MCP servers. Server developers wishing to disallow non-Claude MCP Clients can whitelist these IP addresses, Claude’s OAuth callback URL, and/or Claude’s OAuth client name.

### Protocol Features

- Claude supports tools, prompts, and resources.

  - Claude supports text- and image-based tool results.

  - Claude supports text- and binary- based resources.

- Claude does not yet support resource subscriptions, sampling, and other more advanced or draft capabilities.

## Testing remote MCP servers

The best way to test and validate a server is to try [adding it to Claude](https://support.anthropic.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp#h_3d1a65aded).

Alternatively, use the [inspector tool](https://github.com/modelcontextprotocol/inspector). This will allow you to validate:

- that your server successfully initiates and completes the auth flow.

- that your server correctly implements various parts of the auth flow.

- which tools, prompts, resources, and other MCP features your server exposes.

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1553912673/2d4c61c44a57ca3ad98c05fbb7d1/AD_4nXc-tmHASMQNJRwv3W64SVaojlwe5NqtOr_s9ZYXdmHP1LgBVmb_9fbjBBCUweeerCVsT52ZM5t6lEIzZXPZDY1mYy50H9Pbrlt0ygVVpInpainwVW6-pStYpIwvDJd6wqILHfFFEg?expires=1771277400&signature=83a59143d58c861c72231bf3a283f6cca3d7255d8791fd5fd80c5fa8ee7bf7ff&req=dSUiFcB%2Fn4dYWvMW1HO4za06rLNqQOSkYCouPsdkSdZeR29DFxJpoO0dus1K%0Aymo6uIbKp8lD0TgvSdI%3D%0A)

See the [MCP documentation](https://modelcontextprotocol.io/docs/tools/inspector) for more details on using inspector and for other tips on how to debug and troubleshoot your server.

In addition, other solutions like [Cloudflare’s AI Playground](https://playground.ai.cloudflare.com/) allow you to test remote MCP server functionality.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)

Getting started with custom connectors using remote MCP

[](https://support.claude.com/en/articles/11176164-pre-built-web-connectors-using-remote-mcp)

Pre-built web connectors using remote MCP

[](https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq)

Anthropic Connectors Directory FAQ

[](https://support.claude.com/en/articles/12922490-remote-mcp-server-submission-guide)

Remote MCP Server Submission Guide

[](https://support.claude.com/en/articles/12922929-building-desktop-extensions-with-mcpb)

Building Desktop Extensions with MCPB

Did this answer your question?

😞

😐

😃

[](/en/)

- [Product](https://www.anthropic.com/product)
- [Research](https://www.anthropic.com/research)
- [Company](https://www.anthropic.com/company)
- [News](https://www.anthropic.com/news)
- [Careers](https://www.anthropic.com/careers)

- [Terms of Service - Consumer](https://www.anthropic.com/terms)
- [Terms of Service - Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Privacy Policy](https://www.anthropic.com/privacy)
- [Usage Policy](https://www.anthropic.com/aup)
- [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Compliance](https://trust.anthropic.com/)
