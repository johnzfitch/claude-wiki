---
title: "Legal and compliance"
source_url: "https://code.claude.com/docs/en/legal-and-compliance.md"
category: "02-Claude-Code-CLI"
fetched_at: "2026-04-26T00:00:00Z"
tags: ["claude-code", "security"]
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Legal and compliance

> Legal agreements, compliance certifications, and security information for Claude Code.

## Legal agreements

### License

Your use of Claude Code is subject to:

* [Commercial Terms](https://www.anthropic.com/legal/commercial-terms) - for Team, Enterprise, and Claude API users
* [Consumer Terms of Service](https://www.anthropic.com/legal/consumer-terms) - for Free, Pro, and Max users

### Commercial agreements

Whether you're using the Claude API directly (1P) or accessing it through AWS Bedrock or Google Vertex (3P), your existing commercial agreement will apply to Claude Code usage, unless we've mutually agreed otherwise.

## Compliance

### Healthcare compliance (BAA)

If a customer has a Business Associate Agreement (BAA) with us, and wants to use Claude Code, the BAA will automatically extend to cover Claude Code if the customer has executed a BAA and has [Zero Data Retention (ZDR)](../22-Safety-Policy/zero-data-retention-claude-code-docs-6ec9ee63f1.md) activated. The BAA will be applicable to that customer's API traffic flowing through Claude Code. ZDR is enabled on a per-organization basis, so each organization must have ZDR enabled separately to be covered under the BAA.

## Usage policy

### Acceptable use

Claude Code usage is subject to the [Anthropic Usage Policy](https://www.anthropic.com/legal/aup). Advertised usage limits for Pro and Max plans assume ordinary, individual usage of Claude Code and the Agent SDK.

### Authentication and credential use

Claude Code authenticates with Anthropic's servers using OAuth tokens or API keys. These authentication methods serve different purposes:

* **OAuth authentication** is intended exclusively for purchasers of Claude Free, Pro, Max, Team, and Enterprise subscription plans and is designed to support ordinary use of Claude Code and other native Anthropic applications. More information about how users can authenticate with OAuth tokens can be found in [Logging in to your Claude account](../21-Account-Support/logging-in-to-your-claude-account.md).
* **Developers** building products or services that interact with Claude's capabilities, including those using the [Agent SDK](/en/agent-sdk/overview), should use API key authentication through [Claude Console](../04-API-Reference/Other/platform-claude-com.md) or a supported cloud provider. Anthropic does not permit third-party developers to offer Claude.ai login or to route requests through Free, Pro, or Max plan credentials on behalf of their users.

Anthropic reserves the right to take measures to enforce these restrictions and may do so without prior notice.

For questions about permitted authentication methods for your use case, please [contact sales](https://www.anthropic.com/contact-sales?utm_source=claude_code\&utm_medium=docs\&utm_content=legal_compliance_contact_sales).

## Security and trust

### Trust and safety

You can find more information in the [Anthropic Trust Center](https://trust.anthropic.com) and [Transparency Hub](https://www.anthropic.com/transparency).

### Security vulnerability reporting

Anthropic manages our security program through HackerOne. [Use this form to report vulnerabilities](https://hackerone.com/anthropic-vdp/reports/new?type=team\&report_type=vulnerability).

***

© Anthropic PBC. All rights reserved. Use is subject to applicable Anthropic Terms of Service.
