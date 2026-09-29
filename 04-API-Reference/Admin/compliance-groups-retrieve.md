---
title: "Get Compliance Group - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/groups/retrieve"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-26T06:39:14Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fgroups%2Fretrieve)





SearchCtrlK

Include beta APIs

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


List Compliance Groups


Get Compliance Group

Members

Apps

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)
3.  [Groups](https://platform.claude.com/docs/en/api/http/compliance/groups)

# Get Compliance Group

GET/v1/compliance/groups/{group_id}

Get Compliance Group

##### Path parameters

group_id: string



The group ID (tagged ID, e.g., rbac_group_abc123)

##### Headers

"x-api-key": optional string



##### Returns

id: string



Group identifier (tagged ID)



created_at: string or null



Group creation timestamp (RFC 3339)

formatdate-time

description: string



Group description

name: string



Group name

roles: array of string or null



Role IDs assigned to this group.

source_type: string



How the group was created ('direct' or 'scim')



updated_at: string or null



Group last-updated timestamp (RFC 3339)

formatdate-time

Get Compliance Group

cURL



```python
curl https://api.anthropic.com/v1/compliance/groups/$GROUP_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2025-03-12T18:22:41.123456Z",
  "description": "All members of the engineering organization",
  "name": "Engineering Team",
  "roles": [
    "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
    "rbac_role_01HtCd4mFoAseWS3RnzKcwE7"
  ],
  "source_type": "scim",
  "updated_at": "2025-03-14T09:05:17.456789Z"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2025-03-12T18:22:41.123456Z",
  "description": "All members of the engineering organization",
  "name": "Engineering Team",
  "roles": [
    "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
    "rbac_role_01HtCd4mFoAseWS3RnzKcwE7"
  ],
  "source_type": "scim",
  "updated_at": "2025-03-14T09:05:17.456789Z"
