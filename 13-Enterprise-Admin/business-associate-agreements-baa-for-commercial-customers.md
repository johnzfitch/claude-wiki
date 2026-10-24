---
title: "Business Associate Agreements (BAA) for Commercial Customers | Claude Help Center"
source_url: "https://support.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers"
category: "13-Enterprise-Admin"
fetched_at: "2026-10-23T06:29:14Z"
tags: ["enterprise", "rag"]
---

# Business Associate Agreements (BAA) for Commercial Customers


*This article is about our commercial products such as Claude for Work and the Anthropic API. For our consumer products such as Claude Free, Pro, Max and when accounts from those plans use Claude Code, see **[here](https://privacy.claude.com/en/collections/10663362-consumers)**.*

*For Claude Enterprise features to be covered under a Business Associate Agreement (BAA), the Primary Owner of the organization must activate HIPAA compliance in the HIPAA-ready Claude Enterprise organization settings under “Data and privacy” and accept Anthropic's BAA. Standard Claude Enterprise plans do not include BAA coverage without action from a Primary Owner. For Claude Code (local mode) and Claude Cowork (local mode) to be covered, the Primary Owner must also apply the HIPAA configuration to both products. See **[Use Claude Code (local mode) and Claude Cowork (local mode) on a HIPAA-ready Enterprise plan](https://support.claude.com/en/articles/17318731)**.*

Anthropic provides a BAA covering our HIPAA-ready services, such as use of our first-party API, Claude in Microsoft Foundry, or Enterprise plans. Claude Enterprise Primary Owners can accept the BAA directly when activating HIPAA compliance in the organization settings under “Data and privacy.”

**Important:** To use the 1P API with PHI, your organization’s Primary Owner will need to sign a BAA and then reach out to your Anthropic contact or our **[Sales team](https://claude.com/contact-sales)** to get this turned on.

For clarity, the BAA only covers the single organization that accepted it, and excludes features such as Claude Console, Cowork in the cloud, or features currently in beta such as Claude in Office, Claude Design, Claude Slides, and Claude Docs. As part of the BAA, customers of Anthropic’s HIPAA-ready services are subject to certain configuration requirements and limitations on what features/integrations are available.

Not all API features are covered. See the **[Implementation Guide](https://trust.anthropic.com/resources?s=l1wrssd9hsbi4gak0tp5a6&name=%5Banthropic%5D-hipaa-ready-offering-implementation-guide)** for the full list of eligible and non-eligible features.

**Important: [Covered Models](../15-Claude-AI-Features/covered-models.md)** require 30-day data retention and aren't available with zero data retention (ZDR) enabled unless Anthropic has expressly authorized it for your organization. With the **[HIPAA configuration applied to Claude Code (local mode) and Claude Cowork (local mode)](https://support.claude.com/en/articles/17318731)** on a HIPAA-ready Enterprise plan, members can use Covered Models in both products under the BAA. Claude Code can't use Covered Models while your organization has ZDR for Claude Code, unless Anthropic has expressly authorized it for your organization.

Below is a breakdown of what’s covered under the BAA, by feature and product surface. This article covers:

- Claude Enterprise features

- Claude Code and Claude Cowork features

- API features

- Messages API features

- Product BAA coverage by surface

See **[Manage local session data](../02-Claude-Code-CLI/hipaa-setup.md#manage-local-session-data)** for what Claude Code stores on a member's computer and how to delete it. For Cowork, see **[Manage Cowork data on each computer](https://claude.com/docs/cowork/hipaa-setup#manage-cowork-data-on-each-computer)**.

## What’s covered under Anthropic’s BAA

### Claude Enterprise features

[TABLE]

\*Covered under versions of the BAA accepted after 12/2/25

### Claude Code and Claude Cowork features

Use these tables to check whether you can use a Claude Code or Cowork feature to process protected health information (PHI).

The tables apply to a Claude Enterprise organization that has the HIPAA configuration applied. The HIPAA configuration is an organization setting that brings Claude Code (local mode) and Cowork (local mode) under your Business Associate Agreement (BAA) with Anthropic. "Local mode" means a session that runs on a member's own computer, in one of these places:

- Claude Code in the terminal

- Claude Code in the Code tab of Claude Desktop

- Cowork in Claude Desktop

**Note:**

- If your organization hasn't applied the configuration, see **Coverage without the HIPAA configuration**.

- If you want to apply the configuration, see **[Use Claude Code (local mode) and Cowork (local mode) on a HIPAA-ready Enterprise plan](https://support.claude.com/en/articles/17318731)**.

- If you need the contractual list of Eligible Services, see the **[Implementation Guide for HIPAA Entities](https://trust.anthropic.com/resources?s=l1wrssd9hsbi4gak0tp5a6&name=%5Banthropic%5D-hipaa-ready-offering-implementation-guide)** on the Anthropic Trust Center.

Each table has two columns for every feature. "Availability" says whether members can use the feature. "Coverage under your BAA" says whether your BAA covers it. Check both, because a feature can be available and still not be covered.

**Important:** Process PHI only with a feature marked ✅ **Covered**.

**Availability and coverage values**

Some cells in the "Availability" column add a condition, or name the settings page where an Owner of your organization turns the feature on. Every cell starts with one of these values:

- **Available:** Members can use the feature without any action from an Owner. A feature inside Cowork or the Code tab becomes available after an Owner turns on Cowork or the Code tab.

- **Off until an Owner turns it on:** The feature is off by default. An Owner can turn it on in **Organization settings**.

- **Not available:** The feature is off, and no setting turns it on.

Every cell in the "Coverage under your BAA" column starts with one of these values:

- ✅ **Covered:** Your BAA covers the feature, so members can use it to process PHI. Covered means only that your BAA applies. Whether to allow a feature, such as bypass permissions mode, is your organization's decision.

- ⚠️ **Not covered:** Members can use the feature, right away or after an Owner turns it on, but your BAA doesn't cover it. Keep PHI out of it.

- ❌ **Not available:** The feature isn't available while the HIPAA configuration is applied, so the question of coverage doesn't come up.

Some features that aren't covered are available without any action from an Owner, such as the VS Code and JetBrains extensions and local MCP servers. If you're an Owner, tell members to keep PHI out of every feature marked both **Available** and **Not covered** in the tables below.

**Where members run Claude Code and Cowork**

The table lists the three places that count as local mode, and the other ways members can run Claude Code.

[TABLE]

**Cloud and remote features**

The table lists the features that run a session in the cloud or control a session remotely. None of them are available while the HIPAA configuration is applied.

[TABLE]

**Tools, models, and memory in a session**

The table lists what Claude and members can use inside a Claude Code (local mode) or Cowork (local mode) session.

[TABLE]

**Permission modes**

The table lists the modes that let Claude act with fewer approvals from the member.

[TABLE]

**Connectors, MCP servers, and desktop extensions**

The table lists the features that connect Claude to other tools. Your BAA doesn't cover any of them, even after an Owner turns them on.

[TABLE]

**Skills and plugins**

The table lists each kind of skill and plugin. Several rows depend on one setting named **Skills**, which an Owner turns on or off in **Organization settings \> Plugins & skills**, in the "Policy" tab.

Skill and plugin security scanning isn't available while the HIPAA configuration is applied. Review each skill and plugin before you provide it to members.

[TABLE]

**Other Claude products**

The table lists Claude products other than Claude Code and Cowork. Your BAA doesn't cover any of them.

[TABLE]

**Export, sharing, and feedback**

The table lists features that send session content out of Claude Code or Cowork. None of them are available while the HIPAA configuration is applied. OpenTelemetry export stays available (see **Monitoring and audit**).

[TABLE]

**Monitoring and audit**

The table lists the ways your organization can review sessions and usage.

[TABLE]

**Coverage without the HIPAA configuration**

The table shows what your BAA covers in an organization that has enabled HIPAA but hasn't applied the HIPAA configuration. Members can still use Claude Code and Cowork in that organization where an Owner has them turned on.

[TABLE]

### API features (on a HIPAA ready API org)

[TABLE]

Data retention periods within a HIPAA-Enabled API Organization are described in Anthropic’s **[public documentation](../04-API-Reference/Other/manage-claude-api-and-data-retention.md)**.

### Messages API features

The Messages API is covered as an Eligible Service under your BAA. The following Messages API features are covered under your BAA. Messages API features not listed below are not covered under your BAA.

[TABLE]

\*Covered under versions of the BAA accepted after 4/1/26

## Product BAA coverage by surface

In this table, "the HIPAA configuration" is the configuration that the Primary Owner applies to Claude Code (local mode) and Cowork (local mode). Applying it is a separate step from enabling HIPAA. See **[Use Claude Code (local mode) and Cowork (local mode) on a HIPAA-ready Enterprise plan](https://support.claude.com/en/articles/17318731)**.

[TABLE]

Please see our **[Trust Portal](https://trust.anthropic.com/resources?s=rgirr4qe8u7ek8c2igx3&name=claude-for-enterprise-hipaa-ready-offering-implementation-guide)** for more information about our compliance commitments.
