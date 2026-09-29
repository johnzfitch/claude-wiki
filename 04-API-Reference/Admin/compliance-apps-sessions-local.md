---
title: "Local - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/sessions/local"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-22T06:30:25Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fapps%2Fsessions%2Flocal)

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

Apps

Chats

Projects

Artifacts

Sessions

Local


List local sessions


Retrieve a local session

Messages

Remote

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
3.  [Apps](https://platform.claude.com/docs/en/api/http/compliance/apps)
4.  [Sessions](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions)

# Local

##### [List local sessions](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local/list)

GET/v1/compliance/apps/sessions/local

List local sessions across the organizations the key may read.

##### [Retrieve a local session](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local/retrieve)

GET/v1/compliance/apps/sessions/local/{local_session_id}

Retrieve one local session.

##### Models



LocalRetrieveResponse object{ type: "compliance_local_session", id, created_at, 6 more }



A session that a user ran on their own computer in a Claude app while signed in with their organization account.



LocalListResponse object{ type: "compliance_local_session", id, created_at, 6 more }



A session that a user ran on their own computer in a Claude app while signed in with their organization account.

#### Local[Messages](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local/messages)

##### [Retrieve local session messages](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local/messages/list)

GET/v1/compliance/apps/sessions/local/{local_session_id}/messages

Read one local session's transcript, oldest-first by default.
