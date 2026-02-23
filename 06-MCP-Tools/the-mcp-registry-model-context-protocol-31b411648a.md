---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:21Z"
source_url: "https://modelcontextprotocol.io/registry/about"
title: "The MCP Registry - Model Context Protocol"
---

[Skip to main content](#content-area)

[Model Context Protocol home page](/)

Search...

⌘K

- [Blog](https://blog.modelcontextprotocol.io)
- [GitHub](https://github.com/modelcontextprotocol)

Search...

Navigation

The MCP Registry

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

- [The MCP Registry Ecosystem](#the-mcp-registry-ecosystem)
- [Relationship with Package Registries](#relationship-with-package-registries)
- [Relationship with Server Developers](#relationship-with-server-developers)
- [Relationship with Downstream Aggregators](#relationship-with-downstream-aggregators)
- [Relationship with Other MCP Registries](#relationship-with-other-mcp-registries)
- [Relationship with MCP Host Applications](#relationship-with-mcp-host-applications)
- [Trust and Security](#trust-and-security)
- [Verifying Server Authenticity](#verifying-server-authenticity)
- [Security Scanning](#security-scanning)
- [Spam Prevention](#spam-prevention)

# The MCP Registry

Copy page

Copy page

The MCP Registry is currently in preview. Breaking changes or data resets may occur before general availability. If you encounter any issues, please report them on [GitHub](https://github.com/modelcontextprotocol/registry/issues).

The MCP Registry is the official centralized metadata repository for publicly accessible MCP servers, backed by major trusted contributors to the MCP ecosystem such as Anthropic, GitHub, PulseMCP, and Microsoft. The MCP Registry provides:

- A single place for server creators to publish metadata about their servers
- Namespace management through DNS verification
- A REST API for MCP clients and aggregators to discover available servers
- Standardized installation and configuration information

Server metadata is stored in a standardized [`server.json` format](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/server-json/server.schema.json), which contains:

- The server’s unique name (e.g., `io.github.user/server-name`)
- Where to locate the server (e.g., npm package name, remote server URL)
- Execution instructions (e.g., command-line args, env vars)
- Other discovery data (e.g., description, server capabilities)

## 

[​](#the-mcp-registry-ecosystem)

The MCP Registry Ecosystem

The MCP Registry is part of an ecosystem that looks something like:

### 

[​](#relationship-with-package-registries)

Relationship with Package Registries

Package registries — such as npm, PyPI, and Docker Hub — host packages with code and binaries. The MCP Registry hosts metadata that points to those packages. For example, a `weather-mcp` package could be hosted on npm, and metadata in the MCP Registry could map the “weather v1.2.0” server to `npm:weather-mcp`. The [Package Types guide](./package-types.mdx) lists the supported package types and registries. More package registries may be supported in the future based on community demand. If you are interested in building support for a package registry, please [open an issue](https://github.com/modelcontextprotocol/registry).

### 

[​](#relationship-with-server-developers)

Relationship with Server Developers

The MCP Registry supports both open-source and closed-source servers. Server developers can publish their server’s metadata to the registry as long as the server’s installation method is publicly available (e.g., an npm package or a Docker image on a public registry) *or* the server itself is publicly accessible (e.g., a remote server that is not restricted to private networks). The MCP Registry **does not** support private servers. Private servers are those that are only accessible to a narrow set of users. For example, servers published on a private network (like `mcp.acme-corp.internal`) or on private package registries (e.g. `npx -y @acme/mcp --registry https://artifactory.acme-corp.internal/npm`). If you want to publish private servers, we recommend that you host your own private MCP registry and add them there.

### 

[​](#relationship-with-downstream-aggregators)

Relationship with Downstream Aggregators

The MCP Registry is intended to be consumed primarily by downstream aggregators, such as MCP server marketplaces. The metadata hosted by the MCP Registry is deliberately unopinionated. Downstream aggregators can provide curation or additional metadata such as community ratings. We expect that downstream aggregators will use the MCP Registry API to pull new metadata on a regular but infrequent basis (for example, once per hour). See the [MCP Registry Aggregators guide](./registry-aggregators.mdx) for more information.

### 

[​](#relationship-with-other-mcp-registries)

Relationship with Other MCP Registries

In addition to a public REST API, the MCP Registry defines an [OpenAPI spec](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/api/openapi.yaml) that other MCP registries can implement in order to provide a standardized interface for MCP host applications. We expect that many downstream aggregators will implement this interface. Private MCP registries can implement it as well to benefit from existing host application support. Note that the official MCP Registry codebase is **not** designed for self-hosting, and the registry maintainers cannot provide support for this use case. If you choose to fork it, you would need to maintain and operate it independently.

### 

[​](#relationship-with-mcp-host-applications)

Relationship with MCP Host Applications

The MCP Registry is not intended to be directly consumed by host applications. Instead, host applications should consume other MCP registries, such as downstream marketplaces, via a REST API conforming to the official MCP Registry’s OpenAPI spec.

## 

[​](#trust-and-security)

Trust and Security

### 

[​](#verifying-server-authenticity)

Verifying Server Authenticity

The MCP Registry uses namespace authentication to ensure that servers come from their claimed sources. Server names follow a reverse DNS format (like `io.github.username/server` or `com.example/server`) that ties them to verified GitHub accounts or domains. This namespace system ensures that only the legitimate owner of a GitHub account or domain can publish servers under that namespace, providing trust and accountability in the ecosystem. For details on authentication methods, see the [Authentication guide](./authentication.mdx).

### 

[​](#security-scanning)

Security Scanning

The MCP Registry delegates security scanning to:

- **Underlying package registries** — npm, PyPI, Docker Hub, and other package registries perform their own security scanning and vulnerability detection.
- **Downstream aggregators** — MCP Registry aggregators and marketplaces can implement additional security checks, ratings, or curation.

The MCP Registry focuses on namespace authentication and metadata hosting, while relying on the broader ecosystem for security scanning of actual server code.

### 

[​](#spam-prevention)

Spam Prevention

The MCP Registry uses multiple mechanisms to prevent spam:

- **Namespace authentication requirements** — Publishers must verify ownership of their namespace through GitHub, DNS, or HTTP challenges, preventing arbitrary spam submissions.
- **Character limits and validation** — Free-form fields have strict character limits and regex validation to prevent abuse.
- **Manual takedown** — The registry maintainers can manually remove spam or malicious servers. See the [Moderation Policy](./moderation-policy.mdx) for details on what content is removed.

Future spam prevention measures under consideration include stricter rate limiting, AI-based spam detection, and community reporting capabilities.

Was this page helpful?

Yes

No

[Quickstart: Publish a Server](/registry/quickstart)

[github](https://github.com/modelcontextprotocol)
