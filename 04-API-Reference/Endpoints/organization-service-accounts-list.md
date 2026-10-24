---
title: "List Service Accounts - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/service_accounts/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-17T06:25:36Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Forganization%2Fservice_accounts%2Flist)

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

Invites

Service Accounts


Create Service Account


List Service Accounts


Get Service Account


Update Service Account


Archive Service Account

Workspaces

Users

Workspaces

Rate Limits

Compliance Settings

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles

Plugins

Plugin Marketplaces

Telemetry Destinations


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


Completions


Create a Text Completion Deprecated

OpenTelemetry

[Spans](opentelemetry-spans.md)

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/playground.md)

Copy page



cURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/list).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Service Accounts](https://platform.claude.com/docs/en/api/http/organization/service_accounts)

# List Service Accounts

Copy page



cURL

GET/v1/organizations/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

List service accounts in the caller's organization.

Results are ordered by creation time, newest first. Use `limit` and the `next_page` cursor to paginate; set `include_archived=true` to include archived service accounts.

##### Query parameters



include_archived: optional boolean



Include archived resources. Defaults to false.

defaultfalse

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

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Returns



data: array of [ServiceAccount](https://platform.claude.com/docs/en/api/http/organization/service_accounts#service_account) { type: "service_account", id, archived_at, 8 more }





type: "service_account"



defaultservice_account

id: string



Tagged ID of the service account.



archived_at: string or null



If set, this service account is archived.

formatdate-time

archived_by_actor_id: string or null



Tagged ID (`user_`/`svac_`) of the actor that archived this service account.



created_at: string



When this service account was created.

formatdate-time

created_by_actor_id: string or null



Tagged ID (`user_`/`svac_`) of the actor that created this service account.

description: string or null



Optional free-text description.

name: string



Admin-chosen slug identifier.



organization_role: "admin" or "developer"



Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

One of the following:

"admin"



"developer"





updated_at: string



When this service account was last updated.

formatdate-time

updated_by_actor_id: string or null



Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

next_page: string or null



Opaque cursor for the next page, or null if no more results.

List Service Accounts

cURL



```python
curl https://api.anthropic.com/v1/organizations/service_accounts \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "name": "ci-deploy-bot",
      "organization_role": "admin",
      "type": "service_account",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
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
      "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "name": "ci-deploy-bot",
      "organization_role": "admin",
      "type": "service_account",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
