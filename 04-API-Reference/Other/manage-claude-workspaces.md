---
title: "Workspaces - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/workspaces"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:38Z"
tags: ["api"]
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fworkspaces)

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

[Admin](manage-claude-admin-api.md)Organization

# Workspaces

Copy page



Organize API keys, manage team access, and control costs with workspaces.

Copy page



Workspaces provide a way to organize your API usage within an organization. Use workspaces to separate different projects, environments, or teams while maintaining centralized billing and administration.

## How workspaces work

Every organization has a **Default Workspace** that cannot be renamed, archived, or deleted. When you create additional workspaces, you can assign members, service accounts, API keys, and resource limits to each one.

Key characteristics:

- **Workspace identifiers** use the `wrkspc_` prefix (for example, `wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ`)
- **Maximum 100 workspaces** per organization by default (archived workspaces don't count); contact your account team if you need more
- **Default Workspace** has a `wrkspc_` ID like any other workspace (returned in the [`anthropic-workspace-id` response header](#identify-the-workspace-behind-an-api-response) and accepted by [Get Workspace](../Admin/beta-organization-workspaces-retrieve.md)), but it doesn't appear in [List Workspaces](../Admin/beta-organization-workspaces-list.md) results, and API keys, usage reports, and cost reports show `null` for its `workspace_id`, as do all-workspaces API keys (an API key's `scope` field tells them apart; for a key bound to the Default Workspace it carries the real ID)
- **API keys** can be scoped to a single workspace. In this case, they can only access resources within that workspace. Some API keys can be granted permissions across multiple workspaces, and provide a [workspace ID header](manage-claude-authentication.md#select-a-workspace) to access resources within that workspace

### Claude Code workspace

When a member of your organization first signs in to [Claude Code](https://platform.claude.com/docs/01-Getting-Started/overview.md) with their Claude Console account, Anthropic automatically creates a **Claude Code** workspace in the organization and adds that member to it. Every subsequent member who signs in to Claude Code is added the same way.

The Claude Code workspace keeps Claude Code traffic separate from your other API workloads:

- Claude Code mints a per-user API key in this workspace at sign-in. You cannot create keys in it manually from the Console.
- A Claude Code key stops working if its owner is removed from the workspace or organization, unlike a workspace key.
- Claude Code usage is rate-limited separately, and admins can cap its share of the organization's limits under [Settings \> Workspaces](usage-limits.md).
- It is the only workspace that supports per-user monthly spend limits.



Archiving the Claude Code workspace disables Claude Code sign-in through Console billing for the whole organization.

## Workspace roles and permissions

Members can have different roles in each workspace, allowing fine-grained access control.

| Role                        | Permissions                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| Workspace User              | Use playground only                                                                             |
| Workspace Limited Developer | Create and manage API keys, use the API. Cannot access session tracing views or download files. |
| Workspace Developer         | Create and manage API keys, use the API                                                         |
| Workspace Admin             | Full control over workspace settings and members                                                |
| Workspace Billing           | View workspace billing information (inherited from organization billing role)                   |

### Role inheritance

- **Organization admins** automatically receive Workspace Admin access to all workspaces
- **Organization billing members** automatically receive Workspace Billing access to all workspaces
- **Organization users and developers** must be explicitly added to each workspace
- **Service accounts** are added to workspaces from the service account's page in [Settings → Service accounts](https://platform.claude.com/settings/service-accounts) or from the workspace's **Service accounts** tab



The Workspace Billing role cannot be manually assigned. It's inherited from having the organization billing role.

## Managing workspaces



Only organization admins can create workspaces. Organization users and developers must be added to workspaces by an admin.

### Using the Console

Create and manage workspaces in the [Claude Console](usage-limits.md).

#### Create a workspace

1.  1

    ### Open workspace settings

    In the Claude Console, go to **Settings \> Workspaces**.

2.  2

    ### Create a workspace

    Click **Create workspace**.

3.  3

    ### Configure the workspace

    Enter a workspace name and select a color for visual identification.

4.  4

    ### Create the workspace

    Click **Create** to finalize.



To switch between workspaces in the Console, use the **Workspaces** selector in the top-left corner.

#### Edit workspace details

To modify a workspace's name or color:

1.  Select the workspace from the list.
2.  Click the ellipsis menu (**...**) and choose **Edit details**.
3.  Update the name or color and save your changes.



The Default Workspace cannot be renamed or deleted.

#### Add members to a workspace

1.  Navigate to the workspace's **Members** tab.
2.  Click **Add to Workspace**.
3.  Select an organization member and assign them a [workspace role](#workspace-roles-and-permissions).
4.  Confirm the addition.

To remove a member, click the trash icon next to their name.



Organization admins and billing members cannot be removed from workspaces while they hold those organization roles.

#### Set workspace limits

Each workspace's settings split these across two tabs:

- **Rate limits:** On the **Rate limits** tab, set limits per model tier for requests per minute, input tokens, or output tokens
- **Spend limits:** On the **Spend limits** tab, cap monthly spending and configure alerts when spending reaches certain thresholds

#### Archive a workspace

To archive a workspace, click the ellipsis menu (**...**) and select **Archive**. Archiving:

- Preserves historical data for reporting
- Deactivates the workspace and archives every API key created for it
- Cannot be undone



Archiving a workspace archives every API key created for that workspace within seconds (they remain listed in the Admin API as archived), and multi-workspace keys can no longer act in it. This action cannot be undone. If you archive the [Claude Code workspace](#claude-code-workspace), members of your organization can no longer sign in to Claude Code through Console billing.

### Using the Admin API

Programmatically manage workspaces using the [Admin API](manage-claude-admin-api.md).



Admin API endpoints accept an [Admin API key](manage-claude-admin-api-keys.md), an `org:admin` OAuth token, or a personal or service account key that isn't scoped to a specific workspace. Workspace keys don't work there. See [Authentication](manage-claude-admin-api.md#authentication).

The following SDK and CLI examples construct the default client, which reads the Admin API key from the `ANTHROPIC_API_KEY` environment variable; the SDKs expose these endpoints under `client.beta.organization.workspaces`. SDK list methods fetch further pages on demand, so `limit` sets the page size; the PHP, Ruby, and curl examples return one page.

Create a workspace:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

workspace = client.beta.organization.workspaces.create(name="Production")

print(f"id: {workspace.id}")
print(f"name: {workspace.name}")
```

List workspaces:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

workspaces = client.beta.organization.workspaces.list(limit=10, include_archived=False)

for workspace in workspaces:
    print(f"{workspace.id}: {workspace.name}")
```

Archive a workspace:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

workspace = client.beta.organization.workspaces.archive(
    "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
)

print(f"id: {workspace.id}")
print(f"archived_at: {workspace.archived_at}")
```

For complete parameter details and response schemas, see the [Workspaces API reference](../Admin/beta-organization-workspaces-retrieve.md).

### Managing workspace members

Add a member to a workspace:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

member = client.beta.organization.workspaces.members.add(
    "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
    user_id="user_01XyDMpzjS89pFZXqSFUBDr6",
    workspace_role="workspace_developer",
)

print(f"user_id: {member.user_id}")
print(f"workspace_role: {member.workspace_role}")
```

Update a member's role:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

member = client.beta.organization.workspaces.members.update(
    "user_01XyDMpzjS89pFZXqSFUBDr6",
    workspace_id="wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
    workspace_role="workspace_admin",
)

print(f"user_id: {member.user_id}")
print(f"workspace_role: {member.workspace_role}")
```

Remove a member from a workspace:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

removed_member = client.beta.organization.workspaces.members.remove(
    "user_01XyDMpzjS89pFZXqSFUBDr6",
    workspace_id="wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
)

print(f"user_id: {removed_member.user_id}")
```

For complete parameter details, see the [Workspace Members API reference](../Admin/beta-organization-workspaces-members-retrieve.md).

## API keys and resource scoping

Every request runs in exactly one workspace and can only access resources within that workspace. Which workspace depends on the [key type](manage-claude-authentication.md#key-types):

- A **workspace key** (a legacy key without an owner) belongs to the workspace it was created in and always runs there.
- A **personal key** or **service account key** acts as its user or service account. A single-workspace key always runs in the workspace chosen when it was created. A multi-workspace key runs in the workspace named by each request's `anthropic-workspace-id` header. Accounts must have access to the workspace to use it.

Resources scoped to workspaces include:

- **Files** created through the [Files API](../Guides/build-with-claude-files.md)
- **Message Batches** created through the [Batch API](../Guides/build-with-claude-batch-processing.md)
- **Skills** created through the [Skills API](../Guides/build-with-claude-skills-guide.md)

Some resources are managed differently:

- **[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)** are managed with a `workspace:manage_tunnels` OAuth token obtained through [Workload Identity Federation](manage-claude-workload-identity-federation.md), not an API key. Tunnels are created in a workspace, and the Console **MCP tunnels** list and the Managed Agent server picker show tunnels in the current workspace only; the cap of 10 active tunnels applies organization-wide. Tunnel management requires a role with tunnel management permissions; organization developers can view but not change them.
- **Workspaces** themselves and **organization members** are managed at the organization level through the [Admin API](manage-claude-admin-api.md), using an Admin API key, an `org:admin` OAuth token, or a personal or service account key that isn't scoped to a specific workspace.

To look up your organization's workspace IDs, call the [List Workspaces](../Admin/beta-organization-workspaces-list.md) endpoint or find them in the [Claude Console](usage-limits.md).



[Prompt caches](../Guides/build-with-claude-prompt-caching.md) are also isolated per workspace on the Claude API, [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md), and [Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md). On Amazon Bedrock and Google Cloud, prompt caches are isolated per organization.

## Identify the workspace behind an API response

Claude API responses include an `anthropic-workspace-id` header alongside the `request-id` and `anthropic-organization-id` [response headers](../Endpoints/overview.md#response-headers). Its value is the `wrkspc_`-prefixed ID of the workspace that the request's API key or access token resolved to, including when that workspace is the Default Workspace. For example, a successful response includes headers like these:

```python
HTTP/1.1 200 OK
request-id: req_018EeWyXxfu5pfWkrYcMdjWG
anthropic-organization-id: 0d0e7a3b-52f1-4c7e-9a51-3f6f2f7c1b9e
anthropic-workspace-id: wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ
```



The header is absent when the credential doesn't resolve to a workspace (for example, on Admin API requests) or when the request fails before authentication completes, such as a 401 error.

The following examples send a Messages API request and print the workspace ID from the response headers:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

response = client.messages.with_raw_response.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
workspace_id = response.headers.get("anthropic-workspace-id")
print(f"Workspace ID: {workspace_id}")
```

Output



``` block
Workspace ID: wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ
```

The same accessors read the header from other Claude API endpoints too, including the [Claude Managed Agents](managed-agents-overview.md) APIs. For example, read `anthropic-workspace-id` from the response that [creates a session](managed-agents-sessions.md) to record which workspace the session belongs to.

With the workspace ID from a response, you can:

- Confirm which workspace's usage, cost, and [rate limits](../Endpoints/rate-limits.md) the request counted toward
- Match it against the `workspace_id` field in [Usage and Cost API](manage-claude-usage-cost-api.md) reports and on [Admin API](manage-claude-admin-api.md) objects such as API keys (both report `null` for the Default Workspace, as API keys also do for all-workspaces keys; an API key's `scope` field tells the two apart and, for a key bound to one workspace, carries that workspace's real ID)
- Check whether it's your Default Workspace's ID by passing it to [Get Workspace](../Admin/beta-organization-workspaces-retrieve.md) with an [Admin API key](manage-claude-admin-api-keys.md): the Default Workspace comes back with `"name": "Default"`, even though [List Workspaces](../Admin/beta-organization-workspaces-list.md) omits it
- Open that workspace in the [Console](usage-limits.md) to find the request's resources, such as sessions, files, message batches, and skills

## Workspace limits

You can set custom spend and rate limits for each workspace to protect against overuse and ensure fair resource distribution.

### Setting workspace limits

You can set workspace limits lower than (but not higher than) your organization's limits:

- **Spend limits:** Cap monthly spending for a workspace. Set these on the workspace's **Spend limits** settings tab in the [Claude Console](usage-limits.md).
- **Rate limits:** Limit requests per minute, input tokens per minute, or output tokens per minute. Set these on the workspace's **Rate limits** settings tab in the [Claude Console](usage-limits.md).



- You cannot set limits on the Default Workspace
- If not set, workspace limits match the organization's limits
- Organization-wide limits always apply, even if workspace limits add up to more

For detailed information on rate limits and how they work, see [Rate limits](../Endpoints/rate-limits.md). You can also read your current organization and workspace rate limits programmatically with the [Rate Limits API](manage-claude-rate-limits-api.md).

## Usage and cost tracking

Track usage and costs by workspace using the [Usage and Cost API](manage-claude-usage-cost-api.md):

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

## Common use cases

### Environment separation

Create separate workspaces for development, staging, and production:

| Workspace   | Purpose                                            |
|-------------|----------------------------------------------------|
| Development | Testing and experimentation with lower rate limits |
| Staging     | Pre-production testing with production-like limits |
| Production  | Live traffic with full rate limits and monitoring  |

### Team or department isolation

Assign workspaces to different teams for cost allocation and access control:

- **Engineering team** with developer access
- **Data science team** with their own API keys
- **Support team** with limited access for customer tools

### Project-based organization

Create workspaces for specific projects or products to track usage and costs separately.

## Best practices

1.  1

    ### Plan your workspace structure

    Consider how you'll organize workspaces before creating them. Think about billing, access control, and usage tracking needs.

2.  2

    ### Use meaningful names

    Name workspaces clearly to indicate their purpose (for example, "Production - Customer Chatbot" or "Dev - Internal Tools").

3.  3

    ### Set appropriate limits

    Configure spend and rate limits to prevent unexpected costs and ensure fair resource distribution.

4.  4

    ### Audit access regularly

    Review workspace membership periodically to ensure only appropriate users have access.

5.  5

    ### Monitor usage

    Use the [Usage and Cost API](manage-claude-usage-cost-api.md) to track workspace-level consumption.

## FAQ

### What's the Default Workspace?

Every organization has a "Default Workspace" that cannot be renamed, archived, or deleted. Like every workspace, it has a `wrkspc_` ID: the API returns it in the [`anthropic-workspace-id` response header](#identify-the-workspace-behind-an-api-response), and you can pass it to [Get Workspace](../Admin/beta-organization-workspaces-retrieve.md) and [Update Workspace](../Admin/beta-organization-workspaces-update.md). It has no member list of its own, because access to it follows each member's organization role. It doesn't appear in [List Workspaces](../Admin/beta-organization-workspaces-list.md) results, and API keys, usage reports, and cost reports that belong to it show `null` for `workspace_id`, as do all-workspaces API keys; an API key's `scope` field tells the two apart and, for a key that belongs to the Default Workspace, carries its real ID.

### What's the Claude Code workspace?

Anthropic creates the Claude Code workspace automatically the first time a member of your organization signs in to Claude Code with their Console account. It isolates Claude Code's API keys, usage, and rate limits from your other workloads. See [Claude Code workspace](#claude-code-workspace) for details.

### Are there limits on workspaces?

Yes. Each organization can have up to 100 workspaces by default, and archived workspaces don't count toward this limit. If you need more, contact your account team.

### How do organization roles affect workspace access?

Organization admins automatically get the Workspace Admin role in all workspaces. Organization billing members automatically get the Workspace Billing role. Organization users and developers must be manually added to each workspace.

### Which roles can be assigned in workspaces?

Organization users and developers can be assigned Workspace Admin, Workspace Developer, Workspace Limited Developer, or Workspace User roles. The Workspace Billing role cannot be manually assigned; it's inherited from having the organization `billing` role.

### Can organization admin or billing members' workspace roles be changed?

Organization admins and billing members cannot have their workspace roles changed or be removed from workspaces while they hold those organization roles (with one exception: billing members can be upgraded to a Workspace Admin role). For everyone else covered by this constraint, change their organization role first to change their workspace access.

### What happens to workspace access when organization roles change?

If an organization admin or billing member is demoted to user or developer, they lose access to all workspaces except ones where they were manually assigned roles. When users are promoted to admin or billing roles, they gain automatic access to all workspaces.

### What happens to API keys when a user is removed from a workspace?

Behavior depends on the [key type](manage-claude-authentication.md#key-types).

A personal or service account key stops working in a workspace shortly after its user or service account is removed from it. A service account key keeps working even if the user who created it is removed. Workspace API keys continue to work. In the [Claude Code workspace](#claude-code-workspace), each key is bound to the member who created it and stops working when that member is removed.

Personal keys are archived when their user is removed from the organization. If the user is re-invited, they need to create new keys; archived keys are not restored.

## See also

- [Admin API](manage-claude-admin-api.md)
- [Admin API reference](../Admin/http-beta-organization.md)
- [Rate limits](../Endpoints/rate-limits.md)
- [Usage and Cost API](manage-claude-usage-cost-api.md)
