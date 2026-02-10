---
category: "14-Connectors"
fetched_at: "2026-02-10T10:49:21Z"
source_url: "https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq"
title: "Anthropic Connectors Directory FAQ | Claude Help Center"
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

[](#h_145a48bef0)

[](#h_50d6d141b6)

[](#h_8ce70a4890)

[](#h_eed239a278)

[](#h_063efc7839)

[](#h_05e2c49fde)

[](#h_8063f85fa1)

[](#h_02019eda84)

[](#h_f9fc7edf85)

[](#h_e8c9923d36)

[](#h_bfc45cefaf)

[](#h_5539a36fd8)

[All Collections](/en/)

[Connectors](https://support.claude.com/en/collections/15399129-connectors)

[General](https://support.claude.com/en/collections/17879426-general)

Anthropic Connectors Directory FAQ

# Anthropic Connectors Directory FAQ

Updated this week

Table of contents

[](#h_145a48bef0)

[](#h_50d6d141b6)

[](#h_8ce70a4890)

[](#h_eed239a278)

[](#h_063efc7839)

[](#h_05e2c49fde)

[](#h_8063f85fa1)

[](#h_02019eda84)

[](#h_f9fc7edf85)

[](#h_e8c9923d36)

[](#h_bfc45cefaf)

[](#h_5539a36fd8)

## What is MCP?

MCP stands for Model Context Protocol, an open standard created by Anthropic that allows AI applications to connect to tools and data sources. For comprehensive information about MCPs and how to get started, please refer to our remote MCP guide: [Getting Started with Custom Connectors Using Remote MCP](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp).

## What is the Connectors Directory?

The [Connectors Directory](https://claude.com/connectors) aims to showcase Model Context Protocol servers that work with Claude across all our platforms - Claude web, Claude Desktop, our Claude mobile apps, Claude Code, and our API. The Connectors Directory serves as a single hub where users can discover MCP servers that Anthropic has reviewed.

### How do I get my MCP listed in the directory?

You can fill out our [Connectors Directory server review form](https://docs.google.com/forms/d/e/1FAIpQLSeafJF2NDI7oYx1r8o0ycivCSVLNq92Mpc1FPxMKSw1CzDkqA/viewform) and we'll reach out about next steps if your MCP would be a good fit for the directory at this time.

### Are there standards my MCP will need to adhere to for inclusion in the directory?

Yes, servers must adhere to the security, safety, and compatibility standards laid out in our [MCP Directory Policy](https://support.claude.com/en/articles/11697096-anthropic-mcp-directory-policy). Adherence to these standards does not guarantee inclusion in the directory.

### I filled out the submission form but haven't heard back yet, how long will it take?

While we strive to review every submission as quickly as we can, due to overwhelming interest we cannot promise that we will accept your submission or respond to it individually.

## 1. Authentication and Authorization

### Is OAuth 2.0 required if we don't need user authentication?

OAuth 2.0 is only required if authentication is needed for the MCP server. Servers that do not require authentication do not require OAuth.

### Does Claude support machine-to-machine (client credentials) OAuth flow?

No. Pure client credentials flow (machine-to-machine OAuth with just client_id/client_secret and no user interaction) is not supported. We can provision a static client_id/client_secret for Claude, but users must still complete an OAuth consent flow to authenticate their individual accounts. This works on claude.ai and Claude Desktop, but not Claude Code because Claude Code establishes connections directly from user’s computer to your MCP server (and thus don’t have access to the static credentials).

### Can we identify individual users without implementing OAuth?

No. OAuth is the only way to uniquely identify users. We do not forward IP addresses, user IDs, or other metadata from end-users to MCP servers.

### Where does MCP server communication happen - client-side or Anthropic servers?

It depends on the product surface. Communication occurs through Anthropic servers (claude.ai, Claude Desktop), user's browser, or user's local clients (Claude Code). There is no centralized connection method across all surfaces currently.

### Can users authenticate with personal credentials from within a corporate Claude account?

Yes. Users authenticate with MCP servers on a per-server basis. They can use personal authentication credentials for MCP servers even when logged into claude.ai with a corporate account.

### Can we implement per-tool OAuth instead of per-server OAuth?

No. OAuth occurs when the client connects to the MCP server, not at the tool level. You can enforce tool-level permissions based on user authentication after server connection is established.

### When a user disconnects an MCP tool, are OAuth tokens revoked?

Tokens are removed from Anthropic's systems but not from your own systems. Access and refresh tokens at your identity provider remain valid until expiration, and session cookies are not cleared (as they are browser-level, outside Claude's control).

### How can our MCP service signal to Claude that a user's session is invalid?

Return a 401 Unauthorized response. To trigger full regeneration of DCR client credentials, return an invalid_client error as per RFC 6749 section 5.2.

### Are client_id/client_secret required for standard OAuth flows?

No. Client credentials are not required for standard OAuth flows with user authentication.

## 2. Rate Limiting and Abuse Prevention

### How can we implement per-user rate limiting without OAuth?

Per-user rate limiting requires OAuth. Without OAuth, your options are:

- Option 1: No authentication with global rate limiting

- Option 2: IP allowlisting using Claude's static IPs

### Can we use IP allowlisting to restrict MCP server access to Claude users only?

We strongly recommend using OAuth and not using IP allowlisting. However, this is possible using the static IP addresses available at [https://docs.claude.com/en/api/ip-addresses](https://docs.claude.com/en/api/ip-addresses).

Important limitations:

- Only works for claude.ai and Claude Desktop. Your MCP server will not work in Claude Code.

- Egress IPs could change - advanced notice of change will be posted in docs

- Not recommended as sole security measure, but okay to use when OAuth is not feasible

### Does Claude provide rate limiting or DDoS protection for MCP servers?

No. MCP server owners must implement their own rate limiting and abuse prevention measures.

## 3. Technical Limits and Constraints

### What is the maximum token size for MCP tool results?

25,000 tokens. Use pagination, filtering, or limit parameters to reduce response size if needed.

### What are the timeout limits for MCP tools?

Timeouts vary by component:

- Claude Code: Configurable via MCP_TOOL_TIMEOUT setting

- Claude.ai and Claude Desktop: 300 seconds (5 minutes)

## 4. Directory Submission and Requirements

### Which Claude plan types can access Connectors?

All users can access connectors, except for custom connectors, which are available for paid plans only (Pro, Max, Team, and Enterprise).

### Do we need a specific Claude plan to submit an MCP to the directory?

No. Any organization can submit to the directory regardless of plan type.

### Do we need to provide Anthropic with a test account?

If your server requires authentication / an account to use, we will need you to provide us with a testing account for initial QA purposes. Including dummy data in the account is also helpful to check functionality.

### How many tools should an MCP server provide?

No minimum or maximum requirement. We recommend that you start with a useful set of tools and expand capabilities over time.

### What are the performance requirements for MCP servers?

There are currently no specific SLA requirements. However, connectors with performance or reliability issues may be removed from the directory.

### What are the most common reasons MCP submissions are delayed or rejected?

Top issue: Missing tool annotations (30% of rejections)

Requirement: All tools MUST include readOnlyHint or destructiveHint

Impact: Immediate rejection, requires code changes.

Not optional: Compliance requirement per MCP Directory Policy

Example:

    {
    "name": "read_data",
    "readOnlyHint": true
    }

## 5. Data Privacy and Legal

### What telemetry does Anthropic collect from MCP tool calls?

Telemetry includes all parameters and data passed into tool calls as well as the response from MCP server.

### Is MCP data used for training Claude models?

We only train on consumer data when users explicitly opt in. See [https://www.anthropic.com/news/updates-to-our-consumer-terms](https://www.anthropic.com/news/updates-to-our-consumer-terms) for details. We do not train on Team/Enterprise plans.

### Can MCP servers identify which Claude SKU the user is on?

No. MCP servers cannot determine the Claude SKU being used.

### What does 'Data Processing Agreement URL' mean in the submission form?

Provide a URL to your company's data processing terms applicable to the MCP service. This does not need to be MCP-specific - your standard DPA is acceptable.

### Are connectors available globally? Can we restrict by geography?

Connectors are available to Claude users globally. Geographic restriction is not supported. You can guide the user and Claude’s understanding of any geographic limitations to your MCP description or tool descriptions if needed (e.g., 'only U.S. organizations available').

### Where can I find the MCP Directory Terms of Service and data policies?

Key resources:

- [MCP Directory Terms](https://support.claude.com/en/articles/11697081-anthropic-mcp-directory-terms-and-conditions)

- [MCP Directory Policy](https://support.claude.com/en/articles/11697096-anthropic-mcp-directory-policy)

### What are data protection (e.g. GDPR, CCPA, LGPD) compliance requirements for MCP servers?

MCP servers must handle compliance independently from Claude. If a user exercises a legal data protection right with your service, you must handle this on your end.

### Where must I include privacy policies for local connectors (desktop extensions)?

In your .mcpb, there are two required locations:

1\. README.md - Add a "Privacy Policy" section with URL or full text.

2\. manifest.json - Add privacy_policies array with HTTPS URLs (requires manifest_version 0.2+)

Example:

    {
    "manifest_version": "0.2",
    "privacy_policies": ["https://your-domain.com/privacy"],
    ...
    }

**Must cover:** What data is collected, how it's used/stored, third-party sharing, retention, and contact info. ⚠️ Missing privacy policy will lead to an immediate rejection.

## 6. User Experience and Branding

### How do we update our connector's icon?

We use the Google provided favicon, so you can customize your connector’s icon URL by updating the favicon for your connector URL. You can verify the icon that we will use at [https://www.google.com/s2/favicons?domain=\<YOUR_CONNECTOR_URL\>&sz=64](https://www.google.com/s2/favicons?domain=%3CYOUR_CONNECTOR_URL%3E&sz=64)

Be sure to test each favicon size (16, 32, 48, 64, 96, 128) by updating the &sz= portion of the URL.

**Remote connectors:**

- If using a custom icon URL: Update the icon at your provided URL.

- If relying on auto-detection: Icons are pulled from the Google-indexed favicon at your MCP server URL. Update your favicon and wait for Google to re-index.

Otherwise, provide us with a URL with the favicon you wish to use as your icon.

**Local connectors (desktop extensions):** Replace \`icon.png\` in your bundle and redistribute the updated \`.mcpb\` package to users.

### Does the connector descriptions in Claude support markdown?

Yes. Markdown formatting is supported in connector descriptions.

### Can we include account requirements and sign-up links in the connector details?

Yes. Please include account requirement language (e.g., 'free registered account required') and hyperlinks to sign-up pages in the connector details.

### How can we ensure users see our Terms of Service before connecting?

Implement an OAuth screen. This is the only way to guarantee TOS display. Without OAuth, users could theoretically add connectors to Claude Desktop by directly editing claude_desktop_config.json.

### Can we show consent language with TOS/Privacy Notice links during installation?

Include language in the connector description, but there is no special consent flow or popup. Use an OAuth screen to ensure users see and agree to terms.

## 7. Technical Implementation

### Is SSE transport acceptable, or must we use Streamable HTTP?

You must use Streamable HTTP.

### Can we add server-level descriptions or only tool-level descriptions?

Only tool-level descriptions are currently supported. No server-level description exists. This requires repeating steering guidance across individual tool descriptions. We recognize this is inconvenient and are exploring improvements.

### How do we make local MCP servers (.mcpb) available in Claude Code?

Use the [plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces). Node.js is recommended over Python or other languages for local MCPs due to better compatibility with Claude Desktop's built-in runtime.

### What are the observability best practices for local MCPs in Claude Desktop?

Local MCPs can only log to ~/Library/Logs/Claude/mcp\*.log. Users must manually share log files for troubleshooting. Direct log transmission from local MCP servers is not supported due to security constraints.

## 8. Testing and Debugging

### IP allowlisting isn't working. How do we debug connection issues?

Temporarily remove the IP allowlist to verify other configuration is correct. If connection works without allowlist, the issue is with IP filtering configuration.

### What testing should we complete before submitting to the directory?

Essential testing prevents 80% of submission delays. See our guides for submitting remote and local connectors for best-practices and a pre-submission checklist.

## 9. Common Implementation Patterns

### What authentication approach should we use for our MCP?

Choose based on your security requirements and constraints:

***Option 1: No Auth + Global Rate Limiting***

Best for: Public data with low abuse risk

- Simplest implementation, works across all Claude surfaces

- No per-user rate limiting, accessible by public internet

- Can add IP allowlisting to restrict to Claude-only traffic

***Option 2: Full OAuth with User Registration***

Best for: Enterprise security, sensitive data, per-user rate limiting

- Most secure, works across all surfaces, full user identification

- Requires user registration system, more complex implementation

- Recommended approach for production systems

***Option 3: IP-allowlisting***

We strongly recommend Option 2 over Option 3, but if implementing OAuth is truly infeasible, you can still get some restricted access to Claude users only

- No ability to identify individual users, but restricts to requests from [claude.ai](http://claude.ai) and Claude Desktop.

- MCP server will not work with Claude Code

- Implementation: Use [Claude Static IPs](https://docs.claude.com/en/api/ip-addresses)

## 10. Key Resources

Important links:

- Claude Static IPs: [https://docs.claude.com/en/api/ip-addresses](https://docs.claude.com/en/api/ip-addresses)

- MCP Directory Submission Forms: [https://docs.google.com/forms/d/e/1FAIpQLSeafJF2NDI7oYx1r8o0ycivCSVLNq92Mpc1FPxMKSw1CzDkqA/viewform](https://docs.google.com/forms/d/e/1FAIpQLSeafJF2NDI7oYx1r8o0ycivCSVLNq92Mpc1FPxMKSw1CzDkqA/viewform)

- MCP Directory Terms: <https://support.claude.com/en/articles/11697081-anthropic-mcp-directory-terms-and-conditions>

- MCP Directory Policy: <https://support.claude.com/en/articles/11697096-anthropic-mcp-directory-policy>

- Training Opt-in Policy: [https://www.anthropic.com/news/updates-to-our-consumer-terms](https://www.anthropic.com/news/updates-to-our-consumer-terms)

- MCP Protocol Specification: [https://modelcontextprotocol.io](https://modelcontextprotocol.io)

- Local Desktop MCPB Bundling Utility: [https://github.com/anthropics/mcpb](https://github.com/anthropics/mcpb)

- MCPB Manifest Specification: [https://github.com/anthropics/mcpb/blob/main/MANIFEST.md](https://github.com/anthropics/mcpb/blob/main/MANIFEST.md)

- [Claude Desktop Release Notes](https://support.claude.com/en/articles/12138966-release-notes)

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)

Getting Started with Local MCP Servers on Claude Desktop

[](https://support.claude.com/en/articles/11176164-pre-built-web-connectors-using-remote-mcp)

Pre-built Web Connectors Using Remote MCP

[](https://support.claude.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers)

Building Custom Connectors via Remote MCP Servers

[](https://support.claude.com/en/articles/12922490-remote-mcp-server-submission-guide)

Remote MCP Server Submission Guide

[](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy)

Anthropic Software Directory Policy

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
