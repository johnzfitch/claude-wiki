---
title: "External Keys - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/external_keys"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:20Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)

# External Keys

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

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

Full ARN of the AWS KMS key. On Claude Platform on AWS, alias ARNs are rejected, and your organization's own key must be a single-Region key in your organization's AWS account.

maxLength2048

region: optional string or null



AWS region. Derived from `kms_arn` if omitted.

role_arn: optional string or null⁠Deprecated



IAM role ARN. Deprecated; this field is ignored.

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

ExternalKey object{ type: "external_key", id, attachment, 6 more }

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

ExternalKeyChangedErrorDetails object{ error_code }



The external key changed while the request was validating it. Send the request again.

error_code: "external_key_changed"





ExternalKeyInWorkspacePolicyErrorDetails object{ error_code }



The External Key can't be deleted or reconfigured while the organization's Workspace Policy lists it as an allowed key.

error_code: "external_key_in_workspace_policy"





ExternalKeyUnattachedAttachment object{ type: "unattached" }





type: "unattached"



defaultunattached



ExternalKeyValidationFailedErrorDetails object{ error_code }



The External Key failed Anthropic's validation, so the request was refused. The message gives the reason, if there is one.

error_code: "external_key_validation_failed"





ExternalKeyValidationTimedOutErrorDetails object{ error_code }



Anthropic's validation of the External Key did not finish in time, so the request was refused. Wait a moment, then send the request again.

error_code: "external_key_validation_timed_out"



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
