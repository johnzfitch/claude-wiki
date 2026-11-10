---
title: "IAM permissions for Claude Models on Google Cloud (Anthropic managed) - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/api/claude-models-on-google-cloud-anthropic-managed-iam-permissions"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-08T06:25:18Z"
tags: ["api"]
---

# IAM permissions for Claude Models on Google Cloud (Anthropic managed)

Copy page



Look up Google Cloud IAM permissions, predefined roles, and audit log types for Claude Models on Google Cloud (Anthropic managed).

Copy page



Claude Models on Google Cloud (Anthropic managed) uses Google Cloud IAM for access control. Every API route needs one permission from the `claude.googleapis.com` service. If the caller doesn’t hold that permission, Google Cloud returns an HTTP 403 error. Three predefined roles bundle the permissions. For setup and authentication, see [Claude Models on Google Cloud (Anthropic managed)](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md).

## Service details

The following table describes the Google Cloud service for Claude Models on Google Cloud (Anthropic managed).

[TABLE]

Grant roles on the Google Cloud project. For how projects, organizations, and workspaces relate, see [Workspaces](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md#workspaces).

Permissions on this page are in the short form `resource.verb`, such as `messages.create`.

## Predefined roles

The following table lists the predefined roles for Claude Models on Google Cloud (Anthropic managed).

[TABLE]

In the following tables, **Admin**, **User**, and **Viewer** stand for these three roles.

## Permissions

The following tables list 69 permissions across 113 routes.

The `get` and `list` permissions are the read-only ones.

Unless a section says otherwise, each route’s audit log type is Data Access.

`roles/claude.viewer` can’t send messages or count tokens. Sending a message needs `messages.create`. Counting tokens needs `messages.countTokens`.

Some routes in the following tables might not be available to your organization. To check which features are available, see [Feature support](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md#feature-support).

### Messages

| Permission             | Roles       | Routes authorized                |
|:-----------------------|:------------|:---------------------------------|
| `messages.create`      | Admin, User | `POST /v1/messages`              |
| `messages.countTokens` | Admin, User | `POST /v1/messages/count_tokens` |

### Message batches

[TABLE]

`roles/claude.viewer` can read batch results. `messageBatches.get` authorizes both reading a batch’s metadata and downloading its results.

### Models

| Permission    | Roles               | Routes authorized           |
|:--------------|:--------------------|:----------------------------|
| `models.get`  | Admin, User, Viewer | `GET /v1/models/{model_id}` |
| `models.list` | Admin, User, Viewer | `GET /v1/models`            |

### Files

[TABLE]

`roles/claude.viewer` can download files. `files.get` authorizes both reading a file’s metadata and downloading its content.

### Skills

[TABLE]

Creating or deleting a skill version needs `skills.update`, not `skills.create` or `skills.delete`.

### Agents

[TABLE]

You can archive an agent but not delete it.

### Sessions

[TABLE]

`sessions.get` authorizes reading the session, its event history and event stream, its resources, and its threads. As a result, `roles/claude.viewer` can read every session’s full event history.

Other session operations need the following permissions:

- Sending events: `sessions.update`
- Adding, changing, or removing session resources: `sessions.update`
- Archiving a thread: `sessions.archive`

### Environments

[TABLE]

`roles/claude.user` and `roles/claude.admin` include every permission that a [self-hosted sandbox](../Other/managed-agents-self-hosted-sandboxes.md) worker needs. `environments.processWork` authorizes these worker actions:

- Polling for work
- Acknowledging work items
- Sending heartbeats for work items
- Stopping work items
- Updating work items

This permission is separate from `environments.update`. Reading the work queue and its statistics needs only `environments.get`.

Besides `environments.processWork`, a worker needs other permissions to run a session, such as `sessions.get` to read the session and its events, `sessions.update` to send tool results, and `skills.get` to download the agent’s skills.

### Vaults

Google Cloud records these routes in Admin Activity audit logs, except the route for `vaults.verify`, whose audit log type is Data Access.

[TABLE]

Credential operations need the following permissions:

- Creating, changing, or deleting a credential: `vaults.update`
- Archiving a credential: `vaults.archive`
- Reading a credential: `vaults.get`
- Checking a stored MCP OAuth credential: `vaults.verify`

With `vaults.get`, `roles/claude.viewer` can list a vault’s credentials. Claude Models on Google Cloud (Anthropic managed) never returns a credential’s secret fields. To learn more, see [Authenticate with vaults](../Other/managed-agents-vaults.md).

### Memory stores

[TABLE]

Memory store operations need the following permissions:

- Reading the store, its memories, or its version history: `memoryStores.get`
- Creating, changing, or deleting a memory: `memoryStores.update`
- Redacting a memory version: `memoryStores.update`

### Deployments

[TABLE]

Reading deployment runs needs `deployments.get`.

### Dreams

| Permission       | Roles               | Routes authorized                    |
|:-----------------|:--------------------|:-------------------------------------|
| `dreams.create`  | Admin, User         | `POST /v1/dreams`                    |
| `dreams.get`     | Admin, User, Viewer | `GET /v1/dreams/{dream_id}`          |
| `dreams.list`    | Admin, User, Viewer | `GET /v1/dreams`                     |
| `dreams.archive` | Admin, User         | `POST /v1/dreams/{dream_id}/archive` |
| `dreams.cancel`  | Admin, User         | `POST /v1/dreams/{dream_id}/cancel`  |

Dreams is a research preview feature. To request access, see [Dreams](../Other/managed-agents-dreams.md).

### Encryption keys

Google Cloud records these routes in Admin Activity audit logs.

| Permission | Roles | Routes authorized |
|:---|:---|:---|
| `externalKeys.create` | Admin | `POST /v1/organizations/external_keys` |
| `externalKeys.get` | Admin | `GET /v1/organizations/external_keys/{external_key_id}` |
| `externalKeys.list` | Admin | `GET /v1/organizations/external_keys` |
| `externalKeys.update` | Admin | `POST /v1/organizations/external_keys/{external_key_id}` |
| `externalKeys.delete` | Admin | `DELETE /v1/organizations/external_keys/{external_key_id}` |

These permissions manage your organization’s encryption key registrations. Of the three predefined roles, only `roles/claude.admin` includes them.

### Usage reports

[TABLE]

Of the three predefined roles, only `roles/claude.admin` includes `usageAnalytics.list` and `costAnalytics.list`.

## See also

- [Claude Models on Google Cloud (Anthropic managed)](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)
- [IAM roles](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md#iam-roles)
- [Monitoring and logging](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md#monitoring-and-logging)
