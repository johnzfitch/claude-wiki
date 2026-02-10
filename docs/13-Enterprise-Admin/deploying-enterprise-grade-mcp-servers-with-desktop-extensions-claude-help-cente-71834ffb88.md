---
category: "13-Enterprise-Admin"
fetched_at: "2026-02-10T10:49:31Z"
source_url: "https://support.claude.com/en/articles/12702546-deploying-enterprise-grade-mcp-servers-with-desktop-extensions"
title: "Deploying enterprise-grade MCP servers with desktop extensions | Claude Help Center"
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

[](#h_c56ebfa46f)

[](#h_9b1c720aef)

[All Collections](/en/)

[Claude Desktop](https://support.claude.com/en/collections/16163169-claude-desktop)

[Desktop Extensions](https://support.claude.com/en/collections/17879657-desktop-extensions)

Deploying enterprise-grade MCP servers with desktop extensions

# Deploying enterprise-grade MCP servers with desktop extensions

Updated this week

Table of contents

[](#h_c56ebfa46f)

[](#h_9b1c720aef)

Desktop extensions are installable packages that run Model Context Protocol (MCP) servers locally on your machine. They provide Claude Desktop with secure access to your local resources, internal systems, and personal tools without the complexity of remote infrastructure.

With desktop extensions, you can deploy enterprise-grade MCP implementations with fine-grained admin controls. This article explains why desktop extensions are valuable for organizations and how to use them effectively.

## Why use desktop extensions?

### Seamless authentication

Desktop extensions operate within your corporate network boundaries, using the user’s existing authenticated context without requiring additional firewall rules or VPN configurations. They leverage existing SSO and browser sessions automatically with no token management required – credentials stay securely on user devices.

### Access internal resources

Desktop extensions connect to internal wikis, JIRA, Confluence, and other systems behind your firewall. They can query private databases and APIs without VPN configuration, connect to on-premises systems like SAP, Oracle, and custom applications, and access internal resources without exposing them on public infrastructure.

### Read and manipulate local resources

Desktop extensions provide access to local resources that remote connectors cannot reach. This includes direct filesystem access for code editing and Git operations, integration with locally installed tools like Docker, IDEs, and databases, control over desktop applications via local APIs, and hardware integration for specialized workflows.

### Instant deployment with minimal infrastructure overhead

One-click installation through Claude Desktop comes with no dependencies to manage. The built-in [Node.js](http://node.js) runtime is included, there’s no cloud infrastructure to provision, and updates are distributed directly through the extension marketplace.

### Enterprise-grade controls

Organization owners can upload custom extensions to their organization and control which desktop extensions their users have access to through the desktop extension allowlist. To learn more about managing desktop extensions in your organization, see Enabling and using the desktop extension allowlist.

## Enterprise use cases

**Multiple enterprises are building desktop extensions to serve a variety of use cases:**

- As secure proxies to internal MCP servers, giving them complete control over access, authentication, and audit logs while maintaining their zero-trust architecture.

- To give Claude access to internal documentation and knowledge bases.

- To connect to development tools and databases securely, and maintain complete control over authentication, authorization, and audit logging.

Desktop extensions eliminate the traditional tradeoff between security and usability—providing Claude with powerful capabilities while maintaining your enterprise security posture.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/10065433-installing-claude-desktop)

Installing Claude Desktop

[](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)

Getting Started with Local MCP Servers on Claude Desktop

[](https://support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist)

Enabling and using the desktop extension allowlist

[](https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows)

Deploy Claude Desktop for Windows

[](https://support.claude.com/en/articles/12922929-building-desktop-extensions-with-mcpb)

Building Desktop Extensions with MCPB

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
