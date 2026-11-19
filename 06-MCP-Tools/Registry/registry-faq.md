---
title: "Frequently Asked Questions - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/registry/faq"
category: "06-MCP-Tools/Registry"
fetched_at: "2026-11-13T06:32:55Z"
last_modified: "Fri, 13 Nov 2026 02:23:09 GMT"
tags: ["mcp", "mcp-registry"]
---

## On this page

Back to top

- [General](#general)
  - [What is the difference between “Official MCP Registry”, “MCP Registry”, “MCP registry”, “MCP Registry API”, etc?](#what-is-the-difference-between-%E2%80%9Cofficial-mcp-registry%E2%80%9D-%E2%80%9Cmcp-registry%E2%80%9D-%E2%80%9Cmcp-registry%E2%80%9D-%E2%80%9Cmcp-registry-api%E2%80%9D-etc)
  - [Can I delete/unpublish my server?](#can-i-delete%2Funpublish-my-server)
  - [How do I update my server metadata?](#how-do-i-update-my-server-metadata)
  - [Can I add custom metadata when publishing?](#can-i-add-custom-metadata-when-publishing)
- [Reporting Issues](#reporting-issues)
  - [What if I need to report a spam or malicious server?](#what-if-i-need-to-report-a-spam-or-malicious-server)
  - [What if I need to report a security vulnerability in the registry itself?](#what-if-i-need-to-report-a-security-vulnerability-in-the-registry-itself)

# Frequently Asked Questions

Copy pageCopy page

Copy pageCopy page

The MCP Registry is currently in preview. Breaking changes or data resets may occur before general availability. If you encounter any issues, please report them on [GitHub](https://github.com/modelcontextprotocol/registry/issues).


[​](#general)

General


[​](#what-is-the-difference-between-“official-mcp-registry”-“mcp-registry”-“mcp-registry”-“mcp-registry-api”-etc)

What is the difference between “Official MCP Registry”, “MCP Registry”, “MCP registry”, “MCP Registry API”, etc?

- “MCP Registry API” — An API that implements the [OpenAPI spec](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/api/openapi.yaml) defined by the MCP Registry.
- “Official MCP Registry API” — The REST API served at `https://registry.modelcontextprotocol.io`, which is a superset of the MCP Registry API. Its OpenAPI spec can be downloaded from [https://registry.modelcontextprotocol.io/openapi.yaml](https://registry.modelcontextprotocol.io/openapi.yaml).
- “MCP registry” — A third-party service that provides an MCP Registry API.
- “Official MCP Registry” (or “The MCP Registry”) — The service that lives at `https://registry.modelcontextprotocol.io`.


[​](#can-i-delete/unpublish-my-server)

Can I delete/unpublish my server?

Yes, you can change your server’s status to `deleted` using the `mcp-publisher status` command:

```python
# Delete a specific version
mcp-publisher status --status deleted --message "No longer maintained" \
  io.github.my-username/my-server 1.0.0

# Delete all versions
mcp-publisher status --status deleted --all-versions --message "Project archived" \
  io.github.my-username/my-server
```

Deleted servers are hidden from default API listings but can still be retrieved with `include_deleted=true`. You can restore a deleted server by setting its status back to `active`. **Note**: Server metadata is never permanently removed from the registry. The `deleted` status hides the server from discovery but preserves the historical record.


[​](#how-do-i-update-my-server-metadata)

How do I update my server metadata?

Submit a new `server.json` with a unique version string. Once published, version metadata is immutable (similar to npm).


[​](#can-i-add-custom-metadata-when-publishing)

Can I add custom metadata when publishing?

Yes, custom metadata under `_meta.io.modelcontextprotocol.registry/publisher-provided` is preserved when publishing to the registry. This allows you to include custom metadata specific to your publishing process.

There is a 4KB size limit (4096 bytes of JSON). Publishing will fail if this limit is exceeded.


[​](#reporting-issues)

Reporting Issues


[​](#what-if-i-need-to-report-a-spam-or-malicious-server)

What if I need to report a spam or malicious server?

1.  Report it as abuse to the underlying package registry (e.g. NPM, PyPI, DockerHub, etc.); and
2.  Raise a GitHub issue on the registry repo with a title beginning `Abuse report: `


[​](#what-if-i-need-to-report-a-security-vulnerability-in-the-registry-itself)

What if I need to report a security vulnerability in the registry itself?

Follow [the MCP community SECURITY.md](https://github.com/modelcontextprotocol/.github/blob/main/SECURITY.md).
