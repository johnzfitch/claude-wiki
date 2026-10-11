---
title: "Plugins - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/plugins"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-09T06:27:29Z"
tags: ["api", "plugins"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Fplugins)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

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


Organization


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

Plugins


Create Plugin


Get Plugin


Update Plugin


List Plugins


Delete Plugin

Versions

Installation Settings

Shares

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


List organizations

Users

Roles

Settings


Plugins

Groups

Apps

Code


Completions


Create a Text Completion Deprecated

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/http-beta.md)
3.  [Organization](http-beta-organization.md)

# Plugins

##### [Create Plugin](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/create)

POST/v1/organizations/plugins

Create an organization-owned Plugin and its first version by uploading the version's files.

##### [Get Plugin](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/retrieve)

GET/v1/organizations/plugins/{plugin_id}

Retrieve a Plugin by ID.

##### [Update Plugin](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/update)

POST/v1/organizations/plugins/{plugin_id}

Change which stored version of an organization-owned Plugin is served to members, for example to roll back to an earlier one. This pins the served version: later uploads are stored but no longer change what is served, and pinning cannot currently be undone, here or in claude.ai.

##### [List Plugins](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/list)

GET/v1/organizations/plugins

List the Plugins created under the organization, newest first: those in the organization's own plugin marketplaces and those in members' personal plugin marketplaces.

##### [Delete Plugin](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/delete)

DELETE/v1/organizations/plugins/{plugin_id}

Permanently delete a Plugin and every version it holds, exactly as when an administrator deletes it in claude.ai. The Plugin may belong to the organization or to a member, including a member who has since left the organization.

##### Models



BetaDeletedPlugin object{ type: "plugin_deleted", id }





type: "plugin_deleted"



Always `plugin_deleted`.

defaultplugin_deleted

id: string



The deleted Plugin's ID.



BetaPlugin object{ type: "plugin", id, components, 16 more }





BetaPluginAPIActor object{ type: "api_actor", api_key_id }





type: "api_actor"



An Admin API key, in the same form the Compliance API activity feed uses for it.

defaultapi_actor

api_key_id: string



The key's ID.



BetaPluginComponent object{ type, description, name }





type: "agent" or "cli" or "command" or 3 more



The kind of component.

One of the following:

"agent"



"cli"



"command"



"hook"



"mcp_server"



"skill"



description: string or null



What the component declares about itself; always null for MCP servers, hooks, and CLIs.

name: string



The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.



BetaPluginContentScan object{ assessment, reason, status }





assessment: "fail" or "pass" or "unknown" or "warn" or null



The scan's verdict; set only when `status` is `completed`.

One of the following:

"fail"



"pass"



"unknown"



"warn"



reason: string or null



The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.



status: "completed" or "errored" or "processing"



`processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

One of the following:

"completed"



"errored"



"processing"





BetaPluginOwnerOrganization object{ type: "organization" }





type: "organization"



The Plugin lives in a plugin marketplace the organization owns.

defaultorganization



BetaPluginOwnerUser object{ type: "user", user_id }





type: "user"



The Plugin lives in one member's personal plugin marketplace.

defaultuser

user_id: string



The member's User ID.



BetaPluginTargetOrganization object{ type: "organization" }





type: "organization"



Every member of the organization.

defaultorganization



BetaPluginTargetOrganizationMember object{ type: "organization_member", user_id }





type: "organization_member"



One member of the organization.

defaultorganization_member

user_id: string



The member's User ID.



BetaPluginTargetRBACGroup object{ type: "rbac_group", rbac_group_id }





type: "rbac_group"



An RBAC Group.

defaultrbac_group

rbac_group_id: string



The RBAC Group's ID.



BetaPluginUserActor object{ type: "user_actor", email_address, user_id }





type: "user_actor"



A member of the organization.

defaultuser_actor

email_address: string or null



The member's email address; may be null, for example when they are no longer a member of the organization.

user_id: string



The member's User ID.

#### Plugins[Versions](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions)

##### [Create Plugin Version](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions/create)

POST/v1/organizations/plugins/{plugin_id}/versions

Add a version to an organization-owned Plugin by uploading the new version's files; it becomes the version served to members unless the Plugin's served version has been pinned.

##### [List Plugin Versions](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions/list)

GET/v1/organizations/plugins/{plugin_id}/versions

List a Plugin's versions, newest first.

##### [Get Plugin Version](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions/retrieve)

GET/v1/organizations/plugins/{plugin_id}/versions/{version}

Retrieve one version of a Plugin by its ID, or the Plugin's newest version.

##### [Download Plugin Version Archive](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions/download)

GET/v1/organizations/plugins/{plugin_id}/versions/{version}/content

Download one version's `.zip` archive, exactly as stored. Each download of a Plugin from a member's personal plugin marketplace is recorded on the Compliance API activity feed.

#### Plugins[Installation Settings](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings)

##### [List Plugin Installation Settings](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/list)

GET/v1/organizations/plugins/{plugin_id}/installation_settings

List an organization-owned Plugin's installation settings, which say which members it is for, most recently created first.

##### [Set Plugin Installation Setting](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/set)

POST/v1/organizations/plugins/{plugin_id}/installation_settings/{target}

Set or change an organization-owned Plugin's installation setting for the whole organization or for one RBAC Group.

##### [Remove Plugin Installation Setting](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/remove)

DELETE/v1/organizations/plugins/{plugin_id}/installation_settings/{target}

Remove an organization-owned Plugin's own installation setting for the whole organization or for one RBAC Group.

#### Plugins[Shares](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/shares)

##### [List Plugin Shares](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/shares/list)

GET/v1/organizations/plugins/{plugin_id}/shares

List the shares the owner of a member-owned Plugin has given — to every member of the organization, to an RBAC Group, or to one member — most recently granted first.
