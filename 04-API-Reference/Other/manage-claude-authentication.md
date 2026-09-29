---
title: "Authentication - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/authentication"
category: "04-API-Reference/Other"
fetched_at: "2026-09-27T06:27:09Z"
tags: ["api", "authentication"]
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fauthentication)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](manage-claude-authentication.md)

Building with Claude

[Features overview](../Guides/build-with-claude-overview.md)[Using the Messages API](../Guides/build-with-claude-working-with-messages.md)[Stop reasons and fallback](../Guides/build-with-claude-handling-stop-reasons.md)[Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md)[Fallback credit](../Guides/build-with-claude-fallback-credit.md)

Model capabilities

[Effort](../Guides/build-with-claude-effort.md)[Task budgets (beta)](../Guides/build-with-claude-task-budgets.md)[Fast mode (research preview)](../Guides/build-with-claude-fast-mode.md)[Structured outputs](../Guides/build-with-claude-structured-outputs.md)[Citations](../Guides/build-with-claude-citations.md)[Streaming Messages](../Guides/build-with-claude-streaming.md)[Batch processing](../Guides/build-with-claude-batch-processing.md)[Search results](../Guides/build-with-claude-search-results.md)[Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](../Guides/build-with-claude-multilingual-support.md)[Embeddings](../Guides/build-with-claude-embeddings.md)

[Thinking](../Guides/build-with-claude-thinking.md)

Tools

[Overview](../Agents-Tools/agents-and-tools-tool-use-overview.md)[How tool use works](../Agents-Tools/agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](../Agents-Tools/agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](../Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](../Agents-Tools/agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](../Agents-Tools/agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](../Agents-Tools/agents-and-tools-tool-use-tool-runner.md)[Strict tool use](../Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md)[Server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md)[Web search tool](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](../Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](../Agents-Tools/agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md)[Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md)[Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](../Agents-Tools/agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](../Agents-Tools/agents-and-tools-tool-use-tool-reference.md)[Manage tool context](../Agents-Tools/agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](../Agents-Tools/agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](../Agents-Tools/agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](../Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](../Agents-Tools/agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](../Guides/build-with-claude-context-windows.md)[Context editing](../Guides/build-with-claude-context-editing.md)[Prompt caching](../Guides/build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](../Guides/build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](../Guides/build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](../Guides/build-with-claude-cache-diagnostics.md)[Token counting](../Guides/build-with-claude-token-counting.md)

[Compaction](../Guides/build-with-claude-compaction.md)

Working with files

[Files API](../Guides/build-with-claude-files.md)[PDF support](../Guides/build-with-claude-pdf-support.md)

[Images and vision](../Guides/build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Quickstart](../Agents-Tools/agents-and-tools-agent-skills-quickstart.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)[Skills in the API](../Guides/build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)[MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](../Guides/build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](../Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)[Google Cloud](../Guides/build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md)

[Console](usage-limits.md)

[Messages](../../01-Getting-Started/intro.md)First steps

# Authentication

Copy page



Authenticate to the Claude API with API keys, Workload Identity Federation, or App Attest.

Copy page



The Claude API supports three ways to authenticate requests:

| Method                                                        | Credential                                                                                              | Best for                                                                                                                                        |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [API key](#api-keys)                                          | Static `sk-ant-api...` secret sent as a bearer token in the `Authorization` header                      | Local development, prototyping, scripts, and servers where you control secret storage                                                           |
| [Workload Identity Federation](#workload-identity-federation) | Short-lived bearer token exchanged from your identity provider's identity token                         | Production workloads on cloud platforms (AWS, Google Cloud, Azure), CI/CD pipelines, and Kubernetes, where you want to eliminate static secrets |
| [App Attest](#app-attest)                                     | Short-lived access token issued to a genuine, attested installation of your registered iOS or macOS app | iOS and macOS apps distributed to end users, where the app calls the Claude API directly with no back end or proxy                              |

API keys and Workload Identity Federation grant the same access to Claude API endpoints. Choose API keys to get started quickly: a personal key for your own development, or a service account key for anything shared. Move to Workload Identity Federation when your workload already has a platform-issued identity you can federate. Use App Attest for iOS and macOS apps you distribute to end users.

## API keys

API keys are static secrets that you generate in the Claude Console and send on every request as a bearer token in the `Authorization` header.

### Key types

When you create a key, you choose its type, which determines what the key can do, where it works, and when it stops working:

| Key type                   | Acts as                                                                                   | Works in                                                                                                                                                                                              | Stops working when                                                                                                                                                                                                                   |
|----------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Personal key**           | You, the user, with your roles and permissions                                            | Either a single workspace or the workspaces where your role allows API use, chosen when the key is created                                                                                            | You lose access to the organization or, for a single-workspace key, to that workspace. Personal keys are archived when you are removed from the organization. If you are re-invited, create new keys; archived keys are not restored |
| **Service account key**    | A [service account](manage-claude-workload-identity-federation.md#service-accounts) | Either a single workspace or anything the service account has access to, chosen when the key is created. A service account has access to the Default Workspace and to workspaces it has been added to | The service account is archived or, for a single-workspace key, is removed from that workspace                                                                                                                                       |
| **Workspace key** (legacy) | No one: it belongs to the workspace it was created in                                     | That workspace                                                                                                                                                                                        | It expires, is disabled or deleted, or its workspace is archived, regardless of whether its creator leaves the organization                                                                                                          |

Personal keys and service account keys are identity-backed: each belongs to a user or service account your organization already manages, and every request acts as that identity. When that identity is removed from the organization, the key stops working. This means that keys won't accidentally outlive the people or workloads that own them. Prefer them over workspace keys for new integrations.

Use a personal key for your own development and scripts. A shared personal key acts as one person and breaks when they leave. For shared or automated workloads (CI, production services), have an organization admin create a service account so the workload has its own identity.

Workspace API keys still work but should be considered legacy; identity-backed keys or [Workload Identity Federation](manage-claude-workload-identity-federation.md) are preferred. To migrate, see [Replacing workspace API keys](#replacing-workspace-api-keys).

### Create and use a key

- **Create a key:** Go to [Settings → API keys](usage-limits.md) in the Claude Console and click **Create key**. Name the key and choose an [expiration](#key-expiration). Set **Linked account** to yourself for a personal key, or to a service account for a key shared across multiple users. You can also scope the key to a specific workspace, which lets you skip setting a workspace ID manually in future requests.
- **Use the key:** Send it as `Authorization: Bearer <key>` on direct HTTP requests, or set the `ANTHROPIC_API_KEY` environment variable and the [client SDKs](cli-sdks-libraries-overview.md) pick it up automatically.

```python
POST /v1/messages
Authorization: Bearer YOUR_API_KEY
anthropic-version: 2023-06-01
content-type: application/json
```



The legacy `x-api-key: YOUR_API_KEY` header is still supported in place of `Authorization`.

Store API keys in a secrets manager, rotate them periodically, and disable or delete any key you suspect has leaked. On the [API keys page](usage-limits.md), **Disable** is reversible (the Admin API reports the key's `status` as `"inactive"`, and **Re-enable** returns it to `"active"`), while **Delete** is permanent: the key is archived and still appears in [List API Keys](../Admin/beta-organization-api-keys-list.md) with `status: "archived"`. Expired keys can only be deleted. You can also set an [expiration](#key-expiration) when you create a key to limit how long a leaked credential stays usable.

cURL

Python

TypeScript

Go

Java

C#

PHP

Ruby

CLI



```python
client = Anthropic(api_key="my-anthropic-api-key")
# or, with ANTHROPIC_API_KEY set in the environment:
client = Anthropic()
```

### Select a workspace

API keys that are created for a specific workspace only work in that workspace, and API requests using these keys can omit the workspace ID.

If your API key isn't scoped to a workspace, you must specify the workspace ID in the `anthropic-workspace-id` header for each request. See the following example for how to set this header in a request or in SDKs.

The [Admin API](manage-claude-admin-api.md) accepts a personal key or service account key only if the key isn't scoped to a specific workspace.

You can find a workspace's ID in the **ID** column of [Settings → Workspaces](usage-limits.md) in the Claude Console, or by calling the [List Workspaces](../Admin/beta-organization-workspaces-list.md) endpoint. List Workspaces omits the Default Workspace; its ID is in the `anthropic-workspace-id` [response header](manage-claude-workspaces.md#identify-the-workspace-behind-an-api-response) of any request that runs there.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = Anthropic()  # reads ANTHROPIC_API_KEY

# Required on every request for a multi-workspace key.
# Omit extra_headers for a single-workspace key.
message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    extra_headers={"anthropic-workspace-id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"},
)
print(message.content)

# Or set it once for every request from this client:
workspace_client = Anthropic(
    default_headers={"anthropic-workspace-id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"},
)
```

If a request made with a key that isn't scoped to a workspace omits the header, the API returns a 400 `invalid_request_error`:

JSON



```python
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "anthropic-workspace-id is required when authenticating with an identity-linked API key; send the id of the workspace this request acts in."
  },
  "request_id": "req_011CSHoEeqs5C35K2UUqR7Fy"
}
```

A header value that isn't a valid workspace ID returns a 400 `invalid_request_error` with the message `anthropic-workspace-id header must be a valid workspace ID.` If the workspace doesn't exist, or the key's user or service account doesn't have access to it, the API returns a 404 `not_found_error` with the message `` Workspace `<id>` not found. ``, the same response as for any unknown workspace.

Workload Identity Federation selects a workspace at token exchange instead; see the [WIF reference](manage-claude-wif-reference.md) for details.

### Key expiration

When you create an API key from the [API keys page](usage-limits.md) in the Claude Console, you choose an expiration: a preset (3 hours, 1 day, 7 days, or 30 days), a custom duration, or **Never** for keys you store in a secrets manager and rotate yourself. If your organization has a maximum expiration policy, the Console limits presets and custom durations to the policy maximum, and **Never** is unavailable. Existing keys keep their current behavior; expiration is set at creation time and cannot be changed afterward. The same expiration choice applies when you [create an Admin API key](manage-claude-admin-api-keys.md) in the Claude Console.

Anthropic emails the key's creator as the expiration approaches: 7 days before expiration for keys created with a lifetime of at least 14 days, and 1 day before for keys with a lifetime of at least 7 days. Keys with shorter lifetimes expire without a warning email.

After a key expires, requests made with it return a `401 authentication_error`. Create a new key to restore access; expired keys cannot be reactivated.

The Console API keys table shows each key's expiration, and the Admin API reports each key's `expires_at` timestamp on the [List API Keys](../Admin/beta-organization-api-keys-list.md) and [Retrieve API Key](../Admin/beta-organization-api-keys-retrieve.md) endpoints, so you can audit and rotate keys before they expire. The field is `null` for keys without an expiration.

Expiration limits the lifetime of a leaked credential, but it is not a substitute for secret hygiene. Regardless of expiration, store keys in a secrets manager and disable or delete any key you suspect has leaked.

### Replacing workspace API keys

If you have a workspace key, you may want to replace it with [Workload Identity Federation](manage-claude-wif-reference.md) or a personal or service account key. This provides better security and observability.

See [Workload Identity Federation](manage-claude-wif-reference.md) for details on configuring Workload Identity Federation, which is preferred over long-lived keys.

To replace a workspace key with a personal or service account key:

1.  **Decide the key type.** Your own tooling should use a personal key. A shared or unattended workload should use a service account key.
2.  **Create a service account** if necessary. You may have to ask an organization admin to create one in [Settings → Service accounts](https://platform.claude.com/settings/service-accounts) and add it to the relevant workspace.
3.  **Create the new key.** Create it specifically for the integration's workspace unless multiple workspaces are needed.
4.  **Deploy the new key.** Replace the old key wherever the integration reads it, typically the `ANTHROPIC_API_KEY` environment variable or a secrets manager entry. For a multi-workspace key, also send the `anthropic-workspace-id` header as shown in [Select a workspace](#select-a-workspace).
5.  **Delete the old key.** Confirm that requests succeed, then delete the workspace key on the [API keys page](usage-limits.md).

## Workload Identity Federation

Workload Identity Federation (WIF) lets a workload authenticate with a short-lived identity token issued by an identity provider (IdP) you already trust, such as AWS IAM, Google Cloud, or any standards-compliant OIDC issuer (such as GitHub Actions, Kubernetes service accounts, SPIFFE, Microsoft Entra ID, or Okta). The workload exchanges its IdP-issued JWT at `POST /v1/oauth/token` for a short-lived Claude API access token, and the SDK refreshes that token automatically before it expires. There is no `sk-ant-api...` string to mint, distribute, or rotate.

Federation removes long-lived Claude API keys from your environment, which shrinks the blast radius of a leaked credential and lets you manage access with the same IdP controls you already use for cloud resources. It does not, on its own, guarantee end-to-end security: the trust chain is only as strong as your identity provider's configuration, and a long-lived secret one hop upstream (for example, a static cloud credential that can mint IdP tokens) can still undermine it. Pair federation with your provider's controls, such as IP allowlists, MFA, and audit logging.

To configure federation, you create three resources in the Claude Console (a service account, a federation issuer, and a federation rule) and then point your SDK at the rule. See [Workload Identity Federation](manage-claude-workload-identity-federation.md) for the full setup walkthrough.

## App Attest

App Attest authenticates iOS and macOS apps that call the Claude API directly from the device. Each installation proves that it is a genuine, unmodified build of an app you registered in the Claude Console, using Apple's App Attest service. Anthropic then issues the device a short-lived access token that bills usage to your workspace. Tokens are scoped to your workspace, expire after one hour, and authorize only [Messages API](../Endpoints/messages-create.md) calls.

To register your app and get a client ID, see [App Attest for iOS and macOS apps](manage-claude-app-attest.md).

## Next steps



[Set up Workload Identity Federation](manage-claude-workload-identity-federation.md)

Configure issuers, rules, and service accounts, then exchange tokens



[Identity provider guides](manage-claude-workload-identity-federation.md#identity-providers)

Step-by-step guides for AWS, Google Cloud, Azure, GitHub Actions, Kubernetes, SPIFFE, and Okta



[WIF reference](manage-claude-wif-reference.md)

Environment variables, validation rules, profile configuration, and error reference

[App Attest for iOS and macOS apps](manage-claude-app-attest.md)

Let genuine installations of your app call the Claude API without shipping an API key



[Client SDKs](cli-sdks-libraries-overview.md)

Python, TypeScript, C#, Go, Java, PHP, Ruby, and the CLI
