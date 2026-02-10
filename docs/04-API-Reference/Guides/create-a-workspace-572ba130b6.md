---
category: "04-API-Reference"
source_url: "https://platform.claude.com/docs/en/build-with-claude/workspaces"
title: "Create a workspace"
---


Administration and monitoring
Workspaces
Copy page
Organize API keys, manage team access, and control costs with workspaces.

Workspaces provide a way to organize your API usage within an organization. Use workspaces to separate different projects, environments, or teams while maintaining centralized billing and administration.

How workspaces work

Every organization has a Default Workspace that cannot be renamed, archived, or deleted. When you create additional workspaces, you can assign API keys, members, and resource limits to each one.

Key characteristics:

Workspace identifiers use the wrkspc_ prefix (e.g., wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ)
Maximum 100 workspaces per organization (archived workspaces don't count)
Default Workspace has no ID and doesn't appear in list endpoints
API keys are scoped to a single workspace and can only access resources within that workspace
Workspace roles and permissions

Members can have different roles in each workspace, allowing fine-grained access control.

Role Permissions
Workspace User Use the Workbench only
Workspace Developer Create and manage API keys, use the API
Workspace Admin Full control over workspace settings and members
Workspace Billing View workspace billing information (inherited from organization billing role)
Role inheritance
Organization admins automatically receive Workspace Admin access to all workspaces
Organization billing members automatically receive Workspace Billing access to all workspaces
Organization users and developers must be explicitly added to each workspace

The Workspace Billing role cannot be manually assigned. It's inherited from having the organization billing role.

Managing workspaces

Only organization admins can create workspaces. Organization users and developers must be added to workspaces by an admin.

Via the Console

Create and manage workspaces in the Claude Console.

Create a workspace
1

Open workspace settings

In the Claude Console, go to Settings > Workspaces.

2

Add a new workspace

Click Add Workspace.

3

Configure the workspace

Enter a workspace name and select a color for visual identification.

4

Create the workspace

Click Create to finalize.

To switch between workspaces in the Console, use the Workspaces selector in the top-left corner.

Edit workspace details

To modify a workspace's name or color:

Select the workspace from the list
Click the ellipsis menu (...) and choose Edit details
Update the name or color and save your changes

The Default Workspace cannot be renamed or deleted.

Add members to a workspace
Navigate to the workspace's Members tab
Click Add to Workspace
Select an organization member and assign them a workspace role
Confirm the addition

To remove a member, click the trash icon next to their name.

Organization admins and billing members cannot be removed from workspaces while they hold those organization roles.

Set workspace limits

In the Limits tab, you can configure:

Rate limits: Set limits per model tier for requests per minute, input tokens, or output tokens
Spend notifications: Configure alerts when spending reaches certain thresholds
Archive a workspace

To archive a workspace, click the ellipsis menu (...) and select Archive. Archiving:

Preserves historical data for reporting
Deactivates the workspace and all associated API keys
Cannot be undone

Archiving a workspace immediately revokes all API keys in that workspace. This action cannot be undone.

Via the Admin API

Programmatically manage workspaces using the Admin API.

Admin API endpoints require an Admin API key (starting with sk-ant-admin...) that differs from standard API keys. Only organization members with the admin role can provision Admin API keys through the Claude Console.

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

For complete parameter details and response schemas, see the Workspaces API reference.

Managing workspace members

Add, update, or remove members from a workspace:

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

For complete parameter details, see the Workspace Members API reference.

API keys and resource scoping

API keys are scoped to a specific workspace. When you create an API key in a workspace, it can only access resources within that workspace.

Resources scoped to workspaces include:

Files created via the Files API
Message Batches created via the Batch API
Skills created via the Skills API

Starting February 5, 2026, prompt caches will also be isolated per workspace (applies to the Claude API and Azure only).

To retrieve your organization's workspace IDs, use the List Workspaces endpoint, or find them in the Claude Console.

Workspace limits

You can set custom spend and rate limits for each workspace to protect against overuse and ensure fair resource distribution.

Setting workspace limits

Workspace limits can be set lower than (but not higher than) your organization's limits:

Spend limits: Cap monthly spending for a workspace
Rate limits: Limit requests per minute, input tokens per minute, or output tokens per minute
You cannot set limits on the Default Workspace
If not set, workspace limits match the organization's limits
Organization-wide limits always apply, even if workspace limits add up to more

For detailed information on rate limits and how they work, see Rate limits.

Usage and cost tracking

Track usage and costs by workspace using the Usage and Cost API:

curl "https://api.anthropic.com/v1/organizations/usage_report/messages?\
starting_at=2025-01-01T00:00:00Z&\
ending_at=2025-01-08T00:00:00Z&\
workspace_ids[]=wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ&\
group_by[]=workspace_id&\
bucket_width=1d" \
 --header "anthropic-version: 2023-06-01" \
 --header "x-api-key: $ADMIN_API_KEY"

Usage and costs attributed to the Default Workspace have a null value for workspace_id.

Common use cases
Environment separation

Create separate workspaces for development, staging, and production:

Workspace Purpose
Development Testing and experimentation with lower rate limits
Staging Pre-production testing with production-like limits
Production Live traffic with full rate limits and monitoring
Team or department isolation

Assign workspaces to different teams for cost allocation and access control:

Engineering team with developer access
Data science team with their own API keys
Support team with limited access for customer tools
Project-based organization

Create workspaces for specific projects or products to track usage and costs separately.

Best practices
1

Plan your workspace structure

Consider how you'll organize workspaces before creating them. Think about billing, access control, and usage tracking needs.

2

Use meaningful names

Name workspaces clearly to indicate their purpose (e.g., "Production - Customer Chatbot", "Dev - Internal Tools").

3

Set appropriate limits

Configure spend and rate limits to prevent unexpected costs and ensure fair resource distribution.

4

Audit access regularly

Review workspace membership periodically to ensure only appropriate users have access.

5

Monitor usage

Use the Usage and Cost API to track workspace-level consumption.

FAQ
What's the Default Workspace?
Are there limits on workspaces?
How do organization roles affect workspace access?
Which roles can be assigned in workspaces?
Can organization admin or billing members' workspace roles be changed?
What happens to workspace access when organization roles change?
What happens to API keys when a user is removed from a workspace?
See also
Admin API overview
Admin API reference
Rate limits
Usage and Cost API

Was this page helpful?