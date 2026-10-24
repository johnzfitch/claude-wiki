---
title: "Inference hooks - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/inference-hooks"
category: "04-API-Reference/Other"
fetched_at: "2026-10-23T06:28:46Z"
tags: ["api", "hooks"]
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


[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Finference-hooks)





SearchCtrlK

Organization

[Admin API](manage-claude-admin-api.md)[User management](manage-claude-user-management.md)[Plugins API](manage-claude-plugins-api.md)[Workspaces](manage-claude-workspaces.md)[Organization webhooks (beta)](manage-claude-organization-webhooks.md)[User profiles](manage-claude-user-profiles.md)[Verification Portal links](manage-claude-user-profiles-verification-portal.md)

Authentication

[Overview](manage-claude-authentication.md)[Create an Admin API key](manage-claude-admin-api-keys.md)[App Attest](manage-claude-app-attest.md)[Workload Identity Federation](manage-claude-workload-identity-federation.md)[Manage WIF with the Admin API](manage-claude-wif-admin-api.md)[WIF reference](manage-claude-wif-reference.md)

Identity providers

Monitoring

[Usage and Cost API](manage-claude-usage-cost-api.md)[Rate Limits API](manage-claude-rate-limits-api.md)[Analytics APIs](manage-claude-analytics-api.md)[Claude Code Analytics API](manage-claude-claude-code-analytics-api.md)[Spend Limits API](manage-claude-spend-limits-api.md)

[OpenTelemetry](manage-claude-opentelemetry.md)

Data & compliance

[Data residency](manage-claude-data-residency.md)[API and data retention](manage-claude-api-and-data-retention.md)

[Access Transparency](manage-claude-access-transparency.md)

[Encryption keys (CMEK)](manage-claude-cmek.md)

[Inference hooks](manage-claude-inference-hooks.md)

[Overview](manage-claude-inference-hooks.md)[Configure Inference hooks](manage-claude-inference-hooks-configuration.md)[Build an integration](manage-claude-inference-hooks-endpoint.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](playground.md)

[Admin](manage-claude-admin-api.md)Inference hooks

# Inference hooks

Copy page



Send each governed prompt to your organization's AI security server for an allow or deny verdict before inference proceeds.

Copy page





Inference hooks are available only to Claude Enterprise organizations. Configuring them requires the `organization:manage` permission in claude.ai, which only the Owner and Primary owner roles hold; see [Configure Inference hooks](manage-claude-inference-hooks-configuration.md).

Inference hooks let a Claude Enterprise organization route every governed prompt through an AI security server, an HTTPS service that the organization or its security vendor operates, before inference runs. When a user submits a prompt, Anthropic sends the conversation transcript to your AI security server and waits for an allow or deny verdict; a denied request never reaches the model. Security and compliance teams use Inference hooks to enforce data policies inline, and developers build the AI security server that evaluates each request.

Because the hook runs on Anthropic's servers, after the request leaves the client and before the model runs, it applies to every governed request uniformly, across all Claude products in your organization, with nothing to install or deploy on user devices.

There are two hook events. `prompt` fires once for each governed inference request, before inference starts. `tool_call` fires when Claude's response contains tool calls, before any of them runs, in organizations that have **Validate tool calls** on.

------------------------------------------------------------------------

## How Inference hooks work

1.  A user submits a prompt on a governed surface.
2.  Anthropic sends an HTTPS `POST` to your organization's configured AI security server endpoint. The request body carries the conversation transcript, and each request is signed according to the [Standard Webhooks](https://www.standardwebhooks.com/) specification once your organization generates its signing secret, so your server can verify it came from Anthropic.
3.  Your AI security server evaluates the content and responds with a verdict within the verdict timeout your organization configures (5 seconds by default).
4.  On `allow`, inference proceeds normally. On `deny`, the request is rejected and the user sees a blocked-by-policy message assembled from two parts: the per-request reason your AI security server supplied in the verdict's `deny_reason` field, followed by a standing message your administrators configure (for example, who to contact or where to request an exception). If your administrators haven't configured one, a built-in default directs the user to contact them. Each denial is also recorded in your organization's [Activity Feed](manage-claude-compliance-activity-feed.md).

The following diagram traces one example (a Cowork request where Claude also calls an O365 tool) to illustrate which parts of the flow are hooked. The hooked points are the diagram's steps 1, 2, and 3, where the prompt arrives, Claude calls the tool, and the tool result returns. At each one, your AI security server returns a verdict before the flow continues. Step 2 is hooked only with **Validate tool calls** on, and its one verdict covers all the tool calls in a response.

A verdict is a small JSON object: `{"action": "allow"}` lets the request proceed, and a deny carries the user-facing reason. For the full verdict schema, see [Return a verdict](manage-claude-inference-hooks-endpoint.md#return-a-verdict).

Your AI security server sees what the user sees: transcript text, tool calls and their results, and text extracted from attachments. It never receives raw file or image bytes, system prompts, or Anthropic-internal context.

The Inference hooks system doesn't keep its own copy of prompt or response content. It stores only your hook configuration and metadata about hook activity, such as verdicts, timestamps, and request identifiers. The Claude product you use stores prompts and responses under its own data retention rules, whether or not hooks are on. For example, a message that a hook blocks on claude.ai stays in the conversation.

If your AI security server is unreachable, returns an error, or doesn't respond within the timeout, your organization's failure handling setting determines the outcome: block the request, or allow it to proceed without inspection. Sustained failures attributable to your server trip a circuit breaker: Anthropic stops contacting it and applies your failure handling setting to every request, then resets the breaker automatically once it detects that your server is returning verdicts again; see [Circuit breaker](manage-claude-inference-hooks-configuration.md#circuit-breaker).

Enforcement can roll out at your pace, so nobody has to be blocked on day one: shadow mode observes verdicts on live traffic without blocking anything, a rollout percentage inspects a chosen fraction of requests, and exclusions exempt members of chosen roles entirely. See [Configure Inference hooks](manage-claude-inference-hooks-configuration.md).

For the full request and response schemas, signature verification, and operational details, see [Develop an Inference hooks integration](manage-claude-inference-hooks-endpoint.md).

------------------------------------------------------------------------

## Continue a conversation after a denied request

Each request includes the whole conversation, so a denied message is sent again with every later message. If your AI security server evaluates the whole transcript, it denies those requests too. To continue, the user removes the denied content from what the app sends next, including any file Claude would read again.

The steps depend on the app:

- **claude.ai, including Claude Desktop and the mobile apps.** The user edits the denied message, or an earlier one, rather than sending a corrected copy as a new message. On the web and in Claude Desktop, the edit resends the message's attachments unless the user removes them. A new chat also works.
- **Claude Code.** The user runs `/rewind` and selects the prompt that first brought the content in. If asked, they select **Restore conversation**, then edit or clear the prompt that returns to the input field. `/clear` starts over. See [Checkpointing](../../02-Claude-Code-CLI/checkpointing.md).
- **Cowork.** The user edits the denied message if it is their latest one. The edit resends attached files, and **Restart from here** resends the whole message unchanged. If the content is in a file or an earlier message, the user selects **New task**.
- **Claude Tag.** In Slack, the user first edits the denied message, or deletes it if it is a reply. They then send `@Claude !restart` on its own where Claude was answering: in that thread, or at the channel's top level. The new session rereads the messages still in Slack, so the edit or deletion comes first. See the [`!restart` command](https://claude.com/docs/claude-tag/users/commands#restart-a-stuck-or-wrong-context-session).

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
- Claude Platform organizations (API access through the Platform) are out of scope.

------------------------------------------------------------------------

## Availability

Inference hooks are available to Claude Enterprise organizations. Configuring them requires the `organization:manage` permission, which only the Owner and Primary owner roles hold.

One hook governs conversations across all Claude products in your Claude Enterprise organization, including, but not limited to, claude.ai, Cowork, Claude Code, Claude for Microsoft 365, Claude Tag, and Claude in Chrome, whether they run on the web, in the desktop or mobile apps, in the CLI, or in Slack. Inference hooks are not available on Amazon Bedrock or Google Cloud.

Governed requests are the inference requests behind the user's conversation or session. System prompts and tool definitions are never included in what is sent. In voice mode, prompts and tool calls are sent to your endpoint too, though a small share of tool calls isn't, so don't rely on Inference hooks as your only control for voice. If your endpoint denies a request in voice mode, the voice call usually ends with a general error message, and your deny reason isn't shown.

With **Validate tool calls** on, `tool_call` events may leave out calls to some of claude.ai's own tools, such as tools that list, search for, or suggest connectors, plugins, or skills, suggest starting research or turning on web search, search for other tools, switch to a larger model, end the chat, give Claude the user's local time, or read the user's own past chats and saved memory. These calls and their results stay in the conversation, so the next `prompt` event from that conversation, if there is one, includes them.

Some features that Anthropic runs for your organization make model calls of their own. Your organization sees the results of those calls but not their transcripts. These calls aren't governed requests and aren't sent to your endpoint. They include the following:

- **Claude Security scans (beta).** [Claude Security](../../15-Claude-AI-Features/product-claude-security.md) runs hosted scans on your connected repositories. A session a user opens to fix a finding, and the Claude Security plugin in Claude Code, are governed.
- **Code Review (research preview).** [Code Review](../../02-Claude-Code-CLI/code-review.md) runs reviews on your GitHub pull requests. A review a user runs locally in Claude Code with `/code-review` is governed.
- **Smart reports (beta).** Anthropic makes model calls to build your organization's [smart reports](../../15-Claude-AI-Features/get-started-with-smart-reports.md). What a user types or uploads when creating a report is governed.

------------------------------------------------------------------------

## Inference hooks versus the Compliance API

Both features serve security, legal, and compliance teams at Claude Enterprise organizations.

|              | Inference hooks                                     | Compliance API                                                                                  |
|--------------|-----------------------------------------------------|-------------------------------------------------------------------------------------------------|
| When it acts | Inline, before inference runs                       | After the fact                                                                                  |
| What it does | Allows or denies each governed request in real time | Retrieves activity, chats, files, projects, session transcripts, and users for audit and export |
| Direction    | Anthropic calls your AI security server             | You call Anthropic's API                                                                        |

Use Inference hooks to stop a request before it reaches the model, and the [Compliance API](manage-claude-compliance-api.md) to audit what occurred afterward.

------------------------------------------------------------------------

## In this section

[Configure Inference hooks](manage-claude-inference-hooks-configuration.md)

Allow Inference hooks for your organization, set up and test your AI security server, choose failure handling, and enforce verdicts.

[Develop an Inference hooks integration](manage-claude-inference-hooks-endpoint.md)

The request and verdict schemas, signature verification, operational semantics, and integration patterns for building the AI security server.
