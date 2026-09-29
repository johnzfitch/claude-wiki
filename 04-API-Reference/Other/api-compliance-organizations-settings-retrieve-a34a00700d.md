---
title: "Get effective organization settings - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:02Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Forganizations%2Fsettings%2Fretrieve)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores

Dreams


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Models


List Models


Get a Model


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Organization


Get Current Organization

API Keys

External Keys

Federation

Invites

Service Accounts

Users

Workspaces

Rate Limits

Compliance Settings

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Compliance API

Activities

Organizations


List organizations

Users

Roles

Settings


Get effective organization settings

Groups

Apps

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](/docs/en/manage-claude/compliance-api-access)

Copy page



1.  [API reference](/docs/en/api/http)
2.  [Compliance API](/docs/en/api/http/compliance)
3.  [Organizations](/docs/en/api/http/compliance/organizations)
4.  [Settings](/docs/en/api/http/compliance/organizations/settings)

# Get effective organization settings

GET/v1/compliance/organizations/{organization_id}/settings

Retrieve the effective settings for an organization.

Returns the settings currently in force for the given organization — the enforced state after all policies are applied, which may differ from what is configured in the admin console. Settings an organization's administrators cannot change (for example, ones controlled by Anthropic policy or not available to the organization) are omitted from the list. Settings that report a compliance arrangement with Anthropic are the exception: the HIPAA and Access Transparency settings are always included; the API zero data retention setting is reported for Claude Console organizations, and the Claude Code zero data retention and customer-managed encryption keys (CMEK) settings for Claude Enterprise organizations. Each reports whether the arrangement is in place at the organization level; a retention setting on an individual workspace is not reflected.

The organization must belong to the API key's organization hierarchy; unknown organizations and organizations outside the hierarchy return 404.

##### Path parameters

organization_id: string



The organization's UUID

##### Headers

"x-api-key": optional string



##### Returns



type: optional "effective_organization_settings"



defaulteffective_organization_settings



api_keys: array of object{ type: "compliance_api_key", id, created_at, 5 more }



Compliance API keys configured for the organization hierarchy, ordered by creation time ascending. Key secret values are never included.



type: optional "compliance_api_key"



defaultcompliance_api_key

id: string



Unique identifier for the API key.



created_at: string



When the key was created.

formatdate-time

created_by_id: string or null



Identifier of the user who created the key, or null when the key was created by automation or its creator's account no longer exists.

is_active: boolean



Whether the key is currently active. A deactivated key is listed for audit visibility but cannot authenticate requests.

name: string



The name given to the API key when it was created.

scopes: array of string



The permission scopes granted to the key.



expires_at: optional string or null



When the key will stop authenticating, or null when the key does not expire.

formatdate-time

organization_id: string





settings: array of Boolean or Integer or String or 3 more



One of the following:



Boolean object{ type: "boolean", name, value }



A setting whose enforced value is a single true/false flag.



type: optional "boolean"



defaultboolean



name: "access_transparency_enabled" or "ai_powered_artifacts_enabled" or "api_workbench_feedback_collection_enabled" or 59 more



One of the following:

"access_transparency_enabled"



"ai_powered_artifacts_enabled"



"api_workbench_feedback_collection_enabled"



"api_zero_data_retention_enabled"



"artifact_connectors_enabled"



"ask_your_org_enabled"



"chat_enabled"



"claude_academy_inference_enabled"



"claude_ai_chat_sharing_enabled"



"claude_ai_feedback_collection_enabled"



"claude_ai_integration_sharing_enabled"



"claude_ai_skill_plugins_scanning_enabled"



"claude_code_desktop_bypass_permissions_enabled"



"claude_code_desktop_enabled"



"claude_code_fast_mode_enabled"



"claude_code_metrics_logging_enabled"



"claude_code_remote_control_enabled"



"claude_code_review_enabled"



"claude_code_routines_enabled"



"claude_code_security_enabled"



"claude_code_trusted_devices_required"



"claude_code_web_enabled"



"claude_code_workflows_enabled"



"claude_design_enabled"



"claude_enterprise_claude_code_zero_data_retention_enabled"



"claude_in_slack_enabled"



"claude_science_custom_connectors_enabled"



"claude_science_custom_skills_enabled"



"claude_science_enabled"



"claude_science_managed_network_allowlist_enabled"



"claude_science_memory_enabled"



"claude_science_modal_enabled"



"claude_science_scientific_model_endpoints_enabled"



"claude_science_ssh_hosts_enabled"



"cmek_enabled"



"code_execution_enabled"



"code_execution_network_egress_enabled"



"connector_tools_default_always_allow"



"content_redaction_enabled"



"cowork_trusted_devices_required"



"desktop_extension_allowlist_enabled"



"directory_sync_enabled"



"frontier_data_use_enabled"



"group_skill_sharing_enabled"



"hipaa_compliance_enabled"



"inline_visualizations_enabled"



"ip_allowlist_enabled"



"location_metadata_enabled"



"member_usage_dashboard_visible"



"memory_enabled"



"org_wide_skill_sharing_enabled"



"project_sharing_enabled"



"public_projects_enabled"



"skill_sharing_enabled"



"skills_enabled"



"sso_claude_ai_enforced"



"sso_console_enforced"



"sso_enabled"



"third_party_interactive_content_enabled"



"user_skill_creation_enabled"



"web_search_enabled"



"work_across_apps_enabled"



value: boolean





Integer object{ type: "integer", name, value }



A setting whose enforced value is a whole number; null means no limit is in force.



type: optional "integer"



defaultinteger

name: "account_session_duration_seconds"



value: number or null





String object{ type: "string", name, value }



A setting whose enforced value is a single string; null means no value is configured.



type: optional "string"



defaultstring



name: "claude_code_default_worker_environment_id" or "claude_code_default_worker_pool_id"



One of the following:

"claude_code_default_worker_environment_id"



"claude_code_default_worker_pool_id"



value: string or null





StringList object{ type: "string_list", name, value }



A setting whose enforced value is a list of strings.



type: optional "string_list"



defaultstring_list



name: "allowed_invite_domains" or "disabled_admin_request_types" or "ip_allowlist_ip_ranges"



One of the following:

"allowed_invite_domains"



"disabled_admin_request_types"



"ip_allowlist_ip_ranges"



value: array of string





ProvisioningMode object{ type: "provisioning_mode", value, name }



How organization members are provisioned, resolved to the enforced mode.

A configured mode is reported only while the mechanism that enforces it is active: just-in-time modes require single sign-on to be enabled, and SCIM modes require directory sync to be enabled. Otherwise `login_only` is reported, regardless of any stored configuration.



type: optional "provisioning_mode"



defaultprovisioning_mode



value: "jit_advanced" or "jit_permissive" or "login_only" or 2 more



How organization members are provisioned under SSO.

One of the following:

"jit_advanced"



"jit_permissive"



"login_only"



"scim_advanced"



"scim_permissive"





name: optional "sso_provisioning_mode"



defaultsso_provisioning_mode



DataRetention object{ type: "data_retention", value, name }



The data retention periods in force, keyed by the type of data they apply to.

A key of `all` covers every data type and is exclusive: when present it is the only key. A missing key means no organization-level administrator-configured retention period is in force for that data type; Anthropic's service defaults may still apply.



type: optional "data_retention"



defaultdata_retention



value: map\[Fixed or Indefinite\]



One of the following:



Fixed object{ type: "fixed", duration, timescale }



A fixed retention window measured from each item's last activity.



type: optional "fixed"



defaultfixed

duration: number





timescale: "day" or "month"



One of the following:

"day"



"month"





Indefinite object{ type: "indefinite" }



An indefinite retention period: data is kept with no time limit.



type: optional "indefinite"



defaultindefinite



name: optional "data_retention_periods"



defaultdata_retention_periods

Get effective organization settings

cURL



```python
curl https://api.anthropic.com/v1/compliance/organizations/$ORGANIZATION_ID/settings \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "api_keys": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "created_by_id": "created_by_id",
      "is_active": true,
      "name": "name",
      "scopes": [
        "string"
      ],
      "expires_at": "2019-12-27T18:11:19.117Z",
      "type": "compliance_api_key"
    }
  ],
  "organization_id": "organization_id",
  "settings": [
    {
      "name": "access_transparency_enabled",
      "value": true,
      "type": "boolean"
    }
  ],
  "type": "effective_organization_settings"
}
```

##### Returns Examples

Response 200



```python
{
  "api_keys": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "created_by_id": "created_by_id",
      "is_active": true,
      "name": "name",
      "scopes": [
        "string"
      ],
      "expires_at": "2019-12-27T18:11:19.117Z",
      "type": "compliance_api_key"
    }
  ],
  "organization_id": "organization_id",
  "settings": [
    {
      "name": "access_transparency_enabled",
      "value": true,
      "type": "boolean"
    }
  ],
  "type": "effective_organization_settings"
