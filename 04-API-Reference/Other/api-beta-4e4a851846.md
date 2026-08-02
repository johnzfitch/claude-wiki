---
title: "Beta - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:38:06Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores


Models


List Models


Get a Model


Dreams


Create a Dream


List Dreams


Get a Dream


Cancel a Dream


Archive a Dream


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Webhooks


Admin

Organizations

Invites

Users

RBAC Groups

RBAC Roles

Workspaces

API Keys

External Keys

Usage Report

Cost Report

Analytics

Spend Limits

Rate Limits

Service Accounts

Federation Issuers

Federation Rules

MCP Tunnels


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

[](/login)




API reference

Beta




cURL

# Beta

##### ModelsExpand Collapse 



AnthropicBeta = string or "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more



One of the following:

string



[](#anthropic_beta%5B0%5D)



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 29 more



One of the following:

"message-batches-2024-09-24"



[](#anthropic_beta%5B1%5D%5B0%5D)

"prompt-caching-2024-07-31"



[](#anthropic_beta%5B1%5D%5B1%5D)

"computer-use-2024-10-22"



[](#anthropic_beta%5B1%5D%5B2%5D)

"computer-use-2025-01-24"



[](#anthropic_beta%5B1%5D%5B3%5D)

"pdfs-2024-09-25"



[](#anthropic_beta%5B1%5D%5B4%5D)

"token-counting-2024-11-01"



[](#anthropic_beta%5B1%5D%5B5%5D)

"token-efficient-tools-2025-02-19"



[](#anthropic_beta%5B1%5D%5B6%5D)

"output-128k-2025-02-19"



[](#anthropic_beta%5B1%5D%5B7%5D)

"files-api-2025-04-14"



[](#anthropic_beta%5B1%5D%5B8%5D)

"mcp-client-2025-04-04"



[](#anthropic_beta%5B1%5D%5B9%5D)

"mcp-client-2025-11-20"



[](#anthropic_beta%5B1%5D%5B10%5D)

"dev-full-thinking-2025-05-14"



[](#anthropic_beta%5B1%5D%5B11%5D)

"interleaved-thinking-2025-05-14"



[](#anthropic_beta%5B1%5D%5B12%5D)

"code-execution-2025-05-22"



[](#anthropic_beta%5B1%5D%5B13%5D)

"extended-cache-ttl-2025-04-11"



[](#anthropic_beta%5B1%5D%5B14%5D)

"context-1m-2025-08-07"



[](#anthropic_beta%5B1%5D%5B15%5D)

"context-management-2025-06-27"



[](#anthropic_beta%5B1%5D%5B16%5D)

"model-context-window-exceeded-2025-08-26"



[](#anthropic_beta%5B1%5D%5B17%5D)

"skills-2025-10-02"



[](#anthropic_beta%5B1%5D%5B18%5D)

"fast-mode-2026-02-01"



[](#anthropic_beta%5B1%5D%5B19%5D)

"output-300k-2026-03-24"



[](#anthropic_beta%5B1%5D%5B20%5D)

"user-profiles-2026-03-24"



[](#anthropic_beta%5B1%5D%5B21%5D)

"advisor-tool-2026-03-01"



[](#anthropic_beta%5B1%5D%5B22%5D)

"managed-agents-2026-04-01"



[](#anthropic_beta%5B1%5D%5B23%5D)

"cache-diagnosis-2026-04-07"



[](#anthropic_beta%5B1%5D%5B24%5D)

"dreaming-2026-04-21"



[](#anthropic_beta%5B1%5D%5B25%5D)

"thinking-token-count-2026-05-13"



[](#anthropic_beta%5B1%5D%5B26%5D)

"server-side-fallback-2026-06-01"



[](#anthropic_beta%5B1%5D%5B27%5D)

"server-side-fallback-2026-07-01"



[](#anthropic_beta%5B1%5D%5B28%5D)

"fallback-credit-2026-06-01"



[](#anthropic_beta%5B1%5D%5B29%5D)

"fallback-credit-2026-07-01"



[](#anthropic_beta%5B1%5D%5B30%5D)

"agent-memory-2026-07-22"



[](#anthropic_beta%5B1%5D%5B31%5D)

[](#anthropic_beta%5B1%5D)

[](#anthropic_beta)



BetaAPIError object { message, type }



message: string



[](#beta_api_error.message)

type: "api_error"



[](#beta_api_error.type)

[](#beta_api_error)



BetaAuthenticationError object { message, type }



message: string



[](#beta_authentication_error.message)

type: "authentication_error"



[](#beta_authentication_error.type)

[](#beta_authentication_error)



BetaBillingError object { message, type }



message: string



[](#beta_billing_error.message)

type: "billing_error"



[](#beta_billing_error.type)

[](#beta_billing_error)



BetaError = [BetaInvalidRequestError](/docs/en/api/beta#beta_invalid_request_error) { message, type } or [BetaAuthenticationError](/docs/en/api/beta#beta_authentication_error) { message, type } or [BetaBillingError](/docs/en/api/beta#beta_billing_error) { message, type } or 6 more



One of the following:



BetaInvalidRequestError object { message, type }



message: string



[](#beta_invalid_request_error.message)

type: "invalid_request_error"



[](#beta_invalid_request_error.type)

[](#beta_invalid_request_error)



BetaAuthenticationError object { message, type }



message: string



[](#beta_authentication_error.message)

type: "authentication_error"



[](#beta_authentication_error.type)

[](#beta_authentication_error)



BetaBillingError object { message, type }



message: string



[](#beta_billing_error.message)

type: "billing_error"



[](#beta_billing_error.type)

[](#beta_billing_error)



BetaPermissionError object { message, type }



message: string



[](#beta_permission_error.message)

type: "permission_error"



[](#beta_permission_error.type)

[](#beta_permission_error)



BetaNotFoundError object { message, type }



message: string



[](#beta_not_found_error.message)

type: "not_found_error"



[](#beta_not_found_error.type)

[](#beta_not_found_error)



BetaRateLimitError object { message, type }



message: string



[](#beta_rate_limit_error.message)

type: "rate_limit_error"



[](#beta_rate_limit_error.type)

[](#beta_rate_limit_error)



BetaGatewayTimeoutError object { message, type }



message: string



[](#beta_gateway_timeout_error.message)

type: "timeout_error"



[](#beta_gateway_timeout_error.type)

[](#beta_gateway_timeout_error)



BetaAPIError object { message, type }



message: string



[](#beta_api_error.message)

type: "api_error"



[](#beta_api_error.type)

[](#beta_api_error)



BetaOverloadedError object { message, type }



message: string



[](#beta_overloaded_error.message)

type: "overloaded_error"



[](#beta_overloaded_error.type)

[](#beta_overloaded_error)

[](#beta_error)



BetaErrorResponse object { error, request_id, type }





error: [BetaError](/docs/en/api/beta#beta_error)



One of the following:



BetaInvalidRequestError object { message, type }



message: string



[](#beta_error_response.error%20%2B%20(resource)%20beta.message)

type: "invalid_request_error"



[](#beta_error_response.error%20%2B%20(resource)%20beta.type)

[](#beta_error_response.error%20%2B%20(resource)%20beta)



BetaAuthenticationError object { message, type }



message: string



[](#beta_error_response.error%20%2B%20(resource)%20beta.message)

type: "authentication_error"



[](#beta_error_response.error%20%2B%20(resource)%20beta.type)

[](#beta_error_response.error%20%2B%20(resource)%20beta)



BetaBillingError object { message, type }



message: string



[](#beta_error_response.error%20%2B%20(resource)%20beta.message)

type: "billing_error"



[](#beta_error_response.error%20%2B%20(resource)%20beta.type)

[](#beta_error_response.error%20%2B%20(resource)%20beta)



BetaPermissionError object { message, type }



message: string



[](#beta_error_response.error%20%2B%20(resource)%20beta.message)

type: "permission_error"



[](#beta_error_response.error%20%2B%20(resource)%20beta.type)

[](#beta_error_response.error%20%2B%20(resource)%20beta)



BetaNotFoundError object { message, type }



message: string



[](#beta_error_response.error%20%2B%20(resource)%20beta.message)

type: "not_found_error"



[](#beta_error_response.error%20%2B%20(resource)%20beta.type)

[](#beta_error_response.error%20%2B%20(resource)%20beta)



BetaRateLimitError object { message, type }



message: string



[](#beta_error_response.error%20%2B%20(resource)%20beta.message)

type: "rate_limit_error"



[](#beta_error_response.error%20%2B%20(resource)%20beta.type)

[](#beta_error_response.error%20%2B%20(resource)%20beta)



BetaGatewayTimeoutError object { message, type }



message: string



[](#beta_error_response.error%20%2B%20(resource)%20beta.message)

type: "timeout_error"



[](#beta_error_response.error%20%2B%20(resource)%20beta.type)

[](#beta_error_response.error%20%2B%20(resource)%20beta)



BetaAPIError object { message, type }



message: string



[](#beta_error_response.error%20%2B%20(resource)%20beta.message)

type: "api_error"



[](#beta_error_response.error%20%2B%20(resource)%20beta.type)

[](#beta_error_response.error%20%2B%20(resource)%20beta)



BetaOverloadedError object { message, type }



message: string



[](#beta_error_response.error%20%2B%20(resource)%20beta.message)

type: "overloaded_error"



[](#beta_error_response.error%20%2B%20(resource)%20beta.type)

[](#beta_error_response.error%20%2B%20(resource)%20beta)

[](#beta_error_response.error)

request_id: string



[](#beta_error_response.request_id)

type: "error"



[](#beta_error_response.type)

[](#beta_error_response)



BetaGatewayTimeoutError object { message, type }



message: string



[](#beta_gateway_timeout_error.message)

type: "timeout_error"



[](#beta_gateway_timeout_error.type)

[](#beta_gateway_timeout_error)



BetaInvalidRequestError object { message, type }



message: string



[](#beta_invalid_request_error.message)

type: "invalid_request_error"



[](#beta_invalid_request_error.type)

[](#beta_invalid_request_error)



BetaNotFoundError object { message, type }



message: string



[](#beta_not_found_error.message)

type: "not_found_error"



[](#beta_not_found_error.type)

[](#beta_not_found_error)



BetaOverloadedError object { message, type }



message: string



[](#beta_overloaded_error.message)

type: "overloaded_error"



[](#beta_overloaded_error.type)

[](#beta_overloaded_error)



BetaPermissionError object { message, type }



message: string



[](#beta_permission_error.message)

type: "permission_error"



[](#beta_permission_error.type)

[](#beta_permission_error)



BetaRateLimitError object { message, type }



message: string



[](#beta_rate_limit_error.message)

type: "rate_limit_error"



[](#beta_rate_limit_error.type)

[](#beta_rate_limit_error)

#### BetaModels

##### [List Models](/docs/en/api/beta/models/list)

GET/v1/models

##### [Get a Model](/docs/en/api/beta/models/retrieve)

GET/v1/models/{model_id}

#### BetaMessages

##### [Create a Message](/docs/en/api/beta/messages/create)

POST/v1/messages

##### [Count tokens in a Message](/docs/en/api/beta/messages/count_tokens)

POST/v1/messages/count_tokens

#### BetaMessagesBatches

##### [Create a Message Batch](/docs/en/api/beta/messages/batches/create)

POST/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/beta/messages/batches/retrieve)

GET/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/beta/messages/batches/list)

GET/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/beta/messages/batches/cancel)

POST/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/beta/messages/batches/delete)

DELETE/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/beta/messages/batches/results)

GET/v1/messages/batches/{message_batch_id}/results

#### BetaAgents

##### [Create Agent](/docs/en/api/beta/agents/create)

POST/v1/agents

##### [List Agents](/docs/en/api/beta/agents/list)

GET/v1/agents

##### [Get Agent](/docs/en/api/beta/agents/retrieve)

GET/v1/agents/{agent_id}

##### [Update Agent](/docs/en/api/beta/agents/update)

POST/v1/agents/{agent_id}

##### [Archive Agent](/docs/en/api/beta/agents/archive)

POST/v1/agents/{agent_id}/archive

#### BetaAgentsVersions

##### [List Agent Versions](/docs/en/api/beta/agents/versions/list)

GET/v1/agents/{agent_id}/versions

#### BetaEnvironments

##### [Create Environment](/docs/en/api/beta/environments/create)

POST/v1/environments

##### [List Environments](/docs/en/api/beta/environments/list)

GET/v1/environments

##### [Get Environment](/docs/en/api/beta/environments/retrieve)

GET/v1/environments/{environment_id}

##### [Update Environment](/docs/en/api/beta/environments/update)

POST/v1/environments/{environment_id}

##### [Delete Environment](/docs/en/api/beta/environments/delete)

DELETE/v1/environments/{environment_id}

##### [Archive Environment](/docs/en/api/beta/environments/archive)

POST/v1/environments/{environment_id}/archive

#### BetaEnvironmentsWork

##### [Get Work Item](/docs/en/api/beta/environments/work/retrieve)

GET/v1/environments/{environment_id}/work/{work_id}

##### [Poll for Work](/docs/en/api/beta/environments/work/poll)

GET/v1/environments/{environment_id}/work/poll

##### [Acknowledge Work](/docs/en/api/beta/environments/work/ack)

POST/v1/environments/{environment_id}/work/{work_id}/ack

##### [Record Heartbeat](/docs/en/api/beta/environments/work/heartbeat)

POST/v1/environments/{environment_id}/work/{work_id}/heartbeat

##### [Stop Work](/docs/en/api/beta/environments/work/stop)

POST/v1/environments/{environment_id}/work/{work_id}/stop

##### [List Work Items](/docs/en/api/beta/environments/work/list)

GET/v1/environments/{environment_id}/work

##### [Update Work Item](/docs/en/api/beta/environments/work/update)

POST/v1/environments/{environment_id}/work/{work_id}

##### [Get Queue Statistics](/docs/en/api/beta/environments/work/stats)

GET/v1/environments/{environment_id}/work/stats

#### BetaSessions

##### [Create Session](/docs/en/api/beta/sessions/create)

POST/v1/sessions

##### [List Sessions](/docs/en/api/beta/sessions/list)

GET/v1/sessions

##### [Get Session](/docs/en/api/beta/sessions/retrieve)

GET/v1/sessions/{session_id}

##### [Update Session](/docs/en/api/beta/sessions/update)

POST/v1/sessions/{session_id}

##### [Delete Session](/docs/en/api/beta/sessions/delete)

DELETE/v1/sessions/{session_id}

##### [Archive Session](/docs/en/api/beta/sessions/archive)

POST/v1/sessions/{session_id}/archive

#### BetaSessionsEvents

##### [List Events](/docs/en/api/beta/sessions/events/list)

GET/v1/sessions/{session_id}/events

##### [Send Events](/docs/en/api/beta/sessions/events/send)

POST/v1/sessions/{session_id}/events

##### [Stream Events](/docs/en/api/beta/sessions/events/stream)

GET/v1/sessions/{session_id}/events/stream

#### BetaSessionsResources

##### [Add Session Resource](/docs/en/api/beta/sessions/resources/add)

POST/v1/sessions/{session_id}/resources

##### [List Session Resources](/docs/en/api/beta/sessions/resources/list)

GET/v1/sessions/{session_id}/resources

##### [Get Session Resource](/docs/en/api/beta/sessions/resources/retrieve)

GET/v1/sessions/{session_id}/resources/{resource_id}

##### [Update Session Resource](/docs/en/api/beta/sessions/resources/update)

POST/v1/sessions/{session_id}/resources/{resource_id}

##### [Delete Session Resource](/docs/en/api/beta/sessions/resources/delete)

DELETE/v1/sessions/{session_id}/resources/{resource_id}

#### BetaSessionsThreads

##### [List Session Threads](/docs/en/api/beta/sessions/threads/list)

GET/v1/sessions/{session_id}/threads

##### [Get Session Thread](/docs/en/api/beta/sessions/threads/retrieve)

GET/v1/sessions/{session_id}/threads/{thread_id}

##### [Archive Session Thread](/docs/en/api/beta/sessions/threads/archive)

POST/v1/sessions/{session_id}/threads/{thread_id}/archive

#### BetaSessionsThreadsEvents

##### [List Session Thread Events](/docs/en/api/beta/sessions/threads/events/list)

GET/v1/sessions/{session_id}/threads/{thread_id}/events

##### [Stream Session Thread Events](/docs/en/api/beta/sessions/threads/events/stream)

GET/v1/sessions/{session_id}/threads/{thread_id}/stream

#### BetaDeployments

##### [Create Deployment](/docs/en/api/beta/deployments/create)

POST/v1/deployments

##### [List Deployments](/docs/en/api/beta/deployments/list)

GET/v1/deployments

##### [Get Deployment](/docs/en/api/beta/deployments/retrieve)

GET/v1/deployments/{deployment_id}

##### [Update Deployment](/docs/en/api/beta/deployments/update)

POST/v1/deployments/{deployment_id}

##### [Archive Deployment](/docs/en/api/beta/deployments/archive)

POST/v1/deployments/{deployment_id}/archive

##### [Run Deployment Now](/docs/en/api/beta/deployments/run)

POST/v1/deployments/{deployment_id}/run

##### [Pause Deployment](/docs/en/api/beta/deployments/pause)

POST/v1/deployments/{deployment_id}/pause

##### [Unpause Deployment](/docs/en/api/beta/deployments/unpause)

POST/v1/deployments/{deployment_id}/unpause

#### BetaDeployment Runs

##### [List Deployment Runs](/docs/en/api/beta/deployment_runs/list)

GET/v1/deployment_runs

##### [Get Deployment Run](/docs/en/api/beta/deployment_runs/retrieve)

GET/v1/deployment_runs/{deployment_run_id}

#### BetaVaults

##### [Create Vault](/docs/en/api/beta/vaults/create)

POST/v1/vaults

##### [List Vaults](/docs/en/api/beta/vaults/list)

GET/v1/vaults

##### [Get Vault](/docs/en/api/beta/vaults/retrieve)

GET/v1/vaults/{vault_id}

##### [Update Vault](/docs/en/api/beta/vaults/update)

POST/v1/vaults/{vault_id}

##### [Delete Vault](/docs/en/api/beta/vaults/delete)

DELETE/v1/vaults/{vault_id}

##### [Archive Vault](/docs/en/api/beta/vaults/archive)

POST/v1/vaults/{vault_id}/archive

#### BetaVaultsCredentials

##### [Create Credential](/docs/en/api/beta/vaults/credentials/create)

POST/v1/vaults/{vault_id}/credentials

##### [List Credentials](/docs/en/api/beta/vaults/credentials/list)

GET/v1/vaults/{vault_id}/credentials

##### [Get Credential](/docs/en/api/beta/vaults/credentials/retrieve)

GET/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Update Credential](/docs/en/api/beta/vaults/credentials/update)

POST/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Delete Credential](/docs/en/api/beta/vaults/credentials/delete)

DELETE/v1/vaults/{vault_id}/credentials/{credential_id}

##### [Archive Credential](/docs/en/api/beta/vaults/credentials/archive)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/archive

##### [Validate Credential](/docs/en/api/beta/vaults/credentials/mcp_oauth_validate)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate

#### BetaMemory Stores

##### [Create a memory store](/docs/en/api/beta/memory_stores/create)

POST/v1/memory_stores

##### [List memory stores](/docs/en/api/beta/memory_stores/list)

GET/v1/memory_stores

##### [Retrieve a memory store](/docs/en/api/beta/memory_stores/retrieve)

GET/v1/memory_stores/{memory_store_id}

##### [Update a memory store](/docs/en/api/beta/memory_stores/update)

POST/v1/memory_stores/{memory_store_id}

##### [Delete a memory store](/docs/en/api/beta/memory_stores/delete)

DELETE/v1/memory_stores/{memory_store_id}

##### [Archive a memory store](/docs/en/api/beta/memory_stores/archive)

POST/v1/memory_stores/{memory_store_id}/archive

#### BetaMemory StoresMemories

##### [Create a memory](/docs/en/api/beta/memory_stores/memories/create)

POST/v1/memory_stores/{memory_store_id}/memories

##### [List memories](/docs/en/api/beta/memory_stores/memories/list)

GET/v1/memory_stores/{memory_store_id}/memories

##### [Retrieve a memory](/docs/en/api/beta/memory_stores/memories/retrieve)

GET/v1/memory_stores/{memory_store_id}/memories/{memory_id}

##### [Update a memory](/docs/en/api/beta/memory_stores/memories/update)

POST/v1/memory_stores/{memory_store_id}/memories/{memory_id}

##### [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete)

DELETE/v1/memory_stores/{memory_store_id}/memories/{memory_id}

#### BetaMemory StoresMemory Versions

##### [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list)

GET/v1/memory_stores/{memory_store_id}/memory_versions

##### [Retrieve a memory version](/docs/en/api/beta/memory_stores/memory_versions/retrieve)

GET/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}

##### [Redact a memory version](/docs/en/api/beta/memory_stores/memory_versions/redact)

POST/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact

#### BetaFiles

##### [Upload File](/docs/en/api/beta/files/upload)

POST/v1/files

##### [List Files](/docs/en/api/beta/files/list)

GET/v1/files

##### [Download File](/docs/en/api/beta/files/download)

GET/v1/files/{file_id}/content

##### [Get File Metadata](/docs/en/api/beta/files/retrieve_metadata)

GET/v1/files/{file_id}

##### [Delete File](/docs/en/api/beta/files/delete)

DELETE/v1/files/{file_id}

#### BetaSkills

##### [Create Skill](/docs/en/api/beta/skills/create)

POST/v1/skills

##### [List Skills](/docs/en/api/beta/skills/list)

GET/v1/skills

##### [Get Skill](/docs/en/api/beta/skills/retrieve)

GET/v1/skills/{skill_id}

##### [Delete Skill](/docs/en/api/beta/skills/delete)

DELETE/v1/skills/{skill_id}

#### BetaSkillsVersions

##### [Create Skill Version](/docs/en/api/beta/skills/versions/create)

POST/v1/skills/{skill_id}/versions

##### [List Skill Versions](/docs/en/api/beta/skills/versions/list)

GET/v1/skills/{skill_id}/versions

##### [Download Skill Version Content](/docs/en/api/beta/skills/versions/download)

GET/v1/skills/{skill_id}/versions/{version}/content

##### [Get Skill Version](/docs/en/api/beta/skills/versions/retrieve)

GET/v1/skills/{skill_id}/versions/{version}

##### [Delete Skill Version](/docs/en/api/beta/skills/versions/delete)

DELETE/v1/skills/{skill_id}/versions/{version}

#### BetaUser Profiles

##### [Create User Profile](/docs/en/api/beta/user_profiles/create)

POST/v1/user_profiles

##### [List User Profiles](/docs/en/api/beta/user_profiles/list)

GET/v1/user_profiles

##### [Get User Profile](/docs/en/api/beta/user_profiles/retrieve)

GET/v1/user_profiles/{user_profile_id}

##### [Update User Profile](/docs/en/api/beta/user_profiles/update)

POST/v1/user_profiles/{user_profile_id}

##### [Create Enrollment URL](/docs/en/api/beta/user_profiles/create_enrollment_url)

POST/v1/user_profiles/{user_profile_id}/enrollment_url

#### BetaDreams

##### [Create a Dream](/docs/en/api/beta/dreams/create)

POST/v1/dreams

##### [List Dreams](/docs/en/api/beta/dreams/list)

GET/v1/dreams

##### [Get a Dream](/docs/en/api/beta/dreams/retrieve)

GET/v1/dreams/{dream_id}

##### [Cancel a Dream](/docs/en/api/beta/dreams/cancel)

POST/v1/dreams/{dream_id}/cancel

##### [Archive a Dream](/docs/en/api/beta/dreams/archive)

POST/v1/dreams/{dream_id}/archive

#### BetaTunnels

##### [Create Tunnel](/docs/en/api/beta/tunnels/create)

POST/v1/tunnels

##### [Get Tunnel](/docs/en/api/beta/tunnels/retrieve)

GET/v1/tunnels/{tunnel_id}

##### [List Tunnels](/docs/en/api/beta/tunnels/list)

GET/v1/tunnels

##### [Archive Tunnel](/docs/en/api/beta/tunnels/archive)

POST/v1/tunnels/{tunnel_id}/archive

##### [Reveal Tunnel Token](/docs/en/api/beta/tunnels/reveal_token)

POST/v1/tunnels/{tunnel_id}/reveal_token

##### [Rotate Tunnel Token](/docs/en/api/beta/tunnels/rotate_token)

POST/v1/tunnels/{tunnel_id}/rotate_token

#### BetaTunnelsCertificates

##### [Create Tunnel Certificate](/docs/en/api/beta/tunnels/certificates/create)

POST/v1/tunnels/{tunnel_id}/certificates

##### [Get Tunnel Certificate](/docs/en/api/beta/tunnels/certificates/retrieve)

GET/v1/tunnels/{tunnel_id}/certificates/{certificate_id}

##### [List Tunnel Certificates](/docs/en/api/beta/tunnels/certificates/list)

GET/v1/tunnels/{tunnel_id}/certificates

##### [Archive Tunnel Certificate](/docs/en/api/beta/tunnels/certificates/archive)

POST/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive

#### BetaWebhooks

Helpers for receiving and verifying webhook events. Use `unwrap` in your SDK to verify signatures and parse payloads; see the [webhooks guide](/docs/en/managed-agents/webhooks) for handler examples.

Possible `data.type` values:

- `agent.archived`
- `agent.created`
- `agent.deleted`
- `agent.updated`
- `deployment.archived`
- `deployment.created`
- `deployment.deleted`
- `deployment.paused`
- `deployment.unpaused`
- `deployment.updated`
- `deployment_run.failed`
- `deployment_run.started`
- `deployment_run.succeeded`
- `environment.archived`
- `environment.created`
- `environment.deleted`
- `environment.updated`
- `memory_store.archived`
- `memory_store.created`
- `memory_store.deleted`
- `session.archived`
- `session.created`
- `session.deleted`
- `session.idled`
- `session.outcome_evaluation_ended`
- `session.pending`
- `session.requires_action`
- `session.running`
- `session.status_idled`
- `session.status_rescheduled`
- `session.status_run_started`
- `session.status_terminated`
- `session.thread_created`
- `session.thread_idled`
- `session.thread_terminated`
- `session.updated`
- `vault.archived`
- `vault.created`
- `vault.deleted`
- `vault_credential.archived`
- `vault_credential.created`
- `vault_credential.deleted`
- `vault_credential.refresh_failed`
