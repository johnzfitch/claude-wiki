---
title: "Rules - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/federation/rules"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-28T06:32:30Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Ffederation%2Frules)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

Using the API

[Features overview](../Endpoints/overview.md)[Beta headers](../Endpoints/beta-headers.md)[Errors](../Endpoints/errors.md)


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

Issuers

Rules


Create Federation Rule


List Federation Rules


Get Federation Rule


Update Federation Rule


Archive Federation Rule

Workspaces

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

Groups

Apps

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/http-beta.md)
3.  [Organization](http-beta-organization.md)
4.  [Federation](https://platform.claude.com/docs/en/api/http/beta/organization/federation)

# Rules

##### [Create Federation Rule](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/create)

POST/v1/organizations/federation_rules

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Federation Rules](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/list)

GET/v1/organizations/federation_rules

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Get Federation Rule](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/retrieve)

GET/v1/organizations/federation_rules/{federation_rule_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Update Federation Rule](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/update)

POST/v1/organizations/federation_rules/{federation_rule_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Archive Federation Rule](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/archive)

POST/v1/organizations/federation_rules/{federation_rule_id}/archive

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### Models



BetaFederationRule object{ type: "federation_rule", id, applies_to_all_workspaces, 17 more }



Authorization rule binding an external OIDC identity to Anthropic.

Evaluates the match conditions and mints an OAuth access token for the resolved target, scoped to a single workspace where the rule is enabled (chosen by the caller at exchange time when the rule is enabled for more than one). For rules enabled via `workspace_ids` or `applies_to_all_workspaces`, the target service account must be a member of that workspace (it is implicitly a member of the default workspace); rules carrying only the legacy `workspace_id` binding do not enforce this.



BetaFederationRuleMatch object{ audience, claims, condition, subject_prefix }



Does the incoming JWT qualify?

All populated fields must pass; omitted fields are skipped. At least one of `subject_prefix` (other than a wildcard-only value like `*`), `claims`, or `condition` is required; `audience` alone is not sufficient.



audience: optional string or null



Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

maxLength1024

claims: optional map\[string\] or null



Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.



condition: optional string or null



CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

maxLength4096



subject_prefix: optional string or null



Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

maxLength1024



BetaFederationRuleWorkspace object{ type: "federation_rule_workspace", created_at, created_by_actor_id, 3 more }





type: "federation_rule_workspace"



defaultfederation_rule_workspace



created_at: string



When this workspace was enabled for the rule.

formatdate-time

created_by_actor_id: string or null



Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

federation_rule_id: string



Tagged ID of the federation rule.

workspace_id: string



Tagged ID of the workspace this rule is enabled for.

workspace_name: string or null



Workspace display name. Populated when listing; null in the enable response.



BetaServiceAccountTarget object{ type: "service_account", service_account_id, service_account_name }



Bind to a fixed service account by ID.

type: "service_account"



service_account_id: string



Tagged ID of the service account to mint tokens for.

service_account_name: optional string or null



Service account's display name at read time. Ignored on writes.

#### Rules[Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/workspaces)

##### [Add Federation Rule Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/workspaces/add)

POST/v1/organizations/federation_rules/{federation_rule_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Federation Rule Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/workspaces/list)

GET/v1/organizations/federation_rules/{federation_rule_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Remove Federation Rule Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/workspaces/remove)

DELETE/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).
