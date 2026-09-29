---
title: "Get Skill Version - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/skills/versions/retrieve"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-29T06:30:57Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fskills%2Fversions%2Fretrieve)

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

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/skills/versions/retrieve).

1.  [API reference](http.md)
2.  [Skills](https://platform.claude.com/docs/en/api/http/skills)
3.  [Versions](https://platform.claude.com/docs/en/api/http/skills/versions)

# Get Skill Version

GET/v1/skills/{skill_id}/versions/{version}

Get Skill Version

##### Path parameters



skill_id: string



Unique identifier for the skill.

The format and length of IDs may change over time.



version: string



Identifies the skill version: a version ID, or the literal `latest` for the skill's most recent version.

Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

##### Headers



"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Returns



SkillVersion object{ type: "skill_version", id, created_at, 3 more }





type: "skill_version"



Object type.

For Skill Versions, this is always `"skill_version"`.

defaultskill_version

id: string



Unique identifier for this Skill Version. The id addresses the version in paths and pins it in references.



created_at: string



ISO 8601 timestamp of when the skill was created.

formatdate-time



description: string



Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

name: string



The Skill's immutable kebab-case slug, set at creation from the first upload's SKILL.md frontmatter `name` (or its enclosing directory). Every later upload must resolve to the same value. Also the top-level directory of the Skill's mounted files and the base name of a downloaded archive.



skill_id: string



Unique identifier for the skill.

The format and length of IDs may change over time.

Get Skill Version

cURL



```python
curl https://api.anthropic.com/v1/skills/$SKILL_ID/versions/$VERSION \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "description",
  "name": "name",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "skill_version"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "description",
  "name": "name",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
