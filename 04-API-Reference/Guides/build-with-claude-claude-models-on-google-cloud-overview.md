---
title: "Claude Models on Google Cloud - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/overview"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-16T06:26:13Z"
tags: ["api"]
---

# Claude Models on Google Cloud

Copy page



Compare Claude Models on Google Cloud (Anthropic managed) and Claude Models on Google Cloud (Google managed), and find out which one you use.

Copy page



You can use Claude through your Google Cloud project in two ways:

- **[Claude Models on Google Cloud (Anthropic managed)](build-with-claude-claude-models-on-google-cloud-anthropic-managed.md):** Anthropic operates the [Claude API](../Endpoints/overview.md).
- **[Claude Models on Google Cloud (Google managed)](build-with-claude-claude-models-on-google-cloud-google-managed.md):** Google operates Claude models as part of Google Cloud’s Agent Platform.

## How the two Google Cloud offerings differ

The following table compares Claude Models on Google Cloud (Anthropic managed) with Claude Models on Google Cloud (Google managed).

[TABLE]

## What both offerings share

- **Credentials:** Both offerings use Google Cloud credentials, including Application Default Credentials. You grant access to each offering separately, through its own IAM roles.
  - [Credentials for Claude Models on Google Cloud (Anthropic managed)](build-with-claude-claude-models-on-google-cloud-anthropic-managed.md#authentication)
  - [Credentials for Claude Models on Google Cloud (Google managed)](build-with-claude-claude-models-on-google-cloud-google-managed.md#before-making-api-calls)
- **Billing:** Charges for both offerings appear on your Google Cloud bill.
  - [Billing for Claude Models on Google Cloud (Anthropic managed)](build-with-claude-claude-models-on-google-cloud-anthropic-managed.md#billing)
  - [Billing for Claude Models on Google Cloud (Google managed)](build-with-claude-claude-models-on-google-cloud-google-managed.md#billing)
- **Model IDs:** Claude 4.6 and later models use their Claude API IDs on both offerings. See [Model IDs and versioning](../../20-Models/about-claude-models-model-ids-and-versions.md).
- **SDKs:** Anthropic’s [client SDKs](../Other/cli-sdks-libraries-overview.md) support both offerings.

## Moving between the two offerings

Follow the steps for whichever offering you’re moving to:

- [Steps for moving to Claude Models on Google Cloud (Anthropic managed)](build-with-claude-claude-models-on-google-cloud-anthropic-managed.md#migrating-from-google-managed)
- [Steps for moving to Claude Models on Google Cloud (Google managed)](build-with-claude-claude-models-on-google-cloud-google-managed.md#migrating-from-anthropic-managed)

## Which offering are you using?

The following table lists values that identify Claude Models on Google Cloud (Anthropic managed) and Claude Models on Google Cloud (Google managed). Find a value you already have. For example, look for the host in your request URLs or the SDK client in your code. The heading of that value’s column is your offering.

[TABLE]

If you call `api.anthropic.com` with an API key, you use neither offering. To move those calls to Claude Models on Google Cloud (Anthropic managed), see [Moving from an existing Anthropic organization](build-with-claude-claude-models-on-google-cloud-anthropic-managed.md#moving-from-an-existing-anthropic-organization).

## Next steps



[Claude Models on Google Cloud (Anthropic managed)](build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)

Set up your account and make your first request.



[Claude Models on Google Cloud (Google managed)](build-with-claude-claude-models-on-google-cloud-google-managed.md)

Install an SDK and make your first request.



[IAM permissions for Claude Models on Google Cloud (Anthropic managed)](../Endpoints/claude-models-on-google-cloud-anthropic-managed-iam-permissions.md)

Look up permissions, roles, and audit log types.
