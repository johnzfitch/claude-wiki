---
title: "Skills - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/http/beta/skills"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:39:10Z"
tags: ["api", "skills"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fhttp%2Fbeta%2Fskills)

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

# Skills

##### [Create Skill](http-beta-skills-create.md)

POST/v1/skills

##### [List Skills](http-beta-skills-list.md)

GET/v1/skills

##### [Get Skill](http-beta-skills-retrieve.md)

GET/v1/skills/{skill_id}

##### [Delete Skill](http-beta-skills-delete.md)

DELETE/v1/skills/{skill_id}

##### Models



BetaDeletedSkill object{ type: "skill_deleted", id }





type: "skill_deleted"



Deleted object type.

For Skills, this is always `"skill_deleted"`.

defaultskill_deleted



id: string



Unique identifier for the skill.

The format and length of IDs may change over time.



BetaSkill object{ type: "skill", id, created_at, 4 more }





BetaSkillSource object{ type }





type: "custom" or "anthropic" or "anthropic_example" or "plugin"



Where the Skill comes from.

Possible values:

- `"custom"`: authored by the platform user; private to their workspace
- `"anthropic"`: published by Anthropic; shared and read-only
- `"anthropic_example"`: Anthropic-published sample Skill
- `"plugin"`: resolved from an installed plugin

One of the following:

"custom"



"anthropic"



"anthropic_example"



"plugin"



#### Skills[Versions](https://platform.claude.com/docs/en/api/http/beta/skills/versions)

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
