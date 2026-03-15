---
category: "99-Other"
fetched_at: "2026-03-15T04:10:42Z"
source_url: "https://support.claude.com/en/articles/13455879"
title: "Use Cowork on Team and Enterprise plans | Claude Help Center"
---

4.  Use Cowork on Team and Enterprise plans

# Use Cowork on Team and Enterprise plans

Updated yesterday


This article explains important limitations and considerations for Team and Enterprise organizations using Cowork during the research preview period.

## Availability

Cowork is available as a research preview for paid plans (Pro, Max, Team, Enterprise) on:

- **Claude Desktop for macOS**

  - **[Click here](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect)** to download

- **Claude Desktop for Windows** (x64 only)

**Windows users:** Cowork requires the latest version of Claude for Windows. Download or update at **[claude.com/download](https://claude.com/download)**.

Windows arm64 is not supported.

------------------------------------------------------------------------

## Admin controls

Cowork will be on by default when the research preview launches, but organization owners can manually disable it.

**How to enable or disable Cowork:**

1.  Log in to your Team or Enterprise organization as an Owner or Primary Owner.

2.  Navigate to **[Organization settings \> Capabilities](https://claude.ai/admin-settings/capabilities)**.

3.  Locate the **Cowork** toggle.

4.  Toggle off to disable Cowork for all users in your organization.

**Note:** This is an organization-wide setting. Granular controls by user or role are not available during the research preview.

### Plugins

Plugins are included with Cowork and controlled by the same admin toggle—there's no separate setting to manage plugin access within Cowork.

For details on what members can do with plugins, see **[Use plugins in Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)**.

------------------------------------------------------------------------

## Manage plugins for your organization

Owners can create plugin marketplaces to distribute curated plugins across their organization. This gives you control over which plugins your team members see and use in Cowork.

For each plugin, you can set one of three installation preferences:

- **Auto-install** — Automatically added for everyone in your organization. Members can uninstall if they choose.

- **Available** — Appears in the plugin catalog for members to install on their own.

- **Not available** — Hidden from the catalog. Useful for staging or deprecating plugins.

You can populate your marketplace by uploading plugin files directly. To get started, go to **Organization settings \> Plugins** in Claude Desktop.

For a full walkthrough, see **[Manage plugins for your organization](https://support.claude.com/en/articles/13837433-manage-cowork-plugins-for-your-organization)**.

------------------------------------------------------------------------

## Company branding

Cowork now surfaces your organization's branding, including a redesigned home screen tailored to your team. Team and Enterprise owners can configure branding within **Organization settings**.

------------------------------------------------------------------------

## Compliance and monitoring limitations

Cowork currently lacks several enterprise monitoring and compliance capabilities. These limitations are important to understand before enabling Cowork for your organization.

### No audit logging or data exports

Cowork activity is **not captured** in:

- Audit Logs

- Compliance API

- Data Exports

If your organization requires audit trails for compliance purposes, do not enable Cowork for regulated workloads.

### OpenTelemetry support

Team and Enterprise owners can track usage, costs, and tool activity across their teams using OpenTelemetry. This provides visibility into how Cowork and plugins are being used, though it doesn't replace audit logging for compliance purposes.

For more information, see **[Monitoring](https://claude.com/docs/cowork/monitoring)** in our Claude Docs.

### Local conversation storage

Cowork stores conversation history locally on users' computers. This data is not subject to Anthropic's standard **[data retention policies](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)** and cannot be centrally managed or exported by admins.

### Access controls

The Cowork toggle is organization-wide — either all members have access or none do. If you need to selectively enable Cowork for specific users or teams, reach out to your Anthropic Contact or our **[Sales team](https://claude.com/contact-sales)**.

Within Cowork, admins have more granular control over plugins. You can set per-plugin installation preferences to control which plugins are auto-installed, available for self-service, or hidden from your organization's catalog. See **[Manage plugins for your organization](https://support.claude.com/en/articles/13837433-manage-cowork-plugins-for-your-organization)** for details.

------------------------------------------------------------------------

## Security considerations

### Prompt injection risks

Cowork has unique risks due to its agentic nature and internet access. While we've implemented safety measures including model training and content classifiers, the risk of prompt injection attacks is non-zero.

Users should:

- Avoid granting access to files with sensitive information

- Monitor Claude for suspicious actions

- Limit browser and web access to trusted sources

- Report suspicious behavior immediately

For detailed guidance, see **[Using Cowork safely](https://support.claude.com/en/articles/13364135-using-cowork-safely)**.

### Network access

Cowork respects your organization's current network egress permissions. Review your network access settings in **[Organization settings \> Capabilities](https://claude.ai/admin-settings/capabilities)** under **Code execution** before enabling Cowork.

**Important:** Network egress permissions don't apply to the **[web search tool](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search)**. Team or Enterprise plan owners can turn off web search for Cowork and Chat in **[Organization settings \> Capabilities](https://claude.ai/admin-settings/capabilities)**.

------------------------------------------------------------------------

Related Articles


Get started with Cowork


Use Cowork safely


Manage Cowork plugins for your organization


Use plugins in Cowork


Schedule recurring tasks in Cowork
