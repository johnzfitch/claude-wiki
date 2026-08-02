---
title: "Unpause Deployment - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/deployments/unpause"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:38:13Z"
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


Create Deployment


List Deployments


Get Deployment


Update Deployment


Archive Deployment


Run Deployment Now


Pause Deployment


Unpause Deployment

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

Unpause




cURL

# Unpause Deployment

POST/v1/deployments/{deployment_id}/unpause

Unpause Deployment

##### Path ParametersExpand Collapse 

deployment_id: string



[](#unpause.deployment_id)

##### Header ParametersExpand Collapse 



"anthropic-beta": optional array of [AnthropicBeta](/docs/en/api/beta#anthropic_beta)



Optional header to specify the beta version(s) you want to use.

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

[](#unpause.betas)

##### ReturnsExpand Collapse 



BetaManagedAgentsDeployment object { id, agent, archived_at, 13 more }



A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

id: string



Unique identifier for this deployment.

[](#beta_managed_agents_deployment.id)



agent: [BetaManagedAgentsAgentReference](/docs/en/api/beta/agents#beta_managed_agents_agent_reference) { id, type, version }



A resolved agent reference with a concrete version.

id: string



[](#beta_managed_agents_deployment.agent%20%2B%20(resource)%20beta.agents.id)

type: "agent"



[](#beta_managed_agents_deployment.agent%20%2B%20(resource)%20beta.agents.type)

version: number



[](#beta_managed_agents_deployment.agent%20%2B%20(resource)%20beta.agents.version)

[](#beta_managed_agents_deployment.agent)

archived_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_deployment.archived_at)

created_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_deployment.created_at)

description: string



Description of what the deployment does.

[](#beta_managed_agents_deployment.description)

environment_id: string



ID of the `environment` where sessions run.

[](#beta_managed_agents_deployment.environment_id)



initial_events: array of [BetaManagedAgentsDeploymentInitialEvent](/docs/en/api/beta/deployments#beta_managed_agents_deployment_initial_event)



Events sent to each session immediately after creation.

One of the following:



BetaManagedAgentsDeploymentUserMessageEvent object { content, type }



A user message sent to the session.



content: array of [BetaManagedAgentsTextBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_text_block) { text, type } or [BetaManagedAgentsImageBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_image_block) { source, type } or [BetaManagedAgentsDocumentBlock](/docs/en/api/beta/sessions/events#beta_managed_agents_document_block) { source, type, context, title }



Array of content blocks for the user message.

One of the following:



BetaManagedAgentsTextBlock object { text, type }



Regular text content.

text: string



The text content.

[](#beta_managed_agents_text_block.text)

type: "text"



[](#beta_managed_agents_text_block.type)

[](#beta_managed_agents_text_block)



BetaManagedAgentsImageBlock object { source, type }



Image content specified directly as base64 data or as a reference via a URL.



source: [BetaManagedAgentsBase64ImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_base64_image_source) { data, media_type, type } or [BetaManagedAgentsURLImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_url_image_source) { type, url } or [BetaManagedAgentsFileImageSource](/docs/en/api/beta/sessions/events#beta_managed_agents_file_image_source) { file_id, type }



Union type for image source variants.

One of the following:



BetaManagedAgentsBase64ImageSource object { data, media_type, type }



Base64-encoded image data.

data: string



Base64-encoded image data.

[](#beta_managed_agents_base64_image_source.data)

media_type: string



MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

[](#beta_managed_agents_base64_image_source.media_type)

type: "base64"



[](#beta_managed_agents_base64_image_source.type)

[](#beta_managed_agents_base64_image_source)



BetaManagedAgentsURLImageSource object { type, url }



Image referenced by URL.

type: "url"



[](#beta_managed_agents_url_image_source.type)

url: string



URL of the image to fetch.

[](#beta_managed_agents_url_image_source.url)

[](#beta_managed_agents_url_image_source)



BetaManagedAgentsFileImageSource object { file_id, type }



Image referenced by file ID.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_image_source.file_id)

type: "file"



[](#beta_managed_agents_file_image_source.type)

[](#beta_managed_agents_file_image_source)

[](#beta_managed_agents_image_block.source)

type: "image"



[](#beta_managed_agents_image_block.type)

[](#beta_managed_agents_image_block)



BetaManagedAgentsDocumentBlock object { source, type, context, title }



Document content, either specified directly as base64 data, as text, or as a reference via a URL.



source: [BetaManagedAgentsBase64DocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_base64_document_source) { data, media_type, type } or [BetaManagedAgentsPlainTextDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_plain_text_document_source) { data, media_type, type } or [BetaManagedAgentsURLDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_url_document_source) { type, url } or [BetaManagedAgentsFileDocumentSource](/docs/en/api/beta/sessions/events#beta_managed_agents_file_document_source) { file_id, type }



Union type for document source variants.

One of the following:



BetaManagedAgentsBase64DocumentSource object { data, media_type, type }



Base64-encoded document data.

data: string



Base64-encoded document data.

[](#beta_managed_agents_base64_document_source.data)

media_type: string



MIME type of the document (e.g., "application/pdf").

[](#beta_managed_agents_base64_document_source.media_type)

type: "base64"



[](#beta_managed_agents_base64_document_source.type)

[](#beta_managed_agents_base64_document_source)



BetaManagedAgentsPlainTextDocumentSource object { data, media_type, type }



Plain text document content.

data: string



The plain text content.

[](#beta_managed_agents_plain_text_document_source.data)

media_type: "text/plain"



MIME type of the text content. Must be "text/plain".

[](#beta_managed_agents_plain_text_document_source.media_type)

type: "text"



[](#beta_managed_agents_plain_text_document_source.type)

[](#beta_managed_agents_plain_text_document_source)



BetaManagedAgentsURLDocumentSource object { type, url }



Document referenced by URL.

type: "url"



[](#beta_managed_agents_url_document_source.type)

url: string



URL of the document to fetch.

[](#beta_managed_agents_url_document_source.url)

[](#beta_managed_agents_url_document_source)



BetaManagedAgentsFileDocumentSource object { file_id, type }



Document referenced by file ID.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_document_source.file_id)

type: "file"



[](#beta_managed_agents_file_document_source.type)

[](#beta_managed_agents_file_document_source)

[](#beta_managed_agents_document_block.source)

type: "document"



[](#beta_managed_agents_document_block.type)

context: optional string



Additional context about the document for the model.

[](#beta_managed_agents_document_block.context)

title: optional string



The title of the document.

[](#beta_managed_agents_document_block.title)

[](#beta_managed_agents_document_block)

[](#beta_managed_agents_deployment_user_message_event.content)

type: "user.message"



[](#beta_managed_agents_deployment_user_message_event.type)

[](#beta_managed_agents_deployment_user_message_event)



BetaManagedAgentsDeploymentUserDefineOutcomeEvent object { description, rubric, type, max_iterations }



An outcome the agent should work toward. The agent begins work on receipt.

description: string



What the agent should produce. This is the task specification.

[](#beta_managed_agents_deployment_user_define_outcome_event.description)



rubric: [BetaManagedAgentsFileRubric](/docs/en/api/beta/sessions/events#beta_managed_agents_file_rubric) { file_id, type } or [BetaManagedAgentsTextRubric](/docs/en/api/beta/sessions/events#beta_managed_agents_text_rubric) { content, type }



Rubric for grading the quality of an outcome.

One of the following:



BetaManagedAgentsFileRubric object { file_id, type }



Rubric referenced by a file uploaded via the Files API.

file_id: string



ID of the rubric file.

[](#beta_managed_agents_file_rubric.file_id)

type: "file"



[](#beta_managed_agents_file_rubric.type)

[](#beta_managed_agents_file_rubric)



BetaManagedAgentsTextRubric object { content, type }



Rubric content provided inline as text.

content: string



Rubric content. Plain text or markdown — the grader treats it as freeform text.

[](#beta_managed_agents_text_rubric.content)

type: "text"



[](#beta_managed_agents_text_rubric.type)

[](#beta_managed_agents_text_rubric)

[](#beta_managed_agents_deployment_user_define_outcome_event.rubric)

type: "user.define_outcome"



[](#beta_managed_agents_deployment_user_define_outcome_event.type)

max_iterations: optional number



Eval→revision cycles before giving up. Default 3, max 20.

[](#beta_managed_agents_deployment_user_define_outcome_event.max_iterations)

[](#beta_managed_agents_deployment_user_define_outcome_event)



BetaManagedAgentsDeploymentSystemMessageEvent object { content, type }



Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.



content: array of [BetaManagedAgentsSystemContentBlock](/docs/en/api/beta/sessions#beta_managed_agents_system_content_block) { text, type }



System content blocks to append. Text-only.

text: string



The text content.

[](#beta_managed_agents_system_content_block.text)

type: "text"



[](#beta_managed_agents_system_content_block.type)

[](#beta_managed_agents_deployment_system_message_event.content)

type: "system.message"



[](#beta_managed_agents_deployment_system_message_event.type)

[](#beta_managed_agents_deployment_system_message_event)

[](#beta_managed_agents_deployment.initial_events)

metadata: map\[string\]



Arbitrary key-value metadata. Maximum 16 pairs.

[](#beta_managed_agents_deployment.metadata)

name: string



Human-readable name.

[](#beta_managed_agents_deployment.name)



paused_reason: [BetaManagedAgentsDeploymentPausedReason](/docs/en/api/beta/deployments#beta_managed_agents_deployment_paused_reason)



Why a deployment is paused. Non-null exactly when `status` is `paused`.

One of the following:



BetaManagedAgentsManualDeploymentPausedReason object { type }



The caller invoked the pause endpoint on the deployment.

type: "manual"



[](#beta_managed_agents_deployment.paused_reason%20%2B%20(resource)%20beta.deployments.type)

[](#beta_managed_agents_deployment.paused_reason%20%2B%20(resource)%20beta.deployments)



BetaManagedAgentsErrorDeploymentPausedReason object { error, type }



A scheduled fire recorded a failed run whose error auto-pauses the deployment.



error: [BetaManagedAgentsDeploymentPausedReasonError](/docs/en/api/beta/deployments#beta_managed_agents_deployment_paused_reason_error)



The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:



BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type }



The deployment's environment was archived.

type: "environment_archived_error"



[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments.type)

[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments)



BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type }



The deployment's agent was archived.

type: "agent_archived_error"



[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments.type)

[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments)



BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type }



The deployment's environment no longer exists.

type: "environment_not_found_error"



[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments.type)

[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments)



BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type }



A vault referenced by the deployment no longer exists.

type: "vault_not_found_error"



[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments.type)

[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments)



BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type }



A file resource referenced by the deployment no longer exists.

type: "file_not_found_error"



[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments.type)

[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments)



BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type }



A referenced resource no longer exists and its kind was not reported.

type: "session_resource_not_found_error"



[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments.type)

[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments)



BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type }



The deployment's workspace was archived.

type: "workspace_archived_error"



[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments.type)

[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments)



BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type }



The deployment's organization is disabled.

type: "organization_disabled_error"



[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments.type)

[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments)



BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type }



A memory store referenced by the deployment is archived.

type: "memory_store_archived_error"



[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments.type)

[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments)



BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type }



A skill referenced by the deployment's agent no longer exists.

type: "skill_not_found_error"



[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments.type)

[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments)



BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type }



A vault referenced by the deployment is archived.

type: "vault_archived_error"



[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments.type)

[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments)



BetaManagedAgentsUnknownDeploymentPausedReasonError object { type }



An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

type: "unknown_error"



[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments.type)

[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments)



BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type }



The deployment configures resources, but its environment is self-hosted and cannot mount them.

type: "self_hosted_resources_unsupported_error"



[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments.type)

[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments)



BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type }



An MCP server host used by the deployment's agent is blocked by the environment's network policy.

type: "mcp_egress_blocked_error"



[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments.type)

[](#beta_managed_agents_error_deployment_paused_reason.error%20%2B%20(resource)%20beta.deployments)

[](#beta_managed_agents_deployment.paused_reason%20%2B%20(resource)%20beta.deployments.error)

type: "error"



[](#beta_managed_agents_deployment.paused_reason%20%2B%20(resource)%20beta.deployments.type)

[](#beta_managed_agents_deployment.paused_reason%20%2B%20(resource)%20beta.deployments)

[](#beta_managed_agents_deployment.paused_reason)



resources: array of [BetaManagedAgentsSessionResourceConfig](/docs/en/api/beta/deployments#beta_managed_agents_session_resource_config)



Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

One of the following:



BetaManagedAgentsGitHubRepositoryResourceConfig object { type, url, checkout, mount_path }



A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

type: "github_repository"



[](#beta_managed_agents_github_repository_resource_config.type)

url: string



Github URL of the repository

[](#beta_managed_agents_github_repository_resource_config.url)



checkout: optional [BetaManagedAgentsBranchCheckout](/docs/en/api/beta/sessions#beta_managed_agents_branch_checkout) { name, type } or [BetaManagedAgentsCommitCheckout](/docs/en/api/beta/sessions#beta_managed_agents_commit_checkout) { sha, type }



Branch or commit to check out. Defaults to the repository's default branch.

One of the following:



BetaManagedAgentsBranchCheckout object { name, type }



name: string



Branch name to check out.

[](#beta_managed_agents_branch_checkout.name)

type: "branch"



[](#beta_managed_agents_branch_checkout.type)

[](#beta_managed_agents_branch_checkout)



BetaManagedAgentsCommitCheckout object { sha, type }



sha: string



Full commit SHA to check out.

[](#beta_managed_agents_commit_checkout.sha)

type: "commit"



[](#beta_managed_agents_commit_checkout.type)

[](#beta_managed_agents_commit_checkout)

[](#beta_managed_agents_github_repository_resource_config.checkout)

mount_path: optional string



Mount path in the container. Defaults to `/workspace/<repo-name>`.

[](#beta_managed_agents_github_repository_resource_config.mount_path)

[](#beta_managed_agents_github_repository_resource_config)



BetaManagedAgentsFileResourceConfig object { file_id, type, mount_path }



A file mounted into each session's container.

file_id: string



ID of a previously uploaded file.

[](#beta_managed_agents_file_resource_config.file_id)

type: "file"



[](#beta_managed_agents_file_resource_config.type)

mount_path: optional string



Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

[](#beta_managed_agents_file_resource_config.mount_path)

[](#beta_managed_agents_file_resource_config)



BetaManagedAgentsMemoryStoreResourceConfig object { memory_store_id, type, access, instructions }



A memory store attached to each session created from this deployment.

memory_store_id: string



The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

[](#beta_managed_agents_memory_store_resource_config.memory_store_id)

type: "memory_store"



[](#beta_managed_agents_memory_store_resource_config.type)



access: optional "read_write" or "read_only"



Access mode for an attached memory store.

One of the following:

"read_write"



[](#beta_managed_agents_memory_store_resource_config.access%5B0%5D)

"read_only"



[](#beta_managed_agents_memory_store_resource_config.access%5B1%5D)

[](#beta_managed_agents_memory_store_resource_config.access)

instructions: optional string



Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

[](#beta_managed_agents_memory_store_resource_config.instructions)

[](#beta_managed_agents_memory_store_resource_config)

[](#beta_managed_agents_deployment.resources)



schedule: [BetaManagedAgentsSchedule](/docs/en/api/beta/deployments#beta_managed_agents_schedule) { expression, timezone, type, 2 more }



5-field POSIX cron schedule with computed runtime timestamps.

expression: string



5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, \#, and ? - is not supported, nor are predefined shortcuts (@daily).

[](#beta_managed_agents_deployment.schedule%20%2B%20(resource)%20beta.deployments.expression)

timezone: string



IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

[](#beta_managed_agents_deployment.schedule%20%2B%20(resource)%20beta.deployments.timezone)

type: "cron"



[](#beta_managed_agents_deployment.schedule%20%2B%20(resource)%20beta.deployments.type)

last_run_at: optional string



A timestamp in RFC 3339 format

[](#beta_managed_agents_deployment.schedule%20%2B%20(resource)%20beta.deployments.last_run_at)

upcoming_runs_at: optional array of string



Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

[](#beta_managed_agents_deployment.schedule%20%2B%20(resource)%20beta.deployments.upcoming_runs_at)

[](#beta_managed_agents_deployment.schedule)



status: [BetaManagedAgentsDeploymentStatus](/docs/en/api/beta/deployments#beta_managed_agents_deployment_status)



Lifecycle status of a deployment.

One of the following:

"active"



[](#beta_managed_agents_deployment.status%20%2B%20(resource)%20beta.deployments%5B0%5D)

"paused"



[](#beta_managed_agents_deployment.status%20%2B%20(resource)%20beta.deployments%5B1%5D)

[](#beta_managed_agents_deployment.status)

type: "deployment"



[](#beta_managed_agents_deployment.type)

updated_at: string



A timestamp in RFC 3339 format

[](#beta_managed_agents_deployment.updated_at)

vault_ids: array of string



Vault IDs supplying stored credentials for sessions created from this deployment.

[](#beta_managed_agents_deployment.vault_ids)

[](#beta_managed_agents_deployment)

Unpause Deployment

cURL



```python
curl https://api.anthropic.com/v1/deployments/$DEPLOYMENT_ID/unpause \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ]
}
```

##### Returns Examples

Response 200



```python
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
