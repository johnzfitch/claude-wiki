---
category: "99-Other"
fetched_at: "2026-02-10T10:49:35Z"
source_url: "https://support.claude.com/en/articles/13200993-restrict-access-to-claude-with-ip-allowlisting"
title: "Restrict access to Claude with IP allowlisting | Claude Help Center"
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

[](#h_522036d853)

[All Collections](/en/)

[Team and Enterprise Plans](https://support.claude.com/en/collections/9387370-team-and-enterprise-plans)

[Enterprise Plan](https://support.claude.com/en/collections/10351014-enterprise-plan)

Restrict access to Claude with IP allowlisting

# Restrict access to Claude with IP allowlisting

Updated this week

Table of contents

[](#h_522036d853)

IP allowlisting is available for Enterprise plans only.

IP allowlisting enables Enterprise plan administrators to control which IP addresses can access Claude through their organization. This feature ensures that requests can only be made from approved network locations, providing an additional layer of security.

When enabled, we validate the source IP address of every authenticated request against your organization's configured allowlist. Requests from IP addresses not added to the allowlist will be blocked.

IP allowlisting supports CIDR ranges. For example: `10.0.0.0/8, 2001:db8::/32`.

## How to configure IP allowlisting

If your Enterprise organization is interested in enabling an IP allowlist, please compile a list of all necessary CIDR ranges for your organization, including office locations, VPN exit points, and any other approved access points. Omitting required CIDR ranges could result in users getting locked out of Claude. Then, reach out to your Anthropic Contact or our [Sales team](https://claude.com/contact-sales) to share your list of CIDR ranges. They can add these to your account’s allowlist to enable the feature.

When a request originates from an IP address that’s not in your allowlist, access is denied. Users should contact their IT administrator if they believe they're being blocked in error.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)

Getting Started with Local MCP Servers on Claude Desktop

[](https://support.claude.com/en/articles/11506255-getting-started-with-claude-in-slack)

Getting started with Claude in Slack

[](https://support.claude.com/en/articles/12157520-claude-code-usage-analytics)

Claude Code usage analytics

[](https://support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist)

Enabling and using the desktop extension allowlist

[](https://support.claude.com/en/articles/13065128-claude-in-chrome-admin-controls)

Claude in Chrome Admin Controls

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
