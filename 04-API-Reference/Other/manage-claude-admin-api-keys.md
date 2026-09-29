---
title: "Create an Admin API key - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/admin-api-keys"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:41Z"
tags: ["api", "enterprise"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fadmin-api-keys)





SearchCtrlK

Organization

[Admin API](manage-claude-admin-api.md)[User management](manage-claude-user-management.md)[Workspaces](manage-claude-workspaces.md)

Authentication

[Overview](manage-claude-authentication.md)[Create an Admin API key](manage-claude-admin-api-keys.md)[App Attest](manage-claude-app-attest.md)[Workload Identity Federation](manage-claude-workload-identity-federation.md)[Manage WIF via API](manage-claude-wif-admin-api.md)[WIF reference](manage-claude-wif-reference.md)

Identity providers

Monitoring

[Usage and Cost API](manage-claude-usage-cost-api.md)[Rate Limits API](manage-claude-rate-limits-api.md)[Analytics APIs](manage-claude-analytics-api.md)[Claude Code Analytics API](manage-claude-claude-code-analytics-api.md)[Spend Limits API](manage-claude-spend-limits-api.md)

Data & compliance

[Data residency](../Guides/build-with-claude-data-residency.md)[API and data retention](manage-claude-api-and-data-retention.md)[Access Transparency](manage-claude-access-transparency.md)

[Encryption keys](manage-claude-cmek.md)

[Inference hooks](manage-claude-inference-hooks.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](usage-limits.md)

[Admin](manage-claude-admin-api.md)Authentication

# Create an Admin API key

Copy page



Create an Admin API key for your Claude Console or Claude Enterprise organization.

Copy page



An Admin API key authenticates every API in the **Admin** section of this guide: the [Admin API](manage-claude-admin-api.md), [Analytics APIs](manage-claude-analytics-api.md), [Compliance API](manage-claude-compliance-api.md), [Spend Limits API](manage-claude-spend-limits-api.md), [Usage and Cost API](manage-claude-usage-cost-api.md), and [Rate Limits API](manage-claude-rate-limits-api.md). You do not need a separate key for each API. The one exception is the Admin API's service-account, federation-issuer, and federation-rule endpoints, which accept only an OAuth bearer token with the `org:admin` scope. See [Obtain an OAuth bearer token](manage-claude-admin-api.md#oauth-bearer-token).

Where you create the key depends on which Claude product your organization uses.

## Which key do you need?

| Your organization                                           | Create the key in                                                                           | Key prefix           | Who can create it                                                                                                                                                                          | Works with                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------|---------------------------------------------------------------------------------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Claude Console** (Claude Platform, `platform.claude.com`) | [Claude Console \> Settings \> Admin keys](usage-limits.md) | `sk-ant-admin01-...` | Organization members with the **admin** role                                                                                                                                               | [Admin API](manage-claude-admin-api.md), [Usage and Cost API](manage-claude-usage-cost-api.md), [Rate Limits API](manage-claude-rate-limits-api.md), [Claude Code Analytics API](manage-claude-claude-code-analytics-api.md), and the Compliance API [Activity Feed](manage-claude-compliance-activity-feed.md)                                                        |
| **Claude Enterprise** (`claude.ai`)                         | [claude.ai \> Organization settings \> API](https://claude.ai/admin-settings/api-access)    | `sk-ant-api01-...`   | The parent organization's **primary owner** (all linked organizations). An **organization owner** can create one carrying Compliance API scopes only, restricted to their own organization | [User management](manage-claude-user-management.md) (the Admin API's member, invite, and group endpoints), [Compliance API](manage-claude-compliance-api.md), [Claude Enterprise Analytics API](manage-claude-analytics-api.md), and [Spend Limits API](manage-claude-spend-limits-api.md), according to the [scopes](#choose-scopes-for-a-claude-enterprise-key) you select |

A key created in one organization cannot be used to manage a different organization. If your company uses both Claude Console and Claude Enterprise, create one key in each.

## Create a key for a Claude Console organization

1.  1

    ### Sign in as an organization admin

    Only organization members with the **admin** role can create Admin API keys. See [Organization roles and permissions](manage-claude-admin-api.md#organization-roles-and-permissions).

2.  2

    ### Open Admin keys settings

    Go to [Claude Console \> Settings \> Admin keys](usage-limits.md).

3.  3

    ### Create the key

    Click **Create key**, give it a name, choose a [key expiration](manage-claude-authentication.md#key-expiration), and click **Create**. Claude Console keys do not have selectable scopes; every key carries full access to all endpoints that accept Admin API keys (the service-account and federation endpoints noted at the top of this page do not accept Admin API keys).

4.  4

    ### Copy and store the secret

    Copy the displayed secret (starting with `sk-ant-admin01-`) and store it in your secrets manager. The full secret is shown only once.

## Create a key for a Claude Enterprise organization

1.  1

    ### Sign in as the primary owner or an organization owner

    The **primary owner** of the Claude Enterprise parent organization can create a key that can access every linked organization, or one restricted to a single organization. An **organization owner** can create a key with Compliance API scopes only, restricted to their own organization.

2.  2

    ### Open API settings

    Go to [claude.ai \> Organization settings \> API](https://claude.ai/admin-settings/api-access) and find the **Keys** section.

3.  3

    ### Click + Create key

    Name the key and select the scopes you need from the [scopes table](#choose-scopes-for-a-claude-enterprise-key). The primary owner can combine scopes from different APIs (for example, `read:analytics` and `read:spend_limits`) on a single key.

4.  4

    ### Copy and store the secret

    Copy the displayed secret (starting with `sk-ant-api01-`) and store it in your secrets manager. The full secret is shown only once.

## Choose scopes for a Claude Enterprise key

When you create a Claude Enterprise key, select every scope that the APIs you plan to call require. Scopes are fixed at creation; to add a scope later, create a new key.

| To call...                                                                                                                                                                                                                                                                                                                            | Select these scopes           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| Admin API [user management](manage-claude-user-management.md): list and look up members and invites; read custom roles and their permissions                                                                                                                                                                                    | `read:members`                |
| Admin API [user management](manage-claude-user-management.md): change member roles, remove members, create and withdraw invites                                                                                                                                                                                                 | `write:members`               |
| Admin API [user management](manage-claude-user-management.md): read groups and their members                                                                                                                                                                                                                                    | `read:rbac_groups`            |
| Admin API [user management](manage-claude-user-management.md): create, rename, and delete groups; add and remove group members; assign groups on invite creation                                                                                                                                                                | `write:rbac_groups`           |
| [Spend Limits API](manage-claude-spend-limits-api.md): read members' effective spend limits and increase requests                                                                                                                                                                                                               | `read:spend_limits`           |
| [Spend Limits API](manage-claude-spend-limits-api.md): set or clear per-user spend limits; approve or deny increase requests                                                                                                                                                                                                    | `write:spend_limits`          |
| [Claude Enterprise Analytics API](manage-claude-analytics-api.md): engagement, adoption, cost, and usage reports                                                                                                                                                                                                                | `read:analytics`              |
| [Compliance API Activity Feed](manage-claude-compliance-activity-feed.md): organization-wide activity events                                                                                                                                                                                                                    | `read:compliance_activities`  |
| [Compliance API chat, file, and project endpoints](manage-claude-compliance-content-data.md) and [Compliance API session endpoints](manage-claude-compliance-sessions.md): read chats, files, projects, session transcripts, and [organization users](manage-claude-compliance-org-data.md#list-organization-users) | `read:compliance_user_data`   |
| [Compliance API chat, file, and project endpoints](manage-claude-compliance-content-data.md): delete chats, files, and projects                                                                                                                                                                                                 | `delete:compliance_user_data` |
| [Compliance API organization endpoints](manage-claude-compliance-org-data.md): read organization metadata and effective settings                                                                                                                                                                                                | `read:compliance_org_data`    |
| Admin API [user management](manage-claude-user-management.md) read endpoints and every Compliance API read endpoint, with a single read-only scope (for security-audit integrations; does not include the Spend Limits or Analytics APIs)                                                                                       | `read:org_audit`              |

The Compliance and Analytics APIs must be enabled for your organization before keys with those scopes can be used. See [Set up the Compliance API](manage-claude-compliance-api-access.md#set-up-the-compliance-api) and [Get access to the Claude Enterprise Analytics API](manage-claude-analytics-api.md#get-access-to-the-claude-enterprise-analytics-api).

## Use the key

Pass the key in the `x-api-key` header on every request. See each API's documentation for complete request examples.

A call that exceeds the key's scopes returns `403 Forbidden` with a message listing the scopes the key has and the scopes the endpoint needs.

## Next steps

[Admin API](manage-claude-admin-api.md)

Manage organization members, workspaces, and API keys.

[Spend Limits API](manage-claude-spend-limits-api.md)

Set per-member spend limits and review increase requests for your Claude Enterprise organization.

[Analytics APIs](manage-claude-analytics-api.md)

Report on Claude Code productivity or Claude Enterprise engagement and adoption.

[Compliance API](manage-claude-compliance-api.md)

Audit activity and retrieve or delete user content across your organization.
