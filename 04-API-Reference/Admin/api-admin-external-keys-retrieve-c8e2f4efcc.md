---
title: "Get External Key - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/admin/external_keys/retrieve"
category: "04-API-Reference/Admin"
fetched_at: "2026-08-02T05:38:58Z"
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

Retrieve




# Get External Key

GET/v1/organizations/external_keys/{external_key_id}

Retrieve a single external key config in the caller's organization by ID.

##### Path ParametersExpand Collapse 

external_key_id: string



ID of the External Key.

[](#retrieve.external_key_id)

##### ReturnsExpand Collapse 

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

Get External Key



```python
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```python
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "type": "aws",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "type": "aws",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
