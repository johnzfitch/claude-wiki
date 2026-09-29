---
title: "Files - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/http/beta/files"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:39:03Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fhttp%2Fbeta%2Ffiles)

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

# Files

##### [Upload File](http-beta-files-upload.md)

POST/v1/files

##### [List Files](http-beta-files-list.md)

GET/v1/files

##### [Download File](http-beta-files-download.md)

GET/v1/files/{file_id}/content

##### [Get File Metadata](http-beta-files-retrieve-metadata.md)

GET/v1/files/{file_id}

##### [Delete File](http-beta-files-delete.md)

DELETE/v1/files/{file_id}

##### Models



BetaDeletedFile object{ type: "file_deleted", id }





type: optional "file_deleted"



Deleted object type.

For file deletion, this is always `"file_deleted"`.

defaultfile_deleted

id: string



ID of the deleted file.



BetaFileMetadata object{ type: "file", id, created_at, 6 more }





BetaFileScope object{ type: "session", id }



type: "session"



The type of scope (e.g., `"session"`).

id: string



The ID of the scoping resource (e.g., the session ID).
