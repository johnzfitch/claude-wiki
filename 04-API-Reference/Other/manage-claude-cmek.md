---
title: "Customer-managed encryption keys - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/cmek"
category: "04-API-Reference/Other"
fetched_at: "2026-11-13T06:34:04Z"
tags: ["api"]
---

# Customer-managed encryption keys

Copy page



Use a key you hold in your own cloud to encrypt data that Claude stores.

Copy page



Claude Code

Ask Claude Code about this feature

Run in

`❯``/claude-api`` tell me about customer-managed encryption keys`



With customer-managed encryption keys (CMEK), you create a key in your own AWS KMS, Google Cloud KMS, or Azure Key Vault. Anthropic uses it to encrypt certain data at rest. The key stays under your control, so you can rotate it, audit its use, and remove Anthropic’s access.

## Choose your setup page

Choose the service that holds your key. Claude Platform on AWS, which also uses AWS KMS, has its own page.

[AWS KMS](manage-claude-cmek-aws-kms.md)

For Claude Platform and Claude Enterprise.

[Google Cloud KMS](manage-claude-cmek-google-cloud-kms.md)

For Claude Platform and Claude Enterprise.

[Azure Key Vault](manage-claude-cmek-azure-key-vault.md)

For Claude Platform and Claude Enterprise.

[Claude Platform on AWS](manage-claude-cmek-claude-platform-on-aws.md)

For organizations whose Claude Console sidebar shows **Account managed by AWS**.

On Claude Platform, you can also add and attach your key [with the Admin API](manage-claude-cmek-admin-api.md).

## Understand CMEK before you set it up

Which product you use decides what your key encrypts, what stays under Anthropic’s key, and which features turn off or change.

[How CMEK works](manage-claude-cmek-how-it-works.md)

How your key protects data, when it takes effect, and what you can see.

[CMEK, data retention, and ZDR](manage-claude-cmek-data-retention.md)

Using a key with zero data retention (ZDR), and what Anthropic can preserve outside your key.

[What CMEK covers on Claude Platform](manage-claude-cmek-coverage-claude-platform.md)

Look up a feature or a kind of data.

[What CMEK covers on Claude Enterprise](manage-claude-cmek-coverage-claude-enterprise.md)

Look up a feature, and see what your users will notice.

## What you commit to

- Once you attach a key, you [can’t remove or replace it](manage-claude-cmek-key-lifecycle.md#what-each-action-does).
- Your key protects only data written [after it takes effect](manage-claude-cmek-how-it-works.md#when-your-key-takes-effect).
- If your key is deleted, Anthropic can’t recover the data it protects. [While the key is disabled](manage-claude-cmek-key-lifecycle.md#restore-access), Claude can’t read that data.
- On Claude Platform, a workspace with a key [must retain data](manage-claude-cmek-data-retention.md#data-retention).

## Who can use CMEK

CMEK is optional. To turn it on for an eligible organization, contact your Anthropic account team. You need one of these roles to set it up:

- Claude Platform: Organization Admin
- Claude Platform on AWS: Admin
- Claude Enterprise: Owner or Primary Owner

## After setup

- [What happens when you rotate, disable, or delete your encryption key](manage-claude-cmek-key-lifecycle.md)
- [Troubleshoot CMEK](manage-claude-cmek-troubleshooting.md)
