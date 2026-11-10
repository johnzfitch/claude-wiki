---
title: "Certificates - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/tunnels/certificates"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-05T06:36:15Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)
3.  [Tunnels](platform-claude-com-http-beta-tunnels.md)

# Certificates

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/create)

POST/v1/tunnels/{tunnel_id}/certificates

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. [How to send beta headers](beta-headers.md)

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Get Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/retrieve)

GET/v1/tunnels/{tunnel_id}/certificates/{certificate_id}

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. [How to send beta headers](beta-headers.md)

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [List Tunnel Certificates](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/list)

GET/v1/tunnels/{tunnel_id}/certificates

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. [How to send beta headers](beta-headers.md)

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Archive Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/archive)

POST/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. [How to send beta headers](beta-headers.md)

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### Models



BetaTunnelCertificate object{ type: "tunnel_certificate", id, archived_at, 4 more }



A CA certificate attached to a tunnel.

type: "tunnel_certificate"



id: string



Unique identifier for the certificate, prefixed with `tcrt_`.



archived_at: string or null



RFC 3339 datetime string indicating when the certificate was archived. Null if it is still in the trusted set.

formatdate-time



created_at: string



RFC 3339 datetime string indicating when the certificate was registered.

formatdate-time



expires_at: string or null



RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire.

formatdate-time

fingerprint: string



Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

tunnel_id: string



ID of the tunnel the certificate is registered against.
