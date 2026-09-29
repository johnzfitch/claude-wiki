---
title: "HTTP API reference - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/http"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fhttp)

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

# HTTP API reference

#### [Completions](http-completions.md)

##### [Create a Text Completion](http-completions-create.md)

POST/v1/complete

\[Legacy\] Create a Text Completion.

#### [Messages](https://platform.claude.com/docs/en/api/http/messages)

##### [Create a Message](https://platform.claude.com/docs/en/api/http/messages/create)

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

##### [Count tokens in a Message](https://platform.claude.com/docs/en/api/http/messages/count_tokens)

POST/v1/messages/count_tokens

Count the number of tokens in a Message.

#### [Models](https://platform.claude.com/docs/en/api/http/models)

##### [List Models](https://platform.claude.com/docs/en/api/http/models/list)

GET/v1/models

List available models.

##### [Get a Model](https://platform.claude.com/docs/en/api/http/models/retrieve)

GET/v1/models/{model_id}

Get a specific model.

#### [Files](https://platform.claude.com/docs/en/api/http/files)

##### [Upload File](https://platform.claude.com/docs/en/api/http/files/upload)

POST/v1/files

##### [List Files](https://platform.claude.com/docs/en/api/http/files/list)

GET/v1/files

##### [Download File](https://platform.claude.com/docs/en/api/http/files/download)

GET/v1/files/{file_id}/content
