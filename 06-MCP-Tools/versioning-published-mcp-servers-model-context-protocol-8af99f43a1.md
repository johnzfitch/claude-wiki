---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:22Z"
source_url: "https://modelcontextprotocol.io/registry/versioning"
title: "Versioning Published MCP Servers - Model Context Protocol"
---

[Skip to main content](#content-area)

[Model Context Protocol home page](/)

Search...

⌘K

- [Blog](https://blog.modelcontextprotocol.io)
- [GitHub](https://github.com/modelcontextprotocol)

Search...

Navigation

Publishing

Versioning Published MCP Servers

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

- [Version Format](#version-format)
- [Best Practices](#best-practices)
- [Use Semantic Versioning](#use-semantic-versioning)
- [Align Server Version with Package Version](#align-server-version-with-package-version)
- [Align Server Version with Remote API Version](#align-server-version-with-remote-api-version)
- [Use Prerelease Versions for Registry-only Updates](#use-prerelease-versions-for-registry-only-updates)
- [Aggregator Recommendations](#aggregator-recommendations)

Publishing

# Versioning Published MCP Servers

Copy page

Copy page

The MCP Registry is currently in preview. Breaking changes or data resets may occur before general availability. If you encounter any issues, please report them on [GitHub](https://github.com/modelcontextprotocol/registry/issues).

MCP servers **MUST** define a version string in `server.json`. For example:

server.json

Copy

``` shiki
{
  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json",
  "name": "io.github.username/email-integration-mcp",
  "title": "Email Integration",
  "description": "Send emails and manage email accounts",
  "version": "1.0.0",
  "packages": [
    {
      "registryType": "npm",
      "identifier": "@username/email-integration-mcp",
      "version": "1.0.0",
      "transport": {
        "type": "stdio"
      }
    }
  ]
}
```

The version string **MUST** be unique for each publication of the server. Once published, the version string (and other metadata) cannot be changed.

## 

[​](#version-format)

Version Format

The MCP Registry recommends [semantic versioning](https://semver.org/), but supports any version string format. When a server is published, the MCP Registry will attempt to parse its version as a semantic version string for sorting purposes, and will mark the version as “latest” if appropriate. If parsing fails, the version will always be marked as “latest”.

If a server uses semantic version strings but publishes a new version that does *not* conform to semantic versioning, the new version will be marked as “latest” even if it would otherwise be sorted before the semantic version strings.

As an error prevention mechanism, the MCP Registry prohibits version strings that appear to refer to ranges of versions.

| Example        | Type                | Guidance                       |
|----------------|---------------------|--------------------------------|
| `1.0.0`        | semantic version    | **Recommended**                |
| `2.1.3-alpha`  | semantic prerelease | **Recommended**                |
| `1.0.0-beta.1` | semantic prerelease | **Recommended**                |
| `3.0.0-rc.2`   | semantic prerelease | **Recommended**                |
| `2025.11.25`   | semantic date       | Recommended                    |
| `2025.6.18`    | semantic date       | Recommended **(⚠️Caution!⚠️)** |
| `2025.06.18`   | non-semantic date   | Allowed **(⚠️Caution!⚠️)**     |
| `2025-06-18`   | non-semantic date   | Allowed                        |
| `v1.0`         | prefixed version    | Allowed                        |
| `^1.2.3`       | version range       | Prohibited                     |
| `~1.2.3`       | version range       | Prohibited                     |
| `>=1.2.3`      | version range       | Prohibited                     |
| `<=1.2.3`      | version range       | Prohibited                     |
| `>1.2.3`       | version range       | Prohibited                     |
| `<1.2.3`       | version range       | Prohibited                     |
| `1.x`          | version range       | Prohibited                     |
| `1.2.*`        | version range       | Prohibited                     |
| `1 - 2`        | version range       | Prohibited                     |
| `1.2 || 1.3`   | version range       | Prohibited                     |

## 

[​](#best-practices)

Best Practices

### 

[​](#use-semantic-versioning)

Use Semantic Versioning

Use [semantic versioning](https://semver.org/) for version strings.

### 

[​](#align-server-version-with-package-version)

Align Server Version with Package Version

For local servers, align the server version with the underlying package version in order to prevent confusion:

server.json

Copy

``` shiki
{
  "version": "1.2.3",
  "packages": [
    {
      "registryType": "npm",
      "identifier": "@my-username/my-server",
      "version": "1.2.3",
      "transport": {
        "type": "stdio"
      }
    }
  ]
}
```

If there are multiple underlying packages, use the server version to indicate the overall release version:

server.json

Copy

``` shiki
{
  "version": "1.3.0",
  "packages": [
    {
      "registryType": "npm",
      "identifier": "@my-username/my-server",
      "version": "1.3.0",
      "transport": {
        "type": "stdio"
      }
    },
    {
      "registryType": "nuget",
      "identifier": "MyUsername.MyServer",
      "version": "1.0.0",
      "transport": {
        "type": "stdio"
      }
    }
  ]
}
```

### 

[​](#align-server-version-with-remote-api-version)

Align Server Version with Remote API Version

For remote servers with an API version, the server version should align with the API version:

server.json

Copy

``` shiki
{
  "version": "2.1.0",
  "remotes": [
    {
      "type": "streamable-http",
      "url": "https://api.myservice.com/mcp/v2.1"
    }
  ]
}
```

### 

[​](#use-prerelease-versions-for-registry-only-updates)

Use Prerelease Versions for Registry-only Updates

If you anticipate publishing a server multiple times *without* changing the underlying package or remote URL — for example, to update other parts of the metadata — use semantic prerelease versions:

server.json

Copy

``` shiki
{
  "version": "1.2.3-1",
  "packages": [
    {
      "registryType": "npm",
      "identifier": "@my-username/my-server",
      "version": "1.2.3",
      "transport": {
        "type": "stdio"
      }
    }
  ]
}
```

According to semantic versioning, prerelease versions such as `1.2.3-1` are sorted before regular semantic versions such as `1.2.3`. Therefore, if you publish a prerelease version *after* its corresponding regular version, the prerelease version will **not** be marked as “latest”.

## 

[​](#aggregator-recommendations)

Aggregator Recommendations

MCP Registry aggregators **SHOULD**:

1.  Attempt to interpret versions as semantic versions when possible
2.  Use the following version comparison rules:
    - If one version is marked as “latest”, treat it as later
    - If both versions are valid semantic versions, use semantic versioning comparison rules
    - If neither versions are valid semantic versions, compare published timestamp
    - If one version is a valid semantic version and the other is not, treat the semantic version as later

Was this page helpful?

Yes

No

[Authentication](/registry/authentication)[GitHub Actions](/registry/github-actions)

[github](https://github.com/modelcontextprotocol)
