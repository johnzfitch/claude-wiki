---
title: "Beta - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-05T06:35:38Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)

# Beta

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### Models



AnthropicBeta = string or "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 52 more



Beta names you can send in the `anthropic-beta` header.

See [Beta headers](beta-headers.md) for how to send them and where to find the name a feature needs.

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

BetaError = [BetaInvalidRequestError](platform-claude-com-http-beta.md#beta_invalid_request_error) or [BetaAuthenticationError](platform-claude-com-http-beta.md#beta_authentication_error) or [BetaBillingError](platform-claude-com-http-beta.md#beta_billing_error) or 6 more

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

error: [BetaError](platform-claude-com-http-beta.md#beta_error)

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



amount: string



Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is \$25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

pattern^(0\|\[1-9\]\d\*)\$

currency: [BetaCurrency](platform-claude-com-http-beta.md#beta_currency)

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

#### Beta[Models](platform-claude-com-http-beta-models.md)

##### [List Models](platform-claude-com-http-beta-models-list.md)

GET/v1/models

List available models.

##### [Get a Model](platform-claude-com-http-beta-models-retrieve.md)

GET/v1/models/{model_id}

Get a specific model.

#### Beta[Messages](platform-claude-com-http-beta-messages.md)

##### [Create a Message](http-beta-messages-create.md)

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

##### [Count tokens in a Message](platform-claude-com-http-beta-messages-count-tokens.md)

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

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [List Agents](https://platform.claude.com/docs/en/api/http/beta/agents/list)

GET/v1/agents

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Get Agent](https://platform.claude.com/docs/en/api/http/beta/agents/retrieve)

GET/v1/agents/{agent_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Update Agent](https://platform.claude.com/docs/en/api/http/beta/agents/update)

POST/v1/agents/{agent_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Archive Agent](https://platform.claude.com/docs/en/api/http/beta/agents/archive)

POST/v1/agents/{agent_id}/archive

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

#### BetaAgents[Versions](https://platform.claude.com/docs/en/api/http/beta/agents/versions)

##### [List Agent Versions](https://platform.claude.com/docs/en/api/http/beta/agents/versions/list)

GET/v1/agents/{agent_id}/versions

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

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

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [List Sessions](https://platform.claude.com/docs/en/api/http/beta/sessions/list)

GET/v1/sessions

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Get Session](https://platform.claude.com/docs/en/api/http/beta/sessions/retrieve)

GET/v1/sessions/{session_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Update Session](https://platform.claude.com/docs/en/api/http/beta/sessions/update)

POST/v1/sessions/{session_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Delete Session](https://platform.claude.com/docs/en/api/http/beta/sessions/delete)

DELETE/v1/sessions/{session_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Archive Session](https://platform.claude.com/docs/en/api/http/beta/sessions/archive)

POST/v1/sessions/{session_id}/archive

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

#### BetaSessions[Events](https://platform.claude.com/docs/en/api/http/beta/sessions/events)

##### [List Events](https://platform.claude.com/docs/en/api/http/beta/sessions/events/list)

GET/v1/sessions/{session_id}/events

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Send Events](https://platform.claude.com/docs/en/api/http/beta/sessions/events/send)

POST/v1/sessions/{session_id}/events

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Stream Events](https://platform.claude.com/docs/en/api/http/beta/sessions/events/stream)

GET/v1/sessions/{session_id}/events/stream

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

#### BetaSessions[Resources](https://platform.claude.com/docs/en/api/http/beta/sessions/resources)

##### [Add Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/add)

POST/v1/sessions/{session_id}/resources

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [List Session Resources](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/list)

GET/v1/sessions/{session_id}/resources

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Get Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/retrieve)

GET/v1/sessions/{session_id}/resources/{resource_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Update Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/update)

POST/v1/sessions/{session_id}/resources/{resource_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Delete Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/delete)

DELETE/v1/sessions/{session_id}/resources/{resource_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

#### BetaSessions[Threads](https://platform.claude.com/docs/en/api/http/beta/sessions/threads)

##### [List Session Threads](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/list)

GET/v1/sessions/{session_id}/threads

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Get Session Thread](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/retrieve)

GET/v1/sessions/{session_id}/threads/{thread_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Archive Session Thread](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/archive)

POST/v1/sessions/{session_id}/threads/{thread_id}/archive

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

#### BetaSessionsThreads[Events](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/events)

##### [List Session Thread Events](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/events/list)

GET/v1/sessions/{session_id}/threads/{thread_id}/events

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Stream Session Thread Events](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/events/stream)

GET/v1/sessions/{session_id}/threads/{thread_id}/stream

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

#### Beta[Deployments](https://platform.claude.com/docs/en/api/http/beta/deployments)

##### [Create Deployment](https://platform.claude.com/docs/en/api/http/beta/deployments/create)

POST/v1/deployments

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [List Deployments](https://platform.claude.com/docs/en/api/http/beta/deployments/list)

GET/v1/deployments

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Get Deployment](https://platform.claude.com/docs/en/api/http/beta/deployments/retrieve)

GET/v1/deployments/{deployment_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Update Deployment](https://platform.claude.com/docs/en/api/http/beta/deployments/update)

POST/v1/deployments/{deployment_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Archive Deployment](https://platform.claude.com/docs/en/api/http/beta/deployments/archive)

POST/v1/deployments/{deployment_id}/archive

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Run Deployment Now](https://platform.claude.com/docs/en/api/http/beta/deployments/run)

POST/v1/deployments/{deployment_id}/run

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Pause Deployment](https://platform.claude.com/docs/en/api/http/beta/deployments/pause)

POST/v1/deployments/{deployment_id}/pause

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Unpause Deployment](https://platform.claude.com/docs/en/api/http/beta/deployments/unpause)

POST/v1/deployments/{deployment_id}/unpause

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

#### Beta[Deployment Runs](https://platform.claude.com/docs/en/api/http/beta/deployment_runs)

##### [List Deployment Runs](https://platform.claude.com/docs/en/api/http/beta/deployment_runs/list)

GET/v1/deployment_runs

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Get Deployment Run](https://platform.claude.com/docs/en/api/http/beta/deployment_runs/retrieve)

GET/v1/deployment_runs/{deployment_run_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

#### Beta[Vaults](https://platform.claude.com/docs/en/api/http/beta/vaults)

##### [Create a Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/create)

POST/v1/vaults

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [List Vaults](https://platform.claude.com/docs/en/api/http/beta/vaults/list)

GET/v1/vaults

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Retrieve a Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/retrieve)

GET/v1/vaults/{vault_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Update a Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/update)

POST/v1/vaults/{vault_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Delete a Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/delete)

DELETE/v1/vaults/{vault_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Archive a Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/archive)

POST/v1/vaults/{vault_id}/archive

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

#### BetaVaults[Credentials](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials)

##### [Create a Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/create)

POST/v1/vaults/{vault_id}/credentials

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [List Credentials](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/list)

GET/v1/vaults/{vault_id}/credentials

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Retrieve a Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/retrieve)

GET/v1/vaults/{vault_id}/credentials/{credential_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Update a Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/update)

POST/v1/vaults/{vault_id}/credentials/{credential_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Delete a Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/delete)

DELETE/v1/vaults/{vault_id}/credentials/{credential_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Archive a Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/archive)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/archive

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Validate an MCP OAuth Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/mcp_oauth_validate)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

#### Beta[Memory Stores](https://platform.claude.com/docs/en/api/http/beta/memory_stores)

##### [Create a Memory Store](https://platform.claude.com/docs/en/api/http/beta/memory_stores/create)

POST/v1/memory_stores

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [List Memory Stores](https://platform.claude.com/docs/en/api/http/beta/memory_stores/list)

GET/v1/memory_stores

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Retrieve a Memory Store](https://platform.claude.com/docs/en/api/http/beta/memory_stores/retrieve)

GET/v1/memory_stores/{memory_store_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Update a Memory Store](https://platform.claude.com/docs/en/api/http/beta/memory_stores/update)

POST/v1/memory_stores/{memory_store_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Delete a Memory Store](https://platform.claude.com/docs/en/api/http/beta/memory_stores/delete)

DELETE/v1/memory_stores/{memory_store_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Archive a Memory Store](https://platform.claude.com/docs/en/api/http/beta/memory_stores/archive)

POST/v1/memory_stores/{memory_store_id}/archive

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

#### BetaMemory Stores[Memories](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories)

##### [Create a Memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/create)

POST/v1/memory_stores/{memory_store_id}/memories

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [List Memories](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/list)

GET/v1/memory_stores/{memory_store_id}/memories

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Retrieve a Memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/retrieve)

GET/v1/memory_stores/{memory_store_id}/memories/{memory_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Update a Memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/update)

POST/v1/memory_stores/{memory_store_id}/memories/{memory_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Delete a Memory](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memories/delete)

DELETE/v1/memory_stores/{memory_store_id}/memories/{memory_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

#### BetaMemory Stores[Memory Versions](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions)

##### [List Memory Versions](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions/list)

GET/v1/memory_stores/{memory_store_id}/memory_versions

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Retrieve a Memory Version](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions/retrieve)

GET/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Redact a Memory Version](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions/redact)

POST/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

#### Beta[Files](platform-claude-com-http-beta-files.md)

##### [Upload File](platform-claude-com-http-beta-files-upload.md)

POST/v1/files

##### [List Files](platform-claude-com-http-beta-files-list.md)

GET/v1/files

##### [Download File](platform-claude-com-http-beta-files-download.md)

GET/v1/files/{file_id}/content

##### [Get File Metadata](platform-claude-com-http-beta-files-retrieve-metadata.md)

GET/v1/files/{file_id}

##### [Delete File](platform-claude-com-http-beta-files-delete.md)

DELETE/v1/files/{file_id}

#### Beta[Skills](platform-claude-com-http-beta-skills.md)

##### [Create Skill](platform-claude-com-http-beta-skills-create.md)

POST/v1/skills

##### [List Skills](platform-claude-com-http-beta-skills-list.md)

GET/v1/skills

##### [Get Skill](platform-claude-com-http-beta-skills-retrieve.md)

GET/v1/skills/{skill_id}

##### [Delete Skill](platform-claude-com-http-beta-skills-delete.md)

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

#### Beta[User Profiles](platform-claude-com-http-beta-user-profiles.md)

##### [Create User Profile](platform-claude-com-http-beta-user-profiles-create.md)

POST/v1/user_profiles

##### [List User Profiles](platform-claude-com-http-beta-user-profiles-list.md)

GET/v1/user_profiles

##### [Get User Profile](platform-claude-com-http-beta-user-profiles-retrieve.md)

GET/v1/user_profiles/{user_profile_id}

##### [Update User Profile](platform-claude-com-http-beta-user-profiles-update.md)

POST/v1/user_profiles/{user_profile_id}

##### [Delete User Profile](https://platform.claude.com/docs/en/api/http/beta/user_profiles/delete)

DELETE/v1/user_profiles/{user_profile_id}

##### [Create Enrollment URL](platform-claude-com-http-beta-user-profiles-create-enrollment-url.md)

POST/v1/user_profiles/{user_profile_id}/enrollment_url

#### BetaUser Profiles[Action URLs](https://platform.claude.com/docs/en/api/http/beta/user_profiles/action_urls)

##### [Create Action URL](https://platform.claude.com/docs/en/api/http/beta/user_profiles/action_urls/create)

POST/v1/user_profiles/{user_profile_id}/action_urls

#### Beta[Dreams](https://platform.claude.com/docs/en/api/http/beta/dreams)

##### [Create a Dream](https://platform.claude.com/docs/en/api/http/beta/dreams/create)

POST/v1/dreams

Requires `anthropic-beta: ``dreaming-2026-04-21`. [How to send beta headers](beta-headers.md)

Start an asynchronous job that uses past sessions to produce a reorganized version of a memory store and get back the dream to poll for the result.

##### [List Dreams](https://platform.claude.com/docs/en/api/http/beta/dreams/list)

GET/v1/dreams

Requires `anthropic-beta: ``dreaming-2026-04-21`. [How to send beta headers](beta-headers.md)

List the dreams in the workspace, newest first.

##### [Get a Dream](https://platform.claude.com/docs/en/api/http/beta/dreams/retrieve)

GET/v1/dreams/{dream_id}

Requires `anthropic-beta: ``dreaming-2026-04-21`. [How to send beta headers](beta-headers.md)

Get a dream by ID to check its status, output memory store, and token usage.

##### [Cancel a Dream](https://platform.claude.com/docs/en/api/http/beta/dreams/cancel)

POST/v1/dreams/{dream_id}/cancel

Requires `anthropic-beta: ``dreaming-2026-04-21`. [How to send beta headers](beta-headers.md)

Stop a `pending` or `running` dream.

##### [Archive a Dream](https://platform.claude.com/docs/en/api/http/beta/dreams/archive)

POST/v1/dreams/{dream_id}/archive

Requires `anthropic-beta: ``dreaming-2026-04-21`. [How to send beta headers](beta-headers.md)

Hide a `completed`, `failed`, or `canceled` dream from the default list of dreams.

#### Beta[Tunnels](platform-claude-com-http-beta-tunnels.md)

##### [Create Tunnel](platform-claude-com-http-beta-tunnels-create.md)

POST/v1/tunnels

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. [How to send beta headers](beta-headers.md)

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Get Tunnel](platform-claude-com-http-beta-tunnels-retrieve.md)

GET/v1/tunnels/{tunnel_id}

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. [How to send beta headers](beta-headers.md)

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [List Tunnels](platform-claude-com-http-beta-tunnels-list.md)

GET/v1/tunnels

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. [How to send beta headers](beta-headers.md)

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Archive Tunnel](platform-claude-com-http-beta-tunnels-archive.md)

POST/v1/tunnels/{tunnel_id}/archive

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. [How to send beta headers](beta-headers.md)

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Reveal Tunnel Token](platform-claude-com-http-beta-tunnels-reveal-token.md)

POST/v1/tunnels/{tunnel_id}/reveal_token

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. [How to send beta headers](beta-headers.md)

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Rotate Tunnel Token](platform-claude-com-http-beta-tunnels-rotate-token.md)

POST/v1/tunnels/{tunnel_id}/rotate_token

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. [How to send beta headers](beta-headers.md)

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

#### BetaTunnels[Certificates](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates)

##### [Create Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/create)

POST/v1/tunnels/{tunnel_id}/certificates

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. [How to send beta headers](beta-headers.md)

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Get Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/retrieve)

GET/v1/tunnels/{tunnel_id}/certificates/{certificate_id}

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. [How to send beta headers](beta-headers.md)

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [List Tunnel Certificates](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/list)

GET/v1/tunnels/{tunnel_id}/certificates

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. [How to send beta headers](beta-headers.md)

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

##### [Archive Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/tunnels/certificates/archive)

POST/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive

Requires `anthropic-beta: ``mcp-tunnels-2026-06-22`. [How to send beta headers](beta-headers.md)

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

#### Beta[Organization](../Admin/platform-claude-com-http-beta-organization.md)

##### [Get Current Organization](../Admin/http-beta-organization-retrieve.md)

GET/v1/organizations/me

Retrieve information about the organization associated with the authenticated API key.

#### BetaOrganization[API Keys](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys)

##### [List API Keys](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys/list)

GET/v1/organizations/api_keys

##### [Retrieve API Key (Admin API)](https://platform.claude.com/docs/en/api/http/beta/organization/api_keys/retrieve)

GET/v1/organizations/api_keys/{api_key_id}

Retrieve information about a single API key in your organization, looked up by its ID. This Admin API endpoint requires an Admin API key, is intended for programmatic key management, and never returns the key's secret value. To view or create your own API keys, go to [API keys](../Other/playground.md) in the Claude Console.

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

##### [Set Workspace Rate Limits](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/rate_limits/update)

POST/v1/organizations/workspaces/{workspace_id}/rate_limits/{rate_limit_id}

Set or clear rate-limit overrides for one rate-limit group in a workspace.

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

\[Legacy\] Get a report of your organization's Messages API usage, aggregated into time buckets.

##### [Get Claude Code Usage Report](https://platform.claude.com/docs/en/api/http/beta/organization/usage_report/retrieve_claude_code)

GET/v1/organizations/usage_report/claude_code

Retrieve daily aggregated usage metrics for Claude Code users. Enables organizations to analyze developer productivity and build custom dashboards.

#### BetaOrganization[Cost Report](https://platform.claude.com/docs/en/api/http/beta/organization/cost_report)

##### [Get Cost Report](https://platform.claude.com/docs/en/api/http/beta/organization/cost_report/retrieve)

GET/v1/organizations/cost_report

\[Legacy\] Get a report of your organization's Claude API costs in USD, aggregated into daily buckets.

#### BetaOrganization[MCP Tunnels](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels)

##### [List Tunnels](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/list)

Deprecated

GET/v1/organizations/tunnels

Requires `anthropic-beta: ``mcp-tunnels-2026-05-19`. [How to send beta headers](beta-headers.md)

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Get Tunnel](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}

Requires `anthropic-beta: ``mcp-tunnels-2026-05-19`. [How to send beta headers](beta-headers.md)

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Archive Tunnel](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/archive

Requires `anthropic-beta: ``mcp-tunnels-2026-05-19`. [How to send beta headers](beta-headers.md)

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Reveal Tunnel Token](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/reveal_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/reveal_token

Requires `anthropic-beta: ``mcp-tunnels-2026-05-19`. [How to send beta headers](beta-headers.md)

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Rotate Tunnel Token](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/rotate_token)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/rotate_token

Requires `anthropic-beta: ``mcp-tunnels-2026-05-19`. [How to send beta headers](beta-headers.md)

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

#### BetaOrganizationMCP Tunnels[Tunnel Certificates](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates)

##### [Create Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/create)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates

Requires `anthropic-beta: ``mcp-tunnels-2026-05-19`. [How to send beta headers](beta-headers.md)

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [List Tunnel Certificates](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/list)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates

Requires `anthropic-beta: ``mcp-tunnels-2026-05-19`. [How to send beta headers](beta-headers.md)

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Get Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/retrieve)

Deprecated

GET/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}

Requires `anthropic-beta: ``mcp-tunnels-2026-05-19`. [How to send beta headers](beta-headers.md)

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

##### [Archive Tunnel Certificate](https://platform.claude.com/docs/en/api/http/beta/organization/mcp_tunnels/tunnel_certificates/archive)

Deprecated

POST/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}/archive

Requires `anthropic-beta: ``mcp-tunnels-2026-05-19`. [How to send beta headers](beta-headers.md)

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](http-beta-tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

#### BetaOrganizationAnalytics[Summaries](../Admin/http-beta-organization-analytics-summaries.md)

##### [Get Activity Summaries](../Admin/http-beta-organization-analytics-summaries-list.md)

GET/v1/organizations/analytics/summaries

Get organization-wide activity summaries for a date range.

#### BetaOrganizationAnalytics[Users](../Admin/platform-claude-com-http-beta-organization-analytics-users.md)

##### [List User Activity](../Admin/platform-claude-com-http-beta-organization-analytics-users-list.md)

GET/v1/organizations/analytics/users

Get per-user activity for a given day, with cursor-based pagination.

#### BetaOrganizationAnalyticsAppsChat[Projects](../Admin/http-beta-organization-analytics-apps-chat-projects.md)

##### [Get Chat Project Usage](../Admin/http-beta-organization-analytics-apps-chat-projects-list.md)

GET/v1/organizations/analytics/apps/chat/projects

Get per-project activity for a given day, with cursor-based pagination.

#### BetaOrganizationAnalytics[Connectors](../Admin/http-beta-organization-analytics-connectors.md)

##### [Get Connector Usage](../Admin/platform-claude-com-http-beta-organization-analytics-connectors-list.md)

GET/v1/organizations/analytics/connectors

Get per-connector usage for a given day, with cursor-based pagination.

#### BetaOrganizationAnalytics[Plugins](../Admin/platform-claude-com-http-beta-organization-analytics-plugins.md)

##### [Get Plugin Usage](../Admin/platform-claude-com-http-beta-organization-analytics-plugins-list.md)

GET/v1/organizations/analytics/plugins

Get per-plugin install + invocation usage for a given day, with pagination.

#### BetaOrganizationAnalytics[Skills](../Admin/http-beta-organization-analytics-skills.md)

##### [Get Skill Usage](../Admin/platform-claude-com-http-beta-organization-analytics-skills-list.md)

GET/v1/organizations/analytics/skills

Get per-skill usage for a given day, with cursor-based pagination.

#### BetaOrganizationAnalytics[Artifacts](../Admin/http-beta-organization-analytics-artifacts.md)

##### [Get Artifact Activity](../Admin/platform-claude-com-http-beta-organization-analytics-artifacts-list.md)

GET/v1/organizations/analytics/artifacts

Get artifact-creation activity for a given day, broken out by MIME type.

#### BetaOrganizationAnalytics[Usage](../Admin/platform-claude-com-http-beta-organization-analytics-usage.md)

##### [Get Token Usage By Dimension](../Admin/platform-claude-com-http-beta-organization-analytics-usage-list.md)

GET/v1/organizations/analytics/usage

Requires `anthropic-beta: ``analytics-usage-cost-2026-08-24`. [How to send beta headers](beta-headers.md)

Get token usage across a date range, broken out by dimension.

#### BetaOrganizationAnalytics[Cost](../Admin/platform-claude-com-http-beta-organization-analytics-cost.md)

##### [Get Cost By Dimension](../Admin/platform-claude-com-http-beta-organization-analytics-cost-list.md)

GET/v1/organizations/analytics/cost

Requires `anthropic-beta: ``analytics-usage-cost-2026-08-24`. [How to send beta headers](beta-headers.md)

Get cost in USD across a date range, broken out by dimension.

#### BetaOrganizationAnalytics[Usage Report](../Admin/http-beta-organization-analytics-usage-report.md)

##### [Get Token Usage Over Time](../Admin/http-beta-organization-analytics-usage-report-list.md)

GET/v1/organizations/analytics/usage_report

\[Legacy\] Get token usage over time across a date range.

#### BetaOrganizationAnalytics[User Usage Report](../Admin/http-beta-organization-analytics-user-usage-report.md)

##### [Get Per-User Token Usage](../Admin/http-beta-organization-analytics-user-usage-report-list.md)

GET/v1/organizations/analytics/user_usage_report

\[Legacy\] Get per-user token usage across a date range.

#### BetaOrganizationAnalytics[Cost Report](../Admin/http-beta-organization-analytics-cost-report.md)

##### [Get Cost Over Time](../Admin/http-beta-organization-analytics-cost-report-list.md)

GET/v1/organizations/analytics/cost_report

\[Legacy\] Get cost in USD over time across a date range.

#### BetaOrganizationAnalytics[User Cost Report](../Admin/http-beta-organization-analytics-user-cost-report.md)

##### [Get Per-User Cost](../Admin/http-beta-organization-analytics-user-cost-report-list.md)

GET/v1/organizations/analytics/user_cost_report

\[Legacy\] Get per-user cost in USD across a date range.

#### BetaOrganization[Spend Limits](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits)

##### [Set Spend Limit](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/set)

POST/v1/organizations/spend_limits

Set a spend limit.

##### [Get Spend Limit](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/retrieve)

GET/v1/organizations/spend_limits/{spend_limit_id}

Retrieve a spend limit by ID.

##### [Delete Spend Limit](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/delete)

DELETE/v1/organizations/spend_limits/{spend_limit_id}

Delete a spend limit.

##### [List Spend Limits](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/list)

GET/v1/organizations/spend_limits

Requires `anthropic-beta: ``spend-limit-reads-2026-09-26`. [How to send beta headers](beta-headers.md)

List the organization's spend limits.

#### BetaOrganizationSpend Limits[Effective](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/effective)

##### [List Effective Spend Limits](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits/effective/list)

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

##### [Create RBAC Group](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/create)

POST/v1/organizations/rbac_groups

Create an RBAC Group in the Claude Enterprise tenant. Groups created via the API have source type `"direct"`.

##### [List RBAC Groups](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/list)

GET/v1/organizations/rbac_groups

List RBAC Groups in the Claude Enterprise tenant.

##### [Get RBAC Group](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/retrieve)

GET/v1/organizations/rbac_groups/{rbac_group_id}

Retrieve an RBAC Group by ID.

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

##### [Add RBAC Group Member](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/members/add)

POST/v1/organizations/rbac_groups/{rbac_group_id}/members

Add a User to an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

##### [Remove RBAC Group Member](https://platform.claude.com/docs/en/api/http/beta/organization/rbac_groups/members/remove)

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

#### BetaOrganization[Plugins](https://platform.claude.com/docs/en/api/http/beta/organization/plugins)

##### [Create Plugin](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/create)

POST/v1/organizations/plugins

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

Create an organization-owned Plugin and its first version by uploading the version's files.

##### [Get Plugin](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/retrieve)

GET/v1/organizations/plugins/{plugin_id}

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

Retrieve a Plugin by ID.

##### [Update Plugin](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/update)

POST/v1/organizations/plugins/{plugin_id}

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

Change which stored version of an organization-owned Plugin is served to members, for example to roll back to an earlier one. This pins the served version: later uploads are stored but no longer change what is served, and pinning cannot currently be undone, here or in claude.ai.

##### [List Plugins](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/list)

GET/v1/organizations/plugins

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

List the Plugins created under the organization, newest first: those in the organization's own plugin marketplaces and those in members' personal plugin marketplaces.

##### [Delete Plugin](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/delete)

DELETE/v1/organizations/plugins/{plugin_id}

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

Permanently delete a Plugin and every version it holds, exactly as when an administrator deletes it in claude.ai. The Plugin may belong to the organization or to a member, including a member who has since left the organization.

#### BetaOrganizationPlugins[Versions](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions)

##### [Create Plugin Version](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions/create)

POST/v1/organizations/plugins/{plugin_id}/versions

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

Add a version to an organization-owned Plugin by uploading the new version's files; it becomes the version served to members unless the Plugin's served version has been pinned.

##### [List Plugin Versions](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions/list)

GET/v1/organizations/plugins/{plugin_id}/versions

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

List a Plugin's versions, newest first.

##### [Get Plugin Version](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions/retrieve)

GET/v1/organizations/plugins/{plugin_id}/versions/{version}

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

Retrieve one version of a Plugin by its ID, or the Plugin's newest version.

##### [Download Plugin Version Archive](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions/download)

GET/v1/organizations/plugins/{plugin_id}/versions/{version}/content

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

Download one version's `.zip` archive, exactly as stored. Each download of a Plugin from a member's personal plugin marketplace is recorded on the Compliance API activity feed.

#### BetaOrganizationPlugins[Installation Settings](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings)

##### [List Plugin Installation Settings](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/list)

GET/v1/organizations/plugins/{plugin_id}/installation_settings

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

List an organization-owned Plugin's installation settings, which say which members it is for, most recently created first.

##### [Set Plugin Installation Setting](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/set)

POST/v1/organizations/plugins/{plugin_id}/installation_settings/{target}

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

Set or change an organization-owned Plugin's installation setting for the whole organization or for one RBAC Group.

##### [Remove Plugin Installation Setting](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/remove)

DELETE/v1/organizations/plugins/{plugin_id}/installation_settings/{target}

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

Remove an organization-owned Plugin's own installation setting for the whole organization or for one RBAC Group.

#### BetaOrganizationPlugins[Shares](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/shares)

##### [List Plugin Shares](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/shares/list)

GET/v1/organizations/plugins/{plugin_id}/shares

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

List the shares the owner of a member-owned Plugin has given — to every member of the organization, to an RBAC Group, or to one member — most recently granted first.

#### BetaOrganization[Plugin Marketplaces](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces)

##### [List Plugin Marketplaces](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces/list)

GET/v1/organizations/plugin_marketplaces

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

List the plugin marketplaces Plugins live in, newest first: the organization's own and its members' personal ones.

##### [Get Plugin Marketplace](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces/retrieve)

GET/v1/organizations/plugin_marketplaces/{marketplace_id}

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

Retrieve a plugin marketplace by ID.

##### [Update Plugin Marketplace](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces/update)

POST/v1/organizations/plugin_marketplaces/{marketplace_id}

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

Set the default installation setting of one of the organization's own plugin marketplaces. Every Plugin in it without a setting of its own gets this default as its organization-wide setting, including Plugins added later.

##### [Validate Plugin Marketplace Repository](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces/validate_repository)

POST/v1/organizations/plugin_marketplaces/validate_repository

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

Check whether a plugin marketplace held in a public GitHub repository would synchronize into claude.ai, without connecting or storing it.

##### [Validate Plugin Marketplace Archive](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces/validate_archive)

POST/v1/organizations/plugin_marketplaces/validate_archive

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. [How to send beta headers](beta-headers.md)

Check whether a plugin marketplace, uploaded as a `.zip` of the marketplace directory, would synchronize into claude.ai, without connecting or storing it.

#### BetaOrganization[Telemetry Destinations](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations)

##### [Create a Telemetry Destination](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/create)

POST/v1/organizations/telemetry_destinations

Requires `anthropic-beta: ``telemetry-destinations-2026-08-11`. [How to send beta headers](beta-headers.md)

Register an OpenTelemetry destination for the organization.

##### [List Telemetry Destinations](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/list)

GET/v1/organizations/telemetry_destinations

Requires `anthropic-beta: ``telemetry-destinations-2026-08-11`. [How to send beta headers](beta-headers.md)

List the organization's destinations, newest first, optionally only those that cover given workspaces.

##### [Retrieve a Telemetry Destination](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/retrieve)

GET/v1/organizations/telemetry_destinations/{destination_id}

Requires `anthropic-beta: ``telemetry-destinations-2026-08-11`. [How to send beta headers](beta-headers.md)

Read a destination's configuration, state, and most recent delivery results.

##### [Update a Telemetry Destination](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/update)

POST/v1/organizations/telemetry_destinations/{destination_id}

Requires `anthropic-beta: ``telemetry-destinations-2026-08-11`. [How to send beta headers](beta-headers.md)

Change a telemetry destination's settings, its state, or which workspaces it covers.

##### [Delete a Telemetry Destination](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/delete)

DELETE/v1/organizations/telemetry_destinations/{destination_id}

Requires `anthropic-beta: ``telemetry-destinations-2026-08-11`. [How to send beta headers](beta-headers.md)

Delete a destination and its workspace list.

##### [Test a Telemetry Destination](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/test)

POST/v1/organizations/telemetry_destinations/{destination_id}/test

Requires `anthropic-beta: ``telemetry-destinations-2026-08-11`. [How to send beta headers](beta-headers.md)

Send one test span, named `anthropic.test`, to the destination with its registered headers, once and without retries, and report the destination's answer. The response is 200 whether or not the destination answered with a 2xx status: its `result` has the type `success`, or the type `failure` and the reason in `error`. The destination's configuration, `state` and `delivery_health` do not change. A disabled destination can be tested too. Wait 10 seconds between tests of one destination; a request that comes sooner may be answered with status 429.

#### BetaOrganizationTelemetry Destinations[Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/workspaces)

##### [List Telemetry Destination Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/workspaces/list)

GET/v1/organizations/telemetry_destinations/{destination_id}/workspaces

Requires `anthropic-beta: ``telemetry-destinations-2026-08-11`. [How to send beta headers](beta-headers.md)

List the workspaces on a destination's workspace list, newest entry first.

##### [Add a Telemetry Destination Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/workspaces/add)

POST/v1/organizations/telemetry_destinations/{destination_id}/workspaces/{workspace_id}

Requires `anthropic-beta: ``telemetry-destinations-2026-08-11`. [How to send beta headers](beta-headers.md)

Add one workspace to a destination's workspace list.

##### [Remove a Telemetry Destination Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/workspaces/remove)

DELETE/v1/organizations/telemetry_destinations/{destination_id}/workspaces/{workspace_id}

Requires `anthropic-beta: ``telemetry-destinations-2026-08-11`. [How to send beta headers](beta-headers.md)

Remove one workspace from a destination's workspace list.

#### BetaOrganization[Webhooks](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks)

##### [Create Organization Webhook Endpoint](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/create)

POST/v1/organizations/webhooks

Requires `anthropic-beta: ``webhooks-2026-10-07`. [How to send beta headers](beta-headers.md)

Create an organization webhook endpoint.

##### [List Organization Webhook Endpoints](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/list)

GET/v1/organizations/webhooks

Requires `anthropic-beta: ``webhooks-2026-10-07`. [How to send beta headers](beta-headers.md)

List the organization's webhook endpoints.

##### [Get Organization Webhook Endpoint](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/retrieve)

GET/v1/organizations/webhooks/{webhook_endpoint_id}

Requires `anthropic-beta: ``webhooks-2026-10-07`. [How to send beta headers](beta-headers.md)

Retrieve an organization webhook endpoint by ID.

##### [Update Organization Webhook Endpoint](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/update)

POST/v1/organizations/webhooks/{webhook_endpoint_id}

Requires `anthropic-beta: ``webhooks-2026-10-07`. [How to send beta headers](beta-headers.md)

Update an organization webhook endpoint. Only the fields you send are changed.

##### [Delete Organization Webhook Endpoint](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/delete)

DELETE/v1/organizations/webhooks/{webhook_endpoint_id}

Requires `anthropic-beta: ``webhooks-2026-10-07`. [How to send beta headers](beta-headers.md)

Delete an organization webhook endpoint.

##### [Regenerate Organization Webhook Endpoint Signing Secret](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/regenerate_signing_secret)

POST/v1/organizations/webhooks/{webhook_endpoint_id}/regenerate_signing_secret

Requires `anthropic-beta: ``webhooks-2026-10-07`. [How to send beta headers](beta-headers.md)

Replace an organization webhook endpoint's signing secret. The old secret stops working immediately. The new secret is returned only in this response.

#### BetaOrganizationClaude Tag[Slack Channels](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_channels)

##### [Set Up Slack Channel](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_channels/create)

POST/v1/organizations/claude_tag/slack_channels

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](beta-headers.md)

Set a Slack channel up for Claude Tag and return it with its identifier. If the channel is already set up, whether in claude.ai, by Claude's first use in it or by an earlier request, the existing channel is returned, so the request can be repeated. `settings`, when sent, is applied as an update applies it. Before a channel is set up, Claude's Slack app confirms with Slack that the channel is in the workspace, is not archived and is visible to the app; a channel that fails the confirmation returns 404. Setting the channel up and applying `settings` are two steps: when the second is refused, the response is the refusal, the channel stays set up with every setting unset, and the error's `details.slack_channel_id` holds the channel's identifier.

##### [List Slack Channels](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_channels/list)

GET/v1/organizations/claude_tag/slack_channels

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](beta-headers.md)

List the set-up Slack channels of one Slack workspace, newest first by `created_at`. A channel that is not set up is not listed: Slack holds the full list of a workspace's channels. Pass `slack_channel_id` as well to look one channel up by its Slack identifiers: `data` then holds that channel, or is empty when it is not set up, and `limit` and `page` are ignored. A workspace that the organization owns only through a Slack Enterprise Grid returns 404 until it is set up. With `include_inherited=true` each channel's `settings` holds what applies in it, and the request fails with 503 rather than resolve against a settings level that could not be read. A `page` cursor resumes only a request with the same `include_inherited`.

##### [Get Slack Channel](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_channels/retrieve)

GET/v1/organizations/claude_tag/slack_channels/{id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](beta-headers.md)

Get one Slack channel and its settings. By default `settings` holds what the channel itself stores: a setting that is null there is not set on the channel and is inherited. With `include_inherited=true`, `settings` holds what applies in the channel once the settings levels above it are taken into account, and the request fails with 503 rather than resolve against a settings level that could not be read. Either way `sources` names the settings level each value comes from, so a caller tells the channel's own value from an inherited one by its source, not by whether it is null.

##### [Update Slack Channel](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_channels/update)

POST/v1/organizations/claude_tag/slack_channels/{id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](beta-headers.md)

Change the settings a Slack channel stores. The update is partial: a setting left out is unchanged, and a setting sent as null is cleared, so the channel inherits it. If any value is refused, no setting in the request is stored. A group direct message takes no settings and returns 400.

##### [Remove Slack Channel](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_channels/delete)

DELETE/v1/organizations/claude_tag/slack_channels/{id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](beta-headers.md)

Remove a Slack channel from Claude Tag. This deletes the channel's stored settings and its Bundle Targets at once, and then, in the background, the channel's sessions and their transcripts, its memory, its routines and the artifacts published from it. None of it can be restored. The channel in Slack and its messages are unchanged. The request is refused with 400 and `error.details.error_code` `slack_channel_enabled` while `enabled` resolves to `true` for the channel, as a read with `include_inherited=true` returns it: set `enabled` to `false` on the channel first. This guards against removing a channel in use by mistake; it is not a way to keep Claude out, because the removal deletes the channel's own `enabled: false` with its other settings, after which the channel inherits again and Claude's next use of it can set it up anew with a new identifier. The identifier returns 404 as soon as the request returns, so a repeated removal returns 404. A group direct message returns 400, and so does a channel that holds configuration this API does not manage.

#### BetaOrganizationClaude Tag[Slack Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_workspaces)

##### [List Slack Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_workspaces/list)

GET/v1/organizations/claude_tag/slack_workspaces

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](beta-headers.md)

List the set-up Slack workspaces the organization owns, newest first by `created_at`. Pass `slack_workspace_id` to look one workspace up by its Slack identifier: `data` then holds that workspace, or is empty when it is not set up. A workspace of a Slack Enterprise Grid the organization has connected returns 404 until it is set up. With `include_inherited=true` each workspace's `settings` holds what applies in it, and the request fails with 503 rather than resolve against a settings level that could not be read. A `page` cursor resumes only a request with the same `include_inherited`.

##### [Get Slack Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_workspaces/retrieve)

GET/v1/organizations/claude_tag/slack_workspaces/{id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](beta-headers.md)

Get one Slack workspace and its settings. By default `settings` holds what the workspace itself stores: a setting that is null there is not set on the workspace and is inherited. With `include_inherited=true`, `settings` holds what applies in the workspace once the organization's Slack defaults are taken into account, and the request fails with 503 rather than resolve against a settings level that could not be read. Either way `sources` names the settings level each value comes from.

##### [Update Slack Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_workspaces/update)

POST/v1/organizations/claude_tag/slack_workspaces/{id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](beta-headers.md)

Change the settings a Slack workspace stores. The update is partial: a setting left out is unchanged, and a setting sent as null is cleared, so the workspace inherits it. If any value is refused, no setting in the request is stored.

#### BetaOrganizationClaude Tag[Bundles](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles)

##### [List Bundles](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/list)

GET/v1/organizations/claude_tag/bundles

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](beta-headers.md)

List the organization's Bundles, newest first by `created_at`. A Bundle that Claude Tag manages for itself is not listed.

##### [Get Bundle](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/retrieve)

GET/v1/organizations/claude_tag/bundles/{bundle_id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](beta-headers.md)

Get one Bundle. What the Bundle grants (connectors, repositories and credentials) is never returned.

#### BetaOrganizationClaude TagBundles[Targets](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets)

##### [List Bundle Targets](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets/list)

GET/v1/organizations/claude_tag/bundles/{bundle_id}/targets

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](beta-headers.md)

List the Slack channels and Slack workspaces a Bundle is attached to, newest first by `created_at`. Only channels and workspaces the organization owns are listed; a Bundle that is attached to anything else has no Bundle Target for it.

##### [Attach Bundle](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets/create)

POST/v1/organizations/claude_tag/bundles/{bundle_id}/targets

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](beta-headers.md)

Attach a Bundle to a Slack channel or a Slack workspace. A Bundle attached to a workspace can be used in the workspace and in every channel in it. Attaching a Bundle to a channel or workspace it is already attached to returns the existing Bundle Target. The channel or workspace must be set up: attaching never sets a channel up. A group direct message takes no Bundle and returns 400.

##### [Get Bundle Target](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets/retrieve)

GET/v1/organizations/claude_tag/bundles/{bundle_id}/targets/{target_id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](beta-headers.md)

Get one Bundle Target. Returns 404 when `target_id` is the identifier of another Bundle's Bundle Target, or the Bundle Target was detached.

##### [Detach Bundle](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets/delete)

DELETE/v1/organizations/claude_tag/bundles/{bundle_id}/targets/{target_id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](beta-headers.md)

Detach a Bundle from a Slack channel or a Slack workspace. A repeated detach returns 404.
