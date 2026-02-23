---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:20Z"
source_url: "https://modelcontextprotocol.io/examples"
title: "Example Servers - Model Context Protocol"
---

[Skip to main content](#content-area)

[Model Context Protocol home page](/)

Search...

⌘K

- [Blog](https://blog.modelcontextprotocol.io)
- [GitHub](https://github.com/modelcontextprotocol)

Search...

Navigation

Examples

Example Servers

[Documentation](/docs/getting-started/intro)

[Extensions](/extensions/overview)

[Specification](/specification/2025-11-25)

[Registry](/registry/about)

[Community](/community/contributing)

- [](/community/contributing)
  Contributing to MCP

&nbsp;

- [](/community/communication)
  Contributor Communication

##### Governance

- [](/community/governance)
  Governance and Stewardship
- [](/community/sep-guidelines)
  SEP Guidelines
- [](/community/sdk-tiers)
  SDK Tiering System
- [](/community/working-interest-groups)
  Working and Interest Groups
- [](/community/antitrust)
  Antitrust Policy

##### SEPs

- [](/community/seps)
  SEP Index

- Final

- Draft

##### Roadmap

- [](/development/roadmap)
  Roadmap

##### Examples

- [](/clients)
  Example Clients
- [](/examples)
  Example Servers

On this page

- [Reference implementations](#reference-implementations)
- [Current reference servers](#current-reference-servers)
- [Additional example servers (archived)](#additional-example-servers-archived)
- [Official integrations](#official-integrations)
- [Community implementations](#community-implementations)
- [Getting started](#getting-started)
- [Using reference servers](#using-reference-servers)
- [Configuring with Claude](#configuring-with-claude)
- [Additional resources](#additional-resources)

Examples

# Example Servers

Copy page

A list of example servers and implementations

Copy page

This page showcases various Model Context Protocol (MCP) servers that demonstrate the protocol’s capabilities and versatility. These servers enable Large Language Models (LLMs) to securely access tools and data sources.

## 

[​](#reference-implementations)

Reference implementations

These official reference servers demonstrate core MCP features and SDK usage:

### 

[​](#current-reference-servers)

Current reference servers

- **[Everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything)** - Reference / test server with prompts, resources, and tools
- **[Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)** - Web content fetching and conversion for efficient LLM usage
- **[Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)** - Secure file operations with configurable access controls
- **[Git](https://github.com/modelcontextprotocol/servers/tree/main/src/git)** - Tools to read, search, and manipulate Git repositories
- **[Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)** - Knowledge graph-based persistent memory system
- **[Sequential Thinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)** - Dynamic and reflective problem-solving through thought sequences
- **[Time](https://github.com/modelcontextprotocol/servers/tree/main/src/time)** - Time and timezone conversion capabilities

### 

[​](#additional-example-servers-archived)

Additional example servers (archived)

Visit the [servers-archived repository](https://github.com/modelcontextprotocol/servers-archived) to get access to archived example servers that are no longer actively maintained. They are provided for historical reference only.

## 

[​](#official-integrations)

Official integrations

Visit the [MCP Servers Repository (Official Integrations section)](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#%EF%B8%8F-official-integrations) for a list of MCP servers maintained by companies for their platforms.

## 

[​](#community-implementations)

Community implementations

Visit the [MCP Servers Repository (Community section)](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) for a list of MCP servers maintained by community members.

## 

[​](#getting-started)

Getting started

### 

[​](#using-reference-servers)

Using reference servers

TypeScript-based servers can be used directly with `npx`:

Copy

``` shiki
npx -y @modelcontextprotocol/server-memory
```

Python-based servers can be used with `uvx` (recommended) or `pip`:

Copy

``` shiki
# Using uvx
uvx mcp-server-git

# Using pip
pip install mcp-server-git
python -m mcp_server_git
```

### 

[​](#configuring-with-claude)

Configuring with Claude

To use an MCP server with Claude, add it to your configuration:

Copy

``` shiki
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/allowed/files"
      ]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_TOKEN>"
      }
    }
  }
}
```

## 

[​](#additional-resources)

Additional resources

Visit the [MCP Servers Repository (Resources section)](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-resources) for a collection of other resources and projects related to MCP. Visit our [GitHub Discussions](https://github.com/orgs/modelcontextprotocol/discussions) to engage with the MCP community.

Was this page helpful?

Yes

No

[Example Clients](/clients)

[github](https://github.com/modelcontextprotocol)
