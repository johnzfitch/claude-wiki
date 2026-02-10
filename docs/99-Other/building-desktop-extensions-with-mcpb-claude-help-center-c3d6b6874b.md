---
category: "99-Other"
fetched_at: "2026-02-10T10:49:32Z"
source_url: "https://support.claude.com/en/articles/12922929-building-desktop-extensions-with-mcpb"
title: "Building Desktop Extensions with MCPB | Claude Help Center"
---

[](/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

Search for articles...

Table of contents

[](#h_030b7e2877)

[](#h_3f7b9ab5aa)

[](#h_5b6838d5b5)

[](#h_e0ce54bca6)

[](#h_9aad621eea)

[](#h_8c4563a72f)

[All Collections](/en/)

[Connectors](https://support.claude.com/en/collections/15399129-connectors)

Building Desktop Extensions with MCPB

# Building Desktop Extensions with MCPB

Updated this week

Table of contents

[](#h_030b7e2877)

[](#h_3f7b9ab5aa)

[](#h_5b6838d5b5)

[](#h_e0ce54bca6)

[](#h_9aad621eea)

[](#h_8c4563a72f)

This guide will help you build an MCP Bundle (.mcpb) to create a desktop extension for internal use, private distribution, or as a foundation for submission to [Anthropic’s Connectors Directory](https://claude.ai/directory).

------------------------------------------------------------------------

## 1. Introduction

### What is an MCPB?

MCPB (.mcpb) files are zip archives containing a local MCP server and manifest.json. They enable single-click installation in Claude Desktop, similar to browser extensions.

**Key characteristics:**

- Runs locally on user's machine

- Communicates via stdio transport

- Bundles all dependencies

- Works offline

- No OAuth required

**Learn more:**

- [MCPB Repository](https://github.com/modelcontextprotocol/mcpb) - Complete specification and architecture

- [Desktop Extensions Blog Post](https://www.anthropic.com/engineering/desktop-extensions) - Overview and use cases

------------------------------------------------------------------------

### When should I use a local server (MCPB) vs a remote server?

Choose a local server (MCPB) for:

**Internal Systems and Security**

- Access systems behind your firewall (JIRA, Confluence, internal wikis, private databases)

- Seamless authentication - Uses existing SSO and browser sessions automatically, no token management

- Zero-trust compliance - Operates within your corporate network boundaries without exposing internal resources publicly

**Local Resources**

- Direct filesystem access for code editing and Git operations

- Integration with locally installed tools (Docker, IDEs, databases)

- Hardware integration and desktop application control

- Privacy-sensitive operations that shouldn't leave the user's machine

**Enterprise Deployment**

- One-click installation with built-in Node.js runtime (no dependencies to manage)

- No cloud infrastructure, VPN configurations, or firewall rules required

- Organization-level controls - Admins can upload custom extensions and manage access via allowlists

- Complete control over authentication, authorization, and audit logs\
  ​

Choose a remote connector for:

- Cloud services and public APIs requiring centralized infrastructure

- Distribution across claude on web, mobile and desktop

- Services needing centralized updates across all users

- OAuth flows requiring server-side token management

- Public-facing integrations used by multiple organizations

**Key difference:** MCPBs run on the user's machine via stdio transport with access to local and internal resources. Remote connectors run on your servers via HTTPS and are accessed through Anthropic's infrastructure.

**Real-world use:** Organizations are building MCPBs as secure proxies to internal MCP servers, for internal documentation access, and to connect development tools while maintaining their security architecture.

**For remote connector guidance:** See [MCP Partner FAQ](https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq) for complete remote connector documentation.

------------------------------------------------------------------------

## 2. Getting Started

### Which programming language should I use?

**Node.js is strongly recommended** because:

- Ships with Claude for macOS and Windows (zero installation friction for users)

- Users don't need separate runtime installation

- Best compatibility and reliability with Claude Desktop

- Extensive MCP SDK support

------------------------------------------------------------------------

### What platforms should I support?

Claude Desktop runs on:

- **macOS** (darwin)

- **Windows** (win32)

Specify supported platforms in your manifest.json compatibility section.

**Best practice:** Test on both platforms even if you primarily develop on one.

**Platform compatibility details:** See [MCPB Manifest Spec - Compatibility](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md#compatibility) for platform specification and runtime requirements.

------------------------------------------------------------------------

### How do I create my first MCPB?

Follow this five-step process:

1\. Install MCPB CLI: `npm install -g @anthropic-ai/mcpb`

2\. Create your MCP server (see MCP SDK)

3\. Run mcpb init to create manifest.json

4\. Run mcpb pack to bundle

5\. Install and test in Claude Desktop

**For detailed implementation guidance:**

- [MCPB Repository](https://github.com/modelcontextprotocol/mcpb) - Complete getting started guide, CLI usage, and specifications

- [MCPB Examples](https://github.com/modelcontextprotocol/mcpb/tree/main/examples) - Working reference implementations including "Hello World"

- [MCP SDK](https://www.npmjs.com/package/@modelcontextprotocol/sdk) - Core protocol implementation

**For comprehensive guidance on development, testing, and best practices,** see the [MCPB README's "For Bundle Developers" section](https://github.com/modelcontextprotocol/mcpb/blob/main/README.md).

**Important:** Before distributing your MCPB, review the testing and best practices guidance in the MCPB README to ensure quality.

------------------------------------------------------------------------

## 3. Configuration

### What is manifest.json?

The manifest.json file is required metadata that describes your MCPB - what it does, how to run it, which tools it provides, and what configuration it needs.

For the most up to date information, refer to the official MCPB Specification.

- [MCPB Manifest Spec](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md) - Full schema with all fields

- [Example Manifests](https://github.com/modelcontextprotocol/mcpb/tree/main/examples) - Real-world implementations

- [CLI Documentation](https://github.com/modelcontextprotocol/mcpb/blob/main/CLI.md) - Command reference

------------------------------------------------------------------------

### How do I add an icon?

Icons are optional but recommended for professional appearance.

**Basic approach:** Include icon.png file in your bundle root directory and reference it in manifest.json.

**Requirements:**

- **File name:** icon.png (or custom path)

- **Size:** 512×512px recommended (minimum 256×256px)

- **Format:** PNG with transparency support

- **Location:** Bundle root or specified path

**Advanced options:** Multiple icon variants for different sizes and themes (light/dark mode support).

**Implementation details:** See [MCPB Manifest Spec - Icons](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md#icons) for:

- Icon field configuration

- Multiple icon variants syntax

- Size and theme specifications

- Best practices and requirements

------------------------------------------------------------------------

### How do users configure my MCPB?

Define user_config section in manifest.json. Claude Desktop automatically creates a settings UI where users can configure your extension.

See [MCPB Manifest Spec - User Configuration](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md#user-configuration) for the complete implementation:

- Full schema and examples

- All configuration types and properties

- Validation constraints

- Sensitive data handling

- Multi-select patterns

------------------------------------------------------------------------

### How do users install my MCPB?

There are three different installation methods:

1.  **Double-click** - Download .mcpb file and double-click to open

2.  **Drag-and-drop** - Drag .mcpb file into Claude Desktop window

3.  **File menu** - Developer → Extensions → Install Extension → select .mcpb file

**All methods open installation UI** where users can:

- Review extension details and permissions

- Configure required settings

- Grant necessary permissions

- Complete installation

**Installation scope:** Per-user installation - each user must install separately on their own system.

**User experience and admin controls:** For detailed information about the end-user installation experience and enterprise admin controls (including Team/Enterprise organization management and policy configuration), see:

- [Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop) - Complete user guide covering directory browsing, installation UI, troubleshooting, and admin controls.

------------------------------------------------------------------------

## 4. Resources

### Official Documentation

**MCPB Framework:**

- [MCPB Repository](https://github.com/modelcontextprotocol/mcpb) - Complete specification and tools

- [MCPB Manifest Spec](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md) - Full manifest schema

- [MCPB CLI Documentation](https://github.com/modelcontextprotocol/mcpb/blob/main/CLI.md) - Command-line tool reference

- [MCPB Examples](https://github.com/modelcontextprotocol/mcpb/tree/main/examples) - Reference implementations

**MCP Protocol:**

- [MCP Specification](https://modelcontextprotocol.io/docs/getting-started/intro) - Protocol documentation

- [MCP Quickstart](https://modelcontextprotocol.io/docs/develop/build-server) - Getting started guide

- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Node.js implementation

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Python implementation

**Claude Desktop:**

- [Release Notes](https://support.claude.com/en/articles/12138966-release-notes) - Version updates

- [Desktop Extensions Blog](https://www.anthropic.com/engineering/desktop-extensions) - Architecture overview

------------------------------------------------------------------------

## Getting Help

**Support channels:**

- [MCPB GitHub Issues](https://github.com/modelcontextprotocol/mcpb/issues) - Bug reports and feature requests

- [MCP Specification](https://github.com/modelcontextprotocol/modelcontextprotocol) - Protocol questions

- [Claude Support](https://support.claude.com/en/articles/9015913-how-to-get-support) - General Claude Desktop support

**Community resources:**

- Check repository discussions for community Q&A

- Follow release notes for latest updates

- Review examples for implementation patterns

------------------------------------------------------------------------

## Ready for Public Distribution?

If you've built a working MCPB and want to submit it to the Anthropic Directory for broader distribution and discoverability, see our companion guide: [Submitting to Anthropic Directory](https://support.claude.com/en/articles/12922832-local-mcp-server-submission-guide).

The directory guide covers additional requirements including:

- Mandatory tool annotations for all tools

- Privacy policy requirements

- Minimum of three working examples

- Testing credentials (if applicable)

- Complete submission process and review timeline

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)

Getting Started with Local MCP Servers on Claude Desktop

[](https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq)

Anthropic Connectors Directory FAQ

[](https://support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist)

Enabling and using the desktop extension allowlist

[](https://support.claude.com/en/articles/12614803-using-the-10x-genomics-extension-in-claude)

Using the 10x Genomics Extension in Claude

[](https://support.claude.com/en/articles/12922832-local-mcp-server-submission-guide)

Local MCP Server Submission Guide

Did this answer your question?

😞

😐

😃

[](/en/)

- [Product](https://www.anthropic.com/product)
- [Research](https://www.anthropic.com/research)
- [Company](https://www.anthropic.com/company)
- [News](https://www.anthropic.com/news)
- [Careers](https://www.anthropic.com/careers)

- [Terms of Service - Consumer](https://www.anthropic.com/terms)
- [Terms of Service - Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Privacy Policy](https://www.anthropic.com/privacy)
- [Usage Policy](https://www.anthropic.com/aup)
- [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Compliance](https://trust.anthropic.com/)
