---
category: "16-Mobile-Desktop"
source_url: "https://support.claude.com/en/articles/12922929-building-desktop-extensions-with-mcpb"
---


This guide will help you build an MCP Bundle (.mcpb) to create a desktop extension for internal use, private distribution, or as a foundation for submission to Anthropic’s Connectors Directory.

 

 

1. Introduction
What is an MCPB?

MCPB (.mcpb) files are zip archives containing a local MCP server and manifest.json. They enable single-click installation in Claude Desktop, similar to browser extensions.

 

Key characteristics:

Runs locally on user's machine

Communicates via stdio transport

Bundles all dependencies

Works offline

No OAuth required

Learn more:

MCPB Repository - Complete specification and architecture

Desktop Extensions Blog Post - Overview and use cases

 

When should I use a local server (MCPB) vs a remote server?

Choose a local server (MCPB) for:

 

Internal Systems and Security

Access systems behind your firewall (JIRA, Confluence, internal wikis, private databases)

Seamless authentication - Uses existing SSO and browser sessions automatically, no token management

Zero-trust compliance - Operates within your corporate network boundaries without exposing internal resources publicly

Local Resources

Direct filesystem access for code editing and Git operations

Integration with locally installed tools (Docker, IDEs, databases)

Hardware integration and desktop application control

Privacy-sensitive operations that shouldn't leave the user's machine

Enterprise Deployment

One-click installation with built-in Node.js runtime (no dependencies to manage)

No cloud infrastructure, VPN configurations, or firewall rules required

Organization-level controls - Admins can upload custom extensions and manage access via allowlists

Complete control over authentication, authorization, and audit logs
​

Choose a remote connector for:

Cloud services and public APIs requiring centralized infrastructure

Distribution across claude on web, mobile and desktop

Services needing centralized updates across all users

OAuth flows requiring server-side token management

Public-facing integrations used by multiple organizations

Key difference: MCPBs run on the user's machine via stdio transport with access to local and internal resources. Remote connectors run on your servers via HTTPS and are accessed through Anthropic's infrastructure.

 

Real-world use: Organizations are building MCPBs as secure proxies to internal MCP servers, for internal documentation access, and to connect development tools while maintaining their security architecture.

 

For remote connector guidance: See MCP Partner FAQ for complete remote connector documentation.

 

 

2. Getting Started
Which programming language should I use?

Node.js is strongly recommended because:

Ships with Claude for macOS and Windows (zero installation friction for users)

Users don't need separate runtime installation

Best compatibility and reliability with Claude Desktop

Extensive MCP SDK support

 

 

What platforms should I support?

Claude Desktop runs on:

macOS (darwin)

Windows (win32)

Specify supported platforms in your manifest.json compatibility section.

 

Best practice: Test on both platforms even if you primarily develop on one.

 

Platform compatibility details: See MCPB Manifest Spec - Compatibility for platform specification and runtime requirements.

 

 

How do I create my first MCPB?

Follow this five-step process:

 

1. Install MCPB CLI: npm install -g @anthropic-ai/mcpb

2. Create your MCP server (see MCP SDK)

3. Run mcpb init to create manifest.json

4. Run mcpb pack to bundle

5. Install and test in Claude Desktop

 

For detailed implementation guidance: 

MCPB Repository - Complete getting started guide, CLI usage, and specifications

MCPB Examples - Working reference implementations including "Hello World"

MCP SDK - Core protocol implementation

For comprehensive guidance on development, testing, and best practices, see the MCPB README's "For Bundle Developers" section.

Important: Before distributing your MCPB, review the testing and best practices guidance in the MCPB README to ensure quality.

 

 

3. Configuration
What is manifest.json?

The manifest.json file is required metadata that describes your MCPB - what it does, how to run it, which tools it provides, and what configuration it needs.

 

For the most up to date information, refer to the official MCPB Specification.

MCPB Manifest Spec - Full schema with all fields

Example Manifests - Real-world implementations

CLI Documentation - Command reference

 

 

How do I add an icon?

Icons are optional but recommended for professional appearance.

 

Basic approach: Include icon.png file in your bundle root directory and reference it in manifest.json.

 

Requirements:

File name: icon.png (or custom path)

Size: 512×512px recommended (minimum 256×256px)

Format: PNG with transparency support

Location: Bundle root or specified path

Advanced options: Multiple icon variants for different sizes and themes (light/dark mode support).

 

Implementation details: See MCPB Manifest Spec - Icons for:

Icon field configuration

Multiple icon variants syntax

Size and theme specifications

Best practices and requirements

 

 

How do users configure my MCPB?

Define user_config section in manifest.json. Claude Desktop automatically creates a settings UI where users can configure your extension.

 

See MCPB Manifest Spec - User Configuration for the complete implementation:

Full schema and examples

All configuration types and properties

Validation constraints

Sensitive data handling

Multi-select patterns

 

 

How do users install my MCPB?

There are three different installation methods:

Double-click - Download .mcpb file and double-click to open

Drag-and-drop - Drag .mcpb file into Claude Desktop window

File menu - Developer → Extensions → Install Extension → select .mcpb file

All methods open installation UI where users can:

Review extension details and permissions

Configure required settings

Grant necessary permissions

Complete installation

Installation scope: Per-user installation - each user must install separately on their own system.

 

User experience and admin controls: For detailed information about the end-user installation experience and enterprise admin controls (including Team/Enterprise organization management and policy configuration), see:

Getting Started with Local MCP Servers on Claude Desktop - Complete user guide covering directory browsing, installation UI, troubleshooting, and admin controls.

 

 

4. Resources
Official Documentation

MCPB Framework:

MCPB Repository - Complete specification and tools

MCPB Manifest Spec - Full manifest schema

MCPB CLI Documentation - Command-line tool reference

MCPB Examples - Reference implementations

MCP Protocol:

MCP Specification - Protocol documentation

MCP Quickstart - Getting started guide

TypeScript SDK - Node.js implementation

Python SDK - Python implementation

Claude Desktop:

Release Notes - Version updates

Desktop Extensions Blog - Architecture overview

 

 

Getting Help

Support channels:

MCPB GitHub Issues - Bug reports and feature requests

MCP Specification - Protocol questions

Claude Support - General Claude Desktop support

Community resources:

Check repository discussions for community Q&A

Follow release notes for latest updates

Review examples for implementation patterns

 

 

Ready for Public Distribution?

If you've built a working MCPB and want to submit it to the Anthropic Directory for broader distribution and discoverability, see our companion guide: Submitting to Anthropic Directory.

 

The directory guide covers additional requirements including:

Mandatory tool annotations for all tools

Privacy policy requirements

Minimum of three working examples

Testing credentials (if applicable)

Complete submission process and review timeline

Related Articles
Getting Started with Local MCP Servers on Claude Desktop
Anthropic Connectors Directory FAQ
Enabling and using the desktop extension allowlist
Using the 10x Genomics Extension in Claude
Local MCP Server Submission Guide