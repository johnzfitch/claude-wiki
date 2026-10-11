---
title: "Create Federation Rule - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/federation/rules/create"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-09T06:27:53Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Forganization%2Ffederation%2Frules%2Fcreate)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](overview.md)[Beta headers](beta-headers.md)[Errors](errors.md)


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


Organization


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

Plugins

Plugin Marketplaces


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


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


Create a Text Completion Deprecated

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/create).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Federation](https://platform.claude.com/docs/en/api/http/organization/federation)
4.  [Rules](https://platform.claude.com/docs/en/api/http/organization/federation/rules)

# Create Federation Rule

POST/v1/organizations/federation_rules

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

Create a federation rule owned by your organization.

The referenced issuer and the target service account must already exist in the same organization; invalid references are rejected with a 400 error. The workspace reference is validated. Membership is not checked at rule creation: token exchange resolves a single enabled workspace per call and is rejected unless the target service account is a member of that workspace (it is implicitly a member of the default workspace). Rules on well-known shared issuers (GitHub Actions, GitLab, Buildkite, Terraform Cloud, Google) must constrain tenant identity via an identity-bearing claim, a tenant-pinning subject prefix (such as `repo:YOUR_ORG/...`), or a CEL condition referencing one of those identity claims (e.g. `claims.repository_owner`). OAuth callers may only manage rules whose `oauth_scope` is `workspace:developer` or `workspace:inference`; other scopes require a Console session.

##### Body

issuer_id: string



Tagged ID of the federation issuer.



match: [FederationRuleMatch](https://platform.claude.com/docs/en/api/http/organization/federation/rules#federation_rule_match) { audience, claims, condition, subject_prefix }



Conditions the verified JWT must satisfy for this rule to apply. At least one of `subject_prefix` (other than a wildcard-only value like `*`), `claims`, or `condition` is required; `audience` alone is not sufficient.

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

name: string



Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

minLength1

maxLength255



oauth_scope: string



Space-separated OAuth scopes. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

minLength1



target: [ServiceAccountTarget](https://platform.claude.com/docs/en/api/http/organization/federation/rules#service_account_target) { type: "service_account", service_account_id, service_account_name }



Identity that tokens minted via this rule act as. Currently always a `service_account` target.

type: "service_account"



service_account_id: string



Tagged ID of the service account to mint tokens for.

service_account_name: optional string or null



Service account's display name at read time. Ignored on writes.

applies_to_all_workspaces: optional boolean



When true, enable this rule for every workspace in the org (including workspaces created later).

attributes: optional map\[string\] or null



CEL expressions `{name: expr}` extracting named values from claims. Not yet supported; any non-empty value is rejected with 400.



description: optional string or null



Optional free-text description.

maxLength2000



token_lifetime_seconds: optional number



Lifetime in seconds for access tokens minted via this rule (60-86400). Defaults to 3600 (1h). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

minimum60

maximum86400

workspace_id: optional string or null



Tagged ID of the workspace to enable this rule for. Required unless `applies_to_all_workspaces` is true. Additional workspaces can be added via the `/federation_rules/{federation_rule_id}/workspaces` sub-resource.

##### Returns



FederationRule object{ type: "federation_rule", id, applies_to_all_workspaces, 17 more }



Authorization rule binding an external OIDC identity to Anthropic.

Evaluates the match conditions and mints an OAuth access token for the resolved target, scoped to a single workspace where the rule is enabled (chosen by the caller at exchange time when the rule is enabled for more than one). For rules enabled via `workspace_ids` or `applies_to_all_workspaces`, the target service account must be a member of that workspace (it is implicitly a member of the default workspace); rules carrying only the legacy `workspace_id` binding do not enforce this.

Create Federation Rule

cURL



```python
curl https://api.anthropic.com/v1/organizations/federation_rules \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "issuer_id": "issuer_id",
          "match": {},
          "name": "x",
          "oauth_scope": "x",
          "target": {
            "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
            "type": "service_account"
          }
        }'
```

Response 200



```python
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

##### Returns Examples

Response 200



```python
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
