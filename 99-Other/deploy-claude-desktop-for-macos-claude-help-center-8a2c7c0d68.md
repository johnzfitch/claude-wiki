---
category: "99-Other"
fetched_at: "2026-02-10T10:49:30Z"
source_url: "https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos"
title: "Deploy Claude Desktop for macOS | Claude Help Center"
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

[](#h_c88db44185)

[](#h_f99b92b322)

[](#h_57f9f58867)

[](#h_345e71dc18)

[](#h_a4f41a10a9)

[All Collections](/en/)

[Claude Desktop](https://support.claude.com/en/collections/16163169-claude-desktop)

[General](https://support.claude.com/en/collections/17879568-general)

Deploy Claude Desktop for macOS

# Deploy Claude Desktop for macOS

Updated this week

Table of contents

[](#h_c88db44185)

[](#h_f99b92b322)

[](#h_57f9f58867)

[](#h_345e71dc18)

[](#h_a4f41a10a9)

Administrators on Team or Enterprise plans can deploy Claude Desktop automatically to manage installations and updates centrally. Claude Desktop installs to \`/Applications\` and updates automatically when new versions are released, unless disabled via enterprise policies.

## Available formats:

\- \`.pkg\` - Standard macOS installer package (recommended for enterprise)

\- \`.dmg\` - Drag-and-drop installation

## Download:

- [Universal (x64 or arm64) Claude PKG](https://claude.ai/api/desktop/darwin/universal/pkg/latest/redirect)

The Universal build is compatible with both Intel and Apple Silicon machines and supports all Mac hardware.

## Deploy via MDM

Upload the PKG to your MDM solution (Jamf, Kandji, Microsoft Intune) and deploy to target machines.

## Configuration

To configure Claude Desktop settings such as auto-updates, extensions, and MCP servers, see the [Enterprise Configuration article](https://support.claude.com/en/articles/12622667-enterprise-configuration).

## Troubleshooting

### Users cannot update Claude Desktop

Claude Desktop can be installed to either the user's Applications folder or the system Applications folder, which affects update permissions.:

- \`~/Applications\` (user folder): Users can update without administrator privileges

- \`/Applications\` (system folder): Users need administrator access and write permissions to \`/Applications\`, \`Claude.app\`, and all contained files

For shared machines, disable auto-updates via enterprise policies and manage updates centrally through your MDM solution.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/10065433-installing-claude-desktop)

Installing Claude Desktop

[](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)

Getting Started with Local MCP Servers on Claude Desktop

[](https://support.claude.com/en/articles/12622667-enterprise-configuration)

Enterprise Configuration

[](https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows)

Deploy Claude Desktop for Windows

[](https://support.claude.com/en/articles/12702546-deploying-enterprise-grade-mcp-servers-with-desktop-extensions)

Deploying enterprise-grade MCP servers with desktop extensions

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
