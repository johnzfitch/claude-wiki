---
title: "External Keys - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/external_keys"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-17T06:26:01Z"
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


[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Forganization%2Fexternal_keys)

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

External Keys


Create External Key


List External Keys


Get External Key


Update External Key


Delete External Key


Validate External Key

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


Completions


Create a Text Completion Deprecated

OpenTelemetry

[Spans](opentelemetry-spans.md)

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/playground.md)

Copy page



cURL



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)

# External Keys

Copy page



cURL

##### [Create External Key](https://platform.claude.com/docs/en/api/http/organization/external_keys/create)

POST/v1/organizations/external_keys

Create an external key config owned by the caller's organization.

##### [List External Keys](https://platform.claude.com/docs/en/api/http/organization/external_keys/list)

GET/v1/organizations/external_keys

List external key configs in the caller's organization.

##### [Get External Key](https://platform.claude.com/docs/en/api/http/organization/external_keys/retrieve)

GET/v1/organizations/external_keys/{external_key_id}

Retrieve a single external key config in the caller's organization by ID.

##### [Update External Key](https://platform.claude.com/docs/en/api/http/organization/external_keys/update)

POST/v1/organizations/external_keys/{external_key_id}

Partially update an external key config. Omitted fields are left unchanged.

##### [Delete External Key](https://platform.claude.com/docs/en/api/http/organization/external_keys/delete)

DELETE/v1/organizations/external_keys/{external_key_id}

Delete an external key config.

##### [Validate External Key](https://platform.claude.com/docs/en/api/http/organization/external_keys/validate)

POST/v1/organizations/external_keys/{external_key_id}/validate

Validate an external key config against the customer's KMS.

##### Models



AWSExternalKeyConfig object{ type: "aws", kms_arn, region, role_arn }



type: "aws"





kms_arn: string



Full ARN of the AWS KMS key. On Claude Platform on AWS the key must be a single-Region key in your organization's own AWS account; cross-account keys, multi-Region keys, and alias ARNs are rejected.

maxLength2048

region: optional string or null



AWS region. Derived from `kms_arn` if omitted.

role_arn: optional string or null⁠Deprecated



IAM role ARN. Deprecated — Anthropic reaches the KMS key through its own intermediate role (or, on Claude Platform on AWS, with credentials AWS issues for the Workspace); this field is ignored.



AzureExternalKeyConfig object{ type: "azure", key_name, tenant_id, 2 more }



type: "azure"



key_name: string



Name of the key within the vault.

tenant_id: string



Azure AD tenant ID.

vault_uri: string



Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

client_id: optional string or null



Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.



AzureExternalKeyConfigParam object{ type: "azure", key_name, tenant_id, 2 more }



Azure Key Vault provider configuration.

type: "azure"



key_name: string



Name of the key within the vault.

tenant_id: string



Azure AD tenant ID.

vault_uri: string



Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

client_id: optional string or null



Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.



ExternalKey object{ type: "external_key", id, attachment, 5 more }



CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any workspace references it, the provider fields become effectively immutable (existing encrypted data needs the config for decrypt).



ExternalKeyAttachedAttachment object{ type: "attached" }





type: "attached"



defaultattached



ExternalKeyUnattachedAttachment object{ type: "unattached" }





type: "unattached"



defaultunattached



GCPExternalKeyConfig object{ type: "gcp", key_name }



type: "gcp"



key_name: string



Full resource name of the Cloud KMS key.



ExternalKeyDeleteResponse object{ type: "external_key_deleted", id }





type: "external_key_deleted"



defaultexternal_key_deleted

id: string



ID of the deleted External Key.



ExternalKeyValidateResponse object{ type: "external_key_validation", error, status }



Result of a validation roundtrip against the customer's KMS.

HTTP 200 for both outcomes — the operation completed; `status` says whether the key works.



type: "external_key_validation"



defaultexternal_key_validation

error: string or null



Error message when status is `failure`. Null otherwise.



status: "failure" or "success"



`success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.
