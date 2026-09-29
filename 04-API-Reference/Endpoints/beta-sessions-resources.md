---
title: "Resources - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/sessions/resources"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:43Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fsessions%2Fresources)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

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

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](http.md)
2.  [Beta](http-beta.md)
3.  [Sessions](https://platform.claude.com/docs/en/api/http/beta/sessions)

# Resources

##### [Add Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/add)

POST/v1/sessions/{session_id}/resources

##### [List Session Resources](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/list)

GET/v1/sessions/{session_id}/resources

##### [Get Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/retrieve)

GET/v1/sessions/{session_id}/resources/{resource_id}

##### [Update Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/update)

POST/v1/sessions/{session_id}/resources/{resource_id}

##### [Delete Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/delete)

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

BetaManagedAgentsSessionResource = [BetaManagedAgentsGitHubRepositoryResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_github_repository_resource) or [BetaManagedAgentsFileResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_file_resource) or [BetaManagedAgentsMemoryStoreResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_memory_store_resource)



One of the following:



ResourceRetrieveResponse = [BetaManagedAgentsGitHubRepositoryResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_github_repository_resource) or [BetaManagedAgentsFileResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_file_resource) or [BetaManagedAgentsMemoryStoreResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_memory_store_resource)



The requested session resource.

One of the following:



ResourceUpdateResponse = [BetaManagedAgentsGitHubRepositoryResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_github_repository_resource) or [BetaManagedAgentsFileResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_file_resource) or [BetaManagedAgentsMemoryStoreResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_memory_store_resource)



The updated session resource.
