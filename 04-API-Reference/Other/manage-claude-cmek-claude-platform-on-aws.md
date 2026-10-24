---
title: "Set up CMEK on Claude Platform on AWS - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/cmek-claude-platform-on-aws"
category: "04-API-Reference/Other"
fetched_at: "2026-10-17T06:25:40Z"
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


[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fcmek-claude-platform-on-aws)

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

[Admin](manage-claude-admin-api.md)AWS KMS

# Set up CMEK on Claude Platform on AWS

Copy page



Use an AWS KMS key as a customer-managed encryption key on Claude Platform on AWS.

Copy page



This guide shows how to use an [AWS KMS](https://aws.amazon.com/kms/) key as a [customer-managed encryption key (CMEK)](manage-claude-cmek.md) on [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md). For Claude Platform or Claude Enterprise, follow [Configure AWS KMS for CMEK](manage-claude-cmek-aws-kms.md) instead.



Enabling CMEK is permanent. If your KMS key is deleted or disabled, Anthropic cannot recover the data encrypted under it. Review the [warnings and limitations](manage-claude-cmek.md) before you begin.

## Prerequisites

- The AWS account that hosts your Claude Platform on AWS organization, with permissions to create KMS keys and set key policies (`kms:CreateKey` and `kms:PutKeyPolicy`).

- To create the key from the command line, the [AWS CLI](https://aws.amazon.com/cli/) installed and authenticated.

- The **Admin** role in the Claude Console for Claude Platform on AWS. See [Using the Claude Console](../Guides/build-with-claude-claude-platform-on-aws.md#using-the-claude-console).

- These permissions for the IAM principal you sign in to the Claude Console with:

  - **Sign in:** `aws-external-anthropic:AssumeConsole`
  - **Register a key:** `aws-external-anthropic:RegisterKey`
  - **View registered keys:** `aws-external-anthropic:ListKeys` and `aws-external-anthropic:GetKey`
  - **Attach a key:** `aws-external-anthropic:UpdateWorkspace` or `aws-external-anthropic:CreateWorkspace`, plus `kms:DescribeKey`, `kms:Encrypt`, and `kms:Decrypt` on the key
  - **Pick the key from a list (optional):** `kms:ListKeys` and `kms:DescribeKey`

  `aws-external-anthropic:RegisterKey`, `aws-external-anthropic:ListKeys`, `aws-external-anthropic:GetKey`, and `aws-external-anthropic:CreateWorkspace` are account-scoped. Grant them on `Resource: "*"`. See [IAM actions](../Endpoints/claude-platform-on-aws-iam-actions.md#encryption-keys).

## AWS service principal for Anthropic

The key policy in this guide gives the following AWS service principal access to your key:

``` block
aws-external-anthropic.amazonaws.com
```





Use only this published service principal name. Never trust an identifier provided over email, chat, or any onboarding channel.

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
      "Sid": "AllowClaudePlatformOnAWSCrypto",
      "Effect": "Allow",
      "Principal": {
        "Service": "aws-external-anthropic.amazonaws.com"
      },
      "Action": ["kms:Encrypt", "kms:Decrypt", "kms:GenerateDataKey"],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:anthropic:compartment_uuid": ["<COMPARTMENT_UUID>"]
        }
      }
    },
    {
      "Sid": "AllowClaudePlatformOnAWSDescribe",
      "Effect": "Allow",
      "Principal": {
        "Service": "aws-external-anthropic.amazonaws.com"
      },
      "Action": "kms:DescribeKey",
      "Resource": "*"
    }
  ]
}
```

The `EncryptionContext` condition is optional. It limits the key to the workspaces you list. To remove it, delete the `Condition` block from the `AllowClaudePlatformOnAWSCrypto` statement.

If you keep the condition, add each workspace's compartment ID before you attach the key to it. For a new workspace:

1.  Create the workspace without the key.
2.  Add its compartment ID to the policy.
3.  Attach the key.

If you add the condition later, list the compartment ID of every workspace the key is already attached to.

To limit the key policy further, see the [optional `aws:SourceArn` condition](#source-arn-condition).

Replace the placeholders:

- **`<AWS_ACCOUNT_ID>`:** your [AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console-account-id.html). To print it with the AWS CLI, run `aws sts get-caller-identity --query Account --output text`.
- **`<COMPARTMENT_UUID>`:** the compartment ID of the workspace you attach the key to



**Finding your compartment ID:** In the Claude Console, go to the [Data retention](playground.md) page (`platform.claude.com/settings/privacy`). Select the workspace from the dropdown menu at the top of the page. The ID is under **Encryption key**, in the **Compartment ID** field. You can also read the `compartment_id` field returned by the [Get Workspace](../Endpoints/organization-workspaces-retrieve.md) endpoint.

### Create the key

Create the key in the AWS account that hosts your Claude Platform on AWS organization, in the same region as the workspace.

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

**Optional:** To limit both service principal statements further, add an `aws:SourceArn` condition to each. The source ARN on every call is the [workspace's ARN](../Endpoints/claude-platform-on-aws-iam-actions.md#service-details), in the form `arn:aws:aws-external-anthropic:<REGION>:<AWS_ACCOUNT_ID>:workspace/<WORKSPACE_ID>`.

- **All workspaces in your AWS account:** `"ArnLike": {"aws:SourceArn": "arn:aws:aws-external-anthropic:*:<AWS_ACCOUNT_ID>:workspace/*"}`
- **Specific workspaces:** the same condition, with a list of full workspace ARNs instead of the wildcard

## Register the key with Anthropic

Sign in to the Claude Console through AWS with the Admin role.

1.  1

    ### Open the encryption key settings

    In the Claude Console, go to the [Data retention](playground.md#encryption-keys) page (`platform.claude.com/settings/privacy`). If you don't see **Encryption keys**, select **Organization** from the dropdown menu at the top of the page.

2.  2

    ### Add the key

    Under **Encryption keys**, click **Add key**. Enter a **Display name**.

3.  3

    ### Enter the key ARN

    Anthropic rejects alias ARNs and multi-Region keys.

    In **KMS key ARN**, paste the key ARN. If a list of keys appears instead, select your key, or click **Enter ARN manually** and paste the ARN. Click **Add**.

4.  4

    ### Attach the key to a workspace

    Attaching a key can't be undone. If you can, attach it to a new workspace before that workspace receives any requests. In a workspace that already receives requests, the key can take [up to a day to take effect](manage-claude-cmek.md#how-it-works).

    On the Data retention page, select the workspace from the dropdown menu at the top of the page. Under **Encryption key**, select the key and click **Save**.

5.  5

    ### Confirm the change

    Select the checkbox to confirm that you have read the CMEK documentation, then click **Confirm**.

Attaching validates the key. If it fails with a KMS access error, see [Troubleshoot validation](#troubleshoot-validation).

You can also select a key when you create a workspace in the Claude Console, if your key policy has no `EncryptionContext` condition.

To register and attach keys with the API instead, see [IAM actions](../Endpoints/claude-platform-on-aws-iam-actions.md#encryption-keys). The API identifies a key by its KMS key ARN.

## Troubleshoot validation

If validation fails, common causes are:

- **Key policy mismatch:** Make sure the key policy matches the one in [Prepare the key policy](#prepare-the-key-policy). To check the key policy, run `aws kms get-key-policy --region <REGION> --key-id <KEY_ARN> --policy-name default`.
- **Condition mismatch:** Make sure any `EncryptionContext` or `aws:SourceArn` condition includes this workspace.
- **Key state or location:** Confirm that the key is enabled, single-Region, and in the same AWS account and region as the workspace.
- **Missing permissions:** The principal you are signed in as needs `kms:DescribeKey`, `kms:Encrypt`, and `kms:Decrypt` on the key.
- **Organization policies:** Make sure no service control policy or resource control policy in your AWS organization blocks the service principal or your principal.

If attaching still fails, find the denied `kms:` event in CloudTrail in the key's account. It shows the calling principal and, for cryptographic calls, the encryption context. After you fix the cause, click **Save** again.

## Terraform

To create the key with Terraform, use the `aws_kms_key` and `aws_kms_alias` resources from the `aws` provider.
