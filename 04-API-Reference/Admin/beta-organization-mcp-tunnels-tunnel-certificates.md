---
title: "Tunnel Certificates - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/mcp_tunnels/tunnel_certificates"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:35:45Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [MCP Tunnels](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels)

# Tunnel Certificates

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/create)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates

Requires `anthropic-beta: ``mcp-tunnels-2026-05-19`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](../Endpoints/http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [List Tunnel Certificates](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/list)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates

Requires `anthropic-beta: ``mcp-tunnels-2026-05-19`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](../Endpoints/http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Get Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}

Requires `anthropic-beta: ``mcp-tunnels-2026-05-19`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](../Endpoints/http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Archive Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}/archive

Requires `anthropic-beta: ``mcp-tunnels-2026-05-19`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](../Endpoints/http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### Models



BetaOrganizationTunnelCertificate object{ type: "tunnel_certificate", id, archived_at, 4 more }





type: "tunnel_certificate"



Object type. Always `tunnel_certificate` for Tunnel Certificates.

defaulttunnel_certificate

id: string



ID of the Tunnel Certificate.



archived_at: string or null



RFC 3339 datetime string indicating when the certificate was archived, or `null` if it is not archived.

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

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel_id: string



ID of the Tunnel this certificate is registered against.
