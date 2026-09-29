---
title: "Configure AWS KMS for CMEK - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:33Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fcmek-aws-kms)





SearchCtrlK

Organization

[Admin API](/docs/en/manage-claude/admin-api)[User management](/docs/en/manage-claude/user-management)[Workspaces](/docs/en/manage-claude/workspaces)

Authentication

[Overview](/docs/en/manage-claude/authentication)[Create an Admin API key](/docs/en/manage-claude/admin-api-keys)[App Attest](/docs/en/manage-claude/app-attest)[Workload Identity Federation](/docs/en/manage-claude/workload-identity-federation)[Manage WIF via API](/docs/en/manage-claude/wif-admin-api)[WIF reference](/docs/en/manage-claude/wif-reference)

Identity providers

Monitoring

[Usage and Cost API](/docs/en/manage-claude/usage-cost-api)[Rate Limits API](/docs/en/manage-claude/rate-limits-api)[Analytics APIs](/docs/en/manage-claude/analytics-api)[Claude Code Analytics API](/docs/en/manage-claude/claude-code-analytics-api)[Spend Limits API](/docs/en/manage-claude/spend-limits-api)

Data & compliance

[Data residency](/docs/en/manage-claude/data-residency)[API and data retention](/docs/en/manage-claude/api-and-data-retention)[Access Transparency](/docs/en/manage-claude/access-transparency)

[Encryption keys](/docs/en/manage-claude/cmek)

[Overview](/docs/en/manage-claude/cmek)[AWS KMS](/docs/en/manage-claude/cmek-aws-kms)[Google Cloud KMS](/docs/en/manage-claude/cmek-google-cloud-kms)[Azure Key Vault](/docs/en/manage-claude/cmek-azure-key-vault)

[Inference hooks](/docs/en/manage-claude/inference-hooks)

Compliance API

[Overview](/docs/en/manage-claude/compliance-api)[Set up the Compliance API](/docs/en/manage-claude/compliance-api-access)[Activity Feed](/docs/en/manage-claude/compliance-activity-feed)[Chats, files, and projects](/docs/en/manage-claude/compliance-content-data)[Session transcripts](/docs/en/manage-claude/compliance-sessions)[Organizations, users, roles, groups, and settings](/docs/en/manage-claude/compliance-org-data)[Design your integration](/docs/en/manage-claude/compliance-integration-patterns)[Errors](/docs/en/manage-claude/compliance-errors)[FAQ](/docs/en/manage-claude/compliance-faq)

[Console](/)

[Admin](/docs/en/manage-claude/admin-api)Encryption keys

# Configure AWS KMS for CMEK

Copy page



Use AWS KMS to provide an encryption key for your organization.

Copy page



Configure with the /claude-api skill in Claude Code



```python
claude "/claude-api help me configure a customer-managed encryption key with AWS KMS"
```

This guide walks through configuring an [AWS KMS](https://aws.amazon.com/kms/) key as a [customer-managed encryption key (CMEK)](/docs/en/manage-claude/cmek) for your Anthropic organization.



Enabling CMEK is permanent. If your KMS key is deleted or disabled, Anthropic cannot recover the data encrypted under it. Review the [warnings and limitations](/docs/en/manage-claude/cmek) before you begin.



**Claude Platform on AWS:** On [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws), your key policy grants access to an AWS service principal instead of Anthropic's IAM role, there is no separate validation step, and you register and attach the key in the Claude Console. Follow [Set up CMEK on Claude Platform on AWS](#claude-platform-on-aws) on this page instead of the steps in the next sections.

## Prerequisites

- An AWS account with permissions to create KMS keys and set key policies (`kms:CreateKey` and `kms:PutKeyPolicy`).
- An Anthropic Admin API key for your organization.
- The [AWS CLI](https://aws.amazon.com/cli/) installed and authenticated.

## Amazon Resource Name (ARN) for Anthropic

To have Anthropic use your encryption key, you must give Anthropic's IAM role a KMS key it can use for encrypting data. The ARN for Anthropic CMEK is:

``` block
arn:aws:iam::915198916910:role/anthropic-cmek-client-us
```





Use only this published ARN. Never trust an identifier provided over email, chat, or any onboarding channel.

## Encryption key setup

1.  1

    ### Create the KMS key with a cross-account key policy

    
    **Claude Platform on AWS:** Skip this step. Your key policy grants access to an AWS service principal, and it has no organization condition. [Set up CMEK on Claude Platform on AWS](#claude-platform-on-aws) gives that policy.

    The key policy grants Anthropic's IAM role cross-account access. Three statements are required:

    1.  **Account root admin:** the standard KMS pattern. Your account retains full admin control.
    2.  **Anthropic encrypt and decrypt:** the `kms:Encrypt` and `kms:Decrypt` actions, which Anthropic uses to encrypt and decrypt the data keys that protect your workspace data (envelope encryption).
    3.  **Anthropic describe:** the metadata read Anthropic performs at startup. It is granted separately because `DescribeKey` has no `EncryptionContext` parameter, so an `EncryptionContext` condition on this action would always deny.

    To find [your AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console-account-id.html), run `aws sts get-caller-identity --query Account --output text`.

    In the policy, replace `<AWS_ACCOUNT_ID>` with your AWS account ID and `<ORGANIZATION_UUID>` with your organization ID. The `StringEquals` condition on `kms:EncryptionContext:anthropic:org_uuid` binds the key to your Anthropic organization, and validation refuses a key without it. To share one key among several Anthropic organizations, list each organization ID in the condition value.

    
    **Finding your organization ID:** Copy the **Organization ID** field under **Settings \> Organization** in the Claude Console, or under **Organization settings \> Organization** in claude.ai, or read the `id` field from the [Organization Info](/docs/en/api/beta/organization/retrieve) endpoint. Use the bare UUID, not the `org_`-prefixed ID.

    Save the policy as `key-policy.json`. To create the key in the AWS Console instead, paste the policy there, as described later in this step.

    key-policy.json

    

    ``` shiki
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

    
    **Optional:** To limit the key to some of your workspaces, use this `AllowAnthropicCMEKCrypto` statement instead of the one in the preceding policy JSON, with one compartment ID for each workspace. Add a workspace's compartment ID before you attach the key to it. For a new workspace, create it without the key, add its compartment ID, and then attach the key.

    ``` shiki
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

    ``` shiki
    aws kms create-key \
      --region <REGION> \
      --description "Anthropic CMEK" \
      --key-usage ENCRYPT_DECRYPT \
      --policy file://key-policy.json
    ```

    

    Capture `KeyMetadata.Arn` from the output. You need it when you register the key in the next step.

    
    If the key is already configured for CMEK and protects existing data, you must add a statement that lets Anthropic decrypt that data, in addition to the three statements in the preceding policy. In its condition, list the compartment ID of every workspace the key is or was attached to.

    ``` shiki
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

    Anthropic validates the key when you verify it or attach it to a workspace. Each validation adds four access-denied errors to CloudTrail. These are expected. If you need to filter them out, filter on all three of the following values. The first one alone isn't enough, because any caller can set it:

    - `requestParameters.encryptionContext.associatedData`: `Y21lay12YWxpZGF0aW9u`
    - `userIdentity.accountId`: `915198916910`
    - `resources.ARN`: `arn:aws:kms:<REGION>:<AWS_ACCOUNT_ID>:key/<KEY_ID>`

    
    **Finding your compartment ID:** See the **Claude Platform** tab under **Register the key with Anthropic**.

    You can also create the key from the AWS Console. Choose a symmetric key with the encrypt and decrypt key usage, a single-region key, and KMS key material origin. The Create-key wizard commits a key policy at its **Review** step: If you add Anthropic's account ID `915198916910` under key usage permissions there, the generated policy grants the whole Anthropic account broader actions (such as `kms:ReEncrypt*` and `kms:GenerateDataKey*`) with no `EncryptionContext` condition, and validation refuses it. To avoid leaving an over-permissive key, finish the wizard with administrative permissions only, then open the key's **Key policy** tab and replace the JSON with the `key-policy.json` policy shown earlier in this step.

## Register the key with Anthropic

How you register the key depends on which product you use.

Claude Platform

Claude Enterprise



**Claude Platform on AWS:** The principal, key policy, and registration flow differ, and there is no separate validation step. Follow [Set up CMEK on Claude Platform on AWS](#claude-platform-on-aws) instead of this tab.



**Finding your compartment ID:** Each workspace has a compartment ID that scopes its CMEK data. To find it in the Claude Console, go to [Manage \> Security](/settings/workspaces/default/security-compliance) and select the workspace in the workspace picker at the top of the sidebar. The ID is under **Encryption key**, in the **Compartment ID** field. You can also read the `compartment_id` field returned by the [Get Workspace](/docs/en/api/beta/organization/workspaces/retrieve) endpoint.

You can set up the key in the Claude Console or through the Admin API, with the same result.

Claude Console

API

1.  1

    ### Register the key with Anthropic

    In the Claude Console, open **Settings \> Encryption keys** and click **Add key**. Enter a display name, choose **AWS KMS**, and click **Continue**. Paste the key ARN into **KMS key ARN**, and click **Add**.

    The key details step shows your organization ID. Add it to the [key policy](#key-policy) before you click **Add**.

2.  2

    ### Validate the key

    On the **Encryption keys** page, click **Verify** next to the key. **Connected** appears when the check passes. If it fails, a message gives the reason.

3.  3

    ### Attach the key to a workspace

    In the Claude Console, go to [Manage \> Security](/settings/workspaces/default/security-compliance) and select the workspace in the workspace picker at the top of the sidebar. Under **Encryption key**, select the key, click **Save**, and confirm. Attaching a key can't be undone. For a workspace that already receives requests, the key can take [up to a day to take effect](/docs/en/manage-claude/cmek#how-it-works).

## Set up CMEK on Claude Platform on AWS

On [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws), CMEK uses AWS KMS keys only, and setup differs from the preceding sections in these ways:

- **Principal:** Your key policy grants access to the AWS service principal `aws-external-anthropic.amazonaws.com`. Anthropic's IAM role and account ID are not used, so the [ARN for Anthropic](#amazon-resource-name-arn-for-anthropic) does not apply.
- **Key requirements:** The key must be a symmetric KMS key with encrypt and decrypt usage, single-region, and in the same AWS account and region as the workspace you attach it to. Cross-account keys are not supported: the key must be in the AWS account that hosts your organization. Multi-region keys (key IDs that begin with `mrk-`) and alias ARNs are rejected when you register the key; use the key ARN.
- **No separate validation step:** Apart from those checks on the key ARN at registration, the key is validated when you attach it to a workspace. The attach call performs an encrypt/decrypt round against the key with that workspace's compartment ID as the encryption context, so a key policy problem surfaces at attach time rather than at registration. An `EncryptionContext` condition therefore needs no all-zeros entry.
- **Where you manage keys:** Register and attach keys in the Claude Console, signed in through AWS with the Admin role. The external key endpoints are also available on Claude Platform on AWS, authorized through [IAM actions](/docs/en/api/claude-platform-on-aws-iam-actions#encryption-keys); there, a key is identified by its KMS key ARN rather than an `ekey_` ID.



Use only this published service principal name. Never trust an identifier provided over email, chat, or any onboarding channel.

### Prerequisites

- The AWS account that hosts your Claude Platform on AWS organization, with permissions to create KMS keys and set key policies (`kms:CreateKey` and `kms:PutKeyPolicy`).
- The **Admin** role in the Claude Console for Claude Platform on AWS. See [Using the Claude Console](/docs/en/build-with-claude/claude-platform-on-aws#using-the-claude-console).
- For the IAM principal you sign in to the Claude Console with: besides `aws-external-anthropic:AssumeConsole`, the [IAM actions](/docs/en/api/claude-platform-on-aws-iam-actions#encryption-keys) for the operations you perform there, because the Encryption keys page and key attachment go through the AWS gateway. Registering a key is `RegisterKey` (with `ListKeys` and `GetKey` to view registrations), and attaching one is `UpdateWorkspace` or `CreateWorkspace`. The external key actions (and `CreateWorkspace`) are account-scoped, so grant them on `Resource: "*"`; a policy limited to workspace ARNs does not include them.
- For the IAM principal that attaches the key to a workspace (the identity you signed in to the Claude Console with): `kms:DescribeKey`, `kms:Encrypt`, and `kms:Decrypt` on the key. Your principal's access to the key is checked when you attach it, in addition to the service principal's.
- Optional, for the key picker in the Claude Console: `kms:ListKeys` and `kms:DescribeKey` for the principal you sign in with. Without them, paste the key ARN instead.

### Create the KMS key

The key policy has three statements: your account's root admin statement; a statement that lets the Claude Platform on AWS service principal encrypt, decrypt, and generate data keys; and a separate statement for `kms:DescribeKey`. The crypto statement carries an optional `EncryptionContext` condition that binds the key to the workspaces you list. `DescribeKey` is granted separately because it has no `EncryptionContext` parameter, so an `EncryptionContext` condition on that action would always deny.

If you plan to use the optional `EncryptionContext` condition shown here, create the workspace first (without a key), copy its compartment ID, and substitute it for `<compartment-uuid>`. To find the ID in the Claude Console, go to [Manage \> Security](/settings/workspaces/default/security-compliance) and select the workspace in the workspace picker at the top of the sidebar. The ID is under **Encryption key**, in the **Compartment ID** field. You can also read it from the `compartment_id` field returned by the [Get Workspace](/docs/en/api/beta/organization/workspaces/retrieve) endpoint. If you don't plan to use the condition, delete the `Condition` block from that statement.

```python
export YOUR_ACCOUNT=$(aws sts get-caller-identity --query Account --output text)

aws kms create-key \
  --region <workspace-region> \
  --description "Anthropic CMEK (Claude Platform on AWS)" \
  --key-usage ENCRYPT_DECRYPT \
  --policy "{
    \"Version\": \"2012-10-17\",
    \"Statement\": [
      {
        \"Sid\": \"AccountRootAdmin\",
        \"Effect\": \"Allow\",
        \"Principal\": {\"AWS\": \"arn:aws:iam::${YOUR_ACCOUNT}:root\"},
        \"Action\": \"kms:*\",
        \"Resource\": \"*\"
      },
      {
        \"Sid\": \"AllowClaudePlatformOnAWSCrypto\",
        \"Effect\": \"Allow\",
        \"Principal\": {\"Service\": \"aws-external-anthropic.amazonaws.com\"},
        \"Action\": [\"kms:Encrypt\", \"kms:Decrypt\", \"kms:GenerateDataKey\"],
        \"Resource\": \"*\",
        \"Condition\": {
          \"StringEquals\": {
            \"kms:EncryptionContext:anthropic:compartment_uuid\": [
              \"<compartment-uuid>\"
            ]
          }
        }
      },
      {
        \"Sid\": \"AllowClaudePlatformOnAWSDescribe\",
        \"Effect\": \"Allow\",
        \"Principal\": {\"Service\": \"aws-external-anthropic.amazonaws.com\"},
        \"Action\": \"kms:DescribeKey\",
        \"Resource\": \"*\"
      }
    ]
  }"
```



Capture `KeyMetadata.Arn` from the output. You need it when you register the key.

The `EncryptionContext` condition is optional. Every encrypt, decrypt, and data-key call made for a workspace, including the attach-time check, carries that workspace's compartment ID as `anthropic:compartment_uuid`, so the condition lists the compartment ID of each workspace you attach the key to and needs no all-zeros entry. Adding it binds the key to the workspaces you list at the IAM layer as well. Because a compartment ID exists only once its workspace exists, the order is: create the workspace, put its compartment ID in the condition (at key creation, or later with `kms:PutKeyPolicy`), then attach the key. Before attaching the key to each additional workspace, add that workspace's compartment ID the same way. To start without it, delete the `Condition` block from the `AllowClaudePlatformOnAWSCrypto` statement; if you add it later, include the compartment ID of every workspace the key is already attached to.

You can further restrict both service-principal statements with an `aws:SourceArn` condition. The service passes the [workspace's ARN](/docs/en/api/claude-platform-on-aws-iam-actions#service-details) (`arn:aws:aws-external-anthropic:<region>:<account-id>:workspace/<workspace-id>`) as the source ARN on every call it makes with your key, so `"ArnLike": {"aws:SourceArn": "arn:aws:aws-external-anthropic:*:<account-id>:workspace/*"}` limits the grant to workspaces in your own AWS account, and a list of full workspace ARNs limits it to those workspaces. This condition is not required; the `EncryptionContext` condition on its own binds the key to the workspaces you list.

You can also create the key from the AWS Console: choose a symmetric key with the encrypt and decrypt key usage, a single-region key, and KMS key material origin, in the workspace's region. Leave key usage permissions empty in the Create-key wizard, then open the key's **Key policy** tab and replace the JSON with the policy shown here.

### Register and attach the key

1.  1

    ### Register the key

    In the Claude Console, open **Settings \> Encryption keys** and click **Add key**. Enter a display name, then choose the key from the key picker or choose **Enter ARN manually** and paste the key ARN, and click **Add**. The key must be in the AWS account that hosts your organization; cross-account keys are not supported. The picker lists the enabled, customer-managed, symmetric, single-region keys in your account in one of your organization's regions; for a key the picker doesn't list, enter the ARN. It lists keys only if the principal you signed in with can call `kms:ListKeys` and `kms:DescribeKey`.

2.  2

    ### Attach the key to a workspace

    Attach the key to a new workspace before you send any requests to that workspace. For a workspace that already receives requests, the key can take [up to a day to take effect](/docs/en/manage-claude/cmek#how-it-works). In the Claude Console, go to [Manage \> Security](/settings/workspaces/default/security-compliance) and select the workspace in the workspace picker at the top of the sidebar. Under **Encryption key**, select the key, click **Save**, and confirm. You can also select a key when you create a workspace in the Claude Console, but only if your key policy does not yet name specific workspaces (no `EncryptionContext` condition), because the workspace's compartment ID is assigned at creation. Once attached, a workspace's key can't be changed.

    This is when the key is validated: the attach call checks your principal's access to the key and performs an encrypt/decrypt round against it with the workspace's compartment ID as the encryption context, so a problem with either the key policy or your principal's permissions surfaces as an error on that call. If the attach fails with a KMS access error, check the following:

    - The key policy names the `aws-external-anthropic.amazonaws.com` service principal and grants `kms:Encrypt`, `kms:Decrypt`, and `kms:GenerateDataKey`, plus `kms:DescribeKey` in a separate statement that has no `EncryptionContext` condition.
    - Any `EncryptionContext` condition includes this workspace's compartment ID, and any `aws:SourceArn` condition you added matches this workspace's ARN.
    - The key is enabled, single-region, and in the same AWS account and region as the workspace.
    - The principal you are signed in as has `kms:DescribeKey`, `kms:Encrypt`, and `kms:Decrypt` on the key.
    - No service control policy or resource control policy in your AWS organization prevents the service principal or your principal from using the key.
    - If the policy looks right and the attach still fails, find the denied `kms:` event in CloudTrail in the key's account (it shows the calling principal and, for cryptographic calls, the encryption context), then correct the condition with `kms:PutKeyPolicy` and retry.

## Terraform

For infrastructure-as-code deployments, the same steps map to the `aws` provider with the `aws_kms_key` and `aws_kms_alias` resources.
