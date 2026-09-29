---
title: "Customer-managed encryption keys - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/cmek"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:34Z"
tags: ["api"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fcmek)





SearchCtrlK

Organization

[Admin API](manage-claude-admin-api.md)[User management](manage-claude-user-management.md)[Workspaces](manage-claude-workspaces.md)

Authentication

[Overview](manage-claude-authentication.md)[Create an Admin API key](manage-claude-admin-api-keys.md)[App Attest](manage-claude-app-attest.md)[Workload Identity Federation](manage-claude-workload-identity-federation.md)[Manage WIF via API](manage-claude-wif-admin-api.md)[WIF reference](manage-claude-wif-reference.md)

Identity providers

Monitoring

[Usage and Cost API](manage-claude-usage-cost-api.md)[Rate Limits API](manage-claude-rate-limits-api.md)[Analytics APIs](manage-claude-analytics-api.md)[Claude Code Analytics API](manage-claude-claude-code-analytics-api.md)[Spend Limits API](manage-claude-spend-limits-api.md)

Data & compliance

[Data residency](../Guides/build-with-claude-data-residency.md)[API and data retention](manage-claude-api-and-data-retention.md)[Access Transparency](manage-claude-access-transparency.md)

[Encryption keys](manage-claude-cmek.md)

[Overview](manage-claude-cmek.md)[AWS KMS](manage-claude-cmek-aws-kms.md)[Google Cloud KMS](manage-claude-cmek-google-cloud-kms.md)[Azure Key Vault](manage-claude-cmek-azure-key-vault.md)

[Inference hooks](manage-claude-inference-hooks.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](usage-limits.md)

[Admin](manage-claude-admin-api.md)Encryption keys

# Customer-managed encryption keys

Copy page



Encrypt Claude workspace data at rest with a key you control.

Copy page



Learn more with the /claude-api skill in Claude Code



```python
claude "/claude-api tell me about customer-managed encryption keys"
```

A customer-managed encryption key (CMEK) lets you provision an encryption key in your own [AWS KMS](https://aws.amazon.com/kms/), [Google Cloud KMS](https://cloud.google.com/security/products/security-key-management), or [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault) and have Anthropic use it to encrypt certain workspace data at rest. You retain full control of the key, including rotation, audit, and revocation, and the key operations Anthropic performs against your key are recorded in your cloud provider's audit logs.

The use of CMEK is optional. Eligible organizations can **opt in** to use customer-managed encryption keys instead of the default encryption that Anthropic provides. To activate CMEK, contact your Anthropic account team.



**Enabling CMEK is permanent and can cause irreversible data loss**

Enabling CMEK is permanent. Anthropic keeps no copy of your key, so misconfiguration or key loss can permanently destroy your CMEK-protected data. If you are uncertain about any step, contact your Anthropic representative before applying changes.

- **Permanent data loss:** If your encryption key is deleted, scheduled for deletion, or has its key material destroyed, Anthropic cannot recover your data.
- **Identifier verification is mandatory:** Granting key access to an incorrect or spoofed principal can expose your data to an unauthorized party. Always verify the Anthropic identifier against the published production identities in each configuration guide. On Claude Platform on AWS, that identity is the AWS service principal published in the [AWS KMS guide](manage-claude-cmek-aws-kms.md#claude-platform-on-aws). Never trust an identifier provided over email, chat, or any onboarding channel.

## How it works

Only Organization Admins (on Claude Platform; the Admin role on Claude Platform on AWS) or Owners and the Primary Owner (on Claude Enterprise) can configure CMEK. On Claude Platform, CMEK is scoped per workspace and configured in the Claude Console or with the Admin API (on Claude Platform on AWS, in the Claude Console or through the IAM-authorized external key and workspace endpoints). On Claude Enterprise, CMEK is scoped per organization and configured in [claude.ai \> Organization settings \> Data and privacy](https://claude.ai/admin-settings/data-privacy-controls). On either product, CMEK protects data written after your key takes effect. Existing data (prior chats, files, and sessions) remains encrypted with Anthropic-managed keys and is not re-encrypted under your key.

On Claude Platform, Anthropic recommends attaching your key to a new workspace before you send any requests to that workspace. If you attach a key to a workspace that already receives requests, your key can take up to a day to take effect. Data written before then, like existing data, is encrypted with Anthropic-managed keys and is not re-encrypted.

CMEK configuration events appear in the [Compliance API Activity Feed](manage-claude-compliance-activity-feed.md). The key operations Anthropic performs against your key (such as wrapping and unwrapping data keys) do not appear in the Compliance API; they appear in your cloud provider's audit logs.

Anthropic calls your key management service from its standard public IP range. If you restrict access to your key management service by IP, allow the addresses listed in [IP addresses](../Endpoints/ip-addresses.md). On Claude Platform on AWS, don't rely on IP-based restrictions for your key; scope access with the key policy described in the [AWS KMS guide](manage-claude-cmek-aws-kms.md#claude-platform-on-aws) instead.

## Prerequisites

- Permissions to create encryption keys and manage key access in the account, project, or subscription that will host the encryption key.
- An Organization Admin role in the Claude Console on Claude Platform (the Admin role on Claude Platform on AWS), or an Owner or Primary Owner role on Claude Enterprise.
- Data retention configuration: CMEK is allowed with [Zero data retention (ZDR)](manage-claude-api-and-data-retention.md) for both Claude Platform and Claude Enterprise.

## Availability and regions

Except on Claude Platform on AWS (covered at the end of this section), CMEK is currently available in US regions only, and all encryption operations are processed in US regions. For minimal latency, choose a region close to Anthropic's US infrastructure:

| Provider     | Recommended regions         |
|:-------------|:----------------------------|
| AWS          | `us-east-2`                 |
| Google Cloud | `us-central1`, `us-east5`   |
| Azure        | `northcentralus`, `eastus2` |

On [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md), CMEK is available with AWS KMS keys only; Google Cloud KMS and Azure Key Vault keys cannot be registered. These region recommendations do not apply there: the key must be a single-region KMS key in the same AWS account and region as the workspace it is attached to, and its key policy must grant access to an AWS service principal rather than Anthropic's IAM role; see [Set up CMEK on Claude Platform on AWS](manage-claude-cmek-aws-kms.md#claude-platform-on-aws). Register and attach keys in the Claude Console; the external key endpoints are also available on Claude Platform on AWS, authorized through [IAM actions](../Endpoints/claude-platform-on-aws-iam-actions.md#encryption-keys). There is no separate validation step: the key is implicitly validated when you attach it to a workspace (the attach call performs an encrypt/decrypt round), so a key policy problem surfaces at attach time rather than at registration.

## What CMEK protects

What CMEK covers depends on which product you use.

### Encrypted with CMEK key

**Claude Platform**

- Message content, files and attachments (both inline attachments sent with a request and Files API uploads), and MCP and tool configuration.
- [Claude Managed Agents](managed-agents-overview.md) data, including agent configurations, environments, webhooks, sessions and their events, [memory stores](managed-agents-memory.md) and their memories and memory versions, and [dreams](managed-agents-dreams.md).

**Claude Enterprise**

- Chat content, including skills and plugins.
- Chat attachments and project attachments.
- Claude Code on the CLI, including message content.
- Cowork in Claude Desktop.
- Compliance API [local session transcripts](manage-claude-compliance-sessions.md#retrieve-local-sessions) captured from sessions on users' machines. If your key cannot be used, the messages endpoint returns [503 Service Unavailable](manage-claude-compliance-errors.md#local-sessions-temporarily-unavailable) instead of transcript content. Session metadata is still listed.
- Office agents.
- Claude in Chrome.
- Claude Science. Data that users send from the app to their own compute, such as SSH hosts or cloud compute accounts, is held on those systems, not by Anthropic, and is not covered.

On both products, backups and snapshots inherit the key.

### Disabled or modified

Some features are turned off or substantially modified when CMEK is enabled. This list is not exhaustive; review it with your team before enabling CMEK.

**Claude Platform**

- Playground in the Claude Console is disabled.
- Portions of the Compliance API that return raw content, such as prompts, responses, and files, are disabled.
- Other beta and research preview features might not be covered by CMEK.

**Claude Enterprise**

- Chat search is disabled because chat titles and content are encrypted under your key. Members cannot search past chats, and the **Search and reference chats** toggle stays off, so Claude cannot search them either.
- [Project knowledge search](../../15-Claude-AI-Features/retrieval-augmented-generation-rag-for-projects.md) (retrieval-augmented generation, or RAG) is disabled. Project knowledge loads directly into each conversation's context instead of being indexed and searched. As a result, a project can use substantially less knowledge than it could without CMEK. Knowledge beyond what can be loaded is left out of the conversation.
- Claude Code on the web (including routines) and Claude in Slack are unavailable: new sessions cannot be started and Claude in Slack declines requests, even if an admin turns these products on. Claude Code Desktop remains available for local sessions but is off unless an admin turns it on under [claude.ai \> Organization settings \> Claude Code](https://claude.ai/admin-settings/claude-code).
- In conversations and the **Artifacts** tab, Claude Design, Claude Slides, and Claude Docs are unavailable, and admins cannot turn them on. Claude Code cannot [publish artifacts](../../02-Claude-Code-CLI/artifacts.md#availability).
- Certain analytics are degraded: admin analytics for claude.ai skills and connectors (under claude.ai/analytics/usage and through the [Claude Enterprise Analytics API](manage-claude-analytics-api.md)), Claude smart reports (under claude.ai/analytics/insights), and Claude Code contribution metrics (under claude.ai/analytics/claude-code).
- Organization data exports and audit log exports, both under [claude.ai \> Organization settings \> Data and privacy](https://claude.ai/admin-settings/data-privacy-controls), are disabled.
- Response ratings (thumbs up and thumbs down on Claude's responses) are disabled.

### Encrypted with Anthropic key

These features remain available, but their data is not encrypted under your key. You can disable any feature that is not appropriate for your use case in **Settings**.

**Claude Platform**

- Data that is not at rest (such as cache) and data with a TTL shorter than 24 hours.
- Activity Feed, audit logs, and telemetry network traffic such as OTEL, so customers can maintain compliance even if a key is revoked.
- Claude Managed Agents [vault credential](managed-agents-vaults.md) values, such as OAuth tokens and client secrets. These are stored under Anthropic-managed encryption, are write-only, and are never returned in API responses.
- [User profiles](../Endpoints/http-beta-user-profiles.md): the `name`, `external_id`, and `metadata` fields are stored under Anthropic-managed encryption, not your key. Do not store sensitive personal data in profile `metadata`.

**Claude Enterprise**

- Beta and research preview features might not be covered by CMEK and can break in CMEK organizations, for example, Claude Security and the Claude Design app at claude.ai/design.
- [Personal preferences - Instructions for Claude section](https://claude.ai/new#settings/account) and Cowork Global instructions. These are set at the account level and shared across all of a user's organizations.

On both products, account data for users in your organization (such as names, email addresses, and profile pictures) is not encrypted under your key.

### Feature support

The following Claude Platform APIs and tools store data at rest under your key when CMEK is enabled:

| APIs                  | Tools and features                                                                                |
|:----------------------|:--------------------------------------------------------------------------------------------------|
| Messages              | Web search                                                                                        |
| Models                | Web fetch                                                                                         |
| Files                 | Code execution                                                                                    |
| Batch                 | Bash tool                                                                                         |
| Skills                | Text editor tool                                                                                  |
| Claude Managed Agents | MCP connector                                                                                     |
| Memory stores         | Structured outputs (not available for Claude Fable or Claude Mythos models in CMEK organizations) |
| Dreams                | Advisor tool                                                                                      |
|                       | Computer use                                                                                      |
|                       | Browser use                                                                                       |
|                       | Context management                                                                                |

## Limited preservation outside your key

In three narrow cases, Anthropic may preserve specific records under Anthropic-managed encryption:

- Where Anthropic is required by law to retain records (for example, material reported to NCMEC under 18 U.S.C. § 2258A).
- Exigent risk of serious harm (for example, CBRNE weapons development, offensive cyberattacks, or imminent threats of violence).
- Violations of Section D.4 of Anthropic's [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) or equivalent terms in a customer's other applicable agreement with Anthropic.

Outside of [CSAM screening](../../22-Safety-Policy/csam-detection-and-reporting.md), preservation requires a human reviewer's explicit decision and follows Anthropic's [retention policy for commercial data](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data). For every instance of preservation, a corresponding [Compliance API Activity Feed](manage-claude-compliance-activity-feed.md) event is generated with a reason code conveying the purpose of the preservation. See [CMEK content preservation](manage-claude-access-transparency.md#cmek-content-preservation) for details. Safety screening metadata (records derived from Anthropic's automated safety scans, such as pattern identifiers and match indicators, not conversation content) is retained under Anthropic-managed encryption and remains readable after key revocation.

## Limitations

- **Irreversible action:** Once a key is attached to a workspace, it cannot be detached or swapped. On Claude Platform, attaching a key also locks the workspace's data retention setting: you cannot turn off 30-day data retention for that workspace, and returning to zero data retention requires creating a new workspace and moving your traffic to it. Rotating the key material within the same key (for example, AWS KMS automatic rotation, a Cloud KMS rotation schedule, or an Azure Key Vault rotation policy) is supported transparently and requires no change in Anthropic. Switching to a *different* key requires creating a new workspace with the new key and migrating your data. Revoking or disabling the key makes all CMEK-protected data in that workspace permanently inaccessible, with no backout path.
- **No retroactive encryption:** CMEK only protects data written after your key takes effect (see [How it works](#how-it-works)).
- **Latency:** Operations that wrap or unwrap data keys make a round-trip to your key management service, which can add a small amount of latency to actions that read or write data at rest.
- **Revocation delay:** Key revocation can take up to 1 hour (the cache TTL). Requests already in flight during that window may continue to succeed.
- **KMS costs:** CMEK requires a key in a third-party key management service (AWS KMS, Google Cloud KMS, or Azure Key Vault), which might incur separate charges billed by your KMS provider.
- **Claude Code telemetry behind a gateway:** When Claude Code connects through an LLM gateway or proxy (a custom `ANTHROPIC_BASE_URL`), CMEK does not apply to Claude Code's operational telemetry. To turn this telemetry off, set the `DISABLE_TELEMETRY` environment variable to `1`, as described under [Telemetry services](../../13-Enterprise-Admin/data-usage.md#telemetry-services) in the Claude Code documentation.

## Configure your provider

Follow the guide for the key management service you use.

[AWS KMS](manage-claude-cmek-aws-kms.md)

Create an AWS KMS key with a key policy that grants Anthropic access, then register it.

[Google Cloud KMS](manage-claude-cmek-google-cloud-kms.md)

Create a Cloud KMS crypto key, grant Anthropic's service account access, then register it.

[Azure Key Vault](manage-claude-cmek-azure-key-vault.md)

Create an RSA key, grant the Anthropic service principal access, then register and validate it.
