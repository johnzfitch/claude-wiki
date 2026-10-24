---
title: "Webhooks - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/webhooks"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-21T06:29:30Z"
tags: ["api", "hooks"]
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Fwebhooks)

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

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles

Plugins

Plugin Marketplaces

Telemetry Destinations

Webhooks


Create Organization Webhook Endpoint


List Organization Webhook Endpoints


Get Organization Webhook Endpoint


Update Organization Webhook Endpoint


Delete Organization Webhook Endpoint


Regenerate Organization Webhook Endpoint Signing Secret


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Delete User Profile


Create Enrollment URL

Action URLs


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


Compliance API

Activities

Organizations

Groups

Apps


Completions


Create a Text Completion Deprecated

OpenTelemetry

[Spans](../Endpoints/opentelemetry-spans.md)

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/playground.md)

Copy page



cURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)

# Webhooks

Copy page



cURL

##### [Create Organization Webhook Endpoint](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/create)

POST/v1/organizations/webhooks

Create an organization webhook endpoint.

##### [List Organization Webhook Endpoints](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/list)

GET/v1/organizations/webhooks

List the organization's webhook endpoints.

##### [Get Organization Webhook Endpoint](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/retrieve)

GET/v1/organizations/webhooks/{webhook_endpoint_id}

Retrieve an organization webhook endpoint by ID.

##### [Update Organization Webhook Endpoint](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/update)

POST/v1/organizations/webhooks/{webhook_endpoint_id}

Update an organization webhook endpoint. Only the fields you send are changed.

##### [Delete Organization Webhook Endpoint](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/delete)

DELETE/v1/organizations/webhooks/{webhook_endpoint_id}

Delete an organization webhook endpoint.

##### [Regenerate Organization Webhook Endpoint Signing Secret](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/regenerate_signing_secret)

POST/v1/organizations/webhooks/{webhook_endpoint_id}/regenerate_signing_secret

Replace an organization webhook endpoint's signing secret. The old secret stops working immediately. The new secret is returned only in this response.

##### Models



BetaDeletedOrganizationWebhookEndpoint object{ type: "webhook_endpoint_deleted", id }



A deleted organization webhook endpoint.



type: "webhook_endpoint_deleted"



Always `webhook_endpoint_deleted`.

defaultwebhook_endpoint_deleted

id: string



ID of the deleted webhook endpoint.



BetaNewOrganizationWebhookEndpoint object{ id, created_at, description, 7 more }



A new organization webhook endpoint, with its signing secret.



BetaOrganizationWebhookEndpoint object{ id, created_at, description, 6 more }



A webhook endpoint that belongs to the organization rather than to one of its workspaces.



BetaOrganizationWebhookEndpointSigningSecret object{ signing_secret }



An organization webhook endpoint's new signing secret.

signing_secret: string



The new signing secret. Deliveries are signed with it from now on, and no other response returns it.



BetaOrganizationWebhookEndpointState = "disabled" or "enabled"



Whether deliveries are sent to an organization webhook endpoint.
