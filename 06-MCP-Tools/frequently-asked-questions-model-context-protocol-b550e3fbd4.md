---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:21Z"
source_url: "https://modelcontextprotocol.io/registry/faq"
title: "Frequently Asked Questions - Model Context Protocol"
---

[Skip to main content](#content-area)

[Model Context Protocol home page](/)

Search...

⌘K

- [Blog](https://blog.modelcontextprotocol.io)
- [GitHub](https://github.com/modelcontextprotocol)

Search...

Navigation

Frequently Asked Questions

[Documentation](/docs/getting-started/intro)

[Extensions](/extensions/overview)

[Specification](/specification/2025-11-25)

[Registry](/registry/about)

[Community](/community/contributing)

- [](/registry/about)
  About

&nbsp;

- [](/registry/quickstart)
  Quickstart: Publish a Server

&nbsp;

- [](/registry/faq)
  FAQ

##### Publishing

- [](/registry/package-types)
  Package Types
- [](/registry/remote-servers)
  Remote Servers
- [](/registry/authentication)
  Authentication
- [](/registry/versioning)
  Versioning
- [](/registry/github-actions)
  GitHub Actions
- [](/registry/moderation-policy)
  Moderation Policy

##### Consuming

- [](/registry/registry-aggregators)
  Registry Aggregators

- [](/registry/terms-of-service)
  Terms of Service

On this page

- [General](#general)
- [What is the difference between “Official MCP Registry”, “MCP Registry”, “MCP registry”, “MCP Registry API”, etc?](#what-is-the-difference-between-%E2%80%9Cofficial-mcp-registry%E2%80%9D-%E2%80%9Cmcp-registry%E2%80%9D-%E2%80%9Cmcp-registry%E2%80%9D-%E2%80%9Cmcp-registry-api%E2%80%9D-etc)
- [Can I delete/unpublish my server?](#can-i-delete%2Funpublish-my-server)
- [How do I update my server metadata?](#how-do-i-update-my-server-metadata)
- [Can I add custom metadata when publishing?](#can-i-add-custom-metadata-when-publishing)
- [Reporting Issues](#reporting-issues)
- [What if I need to report a spam or malicious server?](#what-if-i-need-to-report-a-spam-or-malicious-server)
- [What if I need to report a security vulnerability in the registry itself?](#what-if-i-need-to-report-a-security-vulnerability-in-the-registry-itself)

# Frequently Asked Questions

Copy page

Copy page

The MCP Registry is currently in preview. Breaking changes or data resets may occur before general availability. If you encounter any issues, please report them on [GitHub](https://github.com/modelcontextprotocol/registry/issues).

## 

[​](#general)

General

### 

[​](#what-is-the-difference-between-“official-mcp-registry”-“mcp-registry”-“mcp-registry”-“mcp-registry-api”-etc)

What is the difference between “Official MCP Registry”, “MCP Registry”, “MCP registry”, “MCP Registry API”, etc?

- “MCP Registry API” — An API that implements the [OpenAPI spec](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/api/openapi.yaml) defined by the MCP Registry.
- “Official MCP Registry API” — The REST API served at `https://registry.modelcontextprotocol.io`, which is a superset of the MCP Registry API. Its OpenAPI spec can be downloaded from [https://registry.modelcontextprotocol.io/openapi.yaml](https://registry.modelcontextprotocol.io/openapi.yaml).
- “MCP registry” — A third-party service that provides an MCP Registry API.
- “Official MCP Registry” (or “The MCP Registry”) — The service that lives at `https://registry.modelcontextprotocol.io`.

### 

[​](#can-i-delete/unpublish-my-server)

Can I delete/unpublish my server?

Currently, no. At the time of writing, there is [open discussion](https://github.com/modelcontextprotocol/registry/issues/104).

### 

[​](#how-do-i-update-my-server-metadata)

How do I update my server metadata?

Submit a new `server.json` with a unique version string. Once published, version metadata is immutable (similar to npm).

### 

[​](#can-i-add-custom-metadata-when-publishing)

Can I add custom metadata when publishing?

Yes, custom metadata under `_meta.io.modelcontextprotocol.registry/publisher-provided` is preserved when publishing to the registry. This allows you to include custom metadata specific to your publishing process.

There is a 4KB size limit (4096 bytes of JSON). Publishing will fail if this limit is exceeded.

## 

[​](#reporting-issues)

Reporting Issues

### 

[​](#what-if-i-need-to-report-a-spam-or-malicious-server)

What if I need to report a spam or malicious server?

1.  Report it as abuse to the underlying package registry (e.g. NPM, PyPi, DockerHub, etc.); and
2.  Raise a GitHub issue on the registry repo with a title beginning `Abuse report: `

### 

[​](#what-if-i-need-to-report-a-security-vulnerability-in-the-registry-itself)

What if I need to report a security vulnerability in the registry itself?

Follow [the MCP community SECURITY.md](https://github.com/modelcontextprotocol/.github/blob/main/SECURITY.md).

Was this page helpful?

Yes

No

[Quickstart: Publish a Server](/registry/quickstart)[Package Types](/registry/package-types)

[github](https://github.com/modelcontextprotocol)
