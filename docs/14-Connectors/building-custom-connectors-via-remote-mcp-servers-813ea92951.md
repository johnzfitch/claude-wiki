---
category: "14-Connectors"
source_url: "https://support.claude.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers"
---


Custom connectors using remote MCP are available on Claude and Claude Desktop for users on Pro, Max, Team, and Enterprise plans.

Building Remote MCP Servers

To get started with remote servers, start with the following resources:

The auth spec, especially details on the auth flow for third-party services.

The remote server examples in the TypeScript and Python SDKs.

The client and server auth implementations in the TypeScript and Python SDKs.

The official MCP roadmap and draft spec’s changelog for details on how the protocol will evolve.

Other resources (like this) may also be helpful to learn about considerations when building, deploying, and troubleshooting remote servers.

 

In addition, some solutions like Cloudflare provide remote MCP server hosting with built-in autoscaling, OAuth token management, and deployment.

 

MCP Support
Platforms

Remote MCP servers are supported on Claude and Claude Desktop for Pro, Max, Team, and Enterprise plans.

To configure remote MCP servers for use in Claude Desktop, add them via Settings > Connectors. Claude Desktop will not connect to remote servers that are configured directly via claude_desktop_config.json.

As of July, Claude for iOS and Android also support remote MCP servers!

Users can use tools, prompts, and resources from remote servers that they’ve already added via claude.ai. Users cannot add new servers directly from Claude Mobile.

Transport and Auth

Claude supports both SSE- and Streamable HTTP-based remote servers, although support for SSE may be deprecated in the coming months.

Claude supports both authless and OAuth-based remote servers.

Auth Support

Claude supports the 3/26 auth spec and (as of July) the 6/18 auth spec.

Claude supports Dynamic Client Registration (DCR).

OAuth servers can signal to Claude that a DCR client has been deleted and that Claude should re-register the client by returning an HTTP 401 with an error of invalid_client from the token endpoint, as described in RFC 6749.

As of July, users are also able to specify a custom client ID and client secret when configuring a server that doesn’t support DCR.

Claude’s OAuth callback URL is https://claude.ai/api/mcp/auth_callback and its OAuth client name is Claude.

This callback URL may change to https://claude.com/api/mcp/auth_callback in the future – if you choose to allowlist MCP client callback URLs, please allowlist this callback URL as well to ensure that your server continues to work with Claude.

Claude supports token expiry and refresh – servers should support this functionality in order to provide the best experience for users.

See here for the IP addresses used by Claude for inbound and outbound connections to MCP servers. Server developers wishing to disallow non-Claude MCP Clients can whitelist these IP addresses, Claude’s OAuth callback URL, and/or Claude’s OAuth client name.

 

Protocol Features

Claude supports tools, prompts, and resources.

Claude supports text- and image-based tool results.

Claude supports text- and binary- based resources.

Claude does not yet support resource subscriptions, sampling, and other more advanced or draft capabilities.

Testing Remote MCP Servers

The best way to test and validate a server is to try adding it to Claude. 

 

Alternatively, use the inspector tool. This will allow you to validate:

that your server successfully initiates and completes the auth flow.

that your server correctly implements various parts of the auth flow.

which tools, prompts, resources, and other MCP features your server exposes.

 

 

See the MCP documentation for more details on using inspector and for other tips on how to debug and troubleshoot your server.

 

In addition, other solutions like Cloudflare’s AI Playground allow you to test remote MCP server functionality.

Related Articles
Getting started with custom connectors using remote MCP
Pre-built Web Connectors Using Remote MCP
Anthropic Connectors Directory FAQ
Remote MCP Server Submission Guide
Building Desktop Extensions with MCPB