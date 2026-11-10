---
title: "Create External Key - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/external_keys/create"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-06T06:33:25Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [External Keys](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys)

# Create External Key

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/external_keys

Create an external key config owned by the caller's organization.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Body



provider_config: [BetaAWSExternalKeyConfig](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys#beta_aws_external_key_config) or [BetaGCPExternalKeyConfig](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys#beta_gcp_external_key_config) or [BetaAzureExternalKeyConfigParam](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys#beta_azure_external_key_config_param)

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

BetaAzureExternalKeyConfigParam object{ type: "azure", key_name, tenant_id, 2 more }

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

display_name: optional string or null



Human-friendly display name.

minLength1

maxLength255

geo: optional "us"



Data residency geo. Only `us` is supported.

user_profile_id: optional string or null



ID of a user profile to bind the key to. Omit this field for a key that isn't bound to a user profile. Such a key can be attached to a Workspace whatever its user profile. The binding cannot be changed later. A key bound to a user profile can only be attached to a Workspace that has the same user profile.

##### Returns



BetaExternalKey object{ type: "external_key", id, attachment, 6 more }



CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any workspace references it, the provider fields become effectively immutable (existing encrypted data needs the config for decrypt).

Create External Key

cURL



```python
curl https://api.anthropic.com/v1/organizations/external_keys \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "provider_config": {
            "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
            "type": "aws"
          },
          "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
        }'
```

Response 200



```python
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
```

##### Returns Examples

Response 200



```python
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
