---
title: "Set up CMEK with AWS KMS - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms"
category: "04-API-Reference/Other"
fetched_at: "2026-11-05T06:37:02Z"
tags: ["api"]
---

# Set up CMEK with AWS KMS

Copy page



Create an AWS KMS key, give Anthropic access to it, and put it to use in Claude Platform or Claude Enterprise.

Copy page



Claude Code

Let Claude Code set up this feature for you

Run in

`❯``/claude-api`` help me configure a customer-managed encryption key with AWS KMS`



If your Claude Console sidebar shows **Account managed by AWS**, follow [Set up CMEK on Claude Platform on AWS](manage-claude-cmek-claude-platform-on-aws.md) instead.

## Before you start

In Claude:

- Customer-managed encryption keys (CMEK) are [turned on for your organization](manage-claude-cmek.md#availability).
- You have your Anthropic organization ID, the UUID without the `org_` prefix. Copy it from [Organization](playground.md) in the Claude Console, or from **Organization settings \> Organization and access** on claude.ai. Whoever creates the key needs it.
- You’re an Organization Admin on Claude Platform, or an Owner or Primary Owner on Claude Enterprise.
- On Claude Platform, you have a workspace that [retains data](manage-claude-cmek-data-retention.md#data-retention), ideally a new one, because [existing data stays under Anthropic’s key](manage-claude-cmek-how-it-works.md#when-your-key-takes-effect).
- On Claude Enterprise, you know [which features turn off or change](manage-claude-cmek-coverage-claude-enterprise.md#turned-off-or-changed).

In AWS:

- You can create AWS KMS keys and set their key policies (`kms:CreateKey` and `kms:PutKeyPolicy`).
- Any IP restriction on AWS KMS access allows [Anthropic’s outbound IP addresses](../Endpoints/ip-addresses.md#outbound-ip-addresses).

## In AWS: create the key

After a failed **Verify** or **Add**, see the [fixes for AWS KMS](manage-claude-cmek-troubleshooting.md#aws-kms).

### Write the key policy

This policy gives Anthropic’s IAM role access to your key. Use only the role ARN published on this page, never one sent by email or chat. Copy the policy into a text editor:

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

Replace `<AWS_ACCOUNT_ID>` with your [AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console-account-id.html) and `<ORGANIZATION_UUID>` with your [Anthropic organization ID](#prerequisites). Keep the `kms:EncryptionContext:anthropic:org_uuid` condition, or verification fails.

You can also [limit the key to specific workspaces](manage-claude-cmek-aws-kms-workspaces.md) by listing their compartment IDs. If you’re replacing the policy on a key that already protects Claude data, [add one more statement](manage-claude-cmek-troubleshooting.md#existing-data).

### Create the key

You can create the key in any AWS commercial region. For the lowest latency, use `us-east-2`.

To use a key you already have in AWS KMS, [replace its key policy](manage-claude-cmek-aws-kms-workspaces.md#replace-the-key-policy).

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

    Don’t select any key administrators. Your key policy already gives your AWS account full admin control. Click **Next**.

5.  5

    ### Define key usage permissions

    Don’t select any key users, and don’t add anything under **Other AWS accounts**. Your key policy already grants the access that’s needed. Click **Next**.

6.  6

    ### Edit key policy

    Click **Edit**. Replace the whole policy with your key policy, then click **Next**.

7.  7

    ### Review

    Click **Finish**.

8.  8

    ### Copy the key ARN

    In **Customer managed keys**, open the new key and copy its ARN. Whoever adds the key in Claude needs it.

AWS CLI

Save your key policy as `key-policy.json`, then create the key. Replace `<REGION>` with the key’s region.

```python
aws kms create-key \
  --region <REGION> \
  --description "Anthropic CMEK" \
  --key-usage ENCRYPT_DECRYPT \
  --policy file://key-policy.json
```



Copy `KeyMetadata.Arn` from the output. Whoever adds the key in Claude needs the ARN.

Each check of the key in Claude adds four expected access-denied errors to CloudTrail. You can [filter them out](manage-claude-cmek-troubleshooting.md#cloudtrail).

## In Claude: add and attach the key

To script this part on Claude Platform, [use the Admin API](manage-claude-cmek-admin-api.md) instead.

Claude Platform

Claude Enterprise

Claude Platform

1.  1

    ### Open the encryption key settings

    In the Claude Console, open [Encryption keys](playground.md#encryption-keys) on the Data retention page. If the section isn’t there, select **Organization** from the dropdown menu at the top.

2.  2

    ### Add the key

    Under **Encryption keys**, click **Add key**. Enter a **Display name**, select **AWS KMS**, and click **Continue**.

3.  3

    ### Enter the key ARN

    Check that your [key policy](#key-policy) contains the **Organization ID for the key policy** shown in the dialog box. Paste the key ARN into **KMS key ARN** and click **Add**.

4.  4

    ### Verify the key

    In the **Encryption keys** list, click **Verify** next to the key. **Connected** appears when the check passes. If **Connection failed** appears instead, see [Troubleshoot CMEK](manage-claude-cmek-troubleshooting.md).

5.  5

    ### Attach the key to a workspace

    
    Attaching a key [can’t be undone](manage-claude-cmek-key-lifecycle.md#what-each-action-does). You can’t remove it from the workspace or replace it. If the key is deleted, Anthropic can’t recover the data it protects.

    1.  At the top of the Data retention page, select the workspace from the dropdown menu.
    2.  Under **Encryption key**, select the key and click **Save**.
    3.  Select the checkbox to confirm that you have read the CMEK documentation, then click **Confirm**.

    You see **Workspace settings updated.** Once the key [takes effect](manage-claude-cmek-how-it-works.md#when-your-key-takes-effect), your cloud provider’s audit log shows Anthropic’s calls to the key.

    In a [ZDR organization](manage-claude-cmek-data-retention.md#zdr-organizations), after you select the workspace, select **Standard data retention** so that **Encryption key** appears. After you click **Save**, click **Accept** on the data retention terms.

Claude Enterprise

On Claude Enterprise, CMEK applies to the whole organization, and you can add only one key.



Adding a key [can’t be undone](manage-claude-cmek-key-lifecycle.md#what-each-action-does). You can’t remove it from the organization or replace it. If the key is deleted, Anthropic can’t recover the data it protects.

Adding the key [turns off or changes some features](manage-claude-cmek-coverage-claude-enterprise.md#turned-off-or-changed) for every user. To try CMEK first, use a separate organization.

1.  1

    ### Open the encryption key settings

    Go to [claude.ai \> Organization settings \> Data and privacy](https://claude.ai/admin-settings/data-privacy-controls) and find **Encryption keys**.

2.  2

    ### Add the key

    Click **Add key**. Enter a **Display name** and select **AWS KMS**. Select the checkbox to confirm that you have read the CMEK documentation, then click **Continue**.

3.  3

    ### Enter the key ARN

    Check that your [key policy](#key-policy) contains the **Organization ID for the key policy** shown in the dialog box. Paste the key ARN into **KMS key ARN** and click **Add**.

4.  4

    ### Confirm that the key was added

    The check can take up to 30 seconds. When **Encryption key configured.** appears, click **Done**. If **The encryption key couldn’t be added.** appears instead, [find the cause and retry](manage-claude-cmek-troubleshooting.md#claude-ai-add-fails).

    Your key protects data written from then on. Tell your users [which features changed](manage-claude-cmek-coverage-claude-enterprise.md#turned-off-or-changed).
