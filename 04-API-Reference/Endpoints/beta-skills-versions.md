---
title: "Versions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/skills/versions"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:46Z"
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

[API reference](overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fskills%2Fversions)

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

1.  [API reference](http.md)
2.  [Beta](http-beta.md)
3.  [Skills](http-beta-skills.md)

# Versions

##### [Create Skill Version](https://platform.claude.com/docs/en/api/http/beta/skills/versions/create)

POST/v1/skills/{skill_id}/versions

##### [List Skill Versions](https://platform.claude.com/docs/en/api/http/beta/skills/versions/list)

GET/v1/skills/{skill_id}/versions

##### [Download Skill Version Content](https://platform.claude.com/docs/en/api/http/beta/skills/versions/download)

GET/v1/skills/{skill_id}/versions/{version}/content

Download a skill version's content as a zip archive.

##### [Get Skill Version](https://platform.claude.com/docs/en/api/http/beta/skills/versions/retrieve)

GET/v1/skills/{skill_id}/versions/{version}

##### [Delete Skill Version](https://platform.claude.com/docs/en/api/http/beta/skills/versions/delete)

DELETE/v1/skills/{skill_id}/versions/{version}

##### Models



BetaDeletedSkillVersion object{ type: "skill_version_deleted", id }

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



BetaSkillVersion object{ type: "skill_version", id, created_at, 3 more }

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
