---
title: "Claude Platform release notes - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/release-notes/overview"
category: "20-Models"
fetched_at: "2026-09-26T06:39:48Z"
tags: ["models"]
---

- [Managed Agents](../04-API-Reference/Other/managed-agents-overview.md)

- [Admin](../04-API-Reference/Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../04-API-Reference/About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../04-API-Reference/Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](release-notes-overview.md)

[API reference](../04-API-Reference/Endpoints/overview.md)




[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Frelease-notes%2Foverview)





SearchCtrlK

Release notes

[Overview](release-notes-overview.md)

Migration guides

[Migrating to Managed Agents](../04-API-Reference/Other/managed-agents-migration.md)

[Console](../04-API-Reference/Other/usage-limits.md)

Release notes

# Claude Platform release notes

[Subscribe](https://platform.claude.com/docs/en/release-notes/feed.xml)

Copy page



Updates to the Claude Platform, including the Claude API, client SDKs, and the Claude Console.

[Subscribe](https://platform.claude.com/docs/en/release-notes/feed.xml)

Copy page



The Claude Platform release notes list changes to the Claude API, the client SDKs, and the Claude Console, newest first.



For release notes on Claude Apps, see the [Release notes for Claude Apps in the Claude Help Center](../19-Reference/release-notes.md).

For updates to Claude Code, see the [complete CHANGELOG.md](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) in the `claude-code` repository.

### September 24, 2026

- We're resuming billing for refusals that arrive before any output when `stop_details.category` is `"bio"`, `"frontier_llm"`, or `"reasoning_extraction"`, the categories where we measure low volumes of false positives. Mid-stream refusals were already billed. Refusals billed under this change are charged like any other request, at the rates of the model that ran it. Refusals before any output in other categories are still not billed, and fallback credit is unchanged. This change applies on all platforms. See [How refusals are billed](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#how-refusals-are-billed).
- The [Compliance API](../04-API-Reference/Other/manage-claude-compliance-api.md) local session endpoints are out of beta for Claude for Microsoft 365 sessions in Excel, PowerPoint, Word, and Outlook (`product_surface` values beginning with `office_agents`). See [Sessions on users' machines](../04-API-Reference/Other/manage-claude-compliance-sessions.md#retrieve-local-sessions).
- The [Compliance API](../04-API-Reference/Other/manage-claude-compliance-api.md) [Activity Feed](../04-API-Reference/Other/manage-claude-compliance-activity-feed.md) no longer returns file names, project document names, or artifact titles. The `filename` and `title` fields on file, project document, and artifact activities are now always empty or omitted, including on activities recorded before this change. To look up a name or title by the ID on the activity, use a Compliance Access Key with the `read:compliance_user_data` scope. See [Understand the Activity object](../04-API-Reference/Other/manage-claude-compliance-activity-feed.md#understand-the-activity-object).

### September 23, 2026

- [Cache diagnostics](../04-API-Reference/Guides/build-with-claude-cache-diagnostics.md) is out of beta on the Claude API and no longer requires the `cache-diagnosis-2026-04-07` beta header. Include the `diagnostics` object on a Messages request to opt in; requests that still send the header work as before. Responses from `POST /v1/messages` now always include the `diagnostics` field, which is `null` when the request did not include the `diagnostics` object.

### September 22, 2026

- We've launched **Claude Opus 5.5** (`claude-opus-5-5`), a model for long-running agentic coding and knowledge work. It has a [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) by default, 128k max output tokens, and always-on [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md), at \$4 / \$20 USD per MTok (Claude Opus 5 is \$5 / \$25). Claude Opus 5.5 is available on the Claude API, [Claude in Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md), [Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md), [Claude on Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md), and [Claude in Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md). See [What's new in Claude Opus 5.5](models-opus-5-5-whats-new-opus-5-5.md) for capabilities, API changes, and migration guidance.
- On Claude Opus 5.5, thinking can't be disabled: `thinking: {"type": "disabled"}` and `thinking: {"type": "enabled", ...}` return a 400 error. Omit the `thinking` field and control thinking depth with the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md). `tool_choice` types `any` and `tool` also return a 400 error, as on Claude Fable 5.1; use `auto` with [strict tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md). On the Claude API and Google Cloud, [computer use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md) on this model requires the `computer_toolset_20260801` toolset and the earlier `computer_20251124` tool returns a 400 error; on Amazon Bedrock, `computer_20251124` keeps working. See the [migration guide](models-opus-5-5-migration-guide.md#migrating-from-claude-opus-5).
- [Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) (research preview) is available for Claude Opus 5.5 on the Claude API.
- Tools can now be defined inside a [mid-conversation system message](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md#define-tools-in-a-message-beta), in beta on the Claude API with the `inline-tools-2026-09-15` beta header. A `tool_addition` block can carry the tool's full definition (`tool: {"type": "tool_definition", "definition": {...}}`), so you can add a tool, change its schema, or move a server tool to a newer version without editing `tools` or invalidating the prompt cache. The same header covers adding and removing tools by reference. With the MCP connector's `mcp-client-2026-09-15` beta header as well, the definition can be an MCP toolset, and a response records each server's fetched tool list in an `mcp_tool_listing` block, which pins that list when you send it back.

### September 18, 2026

- For [cache diagnostics](../04-API-Reference/Guides/build-with-claude-cache-diagnostics.md), a response to a request that sends the `cache-diagnosis-2026-04-07` beta header now always includes the `diagnostics` field. The field is `null` when the request did not include the `diagnostics` object. Previously the field was omitted in that case.
- The [Compliance API](../04-API-Reference/Other/manage-claude-compliance-api.md) local session endpoints now also return transcripts of Claude in Chrome sessions (`product_surface` value `claude_in_chrome`), in beta for Claude Enterprise organizations, with your existing Compliance Access Key and the `read:compliance_user_data` scope. See [Sessions on users' machines](../04-API-Reference/Other/manage-claude-compliance-sessions.md#retrieve-local-sessions).

### September 14, 2026

- The Messages API can now [compact a conversation on demand](../04-API-Reference/Guides/build-with-claude-compaction-on-demand.md) on the Claude API, in beta with the `compact-2026-09-04` beta header. Send the top-level `compaction` parameter, and the API returns a signed `compaction` block that summarizes the messages you sent. On later requests, send that block first, in place of those messages. You choose when to compact, the request can run in the background, and you can keep recent turns word for word after the summary. On models with preserved thinking, the thinking in those kept turns can stay valid.
- With the `thinking-binding-controls-2026-08-01` beta header, the `input_transformations` response field gains a second entry type, `thinking_mismatch_allowed`. It names a thinking block that failed the prefix check on a request where the API doesn't enforce that check: on Claude Fable 5.1, for example, a request from an account created before August 31, 2026, with `prefix_mismatch_behavior` unset. The block still reaches the model unchanged. Log these entries to find history edits in production traffic before you opt into enforcement. See [Set the mismatch behavior and read `input_transformations`](../04-API-Reference/Guides/build-with-claude-preserved-thinking.md#preserved-thinking-controls).

### September 10, 2026

- Claude Managed Agents permission policies now include `auto`: the server evaluates each agent or MCP tool call and runs it, denies it, or pauses for your approval. `agent.tool_use` and `agent.mcp_tool_use` events report how each call was evaluated in an `evaluation` field alongside `evaluated_permission`. See [Let the server evaluate each call with `auto`](../04-API-Reference/Other/managed-agents-permission-policies.md#let-the-server-evaluate-each-call-with-auto).
- Version 1.32.0 of the `ant` CLI adds `ant beta:sessions connect`, which attaches your terminal to a Claude Managed Agents session. You can follow the session live, send messages, and allow or deny tool calls that are waiting for approval. Pass `--web` to serve the Claude Console's session viewer locally and open the session there instead. See [Connect to a Managed Agents session from your terminal](../04-API-Reference/Other/cli-sdks-libraries-cli-sessions-connect.md).

### September 9, 2026

- For [cache diagnostics](../04-API-Reference/Guides/build-with-claude-cache-diagnostics.md), the API now stores a request's fingerprint only when the request includes the `diagnostics` object. A request that sends only the `cache-diagnosis-2026-04-07` beta header is still accepted, but no fingerprint is stored. A later turn that points `previous_message_id` at it reports `previous_message_not_found`. Include `diagnostics` on every turn, with `"previous_message_id": null` on the first.

### September 3, 2026

- Version 1.30.0 of the `ant` CLI adds `ant apply`, which creates and updates agents, environments, skills, memory stores, and deployments from files in your repository. Describe each resource in a file, run `ant apply`, and approve the plan it prints. Commit the `claude-lock.json` lockfile it writes so that later runs, on your machine or in CI, update the same resources instead of creating new ones. See [Manage resources as code with ant apply](../04-API-Reference/Other/cli-sdks-libraries-cli-apply.md).
- [Per-message effort](../04-API-Reference/Guides/build-with-claude-effort.md#change-effort-mid-conversation-beta) changes, in beta, are also available on [Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md) for Claude Fable 5.1, Claude Mythos 5.1, and Claude Opus 5, with the same `mid-conversation-output-config-2026-07-01` beta header.

### September 1, 2026

- We've launched **Claude Fable 5.1** (`claude-fable-5-1`), the successor to Claude Fable 5 for long-running agentic coding, knowledge work, and research, alongside **Claude Mythos 5.1** (`claude-mythos-5-1`) for Project Glasswing participants. Both models support a [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) by default, 128k max output tokens, and always-on [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md), at \$10 / \$50 USD per MTok, the same as Claude Fable 5, with cache reads cut to \$0.25 per MTok. Claude Fable 5.1 is available on the Claude API, [Claude in Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md), [Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md), [Claude on Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md), and [Claude in Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md). See [What's new in Claude Fable 5.1](models-fable-5-1-whats-new-fable-5-1.md) for capabilities, API changes, and migration guidance.
- Prompt cache reads on Claude Fable 5.1 and Claude Mythos 5.1 cost \$0.25 USD per million tokens: 0.025x the base input price, compared with 0.1x on other models. Cache writes are unchanged. See [Prompt caching pricing](../17-Billing-Plans/about-claude-pricing.md#prompt-caching).
- On Claude Fable 5.1 and Claude Mythos 5.1, `tool_choice` types `any` and `tool` aren't supported and return a 400 error. `auto` and `none` are unchanged. To guarantee schema-conformant tool inputs, use [strict tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md) or [structured outputs](../04-API-Reference/Guides/build-with-claude-structured-outputs.md).
- Thinking blocks produced by Claude Fable 5.1 and Claude Mythos 5.1 are preserved only for the model that produced them or a newer one: earlier models can't read them, and the API drops one replayed to an earlier model. Claude Fable 5.1 accepts thinking blocks from Claude Opus 5, Claude Fable 5, Claude Mythos 5, and earlier Claude models. On Claude Fable 5.1, the API also [checks that nothing before a block has changed](../04-API-Reference/Guides/build-with-claude-thinking.md#preserved-in-conversation): for new accounts created on or after August 31, 2026, replaying one after the `system` prompt, `tools`, or an earlier message changed returns a 400 error. With the `thinking-binding-controls-2026-08-01` beta header, dropped blocks are reported in an `input_transformations` response field, and `thinking.block_binding.prefix_mismatch_behavior` chooses between rejecting and dropping blocks whose history changed. See [Preserved thinking](../04-API-Reference/Guides/build-with-claude-thinking.md#preserved-thinking).
- Per-message effort changes are in beta on Claude Fable 5.1, Claude Mythos 5.1, and Claude Opus 5 on the Claude API. Add a `role: "system"` message with `output_config.effort` inside `messages` to change effort for later turns while preserving the prompt cache. Include the `mid-conversation-output-config-2026-07-01` beta header in your requests. See [Per-message effort](../04-API-Reference/Guides/build-with-claude-effort.md#change-effort-mid-conversation-beta).
- [Turn-scoped system messages](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md#turn-scoped-system-messages) are in beta (`mid-conversation-system-clear-at-2026-08-21` header). Set `clear_at: "next_user_message"` on a mid-conversation `role: "system"` message and it renders for the current turn only, then stays in the history at no token cost. Per-turn reminders don't accumulate and don't invalidate the prompt cache or later thinking blocks.
- `thinking.display` accepts a third value, `"updates"`, in beta (`thinking-display-updates-2026-08-18` header). Reasoning comes back with an empty `thinking` field, as under `"omitted"`, and the short progress updates that Claude Fable 5.1, Claude Mythos 5.1, and Claude Fable 5 write between tool calls come back as text, at most one `thinking` block before a tool call. See [Progress updates between tool calls](../04-API-Reference/Guides/build-with-claude-thinking.md#progress-updates).
- Text generated by Claude Fable 5.1 and Claude Mythos 5.1 carries Anthropic's text watermark, and supported image, video, and audio files that Claude produces through the [code execution tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md) carry C2PA Content Credentials when you retrieve them through the [Files API](../04-API-Reference/Guides/build-with-claude-files.md) on the Claude API. Marking requires no changes to your requests or response handling.
- Like Claude Fable 5, both models require 30-day data retention and aren't available under zero data retention unless expressly authorized by Anthropic. See [Model-specific data retention requirements](../04-API-Reference/Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements).
- The guides for the Claude Enterprise endpoints of the [Admin API](../04-API-Reference/Admin/http-beta-organization.md) ([user management](../04-API-Reference/Other/manage-claude-user-management.md) and [spend limits](../04-API-Reference/Other/manage-claude-spend-limits-api.md)), the [Claude Enterprise Analytics API](../04-API-Reference/Other/manage-claude-analytics-api.md), and the [Compliance API](../04-API-Reference/Other/manage-claude-compliance-api.md) now show the `anthropic-version` header; send it on every request to these endpoints, as in the rest of the Claude API. See [API versions](../04-API-Reference/Endpoints/versioning.md).

### August 27, 2026

- In Python SDK 1.2.0, TypeScript SDK 0.122.0, Go SDK 1.68.0, Java SDK 2.59.0, Ruby SDK 1.67.0, and C# SDK 12.44.0, `client.beta.files` and `client.beta.skills` no longer send the `files-api-2025-04-14` and `skills-2025-10-02` beta headers and return the same shapes as `client.files` and `client.skills`. With this change, `client.beta.skills.delete()` deletes a Skill together with all of its versions, and the beta Messages type `BetaSkill` (the container Skill reference) is renamed `BetaContainerSkill`. Requests that still send the beta headers keep receiving the beta shapes. See [Migrate from `files-api-2025-04-14`](../04-API-Reference/Guides/build-with-claude-files.md#migrate-from-files-api-2025-04-14) and [Migrate from `skills-2025-10-02`](../04-API-Reference/Guides/build-with-claude-skills-guide.md#migrate-from-skills-2025-10-02).


- You can now create **personal keys** and **service account keys** in the Claude Console. They act as you or as a [service account](../04-API-Reference/Other/manage-claude-workload-identity-federation.md#service-accounts), with the same permissions, and stop working when the linked account is removed from an organization. This lets organization admins more easily track usage for each account, and ensure key usage is legitimate. These API keys can be scoped to a specific workspace or [work on admin endpoints and across any workspace](../04-API-Reference/Other/manage-claude-authentication.md#select-a-workspace) the account has access to. Workspace API keys remain supported as a legacy option. See [API keys](../04-API-Reference/Other/manage-claude-authentication.md#api-keys) for more information.

### August 26, 2026

- The [Compliance API](../04-API-Reference/Other/manage-claude-compliance-api.md) session endpoints are out of beta for Cowork and Claude Code sessions. See [Retrieve session transcripts](../04-API-Reference/Other/manage-claude-compliance-sessions.md).
- The [Compliance API](../04-API-Reference/Other/manage-claude-compliance-api.md) local session endpoints now also return transcripts of Claude Science sessions (`product_surface` value `claude_science`) and Claude for Microsoft 365 sessions in Excel, PowerPoint, Word, and Outlook (`product_surface` values beginning with `office_agents`), in beta for Claude Enterprise organizations, with your existing Compliance Access Key and the `read:compliance_user_data` scope. See [Sessions on users' machines](../04-API-Reference/Other/manage-claude-compliance-sessions.md#retrieve-local-sessions).


- The [Admin API](../04-API-Reference/Other/manage-claude-admin-api.md) is now available in the `ant` CLI and the Python, TypeScript, C#, Go, Java, PHP, and Ruby SDKs under `client.beta.organization`. They cover organization info, members, invites, workspaces and workspace members, API keys, rate limits, service accounts, workload identity federation issuers and rules, and customer-managed encryption keys. Usage and cost reports and the Claude Enterprise user-management and analytics endpoints remain curl-only. The CLI and SDKs read an Admin API key from `ANTHROPIC_API_KEY` or an `org:admin` OAuth token from `ANTHROPIC_AUTH_TOKEN`.

### August 20, 2026

- We've released **v1.0 of the [Python SDK](../04-API-Reference/Other/cli-sdks-libraries-sdks-python.md)**. The SDK's HTTP layer moves from `httpx` to [httpx2](https://httpx2.pydantic.dev), a maintained, API-compatible fork: build custom `http_client`, `Timeout`, and transport objects from `httpx2` (the `DefaultHttpxClient` helpers are unchanged), and call `httpx2.alias_httpx()` at startup if you rely on tracing or mocking libraries that patch `httpx`. v1.0 requires Python 3.10 or later and removes long-deprecated surface, including the legacy Text Completions API, the `temperature`, `top_p`, and `top_k` parameters on Messages methods, and the tool runner's client-side `compaction_control`. On the async client, `.with_raw_response` results now need `await response.parse()`, and `AnthropicBedrock` now raises an error when no AWS region is configured instead of defaulting to `us-east-1`. See the [v1 migration guide](https://github.com/anthropics/anthropic-sdk-python/blob/main/MIGRATION.md) for every change with before-and-after snippets.
- The [computer use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md) and [browser use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md) toolsets (`computer_toolset_20260801` and `browser_toolset_20260801`) are now available on [Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md) for Claude Fable 5, Claude Mythos 5, Claude Opus 5, Claude Sonnet 5, and Claude Opus 4.8. Requests use the same `tools` entries as on the Claude API.

### August 19, 2026

- The [computer use tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md) is out of beta on the Claude API as the `computer_toolset_20260801` toolset: no beta header, batch actions (several actions in one turn), `zoom` enabled by default, and per-member configuration through `configs`. Earlier beta versions remain available. Upgrading an existing integration changes the request shape and tool handling; see [Migrate from `computer_20251124`](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#migrate-from-computer-20251124).
- We've launched the [browser use tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md) (`browser_toolset_20260801`), a client toolset for driving a browser that your application hosts. It works inside a browser viewport rather than a whole desktop, reading the page itself (its accessibility tree, elements, forms, and tabs) and adding element references, form input, tab management, download reporting, and opt-in file upload on top of screenshot-and-click control.
- Both toolsets are available for Claude Fable 5, Claude Mythos 5, Claude Opus 5, Claude Sonnet 5, and Claude Opus 4.8 on the Claude API.
- The [Files API](../04-API-Reference/Guides/build-with-claude-files.md) is out of beta on the Claude API. Requests to the `/v1/files` endpoints, and Messages API requests that reference an uploaded file, no longer require the `files-api-2025-04-14` beta header. Requests sent without the header use the current response format: [file expiration](../04-API-Reference/Guides/build-with-claude-files.md#file-expiration) (set `expires_in_seconds` when you upload a file; file objects report `expires_at`), and `page` and `next_page` [pagination](../04-API-Reference/Endpoints/overview.md#pagination) plus an `ids[]` filter when you [list files](../04-API-Reference/Guides/build-with-claude-files.md#list-files). `/v1/files` requests that still send the beta header keep working and return the previous response format. To move an existing integration off the header, see [Migrate from `files-api-2025-04-14`](../04-API-Reference/Guides/build-with-claude-files.md#migrate-from-files-api-2025-04-14).
- [Agent Skills](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-overview.md) and the Skills API (`/v1/skills`) are out of beta on the Claude API. Requests no longer require the `skills-2025-10-02` beta header, including Messages API requests that load Skills through the `container` parameter. Requests that still send the header continue to work unchanged. See [Using Agent Skills with the API](../04-API-Reference/Guides/build-with-claude-skills-guide.md). To move an existing integration off the header, see [Migrate from `skills-2025-10-02`](../04-API-Reference/Guides/build-with-claude-skills-guide.md#migrate-from-skills-2025-10-02).
- The [Admin API](../04-API-Reference/Admin/http-beta-organization.md) user-management endpoints for **Claude Enterprise** (claude.ai) organizations (members, invites, groups, and custom roles) are out of beta. The `anthropic-beta: ce-user-management-2026-07-13` header is no longer required on group and custom-role requests; requests that still send it are accepted unchanged. See [User management](../04-API-Reference/Other/manage-claude-user-management.md).
- You can now restrict which sites a Claude Managed Agents agent's `web_search` and `web_fetch` tools can reach. Set `allowed_domains` or `blocked_domains` on the tool's entry in the `agent_toolset_20260401` `configs` array; `web_fetch` also accepts `max_content_tokens` and `web_search` accepts `user_location`. Each `configs` entry is identified by its `name` and typed by an optional `type`, and requests that pass only `name`, `enabled`, and `permission_policy` continue to work; in the typed SDKs, `configs` entries become per-tool types. See [Restrict web search and web fetch domains](../04-API-Reference/Other/managed-agents-tools.md#restrict-web-search-and-web-fetch-domains).
- Claude Managed Agents sessions that run in a [self-hosted sandbox](../04-API-Reference/Other/managed-agents-self-hosted-sandboxes.md) can now attach [memory stores](../04-API-Reference/Other/managed-agents-memory.md). The Python, TypeScript, and Go SDK workers download each attached store into the sandbox at its `mount_path` and sync the agent's changes back to the store. See [Use memory stores](../04-API-Reference/Other/managed-agents-self-hosted-sandboxes.md#use-memory-stores).
- The session viewer in the Claude Console has been redesigned with a timeline minimap, a transcript grouped by model request, and an Inspector panel for session details and cost, raw events, per-tool statistics, mounted resources, and per-thread activity. See [Console observability](../04-API-Reference/Other/managed-agents-events-and-streaming.md#console-observability).

### August 18, 2026

- Workbench is now [**playground**](../04-API-Reference/Other/usage-limits.md) in the Claude Console. Playground supports every Messages API parameter and includes templates that demonstrate API features such as code execution and web search. It shows the full SDK request and the API response for each run, to help you understand the API and build with it. For more, see the [Claude Help Center](https://support.claude.com/en/articles/8606378-how-do-i-use-playground) or try it at [platform.claude.com/playground](../04-API-Reference/Other/usage-limits.md).

### August 11, 2026

- The [Compliance API](../04-API-Reference/Other/manage-claude-compliance-api.md) now returns transcripts of Cowork and Claude Code sessions that run on your users' machines, in beta for Claude Enterprise organizations. `GET /v1/compliance/apps/sessions/local` lists sessions across your organization, `GET /v1/compliance/apps/sessions/local/{session_id}` retrieves one session's metadata, and `GET /v1/compliance/apps/sessions/local/{session_id}/messages` returns its transcript, all with your existing Compliance Access Key and the `read:compliance_user_data` scope. See [Sessions on users' machines](../04-API-Reference/Other/manage-claude-compliance-sessions.md#retrieve-local-sessions).
- We've added the `anthropic-workspace-id` response header to the Claude API. It carries the `wrkspc_`-prefixed ID of the workspace that the request's API key or access token resolved to, including your organization's Default Workspace. See [Identify the workspace behind an API response](../04-API-Reference/Other/manage-claude-workspaces.md#identify-the-workspace-behind-an-api-response).

### August 10, 2026

- The introductory pricing for **Claude Sonnet 5** (\$2 / \$10 per MTok) is now the standard price: the previously scheduled increase to \$3 / \$15 per MTok on September 1, 2026 will not occur. See [Pricing](../17-Billing-Plans/about-claude-pricing.md).

### August 7, 2026

- You can now set a budget on a Claude Managed Agents session: a hard cap on the session's spend, priced at public list rates. A session that reaches its budget pauses with the `budget_reached` stop reason instead of starting new model requests; changing or removing the budget resumes it. Deployments accept the same budget and apply it to each session they start. See [Session budgets](../04-API-Reference/Other/managed-agents-budgets.md).
- You can now give a Claude Managed Agents session an advisor: a model at least as capable as the agent's own that the session's primary thread can consult mid-turn for strategic guidance. Configure it as a `{"type": "advisor"}` entry in the agent's multiagent roster, naming the `model` to consult. See [Give the session an advisor](../04-API-Reference/Other/managed-agents-multiagent-orchestration.md#give-the-session-an-advisor).
- You can now control where model inference runs for a Claude Managed Agents agent. Set `inference_geo` inside the `model` object when you [create the agent](../04-API-Reference/Other/managed-agents-agent-setup.md#pin-the-inference-geo), or [override it for a single session](../04-API-Reference/Other/managed-agents-sessions.md#pin-the-inference-geo-for-a-session). See [Data residency](../04-API-Reference/Guides/build-with-claude-data-residency.md) for the available geos and pricing.
- Claude Managed Agents sessions can now [load skills from a GitHub repository](../04-API-Reference/Other/managed-agents-skills.md#load-skills-from-a-github-repository). When a session [mounts a repository](../04-API-Reference/Other/managed-agents-github.md), any skills in its root `.claude/skills` directory are discovered automatically at session start and available to the agent for that session.

### August 5, 2026

- **Inference hooks** are now in beta for Claude Enterprise organizations. Point Claude at your organization's AI security server, and each governed prompt across claude.ai, Cowork, and Claude Code is held for the server's allow or deny verdict before inference proceeds. Requests are signed, failure handling is configurable, and every denial is recorded in the compliance [Activity Feed](../04-API-Reference/Other/manage-claude-compliance-activity-feed.md). See [Inference hooks](../04-API-Reference/Other/manage-claude-inference-hooks.md).
- We've retired the Claude Opus 4.1 model (`claude-opus-4-1-20250805`). All requests to this model on the Claude API will now return an error. We recommend upgrading to [Claude Opus 5](about-claude-models-overview.md#latest-models-comparison). Researchers can request ongoing access through the [External Researcher Access Program](../15-Claude-AI-Features/what-is-the-external-researcher-access-program.md).

### August 3, 2026

- The [Compliance API](../04-API-Reference/Other/manage-claude-compliance-api.md) now returns transcripts of Cowork sessions started on claude.ai web or mobile, in beta for Claude Enterprise organizations. `GET /v1/compliance/apps/sessions/remote` lists sessions and `GET /v1/compliance/apps/sessions/remote/{session_id}/messages` returns one session's transcript, using your existing Compliance Access Key with the `read:compliance_user_data` scope. See [Sessions in the cloud](../04-API-Reference/Other/manage-claude-compliance-sessions.md#retrieve-remote-sessions).

### August 1, 2026

- [Dreams](../04-API-Reference/Other/managed-agents-dreams.md) (research preview) now supports Claude Opus 5. See [Supported models](../04-API-Reference/Other/managed-agents-dreams.md#limits).

### July 24, 2026

- We've launched **Claude Opus 5** (`claude-opus-5`), a step-change improvement over Claude Opus 4.8. Claude Opus 5 supports a [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) (both the default and the maximum), 128k max output tokens, and [thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) on by default, at \$5 / \$25 USD per MTok, the same pricing as Claude Opus 4.8. It's available on the Claude API, [Claude in Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md), [Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md), [Claude on Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md), and [Claude in Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md). See [What's new in Claude Opus 5](models-opus-5-overview.md) for new features, behavior changes, and migration guidance, and the [models overview](about-claude-models-overview.md) for complete specs.
- On Claude Opus 5, disabling thinking is allowed only at effort `high` or below: `thinking: {"type": "disabled"}` with effort `xhigh` or `max` returns a 400 error, a breaking change from Claude Opus 4.8. See [What's new in Claude Opus 5](models-opus-5-overview.md).
- [Effort](../04-API-Reference/Guides/build-with-claude-effort.md) is the primary control for steering Claude Opus 5: the model supports the full ladder (`low`, `medium`, `high`, `xhigh`, `max`), with `max` for capability-critical work.
- Mid-conversation tool changes are now in beta on Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, and Claude Opus 5: add or remove tools between turns of a conversation while preserving the prompt cache. Include the `mid-conversation-tool-changes-2026-07-01` beta header in your requests.
- The `fallbacks` parameter now supports a `"default"` mode, which applies Anthropic's recommended fallback models by refusal category. Server-side fallback is in beta, and the `"default"` mode requires the `server-side-fallback-2026-07-01` beta header. See [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md).
- We've removed [fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) for Claude Opus 4.7. Requests to `claude-opus-4-7` with `speed: "fast"` now return an error; unlike Claude Opus 4.6, they do not fall back to standard speed. Claude Opus 4.7 itself remains available at standard speed. To continue using fast mode, migrate to [Claude Opus 5](models-opus-5-overview.md) or Claude Opus 4.8. Read more in [Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md#supported-models).

### July 22, 2026

- You can now set an `effort` level on a Claude Managed Agents agent's model configuration. Pass `effort` inside the `model` object when you [create the agent](../04-API-Reference/Other/managed-agents-agent-setup.md#create-an-agent). See [Effort levels](../04-API-Reference/Guides/build-with-claude-effort.md#effort-levels) for what each level does.
- Webhooks for Claude Managed Agents now cover the environment and memory store lifecycle: four `environment.*` event types and three `memory_store.*` event types. You can react to environment and memory store lifecycle changes without polling. See the Environment events and Memory store events tabs in [Subscribe to webhooks](../04-API-Reference/Other/managed-agents-webhooks.md#supported-event-types).
- When creating a Claude Managed Agents session, you can now [seed it with initial events](../04-API-Reference/Other/managed-agents-sessions.md#seed-the-session-with-initial-events). Pass `initial_events` on `POST /v1/sessions` with up to 50 `user.message` and `user.define_outcome` events. A non-empty list starts the agent loop in the same call, so you don't need a separate send-events request to start work.
- The `version` field is now optional when [updating a Claude Managed Agents agent](../04-API-Reference/Other/managed-agents-agent-setup.md#update-an-agent). Supply it for optimistic concurrency (a mismatch returns a 409 error), or omit it to apply the update unconditionally. See [Update semantics](../04-API-Reference/Other/managed-agents-agent-setup.md#update-semantics).
- Claude Managed Agents session thread event streams now support [event deltas](../04-API-Reference/Other/managed-agents-events-and-streaming.md#event-deltas). `GET /v1/sessions/{session_id}/threads/{thread_id}/stream` accepts the same `event_deltas[]` query parameter as the session-level stream, so you can preview a subagent's text as the model generates it. A connection previews only the thread it's reading. See [Preview session thread events](../04-API-Reference/Other/managed-agents-events-and-streaming.md#preview-session-thread-events).

### July 17, 2026

- The legacy **Workbench** ([platform.claude.com/workbench](https://platform.claude.com/workbench)) in the Claude Console is being sunset with access ending on August 17, 2026. Saved prompts, variables, and evals are not supported in the updated [Workbench](../04-API-Reference/Other/usage-limits.md). You can export any data you want to keep from the banner and under your **Organizational Settings**. For more, see [How do I use the Workbench?](../15-Claude-AI-Features/how-do-i-use-the-playground.md) in the Claude Help Center.
- The experimental prompt tools APIs for generating, improving, and templatizing prompts (`/v1/experimental/generate_prompt`, `/v1/experimental/improve_prompt`, and `/v1/experimental/templatize_prompt`) are being retired along with the Workbench on August 17, 2026. After removal, requests to these endpoints will return an error.

### July 15, 2026

- [Mid-conversation system messages](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md) are available on Claude Fable 5, Claude Mythos 5, and Claude Opus 4.8, on the Claude API, [Claude in Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md), and [Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md). No beta header is required. This corrects earlier availability notes.

### July 14, 2026

- You can now manage the people in your **Claude Enterprise** (claude.ai) organization with the [Admin API](../04-API-Reference/Admin/http-beta-organization.md), in beta for all Claude Enterprise organizations: list members and look them up by email address, change a member's role, remove members, send and withdraw invites, manage groups and their membership, and read custom roles. Group and custom-role requests require the `anthropic-beta: ce-user-management-2026-07-13` beta header; member and invite requests take no beta header. An Admin API key with the `read:org_audit` scope can also call every user-management `GET` endpoint. See [User management](../04-API-Reference/Other/manage-claude-user-management.md).

### July 10, 2026

- [Dreams](../04-API-Reference/Other/managed-agents-dreams.md) (research preview) now supports Claude Fable 5 and Claude Sonnet 5. See [Supported models](../04-API-Reference/Other/managed-agents-dreams.md#limits).
- We've expanded the [Access Transparency](../04-API-Reference/Other/manage-claude-access-transparency.md) documentation of `cmek_preserve` events with a filter example, an example event payload, and two preservation reason codes (`policy_violation_investigation`, `csae_report`). The documentation now also clarifies that a preservation event is written whether the preservation was initiated by a human reviewer or an automated safety pipeline. See [CMEK content preservation](../04-API-Reference/Other/manage-claude-access-transparency.md#cmek-content-preservation).

### July 8, 2026

- You can now set an expiration when you create an API key or an Admin API key in the [Claude Console](../04-API-Reference/Other/usage-limits.md). Choose a preset, a custom duration, or **Never**. For keys with a lifetime of at least 7 days, Anthropic emails the creator before expiration. Existing keys are unaffected. The Admin API reports each key's expiration in the [`expires_at`](../04-API-Reference/Admin/beta-organization-api-keys-list.md) field. See [Authentication](../04-API-Reference/Other/manage-claude-authentication.md#key-expiration).

### July 2, 2026

- We've added the `agent-memory-2026-07-22` beta header, which changes how [listing memories](../04-API-Reference/Other/managed-agents-memory.md#list-memories) (`GET /v1/memory_stores/{memory_store_id}/memories`) behaves: results are returned in a stable, server-defined order and the `order_by` and `order` parameters are ignored; `depth` accepts only `0`, `1`, or being omitted (other values return a `400` error); and `path_prefix` must end with `/` and matches whole path segments instead of a substring. Page cursors issued without the header aren't valid with it, so restart from the first page when you adopt it. On memory store endpoints, `agent-memory-2026-07-22` replaces `managed-agents-2026-04-01`; sending both returns a `400` error. On July 22, 2026, the `managed-agents-2026-04-01` header adopts the same list behavior. See [Beta headers](../04-API-Reference/Endpoints/beta-headers.md#endpoint-specific-headers).
- The Python (0.116.0), TypeScript (0.110.0), Go (1.56.0), Java (2.48.0), Ruby (1.55.0), PHP (0.36.0), C# (12.35.0), and CLI (1.16.0) SDKs now send `agent-memory-2026-07-22` on all memory store calls instead of `managed-agents-2026-04-01`. If your code passes `betas` explicitly on memory store calls, replace `managed-agents-2026-04-01` with `agent-memory-2026-07-22` there rather than adding a second value.

### July 1, 2026

- We've restored access to Claude Fable 5 and Claude Mythos 5. See [our statement](../19-Reference/redeploying-fable-5.md) for more information.

### June 30, 2026

- We've launched **Claude Sonnet 5** (`claude-sonnet-5`), the next generation of our Sonnet model family, at introductory pricing of \$2 / \$10 per MTok (made the standard price on August 10, 2026). Claude Sonnet 5 supports a [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md), 128k max output tokens, and the same set of tools and platform features as Claude Sonnet 4.6, except [Priority Tier](../04-API-Reference/Endpoints/service-tiers.md#supported-models), which is not available on Claude Sonnet 5. Three behavior changes apply when migrating: [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) is now on by default; manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) is removed and returns a 400 error (it was deprecated on Sonnet 4.6); and setting sampling parameters (`temperature`, `top_p`, `top_k`) to non-default values returns a 400 error. Claude Sonnet 5 also uses a new tokenizer that produces approximately 30% more tokens for the same text. The exact increase depends on the content and workload shape. See [What's new in Claude Sonnet 5](models-sonnet-5-whats-new-sonnet-5.md) for details and migration guidance. For behavioral differences and model-specific prompting patterns, see [Prompting Claude Sonnet 5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-sonnet-5.md).
- Claude Managed Agents session event streams now support [event deltas](../04-API-Reference/Other/managed-agents-events-and-streaming.md#event-deltas). Opt in with the `event_deltas[]` query parameter on `GET /v1/sessions/{session_id}/events/stream`. The `event_start` and `event_delta` events preview an agent message's text as it's generated, before the complete `agent.message` event arrives.
- [Listing sessions](../04-API-Reference/Other/managed-agents-session-operations.md#listing-sessions) for Claude Managed Agents now supports backward pagination. `GET /v1/sessions` returns a `prev_page` cursor alongside `next_page`; pass it as the `page` parameter to return to the previous page. See [Pagination](../04-API-Reference/Endpoints/overview.md#pagination).
- When creating a Claude Managed Agents session, you can now [override the agent's configuration for that session](../04-API-Reference/Other/managed-agents-sessions.md#override-agent-configuration-for-a-session). Pass `agent` with `type: "agent_with_overrides"` to replace the model, system prompt, tools, MCP servers, or skills for a single session. The agent itself is unchanged.
- Claude Managed Agents vaults now support an `injection_location` setting on [environment variable credentials](../04-API-Reference/Other/managed-agents-vaults.md#add-a-credential) (the Environment variable tab). It controls whether the credential's value is substituted, at egress, into the agent's outbound request headers, the request body, or both.
- Webhooks for Claude Managed Agents now cover the agent, deployment, and deployment run lifecycle. You can react to a newly published agent version, a paused deployment, or a failed scheduled run without polling. See the Agent events, Deployment events, and Deployment run events tabs in [Subscribe to webhooks](../04-API-Reference/Other/managed-agents-webhooks.md#supported-event-types).

### June 29, 2026

- We've removed [fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) for Claude Opus 4.6. Requests to `claude-opus-4-6` with `speed: "fast"` no longer run at fast speed or premium pricing: they run at standard speed, are billed at standard rates, and do not return an error. The response's `usage.speed` field reports the speed used. To continue using fast mode, migrate to [Claude Opus 4.8](about-claude-models-migration-guide.md). Read more in [Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md#supported-models).

### June 26, 2026

- We've raised [rate limits](../04-API-Reference/Endpoints/rate-limits.md) across the Claude API. Claude Sonnet and Claude Haiku rate limits now match Claude Opus at every usage tier, and usage tiers have been consolidated into three: Start, Build, and Scale. Most organizations move to a higher tier, no organization receives lower limits than before, and no action is required. You can view your tier and current limits in the [Claude Console](../04-API-Reference/Other/usage-limits.md).

### June 25, 2026

- We've deprecated [fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) for Claude Opus 4.7, with removal on July 24, 2026. After removal, requests to `claude-opus-4-7` with `speed: "fast"` will return an error. Migrate to fast mode for Claude Opus 4.8. Read more in [Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md#supported-models).

### June 22, 2026

- **MCP tunnels** (research preview): the management API moved from `/v1/organizations/tunnels` on the Admin API to `/v1/tunnels` on the Claude API. The new surface uses the `anthropic-beta: mcp-tunnels-2026-06-22` header and the `workspace:manage_tunnels` WIF scope. The previous surface remains available during a migration window. See the [Tunnels API reference](../04-API-Reference/Endpoints/http-beta-tunnels.md).

### June 18, 2026

- The Python, TypeScript, Go, Java, Ruby, PHP, and C# SDKs now include support for `code_execution_20260120`, the [code execution tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md) version that adds REPL state persistence and is the minimum version for [programmatic tool calling](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md). To adopt it, set the tool's `type` to `code_execution_20260120`; no beta header is required. It's available on Claude Fable 5, Claude Mythos 5, Claude Opus 4.5 and newer, and Claude Sonnet 4.5 and newer; see the code execution tool's [Compatibility](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md#compatibility) section.

### June 15, 2026

- We've retired the Claude Sonnet 4 model (`claude-sonnet-4-20250514`) and the Claude Opus 4 model (`claude-opus-4-20250514`). All requests to these models on the Claude API will now return an error. We recommend upgrading to [Claude Sonnet 4.6](about-claude-models-overview.md#latest-models-comparison) and [Claude Opus 4.8](about-claude-models-overview.md#latest-models-comparison) respectively. Researchers can request ongoing access through the [External Researcher Access Program](../15-Claude-AI-Features/what-is-the-external-researcher-access-program.md).

### June 11, 2026

- The [code execution tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md) now supports `code_execution_20260521`, which discloses the 90-second per-cell execution time limit in the tool description so Claude can budget long-running cells. No beta header is required.
- The [web search tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-search-tool.md) and [web fetch tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md) now support `web_search_20260318` and `web_fetch_20260318`, adding a `response_inclusion` parameter to drop consumed result blocks from the API response for agentic workflows. No beta header is required.

### June 10, 2026

- The `GET /v1/environments/{id}/work` endpoint, which lists pending work for a [self-hosted sandbox](../04-API-Reference/Other/managed-agents-self-hosted-sandboxes.md), is now available on [Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md). See [IAM actions for Claude Platform on AWS](../04-API-Reference/Endpoints/claude-platform-on-aws-iam-actions.md) for the `GetEnvironment` action that authorizes it.

### June 9, 2026

- We've launched **Claude Fable 5** (`claude-fable-5`), our most capable model open to all customers, alongside **Claude Mythos 5** (`claude-mythos-5`) for Project Glasswing participants. Both models support a [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) by default, 128k max output tokens, and always-on [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md). See [Introducing Claude Fable 5 and Claude Mythos 5](models-fable-5-introducing-claude-fable-5-and-claude-mythos-5.md) for capabilities, API changes, and availability.
- Claude Fable 5 and Claude Mythos 5 use the tokenizer introduced with Claude Opus 4.7. Compared to models before Claude Opus 4.7, the same text produces roughly 30% more tokens. The exact increase depends on the content and workload shape. Use the [token counting API](../04-API-Reference/Guides/build-with-claude-token-counting.md#token-counts-on-claude-fable-5) with `model: "claude-fable-5"` to measure your prompts under the new tokenizer.
- Claude Fable 5 runs safety classifiers on requests and during response generation. When a classifier declines a request, the Messages API returns `stop_reason: "refusal"`. You are not billed for a request refused before any output is generated. An opt-in `fallbacks` parameter (in beta on the Claude API and Claude Platform on AWS; not supported on the Message Batches API) re-runs refused requests on another model, billed at the fallback model's rates. See [Handling stop reasons](../04-API-Reference/Guides/build-with-claude-handling-stop-reasons.md).
- The [`stop_details.category`](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#refusal-response) field on refusal responses now includes `"reasoning_extraction"` on Claude Fable 5, returned when a request is blocked under Anthropic's Terms of Service restrictions on reverse engineering or duplicating model outputs. The existing `"cyber"` and `"bio"` categories are unchanged. No beta header is required.
- On Claude Fable 5 and Claude Mythos 5, [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) is the only thinking mode: `thinking: {"type": "disabled"}` is not supported, and manual extended thinking budgets and assistant prefill are not supported (both return a 400 error). See [Migrating from Claude Mythos Preview to Claude Mythos 5](models-fable-5-migration-guide.md#migrating-from-claude-mythos-preview).
- On Claude Fable 5 and Claude Mythos 5, `thinking.display` defaults to `"omitted"`, the same as Claude Opus 4.8, Claude Opus 4.7, and Claude Mythos Preview; set `display: "summarized"` to receive readable thinking summaries. The raw chain of thought is never returned; pass thinking blocks back unchanged in multi-turn conversations on the same model. See [Thinking output on Claude Fable 5 and Claude Mythos 5](../04-API-Reference/Guides/build-with-claude-thinking.md#thinking-output-on-claude-fable-5-and-claude-mythos-5).
- Claude Fable 5 requires 30-day data retention and is not available under zero data retention. See [Model-specific data retention requirements](../04-API-Reference/Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements).
- Claude Managed Agents now supports [scheduled deployments](../04-API-Reference/Other/managed-agents-scheduled-deployments.md), letting you run sessions on a cron schedule without managing your own scheduler.
- Claude Managed Agents vaults now support [environment variable credentials](../04-API-Reference/Other/managed-agents-vaults.md#add-a-credential), so you can securely inject secrets into the agent's sandbox for CLIs, SDKs, and other services that authenticate through environment variables.
- The [Compliance API](../04-API-Reference/Other/manage-claude-compliance-api.md) [Activity Feed](../04-API-Reference/Other/manage-claude-compliance-activity-feed.md) (`GET /v1/compliance/activities`) is now available on [Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md). See [IAM actions for Claude Platform on AWS](../04-API-Reference/Endpoints/claude-platform-on-aws-iam-actions.md#compliance) for the `ListComplianceActivities` action that authorizes it.
- The `session.thread_*` webhook events now include a `session_thread_id` field identifying the multiagent thread that triggered the event.
- We've released a [Swift package](../04-API-Reference/Other/cli-sdks-libraries-libraries-apple-foundation-models.md) in beta that adds Claude as a server-side `LanguageModel` in Apple's Foundation Models framework. Call Claude through the same `LanguageModelSession` API as Apple's on-device model on iOS 27, macOS 27, visionOS 27, and watchOS 27 (beta).

### June 5, 2026

- We announced the deprecation of the Claude Opus 4.1 model (`claude-opus-4-1-20250805`), with retirement on the Claude API scheduled for August 5, 2026. We recommend migrating to [Claude Opus 4.8](about-claude-models-migration-guide.md). Read more in [Model deprecations](about-claude-model-deprecations.md).

### June 2, 2026

- The [advisor tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-advisor-tool.md) now supports a `max_tokens` parameter to cap the advisor model's output per call, reducing latency and output token cost for workloads that don't need full-length advisor responses. Set `tools[].max_tokens` on the advisor tool definition; see [Capping advisor output](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-advisor-tool.md#capping-advisor-output).
- On the Claude API, you are no longer billed for a request when it returns `stop_reason: "refusal"` without Claude having generated any output. See [Streaming refusals](../04-API-Reference/Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md) for detecting and handling refusals.

### May 29, 2026

- Claude Managed Agents [webhooks](../04-API-Reference/Other/managed-agents-webhooks.md), [multiagent orchestration](../04-API-Reference/Other/managed-agents-multiagent-orchestration.md), and [self-hosted sandboxes](../04-API-Reference/Other/managed-agents-self-hosted-sandboxes.md) are now available on [Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md). See [IAM actions for Claude Platform on AWS](../04-API-Reference/Endpoints/claude-platform-on-aws-iam-actions.md) for the new IAM actions and the `AnthropicSelfHostedEnvironmentAccess` managed policy.

### May 28, 2026

- We've launched **Claude Opus 4.8** (
  claude-opus-4-8
  ), our most capable model. Claude Opus 4.8 supports a [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) by default on the Claude API, Amazon Bedrock, Google Cloud, and Microsoft Foundry, 128k max output tokens, and the same set of tools and platform features as Claude Opus 4.7. See the [migration guide](about-claude-models-migration-guide.md) for baseline settings, features, and migration guidance.
- We've launched [mid-conversation system messages](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md). On Claude Opus 4.8, you can send `role: "system"` messages after a user turn (subject to [placement rules](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md#limitations)) in the `messages` array, preserving prompt cache hits when instructions change during a long-running session. No beta header is required.
- The [`stop_details`](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#refusal-response) field on refusal responses is now publicly documented; it returns a `category` (`cyber`, `bio`, or `null`) and a human-readable `explanation`, so your application can route different classes of refusal to the right next step. No beta header is required.
- On Claude Opus 4.8, the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) defaults to `high` across all surfaces, including Claude Code and the Messages API.
- On Claude Opus 4.8, the minimum cacheable prompt length for [prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md) is 1,024 tokens, lower than on Claude Opus 4.7.
- With [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) enabled, Claude Opus 4.8 triggers reasoning only when a turn needs it, reducing wasted thinking tokens compared to Claude Opus 4.7 at the same effort level.
- Claude Opus 4.8 supports [high-resolution image input](../04-API-Reference/Guides/build-with-claude-vision.md#high-resolution-image-support-on-claude-opus-4-7) (up to 2576 pixels on the long edge), same as Claude Opus 4.7.
- [Task budgets](../04-API-Reference/Guides/build-with-claude-task-budgets.md) now support Claude Opus 4.8.
- The [advisor tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-advisor-tool.md) now supports Claude Opus 4.8.
- [Computer use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md) now supports Claude Opus 4.8.
- [Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) for Claude Opus 4.8 is available as a research preview on the Claude API only.
- Setting the sampling parameters `temperature`, `top_p`, or `top_k` to a non-default value returns a 400 error on Claude Opus 4.8, same as on Claude Opus 4.7. See the [migration guide](about-claude-models-migration-guide.md) for details.
- In Claude Code, we've expanded Auto mode to more users for long-running tasks. See the [Claude Code documentation](../02-Claude-Code-CLI/code-home.md).
- In Claude Code, Max plan users now default to [fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) on Claude Opus 4.8. See the [Claude Code documentation](../02-Claude-Code-CLI/code-home.md).
- In Claude Code, Workflows are available as a research preview, letting you define and run multistep agentic plans. See the [Claude Code documentation](../02-Claude-Code-CLI/code-home.md).
- We've deprecated [fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) for Claude Opus 4.6, with removal approximately 30 days after launch. Migrate to fast mode for Claude Opus 4.8 or Claude Opus 4.7. Read more in [Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md#supported-models).
- For updates to claude.ai, Cowork, Claude for Microsoft 365, and other Claude apps in this release, see the [release notes for Claude Apps](../19-Reference/release-notes.md).

### May 27, 2026

- The Messages API response now includes [`usage.output_tokens_details.thinking_tokens`](../04-API-Reference/Guides/build-with-claude-extended-thinking.md#budget-rules-and-tuning), reporting how many of the billed output tokens were extended thinking. When streaming, the breakdown appears only on the final `message_delta` event. No beta header is required.

### May 19, 2026

- [MCP tunnels](../04-API-Reference/Agents-Tools/agents-and-tools-mcp-tunnels-overview.md) is now available as a research preview, so you can connect to MCP servers in your private network.
- Self-hosted sandboxes are now available for Claude Managed Agents, as an alternative to running tool execution in Anthropic's infrastructure. See [Self-hosted sandboxes](../04-API-Reference/Other/managed-agents-self-hosted-sandboxes.md).
- With Claude Managed Agents, you can now update the agent's MCP server and tool configurations associated with an active session.
- With Claude Managed Agents, large outputs from `agent_toolset` and MCP tools exceeding 100K characters (about 25K tokens) are now automatically spilled to a file in the sandbox. The model receives a truncated preview with the file path and can read the full content from there.

### May 18, 2026

- The [web search tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-search-tool.md) now returns richer SEC filing data, making it easier to ground financial research agents, earnings analysis, and due-diligence workflows in primary sources with citations.

### May 13, 2026

- We've launched [cache diagnostics](../04-API-Reference/Guides/build-with-claude-cache-diagnostics.md) in public beta. Pass `diagnostics.previous_message_id` on a Messages request and the API reports a `cache_miss_reason` explaining where the prompt cache prefix diverged from the previous turn. Include the `cache-diagnosis-2026-04-07` beta header in your requests.

### May 12, 2026

- [Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) (research preview) now supports Claude Opus 4.7. Set `speed: "fast"` with `model: "claude-opus-4-7"` and the `fast-mode-2026-02-01` beta header for significantly faster output token generation at premium pricing. Pricing, rate limits, and access are the same as for Opus 4.6 fast mode; interested customers should join the [waitlist](https://claude.com/fast-mode).

### May 11, 2026

- We've launched **Claude Platform on AWS**, bringing the Claude API to Anthropic-managed infrastructure accessible through AWS, with AWS billing and IAM authentication. Access the full Messages API, Files API, Message Batches API, Claude Managed Agents, Agent Skills, code execution, and tool use through native AWS endpoints. Learn more in [Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md).

### May 6, 2026

- [Multiagent orchestration](../04-API-Reference/Other/managed-agents-multiagent-orchestration.md) and [Outcomes](../04-API-Reference/Other/managed-agents-define-outcomes.md) are now in public beta under the standard `managed-agents-2026-04-01` beta header.
- Claude Managed Agents vault credential background refresh is now supported for `mcp_oauth` credentials. See [Authenticate with vaults](../04-API-Reference/Other/managed-agents-vaults.md).
- Webhooks for Claude Managed Agents are now supported. Webhook event types include session and vault lifecycle events. See [Subscribe to webhooks](../04-API-Reference/Other/managed-agents-webhooks.md).
- Additional filtering and sorting options are now supported for Claude Managed Agents. Sessions can be filtered by status, and events can be filtered by type. Events can now be filtered by creation time.
- [Dreams](../04-API-Reference/Other/managed-agents-dreams.md) for Claude Managed Agents are now available as a research preview. A dream reads an existing memory store alongside past session transcripts and produces a reorganized output memory store with duplicates merged, stale entries replaced, and new insights surfaced. Dream endpoints are gated by the `dreaming-2026-04-21` beta header. [Request access](https://claude.com/form/claude-managed-agents) to try it.

### May 4, 2026

- We've launched [Workload Identity Federation](../04-API-Reference/Other/manage-claude-workload-identity-federation.md). Authenticate workloads to the Claude API with short-lived OIDC tokens from your own identity provider (AWS IAM, Google Cloud, GitHub Actions, Kubernetes, Microsoft Entra ID, Okta, SPIFFE, and more) instead of long-lived static API keys. Configure issuers and federation rules in the Claude Console, and the SDK handles token exchange and refresh automatically. See [Authentication](../04-API-Reference/Other/manage-claude-authentication.md).

### April 30, 2026

- We've retired the 1M token context window beta (`context-1m-2025-08-07`) for Claude Sonnet 4.5 and Claude Sonnet 4. The beta header now has no effect on these models, and requests exceeding the standard 200k-token context window return an error. To use the 1M context window, migrate to [Claude Sonnet 4.6](about-claude-models-overview.md#latest-models-comparison) or [Claude Opus 4.6](about-claude-models-overview.md#latest-models-comparison), where it's included at standard pricing with no beta header required.

### April 29, 2026

- We've released the [Claude API skill](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md), an open-source [Agent Skill](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-overview.md) that gives Claude up-to-date reference material for building on the Messages API and Claude Managed Agents across 8 languages. The skill is bundled with Claude Code and available in the [Anthropic skills repository](https://github.com/anthropics/skills/tree/main/skills/claude-api).

### April 24, 2026

- We've released the [Rate Limits API](../04-API-Reference/Other/manage-claude-rate-limits-api.md), allowing administrators to programmatically query the rate limits configured for their organization and workspaces.

### April 23, 2026

- Memory for Claude Managed Agents is now in public beta under the standard `managed-agents-2026-04-01` header. See [Using agent memory](../04-API-Reference/Other/managed-agents-memory.md) for the full integration guide.

### April 20, 2026

- We've retired the Claude Haiku 3 model (`claude-3-haiku-20240307`). All requests to this model will now return an error. We recommend upgrading to [Claude Haiku 4.5](about-claude-models-overview.md#latest-models-comparison).

### April 16, 2026

- We've launched [Claude Opus 4.7](../19-Reference/claude-opus-4-7.md), our most capable model for complex reasoning and agentic coding, at the same \$5 / \$25 per MTok pricing as Opus 4.6. See [What's new in Claude Opus 4.7](about-claude-models-whats-new-claude-4-7.md) for capability improvements, new features, and the updated tokenizer. Opus 4.7 includes API breaking changes versus Opus 4.6; see the [migration guide](about-claude-models-migration-guide.md) before upgrading.
- [Claude in Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md) is now open to all Amazon Bedrock customers. Claude Opus 4.7 and Claude Haiku 4.5 are available self-serve from the Bedrock console through the Messages API endpoint at `/anthropic/v1/messages`, in 27 AWS regions with global and regional endpoints.
- We've launched [task budgets](../04-API-Reference/Guides/build-with-claude-task-budgets.md) in beta on Claude Opus 4.7. Give Claude an advisory token budget for a full agentic loop (thinking, tool calls, tool results, and output) and the model sees a running countdown, using it to prioritize work and finish gracefully as the budget is consumed. Include the `task-budgets-2026-03-13` beta header in your requests.
- Claude Opus 4.7 supports [high-resolution image input](../04-API-Reference/Guides/build-with-claude-vision.md#high-resolution-image-support-on-claude-opus-4-7), raising the maximum image resolution from 1568 to 2576 pixels on the long edge for improved performance on computer use, screenshot understanding, and document analysis. High-resolution support is automatic and requires no beta header; images may use up to approximately 3x more image tokens than on prior models.
- We've added the `xhigh` [effort](../04-API-Reference/Guides/build-with-claude-effort.md) level on Claude Opus 4.7. `xhigh` sits between `high` and `max` and is tuned for long-running agentic and coding tasks (over 30 minutes) with token budgets in the millions. No beta header is required.

### April 14, 2026

- We announced the deprecation of the Claude Sonnet 4 model (`claude-sonnet-4-20250514`) and the Claude Opus 4 model (`claude-opus-4-20250514`), with retirement on the Claude API scheduled for June 15, 2026. We recommend migrating to [Claude Sonnet 4.6](about-claude-models-overview.md#latest-models-comparison) and [Claude Opus 4.8](about-claude-models-migration-guide.md) respectively. Read more in [Model deprecations](about-claude-model-deprecations.md).

### April 9, 2026

- We've launched the [advisor tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-advisor-tool.md) in public beta. Pair a faster executor model with a higher-intelligence advisor model that provides strategic guidance mid-generation, so long-horizon agentic workloads get close to advisor-solo quality while the bulk of token generation happens at executor-model rates. Include the beta header `advisor-tool-2026-03-01` in your requests.

### April 8, 2026

- We've launched **Claude Managed Agents** in public beta, a fully managed agent harness for running Claude as an autonomous agent with secure sandboxing, built-in tools, and server-sent event streaming. Create agents, configure containers, and run sessions through the API. All endpoints require the `managed-agents-2026-04-01` beta header. Learn more in [Claude Managed Agents overview](../04-API-Reference/Other/managed-agents-overview.md).
- We've launched the **`ant` CLI**, a command-line client for the Claude API that enables faster interaction with the Claude API, native integration with Claude Code, and versioning of API resources in YAML files. Learn more in the [CLI quickstart](../04-API-Reference/Other/cli-sdks-libraries-cli-quickstart.md).

### April 7, 2026

- We announced [Claude Mythos Preview](../22-Safety-Policy/glasswing.md) is available as a gated research preview for defensive cybersecurity work as part of [Project Glasswing](../22-Safety-Policy/glasswing.md). Access is invitation-only.
- The [Messages API](../04-API-Reference/Endpoints/messages.md) is now available on Amazon Bedrock as a research preview. The new Claude in Amazon Bedrock endpoint at `/anthropic/v1/messages` uses the same request shape as the first-party Claude API and runs on AWS-managed infrastructure with zero operator access. Available in `us-east-1`; contact your Anthropic account executive to request access. Learn more in [Claude in Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md).

### March 30, 2026

- We've raised the `max_tokens` cap to 300k on the [Message Batches API](../04-API-Reference/Guides/build-with-claude-batch-processing.md#extended-output-beta) for Claude Opus 4.6 and Sonnet 4.6. Include the `output-300k-2026-03-24` beta header to generate longer single-turn outputs for long-form content, structured data, and large code generation tasks.
- We're retiring the 1M token context window beta for Claude Sonnet 4.5 and Claude Sonnet 4 on **April 30, 2026**. After that date, the `context-1m-2025-08-07` beta header will have no effect on these models, and requests that exceed the standard 200k-token context window will return an error. To continue using 1M context windows, migrate to [Claude Sonnet 4.6](about-claude-models-overview.md#latest-models-comparison) or [Claude Opus 4.6](about-claude-models-overview.md#latest-models-comparison), which support the full 1M token context window at standard pricing with no beta header required.

### March 18, 2026

- We've added model capability fields to the [Models API](../04-API-Reference/Endpoints/models-list.md). `GET /v1/models` and `GET /v1/models/{model_id}` now return `max_input_tokens`, `max_tokens`, and a `capabilities` object. Query the API to discover what each model supports.

### March 16, 2026

- We've launched the `display` field for extended thinking, letting you omit thinking content from responses for faster streaming. Set `thinking.display: "omitted"` to receive thinking blocks with an empty `thinking` field and the `signature` preserved for multi-turn continuity. Billing is unchanged. Learn more in [Controlling thinking display](../04-API-Reference/Guides/build-with-claude-thinking.md#controlling-thinking-display).

### March 13, 2026

- The [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) is out of beta for Claude Opus 4.6 and Sonnet 4.6, at standard pricing. Requests over 200k tokens work automatically for these models with no beta header required. The 1M token context window remains in beta for Claude Sonnet 4.5 and Sonnet 4.
- We've removed the dedicated 1M rate limits for all supported models. Your standard account limits now apply across every context length.
- We've raised the media limit from 100 to 600 images or PDF pages per request when using the 1M token context window.

### February 19, 2026

- We've launched **automatic caching** for the Messages API. Add a single `cache_control` field to your request body and the system automatically caches the last cacheable block, moving the cache point forward as conversations grow. No manual breakpoint management required. Works alongside existing block-level cache control for fine-grained optimization. Available on the Claude API and Microsoft Foundry (preview). Learn more in [Prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md#automatic-caching).
- We've retired the Claude Sonnet 3.7 model (`claude-3-7-sonnet-20250219`) and the Claude Haiku 3.5 model (`claude-3-5-haiku-20241022`). All requests to Claude Sonnet 3.7 will now return an error. Requests to Claude Haiku 3.5 on the Claude API will now return an error; it remains available on Amazon Bedrock and Google Cloud. We recommend upgrading to [Claude Sonnet 4.6](about-claude-models-overview.md#latest-models-comparison) and [Claude Haiku 4.5](about-claude-models-overview.md#latest-models-comparison) respectively. Researchers can request ongoing access through the [External Researcher Access Program](../15-Claude-AI-Features/what-is-the-external-researcher-access-program.md).
- We announced the deprecation of the Claude Haiku 3 model (`claude-3-haiku-20240307`), with retirement scheduled for April 20, 2026. We recommend migrating to [Claude Haiku 4.5](about-claude-models-overview.md#latest-models-comparison). Read more in [Model deprecations](about-claude-model-deprecations.md).

### February 17, 2026

- We've launched [Claude Sonnet 4.6](../19-Reference/claude-sonnet-4-6.md), our latest balanced model combining speed and intelligence for everyday tasks. Sonnet 4.6 delivers improved agentic search performance while consuming fewer tokens. Sonnet 4.6 supports [extended thinking](../04-API-Reference/Guides/build-with-claude-extended-thinking.md) and a [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) (beta). See [Models & Pricing](about-claude-models-overview.md) for details.
- API [code execution](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md) is now **free when used with web search or web fetch**. Sandboxed code execution improves model capability and token efficiency. See the [pricing details](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md#usage-and-pricing) for standalone usage.
- The [web search tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-search-tool.md) and [programmatic tool calling](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md) are available with no beta header required. Web search and web fetch now support [dynamic filtering](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-search-tool.md#dynamic-filtering), which uses code execution to filter results before they reach the context window for better performance and reduced token cost.
- The [code execution tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md), [web fetch tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md), [tool search tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-tool-search-tool.md), [tool use examples](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md#providing-tool-use-examples), and [memory tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-memory-tool.md) no longer require a beta header.

### February 7, 2026

- We've launched [fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) in research preview for Opus 4.6, providing significantly faster output token generation through the `speed` parameter. Fast mode is up to 2.5x as fast at premium pricing. Interested customers should join the [waitlist](https://claude.com/fast-mode).

### February 5, 2026

- We've launched [Claude Opus 4.6](../19-Reference/claude-opus-4-6.md), our most intelligent model for complex agentic tasks and long-horizon work. Opus 4.6 recommends [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) (`thinking: {type: "adaptive"}`); manual thinking (`type: "enabled"` with `budget_tokens`) is deprecated. Opus 4.6 does not support prefilling assistant messages. Learn more in [What's new in Claude 4.6](about-claude-models-whats-new-claude-4-6.md).
- The [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) no longer requires a beta header and now supports Claude Opus 4.6. Effort replaces `budget_tokens` for controlling thinking depth on new models.
- We've launched the [compaction API](../04-API-Reference/Guides/build-with-claude-compaction-threshold.md) in beta, providing server-side context summarization for effectively infinite conversations. Available on Opus 4.6.
- We've introduced [data residency controls](../04-API-Reference/Guides/build-with-claude-data-residency.md), allowing you to specify where model inference runs with the `inference_geo` parameter. US-only inference is available at 1.1x pricing for models released after February 1, 2026.
- The [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) is now available in beta for Claude Opus 4.6, in addition to Sonnet 4.5 and Sonnet 4. [Long context pricing](../17-Billing-Plans/about-claude-pricing.md#long-context-pricing) applies to requests exceeding 200k input tokens.
- [Fine-grained tool streaming](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-fine-grained-tool-streaming.md) no longer requires a beta header on any model or platform.

### January 29, 2026

- [Structured outputs](../04-API-Reference/Guides/build-with-claude-structured-outputs.md) are out of beta on the Claude API for Claude Sonnet 4.5, Claude Opus 4.5, and Claude Haiku 4.5. This release includes expanded schema support, improved grammar compilation latency, and a simplified integration path with no beta header required. The `output_format` parameter has moved to `output_config.format`. Existing beta users can continue using the beta header during the transition period. Structured outputs remain in public beta on Amazon Bedrock and Microsoft Foundry.

### January 12, 2026

- `console.anthropic.com` now redirects to `platform.claude.com`. The Claude Console has moved to its new home as part of our Claude brand consolidation. Existing bookmarks and links will continue working through an automatic redirect. For more details, see the [September 16, 2025 announcement](#september-16-2025).

### January 5, 2026

- We've retired the Claude Opus 3 model (`claude-3-opus-20240229`). All requests to this model will now return an error. We recommend upgrading to [Claude Opus 4.5](about-claude-models-overview.md#latest-models-comparison), which offers significantly improved intelligence at a third of the cost. Researchers can request ongoing access to Claude Opus 3 on the API through the [External Researcher Access Program](../15-Claude-AI-Features/what-is-the-external-researcher-access-program.md).

### December 19, 2025

- We announced the deprecation of the Claude Haiku 3.5 model. Read more in [Model deprecations](about-claude-model-deprecations.md).

### December 4, 2025

- [Structured outputs](../04-API-Reference/Guides/build-with-claude-structured-outputs.md) now supports Claude Haiku 4.5.

### November 24, 2025

- We've launched [Claude Opus 4.5](../19-Reference/claude-opus-4-5.md), our most intelligent model combining maximum capability with practical performance. Ideal for complex specialized tasks, professional software engineering, and advanced agents. Features step-change improvements in vision, coding, and computer use at a more accessible price point than previous Opus models. Learn more in [Models overview](about-claude-models-overview.md).
- We've launched [programmatic tool calling](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md) in public beta, allowing Claude to call tools from within code execution to reduce latency and token usage in multi-tool workflows.
- We've launched the [tool search tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-tool-search-tool.md) in public beta, enabling Claude to dynamically discover and load tools on-demand from large tool catalogs.
- We've launched the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) in public beta for Claude Opus 4.5, allowing you to control token usage by trading off between response thoroughness and efficiency.
- We've added [client-side compaction](../04-API-Reference/Guides/build-with-claude-context-editing.md#client-side-compaction-sdk) to our Python and TypeScript SDKs, automatically managing conversation context through summarization when using `tool_runner`.

### November 21, 2025

- Search result content blocks are now available on Amazon Bedrock with no beta header required. Learn more in [Search results](../04-API-Reference/Guides/build-with-claude-search-results.md).

### November 19, 2025

- We've launched a **new documentation platform** at [platform.claude.com/docs](../04-API-Reference/Other/home.md). Our documentation now lives side by side with the Claude Console, providing a unified developer experience. The previous docs site at docs.claude.com will redirect to the new location.

### November 18, 2025

- We've launched **Claude in Microsoft Foundry**, bringing Claude models to Azure customers with Azure billing and OAuth authentication. Access the full Messages API including extended thinking, prompt caching (5-minute and 1-hour), PDF support, Files API, Agent Skills, and tool use. Learn more in [Claude in Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md).

### November 14, 2025

- We've launched [structured outputs](../04-API-Reference/Guides/build-with-claude-structured-outputs.md) in public beta, providing guaranteed schema conformance for Claude's responses. Use JSON outputs for structured data responses or strict tool use for validated tool inputs. Available for Claude Sonnet 4.5 and Claude Opus 4.1. To enable, use the beta header `structured-outputs-2025-11-13`.

### October 28, 2025

- We announced the deprecation of the Claude Sonnet 3.7 model. Read more in [Model deprecations](about-claude-model-deprecations.md).
- We've retired the Claude Sonnet 3.5 models. All requests to these models will now return an error.
- We've expanded context editing with thinking block clearing (`clear_thinking_20251015`), enabling automatic management of thinking blocks. Learn more in [Context editing](../04-API-Reference/Guides/build-with-claude-context-editing.md).

### October 16, 2025

- We've launched [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) (`skills-2025-10-02` beta), a new way to extend Claude's capabilities. Skills are organized folders of instructions, scripts, and resources that Claude loads dynamically to perform specialized tasks. The initial release includes:
  - **Anthropic-managed Skills**: Pre-built Skills for working with PowerPoint (.pptx), Excel (.xlsx), Word (.docx), and PDF files
  - **Custom Skills**: Upload your own Skills through the Skills API (`/v1/skills` endpoints) to package domain expertise and organizational workflows
  - Skills require the [code execution tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md) to be enabled
  - Learn more in [Agent Skills](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-overview.md) and [API reference](../04-API-Reference/Endpoints/skills-create.md)

### October 15, 2025

- We've launched [Claude Haiku 4.5](../19-Reference/claude-haiku-4-5.md), our fastest and most intelligent Haiku model with near-frontier performance. Ideal for real-time applications, high-volume processing, and cost-sensitive deployments requiring strong reasoning. Learn more in [Models overview](about-claude-models-overview.md).

### September 29, 2025

- We've launched [Claude Sonnet 4.5](../19-Reference/claude-sonnet-4-5.md), our best model for complex agents and coding, with the highest intelligence across most tasks. Learn more in the [models overview](about-claude-models-overview.md).
- We've introduced [global endpoint pricing](../17-Billing-Plans/about-claude-pricing.md#cloud-platform-pricing) for Amazon Bedrock and Vertex AI. The Claude API (1P) pricing is unaffected.
- We've introduced a new stop reason `model_context_window_exceeded` that allows you to request the maximum possible tokens without calculating input size. Learn more in [Handling stop reasons](../04-API-Reference/Guides/build-with-claude-handling-stop-reasons.md).
- We've launched the memory tool in beta, enabling Claude to store and consult information across conversations. Learn more in [Memory tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-memory-tool.md).
- We've launched context editing in beta, providing strategies to automatically manage conversation context. The initial release supports clearing older tool results and calls when approaching token limits. Learn more in [Context editing](../04-API-Reference/Guides/build-with-claude-context-editing.md).

### September 17, 2025

- We've launched tool helpers in beta for the Python and TypeScript SDKs, simplifying tool creation and execution with type-safe input validation and a tool runner for automated tool handling in conversations. For details, see the documentation for [the Python SDK](https://github.com/anthropics/anthropic-sdk-python/blob/main/tools.md) and [the TypeScript SDK](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/helpers.md#tool-helpers).

### September 16, 2025

- We've unified our developer offerings under the Claude brand. You should see updated naming and URLs across our platform and documentation, but **our developer interfaces will remain the same**. Here are some notable changes:
  - Claude Console ([console.anthropic.com](https://console.anthropic.com)) → Claude Console ([platform.claude.com](../04-API-Reference/Other/usage-limits.md)). The console will be available at both URLs until January 12, 2026. After that date, [console.anthropic.com](https://console.anthropic.com) will automatically redirect to [platform.claude.com](../04-API-Reference/Other/usage-limits.md).
  - Anthropic Docs ([docs.anthropic.com](../04-API-Reference/Other/usage-limits.md)) → Claude Docs ([docs.claude.com](https://docs.claude.com))
  - Anthropic Help Center ([support.anthropic.com](https://support.anthropic.com)) → Claude Help Center ([support.claude.com](https://support.claude.com))
  - API endpoints, headers, environment variables, and SDKs remain the same. Your existing integrations will continue working without any changes.

### September 10, 2025

- We've launched the web fetch tool in beta, allowing Claude to retrieve full content from specified web pages and PDF documents. Learn more in [Web fetch tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md).
- We've launched the [Claude Code Analytics API](../04-API-Reference/Other/manage-claude-claude-code-analytics-api.md), enabling organizations to programmatically access daily aggregated usage metrics for Claude Code, including productivity metrics, tool usage statistics, and cost data.

### September 8, 2025

- We launched a beta version of the [C# SDK](https://github.com/anthropics/anthropic-sdk-csharp).

### September 5, 2025

- We've launched [rate limit charts](../04-API-Reference/Endpoints/rate-limits.md#monitoring-your-rate-limits-in-the-console) in the Console [Usage](https://console.anthropic.com/settings/usage) page, allowing you to monitor your API rate limit usage and caching rates over time.

### September 3, 2025

- We've launched support for citable documents in client-side tool results. Learn more in [Handle tool calls](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-handle-tool-calls.md).

### September 2, 2025

- We've launched v2 of the [Code Execution Tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md) in public beta, replacing the original Python-only tool with Bash command execution and direct file manipulation capabilities, including writing code in other languages.

### August 27, 2025

- We launched a beta version of the [PHP SDK](https://github.com/anthropics/anthropic-sdk-php).

### August 26, 2025

- We've increased rate limits on the [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) for Claude Sonnet 4 on the Claude API.
- The 1M token context window is now available on Vertex AI. For more information, see [Claude on Vertex AI](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md).

### August 19, 2025

- Request IDs are now included directly in error response bodies alongside the existing `request-id` header. Learn more in [Errors](../04-API-Reference/Endpoints/errors.md#error-shapes).

### August 18, 2025

- We've released the [Usage & Cost API](../04-API-Reference/Other/manage-claude-usage-cost-api.md), allowing administrators to programmatically monitor their organization's usage and cost data.
- We've added a new endpoint to the Admin API for retrieving organization information. For details, see the [Organization Info Admin API reference](../04-API-Reference/Admin/beta-organization-retrieve.md).

### August 13, 2025

- We announced the deprecation of the Claude Sonnet 3.5 models (`claude-3-5-sonnet-20240620` and `claude-3-5-sonnet-20241022`). These models will be retired on October 28, 2025. We recommend migrating to Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`) for improved performance and capabilities. Read more in [Model deprecations](about-claude-model-deprecations.md).
- The 1-hour cache duration for prompt caching no longer requires a beta header. Learn more in [Prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md#1-hour-cache-duration).

### August 12, 2025

- We've launched beta support for a [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) in Claude Sonnet 4 on the Claude API and Amazon Bedrock.

### August 11, 2025

- Some customers might encounter 429 (`rate_limit_error`) [errors](../04-API-Reference/Endpoints/errors.md) following a sharp increase in API usage due to acceleration limits on the API. Previously, 529 (`overloaded_error`) errors would occur in similar scenarios.

### August 8, 2025

- Search result content blocks are out of beta on the Claude API and Vertex AI. This feature enables natural citations for RAG applications with proper source attribution. The beta header `search-results-2025-06-09` is no longer required. Learn more in [Search results](../04-API-Reference/Guides/build-with-claude-search-results.md).

### August 5, 2025

- We've launched [Claude Opus 4.1](../19-Reference/claude-opus-4-1.md), an incremental update to Claude Opus 4 with enhanced capabilities and performance improvements.^(\*) Learn more in [Models overview](about-claude-models-overview.md).

*^(\*Opus 4.1 does not allow both `temperature` and `top_p` parameters to be specified. Please use only one.)*

### July 28, 2025

- We've released `text_editor_20250728`, an updated text editor tool that fixes some issues from the previous versions and adds an optional `max_characters` parameter that allows you to control the truncation length when viewing large files.

### July 24, 2025

- We've increased [rate limits](../04-API-Reference/Endpoints/rate-limits.md) for Claude Opus 4 on the Claude API to give you more capacity to build and scale with Claude. For customers with [usage tier 1-4 rate limits](../04-API-Reference/Endpoints/rate-limits.md#rate-limits), these changes apply immediately to your account - no action needed.

### July 21, 2025

- We've retired the Claude 2.0, Claude 2.1, and Claude Sonnet 3 models. All requests to these models will now return an error. Read more in [Model deprecations](about-claude-model-deprecations.md).

### July 17, 2025

- We've increased [rate limits](../04-API-Reference/Endpoints/rate-limits.md) for Claude Sonnet 4 on the Claude API to give you more capacity to build and scale with Claude. For customers with [usage tier 1-4 rate limits](../04-API-Reference/Endpoints/rate-limits.md#rate-limits), these changes apply immediately to your account - no action needed.

### July 3, 2025

- We've launched search result content blocks in beta, enabling natural citations for RAG applications. Tools can now return search results with proper source attribution, and Claude will automatically cite these sources in its responses - matching the citation quality of web search. This eliminates the need for document workarounds in custom knowledge base applications. Learn more in [Search results](../04-API-Reference/Guides/build-with-claude-search-results.md). To enable this feature, use the beta header `search-results-2025-06-09`.

### June 30, 2025

- We announced the deprecation of the Claude Opus 3 model. Read more in [Model deprecations](about-claude-model-deprecations.md).

### June 23, 2025

- Console users with the Developer role can now access the [Cost](https://console.anthropic.com/settings/cost) page. Previously, the Developer role allowed access to the [Usage](https://console.anthropic.com/settings/usage) page, but not the Cost page.

### June 11, 2025

- We've launched [fine-grained tool streaming](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-fine-grained-tool-streaming.md) in public beta, a feature that enables Claude to stream tool use parameters without buffering / JSON validation. To enable fine-grained tool streaming, use the [beta header](../04-API-Reference/Endpoints/beta-headers.md) `fine-grained-tool-streaming-2025-05-14`.

### May 22, 2025

- We've launched [Claude Opus 4 and Claude Sonnet 4](../19-Reference/claude-4.md), our latest models with extended thinking capabilities. Learn more in [Models overview](about-claude-models-overview.md).
- The default behavior of [extended thinking](../04-API-Reference/Guides/build-with-claude-extended-thinking.md) in Claude 4 models returns a summary of Claude's full thinking process, with the full thinking encrypted and returned in the `signature` field of `thinking` block output.
- We've launched [interleaved thinking](../04-API-Reference/Guides/build-with-claude-thinking.md#interleaved-thinking) in public beta, a feature that enables Claude to think in between tool calls. To enable interleaved thinking, use the [beta header](../04-API-Reference/Endpoints/beta-headers.md) `interleaved-thinking-2025-05-14`.
- We've launched the [Files API](../04-API-Reference/Guides/build-with-claude-files.md) in public beta, enabling you to upload files and reference them in the Messages API and code execution tool.
- We've launched the [Code execution tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md) in public beta, a tool that enables Claude to execute Python code in a secure, sandboxed environment.
- We've launched the [MCP connector](../04-API-Reference/Agents-Tools/agents-and-tools-mcp-connector.md) in public beta, a feature that allows you to connect to remote MCP servers directly from the Messages API.
- To increase answer quality and decrease tool errors, we've changed the default value for the `top_p` [nucleus sampling](https://en.wikipedia.org/wiki/Top-p_sampling) parameter in the Messages API from 0.999 to 0.99 for all models. To revert this change, set `top_p` to 0.999. Additionally, when extended thinking is enabled, you can now set `top_p` to values between 0.95 and 1.
- Our [Go SDK](https://github.com/anthropics/anthropic-sdk-go) has moved from beta to its first stable release.
- We've included minute and hour level granularity to the [Usage](https://console.anthropic.com/settings/usage) page of Console alongside 429 error rates on the Usage page.

### May 21, 2025

- Our [Ruby SDK](https://github.com/anthropics/anthropic-sdk-ruby) has moved from beta to its first stable release.

### May 7, 2025

- We've launched a web search tool in the API, allowing Claude to access up-to-date information from the web. Learn more in [Web search tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-web-search-tool.md).

### May 1, 2025

- Cache control must now be specified directly in the parent `content` block of `tool_result` and `document.source`. For backwards compatibility, if cache control is detected on the last block in `tool_result.content` or `document.source.content`, it will be automatically applied to the parent block instead. Cache control on any other blocks within `tool_result.content` and `document.source.content` will result in a validation error.

### April 9th, 2025

- We launched a beta version of the [Ruby SDK](https://github.com/anthropics/anthropic-sdk-ruby).

### March 31st, 2025

- Our [Java SDK](https://github.com/anthropics/anthropic-sdk-java) has moved from beta to its first stable release.
- We've moved our [Go SDK](https://github.com/anthropics/anthropic-sdk-go) from alpha to beta.

### February 27th, 2025

- We've added URL source blocks for images and PDFs in the Messages API. You can now reference images and PDFs directly through a URL instead of having to base64-encode them. Learn more in [Vision](../04-API-Reference/Guides/build-with-claude-vision.md) and [PDF support](../04-API-Reference/Guides/build-with-claude-pdf-support.md).
- We've added support for a `none` option to the `tool_choice` parameter in the Messages API that prevents Claude from calling any tools. Additionally, you're no longer required to provide any `tools` when including `tool_use` and `tool_result` blocks.
- We've launched an OpenAI-compatible API endpoint, allowing you to test Claude models by changing just your API key, base URL, and model name in existing OpenAI integrations. This compatibility layer supports core chat completions functionality. Learn more in [OpenAI SDK compatibility](../04-API-Reference/Other/cli-sdks-libraries-libraries-openai-sdk.md).

### February 24th, 2025

- We've launched [Claude Sonnet 3.7](../19-Reference/claude-3-7-sonnet.md), our most intelligent model yet. Claude Sonnet 3.7 can produce near-instant responses or show its extended thinking step-by-step. One model, two ways to think. Learn more about all Claude models in [Models overview](about-claude-models-overview.md).
- We've added vision support to Claude Haiku 3.5, enabling the model to analyze and understand images.
- We've released a token-efficient tool use implementation, improving overall performance when using tools with Claude. Learn more in [Tool use with Claude](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md).
- We've changed the default temperature in the [Console](https://console.anthropic.com/workbench) for new prompts from 0 to 1 for consistency with the default temperature in the API. Existing saved prompts are unchanged.
- We've released updated versions of our tools that decouple the text edit and bash tools from the computer use system prompt:
  - `bash_20250124`: Same functionality as previous version but is independent from computer use. Does not require a beta header.
  - `text_editor_20250124`: Same functionality as previous version but is independent from computer use. Does not require a beta header.
  - `computer_20250124`: Updated computer use tool with new command options including "hold_key", "left_mouse_down", "left_mouse_up", "scroll", "triple_click", and "wait". This tool requires the "computer-use-2025-01-24" anthropic-beta header. Learn more in [Tool use with Claude](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md).

### February 10th, 2025

- We've added the `anthropic-organization-id` response header to all API responses. This header provides the organization ID associated with the API key used in the request.

### January 31st, 2025

- We've moved our [Java SDK](https://github.com/anthropics/anthropic-sdk-java) from alpha to beta.

### January 23rd, 2025

- We've launched citations capability in the API, allowing Claude to provide source attribution for information. Learn more in [Citations](../04-API-Reference/Guides/build-with-claude-citations.md).
- We've added support for plain text documents and custom content documents in the Messages API.

### January 21st, 2025

- We announced the deprecation of the Claude 2, Claude 2.1, and Claude Sonnet 3 models. Read more in [Model deprecations](about-claude-model-deprecations.md).

### January 15th, 2025

- We've updated [prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md) to be easier to use. Now, when you set a cache breakpoint, we'll automatically read from your longest previously cached prefix.
- You can now put words in Claude's mouth when using tools.

### January 10th, 2025

- We've optimized support for [prompt caching in the Message Batches API](../04-API-Reference/Guides/build-with-claude-batch-processing.md#using-prompt-caching-with-message-batches) to improve cache hit rate.

### December 19th, 2024

- We've added support for a [delete endpoint](../04-API-Reference/Endpoints/messages-batches-delete.md) in the Message Batches API.

### December 17th, 2024

The following features are now available in the Claude API without a beta header:

- [Models API](../04-API-Reference/Endpoints/models-list.md): Query available models, validate model IDs, and resolve [model aliases](about-claude-models-overview.md) to their canonical model IDs.
- [Message Batches API](../04-API-Reference/Guides/build-with-claude-batch-processing.md): Process large batches of messages asynchronously at 50% of the standard API cost.
- [Token counting API](../04-API-Reference/Guides/build-with-claude-token-counting.md): Calculate token counts for Messages before sending them to Claude.
- [Prompt Caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md): Reduce costs by up to 90% and latency by up to 80% by caching and reusing prompt content.
- [PDF support](../04-API-Reference/Guides/build-with-claude-pdf-support.md): Process PDFs to analyze both text and visual content within documents.

We also released new official SDKs:

- [Java SDK](https://github.com/anthropics/anthropic-sdk-java) (alpha)
- [Go SDK](https://github.com/anthropics/anthropic-sdk-go) (alpha)

### December 4th, 2024

- We've added the ability to group by API key on the [Usage](https://console.anthropic.com/settings/usage) and [Cost](https://console.anthropic.com/settings/cost) pages of the [Developer Console](https://console.anthropic.com).
- We've added two new **Last used at** and **Cost** columns and the ability to sort by any column on the [API keys](https://console.anthropic.com/settings/keys) page of the [Developer Console](https://console.anthropic.com).

### November 21st, 2024

- We've released the [Admin API](../04-API-Reference/Other/manage-claude-admin-api.md), allowing users to programmatically manage their organization's resources.

### November 20th, 2024

- We've updated our rate limits for the Messages API. We've replaced the tokens per minute rate limit with new input and output tokens per minute rate limits. Read more in [Rate limits](../04-API-Reference/Endpoints/rate-limits.md).
- We've added support for [tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md) in the [Workbench](https://console.anthropic.com/workbench).

### November 13th, 2024

- We've added PDF support for all Claude Sonnet 3.5 models. Read more in [PDF support](../04-API-Reference/Guides/build-with-claude-pdf-support.md).

### November 6th, 2024

- We've retired the Claude 1 and Instant models. Read more in [Model deprecations](about-claude-model-deprecations.md).

### November 4th, 2024

- [Claude Haiku 3.5](../15-Claude-AI-Features/claude-haiku.md) is now available on the Claude API as a text-only model.

### November 1st, 2024

- We've added PDF support for use with the new Claude Sonnet 3.5. Read more in [PDF support](../04-API-Reference/Guides/build-with-claude-pdf-support.md).
- We've also added token counting, which allows you to determine the total number of tokens in a Message prior to sending it to Claude. Read more in [Token counting](../04-API-Reference/Guides/build-with-claude-token-counting.md).

### October 22nd, 2024

- We've added Anthropic-defined computer use tools to our API for use with the new Claude Sonnet 3.5. Read more in [Computer use tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md).
- Claude Sonnet 3.5, our most intelligent model yet, just got an upgrade and is now available on the Claude API. Read more in the [Claude Sonnet documentation](../15-Claude-AI-Features/claude-sonnet.md).

### October 8th, 2024

- The Message Batches API is now available in beta. Process large batches of queries asynchronously in the Claude API for 50% less cost. Read more in [Batch processing](../04-API-Reference/Guides/build-with-claude-batch-processing.md).
- We've loosened restrictions on the ordering of `user`/`assistant` turns in our Messages API. Consecutive `user`/`assistant` messages will be combined into a single message instead of erroring, and we no longer require the first input message to be a `user` message.
- We've deprecated the Build and Scale plans in favor of a standard feature suite (formerly referred to as Build), along with additional features that are available through sales. Read more in our [API pricing information](https://claude.com/platform/api).

### October 3rd, 2024

- We've added the ability to disable parallel tool use in the API. Set `disable_parallel_tool_use: true` in the `tool_choice` field to ensure that Claude uses at most one tool. Read more in [Parallel tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-parallel-tool-use.md).

### September 10th, 2024

- We've added Workspaces to the [Developer Console](https://console.anthropic.com). Workspaces allow you to set custom spend or rate limits, group API keys, track usage by project, and control access with user roles. Read more in our [blog post](https://www.anthropic.com/news/workspaces).

### September 4th, 2024

- We announced the deprecation of the Claude 1 models. Read more in [Model deprecations](about-claude-model-deprecations.md).

### August 22nd, 2024

- We've added support for usage of the SDK in browsers by returning CORS headers in the API responses. Set `dangerouslyAllowBrowser: true` in the SDK instantiation to enable this feature.

### August 19th, 2024

- 8,192-token outputs on Claude Sonnet 3.5 are out of beta and no longer require the `max-tokens-3-5-sonnet-2024-07-15` header.

### August 14th, 2024

- [Prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md) is now available as a beta feature in the Claude API. Cache and re-use prompts to reduce latency by up to 80% and costs by up to 90%.

### July 15th, 2024

- Generate outputs up to 8,192 tokens in length from Claude Sonnet 3.5 with the new `anthropic-beta: max-tokens-3-5-sonnet-2024-07-15` header.

### July 9th, 2024

- Automatically generate test cases for your prompts using Claude in the [Developer Console](https://console.anthropic.com).
- Compare the outputs from different prompts side by side in the new output comparison mode in the [Developer Console](https://console.anthropic.com).

### June 27th, 2024

- View API usage and billing broken down by dollar amount, token count, and API keys in the new [Usage](https://console.anthropic.com/settings/usage) and [Cost](https://console.anthropic.com/settings/cost) tabs in the [Developer Console](https://console.anthropic.com).
- View your current API rate limits in the new [Rate Limits](https://console.anthropic.com/settings/limits) tab in the [Developer Console](https://console.anthropic.com).

### June 20th, 2024

- [Claude Sonnet 3.5](../19-Reference/claude-3-5-sonnet.md), our most intelligent model yet, is now available across the Claude API, Amazon Bedrock, and Vertex AI.

### May 30th, 2024

- [Tool use](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md) is out of beta across the Claude API, Amazon Bedrock, and Vertex AI, with no beta header required.

### May 10th, 2024

- Our prompt generator tool is now available in the [Developer Console](https://console.anthropic.com). Prompt Generator makes it easy to guide Claude to generate a high-quality prompts tailored to your specific tasks. Read more in our [blog post](https://www.anthropic.com/news/prompt-generator).
