---
category: "17-Billing-Plans"
fetched_at: "2026-02-10T10:49:36Z"
source_url: "https://support.claude.com/en/articles/13455879-cowork-for-team-and-enterprise-plans"
title: "Cowork for Team and Enterprise plans | Claude Help Center"
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

[](#h_c3231aa0b4)

[](#h_d199ebca95)

[](#h_0ab0817a27)

[All Collections](/en/)

[Team and Enterprise Plans](https://support.claude.com/en/collections/9387370-team-and-enterprise-plans)

[General](https://support.claude.com/en/collections/9811414-general)

Cowork for Team and Enterprise plans

# Cowork for Team and Enterprise plans

Updated this week

Table of contents

[](#h_c3231aa0b4)

[](#h_d199ebca95)

[](#h_0ab0817a27)

This article explains important limitations and considerations for Team and Enterprise organizations using **[Cowork](https://claude.com/product/cowork)** during the research preview period.

Cowork is available as a research preview for all paid plans (Pro, Max, Team, Enterprise) using the Claude Desktop app on macOS.

## **[Download for macOS](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect)**

------------------------------------------------------------------------

## Admin controls

Cowork will be on by default when the research preview launches, but organization owners can manually disable it.

**How to enable or disable Cowork:**

1.  Log in to your Team or Enterprise organization as an Owner or Primary Owner.

2.  Navigate to [Admin settings \> Capabilities](https://claude.ai/admin-settings/capabilities).

3.  Locate the **Cowork** toggle.

4.  Toggle off to disable Cowork for all users in your organization.

**Note:** This is an organization-wide setting. Granular controls by user or role are not available during the research preview.

### Plugins

Plugins are included with Cowork and controlled by the same admin toggle—there's no separate setting to manage plugin access within Cowork.

When Cowork is enabled, users can:

- Access pre-installed knowledge work plugins (e.g., sales, legal, data analysis, finance, productivity)

- Install additional plugins from Anthropic's public repository

- Customize existing plugins or create new ones locally on their machines

**Note:** During the research preview, plugins are saved locally to each user's machine and cannot be centrally provisioned or managed by admins. Admin-provided plugins and org-wide plugin management are planned for a future release.

------------------------------------------------------------------------

## Compliance and monitoring limitations

Cowork currently lacks several enterprise monitoring and compliance capabilities. These limitations are important to understand before enabling Cowork for your organization.

### No audit logging or data exports

Cowork activity is **not captured** in:

- Audit Logs

- Compliance API

- Data Exports

Security teams will have no visibility into Cowork usage through standard enterprise monitoring tools. If your organization requires audit trails for compliance purposes, do not enable Cowork for regulated workloads.

### Local conversation storage

Cowork stores conversation history locally on users' computers. This data is not subject to Anthropic's standard [data retention policies](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data) and cannot be centrally managed or exported by admins.

### No role-based access controls

Cowork access cannot be selectively limited by user, role, or team within your organization. The admin toggle is organization-wide only—either all users have access or none do.

If you need to selectively enable Cowork for specific users or teams, contact your account representative.

------------------------------------------------------------------------

## Security considerations

### Prompt injection risks

Cowork has unique risks due to its agentic nature and internet access. While we've implemented safety measures including model training and content classifiers, the risk of prompt injection attacks is non-zero.

Users should:

- Avoid granting access to files with sensitive information

- Monitor Claude for suspicious actions

- Limit browser and web access to trusted sources

- Report suspicious behavior immediately

See [Using Cowork Safely](https://support.claude.com/en/articles/13364135-using-cowork-safely) for detailed guidance.

### Network access

Cowork respects your organization's current network egress permissions. Review your network access settings in Admin settings \> Capabilities before enabling Cowork.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/9796617-can-you-delete-data-that-i-sent-via-team-and-enterprise-plans)

Can you delete data that I sent via Team and Enterprise plans?

[](https://support.claude.com/en/articles/12489464-using-enterprise-search)

Using Enterprise Search

[](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans)

Managing members on Team and Enterprise plans

[](https://support.claude.com/en/articles/13345190-getting-started-with-cowork)

Getting started with Cowork

[](https://support.claude.com/en/articles/13364135-using-cowork-safely)

Using Cowork safely

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
