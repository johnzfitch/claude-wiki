---
title: "Tunnels - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/tunnels"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:34:24Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)

# Tunnels

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create Tunnel](platform-claude-com-http-beta-tunnels-create.md)

POST/v1/tunnels

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. Learn [how to send beta headers](beta-headers.md).

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Get Tunnel](platform-claude-com-http-beta-tunnels-retrieve.md)

GET/v1/tunnels/{tunnel_id}

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. Learn [how to send beta headers](beta-headers.md).

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [List Tunnels](platform-claude-com-http-beta-tunnels-list.md)

GET/v1/tunnels

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. Learn [how to send beta headers](beta-headers.md).

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Archive Tunnel](platform-claude-com-http-beta-tunnels-archive.md)

POST/v1/tunnels/{tunnel_id}/archive

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. Learn [how to send beta headers](beta-headers.md).

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Reveal Tunnel Token](platform-claude-com-http-beta-tunnels-reveal-token.md)

POST/v1/tunnels/{tunnel_id}/reveal_token

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. Learn [how to send beta headers](beta-headers.md).

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Rotate Tunnel Token](platform-claude-com-http-beta-tunnels-rotate-token.md)

POST/v1/tunnels/{tunnel_id}/rotate_token

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. Learn [how to send beta headers](beta-headers.md).

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### Models



BetaTunnel object{ type: "tunnel", id, archived_at, 3 more }



An MCP tunnel.

type: "tunnel"



id: string



Unique identifier for the tunnel, prefixed with `tnl_`.



archived_at: string or null



RFC 3339 datetime string indicating when the tunnel was archived. Null if it is not archived.

formatdate-time



created_at: string



RFC 3339 datetime string indicating when the tunnel was created.

formatdate-time

display_name: string or null



Human-readable name for the tunnel (1-255 characters). Null if unset.

domain: string



Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.



BetaTunnelToken object{ type: "tunnel_token", id, tunnel_token }



A tunnel's connector token.

type: "tunnel_token"



id: string



Stable identifier for the current token value. Changes when the token is rotated.

tunnel_token: string



The connector token used to run the tunnel. Treat as a credential.

#### Tunnels[Certificates](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates)

##### [Create Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/create)

POST/v1/tunnels/{tunnel_id}/certificates

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. Learn [how to send beta headers](beta-headers.md).

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Get Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/retrieve)

GET/v1/tunnels/{tunnel_id}/certificates/{certificate_id}

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. Learn [how to send beta headers](beta-headers.md).

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [List Tunnel Certificates](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/list)

GET/v1/tunnels/{tunnel_id}/certificates

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. Learn [how to send beta headers](beta-headers.md).

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Archive Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/archive)

POST/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. Learn [how to send beta headers](beta-headers.md).

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.
