---
title: "IAM actions for Claude Platform on AWS - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions"
category: "20-Models"
fetched_at: "2026-08-02T05:41:22Z"
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

IAM actions (Claude Platform on AWS)

API reference/Support & configuration

# IAM actions for Claude Platform on AWS




IAM action reference for controlling access to Claude Platform on AWS through AWS policies.




Claude Platform on AWS uses AWS IAM for access control. Every API route maps to an IAM action in the `aws-external-anthropic` namespace. This page lists all actions, the routes each action authorizes, and the managed policies available for common access patterns. For platform setup and authentication, see [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws).




Service details

| Attribute              | Value                    |
|------------------------|--------------------------|
| **IAM service prefix** | `aws-external-anthropic` |
| **Resource types**     | `workspace`              |

Workspace ARN format:

``` block
arn:aws:aws-external-anthropic:{region}:{account-id}:workspace/{workspace-id}
```



The ARN region is always populated and matches the region the workspace is bound to. The resource segment is the tagged workspace ID (`wrkspc_...`), the same value you pass in the `anthropic-workspace-id` header.




Actions

The service defines 65 actions. Actions follow the AWS `VerbNoun` convention and use verb discipline so that `Get*` and `List*` wildcards produce a clean read-only boundary.




Inference

| Action            | Routes authorized                |
|-------------------|----------------------------------|
| `CreateInference` | `POST /v1/messages`              |
| `CountTokens`     | `POST /v1/messages/count_tokens` |




Batch processing

[TABLE]



`GetBatchInference` authorizes both reading batch metadata and downloading batch results. The `AnthropicReadOnlyAccess`, `AnthropicInferenceAccess`, and `AnthropicLimitedAccess` policies' `Get*` wildcards include this action.




Models

| Action       | Routes authorized     |
|--------------|-----------------------|
| `GetModel`   | `GET /v1/models/{id}` |
| `ListModels` | `GET /v1/models`      |




Files

[TABLE]



`GetFile` authorizes both metadata and content download. A principal with read-only access can download file bytes, not just list files.




Skills

[TABLE]



`GetSkill` authorizes both skill metadata and skill-content download. A principal with read-only access can download skill bytes, not just list skills.



Creating or deleting an individual skill version maps to `UpdateSkill`, not `CreateSkill` or `DeleteSkill`. A policy that denies `aws-external-anthropic:Delete*` still allows version deletion, and a policy that denies `aws-external-anthropic:Create*` still allows version creation. Deny `UpdateSkill` and `CreateSkill` as well if you need to prevent any skill mutation.




Agents

[TABLE]



Agents support only archive, not hard delete. A policy that denies `aws-external-anthropic:Delete*` does not block `ArchiveAgent`. Deny `ArchiveAgent`, `UpdateAgent`, and `CreateAgent` if you need to prevent any agent mutation.




Sessions

[TABLE]



`GetSession` authorizes reading session metadata, the full event stream (conversation history), and session resources. The `AnthropicReadOnlyAccess`, `AnthropicInferenceAccess`, and `AnthropicLimitedAccess` policies' `Get*` wildcards include this action.



Creating, updating, or deleting an individual session sub-resource (events or session resources) maps to `UpdateSession`, not `CreateSession` or `DeleteSession`. A policy that denies `aws-external-anthropic:Delete*` still allows sub-resource deletion, and a policy that denies `aws-external-anthropic:Create*` still allows sub-resource creation. Deny `UpdateSession`, `CreateSession`, and `ArchiveSession` as well if you need to prevent any session mutation.




Environments

[TABLE]



A policy that denies `aws-external-anthropic:Delete*` does not block `ArchiveEnvironment`. `ProcessEnvironmentWork` is not matched by `Create*`, `Update*`, `Delete*`, or `Archive*` wildcards. Deny `ArchiveEnvironment`, `UpdateEnvironment`, `CreateEnvironment`, and `ProcessEnvironmentWork` as well if you need to prevent any environment mutation.



`ProcessEnvironmentWork` authorizes a [self-hosted sandbox](/docs/en/managed-agents/self-hosted-sandboxes) worker to poll for, acknowledge, heartbeat, stop, and post results on environment work items. Grant it only to principals that run self-hosted environment workers. The `AnthropicSelfHostedEnvironmentAccess` managed policy includes this action.




Vaults

[TABLE]



Creating, updating, archiving, or deleting an individual vault credential maps to `UpdateVault`. Reading a credential maps to `GetVault`. Vault credential secrets are not exposed: secret fields are write-only and are never returned by `GetVault` (see [Authenticate with vaults](/docs/en/managed-agents/vaults)). A policy that denies `aws-external-anthropic:Delete*` still allows credential deletion, and a policy that denies `aws-external-anthropic:Create*` still allows credential creation. Deny `UpdateVault`, `CreateVault`, and `ArchiveVault` as well if you need to prevent any vault mutation.




Memory stores

[TABLE]



`GetMemoryStore` authorizes reading store metadata, all memories, and memory version history. The `AnthropicReadOnlyAccess`, `AnthropicInferenceAccess`, and `AnthropicLimitedAccess` policies' `Get*` wildcards include this action.



Creating, updating, or deleting an individual memory and redacting a memory version both map to `UpdateMemoryStore`, not `CreateMemoryStore` or `DeleteMemoryStore`. A policy that denies `aws-external-anthropic:Delete*` still allows individual-memory deletion and memory-version redaction, and a policy that denies `aws-external-anthropic:Create*` still allows individual-memory creation. Deny `UpdateMemoryStore`, `CreateMemoryStore`, and `ArchiveMemoryStore` as well if you need to prevent any memory-store mutation.




Webhooks

| Action                | Routes authorized                                  |
|-----------------------|----------------------------------------------------|
| `CreateWebhook`       | `POST /v1/webhooks`                                |
| `GetWebhook`          | `GET /v1/webhooks/{id}`                            |
| `ListWebhooks`        | `GET /v1/webhooks`                                 |
| `UpdateWebhook`       | `POST /v1/webhooks/{id}`                           |
| `DeleteWebhook`       | `DELETE /v1/webhooks/{id}`                         |
| `RotateWebhookSecret` | `POST /v1/webhooks/{id}/regenerate_signing_secret` |



Webhook signing secrets are write-only. `GetWebhook` returns webhook metadata only; it does not return the signing secret.



`RotateWebhookSecret` is not matched by `aws-external-anthropic:Create*`, `Update*`, or `Delete*` wildcards. A policy that denies those patterns still allows secret rotation. Deny `RotateWebhookSecret`, `UpdateWebhook`, `CreateWebhook`, and `DeleteWebhook` if you need to prevent any webhook mutation.




User profiles

| Action              | Routes authorized             |
|---------------------|-------------------------------|
| `CreateUserProfile` | `POST /v1/user_profiles`      |
| `GetUserProfile`    | `GET /v1/user_profiles/{id}`  |
| `ListUserProfiles`  | `GET /v1/user_profiles`       |
| `UpdateUserProfile` | `POST /v1/user_profiles/{id}` |



IAM action matching is case-insensitive. The wildcard `aws-external-anthropic:*File` matches `CreateFile`, `GetFile`, and `DeleteFile`, but does not match `ListFiles` (which ends in "files", not "file"). It also over-matches `CreateUserProfile`, `GetUserProfile`, and `UpdateUserProfile` because "Profile" ends in "file". If you intend to grant or deny only Files API actions, enumerate them explicitly (`CreateFile`, `GetFile`, `ListFiles`, `DeleteFile`) rather than using a `*File` suffix pattern.




Workspaces

| Action             | Routes authorized                                |
|--------------------|--------------------------------------------------|
| `CreateWorkspace`  | `POST /v1/organizations/workspaces`              |
| `GetWorkspace`     | `GET /v1/organizations/workspaces/{id}`          |
| `ListWorkspaces`   | `GET /v1/organizations/workspaces`               |
| `UpdateWorkspace`  | `POST /v1/organizations/workspaces/{id}`         |
| `ArchiveWorkspace` | `POST /v1/organizations/workspaces/{id}/archive` |



Workspaces support only archive, not hard delete. A policy that denies `aws-external-anthropic:Delete*` does not block `ArchiveWorkspace`. Deny `ArchiveWorkspace`, `UpdateWorkspace`, and `CreateWorkspace` if you need to prevent any workspace mutation.




Authentication

| Action                | Routes authorized |
|-----------------------|-------------------|
| `CallWithBearerToken` | (none)            |

`CallWithBearerToken` is an authentication-layer permission that authorizes a principal to authenticate through an API key (bearer token) rather than AWS SigV4. It does not map to a route. Grant it alongside the route-mapped actions you want the API key holder to perform.




Console access

| Action          | Routes authorized |
|-----------------|-------------------|
| `AssumeConsole` | (none)            |

`AssumeConsole` authorizes a principal to open the Claude Console for a Claude Platform on AWS workspace through the AWS Console federation flow. It does not map to a route. Grant it to principals who should be able to click **Open Claude Console** on the Claude Platform on AWS service page in the AWS Console. The Claude Console role (Admin or Developer) is assigned separately by your Anthropic account representative; it is not derived from the principal's IAM permissions. See [Using the Claude Console](/docs/en/build-with-claude/claude-platform-on-aws#using-the-claude-console) for the sign-in flow and role descriptions.




Route-to-action mapping

The following table lists every route on Claude Platform on AWS and the IAM action required to call it. Each IAM action also authorizes requests that use the `anthropic-beta` header; beta variants of a route do not require a separate IAM action. CloudTrail classifies each action as either a Data event (high-volume, data-plane operations) or a Management event (control-plane operations). Vault and webhook actions are classified as Management events because they hold secrets (vault credentials and webhook signing secrets) and benefit from default-on audit logging. Workspace actions are also classified as Management events because they are organization-scoped control-plane operations. All other actions, including inference, batch, model, file, skill, user profile, and the remaining Claude Managed Agents actions, are classified as Data events.

| Method   | Route                                                | IAM action               | CloudTrail event type |
|----------|------------------------------------------------------|--------------------------|-----------------------|
| `POST`   | `/v1/messages`                                       | `CreateInference`        | Data                  |
| `POST`   | `/v1/messages/count_tokens`                          | `CountTokens`            | Data                  |
| `POST`   | `/v1/messages/batches`                               | `CreateBatchInference`   | Data                  |
| `GET`    | `/v1/messages/batches`                               | `ListBatchInferences`    | Data                  |
| `GET`    | `/v1/messages/batches/{id}`                          | `GetBatchInference`      | Data                  |
| `GET`    | `/v1/messages/batches/{id}/results`                  | `GetBatchInference`      | Data                  |
| `POST`   | `/v1/messages/batches/{id}/cancel`                   | `CancelBatchInference`   | Data                  |
| `DELETE` | `/v1/messages/batches/{id}`                          | `DeleteBatchInference`   | Data                  |
| `GET`    | `/v1/models`                                         | `ListModels`             | Data                  |
| `GET`    | `/v1/models/{id}`                                    | `GetModel`               | Data                  |
| `POST`   | `/v1/files`                                          | `CreateFile`             | Data                  |
| `GET`    | `/v1/files`                                          | `ListFiles`              | Data                  |
| `GET`    | `/v1/files/{id}`                                     | `GetFile`                | Data                  |
| `GET`    | `/v1/files/{id}/content`                             | `GetFile`                | Data                  |
| `DELETE` | `/v1/files/{id}`                                     | `DeleteFile`             | Data                  |
| `POST`   | `/v1/skills`                                         | `CreateSkill`            | Data                  |
| `GET`    | `/v1/skills`                                         | `ListSkills`             | Data                  |
| `GET`    | `/v1/skills/{id}`                                    | `GetSkill`               | Data                  |
| `DELETE` | `/v1/skills/{id}`                                    | `DeleteSkill`            | Data                  |
| `POST`   | `/v1/skills/{id}/versions`                           | `UpdateSkill`            | Data                  |
| `GET`    | `/v1/skills/{id}/versions`                           | `GetSkill`               | Data                  |
| `GET`    | `/v1/skills/{id}/versions/{version}`                 | `GetSkill`               | Data                  |
| `GET`    | `/v1/skills/{id}/versions/{version}/content`         | `GetSkill`               | Data                  |
| `DELETE` | `/v1/skills/{id}/versions/{version}`                 | `UpdateSkill`            | Data                  |
| `POST`   | `/v1/user_profiles`                                  | `CreateUserProfile`      | Data                  |
| `GET`    | `/v1/user_profiles`                                  | `ListUserProfiles`       | Data                  |
| `GET`    | `/v1/user_profiles/{id}`                             | `GetUserProfile`         | Data                  |
| `POST`   | `/v1/user_profiles/{id}`                             | `UpdateUserProfile`      | Data                  |
| `POST`   | `/v1/organizations/workspaces`                       | `CreateWorkspace`        | Management            |
| `GET`    | `/v1/organizations/workspaces`                       | `ListWorkspaces`         | Management            |
| `GET`    | `/v1/organizations/workspaces/{id}`                  | `GetWorkspace`           | Management            |
| `POST`   | `/v1/organizations/workspaces/{id}`                  | `UpdateWorkspace`        | Management            |
| `POST`   | `/v1/organizations/workspaces/{id}/archive`          | `ArchiveWorkspace`       | Management            |
| `POST`   | `/v1/agents`                                         | `CreateAgent`            | Data                  |
| `GET`    | `/v1/agents`                                         | `ListAgents`             | Data                  |
| `GET`    | `/v1/agents/{id}`                                    | `GetAgent`               | Data                  |
| `POST`   | `/v1/agents/{id}`                                    | `UpdateAgent`            | Data                  |
| `POST`   | `/v1/agents/{id}/archive`                            | `ArchiveAgent`           | Data                  |
| `GET`    | `/v1/agents/{id}/versions`                           | `GetAgent`               | Data                  |
| `POST`   | `/v1/sessions`                                       | `CreateSession`          | Data                  |
| `GET`    | `/v1/sessions`                                       | `ListSessions`           | Data                  |
| `GET`    | `/v1/sessions/{id}`                                  | `GetSession`             | Data                  |
| `POST`   | `/v1/sessions/{id}`                                  | `UpdateSession`          | Data                  |
| `POST`   | `/v1/sessions/{id}/archive`                          | `ArchiveSession`         | Data                  |
| `DELETE` | `/v1/sessions/{id}`                                  | `DeleteSession`          | Data                  |
| `GET`    | `/v1/sessions/{id}/events`                           | `GetSession`             | Data                  |
| `POST`   | `/v1/sessions/{id}/events`                           | `UpdateSession`          | Data                  |
| `GET`    | `/v1/sessions/{id}/events/stream`                    | `GetSession`             | Data                  |
| `GET`    | `/v1/sessions/{id}/resources`                        | `GetSession`             | Data                  |
| `GET`    | `/v1/sessions/{id}/resources/{id}`                   | `GetSession`             | Data                  |
| `POST`   | `/v1/sessions/{id}/resources`                        | `UpdateSession`          | Data                  |
| `POST`   | `/v1/sessions/{id}/resources/{id}`                   | `UpdateSession`          | Data                  |
| `DELETE` | `/v1/sessions/{id}/resources/{id}`                   | `UpdateSession`          | Data                  |
| `POST`   | `/v1/environments`                                   | `CreateEnvironment`      | Data                  |
| `GET`    | `/v1/environments`                                   | `ListEnvironments`       | Data                  |
| `GET`    | `/v1/environments/{id}`                              | `GetEnvironment`         | Data                  |
| `POST`   | `/v1/environments/{id}`                              | `UpdateEnvironment`      | Data                  |
| `POST`   | `/v1/environments/{id}/archive`                      | `ArchiveEnvironment`     | Data                  |
| `DELETE` | `/v1/environments/{id}`                              | `DeleteEnvironment`      | Data                  |
| `GET`    | `/v1/environments/{id}/work`                         | `GetEnvironment`         | Data                  |
| `GET`    | `/v1/environments/{id}/work/poll`                    | `ProcessEnvironmentWork` | Data                  |
| `GET`    | `/v1/environments/{id}/work/{work_id}`               | `GetEnvironment`         | Data                  |
| `GET`    | `/v1/environments/{id}/work/stats`                   | `GetEnvironment`         | Data                  |
| `POST`   | `/v1/environments/{id}/work/{work_id}`               | `ProcessEnvironmentWork` | Data                  |
| `POST`   | `/v1/environments/{id}/work/{work_id}/ack`           | `ProcessEnvironmentWork` | Data                  |
| `POST`   | `/v1/environments/{id}/work/{work_id}/heartbeat`     | `ProcessEnvironmentWork` | Data                  |
| `POST`   | `/v1/environments/{id}/work/{work_id}/stop`          | `ProcessEnvironmentWork` | Data                  |
| `POST`   | `/v1/vaults`                                         | `CreateVault`            | Management            |
| `GET`    | `/v1/vaults`                                         | `ListVaults`             | Management            |
| `GET`    | `/v1/vaults/{id}`                                    | `GetVault`               | Management            |
| `POST`   | `/v1/vaults/{id}`                                    | `UpdateVault`            | Management            |
| `POST`   | `/v1/vaults/{id}/archive`                            | `ArchiveVault`           | Management            |
| `DELETE` | `/v1/vaults/{id}`                                    | `DeleteVault`            | Management            |
| `GET`    | `/v1/vaults/{id}/credentials`                        | `GetVault`               | Management            |
| `POST`   | `/v1/vaults/{id}/credentials`                        | `UpdateVault`            | Management            |
| `GET`    | `/v1/vaults/{id}/credentials/{id}`                   | `GetVault`               | Management            |
| `POST`   | `/v1/vaults/{id}/credentials/{id}`                   | `UpdateVault`            | Management            |
| `POST`   | `/v1/vaults/{id}/credentials/{id}/archive`           | `UpdateVault`            | Management            |
| `DELETE` | `/v1/vaults/{id}/credentials/{id}`                   | `UpdateVault`            | Management            |
| `POST`   | `/v1/memory_stores`                                  | `CreateMemoryStore`      | Data                  |
| `GET`    | `/v1/memory_stores`                                  | `ListMemoryStores`       | Data                  |
| `GET`    | `/v1/memory_stores/{id}`                             | `GetMemoryStore`         | Data                  |
| `POST`   | `/v1/memory_stores/{id}`                             | `UpdateMemoryStore`      | Data                  |
| `POST`   | `/v1/memory_stores/{id}/archive`                     | `ArchiveMemoryStore`     | Data                  |
| `DELETE` | `/v1/memory_stores/{id}`                             | `DeleteMemoryStore`      | Data                  |
| `POST`   | `/v1/memory_stores/{id}/memories`                    | `UpdateMemoryStore`      | Data                  |
| `GET`    | `/v1/memory_stores/{id}/memories`                    | `GetMemoryStore`         | Data                  |
| `GET`    | `/v1/memory_stores/{id}/memories/{id}`               | `GetMemoryStore`         | Data                  |
| `POST`   | `/v1/memory_stores/{id}/memories/{id}`               | `UpdateMemoryStore`      | Data                  |
| `DELETE` | `/v1/memory_stores/{id}/memories/{id}`               | `UpdateMemoryStore`      | Data                  |
| `GET`    | `/v1/memory_stores/{id}/memory_versions`             | `GetMemoryStore`         | Data                  |
| `GET`    | `/v1/memory_stores/{id}/memory_versions/{id}`        | `GetMemoryStore`         | Data                  |
| `POST`   | `/v1/memory_stores/{id}/memory_versions/{id}/redact` | `UpdateMemoryStore`      | Data                  |
| `GET`    | `/v1/webhooks`                                       | `ListWebhooks`           | Management            |
| `GET`    | `/v1/webhooks/{id}`                                  | `GetWebhook`             | Management            |
| `POST`   | `/v1/webhooks`                                       | `CreateWebhook`          | Management            |
| `POST`   | `/v1/webhooks/{id}`                                  | `UpdateWebhook`          | Management            |
| `DELETE` | `/v1/webhooks/{id}`                                  | `DeleteWebhook`          | Management            |
| `POST`   | `/v1/webhooks/{id}/regenerate_signing_secret`        | `RotateWebhookSecret`    | Management            |

Routes not in this table are not available on Claude Platform on AWS. The gateway denies any route not listed here by default.



Workspace routes are the only Admin API routes available on Claude Platform on AWS. The Claude Console Workspaces page is read-only; use the Admin API or the AWS Console to create, update, or archive workspaces.




Managed policies

AWS provides five managed policies for Claude Platform on AWS. All managed policies apply to `Resource: "*"`.

| Policy                                 | Grants                                                                                                                                                                             |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AnthropicFullAccess`                  | `aws-external-anthropic:*`                                                                                                                                                         |
| `AnthropicReadOnlyAccess`              | `Get*`, `List*`, `CallWithBearerToken`                                                                                                                                             |
| `AnthropicInferenceAccess`             | `Get*`, `List*`, `CreateInference`, `CreateBatchInference`, `CancelBatchInference`, `DeleteBatchInference`, `CountTokens`, `CallWithBearerToken`                                   |
| `AnthropicLimitedAccess`               | All `AnthropicInferenceAccess` actions, plus all Claude Managed Agents actions (agents, sessions, environments, vaults, memory stores, webhooks, and self-hosted environment work) |
| `AnthropicSelfHostedEnvironmentAccess` | `GetEnvironment`, `ProcessEnvironmentWork`, `GetSession`, `UpdateSession`, `GetSkill`, `CallWithBearerToken`                                                                       |

`AnthropicInferenceAccess` is the narrowest managed policy sufficient to run inference. It covers both synchronous and batch inference and, through the `Get*` and `List*` wildcards, grants read access to every API resource in the namespace, including Claude Managed Agents (CMA) resources (agents, sessions, environments, vaults, memory stores, and webhooks). This includes file content download through `GetFile` (see the [Files](#files) note), skill content download through `GetSkill` (see the [Skills](#skills) note), and memory contents through `GetMemoryStore`. Vault credential secrets and webhook signing secrets are not exposed: those fields are write-only and are never returned by `GetVault` or `GetWebhook` (see [Authenticate with vaults](/docs/en/managed-agents/vaults)). `AnthropicInferenceAccess` does not grant file creation or deletion, skill management, user profile management, workspace mutation, or any Claude Managed Agents write action (create, update, archive, delete, process, or rotate). To exclude CMA reads, replace `AnthropicInferenceAccess` with a custom policy that enumerates only the specific non-CMA actions you need.



`AnthropicReadOnlyAccess`, `AnthropicInferenceAccess`, and `AnthropicLimitedAccess` all carry the `Get*` and `List*` wildcards, which grant read access to all content in the workspace: file bytes, skill content, batch results, session conversation history, and memory contents. Vault credential secrets and webhook signing secrets are not exposed; those fields are write-only and are never returned by `GetVault` or `GetWebhook`. If your principal should not read existing content, use a custom policy that enumerates only the actions you need.

`AnthropicLimitedAccess` includes all Claude Managed Agents actions in addition to inference actions.

`AnthropicSelfHostedEnvironmentAccess` is the narrowest managed policy sufficient to run a [self-hosted sandbox](/docs/en/managed-agents/self-hosted-sandboxes) worker. Attach it to the principal your environment worker authenticates as.

`AssumeConsole` is not included in `AnthropicReadOnlyAccess`, `AnthropicInferenceAccess`, `AnthropicLimitedAccess`, or `AnthropicSelfHostedEnvironmentAccess`. Principals who need Claude Console access require either `AnthropicFullAccess` or a custom policy that grants `aws-external-anthropic:AssumeConsole`. See [Console access](#console-access).



`CreateInference` and `CreateBatchInference` are separate actions. Denying one does not block the other. If you intend to prevent all model calls, deny both.




Example policies




Synchronous inference on a single workspace

Grants the minimal permissions for an IAM principal that runs inference against one production workspace:

```python
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-external-anthropic:CreateInference",
        "aws-external-anthropic:CountTokens",
        "aws-external-anthropic:GetModel",
        "aws-external-anthropic:ListModels",
        "aws-external-anthropic:GetWorkspace"
      ],
      "Resource": "arn:aws:aws-external-anthropic:us-west-2:123456789012:workspace/wrkspc_01AbCdEf23GhIj"
    }
  ]
}
```





`ListWorkspaces` is account-scoped (see [Provisioning automation](#provisioning-automation)). If your service account needs to enumerate workspaces, add a separate `Allow` statement for `ListWorkspaces` with `Resource: "*"`.

This policy assumes AWS SigV4 authentication. If the principal authenticates with an API key, add a separate `Allow` statement for `aws-external-anthropic:CallWithBearerToken` with `Resource: "*"`. `CallWithBearerToken` is a route-less action that does not bind to a workspace ARN. See [Per-customer workspace isolation](#per-customer-workspace-isolation) for the two-statement pattern.




Per-customer workspace isolation

Restricts a role to a single workspace:

```python
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "aws-external-anthropic:*",
      "Resource": "arn:aws:aws-external-anthropic:us-west-2:123456789012:workspace/wrkspc_01AbCdEf23GhIj"
    },
    {
      "Effect": "Allow",
      "Action": [
        "aws-external-anthropic:CallWithBearerToken",
        "aws-external-anthropic:AssumeConsole"
      ],
      "Resource": "*"
    }
  ]
}
```





The `aws-external-anthropic:*` wildcard in the first statement includes account-scoped actions (`CreateWorkspace`, `ListWorkspaces`) that the workspace ARN constraint silently filters out. This is consistent with the "isolation" intent (the role cannot create or enumerate workspaces), but the policy contains permissions that have no effect. See [Provisioning automation](#provisioning-automation) for the account-scoped pattern.

`CallWithBearerToken` and `AssumeConsole` are route-less actions that do not bind to a workspace ARN. The second statement grants them on `Resource: "*"` so the role can authenticate with an API key and open the Claude Console. Omit this statement if the role uses SigV4 only and does not need Claude Console access.




Feature lockdown for a ZDR-sensitive workspace

Blocks batch processing and file upload on a specific workspace while leaving synchronous inference available. Useful when a workspace handles [Zero Data Retention (ZDR)](/docs/en/manage-claude/api-and-data-retention) data that must not persist server-side. Attach this policy alongside an Allow policy such as `AnthropicInferenceAccess` or the [single-workspace example](#synchronous-inference-on-a-single-workspace); on its own, a Deny-only policy grants no permissions:

```python
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "aws-external-anthropic:CreateBatchInference",
        "aws-external-anthropic:CreateFile"
      ],
      "Resource": "arn:aws:aws-external-anthropic:us-west-2:123456789012:workspace/wrkspc_01AbCdEf23GhIj"
    }
  ]
}
```





This deny blocks creation only. Other file and batch actions are not denied unless you list them as well. For a complete lockdown where the workspace must never hold files or batches, also deny `aws-external-anthropic:GetFile`, `aws-external-anthropic:ListFiles`, `aws-external-anthropic:DeleteFile`, `aws-external-anthropic:GetBatchInference`, `aws-external-anthropic:ListBatchInferences`, `aws-external-anthropic:CancelBatchInference`, and `aws-external-anthropic:DeleteBatchInference`.




Provisioning automation



The Claude Console Workspaces page is read-only; use the Admin API workspace endpoints or the AWS Console to create, update, or archive workspaces.

Grants a CI/CD role the actions needed to create and manage workspaces, without any inference permissions:

```python
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-external-anthropic:CreateWorkspace",
        "aws-external-anthropic:GetWorkspace",
        "aws-external-anthropic:ListWorkspaces",
        "aws-external-anthropic:UpdateWorkspace",
        "aws-external-anthropic:ArchiveWorkspace"
      ],
      "Resource": "*"
    }
  ]
}
```



`CreateWorkspace` and `ListWorkspaces` are account-scoped operations. Specifying a workspace ARN on these actions has no effect; use `Resource: "*"`.




See also

- [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws) for setup, authentication, and platform overview
- [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) for IAM policy syntax and evaluation logic
- [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/) for audit logging configuration
