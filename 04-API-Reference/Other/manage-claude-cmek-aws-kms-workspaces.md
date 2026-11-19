---
title: "Limit an AWS KMS key to specific workspaces - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/cmek-aws-kms-workspaces"
category: "04-API-Reference/Other"
fetched_at: "2026-11-17T06:24:58Z"
tags: ["api"]
---

# Limit an AWS KMS key to specific workspaces

Copy page



Add a key policy condition that names the workspaces allowed to use your AWS KMS key.

Copy page



The [key policy from setup](manage-claude-cmek-aws-kms.md#key-policy) lets every workspace in your organization use the key. With this optional condition, a workspace that isn’t listed can’t use it.

Add a workspace’s [compartment ID](manage-claude-cmek-how-it-works.md#what-one-key-protects) to the policy before you [attach the key](manage-claude-cmek-aws-kms.md#register-the-key-with-anthropic) to that workspace. For a new workspace, that means creating it without the key.

## Copy the workspace’s compartment ID

In the Claude Console, open the [Data retention](playground.md) page and select the workspace from the dropdown menu at the top. Copy the **Compartment ID** under **Encryption key**. The [Get Workspace](../Endpoints/organization-workspaces-retrieve.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. endpoint returns it as `compartment_id`.

A Claude Enterprise organization has one compartment ID. Copy it from your key under **Encryption keys** in [claude.ai \> Organization settings \> Data and privacy](https://claude.ai/admin-settings/data-privacy-controls).

## Add the condition to the key policy

Replace the `AllowAnthropicCMEKCrypto` statement with this one. Fill in your Anthropic organization ID and the compartment ID of every workspace that uses the key. A key that already protects data [needs one more statement](manage-claude-cmek-troubleshooting.md#existing-data).

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

## Replace the key policy on an existing key

1.  In the [AWS KMS console](https://console.aws.amazon.com/kms), open the key and click the **Key policy** tab.
2.  If you see **Switch to policy view**, click it.
3.  Click **Edit**.
4.  Replace the JSON with your key policy.
5.  Click **Save changes**.
