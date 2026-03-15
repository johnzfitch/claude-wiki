---
category: "14-Connectors"
fetched_at: "2026-03-15T12:17:01Z"
source_url: "https://support.claude.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers"
title: "Building custom connectors via remote MCP servers | Claude Help Center"
---

3.  Building custom connectors via remote MCP servers

# Building custom connectors via remote MCP servers

Updated yesterday


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


See the [MCP documentation](https://modelcontextprotocol.io/docs/tools/inspector) for more details on using inspector and for other tips on how to debug and troubleshoot your server.

In addition, other solutions like [Cloudflare’s AI Playground](https://playground.ai.cloudflare.com/) allow you to test remote MCP server functionality.

------------------------------------------------------------------------

Related Articles


Get started with custom connectors using remote MCP


Anthropic Connectors Directory FAQ


Deploying enterprise-grade MCP servers with desktop extensions


Remote MCP Server Submission Guide


Building Desktop Extensions with MCPB
