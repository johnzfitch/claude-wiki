---
title: "Get your Claude API key - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/get-api-key"
category: "04-API-Reference/Other"
fetched_at: "2026-11-13T06:35:01Z"
tags: ["api"]
---

# Get your Claude API key

Copy page



Find, create, and manage your API keys for the Claude API in the Claude Console.

Copy page



API keys for the Claude API (also called Anthropic API keys) live in the Claude Console. To view your existing keys or create a new one, go to the [API keys](playground.md) page (`platform.claude.com/settings/keys`) in the Console.

## Choose a key type

When you create a key, you choose its type, which determines what the key can do, where it works, and when it stops working. A **personal key** acts as you, and stops working if you leave an organization. A **service account key** represents a [service account](manage-claude-workload-identity-federation.md#service-accounts), which can be used by workloads such as CI pipelines, production services, or agents. Use a personal key for your own development, and a service account key for anything shared.

You can also create a **workspace key**, a legacy key without an owner: it belongs to the workspace you create it in and keeps working after its creator leaves. It is preferable to use a personal or service account key, as these stop working automatically when their associated account is removed from the organization.

## Create an API key

1.  1

    ### Sign in to the Claude Console

    Go to the Claude Console at [platform.claude.com](playground.md) and sign in, or create an account if you don’t have one yet.

2.  2

    ### Open the API keys page

    In the Claude Console, go to the [API keys](playground.md) page (`platform.claude.com/settings/keys`).

3.  3

    ### Create a key

    Click **Create key**, name the key, select an [expiration](manage-claude-authentication.md#key-expiration), and set **Linked account** to yourself or a service account. You can also select a [workspace](playground.md) in the Console to scope the key to.

4.  4

    ### Copy and store the key

    The Console shows the full key, which starts with `sk-ant-`, only once, at creation. Copy it and store it somewhere safe, such as a secrets manager. If you lose a key, you can’t view it again in the Console. Create a new key instead.

If the **Create key** button on the API keys page is disabled, your role might not allow you to create keys there. Ask an organization admin to change your role, or to create a service account key for your workload.

## Use your API key

Set the key as an environment variable:

```python
export ANTHROPIC_API_KEY="sk-ant-api03-..."
```



The [client SDK](cli-sdks-libraries-overview.md) reads `ANTHROPIC_API_KEY` automatically. Direct HTTP requests send the key as `Authorization: Bearer <key>`. If your API key isn’t scoped to a workspace, you must also send the `anthropic-workspace-id` header on each Claude API request, as shown in [Select a workspace](manage-claude-authentication.md#select-a-workspace). For the Admin API, see [API keys and the Admin API](#api-keys-and-the-admin-api).

To make your first request, follow the [Quickstart](../../01-Getting-Started/get-started.md), and see [Authentication](manage-claude-authentication.md) for complete details, including short-lived credentials with Workload Identity Federation.

## API keys and the Admin API

The [Admin API](../Endpoints/organization.md) includes endpoints for managing your organization’s API keys programmatically, such as [Retrieve API Key](../Endpoints/organization-api-keys-retrieve.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. and [List API Keys](../Endpoints/organization-api-keys-list.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return.. These endpoints are for organization admins automating key management. They accept an [Admin API key](manage-claude-admin-api-keys.md), an OAuth token with the `org:admin` scope, or a personal or service account key that isn’t scoped to a specific workspace; workspace keys don’t work there. They never return a key’s secret value, only a partially redacted hint.



The Admin API can’t recover a lost key or give you a key to call the Claude API with. To get a usable API key, create one on the [API keys](playground.md) page (`platform.claude.com/settings/keys`) in the Claude Console.
