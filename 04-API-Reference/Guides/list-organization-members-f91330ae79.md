---
category: "04-API-Reference"
source_url: "https://platform.claude.com/docs/en/build-with-claude/administration-api"
title: "List organization members"
---


Administration and monitoring
Admin API overview
Copy page

The Admin API is unavailable for individual accounts. To collaborate with teammates and add members, set up your organization in Console → Settings → Organization.

The Admin API allows you to programmatically manage your organization's resources, including organization members, workspaces, and API keys. This provides programmatic control over administrative tasks that would otherwise require manual configuration in the Claude Console.

The Admin API requires special access

The Admin API requires a special Admin API key (starting with sk-ant-admin...) that differs from standard API keys. Only organization members with the admin role can provision Admin API keys through the Claude Console.

How the Admin API works

When you use the Admin API:

You make requests using your Admin API key in the x-api-key header
The API allows you to manage:
Organization members and their roles
Organization member invites
Workspaces and their members
API keys

This is useful for:

Automating user onboarding/offboarding
Programmatically managing workspace access
Monitoring and managing API key usage
Organization roles and permissions

There are five organization-level roles. See more details here.

Role Permissions
user Can use Workbench
claude_code_user Can use Workbench and Claude Code
developer Can use Workbench and manage API keys
billing Can use Workbench and manage billing details
admin Can do all of the above, plus manage users
Key concepts
Organization Members

You can list organization members, update member roles, and remove members.

Shell
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
Organization Invites

You can invite users to organizations and manage those invites.

Shell
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
Workspaces

For a comprehensive guide to workspaces, see Workspaces.

Create and manage workspaces (console) to organize your resources:

Shell
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
Workspace Members

Manage user access to specific workspaces:

Shell
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
API Keys

Monitor and manage API keys:

Shell
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
Accessing organization info

Get information about your organization programmatically with the /v1/organizations/me endpoint.

For example:

curl "https://api.anthropic.com/v1/organizations/me" \
 --header "anthropic-version: 2023-06-01" \
 --header "x-api-key: $ADMIN_API_KEY"
{
 "id": "12345678-1234-5678-1234-567812345678",
 "type": "organization",
 "name": "Organization Name"
}

This endpoint is useful for programmatically determining which organization an Admin API key belongs to.

For complete parameter details and response schemas, see the Organization Info API reference.

Accessing usage and cost reports

To access usage and cost reports for your organization, use the Usage and Cost API endpoints:

The Usage endpoint (/v1/organizations/usage_report/messages) provides detailed usage data, including token counts and request metrics, grouped by various dimensions such as workspace, user, and model.
The Cost endpoint (/v1/organizations/cost_report) provides cost data associated with your organization's usage, allowing you to track expenses and allocate costs by workspace or description.

These endpoints provide detailed insights into your organization's usage and associated costs.

Accessing Claude Code analytics

For organizations using Claude Code, the Claude Code Analytics API provides detailed productivity metrics and usage insights:

The Claude Code Analytics endpoint (/v1/organizations/usage_report/claude_code) provides daily aggregated metrics for Claude Code usage, including sessions, lines of code, commits, pull requests, tool usage statistics, and cost data broken down by user and model.

This API enables you to track developer productivity, analyze Claude Code adoption, and build custom dashboards for your organization.

Best practices

To effectively use the Admin API:

Use meaningful names and descriptions for workspaces and API keys
Implement proper error handling for failed operations
Regularly audit member roles and permissions
Clean up unused workspaces and expired invites
Monitor API key usage and rotate keys periodically
FAQ
What permissions are needed to use the Admin API?
Can I create new API keys through the Admin API?
What happens to API keys when removing a user?
Can organization admins be removed via the API?
How long do organization invites last?
Are there limits on workspaces?
What's the Default Workspace?
How do organization roles affect Workspace access?
Which roles can be assigned in workspaces?
Can organization admin or billing members' workspace roles be changed?
What happens to workspace access when organization roles change?

Was this page helpful?