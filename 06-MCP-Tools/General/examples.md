---
title: "Example Servers - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/examples"
category: "06-MCP-Tools/General"
fetched_at: "2026-10-31T06:24:34Z"
last_modified: "Fri, 30 Oct 2026 21:02:58 GMT"
tags: ["mcp"]
---

## On this page

Back to top

- [Reference implementations](#reference-implementations)
  - [Current reference servers](#current-reference-servers)
  - [Additional example servers (archived)](#additional-example-servers-archived)
- [More servers](#more-servers)
- [Getting started](#getting-started)
  - [Using reference servers](#using-reference-servers)
  - [Configuring with Claude](#configuring-with-claude)
- [Additional resources](#additional-resources)

Examples

# Example Servers

Copy pageCopy page

A list of example servers and implementations

Copy pageCopy page

This page showcases various Model Context Protocol (MCP) servers that demonstrate the protocol’s capabilities and versatility. These servers enable Large Language Models (LLMs) to securely access tools and data sources.


[​](#reference-implementations)

Reference implementations

These official reference servers demonstrate core MCP features and SDK usage:


[​](#current-reference-servers)

Current reference servers

- **[Everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything)** - Reference / test server with prompts, resources, and tools
- **[Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)** - Web content fetching and conversion for efficient LLM usage
- **[Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)** - Secure file operations with configurable access controls
- **[Git](https://github.com/modelcontextprotocol/servers/tree/main/src/git)** - Tools to read, search, and manipulate Git repositories
- **[Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)** - Knowledge graph-based persistent memory system
- **[Sequential Thinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)** - Dynamic and reflective problem-solving through thought sequences
- **[Time](https://github.com/modelcontextprotocol/servers/tree/main/src/time)** - Time and timezone conversion capabilities


[​](#additional-example-servers-archived)

Additional example servers (archived)

Visit the [servers-archived repository](https://github.com/modelcontextprotocol/servers-archived) to get access to archived example servers that are no longer actively maintained. They are provided for historical reference only.


[​](#more-servers)

More servers

Visit the MCP Registry at [registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io/) for servers published by companies and community members.


[​](#getting-started)

Getting started


[​](#using-reference-servers)

Using reference servers

TypeScript-based servers can be used directly with `npx`:

```python
npx -y @modelcontextprotocol/server-memory
```

Python-based servers can be used with `uvx` (recommended) or `pip`:

```python
# Using uvx
uvx mcp-server-git

# Using pip
pip install mcp-server-git
python -m mcp_server_git
```


[​](#configuring-with-claude)

Configuring with Claude

To use an MCP server with Claude, add it to your configuration:

```python
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
    }
  }
}
```


[​](#additional-resources)

Additional resources

Visit our [GitHub Discussions](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions) to engage with the MCP community.
