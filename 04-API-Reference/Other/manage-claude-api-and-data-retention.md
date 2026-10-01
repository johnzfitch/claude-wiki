---
title: "API and data retention - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/api-and-data-retention"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:33Z"
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fapi-and-data-retention)

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

[Inference hooks](manage-claude-inference-hooks.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](usage-limits.md)

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

Several retention models sit outside the ZDR and HIPAA arrangements described on this page. Data accessible through the [Compliance API](manage-claude-compliance-api.md) follows its own retention model. The [Activity Feed](manage-claude-compliance-activity-feed.md) retains data for 6 years. Chat, file, and project content from claude.ai follows your organization's retention policy set in [claude.ai \> Organization settings \> Data and privacy](https://claude.ai/admin-settings/data-privacy-controls), unless a user deletes it sooner. [Local session transcripts](manage-claude-compliance-sessions.md#retrieve-local-sessions) (from sessions on users' machines, in apps such as Cowork and Claude Code) are stored for 6 years by default, or for your organization's custom conversation retention period when a finite one is set (the same claude.ai setting). [Remote session transcripts](manage-claude-compliance-sessions.md#retrieve-remote-sessions) (Cowork in the cloud) are retained for 6 years, unless a user deletes the session sooner. The Compliance API does not capture local sessions for which ZDR is in effect, or any local sessions from organizations with HIPAA readiness enabled.

## Zero data retention (ZDR)

Under a ZDR arrangement, Anthropic does not store customer prompts or responses at rest after the API response is returned. To request ZDR for your organization, contact the [Anthropic sales team](https://claude.com/contact-sales). ZDR is enabled per organization; each new organization requires ZDR to be enabled separately by your account team, and enablement does not automatically extend to other organizations under the same account.

### What ZDR covers

- **Claude Messages and Token Counting APIs:** ZDR applies to these endpoints for eligible features listed in the [feature eligibility table](#feature-eligibility). Features that ride on `/v1/messages` but are marked "No" in the table (such as code execution) are not covered.
- **Claude Code:** ZDR applies when Claude Code is used with API keys from a Commercial organization (an organization under Anthropic's Commercial Terms of Service, as distinct from a consumer Claude account) or through Claude Enterprise with ZDR enabled. If metrics logging is enabled in Claude Code, productivity data such as usage statistics is exempted from ZDR and may be retained. See the [Claude Code ZDR documentation](https://platform.claude.com/docs/22-Safety-Policy/zero-data-retention-claude-code-docs-6ec9ee63f1.md) for full details.
- **Claude Platform on AWS:** [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md) follows the same data retention policy as the first-party Claude API. ZDR is available on request; contact your Anthropic account representative to enable it.

### What ZDR does not cover

- **Claude Console:** Any usage in the Claude Console, including playground.
- **Claude Managed Agents:** Claude Managed Agents is a stateful resource; session transcripts persist until you delete them.
- **Claude consumer products:** Claude Free, Pro, and Max plans, including when customers on those plans use Claude's web, desktop, or mobile apps or Claude Code.
- **Claude Teams and Claude Enterprise product interfaces:** These interfaces are not ZDR-eligible. The exception is Claude Code used through Claude Enterprise with ZDR enabled; see [What ZDR covers](#what-zdr-covers).
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

    ### Open your organization's privacy settings

    In [Claude Console \> Settings \> Privacy](usage-limits.md), organization admins with the HIPAA management permission see a **HIPAA compliance** card. If your organization is eligible but you don't see the option to enable, ask an organization admin to complete these steps.

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

Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, and Claude Mythos 5 are designated Covered Models (see the [Covered Models support article](../../15-Claude-AI-Features/covered-models-claude-help-center.md)) and require 30-day data retention; ZDR is therefore not available for any of them unless expressly authorized by Anthropic. On the Claude API, requests to Claude Fable 5 from an organization whose data retention configuration does not meet this requirement return a `400 invalid_request_error`:

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

Organizations with a ZDR arrangement can make these models available in a specific workspace by enabling 30-day retention for that workspace only. Other workspaces in the organization keep zero data retention.

1.  1

    ### Open the workspace's privacy controls

    In [Claude Console \> Settings \> Workspaces](usage-limits.md), select the workspace and open its **Privacy controls** tab.

2.  2

    ### Turn on 30-day data retention

    Enable the 30-day data retention setting for the workspace.

3.  3

    ### Verify

    Requests to Covered Models from this workspace now succeed. Workspaces without an override continue to follow the organization default.

## Feature eligibility

The following table lists which Claude API features are eligible for ZDR and HIPAA readiness arrangements.

Each eligibility column uses three values:

- **Yes:** The feature is fully eligible under the arrangement. For ZDR, "Yes" also assumes you are using a model that does not require 30-day data retention; [Covered Models](#model-specific-data-retention-requirements) are not available under ZDR regardless of feature eligibility.
- **Yes (qualified):** Your prompts and Claude's outputs are not stored, but a bounded technical artifact (named in the Details column) is retained briefly for the feature to function. See [How Anthropic approaches data retention](#how-anthropic-approaches-data-retention) for the commitments that govern these features.
- **No:** The feature is not eligible. Under HIPAA readiness, the API blocks requests that include a "No" feature and returns a `400` error, unless the feature's Details column says otherwise. Under ZDR, the API does **not** block these features; using one is a choice to step outside your ZDR arrangement for that specific data, and the feature's own documented retention policy applies. Features marked "No" for ZDR are typically stateful (they store jobs, files, or container state), which is why they cannot be zero-retention.

| Feature                                                                                         | Endpoint                                         | ZDR eligible    | HIPAA eligible | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------|-----------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [1M token context window](../Guides/build-with-claude-context-windows.md)                           | `/v1/messages`                                   | Yes             | Yes            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Adaptive thinking](../Guides/build-with-claude-thinking.md)                                        | `/v1/messages`                                   | Yes             | Yes            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md)                                 | `/v1/messages` (with `advisor` tool)             | Yes             | No             | Advisor model output is returned in the API response; nothing is stored server-side after the response.                                                                                                                                                                                                                                                                                                                                                                            |
| [Agent skills](../Agents-Tools/agents-and-tools-agent-skills-overview.md)                                 | `/v1/messages` (with `skills`) / `/v1/skills`    | No              | No             | Skill data retained per standard policy. See [Agent skills](../Agents-Tools/agents-and-tools-agent-skills-overview.md#data-retention).                                                                                                                                                                                                                                                                                                                                                       |
| [Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md)                                       | `/v1/messages` (with `bash` tool)                | Yes             | Yes            | Client-side tool executed in your environment.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Batch processing](../Guides/build-with-claude-batch-processing.md)                                 | `/v1/messages/batches`                           | No              | No             | 29-day retention; async storage required. See [Batch processing](../Guides/build-with-claude-batch-processing.md#data-retention).                                                                                                                                                                                                                                                                                                                                                      |
| [Browser use](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md)                              | `/v1/messages` (with `browser` toolset)          | Yes             | No             | Client-side tool. Anthropic does not run browser actions or retain page content beyond standard API handling. Not covered under HIPAA readiness; requests that include the browser use tool are not blocked. See [Browser use](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md#data-retention).                                                                                                                                                                                |
| [Cache diagnostics](../Guides/build-with-claude-cache-diagnostics.md)                               | `/v1/messages` (with `diagnostics`)              | Yes (qualified) | No             | Your prompts and Claude's outputs are not stored. A fingerprint of cryptographic hashes and token-count estimates is retained briefly to enable comparison against the next request. See [Cache diagnostics](../Guides/build-with-claude-cache-diagnostics.md#data-retention).                                                                                                                                                                                                         |
| [Citations](../Guides/build-with-claude-citations.md)                                               | `/v1/messages`                                   | Yes             | Yes            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Claude Managed Agents](managed-agents-overview.md)                                       | `/v1/agents`, `/v1/sessions`, `/v1/environments` | No              | No             | Sessions are stateful resources; transcripts persist until you delete them. Applies to all Managed Agents sub-features, including [Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md).                                                                                                                                                                                                                                                                          |
| [Code execution](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md)                        | `/v1/messages` (with `code_execution` tool)      | No              | No             | Container data retained up to 30 days. See [Code execution](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md#data-retention).                                                                                                                                                                                                                                                                                                                                                |
| [Computer use](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md)                            | `/v1/messages` (with `computer` toolset or tool) | Yes             | Yes            | Client-side tool where screenshots and files are captured and stored in your environment, not by Anthropic. See [Computer use](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#data-retention).                                                                                                                                                                                                                                                                               |
| [Context editing](../Guides/build-with-claude-context-editing.md)                                   | `/v1/messages` (with `context_management`)       | Yes             | No             | Context edits (tool use clearing and thinking clearing) are applied in real time.                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Context management (compaction)](../Guides/build-with-claude-compaction-threshold.md)              | `/v1/messages` (with `context_management`)       | Yes             | No             | Server-side compaction results are returned and round-tripped statelessly through the API response.                                                                                                                                                                                                                                                                                                                                                                                |
| [Data residency](../Guides/build-with-claude-data-residency.md)                                         | `/v1/messages` (with `inference_geo`)            | Yes             | Yes            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Effort](../Guides/build-with-claude-effort.md)                                                     | `/v1/messages` (with `effort`)                   | Yes             | Yes            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Fast mode](../Guides/build-with-claude-fast-mode.md)                                               | `/v1/messages` (with `speed: "fast"`)            | Yes             | Yes            | Same Messages API endpoint with faster inference. ZDR applies regardless of speed setting.                                                                                                                                                                                                                                                                                                                                                                                         |
| [Files API](../Guides/build-with-claude-files.md)                                                   | `/v1/files`                                      | No              | No             | Files retained until explicitly deleted or they reach their configured expiration. See [Files API](../Guides/build-with-claude-files.md#data-retention).                                                                                                                                                                                                                                                                                                                               |
| [Fine-grained tool streaming](../Agents-Tools/agents-and-tools-tool-use-fine-grained-tool-streaming.md)   | `/v1/messages`                                   | Yes             | Yes            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md)                                        | `/v1/messages` (with `mcp_servers`)              | No              | No             | Data retained per standard policy. See [MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md#data-retention).                                                                                                                                                                                                                                                                                                                                                                    |
| [MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)                                   | `/v1/tunnels`                                    | No              | No             | Research preview. See [MCP tunnels security](../Agents-Tools/agents-and-tools-mcp-tunnels-security.md) for the data-flow boundary and subprocessor details.                                                                                                                                                                                                                                                                                                                                  |
| [Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md)                                   | `/v1/messages` (with `memory` tool)              | Yes             | Yes            | Client-side memory storage where you control data retention.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Messages API](../Guides/build-with-claude-working-with-messages.md)                                | `/v1/messages`                                   | Yes             | Yes            | Standard API calls for generating Claude responses.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Mid-conversation system messages](../Guides/build-with-claude-mid-conversation-system-messages.md) | `/v1/messages` (with `role: "system"` messages)  | Yes             | Yes            | Request-shape capability of the Messages API; mid-conversation system messages flow through the standard inference path and nothing is stored server-side after the response.                                                                                                                                                                                                                                                                                                      |
| [PDF support](../Guides/build-with-claude-pdf-support.md)                                           | `/v1/messages`                                   | Yes             | Yes            | HIPAA eligibility applies to PDFs sent inline through the Messages API, not through the Files API.                                                                                                                                                                                                                                                                                                                                                                                 |
| [Programmatic tool calling](../Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md)       | `/v1/messages` (with `code_execution` tool)      | No              | No             | Built on code execution containers; data retained up to 30 days. See [Programmatic tool calling](../Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md#data-retention).                                                                                                                                                                                                                                                                                                     |
| [Prompt caching](../Guides/build-with-claude-prompt-caching.md)                                     | `/v1/messages`                                   | Yes             | Yes            | Your prompts and Claude's outputs are not stored. KV cache representations and cryptographic hashes are held in memory for the cache TTL and promptly deleted after expiry. See [Prompt caching](../Guides/build-with-claude-prompt-caching.md#data-retention).                                                                                                                                                                                                                        |
| [Search results](../Guides/build-with-claude-search-results.md)                                     | `/v1/messages` (with `search_results` source)    | Yes             | Yes            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Structured outputs](../Guides/build-with-claude-structured-outputs.md)                             | `/v1/messages`                                   | Yes (qualified) | Yes            | Your prompts and Claude's outputs are not stored. Only the JSON schema is cached, for up to 24 hours since last use. This also covers [strict tool use](../Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md) (`strict: true` on tools), which uses the same grammar pipeline. PHI must not be included in JSON schema definitions; see [PHI handling guidelines](#phi-handling-guidelines). See [Structured outputs](../Guides/build-with-claude-structured-outputs.md#data-retention). |
| [Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md)                         | `/v1/messages` (with `text_editor` tool)         | Yes             | Yes            | Client-side tool executed in your environment.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Thinking](../Guides/build-with-claude-thinking.md)                                                 | `/v1/messages` (with `thinking`)                 | Yes             | Yes            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Token counting](../Guides/build-with-claude-token-counting.md)                                     | `/v1/messages/count_tokens`                      | Yes             | Yes            | Count tokens before sending requests.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Tool search](../Agents-Tools/agents-and-tools-tool-use-tool-search-tool.md)                              | `/v1/messages` (with `tool_search` tool)         | Yes             | No             | Server-side tool executed by Anthropic; the tool definitions in the request are searched in memory per call and nothing is stored after the response.                                                                                                                                                                                                                                                                                                                              |
| [Web fetch](../Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md)                                  | `/v1/messages` (with `web_fetch` tool)           | Yes             | No             | Fetched web content returned in the API response. [Dynamic filtering](../Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md#dynamic-filtering) is not eligible for ZDR or HIPAA. Website publishers may retain request data (such as fetched URLs and request metadata) according to their own policies.                                                                                                                                                                               |
| [Web search](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md)                                | `/v1/messages` (with `web_search` tool)          | Yes             | Yes            | Real-time web search results returned in the API response. [Dynamic filtering](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md#dynamic-filtering) is not eligible for ZDR or HIPAA.                                                                                                                                                                                                                                                                                             |

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

Eligible organizations can enable HIPAA readiness directly in [Claude Console \> Settings \> Privacy](usage-limits.md) by reviewing and executing Anthropic's standard BAA; see [Getting started with HIPAA readiness](#getting-started-with-hipaa-readiness). If your organization requires a negotiated BAA, or self-serve enablement isn't available for your organization, contact the [Anthropic sales team](https://claude.com/contact-sales).

### Does this apply to Amazon Bedrock or Google Cloud?

No. The ZDR and HIPAA arrangements described on this page apply to the Claude API, where Anthropic is the data processor. On Bedrock and Google Cloud, the cloud provider is the data processor; refer to those platforms' data retention and compliance policies for their equivalent controls.

### Is Claude Platform on AWS eligible for ZDR or HIPAA readiness?

Claude Platform on AWS follows the same data retention policy as the first-party Claude API. ZDR is available on request; contact your Anthropic account representative to enable it. HIPAA readiness is not available on Claude Platform on AWS. See [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md) for details.

### Is Claude Code eligible for ZDR?

Claude Code is eligible for ZDR through two paths:

- **API keys:** Claude Code used with pay-as-you-go API keys from a Commercial organization
- **Claude Enterprise:** Claude Code used through Claude Enterprise with ZDR enabled for the organization

ZDR is enabled on a per-organization basis. Each new organization requires ZDR to be enabled separately by your account team. ZDR does not automatically apply to new organizations created under the same account.

Additionally, if you have metrics logging enabled in Claude Code, productivity data (such as usage statistics) is exempted from ZDR and may be retained.

For full details on ZDR for Claude Code on Claude Enterprise, including disabled features and how to request enablement, see the [Claude Code ZDR documentation](https://platform.claude.com/docs/22-Safety-Policy/zero-data-retention-claude-code-docs-6ec9ee63f1.md).

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
