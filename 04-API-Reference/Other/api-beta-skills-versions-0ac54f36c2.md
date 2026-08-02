---
title: "Versions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/skills/versions"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:18Z"
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


Create Skill Version


List Skill Versions


Download Skill Version Content


Get Skill Version


Delete Skill Version


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

Versions




cURL

# Versions

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

##### ModelsExpand Collapse 



VersionCreateResponse object { id, created_at, description, 5 more }





id: string



Unique identifier for the skill version.

The format and length of IDs may change over time.

[](#version_create_response.id)

created_at: string



ISO 8601 timestamp of when the skill version was created.

[](#version_create_response.created_at)



description: string



Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

[](#version_create_response.description)



directory: string



Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

[](#version_create_response.directory)



name: string



Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

[](#version_create_response.name)

skill_id: string



Identifier for the skill that this version belongs to.

[](#version_create_response.skill_id)



type: string



Object type.

For Skill Versions, this is always `"skill_version"`.

[](#version_create_response.type)



version: string



Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

[](#version_create_response.version)

[](#version_create_response)



VersionListResponse object { id, created_at, description, 5 more }





id: string



Unique identifier for the skill version.

The format and length of IDs may change over time.

[](#version_list_response.id)

created_at: string



ISO 8601 timestamp of when the skill version was created.

[](#version_list_response.created_at)



description: string



Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

[](#version_list_response.description)



directory: string



Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

[](#version_list_response.directory)



name: string



Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

[](#version_list_response.name)

skill_id: string



Identifier for the skill that this version belongs to.

[](#version_list_response.skill_id)



type: string



Object type.

For Skill Versions, this is always `"skill_version"`.

[](#version_list_response.type)



version: string



Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

[](#version_list_response.version)

[](#version_list_response)



VersionRetrieveResponse object { id, created_at, description, 5 more }





id: string



Unique identifier for the skill version.

The format and length of IDs may change over time.

[](#version_retrieve_response.id)

created_at: string



ISO 8601 timestamp of when the skill version was created.

[](#version_retrieve_response.created_at)



description: string



Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

[](#version_retrieve_response.description)



directory: string



Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

[](#version_retrieve_response.directory)



name: string



Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

[](#version_retrieve_response.name)

skill_id: string



Identifier for the skill that this version belongs to.

[](#version_retrieve_response.skill_id)



type: string



Object type.

For Skill Versions, this is always `"skill_version"`.

[](#version_retrieve_response.type)



version: string



Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

[](#version_retrieve_response.version)

[](#version_retrieve_response)



VersionDeleteResponse object { id, type }





id: string



Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

[](#version_delete_response.id)



type: string



Deleted object type.

For Skill Versions, this is always `"skill_version_deleted"`.

[](#version_delete_response.type)
