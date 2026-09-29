---
title: "Resources - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/sessions/resources"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:43Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fsessions%2Fresources)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

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


Create Session


List Sessions


Get Session


Update Session


Delete Session


Archive Session

Events

Resources


Add Session Resource


List Session Resources


Get Session Resource


Update Session Resource


Delete Session Resource

Threads

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

1.  [API reference](/docs/en/api/http)
2.  [Beta](/docs/en/api/http/beta)
3.  [Sessions](/docs/en/api/http/beta/sessions)

# Resources

##### [Add Session Resource](/docs/en/api/http/beta/sessions/resources/add)

POST/v1/sessions/{session_id}/resources

##### [List Session Resources](/docs/en/api/http/beta/sessions/resources/list)

GET/v1/sessions/{session_id}/resources

##### [Get Session Resource](/docs/en/api/http/beta/sessions/resources/retrieve)

GET/v1/sessions/{session_id}/resources/{resource_id}

##### [Update Session Resource](/docs/en/api/http/beta/sessions/resources/update)

POST/v1/sessions/{session_id}/resources/{resource_id}

##### [Delete Session Resource](/docs/en/api/http/beta/sessions/resources/delete)

DELETE/v1/sessions/{session_id}/resources/{resource_id}

##### Models



BetaManagedAgentsDeleteSessionResource object{ type: "session_resource_deleted", id }



Confirmation of resource deletion.

type: "session_resource_deleted"



id: string





BetaManagedAgentsFileResource object{ type: "file", id, created_at, 3 more }



type: "file"



id: string





created_at: string



A timestamp in RFC 3339 format

formatdate-time

file_id: string



mount_path: string





updated_at: string



A timestamp in RFC 3339 format

formatdate-time



BetaManagedAgentsGitHubRepositoryResource object{ type: "github_repository", id, created_at, 4 more }





BetaManagedAgentsMemoryStoreResource object{ type: "memory_store", memory_store_id, access, 4 more }



A memory store attached to an agent session.



BetaManagedAgentsSessionResource = [BetaManagedAgentsGitHubRepositoryResource](/docs/en/api/http/beta/sessions/resources#beta_managed_agents_github_repository_resource) or [BetaManagedAgentsFileResource](/docs/en/api/http/beta/sessions/resources#beta_managed_agents_file_resource) or [BetaManagedAgentsMemoryStoreResource](/docs/en/api/http/beta/sessions/resources#beta_managed_agents_memory_store_resource)



One of the following:



ResourceRetrieveResponse = [BetaManagedAgentsGitHubRepositoryResource](/docs/en/api/http/beta/sessions/resources#beta_managed_agents_github_repository_resource) or [BetaManagedAgentsFileResource](/docs/en/api/http/beta/sessions/resources#beta_managed_agents_file_resource) or [BetaManagedAgentsMemoryStoreResource](/docs/en/api/http/beta/sessions/resources#beta_managed_agents_memory_store_resource)



The requested session resource.

One of the following:



ResourceUpdateResponse = [BetaManagedAgentsGitHubRepositoryResource](/docs/en/api/http/beta/sessions/resources#beta_managed_agents_github_repository_resource) or [BetaManagedAgentsFileResource](/docs/en/api/http/beta/sessions/resources#beta_managed_agents_file_resource) or [BetaManagedAgentsMemoryStoreResource](/docs/en/api/http/beta/sessions/resources#beta_managed_agents_memory_store_resource)



The updated session resource.
