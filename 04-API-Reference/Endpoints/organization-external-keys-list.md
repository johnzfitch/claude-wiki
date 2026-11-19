---
title: "List External Keys - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/external_keys/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:28Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys/list).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [External Keys](https://platform.claude.com/docs/en/api/http/organization/external_keys)

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

Read more about versioning and our version history [here](versioning.md).

##### Returns



data: array of [ExternalKey](https://platform.claude.com/docs/en/api/http/organization/external_keys#external_key) { type: "external_key", id, attachment, 6 more }





type: "external_key"



defaultexternal_key

id: string



Identifier of the external key config: a tagged ID prefixed `ekey_`, or, on Claude Platform on AWS, an AWS KMS key's ARN.



attachment: [ExternalKeyAttachedAttachment](https://platform.claude.com/docs/en/api/http/organization/external_keys#external_key_attached_attachment) or [ExternalKeyUnattachedAttachment](https://platform.claude.com/docs/en/api/http/organization/external_keys#external_key_unattached_attachment)



Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

One of the following:

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

provider_config: [AWSExternalKeyConfig](https://platform.claude.com/docs/en/api/http/organization/external_keys#aws_external_key_config) or [GCPExternalKeyConfig](https://platform.claude.com/docs/en/api/http/organization/external_keys#gcp_external_key_config) or [AzureExternalKeyConfig](https://platform.claude.com/docs/en/api/http/organization/external_keys#azure_external_key_config)



KMS provider identity and auth coordinates.

One of the following:



AWSExternalKeyConfig object{ type: "aws", kms_arn, region, role_arn }

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

GCPExternalKeyConfig object{ type: "gcp", key_name }



type: "gcp"



key_name: string



Full resource name of the Cloud KMS key.

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

updated_at: string



formatdate-time

user_profile_id: string or null



ID of the user profile the key is bound to, or null if the key is not bound to one. A key bound to a user profile can only be attached to a Workspace that has the same user profile. A key that isn't bound can only be attached to a Workspace that has no user profile.

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
