---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:05:03Z"
source_url: "https://platform.claude.com/docs/en/build-with-claude/administration-api"
title: "Admin API overview - Claude API Docs"
---

Administration and monitoring

# Admin API overview

Copy page

Copy page

**The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.

The [Admin API](/docs/en/api/admin) allows you to programmatically manage your organization's resources, including organization members, workspaces, and API keys. This provides programmatic control over administrative tasks that would otherwise require manual configuration in the [Claude Console](/).

**The Admin API requires special access**

The Admin API requires a special Admin API key (starting with `sk-ant-admin...`) that differs from standard API keys. Only organization members with the admin role can provision Admin API keys through the Claude Console.

## 

How the Admin API works

When you use the Admin API:

1.  You make requests using your Admin API key in the `x-api-key` header
2.  The API allows you to manage:
    - Organization members and their roles
    - Organization member invites
    - Workspaces and their members
    - API keys

This is useful for:

- Automating user onboarding/offboarding
- Programmatically managing workspace access
- Monitoring and managing API key usage

## 

Organization roles and permissions

There are five organization-level roles. See more details [here](https://support.claude.com/en/articles/10186004-api-console-roles-and-permissions).

| Role | Permissions |
|----|----|
| user | Can use Workbench |
| claude_code_user | Can use Workbench and [Claude Code](https://code.claude.com/docs/en/overview) |
| developer | Can use Workbench and manage API keys |
| billing | Can use Workbench and manage billing details |
| admin | Can do all of the above, plus manage users |

## 

Key concepts

### 

Organization Members

You can list [organization members](/docs/en/api/admin-api/users/get-user), update member roles, and remove members.

Shell

``` shiki
# List organization members
curl "https://api.anthropic.com/v1/organizations/users?limit=10" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

# Update member role
curl "https://api.anthropic.com/v1/organizations/users/{user_id}" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{"role": "developer"}'

# Remove member
curl --request DELETE "https://api.anthropic.com/v1/organizations/users/{user_id}" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

### 

Organization Invites

You can invite users to organizations and manage those [invites](/docs/en/api/admin-api/invites/get-invite).

Shell

``` shiki
# Create invite
curl --request POST "https://api.anthropic.com/v1/organizations/invites" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{
    "email": "newuser@domain.com",
    "role": "developer"
  }'

# List invites
curl "https://api.anthropic.com/v1/organizations/invites?limit=10" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

# Delete invite
curl --request DELETE "https://api.anthropic.com/v1/organizations/invites/{invite_id}" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

### 

Workspaces

For a comprehensive guide to workspaces, see [Workspaces](/docs/en/build-with-claude/workspaces).

Create and manage [workspaces](/docs/en/api/admin-api/workspaces/get-workspace) ([console](/settings/workspaces)) to organize your resources:

Shell

``` shiki
# Create workspace
curl --request POST "https://api.anthropic.com/v1/organizations/workspaces" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{"name": "Production"}'

# List workspaces
curl "https://api.anthropic.com/v1/organizations/workspaces?limit=10&include_archived=false" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

# Archive workspace
curl --request POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/archive" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

### 

Workspace Members

Manage [user access to specific workspaces](/docs/en/api/admin-api/workspace_members/get-workspace-member):

Shell

``` shiki
# Add member to workspace
curl --request POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{
    "user_id": "user_xxx",
    "workspace_role": "workspace_developer"
  }'

# List workspace members
curl "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members?limit=10" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

# Update member role
curl --request POST "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members/{user_id}" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{
    "workspace_role": "workspace_admin"
  }'

# Remove member from workspace
curl --request DELETE "https://api.anthropic.com/v1/organizations/workspaces/{workspace_id}/members/{user_id}" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"
```

### 

API Keys

Monitor and manage [API keys](/docs/en/api/admin-api/apikeys/get-api-key):

Shell

``` shiki
# List API keys
curl "https://api.anthropic.com/v1/organizations/api_keys?limit=10&status=active&workspace_id=wrkspc_xxx" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY"

# Update API key
curl --request POST "https://api.anthropic.com/v1/organizations/api_keys/{api_key_id}" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  --data '{
    "status": "inactive",
    "name": "New Key Name"
  }'
```

## 

Accessing organization info

Get information about your organization programmatically with the `/v1/organizations/me` endpoint.

For example:

``` shiki
curl "https://api.anthropic.com/v1/organizations/me" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

``` shiki
{
  "id": "12345678-1234-5678-1234-567812345678",
  "type": "organization",
  "name": "Organization Name"
}
```

This endpoint is useful for programmatically determining which organization an Admin API key belongs to.

For complete parameter details and response schemas, see the [Organization Info API reference](/docs/en/api/admin-api/organization/get-me).

## 

Accessing usage and cost reports

To access usage and cost reports for your organization, use the Usage and Cost API endpoints:

- The [**Usage endpoint**](/docs/en/build-with-claude/usage-cost-api#usage-api) (`/v1/organizations/usage_report/messages`) provides detailed usage data, including token counts and request metrics, grouped by various dimensions such as workspace, user, and model.
- The [**Cost endpoint**](/docs/en/build-with-claude/usage-cost-api#cost-api) (`/v1/organizations/cost_report`) provides cost data associated with your organization's usage, allowing you to track expenses and allocate costs by workspace or description.

These endpoints provide detailed insights into your organization's usage and associated costs.

## 

Accessing Claude Code analytics

For organizations using Claude Code, the [**Claude Code Analytics API**](/docs/en/build-with-claude/claude-code-analytics-api) provides detailed productivity metrics and usage insights:

- The [**Claude Code Analytics endpoint**](/docs/en/build-with-claude/claude-code-analytics-api) (`/v1/organizations/usage_report/claude_code`) provides daily aggregated metrics for Claude Code usage, including sessions, lines of code, commits, pull requests, tool usage statistics, and cost data broken down by user and model.

This API enables you to track developer productivity, analyze Claude Code adoption, and build custom dashboards for your organization.

## 

Best practices

To effectively use the Admin API:

- Use meaningful names and descriptions for workspaces and API keys
- Implement proper error handling for failed operations
- Regularly audit member roles and permissions
- Clean up unused workspaces and expired invites
- Monitor API key usage and rotate keys periodically

## 

FAQ

### What permissions are needed to use the Admin API?

### Can I create new API keys through the Admin API?

### What happens to API keys when removing a user?

### Can organization admins be removed via the API?

### How long do organization invites last?

### Are there limits on workspaces?

### What's the Default Workspace?

### How do organization roles affect Workspace access?

### Which roles can be assigned in workspaces?

### Can organization admin or billing members' workspace roles be changed?

### What happens to workspace access when organization roles change?

Was this page helpful?

- 

- [How the Admin API works](#how-the-admin-api-works)

- [Organization roles and permissions](#organization-roles-and-permissions)

- [Key concepts](#key-concepts)

- [Organization Members](#organization-members)

- [Organization Invites](#organization-invites)

- [Workspaces](#workspaces)

- [Workspace Members](#workspace-members)

- [API Keys](#api-keys)

- [Accessing organization info](#accessing-organization-info)

- [Accessing usage and cost reports](#accessing-usage-and-cost-reports)

- [Accessing Claude Code analytics](#accessing-claude-code-analytics)

- [Best practices](#best-practices)

- [FAQ](#faq)

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
