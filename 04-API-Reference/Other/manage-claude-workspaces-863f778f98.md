---
title: "Workspaces - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/workspaces"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:47Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


Organization

[Admin API](/docs/en/manage-claude/admin-api)[User management (beta)](/docs/en/manage-claude/user-management)[Workspaces](/docs/en/manage-claude/workspaces)

Authentication

[Overview](/docs/en/manage-claude/authentication)[Create an Admin API key](/docs/en/manage-claude/admin-api-keys)[Workload Identity Federation](/docs/en/manage-claude/workload-identity-federation)[Manage WIF via API](/docs/en/manage-claude/wif-admin-api)[WIF reference](/docs/en/manage-claude/wif-reference)

Identity providers

Monitoring

[Usage and Cost API](/docs/en/manage-claude/usage-cost-api)[Rate Limits API](/docs/en/manage-claude/rate-limits-api)[Analytics APIs](/docs/en/manage-claude/analytics-api)[Claude Code Analytics API](/docs/en/manage-claude/claude-code-analytics-api)[Spend Limits API](/docs/en/manage-claude/spend-limits-api)

Data & compliance

[Data residency](/docs/en/manage-claude/data-residency)[API and data retention](/docs/en/manage-claude/api-and-data-retention)[Access Transparency](/docs/en/manage-claude/access-transparency)

Encryption keys

Compliance API

[Overview](/docs/en/manage-claude/compliance-api)[Set up the Compliance API](/docs/en/manage-claude/compliance-api-access)[Activity Feed](/docs/en/manage-claude/compliance-activity-feed)[Chats, files, and projects](/docs/en/manage-claude/compliance-content-data)[Organizations, users, roles, groups, and settings](/docs/en/manage-claude/compliance-org-data)[Design your integration](/docs/en/manage-claude/compliance-integration-patterns)[Errors](/docs/en/manage-claude/compliance-errors)[FAQ](/docs/en/manage-claude/compliance-faq)

[](/login)




Admin

Workspaces

Admin/Organization

# Workspaces




Organize API keys, manage team access, and control costs with workspaces.




Workspaces provide a way to organize your API usage within an organization. Use workspaces to separate different projects, environments, or teams while maintaining centralized billing and administration.




How workspaces work

Every organization has a **Default Workspace** that cannot be renamed, archived, or deleted. When you create additional workspaces, you can assign API keys, members, and resource limits to each one.

Key characteristics:

- **Workspace identifiers** use the `wrkspc_` prefix (for example, `wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ`)
- **Maximum 100 workspaces** per organization (archived workspaces don't count)
- **Default Workspace** has no ID and doesn't appear in list endpoints
- **API keys** are scoped to a single workspace and can only access resources within that workspace




Claude Code workspace

When a member of your organization first signs in to [Claude Code](https://code.claude.com/docs/en/overview) with their Claude Console account, Anthropic automatically creates a **Claude Code** workspace in the organization and adds that member to it. Every subsequent member who signs in to Claude Code is added the same way.

The Claude Code workspace keeps Claude Code traffic separate from your other API workloads:

- Claude Code mints a per-user API key in this workspace at sign-in. You cannot create keys in it manually from the Console.
- A Claude Code key stops working if its owner is removed from the workspace or organization, unlike standard workspace keys.
- Claude Code usage is rate-limited separately, and admins can cap its share of the organization's limits under [Settings \> Workspaces](/settings/workspaces).
- It is the only workspace that supports per-user monthly spend limits.



Archiving the Claude Code workspace disables Claude Code sign-in through Console billing for the whole organization.




Workspace roles and permissions

Members can have different roles in each workspace, allowing fine-grained access control.

| Role                        | Permissions                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| Workspace User              | Use the Anthropic Workbench only                                                                |
| Workspace Limited Developer | Create and manage API keys, use the API. Cannot access session tracing views or download files. |
| Workspace Developer         | Create and manage API keys, use the API                                                         |
| Workspace Admin             | Full control over workspace settings and members                                                |
| Workspace Billing           | View workspace billing information (inherited from organization billing role)                   |




Role inheritance

- **Organization admins** automatically receive Workspace Admin access to all workspaces
- **Organization billing members** automatically receive Workspace Billing access to all workspaces
- **Organization users and developers** must be explicitly added to each workspace



The Workspace Billing role cannot be manually assigned. It's inherited from having the organization billing role.




Managing workspaces



Only organization admins can create workspaces. Organization users and developers must be added to workspaces by an admin.




Using the Console

Create and manage workspaces in the [Claude Console](/settings/workspaces).




Create a workspace

1.  1

    Open workspace settings

    In the Claude Console, go to **Settings \> Workspaces**.

2.  2

    Create a workspace

    Click **Create workspace**.

3.  3

    Configure the workspace

    Enter a workspace name and select a color for visual identification.

4.  4

    Create the workspace

    Click **Create** to finalize.



To switch between workspaces in the Console, use the **Workspaces** selector in the top-left corner.




Edit workspace details

To modify a workspace's name or color:

1.  Select the workspace from the list.
2.  Click the ellipsis menu (**...**) and choose **Edit details**.
3.  Update the name or color and save your changes.



The Default Workspace cannot be renamed or deleted.




Add members to a workspace

1.  Navigate to the workspace's **Members** tab.
2.  Click **Add to Workspace**.
3.  Select an organization member and assign them a [workspace role](#workspace-roles-and-permissions).
4.  Confirm the addition.

To remove a member, click the trash icon next to their name.



Organization admins and billing members cannot be removed from workspaces while they hold those organization roles.




Set workspace limits

In the **Limits** tab, you can configure:

- **Rate limits:** Set limits per model tier for requests per minute, input tokens, or output tokens
- **Spend notifications:** Configure alerts when spending reaches certain thresholds




Archive a workspace

To archive a workspace, click the ellipsis menu (**...**) and select **Archive**. Archiving:

- Preserves historical data for reporting
- Deactivates the workspace and all associated API keys
- Cannot be undone



Archiving a workspace immediately revokes all API keys in that workspace. This action cannot be undone. If you archive the [Claude Code workspace](#claude-code-workspace), members of your organization can no longer sign in to Claude Code through Console billing.




Using the Admin API

Programmatically manage workspaces using the [Admin API](/docs/en/manage-claude/admin-api).



Admin API endpoints require an Admin API key (starting with `sk-ant-admin...`) that differs from standard API keys. See [Create an Admin API key](/docs/en/manage-claude/admin-api-keys) for how to provision one.

cURL



```python
# Create a workspace
curl -X POST "https://api.anthropic.com/v1/organizations/workspaces" \
  -H "anthropic-version: 2023-06-01" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  -d '{"name": "Production"}'

# List workspaces
curl "https://api.anthropic.com/v1/organizations/workspaces?limit=10&include_archived=false" \
  -H "anthropic-version: 2023-06-01" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"

# Archive a workspace
curl -X POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/archive" \
  -H "anthropic-version: 2023-06-01" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

For complete parameter details and response schemas, see the [Workspaces API reference](/docs/en/api/admin-api/workspaces/get-workspace).




Managing workspace members

Add, update, or remove members from a workspace:

cURL



```python
# Add a member to a workspace
curl -X POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members" \
  -H "anthropic-version: 2023-06-01" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  -d '{
    "user_id": "user_xxx",
    "workspace_role": "workspace_developer"
  }'

# Update a member's role
curl -X POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members/{user_id}" \
  -H "anthropic-version: 2023-06-01" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  -d '{"workspace_role": "workspace_admin"}'

# Remove a member from a workspace
curl -X DELETE "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members/{user_id}" \
  -H "anthropic-version: 2023-06-01" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

For complete parameter details, see the [Workspace Members API reference](/docs/en/api/admin-api/workspace_members/get-workspace-member).




API keys and resource scoping

API keys are scoped to a specific workspace. When you create an API key in a workspace, it can only access resources within that workspace.

Resources scoped to workspaces include:

- **Files** created through the [Files API](/docs/en/build-with-claude/files)
- **Message Batches** created through the [Batch API](/docs/en/build-with-claude/batch-processing)
- **Skills** created through the [Skills API](/docs/en/build-with-claude/skills-guide)

Some resources cannot be managed with a workspace API key:

- **[MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview)** are managed with a `workspace:manage_tunnels` OAuth token obtained through [Workload Identity Federation](/docs/en/manage-claude/workload-identity-federation), not a workspace API key. Tunnels are created in a workspace, and the Console **MCP tunnels** list and the Managed Agent server picker show tunnels in the current workspace only; the cap of 10 active tunnels applies organization-wide. Tunnel management requires a role with tunnel management permissions; organization developers can view but not change them.
- **Workspaces** themselves and **organization members** are managed at the organization level through the [Admin API](/docs/en/manage-claude/admin-api), which requires an Admin API key.



[Prompt caches](/docs/en/build-with-claude/prompt-caching) are also isolated per workspace on the Claude API, [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws), and [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry). On Amazon Bedrock and Google Cloud, prompt caches are isolated per organization.



To retrieve your organization's workspace IDs, use the [List Workspaces](/docs/en/api/admin-api/workspaces/list-workspaces) endpoint, or find them in the [Claude Console](/settings/workspaces).




Workspace limits

You can set custom spend and rate limits for each workspace to protect against overuse and ensure fair resource distribution.




Setting workspace limits

You can set workspace limits lower than (but not higher than) your organization's limits:

- **Spend limits:** Cap monthly spending for a workspace
- **Rate limits:** Limit requests per minute, input tokens per minute, or output tokens per minute



- You cannot set limits on the Default Workspace
- If not set, workspace limits match the organization's limits
- Organization-wide limits always apply, even if workspace limits add up to more

For detailed information on rate limits and how they work, see [Rate limits](/docs/en/api/rate-limits). You can also read your current organization and workspace rate limits programmatically with the [Rate Limits API](/docs/en/manage-claude/rate-limits-api).




Usage and cost tracking

Track usage and costs by workspace using the [Usage and Cost API](/docs/en/manage-claude/usage-cost-api):

cURL



```python
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-01T00:00:00Z&\
ending_at=2025-01-08T00:00:00Z&\
workspace_ids[]=wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ&\
group_by[]=workspace_id&\
bucket_width=1d" \
  -H "anthropic-version: 2023-06-01" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

Usage and costs attributed to the Default Workspace have a `null` value for `workspace_id`.




Common use cases




Environment separation

Create separate workspaces for development, staging, and production:

| Workspace   | Purpose                                            |
|-------------|----------------------------------------------------|
| Development | Testing and experimentation with lower rate limits |
| Staging     | Pre-production testing with production-like limits |
| Production  | Live traffic with full rate limits and monitoring  |




Team or department isolation

Assign workspaces to different teams for cost allocation and access control:

- **Engineering team** with developer access
- **Data science team** with their own API keys
- **Support team** with limited access for customer tools




Project-based organization

Create workspaces for specific projects or products to track usage and costs separately.




Best practices

1.  1

    Plan your workspace structure

    Consider how you'll organize workspaces before creating them. Think about billing, access control, and usage tracking needs.

2.  2

    Use meaningful names

    Name workspaces clearly to indicate their purpose (for example, "Production - Customer Chatbot", "Dev - Internal Tools").

3.  3

    Set appropriate limits

    Configure spend and rate limits to prevent unexpected costs and ensure fair resource distribution.

4.  4

    Audit access regularly

    Review workspace membership periodically to ensure only appropriate users have access.

5.  5

    Monitor usage

    Use the [Usage and Cost API](/docs/en/manage-claude/usage-cost-api) to track workspace-level consumption.





### What's the Default Workspace?

### What's the Claude Code workspace?

### Are there limits on workspaces?

### How do organization roles affect workspace access?

### Which roles can be assigned in workspaces?

### Can organization admin or billing members' workspace roles be changed?

### What happens to workspace access when organization roles change?

### What happens to API keys when a user is removed from a workspace?




See also

- [Admin API](/docs/en/manage-claude/admin-api)
- [Admin API reference](/docs/en/api/admin)
- [Rate limits](/docs/en/api/rate-limits)
- [Usage and Cost API](/docs/en/manage-claude/usage-cost-api)
