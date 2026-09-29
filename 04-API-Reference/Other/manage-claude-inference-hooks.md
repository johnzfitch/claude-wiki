---
title: "Inference hooks - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/inference-hooks"
category: "04-API-Reference/Other"
fetched_at: "2026-09-22T06:30:29Z"
tags: ["api", "hooks"]
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Finference-hooks)

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

[Overview](manage-claude-inference-hooks.md)[Configure Inference hooks](manage-claude-inference-hooks-configuration.md)[Build an integration](manage-claude-inference-hooks-endpoint.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](usage-limits.md)

[Admin](manage-claude-admin-api.md)Inference hooks

# Inference hooks

Copy page



Send each governed prompt to your organization's AI security server for an allow or deny verdict before inference proceeds.

Copy page





Inference hooks are in beta and available to Claude Enterprise organizations. Configuring them requires the `organization:manage` permission in claude.ai, which only the Owner and Primary owner roles hold; see [Configure Inference hooks](manage-claude-inference-hooks-configuration.md).

Inference hooks let a Claude Enterprise organization route every governed prompt through an AI security server, an HTTPS service that the organization or its security vendor operates, before inference runs. When a user submits a prompt, Anthropic sends the conversation transcript to your AI security server and waits for an allow or deny verdict; a denied request never reaches the model. Security and compliance teams use Inference hooks to enforce data policies inline, and developers build the AI security server that evaluates each request.

Because the hook runs on Anthropic's servers, after the request leaves the client and before the model runs, it applies to every governed request uniformly, with nothing to install or deploy on user devices.

Today the only hook event is `prompt`, which fires once per governed inference request, before inference begins. Response-side enforcement is planned as a later event.

------------------------------------------------------------------------

## How Inference hooks work

1.  A user submits a prompt on a governed surface.
2.  Anthropic sends an HTTPS `POST` to your organization's configured AI security server endpoint. The request body carries the conversation transcript, and each request is signed according to the [Standard Webhooks](https://www.standardwebhooks.com/) specification once your organization generates its signing secret, so your server can verify it came from Anthropic.
3.  Your AI security server evaluates the content and responds with a verdict within the verdict timeout your organization configures (5 seconds by default).
4.  On `allow`, inference proceeds normally. On `deny`, the request is rejected and the user sees a blocked-by-policy message assembled from two parts: the per-request reason your AI security server supplied in the verdict's `deny_reason` field, followed by a standing message your administrators configure (for example, who to contact or where to request an exception). If your administrators haven't configured one, a built-in default directs the user to contact them. Each denial is also recorded in your organization's [Activity Feed](manage-claude-compliance-activity-feed.md).

The following diagram traces one example (a Cowork request where Claude also calls an O365 tool) to illustrate which parts of the flow are hooked. The hooked points are the diagram's steps 1 and 6, where the prompt arrives and the tool result returns; each results in the validation exchange with your AI security server shown in steps 2–3 and 7–8.

A verdict is a small JSON object: `{"action": "allow"}` lets the request proceed, and a deny carries the user-facing reason. For the full verdict schema, see [Return a verdict](manage-claude-inference-hooks-endpoint.md#return-a-verdict).

Your AI security server sees what the user sees: transcript text, tool calls and their results, and text extracted from attachments. It never receives raw file or image bytes, system prompts, or Anthropic-internal context.

The Inference hooks system doesn't keep its own copy of prompt or response content. It stores only your hook configuration and metadata about hook activity, such as verdicts, timestamps, and request identifiers. The Claude product you use stores prompts and responses under its own data retention rules, whether or not hooks are on. For example, a message that a hook blocks on claude.ai stays in the conversation.

If your AI security server is unreachable, returns an error, or doesn't respond within the timeout, your organization's failure handling setting decides the outcome: block the request, or allow it to proceed without inspection. Sustained failures attributable to your server trip a circuit breaker: Anthropic stops contacting it and applies your failure handling setting to every request, then resets the breaker automatically once it detects that your server is returning verdicts again; see [Circuit breaker](manage-claude-inference-hooks-configuration.md#circuit-breaker).

Enforcement can roll out at your pace, so nobody has to be blocked on day one: shadow mode observes verdicts on live traffic without blocking anything, a rollout percentage inspects a chosen fraction of requests, and exclusions exempt members of chosen roles entirely. See [Configure Inference hooks](manage-claude-inference-hooks-configuration.md).

For the full request and response schemas, signature verification, and operational details, see [Develop an integration](manage-claude-inference-hooks-endpoint.md).

------------------------------------------------------------------------

## Use cases

- **Data loss prevention (DLP).** Forward the transcript to your DLP scanner and deny prompts that carry regulated or classified material. This is the most common deployment.
- **Real-time transcript archival.** Archive each transcript as it arrives and always return `allow`, as a push-based alternative to polling the [Compliance API](manage-claude-compliance-api.md).
- **Prompt telemetry.** Measure how your organization uses Claude, at the moment of use.
- **Policy engines.** Enforce your own rules before inference: model allowlists, project-scoped restrictions, or working-hours controls.

------------------------------------------------------------------------

## Current limitations

- Attachments are represented by metadata and extracted text. Raw file and image bytes are never sent, so image-only content (for example, a screenshot of a document) is not inspected.
- Verdicts are allow or deny. Rewriting or redacting a prompt is not supported.
- Platform organizations (API access through the Claude Platform) are out of scope.

------------------------------------------------------------------------

## Availability

Inference hooks are available to Claude Enterprise organizations. Configuring them requires the `organization:manage` permission, which only the Owner and Primary owner roles hold.

One hook governs conversations across claude.ai, Cowork, and Claude Code sessions in your Claude Enterprise organization, whether they run on the web, in the desktop or mobile apps, or in the CLI. Inference hooks are not available on Amazon Bedrock or Google Cloud.

Governed requests are the inference requests behind the user's conversation. Ancillary requests, such as conversation title generation, aren't sent to your endpoint, and system prompts and tool definitions are never included in what is sent. Voice mode is not covered.

------------------------------------------------------------------------

## Inference hooks versus the Compliance API

Both features serve security, legal, and compliance teams at Claude Enterprise organizations.

|              | Inference hooks                                     | Compliance API                                                                                  |
|--------------|-----------------------------------------------------|-------------------------------------------------------------------------------------------------|
| When it acts | Inline, before inference runs                       | After the fact                                                                                  |
| What it does | Allows or denies each governed request in real time | Retrieves activity, chats, files, projects, session transcripts, and users for audit and export |
| Direction    | Anthropic calls your AI security server             | You call Anthropic's API                                                                        |

Use Inference hooks to stop a request before it reaches the model, and the [Compliance API](manage-claude-compliance-api.md) to audit what happened afterward.

------------------------------------------------------------------------

## In this section

[Configure Inference hooks](manage-claude-inference-hooks-configuration.md)

Allow Inference hooks for your organization, set up and test your AI security server, choose failure handling, and enforce verdicts.

[Develop an Inference hooks integration](manage-claude-inference-hooks-endpoint.md)

The request and verdict schemas, signature verification, operational semantics, and integration patterns for building the AI security server.
