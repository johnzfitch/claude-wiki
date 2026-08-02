---
title: "Skills - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/skills"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:16Z"
tags: ["api", "skills"]
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

Skills




cURL

# Skills

##### [Create Skill](/docs/en/api/beta/skills/create)

POST/v1/skills

##### [List Skills](/docs/en/api/beta/skills/list)

GET/v1/skills

##### [Get Skill](/docs/en/api/beta/skills/retrieve)

GET/v1/skills/{skill_id}

##### [Delete Skill](/docs/en/api/beta/skills/delete)

DELETE/v1/skills/{skill_id}

##### ModelsExpand Collapse 



SkillCreateResponse object { id, created_at, display_title, 4 more }





id: string



Unique identifier for the skill.

The format and length of IDs may change over time.

[](#skill_create_response.id)

created_at: string



ISO 8601 timestamp of when the skill was created.

[](#skill_create_response.created_at)



display_title: string



Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

[](#skill_create_response.display_title)



latest_version: string



The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

[](#skill_create_response.latest_version)



source: string



Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic

[](#skill_create_response.source)



type: string



Object type.

For Skills, this is always `"skill"`.

[](#skill_create_response.type)

updated_at: string



ISO 8601 timestamp of when the skill was last updated.

[](#skill_create_response.updated_at)

[](#skill_create_response)



SkillListResponse object { id, created_at, display_title, 4 more }





id: string



Unique identifier for the skill.

The format and length of IDs may change over time.

[](#skill_list_response.id)

created_at: string



ISO 8601 timestamp of when the skill was created.

[](#skill_list_response.created_at)



display_title: string



Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

[](#skill_list_response.display_title)



latest_version: string



The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

[](#skill_list_response.latest_version)



source: string



Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic

[](#skill_list_response.source)



type: string



Object type.

For Skills, this is always `"skill"`.

[](#skill_list_response.type)

updated_at: string



ISO 8601 timestamp of when the skill was last updated.

[](#skill_list_response.updated_at)

[](#skill_list_response)



SkillRetrieveResponse object { id, created_at, display_title, 4 more }





id: string



Unique identifier for the skill.

The format and length of IDs may change over time.

[](#skill_retrieve_response.id)

created_at: string



ISO 8601 timestamp of when the skill was created.

[](#skill_retrieve_response.created_at)



display_title: string



Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

[](#skill_retrieve_response.display_title)



latest_version: string



The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

[](#skill_retrieve_response.latest_version)



source: string



Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic

[](#skill_retrieve_response.source)



type: string



Object type.

For Skills, this is always `"skill"`.

[](#skill_retrieve_response.type)

updated_at: string



ISO 8601 timestamp of when the skill was last updated.

[](#skill_retrieve_response.updated_at)

[](#skill_retrieve_response)



SkillDeleteResponse object { id, type }





id: string



Unique identifier for the skill.

The format and length of IDs may change over time.

[](#skill_delete_response.id)



type: string



Deleted object type.

For Skills, this is always `"skill_deleted"`.

[](#skill_delete_response.type)

[](#skill_delete_response)

#### SkillsVersions

##### [Create Skill Version](/docs/en/api/beta/skills/versions/create)

POST/v1/skills/{skill_id}/versions

##### [List Skill Versions](/docs/en/api/beta/skills/versions/list)

GET/v1/skills/{skill_id}/versions

##### [Download Skill Version Content](/docs/en/api/beta/skills/versions/download)

GET/v1/skills/{skill_id}/versions/{version}/content

##### [Get Skill Version](/docs/en/api/beta/skills/versions/retrieve)

GET/v1/skills/{skill_id}/versions/{version}

##### [Delete Skill Version](/docs/en/api/beta/skills/versions/delete)

DELETE/v1/skills/{skill_id}/versions/{version}
