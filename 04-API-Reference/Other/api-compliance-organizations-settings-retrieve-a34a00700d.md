---
title: "Get effective organization settings - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/organizations/settings/retrieve"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:41:42Z"
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


Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores


Models


List Models


Get a Model


Dreams


Create a Dream


List Dreams


Get a Dream


Cancel a Dream


Archive a Dream


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Webhooks


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

Workspaces

API Keys

External Keys

Usage Report

Cost Report

Analytics

Spend Limits

Rate Limits

Service Accounts

Federation Issuers

Federation Rules

MCP Tunnels


Compliance API

Activities

Organizations


List organizations

Users

Roles

Settings


Get effective organization settings

Groups

Apps

Code


Completions


Create a Text Completion

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

[](/login)




API reference

Retrieve






To enable the Compliance API, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).

# Get effective organization settings

GET/v1/compliance/organizations/{organization_id}/settings

Retrieve the effective settings for an organization.

Returns the settings currently in force for the given organization — the enforced state after all policies are applied, which may differ from what is configured in the admin console. Settings an organization's administrators cannot change (for example, ones controlled by Anthropic policy or not available to the organization) are omitted from the list.

The organization must belong to the API key's organization hierarchy; unknown organizations and organizations outside the hierarchy return 404.

##### Path ParametersExpand Collapse 

organization_id: string



The organization's UUID

[](#retrieve.organization_id)

##### Header ParametersExpand Collapse 

"x-api-key": optional string



[](#retrieve.x-api-key)

##### ReturnsExpand Collapse 



api_keys: array of object { id, created_at, created_by_id, 5 more }



Compliance API keys configured for the organization hierarchy, ordered by creation time ascending. Key secret values are never included.

id: string



Unique identifier for the API key.

[](#setting_retrieve_response.api_keys.items.id)

created_at: string



When the key was created.

[](#setting_retrieve_response.api_keys.items.created_at)

created_by_id: string



Identifier of the user who created the key, or null when the key was created by automation or its creator's account no longer exists.

[](#setting_retrieve_response.api_keys.items.created_by_id)

is_active: boolean



Whether the key is currently active. A deactivated key is listed for audit visibility but cannot authenticate requests.

[](#setting_retrieve_response.api_keys.items.is_active)

name: string



The name given to the API key when it was created.

[](#setting_retrieve_response.api_keys.items.name)

scopes: array of string



The permission scopes granted to the key.

[](#setting_retrieve_response.api_keys.items.scopes)

expires_at: optional string



When the key will stop authenticating, or null when the key does not expire.

[](#setting_retrieve_response.api_keys.items.expires_at)

type: optional "compliance_api_key"



[](#setting_retrieve_response.api_keys.items.type)

[](#setting_retrieve_response.api_keys)

organization_id: string



[](#setting_retrieve_response.organization_id)



settings: array of object { name, value, type } or object { name, value, type } or object { name, value, type } or 3 more



One of the following:



Boolean object { name, value, type }



A setting whose enforced value is a single true/false flag.



name: "ai_powered_artifacts_enabled" or "api_workbench_feedback_collection_enabled" or "artifact_connectors_enabled" or 43 more



One of the following:

"ai_powered_artifacts_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B0%5D)

"api_workbench_feedback_collection_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B1%5D)

"artifact_connectors_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B2%5D)

"ask_your_org_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B3%5D)

"chat_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B4%5D)

"claude_ai_chat_sharing_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B5%5D)

"claude_ai_feedback_collection_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B6%5D)

"claude_ai_integration_sharing_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B7%5D)

"claude_code_desktop_auto_permissions_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B8%5D)

"claude_code_desktop_bypass_permissions_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B9%5D)

"claude_code_desktop_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B10%5D)

"claude_code_fast_mode_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B11%5D)

"claude_code_metrics_logging_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B12%5D)

"claude_code_remote_control_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B13%5D)

"claude_code_review_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B14%5D)

"claude_code_routines_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B15%5D)

"claude_code_security_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B16%5D)

"claude_code_trusted_devices_required"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B17%5D)

"claude_code_web_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B18%5D)

"claude_code_workflows_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B19%5D)

"claude_design_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B20%5D)

"claude_in_slack_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B21%5D)

"code_execution_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B22%5D)

"code_execution_network_egress_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B23%5D)

"connector_tools_default_always_allow"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B24%5D)

"content_redaction_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B25%5D)

"desktop_extension_allowlist_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B26%5D)

"directory_sync_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B27%5D)

"frontier_data_use_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B28%5D)

"hipaa_compliance_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B29%5D)

"inline_visualizations_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B30%5D)

"ip_allowlist_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B31%5D)

"location_metadata_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B32%5D)

"member_usage_dashboard_visible"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B33%5D)

"memory_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B34%5D)

"org_wide_skill_sharing_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B35%5D)

"public_projects_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B36%5D)

"skill_sharing_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B37%5D)

"skills_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B38%5D)

"sso_claude_ai_enforced"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B39%5D)

"sso_console_enforced"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B40%5D)

"sso_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B41%5D)

"third_party_interactive_content_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B42%5D)

"user_skill_creation_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B43%5D)

"web_search_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B44%5D)

"work_across_apps_enabled"



[](#setting_retrieve_response.settings.items%5B0%5D.name%5B45%5D)

[](#setting_retrieve_response.settings.items%5B0%5D.name)

value: boolean



[](#setting_retrieve_response.settings.items%5B0%5D.value)

type: optional "boolean"



[](#setting_retrieve_response.settings.items%5B0%5D.type)

[](#setting_retrieve_response.settings.items%5B0%5D)



Integer object { name, value, type }



A setting whose enforced value is a whole number; null means no limit is in force.

name: "account_session_duration_seconds"



[](#setting_retrieve_response.settings.items%5B1%5D.name)

value: number



[](#setting_retrieve_response.settings.items%5B1%5D.value)

type: optional "integer"



[](#setting_retrieve_response.settings.items%5B1%5D.type)

[](#setting_retrieve_response.settings.items%5B1%5D)



String object { name, value, type }



A setting whose enforced value is a single string; null means no value is configured.



name: "claude_code_default_worker_environment_id" or "claude_code_default_worker_pool_id"



One of the following:

"claude_code_default_worker_environment_id"



[](#setting_retrieve_response.settings.items%5B2%5D.name%5B0%5D)

"claude_code_default_worker_pool_id"



[](#setting_retrieve_response.settings.items%5B2%5D.name%5B1%5D)

[](#setting_retrieve_response.settings.items%5B2%5D.name)

value: string



[](#setting_retrieve_response.settings.items%5B2%5D.value)

type: optional "string"



[](#setting_retrieve_response.settings.items%5B2%5D.type)

[](#setting_retrieve_response.settings.items%5B2%5D)



StringList object { name, value, type }



A setting whose enforced value is a list of strings.



name: "allowed_invite_domains" or "disabled_admin_request_types" or "ip_allowlist_ip_ranges"



One of the following:

"allowed_invite_domains"



[](#setting_retrieve_response.settings.items%5B3%5D.name%5B0%5D)

"disabled_admin_request_types"



[](#setting_retrieve_response.settings.items%5B3%5D.name%5B1%5D)

"ip_allowlist_ip_ranges"



[](#setting_retrieve_response.settings.items%5B3%5D.name%5B2%5D)

[](#setting_retrieve_response.settings.items%5B3%5D.name)

value: array of string



[](#setting_retrieve_response.settings.items%5B3%5D.value)

type: optional "string_list"



[](#setting_retrieve_response.settings.items%5B3%5D.type)

[](#setting_retrieve_response.settings.items%5B3%5D)



ProvisioningMode object { value, name, type }



How organization members are provisioned, resolved to the enforced mode.

A configured mode is reported only while the mechanism that enforces it is active: just-in-time modes require single sign-on to be enabled, and SCIM modes require directory sync to be enabled. Otherwise `login_only` is reported, regardless of any stored configuration.



value: "jit_advanced" or "jit_permissive" or "login_only" or 2 more



How organization members are provisioned under SSO.

One of the following:

"jit_advanced"



[](#setting_retrieve_response.settings.items%5B4%5D.value%5B0%5D)

"jit_permissive"



[](#setting_retrieve_response.settings.items%5B4%5D.value%5B1%5D)

"login_only"



[](#setting_retrieve_response.settings.items%5B4%5D.value%5B2%5D)

"scim_advanced"



[](#setting_retrieve_response.settings.items%5B4%5D.value%5B3%5D)

"scim_permissive"



[](#setting_retrieve_response.settings.items%5B4%5D.value%5B4%5D)

[](#setting_retrieve_response.settings.items%5B4%5D.value)

name: optional "sso_provisioning_mode"



[](#setting_retrieve_response.settings.items%5B4%5D.name)

type: optional "provisioning_mode"



[](#setting_retrieve_response.settings.items%5B4%5D.type)

[](#setting_retrieve_response.settings.items%5B4%5D)



DataRetention object { value, name, type }



The data retention periods in force, keyed by the type of data they apply to.

A key of `all` covers every data type and is exclusive: when present it is the only key. A missing key means no organization-level administrator-configured retention period is in force for that data type; Anthropic's service defaults may still apply.



value: map\[object { duration, timescale, type } or object { type } \]



One of the following:



Fixed object { duration, timescale, type }



A fixed retention window measured from each item's last activity.

duration: number



[](#setting_retrieve_response.settings.items%5B5%5D.value.items%5B0%5D.duration)



timescale: "day" or "month"



One of the following:

"day"



[](#setting_retrieve_response.settings.items%5B5%5D.value.items%5B0%5D.timescale%5B0%5D)

"month"



[](#setting_retrieve_response.settings.items%5B5%5D.value.items%5B0%5D.timescale%5B1%5D)

[](#setting_retrieve_response.settings.items%5B5%5D.value.items%5B0%5D.timescale)

type: optional "fixed"



[](#setting_retrieve_response.settings.items%5B5%5D.value.items%5B0%5D.type)

[](#setting_retrieve_response.settings.items%5B5%5D.value.items%5B0%5D)



Indefinite object { type }



An indefinite retention period: data is kept with no time limit.

type: optional "indefinite"



[](#setting_retrieve_response.settings.items%5B5%5D.value.items%5B1%5D.type)

[](#setting_retrieve_response.settings.items%5B5%5D.value.items%5B1%5D)

[](#setting_retrieve_response.settings.items%5B5%5D.value)

name: optional "data_retention_periods"



[](#setting_retrieve_response.settings.items%5B5%5D.name)

type: optional "data_retention"



[](#setting_retrieve_response.settings.items%5B5%5D.type)

[](#setting_retrieve_response.settings.items%5B5%5D)

[](#setting_retrieve_response.settings)

type: optional "effective_organization_settings"



[](#setting_retrieve_response.type)

Get effective organization settings



```python
curl https://api.anthropic.com/v1/compliance/organizations/$ORGANIZATION_ID/settings \
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
      "name": "ai_powered_artifacts_enabled",
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
      "name": "ai_powered_artifacts_enabled",
      "value": true,
      "type": "boolean"
    }
  ],
  "type": "effective_organization_settings"
