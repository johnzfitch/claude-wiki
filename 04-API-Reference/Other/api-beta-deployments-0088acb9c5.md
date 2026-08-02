---
title: "Deployments - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/deployments"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:39:49Z"
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

Deployments




cURL

# Deployments

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

##### ModelsExpand Collapse 



BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type }



The deployment's agent was archived.

type: "agent_archived_error"



[](#beta_managed_agents_agent_archived_deployment_paused_reason_error.type)

[](#beta_managed_agents_agent_archived_deployment_paused_reason_error)



BetaManagedAgentsCronSchedule object { expression, timezone, type, 2 more }



5-field POSIX cron schedule with computed runtime timestamps.

expression: string



5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, \#, and ? - is not supported, nor are predefined shortcuts (@daily).

[](#beta_managed_agents_cron_schedule.expression)

timezone: string



IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

[](#beta_managed_agents_cron_schedule.timezone)

type: "cron"



[](#beta_managed_agents_cron_schedule.type)

last_run_at: optional string



A timestamp in RFC 3339 format

[](#beta_managed_agents_cron_schedule.last_run_at)

upcoming_runs_at: optional array of string



Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

[](#beta_managed_agents_cron_schedule.upcoming_runs_at)

[](#beta_managed_agents_cron_schedule)



BetaManagedAgentsCronScheduleParams object { expression, timezone, type }



5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

expression: string



5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, \#, and ? - is not supported, nor are predefined shortcuts (@daily).

[](#beta_managed_agents_cron_schedule_params.expression)

timezone: string



Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

[](#beta_managed_agents_cron_schedule_params.timezone)

type: "cron"



[](#beta_managed_agents_cron_schedule_params.type)

[](#beta_managed_agents_cron_schedule_params)

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



BetaManagedAgentsDeploymentInitialEvent = [BetaManagedAgentsDeploymentUserMessageEvent](/docs/en/api/beta/deployments#beta_managed_agents_deployment_user_message_event) { content, type } or [BetaManagedAgentsDeploymentUserDefineOutcomeEvent](/docs/en/api/beta/deployments#beta_managed_agents_deployment_user_define_outcome_event) { description, rubric, type, max_iterations } or [BetaManagedAgentsDeploymentSystemMessageEvent](/docs/en/api/beta/deployments#beta_managed_agents_deployment_system_message_event) { content, type }



An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

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

[](#beta_managed_agents_deployment_initial_event)



BetaManagedAgentsDeploymentInitialEventParams = [BetaManagedAgentsUserMessageEventParams](/docs/en/api/beta/sessions/events#beta_managed_agents_user_message_event_params) { content, type } or [BetaManagedAgentsUserDefineOutcomeEventParams](/docs/en/api/beta/sessions/events#beta_managed_agents_user_define_outcome_event_params) { description, rubric, type, max_iterations } or [BetaManagedAgentsSystemMessageEventParams](/docs/en/api/beta/sessions/events#beta_managed_agents_system_message_event_params) { content, type }



An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

One of the following:



BetaManagedAgentsUserMessageEventParams object { content, type }



Parameters for sending a user message to the session.

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

[](#beta_managed_agents_user_message_event_params.content)

type: "user.message"



[](#beta_managed_agents_user_message_event_params.type)

[](#beta_managed_agents_user_message_event_params)



BetaManagedAgentsUserDefineOutcomeEventParams object { description, rubric, type, max_iterations }



Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

description: string



What the agent should produce. This is the task specification.

[](#beta_managed_agents_user_define_outcome_event_params.description)



rubric: [BetaManagedAgentsFileRubricParams](/docs/en/api/beta/sessions/events#beta_managed_agents_file_rubric_params) { file_id, type } or [BetaManagedAgentsTextRubricParams](/docs/en/api/beta/sessions/events#beta_managed_agents_text_rubric_params) { content, type }



Rubric for grading the quality of an outcome.

One of the following:



BetaManagedAgentsFileRubricParams object { file_id, type }



Rubric referenced by a file uploaded via the Files API.

file_id: string



ID of the rubric file.

[](#beta_managed_agents_file_rubric_params.file_id)

type: "file"



[](#beta_managed_agents_file_rubric_params.type)

[](#beta_managed_agents_file_rubric_params)



BetaManagedAgentsTextRubricParams object { content, type }



Rubric content provided inline as text.

content: string



Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

[](#beta_managed_agents_text_rubric_params.content)

type: "text"



[](#beta_managed_agents_text_rubric_params.type)

[](#beta_managed_agents_text_rubric_params)

[](#beta_managed_agents_user_define_outcome_event_params.rubric)

type: "user.define_outcome"



[](#beta_managed_agents_user_define_outcome_event_params.type)

max_iterations: optional number



Eval→revision cycles before giving up. Default 3, max 20.

[](#beta_managed_agents_user_define_outcome_event_params.max_iterations)

[](#beta_managed_agents_user_define_outcome_event_params)



BetaManagedAgentsSystemMessageEventParams object { content, type }



Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

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

[](#beta_managed_agents_system_message_event_params.content)

type: "system.message"



[](#beta_managed_agents_system_message_event_params.type)

[](#beta_managed_agents_system_message_event_params)

[](#beta_managed_agents_deployment_initial_event_params)



BetaManagedAgentsDeploymentPausedReason = [BetaManagedAgentsManualDeploymentPausedReason](/docs/en/api/beta/deployments#beta_managed_agents_manual_deployment_paused_reason) { type } or [BetaManagedAgentsErrorDeploymentPausedReason](/docs/en/api/beta/deployments#beta_managed_agents_error_deployment_paused_reason) { error, type }



Why a deployment is paused. Non-null exactly when `status` is `paused`.

One of the following:



BetaManagedAgentsManualDeploymentPausedReason object { type }



The caller invoked the pause endpoint on the deployment.

type: "manual"



[](#beta_managed_agents_manual_deployment_paused_reason.type)

[](#beta_managed_agents_manual_deployment_paused_reason)

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

[](#beta_managed_agents_error_deployment_paused_reason.error)

type: "error"



[](#beta_managed_agents_error_deployment_paused_reason.type)

[](#beta_managed_agents_error_deployment_paused_reason)

[](#beta_managed_agents_deployment_paused_reason)



BetaManagedAgentsDeploymentPausedReasonError = [BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError](/docs/en/api/beta/deployments#beta_managed_agents_environment_archived_deployment_paused_reason_error) { type } or [BetaManagedAgentsAgentArchivedDeploymentPausedReasonError](/docs/en/api/beta/deployments#beta_managed_agents_agent_archived_deployment_paused_reason_error) { type } or [BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError](/docs/en/api/beta/deployments#beta_managed_agents_environment_not_found_deployment_paused_reason_error) { type } or 11 more



The error that triggered an auto-pause. Matches the failed run's `error.type`.

One of the following:



BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type }



The deployment's environment was archived.

type: "environment_archived_error"



[](#beta_managed_agents_environment_archived_deployment_paused_reason_error.type)

[](#beta_managed_agents_environment_archived_deployment_paused_reason_error)



BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object { type }



The deployment's agent was archived.

type: "agent_archived_error"



[](#beta_managed_agents_agent_archived_deployment_paused_reason_error.type)

[](#beta_managed_agents_agent_archived_deployment_paused_reason_error)



BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type }



The deployment's environment no longer exists.

type: "environment_not_found_error"



[](#beta_managed_agents_environment_not_found_deployment_paused_reason_error.type)

[](#beta_managed_agents_environment_not_found_deployment_paused_reason_error)



BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type }



A vault referenced by the deployment no longer exists.

type: "vault_not_found_error"



[](#beta_managed_agents_vault_not_found_deployment_paused_reason_error.type)

[](#beta_managed_agents_vault_not_found_deployment_paused_reason_error)



BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type }



A file resource referenced by the deployment no longer exists.

type: "file_not_found_error"



[](#beta_managed_agents_file_not_found_deployment_paused_reason_error.type)

[](#beta_managed_agents_file_not_found_deployment_paused_reason_error)



BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type }



A referenced resource no longer exists and its kind was not reported.

type: "session_resource_not_found_error"



[](#beta_managed_agents_session_resource_not_found_deployment_paused_reason_error.type)

[](#beta_managed_agents_session_resource_not_found_deployment_paused_reason_error)



BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type }



The deployment's workspace was archived.

type: "workspace_archived_error"



[](#beta_managed_agents_workspace_archived_deployment_paused_reason_error.type)

[](#beta_managed_agents_workspace_archived_deployment_paused_reason_error)



BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type }



The deployment's organization is disabled.

type: "organization_disabled_error"



[](#beta_managed_agents_organization_disabled_deployment_paused_reason_error.type)

[](#beta_managed_agents_organization_disabled_deployment_paused_reason_error)



BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type }



A memory store referenced by the deployment is archived.

type: "memory_store_archived_error"



[](#beta_managed_agents_memory_store_archived_deployment_paused_reason_error.type)

[](#beta_managed_agents_memory_store_archived_deployment_paused_reason_error)



BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type }



A skill referenced by the deployment's agent no longer exists.

type: "skill_not_found_error"



[](#beta_managed_agents_skill_not_found_deployment_paused_reason_error.type)

[](#beta_managed_agents_skill_not_found_deployment_paused_reason_error)



BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type }



A vault referenced by the deployment is archived.

type: "vault_archived_error"



[](#beta_managed_agents_vault_archived_deployment_paused_reason_error.type)

[](#beta_managed_agents_vault_archived_deployment_paused_reason_error)



BetaManagedAgentsUnknownDeploymentPausedReasonError object { type }



An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

type: "unknown_error"



[](#beta_managed_agents_unknown_deployment_paused_reason_error.type)

[](#beta_managed_agents_unknown_deployment_paused_reason_error)



BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type }



The deployment configures resources, but its environment is self-hosted and cannot mount them.

type: "self_hosted_resources_unsupported_error"



[](#beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error.type)

[](#beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error)



BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type }



An MCP server host used by the deployment's agent is blocked by the environment's network policy.

type: "mcp_egress_blocked_error"



[](#beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error.type)

[](#beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error)

[](#beta_managed_agents_deployment_paused_reason_error)



BetaManagedAgentsDeploymentStatus = "active" or "paused"



Lifecycle status of a deployment.

One of the following:

"active"



[](#beta_managed_agents_deployment_status%5B0%5D)

"paused"



[](#beta_managed_agents_deployment_status%5B1%5D)

[](#beta_managed_agents_deployment_status)

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

BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object { type }



The deployment's environment was archived.

type: "environment_archived_error"



[](#beta_managed_agents_environment_archived_deployment_paused_reason_error.type)

[](#beta_managed_agents_environment_archived_deployment_paused_reason_error)



BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object { type }



The deployment's environment no longer exists.

type: "environment_not_found_error"



[](#beta_managed_agents_environment_not_found_deployment_paused_reason_error.type)

[](#beta_managed_agents_environment_not_found_deployment_paused_reason_error)

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

[](#beta_managed_agents_error_deployment_paused_reason.error)

type: "error"



[](#beta_managed_agents_error_deployment_paused_reason.type)

[](#beta_managed_agents_error_deployment_paused_reason)



BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object { type }



A file resource referenced by the deployment no longer exists.

type: "file_not_found_error"



[](#beta_managed_agents_file_not_found_deployment_paused_reason_error.type)

[](#beta_managed_agents_file_not_found_deployment_paused_reason_error)

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

BetaManagedAgentsManualDeploymentPausedReason object { type }



The caller invoked the pause endpoint on the deployment.

type: "manual"



[](#beta_managed_agents_manual_deployment_paused_reason.type)

[](#beta_managed_agents_manual_deployment_paused_reason)



BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object { type }



An MCP server host used by the deployment's agent is blocked by the environment's network policy.

type: "mcp_egress_blocked_error"



[](#beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error.type)

[](#beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error)



BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object { type }



A memory store referenced by the deployment is archived.

type: "memory_store_archived_error"



[](#beta_managed_agents_memory_store_archived_deployment_paused_reason_error.type)

[](#beta_managed_agents_memory_store_archived_deployment_paused_reason_error)

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



BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object { type }



The deployment's organization is disabled.

type: "organization_disabled_error"



[](#beta_managed_agents_organization_disabled_deployment_paused_reason_error.type)

[](#beta_managed_agents_organization_disabled_deployment_paused_reason_error)



BetaManagedAgentsSchedule object { expression, timezone, type, 2 more }



5-field POSIX cron schedule with computed runtime timestamps.

expression: string



5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, \#, and ? - is not supported, nor are predefined shortcuts (@daily).

[](#beta_managed_agents_schedule.expression)

timezone: string



IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

[](#beta_managed_agents_schedule.timezone)

type: "cron"



[](#beta_managed_agents_schedule.type)

last_run_at: optional string



A timestamp in RFC 3339 format

[](#beta_managed_agents_schedule.last_run_at)

upcoming_runs_at: optional array of string



Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

[](#beta_managed_agents_schedule.upcoming_runs_at)

[](#beta_managed_agents_schedule)



BetaManagedAgentsScheduleParams object { expression, timezone, type }



5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

expression: string



5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 \* \* 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, \#, and ? - is not supported, nor are predefined shortcuts (@daily).

[](#beta_managed_agents_schedule_params.expression)

timezone: string



Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

[](#beta_managed_agents_schedule_params.timezone)

type: "cron"



[](#beta_managed_agents_schedule_params.type)

[](#beta_managed_agents_schedule_params)



BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object { type }



The deployment configures resources, but its environment is self-hosted and cannot mount them.

type: "self_hosted_resources_unsupported_error"



[](#beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error.type)

[](#beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error)



BetaManagedAgentsSessionResourceConfig = [BetaManagedAgentsGitHubRepositoryResourceConfig](/docs/en/api/beta/deployments#beta_managed_agents_github_repository_resource_config) { type, url, checkout, mount_path } or [BetaManagedAgentsFileResourceConfig](/docs/en/api/beta/deployments#beta_managed_agents_file_resource_config) { file_id, type, mount_path } or [BetaManagedAgentsMemoryStoreResourceConfig](/docs/en/api/beta/deployments#beta_managed_agents_memory_store_resource_config) { memory_store_id, type, access, instructions }



A configured session resource. Echoes the input minus write-only credentials.

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

[](#beta_managed_agents_session_resource_config)



BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object { type }



A referenced resource no longer exists and its kind was not reported.

type: "session_resource_not_found_error"



[](#beta_managed_agents_session_resource_not_found_deployment_paused_reason_error.type)

[](#beta_managed_agents_session_resource_not_found_deployment_paused_reason_error)



BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object { type }



A skill referenced by the deployment's agent no longer exists.

type: "skill_not_found_error"



[](#beta_managed_agents_skill_not_found_deployment_paused_reason_error.type)

[](#beta_managed_agents_skill_not_found_deployment_paused_reason_error)



BetaManagedAgentsUnknownDeploymentPausedReasonError object { type }



An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

type: "unknown_error"



[](#beta_managed_agents_unknown_deployment_paused_reason_error.type)

[](#beta_managed_agents_unknown_deployment_paused_reason_error)



BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object { type }



A vault referenced by the deployment is archived.

type: "vault_archived_error"



[](#beta_managed_agents_vault_archived_deployment_paused_reason_error.type)

[](#beta_managed_agents_vault_archived_deployment_paused_reason_error)



BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object { type }



A vault referenced by the deployment no longer exists.

type: "vault_not_found_error"



[](#beta_managed_agents_vault_not_found_deployment_paused_reason_error.type)

[](#beta_managed_agents_vault_not_found_deployment_paused_reason_error)



BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object { type }



The deployment's workspace was archived.

type: "workspace_archived_error"



[](#beta_managed_agents_workspace_archived_deployment_paused_reason_error.type)

[](#beta_managed_agents_workspace_archived_deployment_paused_reason_error)
