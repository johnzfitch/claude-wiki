---
title: "Configure AWS KMS for CMEK - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms"
category: "04-API-Reference/Other"
fetched_at: "2026-10-20T06:40:16Z"
tags: ["api"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fcmek-aws-kms)





SearchCtrlK

Organization

[Admin API](manage-claude-admin-api.md)[User management](manage-claude-user-management.md)[Plugins API](manage-claude-plugins-api.md)[Workspaces](manage-claude-workspaces.md)

Authentication

[Overview](manage-claude-authentication.md)[Create an Admin API key](manage-claude-admin-api-keys.md)[App Attest](manage-claude-app-attest.md)[Workload Identity Federation](manage-claude-workload-identity-federation.md)[Manage WIF via API](manage-claude-wif-admin-api.md)[WIF reference](manage-claude-wif-reference.md)

Identity providers

Monitoring

[Usage and Cost API](manage-claude-usage-cost-api.md)[Rate Limits API](manage-claude-rate-limits-api.md)[Analytics APIs](manage-claude-analytics-api.md)[Claude Code Analytics API](manage-claude-claude-code-analytics-api.md)[Spend Limits API](manage-claude-spend-limits-api.md)

[OpenTelemetry](manage-claude-opentelemetry.md)

Data & compliance

[Data residency](manage-claude-data-residency.md)[API and data retention](manage-claude-api-and-data-retention.md)

[Access Transparency](manage-claude-access-transparency.md)

[Encryption keys (CMEK)](manage-claude-cmek.md)

[Overview](manage-claude-cmek.md)[Google Cloud KMS](manage-claude-cmek-google-cloud-kms.md)[Azure Key Vault](manage-claude-cmek-azure-key-vault.md)

[AWS KMS](manage-claude-cmek-aws-kms.md)

[Overview](manage-claude-cmek-aws-kms.md)[Claude Platform on AWS](manage-claude-cmek-claude-platform-on-aws.md)

[Inference hooks](manage-claude-inference-hooks.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](playground.md)

[Admin](manage-claude-admin-api.md)Encryption keys (CMEK)

# Configure AWS KMS for CMEK

Copy page



Use AWS KMS to provide an encryption key for your organization.

Copy page



Claude Code

Let Claude Code set up this feature for you

Run in

`❯``/claude-api`` help me configure a customer-managed encryption key with AWS KMS`



This guide shows how to use an [AWS KMS](https://aws.amazon.com/kms/) key as a [customer-managed encryption key (CMEK)](manage-claude-cmek.md) for your Anthropic organization.



Enabling CMEK is permanent. If your KMS key is deleted or disabled, Anthropic cannot recover the data encrypted under it. Review the [warnings and limitations](manage-claude-cmek.md) before you begin.



**Claude Platform on AWS:** If your Claude Console sidebar shows **Account managed by AWS**, your organization is on Claude Platform on AWS. Follow [Set up CMEK on Claude Platform on AWS](manage-claude-cmek-claude-platform-on-aws.md) instead.

## Prerequisites

- An AWS account with permissions to create KMS keys and set key policies (`kms:CreateKey` and `kms:PutKeyPolicy`).
- To create the key from the command line, the [AWS CLI](https://aws.amazon.com/cli/) installed and authenticated.
- To register the key through the API, an Anthropic Admin API key for your organization.

## Amazon Resource Name (ARN) for Anthropic

The key policy in this guide gives the following Anthropic IAM role access to your key:

``` block
arn:aws:iam::915198916910:role/anthropic-cmek-client-us
```





Use only this published ARN. Never trust an identifier provided over email, chat, or any onboarding channel.

## Encryption key setup

### Prepare the key policy

Copy this policy into a text editor:

key-policy.json



```python
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AccountRootAdmin",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<AWS_ACCOUNT_ID>:root"
      },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "AllowAnthropicCMEKCrypto",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::915198916910:role/anthropic-cmek-client-us"
      },
      "Action": ["kms:Encrypt", "kms:Decrypt"],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:anthropic:org_uuid": ["<ORGANIZATION_UUID>"]
        }
      }
    },
    {
      "Sid": "AllowAnthropicCMEKDescribe",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::915198916910:role/anthropic-cmek-client-us"
      },
      "Action": "kms:DescribeKey",
      "Resource": "*"
    }
  ]
}
```

Replace the two placeholders:

- **`<AWS_ACCOUNT_ID>`:** your [AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console-account-id.html). To print it with the AWS CLI, run `aws sts get-caller-identity --query Account --output text`.
- **`<ORGANIZATION_UUID>`:** your Anthropic organization ID



**Finding your organization ID:** Use the bare UUID, not the `org_`-prefixed ID. Copy it from one of these places:

- **Claude Console:** the **Organization ID** field on the [Organization](playground.md) page (`platform.claude.com/settings/organization`)
- **claude.ai:** the **Organization ID** field under **Organization settings \> Organization**
- **Admin API:** the `id` field from the [Organization Info](../Endpoints/organization-retrieve.md) endpoint

Don't remove the `kms:EncryptionContext:anthropic:org_uuid` condition, or validation fails. To share one key among several Anthropic organizations, list each organization ID in it. To limit the key to specific workspaces, see the [optional workspace condition](#workspace-condition).



**Keys that already protect data:** If the key is already configured for CMEK, add this fourth statement so that Anthropic can still decrypt the existing data. In its condition, list the [compartment ID](#compartment-id) of every workspace the key is or was attached to.

```python
{
  "Sid": "AllowAnthropicCMEKDecryptExistingData",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::915198916910:role/anthropic-cmek-client-us"
  },
  "Action": "kms:Decrypt",
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:EncryptionContext:anthropic:compartment_uuid": ["<COMPARTMENT_UUID>"]
    }
  }
}
```



### Create the key

Create the key in a [US region](manage-claude-cmek.md#availability-and-regions). For the lowest latency, use `us-east-2`.

AWS Console

AWS CLI

AWS Console

1.  1

    ### Open the Create key wizard

    Open the [AWS KMS console](https://console.aws.amazon.com/kms) and switch to the region for the key. Go to **Customer managed keys** and click **Create key**.

2.  2

    ### Configure key

    Make sure that these options are selected:

    - **Key type:** Symmetric
    - **Key usage:** Encrypt and decrypt
    - **Advanced options \> Key material origin:** KMS
    - **Advanced options \> Regionality:** Single-Region key

    Click **Next**.

3.  3

    ### Add labels

    Enter an **Alias** for the key, such as `anthropic-cmek`. Click **Next**.

4.  4

    ### Define key administrative permissions

    Don't select any key administrators. Your key policy already gives your AWS account full admin control. Click **Next**.

5.  5

    ### Define key usage permissions

    Don't select any key users, and don't add anything under **Other AWS accounts**. Your key policy already grants the access that's needed. Click **Next**.

6.  6

    ### Edit key policy

    Click **Edit**. Replace the whole policy with your key policy, then click **Next**.

7.  7

    ### Review

    Click **Finish**.

8.  8

    ### Copy the key ARN

    In **Customer managed keys**, open the new key and copy its ARN. You need the ARN to register the key.

To replace the key policy on a key that already exists:

1.  Open the key and click the **Key policy** tab.
2.  If you see **Switch to policy view**, click it.
3.  Click **Edit**.
4.  Replace the JSON with your key policy.
5.  Click **Save changes**.

AWS CLI

Save your key policy as `key-policy.json`, then create the key. Replace `<REGION>` with the key's region.

```python
aws kms create-key \
  --region <REGION> \
  --description "Anthropic CMEK" \
  --key-usage ENCRYPT_DECRYPT \
  --policy file://key-policy.json
```



Copy `KeyMetadata.Arn` from the output. You need it to register the key.



**Optional:** To limit the key to specific workspaces, replace the `AllowAnthropicCMEKCrypto` statement in the key policy with this one. List one compartment ID for each workspace.

```python
{
  "Sid": "AllowAnthropicCMEKCrypto",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::915198916910:role/anthropic-cmek-client-us"
  },
  "Action": ["kms:Encrypt", "kms:Decrypt"],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "kms:EncryptionContext:anthropic:org_uuid": ["<ORGANIZATION_UUID>"]
    },
    "StringEqualsIfExists": {
      "kms:EncryptionContext:anthropic:compartment_uuid": ["<COMPARTMENT_UUID>"]
    }
  }
}
```



Add each workspace's compartment ID before you attach the key to it. For a new workspace:

1.  Create the workspace without the key.
2.  Add its compartment ID to the policy.
3.  Attach the key.

**Finding your compartment ID:** In the Claude Console, go to the [Data retention](playground.md) page (`platform.claude.com/settings/privacy`). Select the workspace from the dropdown menu at the top of the page. The ID is under **Encryption key**, in the **Compartment ID** field. You can also read the `compartment_id` field returned by the [Get Workspace](../Endpoints/organization-workspaces-retrieve.md) endpoint.

## Register the key with Anthropic

Validating the key adds expected access-denied errors to CloudTrail. If you alert on these errors, see [Expected errors in CloudTrail](#expected-errors-in-cloud-trail) first.

Claude Platform

Claude Enterprise

Claude Platform

Claude Console

API

Claude Console

1.  1

    ### Open the encryption key settings

    In the Claude Console, go to the [Data retention](playground.md#encryption-keys) page (`platform.claude.com/settings/privacy`). If you don't see **Encryption keys**, select **Organization** from the dropdown menu at the top of the page.

2.  2

    ### Add the key

    Under **Encryption keys**, click **Add key**. Enter a **Display name** and select **AWS KMS**. Click **Continue**.

3.  3

    ### Enter the key ARN

    The dialog box shows the **Organization ID for the key policy**. Check that your [key policy](#key-policy) contains this ID. Paste the key ARN into **KMS key ARN** and click **Add**.

4.  4

    ### Validate the key

    In the **Encryption keys** list, click **Verify** next to the key. **Connected** appears when the check passes. If it fails, see [Troubleshoot validation](#troubleshoot-validation) for common causes.

5.  5

    ### Attach the key to a workspace

    Attaching a key can't be undone. If you can, attach it to a new workspace before that workspace receives any requests. In a workspace that already receives requests, the key can take [up to a day to take effect](manage-claude-cmek.md#how-it-works).

    On the Data retention page, select the workspace from the dropdown menu at the top of the page. Under **Encryption key**, select the key and click **Save**.

6.  6

    ### Confirm the change

    Select the checkbox to confirm that you have read the CMEK documentation, then click **Confirm**.

API

1.  1

    ### Create the external key

    Replace `<friendly-name>` with a display name and `<key-arn-from-create-key-step>` with the key ARN.

    cURL
    CLI
    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    Python

    

    ``` shiki
    client = anthropic.Anthropic()

    external_key = client.organization.external_keys.create(
        display_name="<friendly-name>",
        geo="us",
        provider_config={"type": "aws", "kms_arn": "<key-arn-from-create-key-step>"},
    )

    print(f"id: {external_key.id}")
    print(f"display_name: {external_key.display_name}")
    ```

    The `id` field of the response contains the external key ID. Copy it for the next two steps:

    ``` shiki
    {
      "type": "external_key",
      "id": "ekey_<id>",
      "display_name": "<friendly-name>"
    }
    ```

    

2.  2

    ### Validate the key

    Replace `ekey_<id>` with the external key ID.

    cURL
    CLI
    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    Python

    

    ``` shiki
    client = anthropic.Anthropic()

    validation = client.organization.external_keys.validate("ekey_<id>")

    print(f"status: {validation.status}")
    print(f"error: {validation.error}")
    ```

    A successful response looks like this:

    ``` shiki
    { "type": "external_key_validation", "status": "success", "error": null }
    ```

    

    If validation fails, see [Troubleshoot validation](#troubleshoot-validation).

3.  3

    ### Attach the key to a workspace

    Attaching a key can't be undone. If you can, attach it to a new workspace before that workspace receives any requests. In a workspace that already receives requests, the key can take [up to a day to take effect](manage-claude-cmek.md#how-it-works).

    Replace `<workspace-id>` with the workspace ID and `ekey_<id>` with the external key ID.

    cURL
    CLI
    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    Python

    

    ``` shiki
    client = anthropic.Anthropic()

    workspace = client.organization.workspaces.update(
        "<workspace-id>", external_key_id="ekey_<id>"
    )

    print(f"id: {workspace.id}")
    print(f"external_key_id: {workspace.external_key_id}")
    ```

Claude Enterprise

On Claude Enterprise, CMEK applies to the whole organization, and an organization can have only one key.

1.  1

    ### Open the encryption key settings

    Go to [claude.ai \> Organization settings \> Data and privacy](https://claude.ai/admin-settings/data-privacy-controls) and find **Encryption keys**.

2.  2

    ### Add the key

    Click **Add key**. Enter a **Display name** and select **AWS KMS**. Select the checkbox to confirm that you have read the CMEK documentation, then click **Continue**.

3.  3

    ### Enter the key ARN

    The dialog box shows the **Organization ID for the key policy**. Check that your [key policy](#key-policy) contains this ID. Paste the key ARN into **KMS key ARN** and click **Add**.

4.  4

    ### Confirm that validation passed

    When the check passes, **Encryption key configured** appears, and your organization is CMEK-protected from then on. If the check fails, see [Troubleshoot validation](#troubleshoot-validation).

## Troubleshoot validation

If validation fails, common causes are:

- **Wrong organization ID:** Make sure the `org_uuid` condition lists your bare organization ID, not the `org_`-prefixed ID.
- **Encryption context mismatch:** If the policy has a `kms:EncryptionContext:anthropic:compartment_uuid` condition, make sure it lists the [compartment ID](#compartment-id) of each workspace the key is attached to. On an older key, the compartment statement might still allow `kms:Encrypt`. In that case, keep the all-zeros value (`00000000-0000-0000-0000-000000000000`) in the list too.
- **Resource control policies (RCPs):** Some RCPs deny KMS operations when `aws:PrincipalOrgID` does not match your AWS organization. An RCP like this blocks Anthropic's role. Add an exception to it for this key or for Anthropic's role ARN. Service control policies do not apply here.
- **Access granted through IAM instead of the key policy:** Grant Anthropic's role access in the key policy itself, not through an IAM policy in your account. To check the key policy, run `aws kms get-key-policy --region <REGION> --key-id <KEY_ARN> --policy-name default`.
- **Region mismatch:** Confirm that the key is in a US region.

### Expected errors in CloudTrail

Anthropic validates the key whenever you verify it, attach it to a workspace, or view it in the Claude Enterprise settings. Each validation adds four access-denied errors to CloudTrail. These errors are expected.

To filter them out, match all three of these values:

- `requestParameters.encryptionContext.associatedData`: `Y21lay12YWxpZGF0aW9u`
- `userIdentity.accountId`: `915198916910`
- `resources.ARN`: `arn:aws:kms:<REGION>:<AWS_ACCOUNT_ID>:key/<KEY_ID>`

The first value alone isn't enough, because any caller can set it.

## Terraform

To create the key with Terraform, use the `aws_kms_key` and `aws_kms_alias` resources from the `aws` provider.
