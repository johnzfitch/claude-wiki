---
title: "List Federation Rule Workspaces - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/federation/rules/workspaces/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-09T06:27:36Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Forganization%2Ffederation%2Frules%2Fworkspaces%2Flist)

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


Add Federation Rule Workspace


List Federation Rule Workspaces


Remove Federation Rule Workspace

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

A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/workspaces/list).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Federation](https://platform.claude.com/docs/en/api/http/organization/federation)
4.  [Rules](https://platform.claude.com/docs/en/api/http/organization/federation/rules)
5.  [Workspaces](https://platform.claude.com/docs/en/api/http/organization/federation/rules/workspaces)

# List Federation Rule Workspaces

GET/v1/organizations/federation_rules/{federation_rule_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

List workspaces where this federation rule is enabled.

Returns all workspace enablements in a single response; the `limit` and `page` parameters are accepted but have no effect, and `next_page` is always `null`. Returns explicit per-workspace enablements only; for rules with `applies_to_all_workspaces` or a legacy single `workspace_id`, check those fields on the rule itself.

##### Path parameters

federation_rule_id: string



ID of the federation rule.

##### Query parameters



limit: optional number



Number of results per page.

default20

minimum1

maximum100

page: optional string



Opaque cursor from a previous response's `next_page`.

##### Returns



data: array of [FederationRuleWorkspace](https://platform.claude.com/docs/en/api/http/organization/federation/rules#federation_rule_workspace) { type: "federation_rule_workspace", created_at, created_by_actor_id, 3 more }

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

next_page: string or null



Opaque cursor for the next page; null when there are no more results.

List Federation Rule Workspaces

cURL



```python
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "federation_rule_id": "federation_rule_id",
      "type": "federation_rule_workspace",
      "workspace_id": "workspace_id",
      "workspace_name": "workspace_name"
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
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "federation_rule_id": "federation_rule_id",
      "type": "federation_rule_workspace",
      "workspace_id": "workspace_id",
      "workspace_name": "workspace_name"
