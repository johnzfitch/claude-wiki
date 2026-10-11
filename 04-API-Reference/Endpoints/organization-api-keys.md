---
title: "API Keys - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/api_keys"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-09T06:27:53Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Forganization%2Fapi_keys)

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


Organization


Get Current Organization

API Keys


List API Keys


Retrieve API Key (Admin API)


Update API Key

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

Plugins

Plugin Marketplaces


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


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


Create a Text Completion Deprecated

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL



Looking for your API keys? You can view and create them in [Settings → API keys](../Other/playground.md) in the Claude Console.



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)

# API Keys

##### [List API Keys](https://platform.claude.com/docs/en/api/http/organization/api_keys/list)

GET/v1/organizations/api_keys

##### [Retrieve API Key (Admin API)](https://platform.claude.com/docs/en/api/http/organization/api_keys/retrieve)

GET/v1/organizations/api_keys/{api_key_id}

Retrieve information about a single API key in your organization, looked up by its ID. This Admin API endpoint requires an Admin API key, is intended for programmatic key management, and never returns the key's secret value. To view or create your own API keys, go to [API keys](../Other/playground.md) in the Claude Console.

##### [Update API Key](https://platform.claude.com/docs/en/api/http/organization/api_keys/update)

POST/v1/organizations/api_keys/{api_key_id}

##### Models



APIKey object{ type: "api_key", id, created_at, 8 more }





APIKeyCreatedBy object{ type, id }





type: "service_account" or "user"



Type of the actor that created the object.

One of the following:

"service_account"



"user"



id: string



ID of the actor that created the object.



APIKeyOrganizationScope object{ type: "organization" }





type: "organization"



Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

defaultorganization



APIKeyServiceAccountActor object{ type: "service_account_actor", service_account_id }





type: "service_account_actor"



Principal type. Always `"service_account_actor"` for a Service Account.

defaultservice_account_actor

service_account_id: string



ID of the Service Account the API key acts as.



APIKeyUserActor object{ type: "user_actor", user_id }





type: "user_actor"



Principal type. Always `"user_actor"` for a User.

defaultuser_actor

user_id: string



ID of the User the API key acts as.



APIKeyWorkspaceScope object{ type: "workspace", workspace_id }





type: "workspace"



Scope type. Always `"workspace"`: the API key belongs to one Workspace.

defaultworkspace

workspace_id: string



ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.
