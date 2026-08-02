---
title: "External Keys - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/external_keys"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:38:57Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores


Models


List Models


Get a Model


Dreams


Create a Dream


List Dreams


Get a Dream


Cancel a Dream


Archive a Dream


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Webhooks


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

Workspaces

API Keys

External Keys


Create External Key


List External Keys


Get External Key


Update External Key


Delete External Key


Validate External Key

Usage Report

Cost Report

Analytics

Spend Limits

Rate Limits

Service Accounts

Federation Issuers

Federation Rules

MCP Tunnels


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

[](/login)




API reference

External keys




# External Keys

##### [Create External Key](/docs/en/api/admin/external_keys/create)

POST/v1/organizations/external_keys

##### [List External Keys](/docs/en/api/admin/external_keys/list)

GET/v1/organizations/external_keys

##### [Get External Key](/docs/en/api/admin/external_keys/retrieve)

GET/v1/organizations/external_keys/{external_key_id}

##### [Update External Key](/docs/en/api/admin/external_keys/update)

POST/v1/organizations/external_keys/{external_key_id}

##### [Delete External Key](/docs/en/api/admin/external_keys/delete)

DELETE/v1/organizations/external_keys/{external_key_id}

##### [Validate External Key](/docs/en/api/admin/external_keys/validate)

POST/v1/organizations/external_keys/{external_key_id}/validate

##### ModelsExpand Collapse 



ExternalKeyCreateResponse object { id, created_at, display_name, 4 more }



CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any workspace references it, the provider fields become effectively immutable (existing encrypted data needs the config for decrypt).

id: string



Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

[](#external_key_create_response.id)

created_at: string



[](#external_key_create_response.created_at)

display_name: string



Human-friendly display name. Null if none was set.

[](#external_key_create_response.display_name)

geo: string



Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

[](#external_key_create_response.geo)



provider_config: object { kms_arn, type, region, role_arn } or object { key_name, type } or object { key_name, tenant_id, type, 2 more }



KMS provider identity and auth coordinates.

One of the following:



Aws object { kms_arn, type, region, role_arn }



kms_arn: string



Full ARN of the AWS KMS key.

[](#external_key_create_response.provider_config%5B0%5D.kms_arn)

type: "aws"



[](#external_key_create_response.provider_config%5B0%5D.type)

region: optional string



AWS region. Derived from kms_arn if omitted.

[](#external_key_create_response.provider_config%5B0%5D.region)

role_arn: optional string⁠Deprecated



IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

[](#external_key_create_response.provider_config%5B0%5D.role_arn)

[](#external_key_create_response.provider_config%5B0%5D)



Gcp object { key_name, type }



key_name: string



Full resource name of the Cloud KMS key.

[](#external_key_create_response.provider_config%5B1%5D.key_name)

type: "gcp"



[](#external_key_create_response.provider_config%5B1%5D.type)

[](#external_key_create_response.provider_config%5B1%5D)



Azure object { key_name, tenant_id, type, 2 more }



key_name: string



Name of the key within the vault.

[](#external_key_create_response.provider_config%5B2%5D.key_name)

tenant_id: string



Azure AD tenant ID.

[](#external_key_create_response.provider_config%5B2%5D.tenant_id)

type: "azure"



[](#external_key_create_response.provider_config%5B2%5D.type)

vault_uri: string



Key Vault data-plane URI — https://\<vault-name\>.vault.azure.net or https://\<hsm-name\>.managedhsm.azure.net.

[](#external_key_create_response.provider_config%5B2%5D.vault_uri)

client_id: optional string



Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

[](#external_key_create_response.provider_config%5B2%5D.client_id)

[](#external_key_create_response.provider_config%5B2%5D)

[](#external_key_create_response.provider_config)

type: "external_key"



[](#external_key_create_response.type)

updated_at: string



[](#external_key_create_response.updated_at)

[](#external_key_create_response)



ExternalKeyListResponse object { id, created_at, display_name, 4 more }



CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any workspace references it, the provider fields become effectively immutable (existing encrypted data needs the config for decrypt).

id: string



Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

[](#external_key_list_response.id)

created_at: string



[](#external_key_list_response.created_at)

display_name: string



Human-friendly display name. Null if none was set.

[](#external_key_list_response.display_name)

geo: string



Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

[](#external_key_list_response.geo)



provider_config: object { kms_arn, type, region, role_arn } or object { key_name, type } or object { key_name, tenant_id, type, 2 more }



KMS provider identity and auth coordinates.

One of the following:



Aws object { kms_arn, type, region, role_arn }



kms_arn: string



Full ARN of the AWS KMS key.

[](#external_key_list_response.provider_config%5B0%5D.kms_arn)

type: "aws"



[](#external_key_list_response.provider_config%5B0%5D.type)

region: optional string



AWS region. Derived from kms_arn if omitted.

[](#external_key_list_response.provider_config%5B0%5D.region)

role_arn: optional string⁠Deprecated



IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

[](#external_key_list_response.provider_config%5B0%5D.role_arn)

[](#external_key_list_response.provider_config%5B0%5D)



Gcp object { key_name, type }



key_name: string



Full resource name of the Cloud KMS key.

[](#external_key_list_response.provider_config%5B1%5D.key_name)

type: "gcp"



[](#external_key_list_response.provider_config%5B1%5D.type)

[](#external_key_list_response.provider_config%5B1%5D)



Azure object { key_name, tenant_id, type, 2 more }



key_name: string



Name of the key within the vault.

[](#external_key_list_response.provider_config%5B2%5D.key_name)

tenant_id: string



Azure AD tenant ID.

[](#external_key_list_response.provider_config%5B2%5D.tenant_id)

type: "azure"



[](#external_key_list_response.provider_config%5B2%5D.type)

vault_uri: string



Key Vault data-plane URI — https://\<vault-name\>.vault.azure.net or https://\<hsm-name\>.managedhsm.azure.net.

[](#external_key_list_response.provider_config%5B2%5D.vault_uri)

client_id: optional string



Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

[](#external_key_list_response.provider_config%5B2%5D.client_id)

[](#external_key_list_response.provider_config%5B2%5D)

[](#external_key_list_response.provider_config)

type: "external_key"



[](#external_key_list_response.type)

updated_at: string



[](#external_key_list_response.updated_at)

[](#external_key_list_response)



ExternalKeyRetrieveResponse object { id, created_at, display_name, 4 more }



CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any workspace references it, the provider fields become effectively immutable (existing encrypted data needs the config for decrypt).

id: string



Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

[](#external_key_retrieve_response.id)

created_at: string



[](#external_key_retrieve_response.created_at)

display_name: string



Human-friendly display name. Null if none was set.

[](#external_key_retrieve_response.display_name)

geo: string



Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

[](#external_key_retrieve_response.geo)



provider_config: object { kms_arn, type, region, role_arn } or object { key_name, type } or object { key_name, tenant_id, type, 2 more }



KMS provider identity and auth coordinates.

One of the following:



Aws object { kms_arn, type, region, role_arn }



kms_arn: string



Full ARN of the AWS KMS key.

[](#external_key_retrieve_response.provider_config%5B0%5D.kms_arn)

type: "aws"



[](#external_key_retrieve_response.provider_config%5B0%5D.type)

region: optional string



AWS region. Derived from kms_arn if omitted.

[](#external_key_retrieve_response.provider_config%5B0%5D.region)

role_arn: optional string⁠Deprecated



IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

[](#external_key_retrieve_response.provider_config%5B0%5D.role_arn)

[](#external_key_retrieve_response.provider_config%5B0%5D)



Gcp object { key_name, type }



key_name: string



Full resource name of the Cloud KMS key.

[](#external_key_retrieve_response.provider_config%5B1%5D.key_name)

type: "gcp"



[](#external_key_retrieve_response.provider_config%5B1%5D.type)

[](#external_key_retrieve_response.provider_config%5B1%5D)



Azure object { key_name, tenant_id, type, 2 more }



key_name: string



Name of the key within the vault.

[](#external_key_retrieve_response.provider_config%5B2%5D.key_name)

tenant_id: string



Azure AD tenant ID.

[](#external_key_retrieve_response.provider_config%5B2%5D.tenant_id)

type: "azure"



[](#external_key_retrieve_response.provider_config%5B2%5D.type)

vault_uri: string



Key Vault data-plane URI — https://\<vault-name\>.vault.azure.net or https://\<hsm-name\>.managedhsm.azure.net.

[](#external_key_retrieve_response.provider_config%5B2%5D.vault_uri)

client_id: optional string



Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

[](#external_key_retrieve_response.provider_config%5B2%5D.client_id)

[](#external_key_retrieve_response.provider_config%5B2%5D)

[](#external_key_retrieve_response.provider_config)

type: "external_key"



[](#external_key_retrieve_response.type)

updated_at: string



[](#external_key_retrieve_response.updated_at)

[](#external_key_retrieve_response)



ExternalKeyUpdateResponse object { id, created_at, display_name, 4 more }



CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any workspace references it, the provider fields become effectively immutable (existing encrypted data needs the config for decrypt).

id: string



Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

[](#external_key_update_response.id)

created_at: string



[](#external_key_update_response.created_at)

display_name: string



Human-friendly display name. Null if none was set.

[](#external_key_update_response.display_name)

geo: string



Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

[](#external_key_update_response.geo)



provider_config: object { kms_arn, type, region, role_arn } or object { key_name, type } or object { key_name, tenant_id, type, 2 more }



KMS provider identity and auth coordinates.

One of the following:



Aws object { kms_arn, type, region, role_arn }



kms_arn: string



Full ARN of the AWS KMS key.

[](#external_key_update_response.provider_config%5B0%5D.kms_arn)

type: "aws"



[](#external_key_update_response.provider_config%5B0%5D.type)

region: optional string



AWS region. Derived from kms_arn if omitted.

[](#external_key_update_response.provider_config%5B0%5D.region)

role_arn: optional string⁠Deprecated



IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

[](#external_key_update_response.provider_config%5B0%5D.role_arn)

[](#external_key_update_response.provider_config%5B0%5D)



Gcp object { key_name, type }



key_name: string



Full resource name of the Cloud KMS key.

[](#external_key_update_response.provider_config%5B1%5D.key_name)

type: "gcp"



[](#external_key_update_response.provider_config%5B1%5D.type)

[](#external_key_update_response.provider_config%5B1%5D)



Azure object { key_name, tenant_id, type, 2 more }



key_name: string



Name of the key within the vault.

[](#external_key_update_response.provider_config%5B2%5D.key_name)

tenant_id: string



Azure AD tenant ID.

[](#external_key_update_response.provider_config%5B2%5D.tenant_id)

type: "azure"



[](#external_key_update_response.provider_config%5B2%5D.type)

vault_uri: string



Key Vault data-plane URI — https://\<vault-name\>.vault.azure.net or https://\<hsm-name\>.managedhsm.azure.net.

[](#external_key_update_response.provider_config%5B2%5D.vault_uri)

client_id: optional string



Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

[](#external_key_update_response.provider_config%5B2%5D.client_id)

[](#external_key_update_response.provider_config%5B2%5D)

[](#external_key_update_response.provider_config)

type: "external_key"



[](#external_key_update_response.type)

updated_at: string



[](#external_key_update_response.updated_at)

[](#external_key_update_response)



ExternalKeyDeleteResponse object { id, type }



id: string



ID of the deleted External Key.

[](#external_key_delete_response.id)

type: "external_key_deleted"



[](#external_key_delete_response.type)

[](#external_key_delete_response)



ExternalKeyValidateResponse object { error, status, type }



Result of a validation roundtrip against the customer's KMS.

HTTP 200 for both outcomes — the operation completed; `status` says whether the key works.

error: string



Error message when status is `failure`. Null otherwise.

[](#external_key_validate_response.error)



status: "failure" or "success"



`success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

One of the following:

"failure"



[](#external_key_validate_response.status%5B0%5D)

"success"



[](#external_key_validate_response.status%5B1%5D)

[](#external_key_validate_response.status)

type: "external_key_validation"



[](#external_key_validate_response.type)

[](#external_key_validate_response)
