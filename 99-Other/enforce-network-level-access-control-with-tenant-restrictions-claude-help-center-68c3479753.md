---
category: "99-Other"
fetched_at: "2026-02-10T10:49:35Z"
source_url: "https://support.claude.com/en/articles/13198485-enforce-network-level-access-control-with-tenant-restrictions"
title: "Enforce network-level access control with Tenant Restrictions | Claude Help Center"
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

[](#h_dfe567f97f)

[](#h_f0f490f8bb)

[](#h_6f99b8da20)

[](#h_fb8ce22699)

[](#h_d2700fbcae)

[](#h_7018c24d98)

[](#h_8b7e90430d)

[](#h_8455619572)

[All Collections](/en/)

[Claude](https://support.claude.com/en/collections/4078531-claude)

[Account Management](https://support.claude.com/en/collections/9811145-account-management)

Enforce network-level access control with Tenant Restrictions

# Enforce network-level access control with Tenant Restrictions

Updated this week

Table of contents

[](#h_dfe567f97f)

[](#h_f0f490f8bb)

[](#h_6f99b8da20)

[](#h_fb8ce22699)

[](#h_d2700fbcae)

[](#h_7018c24d98)

[](#h_8b7e90430d)

[](#h_8455619572)

Tenant Restrictions are available for members of Enterprise plans and Console organizations.

Tenant Restrictions enable IT administrators on Enterprise plans to enforce network-level access control for Claude. This feature ensures that users on corporate networks can only access approved organizational accounts, preventing unauthorized use of personal accounts.

## How It Works

When enabled, your network proxy injects an HTTP header into requests to Claude. Anthropic validates this header and blocks access from any organization not in the allowed list.

**Supported Authentication Methods:**

- Web access ([claude.ai](http://claude.ai))

- Desktop / App Access

- API key authentication

- OAuth token authentication

## Header Format

    anthropic-allowed-org-ids: <org-uuid-1>,<org-uuid-2>,...

- Comma-delimited list of organization UUIDs

- No spaces between values

**Example:**

    anthropic-allowed-org-ids: 550e8400-e29b-41d4-a716-446655440000,6ba7b810-
    9dad-11d1-80b4-00c04fd430c8

## Configuration Steps

### 1. Find Your Organization UUID

Members of Enterprise plans can find this in two different places:

1.  Navigate to [Settings \> Account](https://claude.ai/settings/account) and find **Organization ID**.

2.  Navigate to [Admin settings \> Organization](https://claude.ai/admin-settings/organization) and scroll down to the bottom of the page to locate **Organization ID**.

Members of Console organizations can find this in [Settings \> Organization](https://platform.claude.com/settings/organization).

### 2. Configure Your Network Proxy

Configure your proxy to inject the header for Claude traffic:

    Rule: Claude Tenant Restriction
    Application: claude.ai, api.anthropic.com
    Action: Inject Header
    Header Name: anthropic-allowed-org-ids
    Header Value: 
    TLS Inspection: Required

### 3. Test Your Configuration

From restricted network, test with your org's API key:

    curl https://api.anthropic.com/v1/messages \
      -H "x-api-key: $CLAUDE_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -H "content-type: application/json" \
      -d '{"model":"claude-sonnet-4-20250514","max_tokens":1024,"messages":
     [{"role":"user","content":"Hello"}]}'

## Error Response

When access is blocked, users receive the following error:

    {
      "type": "error",
      "error": {
        "type": "permission_error",
        "message": "Access restricted by network policy. Contact IT Administrator.",
        "error_code": "tenant_restriction_violation"
      }
    }

## Supported Proxy Platforms

- Zscaler ZIA (Cloud App Control policies)

- Palo Alto Prisma Access (SaaS App Management)

- Cato Networks (Tenant Restriction policy)

- Netskope (Header Insertion rules)

- Generic HTTPS proxies with header injection capability

## Use Cases

[TABLE]

## Security Benefits

- **Data Loss Prevention:** Block personal account usage from corporate networks.

- **Compliance:** Enforce data residency and access policies.

- **Shadow IT Control:** Prevent unauthorized Claude usage.

- **Audit Trail:** Complete visibility into access attempts.

## Backward Compatibility

- No impact to networks without tenant restrictions configured.

- Standard authentication continues for unmanaged networks.

- Existing API key authentication remains unchanged.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/9267385-does-anthropic-act-as-a-data-processor-or-controller)

Does Anthropic Act as a Data Processor or Controller?

[](https://support.claude.com/en/articles/12386420-claude-code-faq)

Claude Code FAQ

[](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide)

Microsoft 365 Connector: Security Guide

[](https://support.claude.com/en/articles/13200993-restrict-access-to-claude-with-ip-allowlisting)

Restrict access to Claude with IP allowlisting

[](https://support.claude.com/en/articles/13455879-cowork-for-team-and-enterprise-plans)

Cowork for Team and Enterprise plans

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
