---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:19Z"
source_url: "https://modelcontextprotocol.io/docs/tools/inspector"
title: "MCP Inspector - Model Context Protocol"
---

[Skip to main content](#content-area)

[Model Context Protocol home page](/)

Search...

⌘K

- [Blog](https://blog.modelcontextprotocol.io)
- [GitHub](https://github.com/modelcontextprotocol)

Search...

Navigation

Developer tools

MCP Inspector

[Documentation](/docs/getting-started/intro)

[Extensions](/extensions/overview)

[Specification](/specification/2025-11-25)

[Registry](/registry/about)

[Community](/community/contributing)

##### Get started

- [](/docs/getting-started/intro)
  What is MCP?

##### About MCP

- [](/docs/learn/architecture)
  Architecture
- [](/docs/learn/server-concepts)
  Servers
- [](/docs/learn/client-concepts)
  Clients
- [](/specification/versioning)
  Versioning

##### Develop with MCP

- [](/docs/develop/connect-local-servers)
  Connect to local MCP servers

- [](/docs/develop/connect-remote-servers)
  Connect to remote MCP Servers

- [](/docs/develop/build-server)
  Build an MCP server

- [](/docs/develop/build-client)
  Build an MCP client

- [](/docs/sdk)
  SDKs

- Security

##### Developer tools

- [](/docs/tools/inspector)
  MCP Inspector

On this page

- [Getting started](#getting-started)
- [Installation and basic usage](#installation-and-basic-usage)
- [Inspecting servers from npm or PyPI](#inspecting-servers-from-npm-or-pypi)
- [Inspecting locally developed servers](#inspecting-locally-developed-servers)
- [Feature overview](#feature-overview)
- [Server connection pane](#server-connection-pane)
- [Resources tab](#resources-tab)
- [Prompts tab](#prompts-tab)
- [Tools tab](#tools-tab)
- [Notifications pane](#notifications-pane)
- [Best practices](#best-practices)
- [Development workflow](#development-workflow)
- [Next steps](#next-steps)

Developer tools

# MCP Inspector

Copy page

In-depth guide to using the MCP Inspector for testing and debugging Model Context Protocol servers

Copy page

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is an interactive developer tool for testing and debugging MCP servers. While the [Debugging Guide](/legacy/tools/debugging) covers the Inspector as part of the overall debugging toolkit, this document provides a detailed exploration of the Inspector’s features and capabilities.

## 

[​](#getting-started)

Getting started

### 

[​](#installation-and-basic-usage)

Installation and basic usage

The Inspector runs directly through `npx` without requiring installation:

Copy

``` shiki
npx @modelcontextprotocol/inspector <command>
```

Copy

``` shiki
npx @modelcontextprotocol/inspector <command> <arg1> <arg2>
```

#### 

[​](#inspecting-servers-from-npm-or-pypi)

Inspecting servers from npm or PyPI

A common way to start server packages from [npm](https://npmjs.com) or [PyPI](https://pypi.org).

- npm package

- PyPI package

Copy

``` shiki
npx -y @modelcontextprotocol/inspector npx <package-name> <args>
# For example
npx -y @modelcontextprotocol/inspector npx @modelcontextprotocol/server-filesystem /Users/username/Desktop
```

Copy

``` shiki
npx @modelcontextprotocol/inspector uvx <package-name> <args>
# For example
npx @modelcontextprotocol/inspector uvx mcp-server-git --repository ~/code/mcp/servers.git
```

#### 

[​](#inspecting-locally-developed-servers)

Inspecting locally developed servers

To inspect servers locally developed or downloaded as a repository, the most common way is:

- TypeScript

- Python

Copy

``` shiki
npx @modelcontextprotocol/inspector node path/to/server/index.js args...
```

Copy

``` shiki
npx @modelcontextprotocol/inspector \
  uv \
  --directory path/to/server \
  run \
  package-name \
  args...
```

Please carefully read any attached README for the most accurate instructions.

## 

[​](#feature-overview)

Feature overview

The Inspector provides several features for interacting with your MCP server:

### 

[​](#server-connection-pane)

Server connection pane

- Allows selecting the [transport](/legacy/concepts/transports) for connecting to the server
- For local servers, supports customizing the command-line arguments and environment

### 

[​](#resources-tab)

Resources tab

- Lists all available resources
- Shows resource metadata (MIME types, descriptions)
- Allows resource content inspection
- Supports subscription testing

### 

[​](#prompts-tab)

Prompts tab

- Displays available prompt templates
- Shows prompt arguments and descriptions
- Enables prompt testing with custom arguments
- Previews generated messages

### 

[​](#tools-tab)

Tools tab

- Lists available tools
- Shows tool schemas and descriptions
- Enables tool testing with custom inputs
- Displays tool execution results

### 

[​](#notifications-pane)

Notifications pane

- Presents all logs recorded from the server
- Shows notifications received from the server

## 

[​](#best-practices)

Best practices

### 

[​](#development-workflow)

Development workflow

1.  Start Development
    - Launch Inspector with your server
    - Verify basic connectivity
    - Check capability negotiation
2.  Iterative testing
    - Make server changes
    - Rebuild the server
    - Reconnect the Inspector
    - Test affected features
    - Monitor messages
3.  Test edge cases
    - Invalid inputs
    - Missing prompt arguments
    - Concurrent operations
    - Verify error handling and error responses

## 

[​](#next-steps)

Next steps

[](https://github.com/modelcontextprotocol/inspector)

## Inspector Repository

Check out the MCP Inspector source code

[](/legacy/tools/debugging)

## Debugging Guide

Learn about broader debugging strategies

Was this page helpful?

Yes

No

[Security Best Practices](/docs/tutorials/security/security_best_practices)

[github](https://github.com/modelcontextprotocol)
