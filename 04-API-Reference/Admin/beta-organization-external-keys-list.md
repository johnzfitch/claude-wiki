---
title: "List External Keys - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/external_keys/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-14T06:24:45Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [External Keys](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys)

# List External Keys

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/organizations/external_keys

List external key configs in the caller's organization.

Results are ordered by creation time (newest first). Use the `next_page` cursor from the response to fetch subsequent pages.

##### Query parameters



limit: optional number



Number of results per page.

default20

minimum1

maximum100

page: optional string



Opaque cursor from a previous response's `next_page`.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Returns



data: array of [BetaExternalKey](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys#beta_external_key) { type: "external_key", id, attachment, 6 more }





type: "external_key"



defaultexternal_key

id: string



Identifier of the external key config: a tagged ID prefixed `ekey_`, or, on Claude Platform on AWS, an AWS KMS key's ARN.



attachment: [BetaExternalKeyAttachedAttachment](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys#beta_external_key_attached_attachment) or [BetaExternalKeyUnattachedAttachment](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys#beta_external_key_unattached_attachment)



Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

One of the following:



BetaExternalKeyAttachedAttachment object{ type: "attached" }





type: "attached"



defaultattached



BetaExternalKeyUnattachedAttachment object{ type: "unattached" }





type: "unattached"



defaultunattached



created_at: string



formatdate-time

display_name: string or null



Human-friendly display name. Null if none was set.

geo: string



Data residency geo. Selects the region this key is used in.



provider_config: [BetaAWSExternalKeyConfig](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys#beta_aws_external_key_config) or [BetaGCPExternalKeyConfig](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys#beta_gcp_external_key_config) or [BetaAzureExternalKeyConfig](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys#beta_azure_external_key_config)



KMS provider identity and auth coordinates.

One of the following:



BetaAWSExternalKeyConfig object{ type: "aws", kms_arn, region, role_arn }



type: "aws"





kms_arn: string



Full ARN of the AWS KMS key. On Claude Platform on AWS, alias ARNs are rejected, and your organization's own key must be a single-Region key in your organization's AWS account.

maxLength2048

region: optional string or null



AWS region. Derived from `kms_arn` if omitted.

role_arn: optional string or null⁠Deprecated



IAM role ARN. Deprecated; this field is ignored.



BetaGCPExternalKeyConfig object{ type: "gcp", key_name }



type: "gcp"



key_name: string



Full resource name of the Cloud KMS key.



BetaAzureExternalKeyConfig object{ type: "azure", key_name, tenant_id, 2 more }

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

updated_at: string



formatdate-time

user_profile_id: string or null



ID of the user profile the key is bound to, or null if the key is not bound to one. A key bound to a user profile can only be attached to a Workspace that has the same user profile. A key that isn't bound can be attached to a Workspace whatever its user profile.

next_page: string or null



Opaque cursor for the next page, or null if no more results. Pass as `?page=` to fetch the next page.

List External Keys

cURL



```python
curl https://api.anthropic.com/v1/organizations/external_keys \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
      "attachment": {
        "type": "attached"
      },
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
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
      "attachment": {
        "type": "attached"
      },
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
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
