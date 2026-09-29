---
title: "HTTP API reference - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/http"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:03Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fhttp)

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

# HTTP API reference

#### [Completions](/docs/en/api/http/completions)

##### [Create a Text Completion](/docs/en/api/http/completions/create)

POST/v1/complete

\[Legacy\] Create a Text Completion.

#### [Messages](/docs/en/api/http/messages)

##### [Create a Message](/docs/en/api/http/messages/create)

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

##### [Count tokens in a Message](/docs/en/api/http/messages/count_tokens)

POST/v1/messages/count_tokens

Count the number of tokens in a Message.

#### [Models](/docs/en/api/http/models)

##### [List Models](/docs/en/api/http/models/list)

GET/v1/models

List available models.

##### [Get a Model](/docs/en/api/http/models/retrieve)

GET/v1/models/{model_id}

Get a specific model.

#### [Files](/docs/en/api/http/files)

##### [Upload File](/docs/en/api/http/files/upload)

POST/v1/files

##### [List Files](/docs/en/api/http/files/list)

GET/v1/files

##### [Download File](/docs/en/api/http/files/download)

GET/v1/files/{file_id}/content
