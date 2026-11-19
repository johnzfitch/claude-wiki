---
title: "Organization - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:26Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](../Admin/platform-claude-com-http-beta-organization.md).

1.  [API reference](http.md)

# Organization

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Get Current Organization](https://platform.claude.com/docs/en/api/http/organization/retrieve)

GET/v1/organizations/me

Retrieve information about the organization associated with the authenticated API key.

##### Models



ConcurrentMembershipChangeErrorDetails object{ error_code }



Another change to the organization's members is in progress. Retry the request once it completes.

error_code: "concurrent_membership_change"





OrgMemberLimitExceededErrorDetails object{ error_code }



The organization has reached the member limit that Anthropic set for it. Pending invites count toward the limit.

error_code: "org_member_limit_exceeded"





OrganizationInfo object{ type: "organization", id, name }





type: "organization"



Object type.

For Organizations, this is always `"organization"`.

defaultorganization



id: string



ID of the Organization.

formatuuid

name: string



Name of the Organization.



OrganizationRole = "admin" or "billing" or "claude_code_user" or 6 more



One of the following:

"admin"



"billing"



"claude_code_user"



"developer"



"managed"



"membership_admin"



"owner"



"primary_owner"



"user"





RBACRoleNotFoundErrorDetails object{ error_code }



No RBAC Role with this ID was found.

error_code: "rbac_role_not_found"



#### Organization[API Keys](https://platform.claude.com/docs/en/api/http/organization/api_keys)

##### [List API Keys](https://platform.claude.com/docs/en/api/http/organization/api_keys/list)

GET/v1/organizations/api_keys

##### [Retrieve API Key (Admin API)](https://platform.claude.com/docs/en/api/http/organization/api_keys/retrieve)

GET/v1/organizations/api_keys/{api_key_id}

Retrieve information about a single API key in your organization, looked up by its ID. This Admin API endpoint requires an Admin API key, is intended for programmatic key management, and never returns the key's secret value. To view or create your own API keys, go to [API keys](../Other/playground.md) in the Claude Console.

##### [Update API Key](https://platform.claude.com/docs/en/api/http/organization/api_keys/update)

POST/v1/organizations/api_keys/{api_key_id}

#### Organization[External Keys](https://platform.claude.com/docs/en/api/http/organization/external_keys)

##### [Create External Key](https://platform.claude.com/docs/en/api/http/organization/external_keys/create)

POST/v1/organizations/external_keys

Create an external key config owned by the caller's organization.

##### [List External Keys](https://platform.claude.com/docs/en/api/http/organization/external_keys/list)

GET/v1/organizations/external_keys

List external key configs in the caller's organization.

##### [Get External Key](https://platform.claude.com/docs/en/api/http/organization/external_keys/retrieve)

GET/v1/organizations/external_keys/{external_key_id}

Retrieve a single external key config in the caller's organization by ID.

##### [Update External Key](https://platform.claude.com/docs/en/api/http/organization/external_keys/update)

POST/v1/organizations/external_keys/{external_key_id}

Partially update an external key config. Omitted fields are left unchanged.

##### [Delete External Key](https://platform.claude.com/docs/en/api/http/organization/external_keys/delete)

DELETE/v1/organizations/external_keys/{external_key_id}

Delete an external key config.

##### [Validate External Key](https://platform.claude.com/docs/en/api/http/organization/external_keys/validate)

POST/v1/organizations/external_keys/{external_key_id}/validate

Validate an external key config against the customer's KMS.

#### OrganizationFederation[Issuers](https://platform.claude.com/docs/en/api/http/organization/federation/issuers)

##### [Create Federation Issuer](https://platform.claude.com/docs/en/api/http/organization/federation/issuers/create)

POST/v1/organizations/federation_issuers

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Federation Issuers](https://platform.claude.com/docs/en/api/http/organization/federation/issuers/list)

GET/v1/organizations/federation_issuers

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Get Federation Issuer](https://platform.claude.com/docs/en/api/http/organization/federation/issuers/retrieve)

GET/v1/organizations/federation_issuers/{federation_issuer_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Update Federation Issuer](https://platform.claude.com/docs/en/api/http/organization/federation/issuers/update)

POST/v1/organizations/federation_issuers/{federation_issuer_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Archive Federation Issuer](https://platform.claude.com/docs/en/api/http/organization/federation/issuers/archive)

POST/v1/organizations/federation_issuers/{federation_issuer_id}/archive

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### OrganizationFederation[Rules](https://platform.claude.com/docs/en/api/http/organization/federation/rules)

##### [Create Federation Rule](https://platform.claude.com/docs/en/api/http/organization/federation/rules/create)

POST/v1/organizations/federation_rules

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Federation Rules](https://platform.claude.com/docs/en/api/http/organization/federation/rules/list)

GET/v1/organizations/federation_rules

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Get Federation Rule](https://platform.claude.com/docs/en/api/http/organization/federation/rules/retrieve)

GET/v1/organizations/federation_rules/{federation_rule_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Update Federation Rule](https://platform.claude.com/docs/en/api/http/organization/federation/rules/update)

POST/v1/organizations/federation_rules/{federation_rule_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Archive Federation Rule](https://platform.claude.com/docs/en/api/http/organization/federation/rules/archive)

POST/v1/organizations/federation_rules/{federation_rule_id}/archive

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### OrganizationFederationRules[Workspaces](https://platform.claude.com/docs/en/api/http/organization/federation/rules/workspaces)

##### [Add Federation Rule Workspace](https://platform.claude.com/docs/en/api/http/organization/federation/rules/workspaces/add)

POST/v1/organizations/federation_rules/{federation_rule_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Federation Rule Workspaces](https://platform.claude.com/docs/en/api/http/organization/federation/rules/workspaces/list)

GET/v1/organizations/federation_rules/{federation_rule_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Remove Federation Rule Workspace](https://platform.claude.com/docs/en/api/http/organization/federation/rules/workspaces/remove)

DELETE/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### Organization[Invites](https://platform.claude.com/docs/en/api/http/organization/invites)

##### [Create Invite](https://platform.claude.com/docs/en/api/http/organization/invites/create)

POST/v1/organizations/invites

Invite a user to join the organization by email.

##### [List Invites](https://platform.claude.com/docs/en/api/http/organization/invites/list)

GET/v1/organizations/invites

List the organization's invites.

##### [Get Invite](https://platform.claude.com/docs/en/api/http/organization/invites/retrieve)

GET/v1/organizations/invites/{invite_id}

Retrieve an invite by ID.

##### [Delete Invite](https://platform.claude.com/docs/en/api/http/organization/invites/delete)

DELETE/v1/organizations/invites/{invite_id}

Delete a pending invite.

#### Organization[Service Accounts](https://platform.claude.com/docs/en/api/http/organization/service_accounts)

##### [Create Service Account](https://platform.claude.com/docs/en/api/http/organization/service_accounts/create)

POST/v1/organizations/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Service Accounts](https://platform.claude.com/docs/en/api/http/organization/service_accounts/list)

GET/v1/organizations/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Get Service Account](https://platform.claude.com/docs/en/api/http/organization/service_accounts/retrieve)

GET/v1/organizations/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Update Service Account](https://platform.claude.com/docs/en/api/http/organization/service_accounts/update)

POST/v1/organizations/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Archive Service Account](https://platform.claude.com/docs/en/api/http/organization/service_accounts/archive)

POST/v1/organizations/service_accounts/{service_account_id}/archive

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### OrganizationService Accounts[Workspaces](https://platform.claude.com/docs/en/api/http/organization/service_accounts/workspaces)

##### [Add Workspace To Service Account](https://platform.claude.com/docs/en/api/http/organization/service_accounts/workspaces/add)

POST/v1/organizations/service_accounts/{service_account_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Workspaces For Service Account](https://platform.claude.com/docs/en/api/http/organization/service_accounts/workspaces/list)

GET/v1/organizations/service_accounts/{service_account_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Remove Workspace From Service Account](https://platform.claude.com/docs/en/api/http/organization/service_accounts/workspaces/remove)

DELETE/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### Organization[Users](https://platform.claude.com/docs/en/api/http/organization/users)

##### [List Users](https://platform.claude.com/docs/en/api/http/organization/users/list)

GET/v1/organizations/users

List the organization's members.

##### [Get User](https://platform.claude.com/docs/en/api/http/organization/users/retrieve)

GET/v1/organizations/users/{user_id}

Retrieve a member of the organization by user ID.

##### [Update User](https://platform.claude.com/docs/en/api/http/organization/users/update)

POST/v1/organizations/users/{user_id}

Update a member's organization role.

##### [Remove User](https://platform.claude.com/docs/en/api/http/organization/users/remove)

DELETE/v1/organizations/users/{user_id}

Remove a member from the organization.

#### Organization[Workspaces](https://platform.claude.com/docs/en/api/http/organization/workspaces)

##### [List Workspaces](https://platform.claude.com/docs/en/api/http/organization/workspaces/list)

GET/v1/organizations/workspaces

##### [Create Workspace](https://platform.claude.com/docs/en/api/http/organization/workspaces/create)

POST/v1/organizations/workspaces

##### [Get Workspace](https://platform.claude.com/docs/en/api/http/organization/workspaces/retrieve)

GET/v1/organizations/workspaces/{workspace_id}

##### [Update Workspace](https://platform.claude.com/docs/en/api/http/organization/workspaces/update)

POST/v1/organizations/workspaces/{workspace_id}

##### [Archive Workspace](https://platform.claude.com/docs/en/api/http/organization/workspaces/archive)

POST/v1/organizations/workspaces/{workspace_id}/archive

#### OrganizationWorkspaces[Rate Limits](https://platform.claude.com/docs/en/api/http/organization/workspaces/rate_limits)

##### [List Workspace Rate Limits](https://platform.claude.com/docs/en/api/http/organization/workspaces/rate_limits/list)

GET/v1/organizations/workspaces/{workspace_id}/rate_limits

List a workspace's rate limits.

##### [Set Workspace Rate Limits](https://platform.claude.com/docs/en/api/http/organization/workspaces/rate_limits/update)

POST/v1/organizations/workspaces/{workspace_id}/rate_limits/{rate_limit_id}

Set or clear rate-limit overrides for one rate-limit group in a workspace.

#### OrganizationWorkspaces[Members](https://platform.claude.com/docs/en/api/http/organization/workspaces/members)

##### [List Workspace Members](https://platform.claude.com/docs/en/api/http/organization/workspaces/members/list)

GET/v1/organizations/workspaces/{workspace_id}/members

##### [Create Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/members/add)

POST/v1/organizations/workspaces/{workspace_id}/members

##### [Get Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/members/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Update Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/members/update)

POST/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Delete Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/members/remove)

DELETE/v1/organizations/workspaces/{workspace_id}/members/{user_id}

#### OrganizationWorkspaces[Service Accounts](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts)

##### [List Service Account Workspace Members](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts/list)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Create Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts/add)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Get Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Update Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts/update)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Delete Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/organization/workspaces/service_accounts/remove)

DELETE/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### Organization[Rate Limits](https://platform.claude.com/docs/en/api/http/organization/rate_limits)

##### [List Organization Rate Limits](https://platform.claude.com/docs/en/api/http/organization/rate_limits/list)

GET/v1/organizations/rate_limits

List Messages API rate limits for your organization.

#### Organization[Compliance Settings](https://platform.claude.com/docs/en/api/http/organization/compliance_settings)

##### [Get Compliance Settings](https://platform.claude.com/docs/en/api/http/organization/compliance_settings/retrieve)

GET/v1/organizations/compliance_settings

Retrieve your organization's Compliance Settings.

##### [Update Compliance Settings](https://platform.claude.com/docs/en/api/http/organization/compliance_settings/update)

POST/v1/organizations/compliance_settings

Update your organization's Compliance Settings.

#### OrganizationAnalytics[Summaries](https://platform.claude.com/docs/en/api/http/organization/analytics/summaries)

##### [Get Activity Summaries](https://platform.claude.com/docs/en/api/http/organization/analytics/summaries/list)

GET/v1/organizations/analytics/summaries

Get organization-wide activity summaries for a date range.

#### OrganizationAnalytics[Users](https://platform.claude.com/docs/en/api/http/organization/analytics/users)

##### [List User Activity](https://platform.claude.com/docs/en/api/http/organization/analytics/users/list)

GET/v1/organizations/analytics/users

Get per-user activity for a given day, with cursor-based pagination.

#### OrganizationAnalyticsAppsChat[Projects](https://platform.claude.com/docs/en/api/http/organization/analytics/apps/chat/projects)

##### [Get Chat Project Usage](https://platform.claude.com/docs/en/api/http/organization/analytics/apps/chat/projects/list)

GET/v1/organizations/analytics/apps/chat/projects

Get per-project activity for a given day, with cursor-based pagination.

#### OrganizationAnalytics[Connectors](https://platform.claude.com/docs/en/api/http/organization/analytics/connectors)

##### [Get Connector Usage](https://platform.claude.com/docs/en/api/http/organization/analytics/connectors/list)

GET/v1/organizations/analytics/connectors

Get per-connector usage for a given day, with cursor-based pagination.

#### OrganizationAnalytics[Plugins](https://platform.claude.com/docs/en/api/http/organization/analytics/plugins)

##### [Get Plugin Usage](https://platform.claude.com/docs/en/api/http/organization/analytics/plugins/list)

GET/v1/organizations/analytics/plugins

Get per-plugin install + invocation usage for a given day, with pagination.

#### OrganizationAnalytics[Skills](https://platform.claude.com/docs/en/api/http/organization/analytics/skills)

##### [Get Skill Usage](https://platform.claude.com/docs/en/api/http/organization/analytics/skills/list)

GET/v1/organizations/analytics/skills

Get per-skill usage for a given day, with cursor-based pagination.

#### OrganizationAnalytics[Artifacts](https://platform.claude.com/docs/en/api/http/organization/analytics/artifacts)

##### [Get Artifact Activity](https://platform.claude.com/docs/en/api/http/organization/analytics/artifacts/list)

GET/v1/organizations/analytics/artifacts

Get artifact-creation activity for a given day, broken out by MIME type.

#### OrganizationSpend Limits[Effective](https://platform.claude.com/docs/en/api/http/organization/spend_limits/effective)

##### [List Effective Spend Limits](https://platform.claude.com/docs/en/api/http/organization/spend_limits/effective/list)

GET/v1/organizations/spend_limits/effective

List each member's effective spend limit and period-to-date spend.

#### OrganizationSpend Limits[Increase Requests](https://platform.claude.com/docs/en/api/http/organization/spend_limits/increase_requests)

##### [List Spend Limit Increase Requests](https://platform.claude.com/docs/en/api/http/organization/spend_limits/increase_requests/list)

GET/v1/organizations/spend_limit_increase_requests

List spend limit increase requests, most recent first.

##### [Get Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/organization/spend_limits/increase_requests/retrieve)

GET/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}

Retrieve a spend limit increase request.

##### [Approve Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/organization/spend_limits/increase_requests/approve)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve

Approve a pending spend limit increase request.

##### [Deny Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/organization/spend_limits/increase_requests/deny)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny

Deny a pending spend limit increase request.

#### Organization[RBAC Groups](https://platform.claude.com/docs/en/api/http/organization/rbac_groups)

##### [Create RBAC Group](https://platform.claude.com/docs/en/api/http/organization/rbac_groups/create)

POST/v1/organizations/rbac_groups

Create an RBAC Group in the Claude Enterprise tenant. Groups created via the API have source type `"direct"`.

##### [List RBAC Groups](https://platform.claude.com/docs/en/api/http/organization/rbac_groups/list)

GET/v1/organizations/rbac_groups

List RBAC Groups in the Claude Enterprise tenant.

##### [Get RBAC Group](https://platform.claude.com/docs/en/api/http/organization/rbac_groups/retrieve)

GET/v1/organizations/rbac_groups/{rbac_group_id}

Retrieve an RBAC Group by ID.

##### [Update RBAC Group](https://platform.claude.com/docs/en/api/http/organization/rbac_groups/update)

POST/v1/organizations/rbac_groups/{rbac_group_id}

Update an RBAC Group's name. Groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

##### [Delete RBAC Group](https://platform.claude.com/docs/en/api/http/organization/rbac_groups/delete)

DELETE/v1/organizations/rbac_groups/{rbac_group_id}

Delete an RBAC Group. Groups provisioned by an identity provider (source type `"scim"`) cannot be deleted via the API while an organization in the tenant uses SCIM provisioning.

#### OrganizationRBAC Groups[Members](https://platform.claude.com/docs/en/api/http/organization/rbac_groups/members)

##### [List RBAC Group Members](https://platform.claude.com/docs/en/api/http/organization/rbac_groups/members/list)

GET/v1/organizations/rbac_groups/{rbac_group_id}/members

List members of an RBAC Group.

##### [Add RBAC Group Member](https://platform.claude.com/docs/en/api/http/organization/rbac_groups/members/add)

POST/v1/organizations/rbac_groups/{rbac_group_id}/members

Add a User to an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

##### [Remove RBAC Group Member](https://platform.claude.com/docs/en/api/http/organization/rbac_groups/members/remove)

DELETE/v1/organizations/rbac_groups/{rbac_group_id}/members/{user_id}

Remove a User from an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

#### Organization[RBAC Roles](https://platform.claude.com/docs/en/api/http/organization/rbac_roles)

##### [List RBAC Roles](https://platform.claude.com/docs/en/api/http/organization/rbac_roles/list)

GET/v1/organizations/rbac_roles

List RBAC Roles in the organization.

##### [Get RBAC Role](https://platform.claude.com/docs/en/api/http/organization/rbac_roles/retrieve)

GET/v1/organizations/rbac_roles/{rbac_role_id}

Retrieve an RBAC Role by ID.

#### OrganizationRBAC Roles[Permissions](https://platform.claude.com/docs/en/api/http/organization/rbac_roles/permissions)

##### [List RBAC Role Permissions](https://platform.claude.com/docs/en/api/http/organization/rbac_roles/permissions/list)

GET/v1/organizations/rbac_roles/{rbac_role_id}/permissions

List the permissions an RBAC Role grants.
