---
title: "Workspaces - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/workspaces"
category: "04-API-Reference/Other"
fetched_at: "2026-11-05T06:36:45Z"
tags: ["api"]
---

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

- **Workspace identifiers** use the `wrkspc_` prefix (for example, `wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ`).
- **Maximum 100 workspaces** for each organization by default (archived workspaces don’t count). Contact your account team if you need more.
- **Default Workspace** has a `wrkspc_` ID like any other workspace (returned in the [`anthropic-workspace-id` response header](#identify-the-workspace-behind-an-api-response) and accepted by [Get Workspace](../Endpoints/organization-workspaces-retrieve.md)), but it appears in [List Workspaces](../Endpoints/organization-workspaces-list.md) results only when you pass `include_default=true`. The [Usage and Cost Analytics API](manage-claude-usage-cost-analytics-api.md) reports its usage and cost under that ID, whereas the legacy [Usage and Cost API](manage-claude-usage-cost-api.md) reports show `null` for its `workspace_id` (an API key’s `scope` field carries the real ID for a key bound to the Default Workspace).
- **API keys** can be scoped to a single workspace. In this case, they can only access resources within that workspace. Other API keys aren’t scoped to a workspace. With one of these keys, send a [workspace ID header](manage-claude-authentication.md#select-a-workspace) on each request to choose the workspace. The key’s user or service account must have access to that workspace.

### Claude Code workspace

When a member of your organization first signs in to [Claude Code](../../01-Getting-Started/overview.md) with their Claude Console account, Anthropic automatically creates a **Claude Code** workspace in the organization and adds that member to it. Every subsequent member who signs in to Claude Code is added the same way.

The Claude Code workspace keeps Claude Code traffic separate from your other API workloads:

- Claude Code mints a per-user API key in this workspace at sign-in. You cannot create keys in it manually from the Console.
- A Claude Code key stops working if its owner is removed from the workspace or organization, unlike a workspace key.
- Claude Code usage is rate-limited separately, and admins can cap its share of the organization’s limits under [Rate limits in the Claude Console](playground.md).
- It is the only workspace that supports per-user monthly spend limits.



Archiving the Claude Code workspace disables Claude Code sign-in through Console billing for the whole organization.

## Workspace roles and permissions

Members can have different roles in each workspace, allowing fine-grained access control.

[TABLE]

### Role inheritance

- **Organization admins** automatically receive Workspace Admin access to all workspaces.
- **Organization billing members** automatically receive Workspace Billing access to all workspaces.
- **Organization users and developers** must be explicitly added to each workspace.
- **Service accounts** are added to workspaces on the [Service accounts](https://platform.claude.com/settings/service-accounts) page (`platform.claude.com/settings/service-accounts`) in the Claude Console: select **Add to workspace** in the account’s menu or on its own page. To see the accounts in one workspace, filter the list by workspace.



The Workspace Billing role cannot be manually assigned. It’s inherited from having the organization billing role.

## Managing workspaces



Only organization admins can create workspaces. Organization users and developers must be added to workspaces by an admin.

### Using the Console

Create and manage workspaces on the [Workspaces](playground.md) page in the Claude Console.

#### Create a workspace

1.  1

    ### Open workspace settings

    In the Claude Console, go to the [Workspaces](playground.md) page (`platform.claude.com/settings/workspaces`).

2.  2

    ### Open the Create workspace page

    Click **Create workspace** to open the [Create workspace](https://platform.claude.com/settings/workspaces/new) page (`platform.claude.com/settings/workspaces/new`) in the Console.

3.  3

    ### Configure the workspace

    Enter a workspace name and select a color for visual identification.

4.  4

    ### Create the workspace

    Click **Create workspace** to finalize.



To switch between workspaces in the Console, open a page that belongs to a workspace, such as [Files](playground.md) (`platform.claude.com/files`), and use the workspace picker in the sidebar.

#### Edit workspace details

To modify a workspace’s name or color:

1.  Select the workspace from the list.
2.  Open the **More actions** menu (three dots) and select **Edit details**.
3.  Update the name or color and save your changes.



The Default Workspace cannot be renamed or deleted.

#### Add members to a workspace

1.  In the Claude Console, go to the [Members](playground.md) page (`platform.claude.com/settings/members`).
2.  Click **Add to workspace**.
3.  Select the workspace, the organization member to add, and their [workspace role](#workspace-roles-and-permissions).
4.  Click **Add to workspace** to confirm.

#### Remove members from a workspace

1.  On the [Members](playground.md) page in the Claude Console, select the workspace from the **Workspace** dropdown menu. If it shows **All**, **Remove member** removes the member from your organization instead.
2.  At the end of the member’s row, open the **More actions** menu (three dots) and select **Remove member**.
3.  Click **Remove** to confirm.



Organization admins and billing members cannot be removed from workspaces while they hold those organization roles.

#### Set workspace limits

You set a workspace’s rate limits and spend limits in different places:

- **Rate limits:** Under [Rate limits in the Claude Console](playground.md), select the workspace from the **Workspace** dropdown menu and click **Edit** next to a model to set limits for requests per minute, input tokens, or output tokens.
- **Spend limits:** On the [Workspaces](playground.md) page in the Claude Console, select the workspace. In the panel that opens, click **Spend limits** to cap monthly spending and configure alerts when spending reaches certain thresholds.

#### Archive a workspace

To archive a workspace, open its **More actions** menu (three dots) and select **Archive workspace**. Archiving:

- Preserves historical data for reporting
- Deactivates the workspace and archives every API key created for it
- Cannot be undone



Archiving a workspace archives every API key created for that workspace within seconds (they remain listed in the Admin API as archived), and keys that aren’t scoped to a workspace can no longer act in it. This action cannot be undone. If you archive the [Claude Code workspace](#claude-code-workspace), members of your organization can no longer sign in to Claude Code through Console billing.

### Using the Admin API

Programmatically manage workspaces using the [Admin API](manage-claude-admin-api.md).



Admin API endpoints accept an [Admin API key](manage-claude-admin-api-keys.md), an `org:admin` OAuth token, or a personal or service account key that isn’t scoped to a specific workspace. Workspace keys don’t work there. See [Authentication](manage-claude-admin-api.md#authentication).

The following SDK and CLI examples construct the default client, which reads the Admin API key from the `ANTHROPIC_API_KEY` environment variable; the SDK exposes these endpoints under `client.organization.workspaces`. SDK list methods fetch further pages on demand, so `limit` sets the page size; the PHP, Ruby, and curl examples return one page.

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

Python



```python
client = anthropic.Anthropic()

workspace = client.organization.workspaces.create(name="Production")

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

Python



```python
client = anthropic.Anthropic()

workspaces = client.organization.workspaces.list(limit=10, include_archived=False)

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

Python



```python
client = anthropic.Anthropic()

workspace = client.organization.workspaces.archive("wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ")

print(f"id: {workspace.id}")
print(f"archived_at: {workspace.archived_at}")
```

For complete parameter details and response schemas, see the [Workspaces API reference](../Endpoints/organization-workspaces-retrieve.md).

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

Python



```python
client = anthropic.Anthropic()

member = client.organization.workspaces.members.add(
    "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
    user_id="user_01WxYzAbCdEfGhJkMnPqRsTu",
    workspace_role="workspace_developer",
)

print(f"user_id: {member.user_id}")
print(f"workspace_role: {member.workspace_role}")
```

Update a member’s role:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

member = client.organization.workspaces.members.update(
    "user_01WxYzAbCdEfGhJkMnPqRsTu",
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

Python



```python
client = anthropic.Anthropic()

removed_member = client.organization.workspaces.members.remove(
    "user_01WxYzAbCdEfGhJkMnPqRsTu",
    workspace_id="wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
)

print(f"user_id: {removed_member.user_id}")
```

For complete parameter details, see the [Workspace Members API reference](../Endpoints/organization-workspaces-members-retrieve.md).

## API keys and resource scoping

Every request runs in exactly one workspace and can only access resources within that workspace. Which workspace depends on the [key type](manage-claude-authentication.md#key-types):

- A **workspace key** (a legacy key without an owner) belongs to the workspace it was created in and always runs there.
- A **personal key** or **service account key** acts as its user or service account. A single-workspace key always runs in the workspace chosen when it was created. A key that isn’t scoped to a workspace runs in the workspace named by each request’s `anthropic-workspace-id` header. Accounts must have access to the workspace to use it.

Resources scoped to workspaces include:

- **Files** created through the [Files API](../Guides/build-with-claude-files.md)
- **Message Batches** created through the [Batch API](../Guides/build-with-claude-batch-processing.md)
- **Skills** created through the [Skills API](../Guides/build-with-claude-skills-guide.md)

Some resources are managed differently:

- **[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)** are managed with a `workspace:manage_tunnels` OAuth token obtained through [Workload Identity Federation](manage-claude-workload-identity-federation.md), not an API key. Tunnels are created in a workspace, and the Console **MCP tunnels** list and the Managed Agent server picker show tunnels in the current workspace only; the cap of 10 active tunnels applies organization-wide. Tunnel management requires a role with tunnel management permissions; organization developers can view but not change them.
- **Workspaces** themselves and **organization members** are managed at the organization level through the [Admin API](manage-claude-admin-api.md), using an Admin API key, an `org:admin` OAuth token, or a personal or service account key that isn’t scoped to a specific workspace.

To look up your organization’s workspace IDs, call the [List Workspaces](../Endpoints/organization-workspaces-list.md) endpoint (pass `include_default=true` to include the Default Workspace) or find them on the [Workspaces](playground.md) page in the Claude Console.



[Prompt caches](../Guides/build-with-claude-prompt-caching.md) are also isolated by workspace on the Claude API, [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md), and [Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md). On Claude Models on Google Cloud (Google managed) and Amazon Bedrock, prompt caches are isolated by organization.

## Identify the workspace behind an API response

Claude API responses include an `anthropic-workspace-id` header alongside the `request-id` and `anthropic-organization-id` [response headers](../Endpoints/overview.md#response-headers). Its value is the `wrkspc_`-prefixed ID of the workspace that the request’s API key or access token resolved to, including when that workspace is the Default Workspace. For example, a successful response includes headers like these:

```python
HTTP/1.1 200 OK
request-id: req_018EeWyXxfu5pfWkrYcMdjWG
anthropic-organization-id: 0d0e7a3b-52f1-4c7e-9a51-3f6f2f7c1b9e
anthropic-workspace-id: wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ
```



The header is absent when the credential doesn’t resolve to a workspace (for example, on Admin API requests) or when the request fails before authentication completes, such as a 401 error.

The following examples send a Messages API request and read the workspace ID from the response headers:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python

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

- Confirm which workspace’s usage, cost, and [rate limits](../Endpoints/rate-limits.md) the request counted toward
- Match it against the `workspace_id` field in [Usage and Cost Analytics API](manage-claude-usage-cost-analytics-api.md) rows, which carry this same ID for the Default Workspace, and against the `scope` field of API keys in the [Admin API](manage-claude-admin-api.md), which carries the real ID of the workspace a key is bound to, including the Default Workspace
- Check whether it’s your Default Workspace’s ID by passing it to [Get Workspace](../Endpoints/organization-workspaces-retrieve.md) with an [Admin API key](manage-claude-admin-api-keys.md): the Default Workspace comes back with `"name": "Default"`, even though [List Workspaces](../Endpoints/organization-workspaces-list.md) omits it unless you pass `include_default=true`
- Open that workspace in the [Console](playground.md) to find the request’s resources, such as sessions, files, message batches, and skills

## Workspace limits

You can set custom spend and rate limits for each workspace to protect against overuse and ensure fair resource distribution.

### Setting workspace limits

You can set workspace limits lower than (but not higher than) your organization’s limits:

- **Spend limits:** Cap monthly spending for a workspace. To set these, go to the [Workspaces](playground.md) page (`platform.claude.com/settings/workspaces`) in the Claude Console and select the workspace. In the panel that opens, click **Spend limits**.
- **Rate limits:** Limit requests per minute, input tokens per minute, or output tokens per minute. To set these, go to [Rate limits in the Claude Console](playground.md), select the workspace from the **Workspace** dropdown menu, and click **Edit** next to a model.



- You cannot set spend limits on the Default Workspace.
- If not set, workspace limits match the organization’s limits.
- Organization-wide limits always apply, even if workspace limits add up to more.

For detailed information on rate limits and how they work, see [Rate limits](../Endpoints/rate-limits.md). You can also read your current organization and workspace rate limits and set workspace rate limits programmatically with the [Rate Limits API](manage-claude-rate-limits-api.md), which stores a value above the organization’s limit but still enforces the lower of the two.

## Usage and cost tracking

Track usage and costs by workspace using the [Usage and Cost Analytics API](manage-claude-usage-cost-analytics-api.md):

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

rows = client.beta.organization.analytics.usage.list(
    starting_at="2026-09-01T00:00:00Z",
    ending_at="2026-09-08T00:00:00Z",
    time_bucket_width="1d",
    workspace_ids=["wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"],
    group_by=["workspace_id"],
)

for row in rows:
    print(f"{row.starting_at} {row.group.workspace_id}: {row.usage.total_tokens}")
```

Usage and costs in the Default Workspace are reported under the Default Workspace’s own ID.

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

    Consider how you’ll organize workspaces before creating them. Think about billing, access control, and usage tracking needs.

2.  2

    ### Use meaningful names

    Name workspaces clearly to indicate their purpose (for example, “Production - Customer Chatbot” or “Dev - Internal Tools”).

3.  3

    ### Set appropriate limits

    Configure spend and rate limits to prevent unexpected costs and ensure fair resource distribution.

4.  4

    ### Audit access regularly

    Review workspace membership periodically to ensure only appropriate users have access.

5.  5

    ### Monitor usage

    Use the [Usage and Cost Analytics API](manage-claude-usage-cost-analytics-api.md) to track workspace-level consumption.

## FAQ

### What’s the Default Workspace?

Every organization has a “Default Workspace” that cannot be renamed, archived, or deleted. Like every workspace, it has a `wrkspc_` ID: the API returns it in the [`anthropic-workspace-id` response header](#identify-the-workspace-behind-an-api-response), and you can pass it to [Get Workspace](../Endpoints/organization-workspaces-retrieve.md) and [Update Workspace](../Endpoints/organization-workspaces-update.md). It has no member list of its own, because access to it follows each member’s organization role. It appears in [List Workspaces](../Endpoints/organization-workspaces-list.md) results only when you pass `include_default=true`. The [Usage and Cost Analytics API](manage-claude-usage-cost-analytics-api.md) reports its usage and cost under its real ID. The legacy [Usage and Cost API](manage-claude-usage-cost-api.md) reports show `null` for `workspace_id`. For an API key that belongs to it, the key’s `scope` field carries the workspace’s real ID.

### What’s the Claude Code workspace?

Anthropic creates the Claude Code workspace automatically the first time a member of your organization signs in to Claude Code with their Console account. It isolates Claude Code’s API keys, usage, and rate limits from your other workloads. See [Claude Code workspace](#claude-code-workspace) for details.

### Are there limits on workspaces?

Yes. Each organization can have up to 100 workspaces by default, and archived workspaces don’t count toward this limit. If you need more, contact your account team.

### How do organization roles affect workspace access?

Organization admins automatically get the Workspace Admin role in all workspaces. Organization billing members automatically get the Workspace Billing role. Organization users and developers must be manually added to each workspace.

### Which roles can be assigned in workspaces?

Organization users and developers can be assigned Workspace Admin, Workspace Developer, Workspace Limited Developer, or Workspace User roles. The Workspace Billing role cannot be manually assigned; it’s inherited from having the organization `billing` role.

### Can organization admin or billing members’ workspace roles be changed?

Organization admins and billing members cannot have their workspace roles changed or be removed from workspaces while they hold those organization roles (with one exception: billing members can be upgraded to a Workspace Admin role). For everyone else covered by this constraint, change their organization role first to change their workspace access.

### What happens to workspace access when organization roles change?

If an organization admin or billing member is demoted to user or developer, they lose access to all workspaces except ones where they were manually assigned roles. When users are promoted to admin or billing roles, they gain automatic access to all workspaces.

### What happens to API keys when a user is removed from a workspace?

Behavior depends on the [key type](manage-claude-authentication.md#key-types).

A personal or service account key stops working in a workspace shortly after its user or service account is removed from it. A service account key keeps working even if the user who created it is removed. Workspace API keys continue to work. In the [Claude Code workspace](#claude-code-workspace), each key is bound to the member who created it and stops working when that member is removed.

Personal keys are archived when their user is removed from the organization. If the user is re-invited, they need to create new keys; archived keys are not restored.

## See also

- [Admin API](manage-claude-admin-api.md)
- [Admin API reference](../Endpoints/organization.md)
- [Rate limits](../Endpoints/rate-limits.md)
- [Usage and Cost Analytics API](manage-claude-usage-cost-analytics-api.md) and the legacy [Usage and Cost API](manage-claude-usage-cost-api.md)
