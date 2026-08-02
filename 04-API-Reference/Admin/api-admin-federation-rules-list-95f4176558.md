---
title: "List Federation Rules - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/federation_rules/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:39:00Z"
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


Create Federation Rule


Get Federation Rule


List Federation Rules


Update Federation Rule


Archive Federation Rule

Workspaces

MCP Tunnels


Compliance API

Activities

Organizations

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

List




# List Federation Rules

GET/v1/organizations/federation_rules

List federation rules in your organization.

Optionally filter by issuer with `issuer_id`. Archived rules are excluded unless `include_archived=true`.

##### Query ParametersExpand Collapse 

include_archived: optional boolean



Include archived resources. Defaults to false.

[](#list.include_archived)

issuer_id: optional string



Filter to rules referencing this federation issuer.

[](#list.issuer_id)

limit: optional number



Number of results per page.

[](#list.limit)

page: optional string



Opaque cursor from a previous response's `next_page`.

[](#list.page)

##### Header ParametersExpand Collapse 



"anthropic-beta": optional array of string



Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

[](#list.anthropic-beta)

##### ReturnsExpand Collapse 



data: array of [FederationRule](/docs/en/api/admin/federation_rules#federation_rule) { id, applies_to_all_workspaces, archived_at, 17 more }



id: string



Tagged ID of the federation rule.

[](#federation_rule.id)

applies_to_all_workspaces: boolean



When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

[](#federation_rule.applies_to_all_workspaces)

archived_at: string



If set, this rule is archived and rejects token exchange.

[](#federation_rule.archived_at)

archived_by_actor_id: string



Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

[](#federation_rule.archived_by_actor_id)

attributes: map\[string\]



CEL expressions extracting named values from claims. Not yet supported; always null.

[](#federation_rule.attributes)

created_at: string



When this rule was created.

[](#federation_rule.created_at)

created_by_actor_id: string



Tagged ID (`user_`/`svac_`) of the actor that created this rule.

[](#federation_rule.created_by_actor_id)

description: string



Optional free-text description.

[](#federation_rule.description)

issuer_id: string



Tagged ID of the issuer whose tokens this rule accepts.

[](#federation_rule.issuer_id)

issuer_name: string



Issuer's display name at read time.

[](#federation_rule.issuer_name)



match: object { audience, claims, condition, subject_prefix }



Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

audience: optional string



Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

[](#federation_rule.match.audience)

claims: optional map\[string\]



Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

[](#federation_rule.match.claims)

condition: optional string



CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

[](#federation_rule.match.condition)

subject_prefix: optional string



Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

[](#federation_rule.match.subject_prefix)

[](#federation_rule.match)

name: string



Admin-chosen slug identifier.

[](#federation_rule.name)

oauth_scope: string



Space-separated OAuth scopes granted on the minted token.

[](#federation_rule.oauth_scope)



target: object { service_account_id, type, service_account_name }



Identity that tokens minted via this rule act as. Currently always a `service_account` target.

service_account_id: string



Tagged ID of the service account to mint tokens for.

[](#federation_rule.target.service_account_id)

type: "service_account"



[](#federation_rule.target.type)

service_account_name: optional string



Service account's display name at read time. Ignored on writes.

[](#federation_rule.target.service_account_name)

[](#federation_rule.target)

token_lifetime_seconds: number



Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

[](#federation_rule.token_lifetime_seconds)

type: "federation_rule"



[](#federation_rule.type)

updated_at: string



When this rule was last updated.

[](#federation_rule.updated_at)

updated_by_actor_id: string



Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

[](#federation_rule.updated_by_actor_id)

workspace_id: string



Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

[](#federation_rule.workspace_id)

workspace_ids: array of string



Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

[](#federation_rule.workspace_ids)

[](#list)

next_page: string



Opaque cursor for the next page, or null if no more results.

[](#list)

List Federation Rules



```python
curl https://api.anthropic.com/v1/organizations/federation_rules \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```python
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
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
