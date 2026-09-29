---
title: "Delete Skill Version - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/skills/versions/delete"
category: "04-API-Reference/Other"
fetched_at: "2026-09-28T06:32:38Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fskills%2Fversions%2Fdelete)

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


Create Skill Version


List Skill Versions


Download Skill Version Content


Get Skill Version


Delete Skill Version


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

Apps

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

Copy page



cURL



A beta version of this method exists and may have additional functionality. [View the beta version](/docs/en/api/http/beta/skills/versions/delete).

1.  [API reference](/docs/en/api/http)
2.  [Skills](/docs/en/api/http/skills)
3.  [Versions](/docs/en/api/http/skills/versions)

# Delete Skill Version

DELETE/v1/skills/{skill_id}/versions/{version}

Delete Skill Version

##### Path parameters



skill_id: string



Unique identifier for the skill.

The format and length of IDs may change over time.



version: string



Identifies the skill version by its version ID.

Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

##### Headers



"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Returns



DeletedSkillVersion object{ type: "skill_version_deleted", id }





type: "skill_version_deleted"



Deleted object type.

For Skill Versions, this is always `"skill_version_deleted"`.

defaultskill_version_deleted

id: string



Unique identifier for this Skill Version. The id addresses the version in paths and pins it in references.

Delete Skill Version

cURL



```python
curl https://api.anthropic.com/v1/skills/$SKILL_ID/versions/$VERSION \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "id",
  "type": "skill_version_deleted"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "id",
  "type": "skill_version_deleted"
