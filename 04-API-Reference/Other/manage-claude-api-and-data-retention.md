---
title: "API and data retention - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/api-and-data-retention"
category: "04-API-Reference/Other"
fetched_at: "2026-10-20T06:37:52Z"
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


[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fapi-and-data-retention)

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

[Inference hooks](manage-claude-inference-hooks.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](playground.md)

[Admin](manage-claude-admin-api.md)Data & compliance

# API and data retention

Copy page



Learn about how Anthropic's APIs and associated features retain data, including information about zero data retention (ZDR) and HIPAA-ready API access.

Copy page



This page covers the Claude API (`api.anthropic.com`), Claude Platform on AWS, and [Claude in Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md), where Anthropic is the data processor. On Amazon Bedrock and Google Cloud's Agent Platform, the cloud provider is the data processor; refer to those platforms' data retention and compliance documentation for their equivalent controls.

Anthropic offers two data handling arrangements for the Claude API: [zero data retention (ZDR)](#zero-data-retention-zdr-scope) and [HIPAA readiness](#hipaa-readiness). The [feature eligibility table](#feature-eligibility) lists which API features each arrangement covers. For Anthropic's standard retention policies outside these arrangements, see the [commercial data retention policy](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data) and the [consumer data retention policy](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data).

## How Anthropic approaches data retention

Different APIs and features have different storage needs. Where a feature does not require storage of customer prompts or responses, it may be eligible for ZDR. Where a feature necessarily requires storage, Anthropic designs for the smallest possible retention footprint under the following commitments:

- Retained data is never used for model training without your express permission.
- Only what is technically necessary for the feature to work is retained. Conversation content (your prompts and Claude's outputs) is not retained by default; the exception is [Covered Models](#model-specific-data-retention-requirements), which require 30-day retention.
- Retained data is purged on the shortest practical time to live (TTL), and Anthropic aims to give customers control over how long data is retained. What is held, and the retention duration where a specific TTL applies, is documented on each feature's page.

Several retention models sit outside the ZDR and HIPAA arrangements described on this page. Data accessible through the [Compliance API](manage-claude-compliance-api.md) follows its own retention model. The [Activity Feed](manage-claude-compliance-activity-feed.md) retains data for 6 years. Chat, file, and project content from claude.ai follows your organization's retention policy set in [claude.ai \> Organization settings \> Data and privacy](https://claude.ai/admin-settings/data-privacy-controls), unless a user deletes it sooner. [Local session transcripts](manage-claude-compliance-sessions.md#retrieve-local-sessions) (from sessions on users' machines, in apps such as Cowork and Claude Code) are stored for 6 years by default, or for your organization's custom conversation retention period when a finite one is set (the same claude.ai setting). [Remote session transcripts](manage-claude-compliance-sessions.md#retrieve-remote-sessions) (Cowork in the cloud) are retained for 6 years, unless a user deletes the session sooner. The Compliance API does not capture local sessions for which ZDR is in effect. For organizations with HIPAA readiness enabled, it captures Cowork and Claude Code local sessions only and stores their transcripts for 30 days.

## Zero data retention (ZDR)

Under a ZDR arrangement, Anthropic does not store customer prompts or responses at rest after the API response is returned. To request ZDR for your organization, contact the [Anthropic sales team](https://claude.com/contact-sales). ZDR is enabled per organization; each new organization requires ZDR to be enabled separately by your account team, and enablement does not automatically extend to other organizations under the same account.

### What ZDR covers

- **Claude Messages and Token Counting APIs:** ZDR applies to these endpoints for eligible features listed in the [feature eligibility table](#feature-eligibility). Features that ride on `/v1/messages` but are marked "No" in the table (such as code execution) are not covered.
- **Claude Code with API keys:** ZDR applies when Claude Code is used with API keys from a Commercial organization (an organization under Anthropic's Commercial Terms of Service, as distinct from a consumer Claude account). If metrics logging is enabled in Claude Code, productivity data such as usage statistics is exempted from ZDR and may be retained. Claude Code on Claude Enterprise is not covered by this arrangement and has a separate ZDR offering; see [What ZDR does not cover](#what-zdr-does-not-cover).
- **Claude Platform on AWS:** [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md) follows the same data retention policy as the first-party Claude API. ZDR is available on request; contact your Anthropic account representative to enable it.

### What ZDR does not cover

- **Claude Console:** Any usage in the Claude Console, including playground.
- **Claude Managed Agents:** Claude Managed Agents is a stateful resource; session transcripts persist until you delete them.
- **Claude consumer products:** Claude Free, Pro, and Max plans, including when customers on those plans use Claude's web, desktop, or mobile apps or Claude Code.
- **Claude Teams and Claude Enterprise product interfaces:** These interfaces are not ZDR-eligible. The one exception is Claude Code on Claude Enterprise, which has its own ZDR offering, separate from the ZDR arrangement described on this page. That offering is available only to qualified accounts on Claude Enterprise and requires separate enablement by Anthropic. See the [Claude Code ZDR documentation](../../02-Claude-Code-CLI/zero-data-retention.md), which applies to Claude Enterprise organizations only.
- **Claude for Excel:** Not currently ZDR-eligible.
- **Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, and Claude Mythos 5:** These models require 30-day data retention and are not available under ZDR unless expressly authorized by Anthropic. See [Model-specific data retention requirements](#model-specific-data-retention-requirements).
- **Third-party integrations:** Data processed by third-party websites, tools, or other integrations is not covered, though some may have similar offerings. Review each service's data handling practices.
- **Cross-Origin Resource Sharing (CORS):** CORS is not supported for organizations with ZDR arrangements. To make API calls from browser-based applications, route requests through a backend proxy server. See the [API security guidance](../Endpoints/overview.md) for proxy patterns and API-key handling.
- **Flagged content and legal holds:** See [Retention regardless of arrangement](#retention-regardless-of-arrangement).



For the most up-to-date information on which products and features are ZDR-eligible, refer to your contract terms or contact your Anthropic account representative.

## HIPAA readiness

The Claude API supports HIPAA-ready integrations for organizations that handle protected health information (PHI). With a signed BAA and a HIPAA-enabled organization, you can use supported API features to process PHI while supporting your organization's HIPAA compliance. Eligible organizations can review and execute the BAA and enable HIPAA readiness directly from the Claude Console. HIPAA readiness applies a broader set of privacy and security safeguards than ZDR (encryption, access controls, and audit logging that protect PHI throughout its lifecycle) rather than requiring immediate deletion. If your organization handles PHI, HIPAA readiness is the arrangement to use; you do not also need ZDR. See the [feature eligibility table](#feature-eligibility) for which features each arrangement covers.



This page covers HIPAA readiness for the Claude API. For the full HIPAA Implementation Guide covering Claude Enterprise and configuration requirements, see the [Anthropic Trust Center](https://trust.anthropic.com/resources).

### What HIPAA readiness covers

- **Claude API:** HIPAA readiness applies to the Claude API (`api.anthropic.com`) for eligible features listed in the [feature eligibility table](#feature-eligibility).

### What HIPAA readiness does not cover

- **Claude consumer products:** Claude Free, Pro, and Max plans.
- **Claude Console:** Usage through the Claude Console interface (enabling HIPAA readiness from Console settings is supported; processing PHI through the Console is not covered).
- **Partner-operated platforms:** Amazon Bedrock and Google Cloud's Agent Platform. Refer to those platforms' compliance documentation.
- **Claude Platform on AWS and Microsoft Foundry:** HIPAA readiness is not available on these platforms.
- **Third-party integrations:** Data processed by external tools or services connected to your application.
- **Claude Code:** Claude Code is not covered under HIPAA readiness.
- **Beta features:** Features in beta are generally not covered under the BAA unless explicitly listed as eligible in the [feature eligibility table](#feature-eligibility).
- **Flagged content and legal holds:** See [Retention regardless of arrangement](#retention-regardless-of-arrangement).

### PHI handling guidelines

Protected health information (PHI) includes any individually identifiable health information. In the context of the Claude API, PHI typically appears in message content (prompts and Claude's responses), attached files (images, PDFs), and file names or metadata associated with message content. The following fields are not expected to contain PHI under the BAA: workspace names, user information (name, email, phone number), billing data, and support tickets.

When using [structured outputs](../Guides/build-with-claude-structured-outputs.md) or tools with `strict: true`, the API compiles JSON schemas into grammars that are cached separately from message content. These cached schemas do not receive the same PHI protections as prompts and responses. **Do not include PHI in JSON schema definitions.** This restriction applies to schema property names, `enum` values, `const` values, and `pattern` regular expressions. Patient-specific information should appear only in message content, where it is protected under HIPAA safeguards.

### HIPAA error handling

Your signed BAA is the official source of truth for which features are covered. The API also enforces these restrictions automatically. When a HIPAA-enabled organization sends a request that includes a non-eligible feature, the API returns a `400` error to prevent accidental use of features not covered by your BAA:

```python
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "The requested features are not available for HIPAA-regulated organizations without Zero Data Retention: code_execution."
  }
}
```



The error message lists the non-eligible features detected in the request; remove them and retry. The phrase "without Zero Data Retention" is the API's own wording and does not change the resolution. Client-side tools whose Details column in the [feature eligibility table](#feature-eligibility) says they are not blocked are accepted but remain outside HIPAA readiness.

### Getting started with HIPAA readiness

There are two ways to set up HIPAA-ready API access. Most organizations can enable it directly in the Claude Console with Anthropic's standard BAA; organizations that require a negotiated BAA should work with their account team.

#### Enable in the Console (standard BAA)

1.  1

    ### Open your organization's data retention settings

    In the Claude Console, go to the [Data retention](playground.md) page (`platform.claude.com/settings/privacy`). Organization admins with the HIPAA management permission see a **HIPAA compliance** card there. If you don't see the card, select **Organization** from the dropdown menu at the top of the page. If your organization is eligible but you still don't see the option to enable, ask an organization admin to complete these steps.

2.  2

    ### Review and execute the BAA

    Download the Business Associate Agreement and the HIPAA Implementation Guide, then accept the agreement as an authorized legal representative of your organization. Each step becomes available after you download the prior document, and your enablement is bound to the exact BAA version you downloaded.

3.  3

    ### Enablement takes effect immediately

    HIPAA readiness controls are applied to your organization as soon as you accept. Once HIPAA readiness is enabled for your organization, the configuration is permanent and cannot be disabled by an administrator. The API automatically enforces feature restrictions, returning an error for requests that use non-eligible features. See [HIPAA error handling](#hipaa-error-handling) for the error and the client-side tool exception.

#### Contact sales (custom BAA)

If your organization requires a negotiated or custom BAA, or if self-serve enablement isn't available for your organization, contact the [Anthropic sales team](https://claude.com/contact-sales). Anthropic will execute the BAA and enable HIPAA readiness for your organization.

#### Build with eligible features

Whichever path you use, confirm which features are supported in the [feature eligibility table](#feature-eligibility) and review the [PHI handling guidelines](#phi-handling-guidelines) for features that restrict where PHI can appear. For detailed configuration and compliance requirements, refer to the [HIPAA Implementation Guide](https://trust.anthropic.com/resources).



HIPAA readiness is enforced at the organization level. If you need both HIPAA-ready and general-purpose API access, use separate organizations for each.

## Model-specific data retention requirements

Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, and Claude Mythos 5 are designated Covered Models (see the [Covered Models support article](https://support.claude.com/en/articles/15425695)) and require 30-day data retention; ZDR is therefore not available for any of them unless expressly authorized by Anthropic. On the Claude API, requests to Claude Fable 5 from an organization whose data retention configuration does not meet this requirement return a `400 invalid_request_error`:

```python
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "In order to access this model, your organization or workspace must have data retention enabled."
  }
}
```



The 30-day data retention requirement applies wherever Covered Models are offered. On the Claude API (including Claude Platform on AWS), Anthropic handles retained data. On Amazon Bedrock and Google Cloud's Agent Platform, retained data stays within your cloud provider's environment; review each platform's documentation for enablement steps.

### Enable 30-day retention for a workspace

Organizations with a ZDR arrangement can make these models available in a specific workspace by enabling 30-day retention for that workspace only. Other workspaces in the organization keep zero data retention. The Default Workspace always follows the organization's setting, so use another workspace.

1.  1

    ### Open the workspace's data retention settings

    In the Claude Console, go to the [Data retention](playground.md) page (`platform.claude.com/settings/privacy`) and select the workspace from the dropdown menu at the top of the page.

2.  2

    ### Turn on 30-day data retention

    Select **Standard data retention** (30-day retention) and click **Save**. A confirmation dialog box then asks you to review and accept the terms that apply to data retention for the workspace. Data retention turns on for the workspace only after you accept them.

3.  3

    ### Verify

    Requests to Covered Models from this workspace now succeed. Workspaces without an override continue to follow the organization default.

## Feature eligibility

The following table lists which Claude API features are eligible for ZDR and HIPAA readiness arrangements.

Each eligibility column uses three values:

- **Yes:** The feature is fully eligible under the arrangement. For ZDR, "Yes" also assumes you are using a model that does not require 30-day data retention; [Covered Models](#model-specific-data-retention-requirements) are not available under ZDR regardless of feature eligibility.
- **Yes (qualified):** Your prompts and Claude's outputs are not stored, but a bounded technical artifact (named in the Details column) is retained briefly for the feature to function. See [How Anthropic approaches data retention](#how-anthropic-approaches-data-retention) for the commitments that govern these features.
- **No:** The feature is not eligible. Under HIPAA readiness, the API blocks requests that include a "No" feature and returns a `400` error, unless the feature's Details column says otherwise. Under ZDR, the API does **not** block these features; using one is a choice to step outside your ZDR arrangement for that specific data, and the feature's own documented retention policy applies. Features marked "No" for ZDR are typically stateful (they store jobs, files, or container state), which is why they cannot be zero-retention.

[TABLE]

## Retention regardless of arrangement

Even with ZDR or HIPAA arrangements in place, Anthropic may retain data where required by law or where it has been flagged by Anthropic's automated trust and safety systems. As a result, if a chat or session is flagged, Anthropic may retain inputs and outputs for up to 2 years.

## Frequently asked questions

### How do I know if my organization has ZDR arrangements?

Check your contract terms or contact your Anthropic account representative to confirm whether your organization has ZDR arrangements in place.

### Can I use ZDR-eligible (qualified) features under my ZDR arrangement?

Yes. These features retain a minimal, documented set of technical data, not your prompts or Claude's outputs. See the [feature eligibility table](#feature-eligibility) legend for what "Yes (qualified)" means and [How Anthropic approaches data retention](#how-anthropic-approaches-data-retention) for the commitments that govern these features.

### What happens if I use a feature marked "No" under ZDR?

Nothing blocks the request. Features marked "No" for ZDR are fundamentally stateful: the Batch API stores your jobs, the Files API stores your files, and code execution runs in persistent containers. Data for these features is retained per the feature's documented policy. Using them is a choice to step outside your ZDR arrangement for that specific data.

### Can I request deletion of data from features that are not ZDR-eligible?

Contact your Anthropic account representative to discuss deletion options for non-ZDR features.

### How does HIPAA readiness differ from ZDR?

ZDR prevents customer data from being stored at rest after the API response is returned. HIPAA readiness involves a broader set of privacy and security safeguards that protect PHI throughout its lifecycle, including encryption, access controls, and audit logging. Under HIPAA readiness, data can be retained with these safeguards in place rather than requiring immediate deletion. The two arrangements cover different feature sets; see the [feature eligibility table](#feature-eligibility).

### Do I still need ZDR if I have HIPAA readiness?

No. HIPAA-ready API access is designed as an alternative to ZDR for organizations handling PHI. With HIPAA readiness enabled, you get access to supported API features while maintaining the privacy and security protections that HIPAA requires.

### What happens if I use a non-eligible feature under HIPAA?

The API returns a `400` error with an `invalid_request_error` type, except for the client-side tools whose Details column in the [feature eligibility table](#feature-eligibility) says they are not blocked (those are accepted but remain outside HIPAA readiness). The error message identifies which features are not available. Remove those features from your request and retry. See [HIPAA error handling](#hipaa-error-handling).

### Can I use the same organization for HIPAA and non-HIPAA workloads?

No. HIPAA readiness is enforced at the organization level and automatically blocks non-eligible features (client-side tools noted in the table's Details column are the exception: they are not blocked, but they are still outside HIPAA readiness). Use a separate organization for workloads that do not require HIPAA readiness.

### How do I request HIPAA-ready API access?

Eligible organizations can enable HIPAA readiness directly on the [Data retention](playground.md) page (`platform.claude.com/settings/privacy`) in the Claude Console by reviewing and executing Anthropic's standard BAA; see [Getting started with HIPAA readiness](#getting-started-with-hipaa-readiness). If your organization requires a negotiated BAA, or self-serve enablement isn't available for your organization, contact the [Anthropic sales team](https://claude.com/contact-sales).

### Does this apply to Amazon Bedrock or Google Cloud?

No. The ZDR and HIPAA arrangements described on this page apply to the Claude API, where Anthropic is the data processor. On Bedrock and Google Cloud, the cloud provider is the data processor; refer to those platforms' data retention and compliance policies for their equivalent controls.

### Is Claude Platform on AWS eligible for ZDR or HIPAA readiness?

Claude Platform on AWS follows the same data retention policy as the first-party Claude API. ZDR is available on request; contact your Anthropic account representative to enable it. HIPAA readiness is not available on Claude Platform on AWS. See [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md) for details.

### Is Claude Code eligible for ZDR?

Claude Code is eligible for ZDR under two separate offerings:

- **API keys:** Claude Code used with pay-as-you-go API keys from a Commercial organization is covered when that organization has a ZDR arrangement for the Claude API, which this page describes.
- **Claude Enterprise:** Claude Code used through Claude Enterprise is covered by a separate offering, ZDR for Claude Code on Claude Enterprise, when Anthropic has enabled it for the organization.

ZDR is enabled on a per-organization basis. Each new organization requires ZDR to be enabled separately by your account team. ZDR does not automatically apply to new organizations created under the same account.

Additionally, if you have metrics logging enabled in Claude Code, productivity data (such as usage statistics) is exempted from ZDR and may be retained.

For full details on ZDR for Claude Code on Claude Enterprise, including disabled features and how to request enablement, see the [Claude Code ZDR documentation](../../02-Claude-Code-CLI/zero-data-retention.md). That documentation applies to Claude Enterprise organizations only and does not describe the ZDR arrangement for the Claude API.

### Does Claude for Excel support ZDR?

No, Claude for Excel is not currently ZDR-eligible.

### How do I request ZDR?

To request a ZDR arrangement, contact the [Anthropic sales team](https://claude.com/contact-sales).

## Related resources

- [Privacy Policy](https://www.anthropic.com/legal/privacy)
- [Structured outputs](../Guides/build-with-claude-structured-outputs.md)
- [Prompt caching](../Guides/build-with-claude-prompt-caching.md)
- [Batch processing](../Guides/build-with-claude-batch-processing.md)
- [Files API reference](../Endpoints/files-upload.md)
- [Trust Center](https://trust.anthropic.com/resources)
