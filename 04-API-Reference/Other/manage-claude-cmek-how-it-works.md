---
title: "How CMEK works - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/cmek-how-it-works"
category: "04-API-Reference/Other"
fetched_at: "2026-11-17T06:24:40Z"
tags: ["api"]
---

# How CMEK works

Copy page



How your key protects stored data, what one key covers, when it takes effect, and what you can see.

Copy page



## Your key wraps the keys that encrypt your data

Anthropic encrypts your stored data with data keys. With customer-managed encryption keys (CMEK), your key encrypts, or wraps, those data keys. This is envelope encryption. To write or read data, Anthropic asks your key management service (KMS) to wrap or unwrap a data key.

Data keys cross between Anthropic and your cloud. Your key never leaves your KMS. Your data never goes to it.

Anthropic keeps no copy of your key, so without it, Claude [can’t read the data it protects](manage-claude-cmek-key-lifecycle.md).

## What one key protects

On Claude Platform and Claude Platform on AWS, a key protects a workspace, and one key can serve several. On Claude Enterprise, a key protects the whole organization, which can have only one key. [Which data your key protects](manage-claude-cmek.md#what-cmek-protects) depends on your product.

On Claude Platform and Claude Enterprise, your key carries your Anthropic organization ID, which ties the key to your organization. Depending on your KMS, the ID goes in a key policy condition, a label, or a tag. A key without the ID fails verification. A key shared between organizations carries each ID.

An AWS KMS key policy can [name workspaces](manage-claude-cmek-aws-kms-workspaces.md) by their compartment IDs. A compartment ID is the UUID Anthropic gives each workspace for encryption, not the workspace ID that starts with `wrkspc_`.

## Where your key lives

Your key lives in AWS KMS, Google Cloud KMS, or Azure Key Vault. Your provider might charge for it.

On Claude Platform and Claude Enterprise, Anthropic processes all encryption operations in US regions. Your key can be outside the US, at some cost in latency. [Each setup page](manage-claude-cmek.md#set-it-up) names the lowest-latency regions.

## When your key takes effect

Your key protects only data written after it takes effect. Existing data (prior chats, files, and sessions) stays under Anthropic’s key and isn’t re-encrypted.

On Claude Platform and Claude Platform on AWS, a key attached to a workspace before its first request takes effect with that request. In a workspace in use, your key can take up to a day to take effect, and data written meanwhile stays under Anthropic’s key. That’s why Anthropic recommends a new workspace.

## What you can see

Your cloud’s audit log can record every operation Anthropic performs with your key. Where you have to turn that logging on, your setup page lists it as a prerequisite. In AWS CloudTrail, some entries are [expected errors](manage-claude-cmek-troubleshooting.md#cloudtrail).

Changes to your CMEK configuration appear in the [Compliance API Activity Feed](manage-claude-compliance-activity-feed.md). Key operations don’t.

## Latency and standards

Each wrap or unwrap is a round trip to your KMS, which can add a little latency to reading and writing stored data. For cryptographic standards such as FIPS, see the CMEK whitepaper in the [Trust Center](https://trust.anthropic.com/resources).

Next, read [what each key action does](manage-claude-cmek-key-lifecycle.md#what-each-action-does).
