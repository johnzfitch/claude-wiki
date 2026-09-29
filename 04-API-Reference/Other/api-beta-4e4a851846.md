---
title: "Beta - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:31Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


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

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

Copy page



cURL

1.  [API reference](/docs/en/api/http)

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

BetaError = [BetaInvalidRequestError](/docs/en/api/http/beta#beta_invalid_request_error) or [BetaAuthenticationError](/docs/en/api/http/beta#beta_authentication_error) or [BetaBillingError](/docs/en/api/http/beta#beta_billing_error) or 6 more

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

error: [BetaError](/docs/en/api/http/beta#beta_error)

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

currency: [BetaCurrency](/docs/en/api/http/beta#beta_currency)

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

#### Beta[Models](/docs/en/api/http/beta/models)

##### [List Models](/docs/en/api/http/beta/models/list)

GET/v1/models

List available models.

##### [Get a Model](/docs/en/api/http/beta/models/retrieve)

GET/v1/models/{model_id}

Get a specific model.

#### Beta[Messages](/docs/en/api/http/beta/messages)

##### [Create a Message](/docs/en/api/http/beta/messages/create)

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

##### [Count tokens in a Message](/docs/en/api/http/beta/messages/count_tokens)

POST/v1/messages/count_tokens

Count the number of tokens in a Message.

#### BetaMessages[Batches](/docs/en/api/http/beta/messages/batches)

##### [Create a Message Batch](/docs/en/api/http/beta/messages/batches/create)

POST/v1/messages/batches

Send a batch of Message creation requests.

##### [Retrieve a Message Batch](/docs/en/api/http/beta/messages/batches/retrieve)

GET/v1/messages/batches/{message_batch_id}

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

##### [List Message Batches](/docs/en/api/http/beta/messages/batches/list)

GET/v1/messages/batches

List all Message Batches within a Workspace. Most recently created batches are returned first.

##### [Cancel a Message Batch](/docs/en/api/http/beta/messages/batches/cancel)

POST/v1/messages/batches/{message_batch_id}/cancel

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

##### [Delete a Message Batch](/docs/en/api/http/beta/messages/batches/delete)

DELETE/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/http/beta/messages/batches/results)

GET/v1/messages/batches/{message_batch_id}/results

Streams the results of a Message Batch as a `.jsonl` file.

#### Beta[Agents](/docs/en/api/http/beta/agents)

##### [Create Agent](/docs/en/api/http/beta/agents/create)

POST/v1/agents

##### [List Agents](/docs/en/api/http/beta/agents/list)

GET/v1/agents

##### [Get Agent](/docs/en/api/http/beta/agents/retrieve)

GET/v1/agents/{agent_id}

##### [Update Agent](/docs/en/api/http/beta/agents/update)

POST/v1/agents/{agent_id}

##### [Archive Agent](/docs/en/api/http/beta/agents/archive)

POST/v1/agents/{agent_id}/archive

#### BetaAgents[Versions](/docs/en/api/http/beta/agents/versions)

##### [List Agent Versions](/docs/en/api/http/beta/agents/versions/list)

GET/v1/agents/{agent_id}/versions

#### Beta[Environments](/docs/en/api/http/beta/environments)

##### [Create Environment](/docs/en/api/http/beta/environments/create)

POST/v1/environments

Create a new environment with the specified configuration.

##### [List Environments](/docs/en/api/http/beta/environments/list)

GET/v1/environments

List environments with pagination support.

##### [Get Environment](/docs/en/api/http/beta/environments/retrieve)

GET/v1/environments/{environment_id}

Retrieve a specific environment by ID.

##### [Update Environment](/docs/en/api/http/beta/environments/update)

POST/v1/environments/{environment_id}

Update an existing environment's configuration.

##### [Delete Environment](/docs/en/api/http/beta/environments/delete)

DELETE/v1/environments/{environment_id}

Delete an environment by ID. Returns a confirmation of the deletion.

##### [Archive Environment](/docs/en/api/http/beta/environments/archive)

POST/v1/environments/{environment_id}/archive

Archive an environment by ID. Archived environments cannot be used to create new sessions.

#### BetaEnvironments[Work](/docs/en/api/http/beta/environments/work)

##### [Get Work Item](/docs/en/api/http/beta/environments/work/retrieve)

GET/v1/environments/{environment_id}/work/{work_id}

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Poll for Work](/docs/en/api/http/beta/environments/work/poll)

GET/v1/environments/{environment_id}/work/poll

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Acknowledge Work](/docs/en/api/http/beta/environments/work/ack)

POST/v1/environments/{environment_id}/work/{work_id}/ack

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Record Heartbeat](/docs/en/api/http/beta/environments/work/heartbeat)

POST/v1/environments/{environment_id}/work/{work_id}/heartbeat

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Stop Work](/docs/en/api/http/beta/environments/work/stop)

POST/v1/environments/{environment_id}/work/{work_id}/stop

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [List Work Items](/docs/en/api/http/beta/environments/work/list)

GET/v1/environments/{environment_id}/work

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Update Work Item](/docs/en/api/http/beta/environments/work/update)

POST/v1/environments/{environment_id}/work/{work_id}

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

##### [Get Queue Statistics](/docs/en/api/http/beta/environments/work/stats)

GET/v1/environments/{environment_id}/work/stats

Get statistics about the work queue for an environment.

#### Beta[Sessions](/docs/en/api/http/beta/sessions)

##### [Create Session](/docs/en/api/http/beta/sessions/create)

POST/v1/sessions

##### [List Sessions](/docs/en/api/http/beta/sessions/list)

GET/v1/sessions

##### [Get Session](/docs/en/api/http/beta/sessions/retrieve)

GET/v1/sessions/{session_id}

##### [Update Session](/docs/en/api/http/beta/sessions/update)

POST/v1/sessions/{session_id}

##### [Delete Session](/docs/en/api/http/beta/sessions/delete)

DELETE/v1/sessions/{session_id}

##### [Archive Session](/docs/en/api/http/beta/sessions/archive)

POST/v1/sessions/{session_id}/archive

#### BetaSessions[Events](/docs/en/api/http/beta/sessions/events)

##### [List Events](/docs/en/api/http/beta/sessions/events/list)

GET/v1/sessions/{session_id}/events

##### [Send Events](/docs/en/api/http/beta/sessions/events/send)

POST/v1/sessions/{session_id}/events

##### [Stream Events](/docs/en/api/http/beta/sessions/events/stream)

GET/v1/sessions/{session_id}/events/stream

#### BetaSessions[Resources](/docs/en/api/http/beta/sessions/resources)

##### [Add Session Resource](/docs/en/api/http/beta/sessions/resources/add)

POST/v1/sessions/{session_id}/resources

##### [List Session Resources](/docs/en/api/http/beta/sessions/resources/list)

GET/v1/sessions/{session_id}/resources

##### [Get Session Resource](/docs/en/api/http/beta/sessions/resources/retrieve)

GET/v1/sessions/{session_id}/resources/{resource_id}

##### [Update Session Resource](/docs/en/api/http/beta/sessions/resources/update)

POST/v1/sessions/{session_id}/resources/{resource_id}

##### [Delete Session Resource](/docs/en/api/http/beta/sessions/resources/delete)

DELETE/v1/sessions/{session_id}/resources/{resource_id}

#### BetaSessions[Threads](/docs/en/api/http/beta/sessions/threads)

##### [List Session Threads](/docs/en/api/http/beta/sessions/threads/list)

GET/v1/sessions/{session_id}/threads

##### [Get Session Thread](/docs/en/api/http/beta/sessions/threads/retrieve)

GET/v1/sessions/{session_id}/threads/{thread_id}

##### [Archive Session Thread](/docs/en/api/http/beta/sessions/threads/archive)

POST/v1/sessions/{session_id}/threads/{thread_id}/archive

#### BetaSessionsThreads[Events](/docs/en/api/http/beta/sessions/threads/events)

##### [List Session Thread Events](/docs/en/api/http/beta/sessions/threads/events/list)

GET/v1/sessions/{session_id}/threads/{thread_id}/events

##### [Stream Session Thread Events](/docs/en/api/http/beta/sessions/threads/events/stream)

GET/v1/sessions/{session_id}/threads/{thread_id}/stream

#### Beta[Deployments](/docs/en/api/http/beta/deployments)

##### [Create Deployment](/docs/en/api/http/beta/deployments/create)

POST/v1/deployments

##### [List Deployments](/docs/en/api/http/beta/deployments/list)

GET/v1/deployments

##### [Get Deployment](/docs/en/api/http/beta/deployments/retrieve)

GET/v1/deployments/{deployment_id}

##### [Update Deployment](/docs/en/api/http/beta/deployments/update)

POST/v1/deployments/{deployment_id}

##### [Archive Deployment](/docs/en/api/http/beta/deployments/archive)

POST/v1/deployments/{deployment_id}/archive

##### [Run Deployment Now](/docs/en/api/http/beta/deployments/run)

POST/v1/deployments/{deployment_id}/run

##### [Pause Deployment](/docs/en/api/http/beta/deployments/pause)

POST/v1/deployments/{deployment_id}/pause

##### [Unpause Deployment](/docs/en/api/http/beta/deployments/unpause)

POST/v1/deployments/{deployment_id}/unpause

#### Beta[Deployment Runs](/docs/en/api/http/beta/deployment_runs)

##### [List Deployment Runs](/docs/en/api/http/beta/deployment_runs/list)

GET/v1/deployment_runs

##### [Get Deployment Run](/docs/en/api/http/beta/deployment_runs/retrieve)

GET/v1/deployment_runs/{deployment_run_id}

#### Beta[Vaults](/docs/en/api/http/beta/vaults)

##### [Create Vault](/docs/en/api/http/beta/vaults/create)

POST/v1/vaults

##### [List Vaults](/docs/en/api/http/beta/vaults/list)

GET/v1/vaults

##### [Get Vault](/docs/en/api/http/beta/vaults/retrieve)

GET/v1/vaults/{vault_id}

##### [Update Vault](/docs/en/api/http/beta/vaults/update)

POST/v1/vaults/{vault_id}

##### [Delete Vault](/docs/en/api/http/beta/vaults/delete)

DELETE/v1/vaults/{vault_id}

##### [Archive Vault](/docs/en/api/http/beta/vaults/archive)

POST/v1/vaults/{vault_id}/archive

#### BetaVaults[Credentials](/docs/en/api/http/beta/vaults/credentials)

##### [Create Credential](/docs/en/api/http/beta/vaults/credentials/create)

POST/v1/vaults/{vault_id}/credentials

##### [List Credentials](/docs/en/api/http/beta/vaults/credentials/list)

GET/v1/vaults/{vault_id}/credentials

##### [Get Credential](/docs/en/api/http/beta/vaults/credentials/retrieve)

GET/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Update Credential](/docs/en/api/http/beta/vaults/credentials/update)

POST/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Delete Credential](/docs/en/api/http/beta/vaults/credentials/delete)

DELETE/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Archive Credential](/docs/en/api/http/beta/vaults/credentials/archive)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/archive

##### [Validate Credential](/docs/en/api/http/beta/vaults/credentials/mcp_oauth_validate)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate

#### Beta[Memory Stores](/docs/en/api/http/beta/memory_stores)

##### [Create a memory store](/docs/en/api/http/beta/memory_stores/create)

POST/v1/memory_stores

##### [List memory stores](/docs/en/api/http/beta/memory_stores/list)

GET/v1/memory_stores

##### [Retrieve a memory store](/docs/en/api/http/beta/memory_stores/retrieve)

GET/v1/memory_stores/{memory_store_id}

##### [Update a memory store](/docs/en/api/http/beta/memory_stores/update)

POST/v1/memory_stores/{memory_store_id}

##### [Delete a memory store](/docs/en/api/http/beta/memory_stores/delete)

DELETE/v1/memory_stores/{memory_store_id}

##### [Archive a memory store](/docs/en/api/http/beta/memory_stores/archive)

POST/v1/memory_stores/{memory_store_id}/archive

#### BetaMemory Stores[Memories](/docs/en/api/http/beta/memory_stores/memories)

##### [Create a memory](/docs/en/api/http/beta/memory_stores/memories/create)

POST/v1/memory_stores/{memory_store_id}/memories

##### [List memories](/docs/en/api/http/beta/memory_stores/memories/list)

GET/v1/memory_stores/{memory_store_id}/memories

##### [Retrieve a memory](/docs/en/api/http/beta/memory_stores/memories/retrieve)

GET/v1/memory_stores/{memory_store_id}/memories/{memory_id}

##### [Update a memory](/docs/en/api/http/beta/memory_stores/memories/update)

POST/v1/memory_stores/{memory_store_id}/memories/{memory_id}

##### [Delete a memory](/docs/en/api/http/beta/memory_stores/memories/delete)

DELETE/v1/memory_stores/{memory_store_id}/memories/{memory_id}

#### BetaMemory Stores[Memory Versions](/docs/en/api/http/beta/memory_stores/memory_versions)

##### [List memory versions](/docs/en/api/http/beta/memory_stores/memory_versions/list)

GET/v1/memory_stores/{memory_store_id}/memory_versions

##### [Retrieve a memory version](/docs/en/api/http/beta/memory_stores/memory_versions/retrieve)

GET/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}

##### [Redact a memory version](/docs/en/api/http/beta/memory_stores/memory_versions/redact)

POST/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact

#### Beta[Files](/docs/en/api/http/beta/files)

##### [Upload File](/docs/en/api/http/beta/files/upload)

POST/v1/files

##### [List Files](/docs/en/api/http/beta/files/list)

GET/v1/files

##### [Download File](/docs/en/api/http/beta/files/download)

GET/v1/files/{file_id}/content

##### [Get File Metadata](/docs/en/api/http/beta/files/retrieve_metadata)

GET/v1/files/{file_id}

##### [Delete File](/docs/en/api/http/beta/files/delete)

DELETE/v1/files/{file_id}

#### Beta[Skills](/docs/en/api/http/beta/skills)

##### [Create Skill](/docs/en/api/http/beta/skills/create)

POST/v1/skills

##### [List Skills](/docs/en/api/http/beta/skills/list)

GET/v1/skills

##### [Get Skill](/docs/en/api/http/beta/skills/retrieve)

GET/v1/skills/{skill_id}

##### [Delete Skill](/docs/en/api/http/beta/skills/delete)

DELETE/v1/skills/{skill_id}

#### BetaSkills[Versions](/docs/en/api/http/beta/skills/versions)

##### [Create Skill Version](/docs/en/api/http/beta/skills/versions/create)

POST/v1/skills/{skill_id}/versions

##### [List Skill Versions](/docs/en/api/http/beta/skills/versions/list)

GET/v1/skills/{skill_id}/versions

##### [Download Skill Version Content](/docs/en/api/http/beta/skills/versions/download)

GET/v1/skills/{skill_id}/versions/{version}/content

Download a skill version's content as a zip archive.

##### [Get Skill Version](/docs/en/api/http/beta/skills/versions/retrieve)

GET/v1/skills/{skill_id}/versions/{version}

##### [Delete Skill Version](/docs/en/api/http/beta/skills/versions/delete)

DELETE/v1/skills/{skill_id}/versions/{version}

#### Beta[User Profiles](/docs/en/api/http/beta/user_profiles)

##### [Create User Profile](/docs/en/api/http/beta/user_profiles/create)

POST/v1/user_profiles

##### [List User Profiles](/docs/en/api/http/beta/user_profiles/list)

GET/v1/user_profiles

##### [Get User Profile](/docs/en/api/http/beta/user_profiles/retrieve)

GET/v1/user_profiles/{user_profile_id}

##### [Update User Profile](/docs/en/api/http/beta/user_profiles/update)

POST/v1/user_profiles/{user_profile_id}

##### [Create Enrollment URL](/docs/en/api/http/beta/user_profiles/create_enrollment_url)

POST/v1/user_profiles/{user_profile_id}/enrollment_url

#### Beta[Dreams](/docs/en/api/http/beta/dreams)

##### [Create a Dream](/docs/en/api/http/beta/dreams/create)

POST/v1/dreams

Start an asynchronous job that uses past sessions to produce a reorganized version of a memory store and get back the dream to poll for the result.

##### [List Dreams](/docs/en/api/http/beta/dreams/list)

GET/v1/dreams

List the dreams in the workspace, newest first.

##### [Get a Dream](/docs/en/api/http/beta/dreams/retrieve)

GET/v1/dreams/{dream_id}

Get a dream by ID to check its status, output memory store, and token usage.

##### [Cancel a Dream](/docs/en/api/http/beta/dreams/cancel)

POST/v1/dreams/{dream_id}/cancel

Stop a `pending` or `running` dream.

##### [Archive a Dream](/docs/en/api/http/beta/dreams/archive)

POST/v1/dreams/{dream_id}/archive

Hide a `completed`, `failed`, or `canceled` dream from the default list of dreams.

#### Beta[Tunnels](/docs/en/api/http/beta/tunnels)

##### [Create Tunnel](/docs/en/api/http/beta/tunnels/create)

POST/v1/tunnels

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Get Tunnel](/docs/en/api/http/beta/tunnels/retrieve)

GET/v1/tunnels/{tunnel_id}

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [List Tunnels](/docs/en/api/http/beta/tunnels/list)

GET/v1/tunnels

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Archive Tunnel](/docs/en/api/http/beta/tunnels/archive)

POST/v1/tunnels/{tunnel_id}/archive

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Reveal Tunnel Token](/docs/en/api/http/beta/tunnels/reveal_token)

POST/v1/tunnels/{tunnel_id}/reveal_token

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Rotate Tunnel Token](/docs/en/api/http/beta/tunnels/rotate_token)

POST/v1/tunnels/{tunnel_id}/rotate_token

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

#### BetaTunnels[Certificates](/docs/en/api/http/beta/tunnels/certificates)

##### [Create Tunnel Certificate](/docs/en/api/http/beta/tunnels/certificates/create)

POST/v1/tunnels/{tunnel_id}/certificates

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Get Tunnel Certificate](/docs/en/api/http/beta/tunnels/certificates/retrieve)

GET/v1/tunnels/{tunnel_id}/certificates/{certificate_id}

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [List Tunnel Certificates](/docs/en/api/http/beta/tunnels/certificates/list)

GET/v1/tunnels/{tunnel_id}/certificates

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Archive Tunnel Certificate](/docs/en/api/http/beta/tunnels/certificates/archive)

POST/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

#### Beta[Organization](/docs/en/api/http/beta/organization)

##### [Get Current Organization](/docs/en/api/http/beta/organization/retrieve)

GET/v1/organizations/me

Retrieve information about the organization associated with the authenticated API key.

#### BetaOrganization[API Keys](/docs/en/api/http/beta/organization/api_keys)

##### [List API Keys](/docs/en/api/http/beta/organization/api_keys/list)

GET/v1/organizations/api_keys

##### [Retrieve API Key (Admin API)](/docs/en/api/http/beta/organization/api_keys/retrieve)

GET/v1/organizations/api_keys/{api_key_id}

Retrieve information about a single API key in your organization, looked up by its ID. This Admin API endpoint requires an Admin API key, is intended for programmatic key management, and never returns the key's secret value. To view or create your own API keys, go to [API keys](https://platform.claude.com/settings/keys) in the Claude Console.

##### [Update API Key](/docs/en/api/http/beta/organization/api_keys/update)

POST/v1/organizations/api_keys/{api_key_id}

#### BetaOrganization[External Keys](/docs/en/api/http/beta/organization/external_keys)

##### [Create External Key](/docs/en/api/http/beta/organization/external_keys/create)

POST/v1/organizations/external_keys

Create an external key config owned by the caller's organization.

##### [List External Keys](/docs/en/api/http/beta/organization/external_keys/list)

GET/v1/organizations/external_keys

List external key configs in the caller's organization.

##### [Get External Key](/docs/en/api/http/beta/organization/external_keys/retrieve)

GET/v1/organizations/external_keys/{external_key_id}

Retrieve a single external key config in the caller's organization by ID.

##### [Update External Key](/docs/en/api/http/beta/organization/external_keys/update)

POST/v1/organizations/external_keys/{external_key_id}

Partially update an external key config. Omitted fields are left unchanged.

##### [Delete External Key](/docs/en/api/http/beta/organization/external_keys/delete)

DELETE/v1/organizations/external_keys/{external_key_id}

Delete an external key config.

##### [Validate External Key](/docs/en/api/http/beta/organization/external_keys/validate)

POST/v1/organizations/external_keys/{external_key_id}/validate

Validate an external key config against the customer's KMS.

#### BetaOrganizationFederation[Issuers](/docs/en/api/http/beta/organization/federation/issuers)

##### [Create Federation Issuer](/docs/en/api/http/beta/organization/federation/issuers/create)

POST/v1/organizations/federation_issuers

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [List Federation Issuers](/docs/en/api/http/beta/organization/federation/issuers/list)

GET/v1/organizations/federation_issuers

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [Get Federation Issuer](/docs/en/api/http/beta/organization/federation/issuers/retrieve)

GET/v1/organizations/federation_issuers/{federation_issuer_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [Update Federation Issuer](/docs/en/api/http/beta/organization/federation/issuers/update)

POST/v1/organizations/federation_issuers/{federation_issuer_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [Archive Federation Issuer](/docs/en/api/http/beta/organization/federation/issuers/archive)

POST/v1/organizations/federation_issuers/{federation_issuer_id}/archive

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

#### BetaOrganizationFederation[Rules](/docs/en/api/http/beta/organization/federation/rules)

##### [Create Federation Rule](/docs/en/api/http/beta/organization/federation/rules/create)

POST/v1/organizations/federation_rules

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [List Federation Rules](/docs/en/api/http/beta/organization/federation/rules/list)

GET/v1/organizations/federation_rules

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [Get Federation Rule](/docs/en/api/http/beta/organization/federation/rules/retrieve)

GET/v1/organizations/federation_rules/{federation_rule_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [Update Federation Rule](/docs/en/api/http/beta/organization/federation/rules/update)

POST/v1/organizations/federation_rules/{federation_rule_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [Archive Federation Rule](/docs/en/api/http/beta/organization/federation/rules/archive)

POST/v1/organizations/federation_rules/{federation_rule_id}/archive

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

#### BetaOrganizationFederationRules[Workspaces](/docs/en/api/http/beta/organization/federation/rules/workspaces)

##### [Add Federation Rule Workspace](/docs/en/api/http/beta/organization/federation/rules/workspaces/add)

POST/v1/organizations/federation_rules/{federation_rule_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [List Federation Rule Workspaces](/docs/en/api/http/beta/organization/federation/rules/workspaces/list)

GET/v1/organizations/federation_rules/{federation_rule_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [Remove Federation Rule Workspace](/docs/en/api/http/beta/organization/federation/rules/workspaces/remove)

DELETE/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

#### BetaOrganization[Invites](/docs/en/api/http/beta/organization/invites)

##### [Create Invite](/docs/en/api/http/beta/organization/invites/create)

POST/v1/organizations/invites

Invite a user to join the organization by email.

##### [List Invites](/docs/en/api/http/beta/organization/invites/list)

GET/v1/organizations/invites

List the organization's invites.

##### [Get Invite](/docs/en/api/http/beta/organization/invites/retrieve)

GET/v1/organizations/invites/{invite_id}

Retrieve an invite by ID.

##### [Delete Invite](/docs/en/api/http/beta/organization/invites/delete)

DELETE/v1/organizations/invites/{invite_id}

Delete a pending invite.

#### BetaOrganization[Service Accounts](/docs/en/api/http/beta/organization/service_accounts)

##### [Create Service Account](/docs/en/api/http/beta/organization/service_accounts/create)

POST/v1/organizations/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [List Service Accounts](/docs/en/api/http/beta/organization/service_accounts/list)

GET/v1/organizations/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [Get Service Account](/docs/en/api/http/beta/organization/service_accounts/retrieve)

GET/v1/organizations/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [Update Service Account](/docs/en/api/http/beta/organization/service_accounts/update)

POST/v1/organizations/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [Archive Service Account](/docs/en/api/http/beta/organization/service_accounts/archive)

POST/v1/organizations/service_accounts/{service_account_id}/archive

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

#### BetaOrganizationService Accounts[Workspaces](/docs/en/api/http/beta/organization/service_accounts/workspaces)

##### [Add Workspace To Service Account](/docs/en/api/http/beta/organization/service_accounts/workspaces/add)

POST/v1/organizations/service_accounts/{service_account_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [List Workspaces For Service Account](/docs/en/api/http/beta/organization/service_accounts/workspaces/list)

GET/v1/organizations/service_accounts/{service_account_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [Remove Workspace From Service Account](/docs/en/api/http/beta/organization/service_accounts/workspaces/remove)

DELETE/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

#### BetaOrganization[Users](/docs/en/api/http/beta/organization/users)

##### [List Users](/docs/en/api/http/beta/organization/users/list)

GET/v1/organizations/users

List the organization's members.

##### [Get User](/docs/en/api/http/beta/organization/users/retrieve)

GET/v1/organizations/users/{user_id}

Retrieve a member of the organization by user ID.

##### [Update User](/docs/en/api/http/beta/organization/users/update)

POST/v1/organizations/users/{user_id}

Update a member's organization role.

##### [Remove User](/docs/en/api/http/beta/organization/users/remove)

DELETE/v1/organizations/users/{user_id}

Remove a member from the organization.

#### BetaOrganization[Workspaces](/docs/en/api/http/beta/organization/workspaces)

##### [List Workspaces](/docs/en/api/http/beta/organization/workspaces/list)

GET/v1/organizations/workspaces

##### [Create Workspace](/docs/en/api/http/beta/organization/workspaces/create)

POST/v1/organizations/workspaces

##### [Get Workspace](/docs/en/api/http/beta/organization/workspaces/retrieve)

GET/v1/organizations/workspaces/{workspace_id}

##### [Update Workspace](/docs/en/api/http/beta/organization/workspaces/update)

POST/v1/organizations/workspaces/{workspace_id}

##### [Archive Workspace](/docs/en/api/http/beta/organization/workspaces/archive)

POST/v1/organizations/workspaces/{workspace_id}/archive

#### BetaOrganizationWorkspaces[Rate Limits](/docs/en/api/http/beta/organization/workspaces/rate_limits)

##### [List Workspace Rate Limits](/docs/en/api/http/beta/organization/workspaces/rate_limits/list)

GET/v1/organizations/workspaces/{workspace_id}/rate_limits

List a workspace's rate limits.

#### BetaOrganizationWorkspaces[Members](/docs/en/api/http/beta/organization/workspaces/members)

##### [List Workspace Members](/docs/en/api/http/beta/organization/workspaces/members/list)

GET/v1/organizations/workspaces/{workspace_id}/members

##### [Create Workspace Member](/docs/en/api/http/beta/organization/workspaces/members/add)

POST/v1/organizations/workspaces/{workspace_id}/members

##### [Get Workspace Member](/docs/en/api/http/beta/organization/workspaces/members/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Update Workspace Member](/docs/en/api/http/beta/organization/workspaces/members/update)

POST/v1/organizations/workspaces/{workspace_id}/members/{user_id}

##### [Delete Workspace Member](/docs/en/api/http/beta/organization/workspaces/members/remove)

DELETE/v1/organizations/workspaces/{workspace_id}/members/{user_id}

#### BetaOrganizationWorkspaces[Service Accounts](/docs/en/api/http/beta/organization/workspaces/service_accounts)

##### [List Service Account Workspace Members](/docs/en/api/http/beta/organization/workspaces/service_accounts/list)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [Create Service Account Workspace Member](/docs/en/api/http/beta/organization/workspaces/service_accounts/add)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [Get Service Account Workspace Member](/docs/en/api/http/beta/organization/workspaces/service_accounts/retrieve)

GET/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [Update Service Account Workspace Member](/docs/en/api/http/beta/organization/workspaces/service_accounts/update)

POST/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

##### [Delete Service Account Workspace Member](/docs/en/api/http/beta/organization/workspaces/service_accounts/remove)

DELETE/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

#### BetaOrganization[Rate Limits](/docs/en/api/http/beta/organization/rate_limits)

##### [List Organization Rate Limits](/docs/en/api/http/beta/organization/rate_limits/list)

GET/v1/organizations/rate_limits

List Messages API rate limits for your organization.

#### BetaOrganization[Compliance Settings](/docs/en/api/http/beta/organization/compliance_settings)

##### [Get Compliance Settings](/docs/en/api/http/beta/organization/compliance_settings/retrieve)

GET/v1/organizations/compliance_settings

Retrieve your organization's Compliance Settings.

##### [Update Compliance Settings](/docs/en/api/http/beta/organization/compliance_settings/update)

POST/v1/organizations/compliance_settings

Update your organization's Compliance Settings.

#### BetaOrganization[Usage Report](/docs/en/api/http/beta/organization/usage_report)

##### [Get Messages Usage Report](/docs/en/api/http/beta/organization/usage_report/retrieve_messages)

GET/v1/organizations/usage_report/messages

##### [Get Claude Code Usage Report](/docs/en/api/http/beta/organization/usage_report/retrieve_claude_code)

GET/v1/organizations/usage_report/claude_code

Retrieve daily aggregated usage metrics for Claude Code users. Enables organizations to analyze developer productivity and build custom dashboards.

#### BetaOrganization[Cost Report](/docs/en/api/http/beta/organization/cost_report)

##### [Get Cost Report](/docs/en/api/http/beta/organization/cost_report/retrieve)

GET/v1/organizations/cost_report

#### BetaOrganization[MCP Tunnels](/docs/en/api/http/beta/organization/mcp_tunnels)

##### [List Tunnels](/docs/en/api/http/beta/organization/mcp_tunnels/list)

Deprecated

GET/v1/organizations/tunnels

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Get Tunnel](/docs/en/api/http/beta/organization/mcp_tunnels/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Archive Tunnel](/docs/en/api/http/beta/organization/mcp_tunnels/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/archive

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Reveal Tunnel Token](/docs/en/api/http/beta/organization/mcp_tunnels/reveal_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/reveal_token

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Rotate Tunnel Token](/docs/en/api/http/beta/organization/mcp_tunnels/rotate_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/rotate_token

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

#### BetaOrganizationMCP Tunnels[Tunnel Certificates](/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates)

##### [Create Tunnel Certificate](/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/create)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [List Tunnel Certificates](/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/list)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Get Tunnel Certificate](/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Archive Tunnel Certificate](/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}/archive

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

#### BetaOrganization[Analytics](/docs/en/api/http/beta/organization/analytics)

##### [Get Activity Summaries](/docs/en/api/http/beta/organization/analytics/retrieve_summaries)

GET/v1/organizations/analytics/summaries

Get organization-wide activity summaries for a date range.

#### BetaOrganizationAnalytics[Usage](/docs/en/api/http/beta/organization/analytics/usage)

##### [Get Token Usage Over Time](/docs/en/api/http/beta/organization/analytics/usage/list)

GET/v1/organizations/analytics/usage_report

Get token usage over time across a date range.

##### [Get Per-User Token Usage](/docs/en/api/http/beta/organization/analytics/usage/list_by_user)

GET/v1/organizations/analytics/user_usage_report

Get per-user token usage across a date range.

#### BetaOrganizationAnalytics[Cost](/docs/en/api/http/beta/organization/analytics/cost)

##### [Get Cost Over Time](/docs/en/api/http/beta/organization/analytics/cost/list)

GET/v1/organizations/analytics/cost_report

Get cost in USD over time across a date range.

##### [Get Per-User Cost](/docs/en/api/http/beta/organization/analytics/cost/list_by_user)

GET/v1/organizations/analytics/user_cost_report

Get per-user cost in USD across a date range.

#### BetaOrganizationAnalytics[Users](/docs/en/api/http/beta/organization/analytics/users)

##### [List User Activity](/docs/en/api/http/beta/organization/analytics/users/list)

GET/v1/organizations/analytics/users

Get per-user activity for a given day, with cursor-based pagination.

#### BetaOrganizationAnalytics[Skills](/docs/en/api/http/beta/organization/analytics/skills)

##### [Get Skill Usage](/docs/en/api/http/beta/organization/analytics/skills/list)

GET/v1/organizations/analytics/skills

Get per-skill usage for a given day, with cursor-based pagination.

#### BetaOrganizationAnalytics[Connectors](/docs/en/api/http/beta/organization/analytics/connectors)

##### [Get Connector Usage](/docs/en/api/http/beta/organization/analytics/connectors/list)

GET/v1/organizations/analytics/connectors

Get per-connector usage for a given day, with cursor-based pagination.

#### BetaOrganizationAnalytics[Chat Projects](/docs/en/api/http/beta/organization/analytics/chat_projects)

##### [Get Chat Project Usage](/docs/en/api/http/beta/organization/analytics/chat_projects/list)

GET/v1/organizations/analytics/apps/chat/projects

Get per-project activity for a given day, with cursor-based pagination.

#### BetaOrganizationAnalytics[Plugins](/docs/en/api/http/beta/organization/analytics/plugins)

##### [Get Plugin Usage](/docs/en/api/http/beta/organization/analytics/plugins/list)

GET/v1/organizations/analytics/plugins

Get per-plugin install + invocation usage for a given day, with pagination.

#### BetaOrganizationAnalytics[Artifacts](/docs/en/api/http/beta/organization/analytics/artifacts)

##### [Get Artifact Activity](/docs/en/api/http/beta/organization/analytics/artifacts/list)

GET/v1/organizations/analytics/artifacts

Get artifact-creation activity for a given day, broken out by MIME type.

#### BetaOrganization[Spend Limits](/docs/en/api/http/beta/organization/spend_limits)

##### [Set Spend Limit](/docs/en/api/http/beta/organization/spend_limits/create)

POST/v1/organizations/spend_limits

Set a spend limit.

##### [Get Spend Limit](/docs/en/api/http/beta/organization/spend_limits/retrieve)

GET/v1/organizations/spend_limits/{spend_limit_id}

Retrieve a spend limit by ID.

##### [Delete Spend Limit](/docs/en/api/http/beta/organization/spend_limits/delete)

DELETE/v1/organizations/spend_limits/{spend_limit_id}

Delete a spend limit.

##### [List Effective Spend Limits](/docs/en/api/http/beta/organization/spend_limits/list_effective)

GET/v1/organizations/spend_limits/effective

List each member's effective spend limit and period-to-date spend.

#### BetaOrganizationSpend Limits[Increase Requests](/docs/en/api/http/beta/organization/spend_limits/increase_requests)

##### [List Spend Limit Increase Requests](/docs/en/api/http/beta/organization/spend_limits/increase_requests/list)

GET/v1/organizations/spend_limit_increase_requests

List spend limit increase requests, most recent first.

##### [Get Spend Limit Increase Request](/docs/en/api/http/beta/organization/spend_limits/increase_requests/retrieve)

GET/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}

Retrieve a spend limit increase request.

##### [Approve Spend Limit Increase Request](/docs/en/api/http/beta/organization/spend_limits/increase_requests/approve)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve

Approve a pending spend limit increase request.

##### [Deny Spend Limit Increase Request](/docs/en/api/http/beta/organization/spend_limits/increase_requests/deny)

POST/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny

Deny a pending spend limit increase request.

#### BetaOrganization[RBAC Groups](/docs/en/api/http/beta/organization/rbac_groups)

##### [List RBAC Groups](/docs/en/api/http/beta/organization/rbac_groups/list)

GET/v1/organizations/rbac_groups

List RBAC Groups in the Claude Enterprise tenant.

##### [Get RBAC Group](/docs/en/api/http/beta/organization/rbac_groups/retrieve)

GET/v1/organizations/rbac_groups/{rbac_group_id}

Retrieve an RBAC Group by ID.

##### [Create RBAC Group](/docs/en/api/http/beta/organization/rbac_groups/create)

POST/v1/organizations/rbac_groups

Create an RBAC Group in the Claude Enterprise tenant. Groups created via the API have source type `"direct"`.

##### [Update RBAC Group](/docs/en/api/http/beta/organization/rbac_groups/update)

POST/v1/organizations/rbac_groups/{rbac_group_id}

Update an RBAC Group's name. Groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

##### [Delete RBAC Group](/docs/en/api/http/beta/organization/rbac_groups/delete)

DELETE/v1/organizations/rbac_groups/{rbac_group_id}

Delete an RBAC Group. Groups provisioned by an identity provider (source type `"scim"`) cannot be deleted via the API while an organization in the tenant uses SCIM provisioning.

#### BetaOrganizationRBAC Groups[Members](/docs/en/api/http/beta/organization/rbac_groups/members)

##### [List RBAC Group Members](/docs/en/api/http/beta/organization/rbac_groups/members/list)

GET/v1/organizations/rbac_groups/{rbac_group_id}/members

List members of an RBAC Group.

##### [Add RBAC Group Member](/docs/en/api/http/beta/organization/rbac_groups/members/create)

POST/v1/organizations/rbac_groups/{rbac_group_id}/members

Add a User to an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

##### [Remove RBAC Group Member](/docs/en/api/http/beta/organization/rbac_groups/members/delete)

DELETE/v1/organizations/rbac_groups/{rbac_group_id}/members/{user_id}

Remove a User from an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

#### BetaOrganization[RBAC Roles](/docs/en/api/http/beta/organization/rbac_roles)

##### [List RBAC Roles](/docs/en/api/http/beta/organization/rbac_roles/list)

GET/v1/organizations/rbac_roles

List RBAC Roles in the organization.

##### [Get RBAC Role](/docs/en/api/http/beta/organization/rbac_roles/retrieve)

GET/v1/organizations/rbac_roles/{rbac_role_id}

Retrieve an RBAC Role by ID.

#### BetaOrganizationRBAC Roles[Permissions](/docs/en/api/http/beta/organization/rbac_roles/permissions)

##### [List RBAC Role Permissions](/docs/en/api/http/beta/organization/rbac_roles/permissions/list)

GET/v1/organizations/rbac_roles/{rbac_role_id}/permissions

List the permissions an RBAC Role grants.
