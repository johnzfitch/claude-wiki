---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:05:05Z"
source_url: "https://platform.claude.com/docs/en/build-with-claude/workspaces"
title: "Workspaces - Claude API Docs"
---

Administration and monitoring

# Workspaces

Copy page

Organize API keys, manage team access, and control costs with workspaces.

Copy page

Workspaces provide a way to organize your API usage within an organization. Use workspaces to separate different projects, environments, or teams while maintaining centralized billing and administration.

## 

How workspaces work

Every organization has a **Default Workspace** that cannot be renamed, archived, or deleted. When you create additional workspaces, you can assign API keys, members, and resource limits to each one.

Key characteristics:

- **Workspace identifiers** use the `wrkspc_` prefix (e.g., `wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ`)
- **Maximum 100 workspaces** per organization (archived workspaces don't count)
- **Default Workspace** has no ID and doesn't appear in list endpoints
- **API keys** are scoped to a single workspace and can only access resources within that workspace

## 

Workspace roles and permissions

Members can have different roles in each workspace, allowing fine-grained access control.

| Role | Permissions |
|----|----|
| Workspace User | Use the Workbench only |
| Workspace Developer | Create and manage API keys, use the API |
| Workspace Admin | Full control over workspace settings and members |
| Workspace Billing | View workspace billing information (inherited from organization billing role) |

### 

Role inheritance

- **Organization admins** automatically receive Workspace Admin access to all workspaces
- **Organization billing members** automatically receive Workspace Billing access to all workspaces
- **Organization users and developers** must be explicitly added to each workspace

The Workspace Billing role cannot be manually assigned. It's inherited from having the organization billing role.

## 

Managing workspaces

Only organization admins can create workspaces. Organization users and developers must be added to workspaces by an admin.

### 

Via the Console

Create and manage workspaces in the [Claude Console](/settings/workspaces).

#### 

Create a workspace

1.  1

    Open workspace settings

    In the Claude Console, go to **Settings \> Workspaces**.

2.  2

    Add a new workspace

    Click **Add Workspace**.

3.  3

    Configure the workspace

    Enter a workspace name and select a color for visual identification.

4.  4

    Create the workspace

    Click **Create** to finalize.

To switch between workspaces in the Console, use the **Workspaces** selector in the top-left corner.

#### 

Edit workspace details

To modify a workspace's name or color:

1.  Select the workspace from the list
2.  Click the ellipsis menu (**...**) and choose **Edit details**
3.  Update the name or color and save your changes

The Default Workspace cannot be renamed or deleted.

#### 

Add members to a workspace

1.  Navigate to the workspace's **Members** tab
2.  Click **Add to Workspace**
3.  Select an organization member and assign them a [workspace role](#workspace-roles-and-permissions)
4.  Confirm the addition

To remove a member, click the trash icon next to their name.

Organization admins and billing members cannot be removed from workspaces while they hold those organization roles.

#### 

Set workspace limits

In the **Limits** tab, you can configure:

- **Rate limits**: Set limits per model tier for requests per minute, input tokens, or output tokens
- **Spend notifications**: Configure alerts when spending reaches certain thresholds

#### 

Archive a workspace

To archive a workspace, click the ellipsis menu (**...**) and select **Archive**. Archiving:

- Preserves historical data for reporting
- Deactivates the workspace and all associated API keys
- Cannot be undone

Archiving a workspace immediately revokes all API keys in that workspace. This action cannot be undone.

### 

Via the Admin API

Programmatically manage workspaces using the [Admin API](/docs/en/build-with-claude/administration-api).

Admin API endpoints require an Admin API key (starting with `sk-ant-admin...`) that differs from standard API keys. Only organization members with the admin role can provision Admin API keys through the [Claude Console](/settings/admin-keys).

``` shiki
# Create a workspace
curl --request POST "https://api.anthropic.com/v1/organizations/workspaces" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{"name": "Production"}'

# List workspaces
curl "https://api.anthropic.com/v1/organizations/workspaces?limit=10&include_archived=false" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

# Archive a workspace
curl --request POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/archive" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

For complete parameter details and response schemas, see the [Workspaces API reference](/docs/en/api/admin-api/workspaces/get-workspace).

### 

Managing workspace members

Add, update, or remove members from a workspace:

``` shiki
# Add a member to a workspace
curl --request POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{
    "user_id": "user_xxx",
    "workspace_role": "workspace_developer"
  }'

# Update a member's role
curl --request POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members/{user_id}" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{"workspace_role": "workspace_admin"}'

# Remove a member from a workspace
curl --request DELETE "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members/{user_id}" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

For complete parameter details, see the [Workspace Members API reference](/docs/en/api/admin-api/workspace_members/get-workspace-member).

## 

API keys and resource scoping

API keys are scoped to a specific workspace. When you create an API key in a workspace, it can only access resources within that workspace.

Resources scoped to workspaces include:

- **Files** created via the [Files API](/docs/en/build-with-claude/files)
- **Message Batches** created via the [Batch API](/docs/en/build-with-claude/batch-processing)
- **Skills** created via the [Skills API](/docs/en/build-with-claude/skills-guide)

Starting February 5, 2026, [prompt caches](/docs/en/build-with-claude/prompt-caching) will also be isolated per workspace (applies to the Claude API and Azure only).

To retrieve your organization's workspace IDs, use the [List Workspaces](/docs/en/api/admin-api/workspaces/list-workspaces) endpoint, or find them in the [Claude Console](/settings/workspaces).

## 

Workspace limits

You can set custom spend and rate limits for each workspace to protect against overuse and ensure fair resource distribution.

### 

Setting workspace limits

Workspace limits can be set lower than (but not higher than) your organization's limits:

- **Spend limits**: Cap monthly spending for a workspace
- **Rate limits**: Limit requests per minute, input tokens per minute, or output tokens per minute

- You cannot set limits on the Default Workspace
- If not set, workspace limits match the organization's limits
- Organization-wide limits always apply, even if workspace limits add up to more

For detailed information on rate limits and how they work, see [Rate limits](/docs/en/api/rate-limits).

## 

Usage and cost tracking

Track usage and costs by workspace using the [Usage and Cost API](/docs/en/build-with-claude/usage-cost-api):

``` shiki
curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-01T00:00:00Z&\
ending_at=2025-01-08T00:00:00Z&\
workspace_ids[]=wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ&\
group_by[]=workspace_id&\
bucket_width=1d" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

Usage and costs attributed to the Default Workspace have a `null` value for `workspace_id`.

## 

Common use cases

### 

Environment separation

Create separate workspaces for development, staging, and production:

| Workspace   | Purpose                                            |
|-------------|----------------------------------------------------|
| Development | Testing and experimentation with lower rate limits |
| Staging     | Pre-production testing with production-like limits |
| Production  | Live traffic with full rate limits and monitoring  |

### 

Team or department isolation

Assign workspaces to different teams for cost allocation and access control:

- **Engineering team** with developer access
- **Data science team** with their own API keys
- **Support team** with limited access for customer tools

### 

Project-based organization

Create workspaces for specific projects or products to track usage and costs separately.

## 

Best practices

1.  1

    Plan your workspace structure

    Consider how you'll organize workspaces before creating them. Think about billing, access control, and usage tracking needs.

2.  2

    Use meaningful names

    Name workspaces clearly to indicate their purpose (e.g., "Production - Customer Chatbot", "Dev - Internal Tools").

3.  3

    Set appropriate limits

    Configure spend and rate limits to prevent unexpected costs and ensure fair resource distribution.

4.  4

    Audit access regularly

    Review workspace membership periodically to ensure only appropriate users have access.

5.  5

    Monitor usage

    Use the [Usage and Cost API](/docs/en/build-with-claude/usage-cost-api) to track workspace-level consumption.

## 

FAQ

### What's the Default Workspace?

### Are there limits on workspaces?

### How do organization roles affect workspace access?

### Which roles can be assigned in workspaces?

### Can organization admin or billing members' workspace roles be changed?

### What happens to workspace access when organization roles change?

### What happens to API keys when a user is removed from a workspace?

## 

See also

- [Admin API overview](/docs/en/build-with-claude/administration-api)
- [Admin API reference](/docs/en/api/admin)
- [Rate limits](/docs/en/api/rate-limits)
- [Usage and Cost API](/docs/en/build-with-claude/usage-cost-api)

Was this page helpful?

- 

- [How workspaces work](#how-workspaces-work)

- [Workspace roles and permissions](#workspace-roles-and-permissions)

- [Role inheritance](#role-inheritance)

- [Managing workspaces](#managing-workspaces)

- [Via the Console](#via-the-console)

- [Via the Admin API](#via-the-admin-api)

- [Managing workspace members](#managing-workspace-members)

- [API keys and resource scoping](#api-keys-and-resource-scoping)

- [Workspace limits](#workspace-limits)

- [Setting workspace limits](#setting-workspace-limits)

- [Usage and cost tracking](#usage-and-cost-tracking)

- [Common use cases](#common-use-cases)

- [Environment separation](#environment-separation)

- [Team or department isolation](#team-or-department-isolation)

- [Project-based organization](#project-based-organization)

- [Best practices](#best-practices)

- [FAQ](#faq)

- [See also](#see-also)

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
