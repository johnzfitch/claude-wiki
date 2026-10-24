---
title: "Migrating to API version 2026-10-21 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/api/migration-2026-10-21"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-22T06:28:18Z"
tags: ["api", "cli", "sdk"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](overview.md)




[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fmigration-2026-10-21)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](overview.md)[Beta headers](beta-headers.md)[Errors](errors.md)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores

Dreams


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Models


List Models


Get a Model


Organization


Get Current Organization

API Keys

External Keys

Federation

Invites

Service Accounts

Users

Workspaces

Rate Limits

Compliance Settings

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles

Plugins

Plugin Marketplaces

Telemetry Destinations

Webhooks


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Delete User Profile


Create Enrollment URL

Action URLs


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


Compliance API

Activities

Organizations

Groups

Apps


Completions


Create a Text Completion Deprecated

OpenTelemetry

[Spans](opentelemetry-spans.md)

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[AWS IAM actions](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[Migrating to API version 2026-10-21](migration-2026-10-21.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/playground.md)

[API reference](overview.md)Support & configuration

# Migrating to API version 2026-10-21

Copy page



Upgrade a Claude API integration from API version 2023-06-01 to 2026-10-21: the SDK version to install and the code changes to make.

Copy page



This guide lists the code changes for moving from API version `2023-06-01` to `2026-10-21`. The [upgrade steps](#migration-checklist) say what to do, in order.

## Upgrade steps

1.  1

    ### Switch to 2026-10-21

    If you use an SDK, your requests use the API version that was current when your SDK's major version was released. The versions shown for your language are the first to use `2026-10-21`, so upgrade to them. If you call the API without an SDK, set the `anthropic-version` header to `2026-10-21`.

    cURL
    CLI
    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    Python

    Upgrade the `anthropic` package to version 2.0.0.

    
    On Amazon Bedrock, `2026-10-21` is available only for Claude 4.7 and later models. If you call an older model on Bedrock, listed in [Claude on Amazon Bedrock (Opus 4.6 and earlier)](../Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md), stay on the SDK version you use today, or, if you set the API version yourself, keep sending the version you send today. To move those calls to `2026-10-21`, first switch them to a Claude 4.7 or later model.

    Release the upgrade together with your fixes from the next step.

2.  2

    ### Update your code for the breaking changes

    Go through the [breaking changes](#breaking-changes), and update your code for each one that affects you. Also make the [code changes that the new SDK or CLI version needs](#sdk-changes).

3.  3

    ### Test against 2026-10-21

    Test your integration against `2026-10-21` before you release.

## Breaking changes

### Messages API

These changes apply to requests to the Messages API (`POST /v1/messages`), to [token counting](../Guides/build-with-claude-token-counting.md), and to each request in a [Message Batch](../Guides/build-with-claude-batch-processing.md) created with `2026-10-21`.

#### Document blocks in assistant messages return an error

Affects you if you send `document` blocks directly in `assistant` messages.

In `2026-10-21`, a request that places a `document` block directly in an `assistant` message returns a 400 error. Send documents in `user` messages instead. A document nested inside another block, such as a web fetch tool result that Claude returned, is still accepted.

#### Citations in user messages return an error

Affects you if you send `citations` on `text` blocks in `user` messages, including inside `search_result` blocks.

In `2026-10-21`, a request that sends a `text` block with a non-empty `citations` array in a `user` message returns a 400 error. Remove `citations` from those blocks. Citations on `text` blocks in `assistant` messages, such as Claude's earlier replies that you send back, are still accepted, and so is the `"citations": {"enabled": true}` setting on documents and search results.

#### Sampling parameters are removed

Affects you if you send `temperature`, `top_p`, or `top_k` in Messages requests or Message Batch requests.

In `2026-10-21`, a request that sends `temperature`, `top_p`, or `top_k` returns a 400 error, even at the parameter's default value.

Remove the three parameters from your requests.

As of the latest major versions, the SDK and the CLI no longer have the three parameters.

Without these parameters, a request samples with their defaults, including a `temperature` of 1.0, the same as a `2023-06-01` request that leaves them out. Models that already accept only the defaults, such as Claude 4.7 and later models, sample as before. On models that accept other values, such as Claude Sonnet 4.6, a request that lowered `temperature` for more consistent output loses that effect. No other setting replaces it. If a request relies on a non-default value, either stop sending the parameter, or keep that request on `2023-06-01`.

### Admin API and Claude Enterprise Analytics API

Affects you if your code reads the Admin API or Claude Enterprise Analytics API response fields in the following tables.

In `2026-10-21`, responses from the Admin API and the [Claude Enterprise Analytics API](../Other/manage-claude-analytics-api.md) no longer include the old names of renamed fields. Use the new names instead.

Admin API:

| Endpoints                                                                                                                                                                                                  | Old name       | New name                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|-------------------------------------------------------------------------------------|
| [RBAC groups](../Admin/beta-organization-rbac-groups-list.md): create, list, retrieve, and update                                                                                                         | `roles`        | `role_ids`                                                                          |
| [RBAC group members](../Admin/beta-organization-rbac-groups-members-list.md): list and add, and the response to [removing a member](../Admin/beta-organization-rbac-groups-members-remove.md)            | `group_id`     | `rbac_group_id`                                                                     |
| [RBAC roles](../Admin/beta-organization-rbac-roles-list.md): list and retrieve                                                                                                                            | `name`         | `display_name`                                                                      |
| [Organization](organization-rate-limits-list.md) and [workspace](organization-workspaces-rate-limits-list.md) rate limits: list, and the response to setting a workspace's rate limits | `group_type`   | `group.type`                                                                        |
| [API keys](organization-api-keys-list.md): list, retrieve, and update                                                                                                                            | `workspace_id` | `scope` (different values; see [`workspace_id` on API keys](#api-key-workspace-id)) |

Claude Enterprise Analytics API:

| Endpoints                                                                                                                                                            | Old name      | New name              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|-----------------------|
| Per-user [usage](../Admin/beta-organization-analytics-user-usage-report-list.md) and [cost](../Admin/beta-organization-analytics-user-cost-report-list.md) reports | `actor.email` | `actor.email_address` |
| [Activity summaries](../Admin/beta-organization-analytics-summaries-list.md)                                                                                        | `summaries`   | `data`                |

The `group_type` query parameter on the rate-limit list endpoints and the `workspace_id` filter on the API key list endpoint are unchanged.

#### `workspace_id` on API keys

Affects you if your code reads `workspace_id` on API keys.

In `2023-06-01`, an API key's `workspace_id` is the ID of the workspace the key is bound to, or `null` for a key bound to the Default Workspace and for a key that isn't bound to one workspace (an all-workspaces key).

In `2026-10-21`, `workspace_id` is removed. Read `scope` instead: for a key bound to a workspace, including the Default Workspace, `scope.workspace_id` is that workspace's real ID, and an all-workspaces key has a `scope` of `{"type": "organization"}`, with no `workspace_id`.

If your code treated a `null` `workspace_id` as the Default Workspace, compare `scope.workspace_id` with your Default Workspace's ID instead. To find that ID, call [List Workspaces](organization-workspaces-list.md) with `include_default=true` and take the workspace named `"Default"`.

## SDK and CLI changes

Earlier SDK and CLI versions sent `anthropic-version: 2023-06-01` with every request. The versions under [Switch to 2026-10-21](#upgrade) send `2026-10-21`, including their Amazon Bedrock and Google Cloud clients. The changes in [Breaking changes](#breaking-changes) apply to them too: the removed parameters and the old field names are also gone from the SDK's types and from the CLI's flags and output.

### `MessageParam` is a union with one type for each role

In earlier versions, `MessageParam` was one type for all roles. Each role now has a type of its own: `UserMessageParam`, `AssistantMessageParam`, and `SystemMessageParam`. `BetaMessageParam` is split the same way, into `BetaUserMessageParam`, `BetaAssistantMessageParam`, and `BetaSystemMessageParam`. The requests that the SDK sends have the same fields and values as before.

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python

A message written as a dict literal, such as `{"role": "user", "content": "Hello"}`, needs no change.

In v1, `anthropic.types.MessageParam` was one `TypedDict`. In v2 it is a union of the three types, and `anthropic.types.beta.BetaMessageParam` is a union of its three. Both names still work in annotations, such as `list[MessageParam]`.

Calling either name now raises a `TypeError`, and a type checker flags it. Write the message as a dict:

```python
# Before
message = MessageParam(role="user", content="Hello")

# After
message: MessageParam = {"role": "user", "content": "Hello"}
```



Subclassing either name also raises a `TypeError`. Subclass the type for the role, such as `UserMessageParam`.

The remaining changes affect type checking only. A dict whose `role` is a variable that can hold more than one role matches no type in the union, so build the dict for one role at a time:

```python
# Before
def to_message(role: Literal["user", "assistant"], text: str) -> MessageParam:
    return {"role": role, "content": text}


# After
def to_message(role: Literal["user", "assistant"], text: str) -> MessageParam:
    if role == "user":
        return {"role": "user", "content": text}
    return {"role": "assistant", "content": text}
```



Two more apply to `BetaMessageParam` only:

- `clear_at` and `output_config` are keys of `BetaSystemMessageParam`, so a user or assistant message can't have them.
- `content` is optional in `BetaSystemMessageParam`, so pyright reports `message["content"]`. Read it with `message.get("content")`, or check first that `message["role"]` is not `"system"`.

### One-value enums are constants

This affects the C#, Go, Java, PHP, and Ruby SDKs and one CLI flag. In earlier versions, a required field that can hold only one value had an enum type of its own with a single member. These fields are now constants, and the enum types are gone. The JSON that the SDK sends and reads is the same.

CLI

C#

Go

Java

PHP

Ruby

CLI

`--type` is optional on `ant beta:sessions:resources add`. `file` is the only value `--type` can take there, so v2 sends it for you. Commands that still pass `--type file` keep working, so there is nothing to change.

### Client-side compaction is removed from the tool runner

This affects the TypeScript and Ruby SDKs. Client-side compaction in the tool runner has been removed in favor of server-side compaction, which summarizes the conversation inside the API instead of with an extra request from the client.

TypeScript

Ruby

TypeScript

The `compactionControl` option and the `@anthropic-ai/sdk/lib/tools/CompactionControl` module are gone. The option stopped working in v0.129.0, where passing it threw an `AnthropicError`. It isn't in the tool runner's parameters type, so TypeScript reports it as an unknown property.

To keep compacting automatically at a token threshold:

```python
// Before
const runner = client.beta.messages.toolRunner({
  // ...
  compactionControl: { enabled: true, contextTokenThreshold: 100_000 }
});

// After
const runner = client.beta.messages.toolRunner({
  // ...
  betas: ["compact-2026-01-12"],
  context_management: {
    edits: [{ type: "compact_20260112", trigger: { type: "input_tokens", value: 100_000 } }]
  }
});
```



To decide yourself when the conversation is compacted, call [`runner.compactBeforeNextTurn()`](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/helpers.md#compaction).

The trigger threshold must be at least 50,000 tokens. See [compaction](../Guides/build-with-claude-compaction-threshold.md) for the other options (`pause_after_compaction`, custom `instructions`).

### Text Completions is removed

The legacy Text Completions API is removed from the TypeScript, Go, Java, and Ruby SDKs and from the CLI. Newer models and features don't support it. Use the [Messages API](messages.md) instead.

CLI

TypeScript

Go

Java

Ruby

CLI

The `ant completions create` command is gone.

```python
# Before
ant completions create \
  --model "$MODEL" \
  --max-tokens-to-sample 1024 \
  --prompt $'\n\nHuman: Hello, Claude\n\nAssistant:'

# After
ant messages create \
  --model "$MODEL" \
  --max-tokens 1024 \
  --message '{role: user, content: "Hello, Claude"}'
```



The reply text moves from the `completion` field to `content.0.text`, so a script that passed `--transform completion` passes `--transform content.0.text` instead.

`ant messages create` also takes `--stream`, but its events have another shape: the text arrives in `delta.text` of `content_block_delta` events, so `--transform content.0.text` does not apply to a stream.

### `betas` is removed from the non-beta Models methods

The non-beta Models methods no longer take `betas`, and the `ant models` commands no longer take `--beta`. To send beta headers, call the same methods on `client.beta.models`, or `ant beta:models` in the CLI. In the SDK, those methods return `BetaModelInfo` where the non-beta ones return `ModelInfo`.

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python

`client.models.retrieve()` and `client.models.list()` no longer take `betas` (passing it is a `TypeError`, and a type checker flags it), and `anthropic.types.ModelListParams` no longer has a `betas` key.

```python
# Before
page = client.models.list(betas=[beta])

# After
page = client.beta.models.list(betas=[beta])
```



### API keys are sent as `Authorization: Bearer`

The SDK and the CLI send your API key as `Authorization: Bearer <key>` instead of in the `X-Api-Key` header, so change any proxy or gateway that reads or sets `X-Api-Key` to use `Authorization`, or [send the key in `X-Api-Key` yourself](#sdk-proxy-x-api-key). The Claude API accepts a key in either header, so a program that talks to the API directly needs no change.

``` block
# Before
X-Api-Key: <key>

# After
Authorization: Bearer <key>
```



CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python

`Authorization` is the header `auth_token` already uses.

This applies to the `api_key` argument and the `ANTHROPIC_API_KEY` environment variable of `Anthropic` and `AsyncAnthropic`, and to `api_key` and `ANTHROPIC_AWS_API_KEY` of `AnthropicAWS`. `AnthropicFoundry` still sends its key as `x-api-key`, and `AnthropicBedrockMantle` already sent a bearer token.

#### If a proxy or gateway reads `X-Api-Key`

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python

Move the key back with an `auth` function on the HTTP client. It runs on every request the client sends, including retries:

```python
import httpx2
from anthropic import Anthropic, DefaultHttpxClient


def send_x_api_key(request: httpx2.Request) -> httpx2.Request:
    if request.headers.get("Authorization") == f"Bearer {api_key}":
        del request.headers["Authorization"]
        request.headers["X-Api-Key"] = api_key
    return request


client = Anthropic(api_key=api_key, http_client=DefaultHttpxClient(auth=send_x_api_key))
```



`AsyncAnthropic` takes the same function, in `http_client=DefaultAsyncHttpxClient(auth=send_x_api_key)`.

#### If you set or removed `X-Api-Key` on a request

This affects the Python, TypeScript, Go, PHP, and Ruby SDKs.

If you removed `X-Api-Key` so that a request sent only an authentication token, delete that code instead of changing it, because removing `Authorization` would remove the token. [A client holds one credential](#sdk-one-credential), so make sure that it's the token: with none passed in code and both `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` set, the client uses the key.

Python

TypeScript

Go

PHP

Ruby

Python

Code that passes `extra_headers={"X-Api-Key": omit}` to keep the key off a request no longer does that. Pass `extra_headers={"Authorization": omit}` instead.

`extra_headers={"X-Api-Key": other_key}` no longer replaces the client's key: both keys go out. To send another key with one request, pass `extra_headers={"Authorization": f"Bearer {other_key}"}`.

### A client holds one credential

An API key and an authentication token now share a header, so an SDK client holds one credential. With none passed in code, it follows the [credential precedence](../Other/manage-claude-wif-reference.md#credential-precedence) order.

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python

v1 sent both an API key and an authentication token when the client had both, each in its own header. The credential is one of `api_key`, `auth_token`, `credentials`, `config`, or `profile`.

- **Pass at most one.** Two or more in the constructor, or in one `copy()` or `with_options()` call, raise `ValueError`. `None` doesn't count. v1 raised `TypeError`, and only for two of `credentials`, `config`, and `profile`.
- **The one you pass is the only one.** As in v1, the client does not look for another in the environment or on disk.
- **With none passed, only the first of these that is set is used:** `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, the profile that `ANTHROPIC_PROFILE` names, the workload identity federation variables, the active profile on disk (the one the `active_config` file names, otherwise `default`). When both of the first two are set, the client logs a warning once. v1 used the active profile ahead of the federation variables when `ANTHROPIC_CONFIG_DIR` was set or an `active_config` file existed; set `ANTHROPIC_PROFILE` to keep using it.
- **`copy()` and `with_options()` replace.** A credential you pass replaces the client's own, whichever kind either one is. A base URL and headers that came from the old credential's config or profile go with it, and the new credential's are used. A base URL you passed stays.

```python
client = Anthropic(api_key=key, auth_token=token)

# Before: sent `X-Api-Key: <key>` and `Authorization: Bearer <token>`
# After:  raises `ValueError`
```



The platform clients keep their own rules. `AnthropicAWS` takes `auth_token` next to `api_key` without an error, and sends the key.

The docstrings of `Anthropic.__init__` and `Anthropic.copy` in [`_client.py`](https://github.com/anthropics/anthropic-sdk-python/blob/main/src/anthropic/_client.py) have the details.

If you relied on sending both, for example a token for a gateway and a key for the API behind it, pass the token as `auth_token` and set `X-Api-Key` in `default_headers`. Have the gateway remove its `Authorization` header before it forwards the request. The Claude API expects one credential for each request.

### Changes in one SDK or the CLI

These changes each affect one SDK or the CLI.

CLI

C#

Go

Java

PHP

Ruby

CLI

**`--api-key` and `--auth-token` are removed.** `ant` no longer takes an API key or authentication token as a flag value, because a value on the command line is visible in shell history and process listings. Both flags have printed a deprecation warning since v1.27.0. A command that still passes one stops with `flag provided but not defined`.

| Removed                | Use instead                                                 |
|------------------------|-------------------------------------------------------------|
| `--api-key <key>`      | `ANTHROPIC_API_KEY`, `--api-key-stdin`, or `ant auth login` |
| `--auth-token <token>` | `ANTHROPIC_AUTH_TOKEN` or `--auth-token-stdin`              |

```python
# Before
ant --api-key "$KEY" models list

# After, from the environment
export ANTHROPIC_API_KEY="$KEY"
ant models list

# After, from a secret manager
op read op://vault/anthropic/api-key | ant --api-key-stdin models list
```



`--api-key-stdin` and `--auth-token-stdin` read all of standard input, so a command that uses one takes its request body from flags.

`ant auth status`, the first-run prompt of `ant apply`, and the note about multiple authentication sources now call these credentials `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN`, where they printed `--api-key / ANTHROPIC_API_KEY` and `--auth-token / ANTHROPIC_AUTH_TOKEN`.

### The license is Apache 2.0

Starting with these versions, the SDK and the CLI are licensed under the Apache License, Version 2.0. Earlier versions remain under the MIT License. No code changes are needed. If you track the licenses of your dependencies, update their entries.

- **TypeScript:** The platform packages (`@anthropic-ai/bedrock-sdk`, `@anthropic-ai/vertex-sdk`, `@anthropic-ai/foundry-sdk`, `@anthropic-ai/aws-sdk`, and `@anthropic-ai/google-cloud-sdk`) change license in their own 1.0.0 releases.
- **C#:** The other packages (`Anthropic.Bedrock`, `Anthropic.Vertex`, `Anthropic.Foundry`, `Anthropic.Aws`, `Anthropic.GoogleCloud`, and `Anthropic.Mcp`) change license in their own 1.0.0 releases.
- **Java:** The change covers every `com.anthropic` artifact.
