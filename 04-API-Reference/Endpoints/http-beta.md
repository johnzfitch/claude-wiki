---
title: "Beta - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/http/beta"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-27T06:27:05Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fhttp%2Fbeta)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

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


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Organization


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

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](http.md)

# Beta

##### Models



AnthropicBeta = string or "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 45 more



One of the following:



BetaAPIError object{ type: "api_error", message }





type: "api_error"



defaultapi_error



message: string



defaultInternal server error



BetaAuthenticationError object{ type: "authentication_error", message }





type: "authentication_error"



defaultauthentication_error



message: string



defaultAuthentication error



BetaBillingError object{ type: "billing_error", message }





type: "billing_error"



defaultbilling_error



message: string



defaultBilling error

BetaCurrency = "USD"





BetaError = [BetaInvalidRequestError](http-beta.md#beta_invalid_request_error) or [BetaAuthenticationError](http-beta.md#beta_authentication_error) or [BetaBillingError](http-beta.md#beta_billing_error) or 6 more



One of the following:



BetaErrorResponse object{ type: "error", error, request_id }





type: "error"



defaulterror



error: [BetaError](http-beta.md#beta_error)



One of the following:

request_id: string or null





BetaGatewayTimeoutError object{ type: "timeout_error", message }





type: "timeout_error"



defaulttimeout_error



message: string



defaultRequest timeout



BetaInvalidRequestError object{ type: "invalid_request_error", message }





type: "invalid_request_error"



defaultinvalid_request_error



message: string



defaultInvalid request



BetaMonetaryAmount object{ amount, currency }



A monetary amount in a specific currency.

amount: string



Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is \$25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

currency: [BetaCurrency](http-beta.md#beta_currency)



Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.



BetaNotFoundError object{ type: "not_found_error", message }





type: "not_found_error"



defaultnot_found_error



message: string



defaultNot found



BetaOverloadedError object{ type: "overloaded_error", message }





type: "overloaded_error"



defaultoverloaded_error



message: string



defaultOverloaded



BetaPermissionError object{ type: "permission_error", message }





type: "permission_error"



defaultpermission_error



message: string



defaultPermission denied



BetaRateLimitError object{ type: "rate_limit_error", message }





type: "rate_limit_error"



defaultrate_limit_error



message: string



defaultRate limited

#### Beta[Models](http-beta-models.md)

##### [List Models](http-beta-models-list.md)

GET/v1/models

List available models.

##### [Get a Model](http-beta-models-retrieve.md)

GET/v1/models/{model_id}

Get a specific model.

#### Beta[Messages](http-beta-messages.md)

##### [Create a Message](http-beta-messages-create.md)

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

##### [Count tokens in a Message](http-beta-messages-count-tokens.md)

POST/v1/messages/count_tokens

Count the number of tokens in a Message.

#### BetaMessages[Batches](https://platform.claude.com/docs/en/api/http/beta/messages/batches)

##### [Create a Message Batch](https://platform.claude.com/docs/en/api/http/beta/messages/batches/create)

POST/v1/messages/batches

Send a batch of Message creation requests.

##### [Retrieve a Message Batch](https://platform.claude.com/docs/en/api/http/beta/messages/batches/retrieve)

GET/v1/messages/batches/{message_batch_id}

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

##### [List Message Batches](https://platform.claude.com/docs/en/api/http/beta/messages/batches/list)

GET/v1/messages/batches

List all Message Batches within a Workspace. Most recently created batches are returned first.

##### [Cancel a Message Batch](https://platform.claude.com/docs/en/api/http/beta/messages/batches/cancel)

POST/v1/messages/batches/{message_batch_id}/cancel

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

##### [Delete a Message Batch](https://platform.claude.com/docs/en/api/http/beta/messages/batches/delete)

DELETE/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](https://platform.claude.com/docs/en/api/http/beta/messages/batches/results)

GET/v1/messages/batches/{message_batch_id}/results

Streams the results of a Message Batch as a `.jsonl` file.

#### Beta[Agents](https://platform.claude.com/docs/en/api/http/beta/agents)

##### [Create Agent](https://platform.claude.com/docs/en/api/http/beta/agents/create)

POST/v1/agents

##### [List Agents](https://platform.claude.com/docs/en/api/http/beta/agents/list)

GET/v1/agents

##### [Get Agent](https://platform.claude.com/docs/en/api/http/beta/agents/retrieve)

GET/v1/agents/{agent_id}

##### [Update Agent](https://platform.claude.com/docs/en/api/http/beta/agents/update)

POST/v1/agents/{agent_id}

##### [Archive Agent](https://platform.claude.com/docs/en/api/http/beta/agents/archive)

POST/v1/agents/{agent_id}/archive

#### BetaAgents[Versions](https://platform.claude.com/docs/en/api/http/beta/agents/versions)

##### [List Agent Versions](https://platform.claude.com/docs/en/api/http/beta/agents/versions/list)

GET/v1/agents/{agent_id}/versions

#### Beta[Environments](https://platform.claude.com/docs/en/api/http/beta/environments)

##### [Create Environment](https://platform.claude.com/docs/en/api/http/beta/environments/create)

POST/v1/environments

Create a new environment with the specified configuration.

##### [List Environments](https://platform.claude.com/docs/en/api/http/beta/environments/list)

GET/v1/environments

List environments with pagination support.

##### [Get Environment](https://platform.claude.com/docs/en/api/http/beta/environments/retrieve)

GET/v1/environments/{environment_id}

Retrieve a specific environment by ID.

##### [Update Environment](https://platform.claude.com/docs/en/api/http/beta/environments/update)

POST/v1/environments/{environment_id}

Update an existing environment's configuration.

##### [Delete Environment](https://platform.claude.com/docs/en/api/http/beta/environments/delete)

DELETE/v1/environments/{environment_id}

Delete an environment by ID. Returns a confirmation of the deletion.

##### [Archive Environment](https://platform.claude.com/docs/en/api/http/beta/environments/archive)

POST/v1/environments/{environment_id}/archive

Archive an environment by ID. Archived environments cannot be used to create new sessions.

#### BetaEnvironments[Work](https://platform.claude.com/docs/en/api/http/beta/environments/work)

##### [Get Work Item](https://platform.claude.com/docs/en/api/http/beta/environments/work/retrieve)

GET/v1/environments/{environment_id}/work/{work_id}

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Poll for Work](https://platform.claude.com/docs/en/api/http/beta/environments/work/poll)

GET/v1/environments/{environment_id}/work/poll

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Acknowledge Work](https://platform.claude.com/docs/en/api/http/beta/environments/work/ack)

POST/v1/environments/{environment_id}/work/{work_id}/ack

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Record Heartbeat](https://platform.claude.com/docs/en/api/http/beta/environments/work/heartbeat)

POST/v1/environments/{environment_id}/work/{work_id}/heartbeat

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Stop Work](https://platform.claude.com/docs/en/api/http/beta/environments/work/stop)

POST/v1/environments/{environment_id}/work/{work_id}/stop

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [List Work Items](https://platform.claude.com/docs/en/api/http/beta/environments/work/list)

GET/v1/environments/{environment_id}/work

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Update Work Item](https://platform.claude.com/docs/en/api/http/beta/environments/work/update)

POST/v1/environments/{environment_id}/work/{work_id}

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Get Queue Statistics](https://platform.claude.com/docs/en/api/http/beta/environments/work/stats)

GET/v1/environments/{environment_id}/work/stats

Get statistics about the work queue for an environment.

#### Beta[Sessions](https://platform.claude.com/docs/en/api/http/beta/sessions)

##### [Create Session](https://platform.claude.com/docs/en/api/http/beta/sessions/create)

POST/v1/sessions

##### [List Sessions](https://platform.claude.com/docs/en/api/http/beta/sessions/list)

GET/v1/sessions

##### [Get Session](https://platform.claude.com/docs/en/api/http/beta/sessions/retrieve)

GET/v1/sessions/{session_id}

##### [Update Session](https://platform.claude.com/docs/en/api/http/beta/sessions/update)

POST/v1/sessions/{session_id}

##### [Delete Session](https://platform.claude.com/docs/en/api/http/beta/sessions/delete)

DELETE/v1/sessions/{session_id}

##### [Archive Session](https://platform.claude.com/docs/en/api/http/beta/sessions/archive)

POST/v1/sessions/{session_id}/archive

#### BetaSessions[Events](https://platform.claude.com/docs/en/api/http/beta/sessions/events)

##### [List Events](https://platform.claude.com/docs/en/api/http/beta/sessions/events/list)

GET/v1/sessions/{session_id}/events

##### [Send Events](https://platform.claude.com/docs/en/api/http/beta/sessions/events/send)

POST/v1/sessions/{session_id}/events

##### [Stream Events](https://platform.claude.com/docs/en/api/http/beta/sessions/events/stream)

GET/v1/sessions/{session_id}/events/stream

#### BetaSessions[Resources](https://platform.claude.com/docs/en/api/http/beta/sessions/resources)

##### [Add Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/add)

POST/v1/sessions/{session_id}/resources

##### [List Session Resources](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/list)

GET/v1/sessions/{session_id}/resources

##### [Get Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/retrieve)

GET/v1/sessions/{session_id}/resources/{resource_id}

##### [Update Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/update)

POST/v1/sessions/{session_id}/resources/{resource_id}

##### [Delete Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/delete)

DELETE/v1/sessions/{session_id}/resources/{resource_id}

#### BetaSessions[Threads](https://platform.claude.com/docs/en/api/http/beta/sessions/threads)

##### [List Session Threads](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/list)

GET/v1/sessions/{session_id}/threads

##### [Get Session Thread](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/retrieve)

GET/v1/sessions/{session_id}/threads/{thread_id}

##### [Archive Session Thread](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/archive)

POST/v1/sessions/{session_id}/threads/{thread_id}/archive

#### BetaSessionsThreads[Events](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/events)

##### [List Session Thread Events](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/events/list)

GET/v1/sessions/{session_id}/threads/{thread_id}/events

##### [Stream Session Thread Events](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/events/stream)

GET/v1/sessions/{session_id}/threads/{thread_id}/stream

#### Beta[Deployments](https://platform.claude.com/docs/en/api/http/beta/deployments)

##### [Create Deployment](https://platform.claude.com/docs/en/api/http/beta/deployments/create)

POST/v1/deployments

##### [List Deployments](https://platform.claude.com/docs/en/api/http/beta/deployments/list)

GET/v1/deployments

##### [Get Deployment](https://platform.claude.com/docs/en/api/http/beta/deployments/retrieve)

GET/v1/deployments/{deployment_id}

##### [Update Deployment](https://platform.claude.com/docs/en/api/http/beta/deployments/update)

POST/v1/deployments/{deployment_id}

##### [Archive Deployment](https://platform.claude.com/docs/en/api/http/beta/deployments/archive)

POST/v1/deployments/{deployment_id}/archive

##### [Run Deployment Now](https://platform.claude.com/docs/en/api/http/beta/deployments/run)

POST/v1/deployments/{deployment_id}/run

##### [Pause Deployment](https://platform.claude.com/docs/en/api/http/beta/deployments/pause)

POST/v1/deployments/{deployment_id}/pause

##### [Unpause Deployment](https://platform.claude.com/docs/en/api/http/beta/deployments/unpause)

POST/v1/deployments/{deployment_id}/unpause

#### Beta[Deployment Runs](https://platform.claude.com/docs/en/api/http/beta/deployment_runs)

##### [List Deployment Runs](https://platform.claude.com/docs/en/api/http/beta/deployment_runs/list)

GET/v1/deployment_runs

##### [Get Deployment Run](https://platform.claude.com/docs/en/api/http/beta/deployment_runs/retrieve)

GET/v1/deployment_runs/{deployment_run_id}

#### Beta[Vaults](https://platform.claude.com/docs/en/api/http/beta/vaults)

##### [Create Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/create)

POST/v1/vaults

##### [List Vaults](https://platform.claude.com/docs/en/api/http/beta/vaults/list)

GET/v1/vaults

##### [Get Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/retrieve)

GET/v1/vaults/{vault_id}

##### [Update Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/update)

POST/v1/vaults/{vault_id}

##### [Delete Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/delete)

DELETE/v1/vaults/{vault_id}

##### [Archive Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/archive)

POST/v1/vaults/{vault_id}/archive

#### BetaVaults[Credentials](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials)

##### [Create Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/create)

POST/v1/vaults/{vault_id}/credentials

##### [List Credentials](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/list)

GET/v1/vaults/{vault_id}/credentials

##### [Get Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/retrieve)

GET/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Update Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/update)

POST/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Delete Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/delete)

DELETE/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Archive Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/archive)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/archive

##### [Validate Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/mcp_oauth_validate)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate

#### Beta[Memory Stores](https://platform.claude.com/docs/en/api/http/beta/memory_stores)

##### [Create a memory store](https://platform.claude.com/docs/en/api/http/beta/memory_stores/create)

POST/v1/memory_stores

##### [List memory stores](https://platform.claude.com/docs/en/api/http/beta/memory_stores/list)

GET/v1/memory_stores

##### [Retrieve a memory store](https://platform.claude.com/docs/en/api/http/beta/memory_stores/retrieve)

GET/v1/memory_stores/{memory_store_id}

##### [Update a memory store](https://platform.claude.com/docs/en/api/http/beta/memory_stores/update)

POST/v1/memory_stores/{memory_store_id}

##### [Delete a memory store](https://platform.claude.com/docs/en/api/http/beta/memory_stores/delete)

DELETE/v1/memory_stores/{memory_store_id}

##### [Archive a memory store](https://platform.claude.com/docs/en/api/http/beta/memory_stores/archive)

POST/v1/memory_stores/{memory_store_id}/archive

#### BetaMemory Stores[Memories](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories)

##### [Create a memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/create)

POST/v1/memory_stores/{memory_store_id}/memories

##### [List memories](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/list)

GET/v1/memory_stores/{memory_store_id}/memories

##### [Retrieve a memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/retrieve)

GET/v1/memory_stores/{memory_store_id}/memories/{memory_id}

##### [Update a memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/update)

POST/v1/memory_stores/{memory_store_id}/memories/{memory_id}

##### [Delete a memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/delete)

DELETE/v1/memory_stores/{memory_store_id}/memories/{memory_id}

#### BetaMemory Stores[Memory Versions](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions)

##### [List memory versions](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions/list)

GET/v1/memory_stores/{memory_store_id}/memory_versions

##### [Retrieve a memory version](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions/retrieve)

GET/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}

##### [Redact a memory version](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions/redact)

POST/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact

#### Beta[Files](http-beta-files.md)

##### [Upload File](http-beta-files-upload.md)

POST/v1/files

##### [List Files](http-beta-files-list.md)

GET/v1/files

##### [Download File](http-beta-files-download.md)

GET/v1/files/{file_id}/content

##### [Get File Metadata](http-beta-files-retrieve-metadata.md)

GET/v1/files/{file_id}

##### [Delete File](http-beta-files-delete.md)

DELETE/v1/files/{file_id}

#### Beta[Skills](http-beta-skills.md)

##### [Create Skill](http-beta-skills-create.md)

POST/v1/skills

##### [List Skills](http-beta-skills-list.md)

GET/v1/skills

##### [Get Skill](http-beta-skills-retrieve.md)

GET/v1/skills/{skill_id}

##### [Delete Skill](http-beta-skills-delete.md)

DELETE/v1/skills/{skill_id}

#### BetaSkills[Versions](https://platform.claude.com/docs/en/api/http/beta/skills/versions)

##### [Create Skill Version](https://platform.claude.com/docs/en/api/http/beta/skills/versions/create)

POST/v1/skills/{skill_id}/versions

##### [List Skill Versions](https://platform.claude.com/docs/en/api/http/beta/skills/versions/list)

GET/v1/skills/{skill_id}/versions

##### [Download Skill Version Content](https://platform.claude.com/docs/en/api/http/beta/skills/versions/download)

GET/v1/skills/{skill_id}/versions/{version}/content

Download a skill version's content as a zip archive.

##### [Get Skill Version](https://platform.claude.com/docs/en/api/http/beta/skills/versions/retrieve)

GET/v1/skills/{skill_id}/versions/{version}

##### [Delete Skill Version](https://platform.claude.com/docs/en/api/http/beta/skills/versions/delete)

DELETE/v1/skills/{skill_id}/versions/{version}

#### Beta[User Profiles](http-beta-user-profiles.md)

##### [Create User Profile](http-beta-user-profiles-create.md)

POST/v1/user_profiles

##### [List User Profiles](http-beta-user-profiles-list.md)

GET/v1/user_profiles

##### [Get User Profile](http-beta-user-profiles-retrieve.md)

GET/v1/user_profiles/{user_profile_id}

##### [Update User Profile](http-beta-user-profiles-update.md)

POST/v1/user_profiles/{user_profile_id}

##### [Create Enrollment URL](http-beta-user-profiles-create-enrollment-url.md)

POST/v1/user_profiles/{user_profile_id}/enrollment_url

#### Beta[Dreams](https://platform.claude.com/docs/en/api/http/beta/dreams)

##### [Create a Dream](https://platform.claude.com/docs/en/api/http/beta/dreams/create)

POST/v1/dreams

Start an asynchronous job that uses past sessions to produce a reorganized version of a memory store and get back the dream to poll for the result.

##### [List Dreams](https://platform.claude.com/docs/en/api/http/beta/dreams/list)

GET/v1/dreams

List the dreams in the workspace, newest first.

##### [Get a Dream](https://platform.claude.com/docs/en/api/http/beta/dreams/retrieve)

GET/v1/dreams/{dream_id}

Get a dream by ID to check its status, output memory store, and token usage.

##### [Cancel a Dream](https://platform.claude.com/docs/en/api/http/beta/dreams/cancel)

POST/v1/dreams/{dream_id}/cancel

Stop a `pending` or `running` dream.

##### [Archive a Dream](https://platform.claude.com/docs/en/api/http/beta/dreams/archive)

POST/v1/dreams/{dream_id}/archive

Hide a `completed`, `failed`, or `canceled` dream from the default list of dreams.

#### Beta[Tunnels](http-beta-tunnels.md)

##### [Create Tunnel](http-beta-tunnels-create.md)

POST/v1/tunnels

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Get Tunnel](http-beta-tunnels-retrieve.md)

GET/v1/tunnels/{tunnel_id}

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [List Tunnels](http-beta-tunnels-list.md)

GET/v1/tunnels

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Archive Tunnel](http-beta-tunnels-archive.md)

POST/v1/tunnels/{tunnel_id}/archive

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Reveal Tunnel Token](http-beta-tunnels-reveal-token.md)

POST/v1/tunnels/{tunnel_id}/reveal_token

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Rotate Tunnel Token](http-beta-tunnels-rotate-token.md)

POST/v1/tunnels/{tunnel_id}/rotate_token

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

#### BetaTunnels[Certificates](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates)

##### [Create Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/create)

POST/v1/tunnels/{tunnel_id}/certificates

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Get Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/retrieve)

GET/v1/tunnels/{tunnel_id}/certificates/{certificate_id}

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [List Tunnel Certificates](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/list)

GET/v1/tunnels/{tunnel_id}/certificates

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Archive Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/archive)

POST/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

#### Beta[Organization](../Admin/http-beta-organization.md)

##### [Get Current Organization](../Admin/beta-organization-retrieve.md)

GET/v1/organizations/me

Retrieve information about the organization associated with the authenticated API key.

#### BetaOrganization[API Keys](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys)

##### [List API Keys](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys/list)

GET/v1/organizations/api_keys

##### [Retrieve API Key (Admin API)](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys/retrieve)

GET/v1/organizations/api_keys/{api_key_id}

Retrieve information about a single API key in your organization, looked up by its ID. This Admin API endpoint requires an Admin API key, is intended for programmatic key management, and never returns the key's secret value. To view or create your own API keys, go to [API keys](../Other/usage-limits.md) in the Claude Console.

##### [Update API Key](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys/update)

POST/v1/organizations/api_keys/{api_key_id}

#### BetaOrganization[External Keys](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys)

##### [Create External Key](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys/create)

POST/v1/organizations/external_keys

Create an external key config owned by the caller's organization.

##### [List External Keys](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys/list)

GET/v1/organizations/external_keys

List external key configs in the caller's organization.

##### [Get External Key](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys/retrieve)

GET/v1/organizations/external_keys/{external_key_id}

Retrieve a single external key config in the caller's organization by ID.

##### [Update External Key](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys/update)

POST/v1/organizations/external_keys/{external_key_id}

Partially update an external key config. Omitted fields are left unchanged.

##### [Delete External Key](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys/delete)

DELETE/v1/organizations/external_keys/{external_key_id}

Delete an external key config.

##### [Validate External Key](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys/validate)

POST/v1/organizations/external_keys/{external_key_id}/validate

Validate an external key config against the customer's KMS.

#### BetaOrganizationFederation[Issuers](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers)

##### [Create Federation Issuer](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers/create)

POST/v1/organizations/federation_issuers

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Federation Issuers](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers/list)

GET/v1/organizations/federation_issuers

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Get Federation Issuer](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers/retrieve)

GET/v1/organizations/federation_issuers/{federation_issuer_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Update Federation Issuer](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers/update)

POST/v1/organizations/federation_issuers/{federation_issuer_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Archive Federation Issuer](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers/archive)

POST/v1/organizations/federation_issuers/{federation_issuer_id}/archive

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### BetaOrganizationFederation[Rules](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules)

##### [Create Federation Rule](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/create)

POST/v1/organizations/federation_rules

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Federation Rules](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/list)

GET/v1/organizations/federation_rules

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Get Federation Rule](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/retrieve)

GET/v1/organizations/federation_rules/{federation_rule_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Update Federation Rule](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/update)

POST/v1/organizations/federation_rules/{federation_rule_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Archive Federation Rule](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/archive)

POST/v1/organizations/federation_rules/{federation_rule_id}/archive

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### BetaOrganizationFederationRules[Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/workspaces)

##### [Add Federation Rule Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/workspaces/add)

POST/v1/organizations/federation_rules/{federation_rule_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Federation Rule Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/workspaces/list)

GET/v1/organizations/federation_rules/{federation_rule_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Remove Federation Rule Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/workspaces/remove)

DELETE/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### BetaOrganization[Invites](https://platform.claude.com/docs/en/api/http/beta/organization/invites)

##### [Create Invite](https://platform.claude.com/docs/en/api/http/beta/organization/invites/create)

POST/v1/organizations/invites

Invite a user to join the organization by email.

##### [List Invites](https://platform.claude.com/docs/en/api/http/beta/organization/invites/list)

GET/v1/organizations/invites

List the organization's invites.

##### [Get Invite](https://platform.claude.com/docs/en/api/http/beta/organization/invites/retrieve)

GET/v1/organizations/invites/{invite_id}

Retrieve an invite by ID.

##### [Delete Invite](https://platform.claude.com/docs/en/api/http/beta/organization/invites/delete)

DELETE/v1/organizations/invites/{invite_id}

Delete a pending invite.

#### BetaOrganization[Service Accounts](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts)

##### [Create Service Account](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/create)

POST/v1/organizations/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Service Accounts](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/list)

GET/v1/organizations/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Get Service Account](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/retrieve)

GET/v1/organizations/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Update Service Account](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/update)

POST/v1/organizations/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Archive Service Account](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/archive)

POST/v1/organizations/service_accounts/{service_account_id}/archive

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### BetaOrganizationService Accounts[Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/workspaces)

##### [Add Workspace To Service Account](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/workspaces/add)

POST/v1/organizations/service_accounts/{service_account_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [List Workspaces For Service Account](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/workspaces/list)

GET/v1/organizations/service_accounts/{service_account_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Remove Workspace From Service Account](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/workspaces/remove)

DELETE/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### BetaOrganization[Users](https://platform.claude.com/docs/en/api/http/beta/organization/users)

##### [List Users](https://platform.claude.com/docs/en/api/http/beta/organization/users/list)

GET/v1/organizations/users

List the organization's members.

##### [Get User](https://platform.claude.com/docs/en/api/http/beta/organization/users/retrieve)

GET/v1/organizations/users/{user_id}

Retrieve a member of the organization by user ID.

##### [Update User](https://platform.claude.com/docs/en/api/http/beta/organization/users/update)

POST/v1/organizations/users/{user_id}

Update a member's organization role.

##### [Remove User](https://platform.claude.com/docs/en/api/http/beta/organization/users/remove)

DELETE/v1/organizations/users/{user_id}

Remove a member from the organization.

#### BetaOrganization[Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces)

##### [List Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/list)

GET/v1/organizations/workspaces

##### [Create Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/create)

POST/v1/organizations/workspaces

##### [Get Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/retrieve)

GET/v1/organizations/workspaces/{workspace_id}

##### [Update Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/update)

POST/v1/organizations/workspaces/{workspace_id}

##### [Archive Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/archive)

POST/v1/organizations/workspaces/{workspace_id}/archive

#### BetaOrganizationWorkspaces[Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits)

##### [List Workspace Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits/list)

GET/v1/organizations/workspaces/{workspace_id}/rate_limits

List a workspace's rate limits.

#### BetaOrganizationWorkspaces[Members](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members)

##### [List Workspace Members](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members/list)

GET/v1/organizations/workspaces/{workspace_id}/members

##### [Create Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members/add)

POST/v1/organizations/workspaces/{workspace_id}/members

##### [Get Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Update Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members/update)

POST/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Delete Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/members/remove)

DELETE/v1/organizations/workspaces/{workspace_id}/members/{user_id}

#### BetaOrganizationWorkspaces[Service Accounts](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts)

##### [List Service Account Workspace Members](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts/list)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Create Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts/add)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Get Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Update Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts/update)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

##### [Delete Service Account Workspace Member](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/service_accounts/remove)

DELETE/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

#### BetaOrganization[Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/rate_limits)

##### [List Organization Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/rate_limits/list)

GET/v1/organizations/rate_limits

List Messages API rate limits for your organization.

#### BetaOrganization[Compliance Settings](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings)

##### [Get Compliance Settings](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings/retrieve)

GET/v1/organizations/compliance_settings

Retrieve your organization's Compliance Settings.

##### [Update Compliance Settings](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings/update)

POST/v1/organizations/compliance_settings

Update your organization's Compliance Settings.

#### BetaOrganization[Usage Report](https://platform.claude.com/docs/en/api/http/beta/organization/usage_report)

##### [Get Messages Usage Report](https://platform.claude.com/docs/en/api/http/beta/organization/usage_report/retrieve_messages)

GET/v1/organizations/usage_report/messages

##### [Get Claude Code Usage Report](https://platform.claude.com/docs/en/api/http/beta/organization/usage_report/retrieve_claude_code)

GET/v1/organizations/usage_report/claude_code

Retrieve daily aggregated usage metrics for Claude Code users. Enables organizations to analyze developer productivity and build custom dashboards.

#### BetaOrganization[Cost Report](https://platform.claude.com/docs/en/api/http/beta/organization/cost_report)

##### [Get Cost Report](https://platform.claude.com/docs/en/api/http/beta/organization/cost_report/retrieve)

GET/v1/organizations/cost_report

#### BetaOrganization[MCP Tunnels](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels)

##### [List Tunnels](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/list)

Deprecated

GET/v1/organizations/tunnels

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Get Tunnel](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Archive Tunnel](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/archive

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Reveal Tunnel Token](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/reveal_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/reveal_token

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Rotate Tunnel Token](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/rotate_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/rotate_token

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

#### BetaOrganizationMCP Tunnels[Tunnel Certificates](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates)

##### [Create Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/create)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [List Tunnel Certificates](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/list)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Get Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Archive Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}/archive

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

#### BetaOrganization[Analytics](../Admin/http-beta-organization-analytics.md)

##### [Get Activity Summaries](../Admin/http-beta-organization-analytics-retrieve-summaries.md)

GET/v1/organizations/analytics/summaries

Get organization-wide activity summaries for a date range.

#### BetaOrganizationAnalytics[Usage](../Admin/http-beta-organization-analytics-usage.md)

##### [Get Token Usage Over Time](../Admin/http-beta-organization-analytics-usage-list.md)

GET/v1/organizations/analytics/usage_report

Get token usage over time across a date range.

##### [Get Per-User Token Usage](../Admin/beta-organization-analytics-usage-list-by-user.md)

GET/v1/organizations/analytics/user_usage_report

Get per-user token usage across a date range.

#### BetaOrganizationAnalytics[Cost](../Admin/http-beta-organization-analytics-cost.md)

##### [Get Cost Over Time](../Admin/http-beta-organization-analytics-cost-list.md)

GET/v1/organizations/analytics/cost_report

Get cost in USD over time across a date range.

##### [Get Per-User Cost](../Admin/beta-organization-analytics-cost-list-by-user.md)

GET/v1/organizations/analytics/user_cost_report

Get per-user cost in USD across a date range.

#### BetaOrganizationAnalytics[Users](../Admin/http-beta-organization-analytics-users.md)

##### [List User Activity](../Admin/http-beta-organization-analytics-users-list.md)

GET/v1/organizations/analytics/users

Get per-user activity for a given day, with cursor-based pagination.

#### BetaOrganizationAnalytics[Skills](../Admin/beta-organization-analytics-skills.md)

##### [Get Skill Usage](../Admin/http-beta-organization-analytics-skills-list.md)

GET/v1/organizations/analytics/skills

Get per-skill usage for a given day, with cursor-based pagination.

#### BetaOrganizationAnalytics[Connectors](../Admin/beta-organization-analytics-connectors.md)

##### [Get Connector Usage](../Admin/http-beta-organization-analytics-connectors-list.md)

GET/v1/organizations/analytics/connectors

Get per-connector usage for a given day, with cursor-based pagination.

#### BetaOrganizationAnalytics[Chat Projects](../Admin/http-beta-organization-analytics-chat-projects.md)

##### [Get Chat Project Usage](../Admin/http-beta-organization-analytics-chat-projects-list.md)

GET/v1/organizations/analytics/apps/chat/projects

Get per-project activity for a given day, with cursor-based pagination.

#### BetaOrganizationAnalytics[Plugins](../Admin/http-beta-organization-analytics-plugins.md)

##### [Get Plugin Usage](../Admin/http-beta-organization-analytics-plugins-list.md)

GET/v1/organizations/analytics/plugins

Get per-plugin install + invocation usage for a given day, with pagination.

#### BetaOrganizationAnalytics[Artifacts](../Admin/beta-organization-analytics-artifacts.md)

##### [Get Artifact Activity](../Admin/http-beta-organization-analytics-artifacts-list.md)

GET/v1/organizations/analytics/artifacts

Get artifact-creation activity for a given day, broken out by MIME type.

#### BetaOrganization[Spend Limits](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits)

##### [Set Spend Limit](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/create)

POST/v1/organizations/spend_limits

Set a spend limit.

##### [Get Spend Limit](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/retrieve)

GET/v1/organizations/spend_limits/{spend_limit_id}

Retrieve a spend limit by ID.

##### [Delete Spend Limit](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/delete)

DELETE/v1/organizations/spend_limits/{spend_limit_id}

Delete a spend limit.

##### [List Effective Spend Limits](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/list_effective)

GET/v1/organizations/spend_limits/effective

List each member's effective spend limit and period-to-date spend.

#### BetaOrganizationSpend Limits[Increase Requests](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests)

##### [List Spend Limit Increase Requests](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/list)

GET/v1/organizations/spend_limit_increase_requests

List spend limit increase requests, most recent first.

##### [Get Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/retrieve)

GET/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}

Retrieve a spend limit increase request.

##### [Approve Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/approve)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve

Approve a pending spend limit increase request.

##### [Deny Spend Limit Increase Request](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/increase_requests/deny)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny

Deny a pending spend limit increase request.

#### BetaOrganization[RBAC Groups](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups)

##### [List RBAC Groups](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/list)

GET/v1/organizations/rbac_groups

List RBAC Groups in the Claude Enterprise tenant.

##### [Get RBAC Group](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/retrieve)

GET/v1/organizations/rbac_groups/{rbac_group_id}

Retrieve an RBAC Group by ID.

##### [Create RBAC Group](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/create)

POST/v1/organizations/rbac_groups

Create an RBAC Group in the Claude Enterprise tenant. Groups created via the API have source type `"direct"`.

##### [Update RBAC Group](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/update)

POST/v1/organizations/rbac_groups/{rbac_group_id}

Update an RBAC Group's name. Groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

##### [Delete RBAC Group](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/delete)

DELETE/v1/organizations/rbac_groups/{rbac_group_id}

Delete an RBAC Group. Groups provisioned by an identity provider (source type `"scim"`) cannot be deleted via the API while an organization in the tenant uses SCIM provisioning.

#### BetaOrganizationRBAC Groups[Members](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/members)

##### [List RBAC Group Members](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/members/list)

GET/v1/organizations/rbac_groups/{rbac_group_id}/members

List members of an RBAC Group.

##### [Add RBAC Group Member](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/members/create)

POST/v1/organizations/rbac_groups/{rbac_group_id}/members

Add a User to an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

##### [Remove RBAC Group Member](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/members/delete)

DELETE/v1/organizations/rbac_groups/{rbac_group_id}/members/{user_id}

Remove a User from an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

#### BetaOrganization[RBAC Roles](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles)

##### [List RBAC Roles](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles/list)

GET/v1/organizations/rbac_roles

List RBAC Roles in the organization.

##### [Get RBAC Role](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles/retrieve)

GET/v1/organizations/rbac_roles/{rbac_role_id}

Retrieve an RBAC Role by ID.

#### BetaOrganizationRBAC Roles[Permissions](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles/permissions)

##### [List RBAC Role Permissions](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_roles/permissions/list)

GET/v1/organizations/rbac_roles/{rbac_role_id}/permissions

List the permissions an RBAC Role grants.
