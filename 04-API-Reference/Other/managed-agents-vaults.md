---
title: "Authenticate with vaults - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/vaults"
category: "04-API-Reference/Other"
fetched_at: "2026-10-20T06:39:40Z"
tags: ["api"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fvaults)





SearchCtrlK

First steps

[Overview](managed-agents-overview.md)[Quickstart](managed-agents-quickstart.md)[Build in Console](managed-agents-onboarding.md)[Migration](managed-agents-migration.md)

Define your agent

[Agent setup](managed-agents-agent-setup.md)[Tools](managed-agents-tools.md)[Web tool restrictions](managed-agents-tools-web-restrictions.md)[MCP connector](managed-agents-mcp-connector.md)[Permission policies](managed-agents-permission-policies.md)[Agent Skills](managed-agents-skills.md)

Configure agent environment

[Choose an environment](managed-agents-choosing-an-environment.md)[Cloud environment setup](managed-agents-environments.md)[Cloud sandbox reference](managed-agents-cloud-sandboxes-reference.md)

[Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md)

Delegate work to your agent

[Start a session](managed-agents-sessions.md)[Session operations](managed-agents-session-operations.md)[Session event stream](managed-agents-events-and-streaming.md)[Event deltas](managed-agents-event-deltas.md)[Inspect and track usage](managed-agents-session-observability.md)[Session budgets](managed-agents-budgets.md)[Subscribe to webhooks](managed-agents-webhooks.md)[Define outcomes](managed-agents-define-outcomes.md)[Authenticate with vaults](managed-agents-vaults.md)

Manage agent context

[Access GitHub](managed-agents-github.md)[Attach and download files](managed-agents-files.md)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](managed-agents-multiagent-orchestration.md)[Session threads](managed-agents-session-threads.md)[Workflow runs](managed-agents-workflow-runs.md)[Scheduled deployments](managed-agents-scheduled-deployments.md)

Security

[Secure your deployment](managed-agents-secure-deployment.md)[Review and monitor sessions](managed-agents-secure-deployment-monitoring.md)[Risks and boundaries](managed-agents-secure-deployment-risks.md)

Reference

[Managed Agents reference](managed-agents-reference.md)

Working with files

[Files API](../Guides/build-with-claude-files.md)[PDF support](../Guides/build-with-claude-pdf-support.md)

[Images and vision](../Guides/build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)

[Console](playground.md)

[Managed Agents](managed-agents-overview.md)Delegate work to your agent

[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

# Authenticate with vaults

Copy page



Register per-user credentials when creating sessions.

Copy page



Vaults and credentials are authentication primitives that let you register credentials for third-party services once and reference them by ID at session creation. This means you don't need to run your own secret store, transmit tokens on every call, or lose track of which end user an agent acted on behalf of.

The vault reference is a per-session parameter, so you can manage your product at the `agent` resource granularity and your users at the `session` resource granularity.

## Create a vault



Vaults and credentials are workspace-scoped, meaning any API key with workspace access can reference them when creating a session. To revoke access, delete the vault or credential.

A vault is the collection of `credentials` associated with an end user. Give it a `display_name` and optionally tag it with `metadata` so you can map it back to your own user records.

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



```python
vault = client.beta.vaults.create(
    display_name="Alice",
    metadata={"external_user_id": "usr_abc123"},
)
print(vault.id)  # "vlt_01ABC..."
```

The response is the full vault record:

```python
{
  "type": "vault",
  "id": "vlt_01ABC...",
  "display_name": "Alice",
  "metadata": { "external_user_id": "usr_abc123" },
  "created_at": "2026-03-18T10:00:00Z",
  "updated_at": "2026-03-18T10:00:00Z",
  "archived_at": null
}
```



## Add a credential

Two credential categories are supported:

- **MCP credentials** (`mcp_oauth`, `static_bearer`): each credential is keyed by an `mcp_server_url`. When the agent connects to a server at that URL at session runtime, the token is injected automatically.
- **Environment variables** (`environment_variable`): each credential is keyed by a `secret_name` (the environment variable name) and stored in the sandbox as an opaque placeholder. When the agent initiates an outbound request, the opaque placeholder is substituted with the real secret at egress. The agent never sees the secret value. Use this for any service that authenticates through an environment variable, such as CLIs, SDKs, or direct API calls.

The actual credential values you supply (`token`, `access_token`, `refresh_token`, `client_secret`, `secret_value`) are treated as sensitive, write-only fields and never returned in API responses.



Environment variable credentials (`environment_variable`) are not yet supported with [self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md).

To get the same behavior with a self-hosted sandbox, you can run your own proxy that replaces placeholder values with the real secrets at egress.

MCP OAuth

MCP static bearer

Environment variable

MCP OAuth

Use `mcp_oauth` when the MCP server uses OAuth 2.0. If you supply a `refresh` block, Anthropic refreshes the access token on your behalf when it expires.

The `refresh.token_endpoint_auth.type` field indicates how to authenticate the refresh call:

- `none`: public client
- `client_secret_basic`: HTTP Basic authentication with the client secret
- `client_secret_post`: client secret in the POST body

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



```python
credential = client.beta.vaults.credentials.create(
    vault_id=vault.id,
    display_name="Alice's Slack",
    auth={
        "type": "mcp_oauth",
        "mcp_server_url": "https://mcp.slack.com/mcp",
        "access_token": "xoxp-...",
        "expires_at": "2099-12-31T23:59:59Z",
        "refresh": {
            "token_endpoint": "https://slack.com/api/oauth.v2.user.access",
            "client_id": "1234567890.0987654321",
            "scope": "channels:read chat:write",
            "refresh_token": "xoxe-1-...",
            "token_endpoint_auth": {
                "type": "client_secret_post",
                "client_secret": "abc123...",
            },
        },
    },
)
```

Set `refresh.token_endpoint` to the token endpoint of the OAuth flow that issued the refresh token, because Anthropic sends every refresh request to that URL and the field can't be changed after the credential is created.

MCP static bearer

Use `static_bearer` when the MCP server accepts a fixed bearer token (API key, personal access token, or similar). No refresh flow is needed.

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



```python
bearer_credential = client.beta.vaults.credentials.create(
    vault_id=vault.id,
    display_name="Linear API key",
    auth={
        "type": "static_bearer",
        "mcp_server_url": "https://mcp.linear.app/mcp",
        "token": "lin_api_your_linear_key",
    },
)
```

Environment variable

Use `environment_variable` to authenticate to external services through an environment variable, such as CLIs, SDKs, or direct API calls. Environment variable credentials work for clients that send the secret value verbatim in an outbound request, so check the client eligibility criteria in this tab before configuring one.

The `allowed_hosts` array in `networking` controls which outbound hosts the secret can be substituted for. Use `"type": "limited"` with a specific list, or `"type": "unrestricted"` if the caller reaches domains you can't enumerate in advance.

Limiting domains is strongly recommended for security purposes, and prevents your key from ever being shared with unauthorized hosts.



`allowed_hosts` in `networking` on a vault credential controls which requests use the secret, not which requests are allowed. For the agent to actually reach a domain, it must also be allowed at the [environment level](managed-agents-environments.md). Both levels must include the domain (either through `unrestricted` networking or by explicitly listing the domain in `allowed_hosts`) for a secret-substituted request to succeed.

The optional `injection_location` field scopes where the secret is substituted; the full semantics follow the example.

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



```python
env_credential = client.beta.vaults.credentials.create(
    vault_id=vault.id,
    display_name="Notion API key for sandbox",
    auth={
        "type": "environment_variable",
        "secret_name": "NOTION_API_KEY",
        "secret_value": "ntn_your-secret-here",
        "networking": {
            "type": "limited",
            "allowed_hosts": ["api.notion.com"],
        },
        "injection_location": {"header": True},
    },
)
if env_credential.auth.type == "environment_variable":
    location = env_credential.auth.injection_location
    print(
        f"header: {location.header}, body: {location.body}"
    )  # header: True, body: False
```

Request payloads are often assembled from content the agent is working with, so the request body is the broader exposure surface. Most services read an API key from a request header, so enabling only `header` is the narrower configuration. It scopes substitution to request header values for that credential.

The credential's `injection_location` controls which parts of an outbound request the secret is substituted into. It is an optional object, a sibling of `networking`, with two Boolean fields: `header` (request headers) and `body` (request body). `injection_location` is independent of `allowed_hosts` in `networking`: `allowed_hosts` scopes which hosts the secret is substituted for, and `injection_location` scopes which parts of the request it is substituted into.

`injection_location` behaves differently on create and on update:

| Operation         | `injection_location` behavior                                                                                                                                                              |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create credential | If you provide the object, any field you omit inside it defaults to `false`: `{"header": true}` creates a header-only credential. Omit the object entirely and both locations are enabled. |
| Update credential | Fields merge individually: `{"body": false}` disables body substitution and leaves `header` unchanged.                                                                                     |

A credential must have at least one location enabled, so a create or update that would disable both locations returns a 400 error. Passing an explicit `null` for the `injection_location` object or for either field also returns a 400 error ("omit the field instead"). The response always returns both fields with their resolved values.

A placeholder in a disabled location is neither substituted nor stripped. The request is sent to the third party with the literal opaque placeholder string in that location. If a request arrives at the third party containing the literal placeholder string, either that location is disabled for the credential or the destination host is not covered by the `allowed_hosts` in the credential's `networking`.



Credentials created in the Console enable header injection only. If your client sends the secret in the request body, such as a form-encoded token request, the placeholder passes through literally and the service rejects it with its own authentication error. Enable body injection in the Console form when you create the credential, or update the credential with `{"injection_location": {"body": true}}`.

The substitution happens at egress, not inside the sandbox. Anything that processes the credential locally sees the opaque placeholder, not the real value: clients that validate the credential format at startup may reject it, and clients that compute a request signature from the secret (for example, AWS SigV4) produce an invalid signature. Environment variable credentials work for clients that send the secret value verbatim in an outbound request, in a location the credential's `injection_location` enables.

Substitution is outbound only. If a client uses the stored secret to fetch a session token (for example, an OAuth client-credentials grant), the returned token arrives in the sandbox unredacted. For exchange-based flows, perform the exchange yourself and store the resulting token in the vault instead.



Scope the API key to only the permissions the agent needs. The agent can do anything the key allows, so a key with broader permissions than necessary increases the blast radius if the agent behaves unexpectedly.

Credentials are stored as provided and are not validated until session runtime. An invalid credential surfaces as an authentication or downstream error during the session, which is emitted but does not block the session from continuing.

Constraints:

- **Unique key per vault.** `mcp_server_url` (MCP credentials) and `secret_name` (environment variable credentials) must be unique among active credentials in a vault. Creating a duplicate returns a 409.
- **Keys are immutable.** To change `mcp_server_url` or `secret_name`, archive the credential and create a new one.
- **Maximum 20 credentials per vault.**

## Reference the vault at session creation

Pass `vault_ids` when creating a session:

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



```python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    vault_ids=[vault.id],
    title="Alice's Slack digest",
)
```

Runtime behavior:

- When no MCP credential matches by `mcp_server_url`, the connection is attempted unauthenticated and will error if the server requires authentication.
- When multiple vaults contain a matching credential, the first vault with a match wins.
- In [multiagent sessions](managed-agents-multiagent-orchestration.md), vault credentials apply to every thread. An agent whose own definition declares the matching MCP server authenticates with these credentials. See [Connect agents to MCP servers](managed-agents-multiagent-orchestration.md#connect-agents-to-mcp-servers).

## Rotate a credential

Secret values, `display_name`, and (on environment variable credentials) `injection_location` can be updated. `injection_location` updates merge per field, as described in the Environment variable tab of [Add a credential](#add-a-credential). For a running session, an `injection_location` update propagates the same way as a secret rotation: the session's credentials are re-resolved without a restart, as described in [Credential lifecycle](#credential-lifecycle), and the updated locations apply to the session's subsequent outbound requests. Structural fields (`mcp_server_url`, `secret_name`, `token_endpoint`, `client_id`) are locked after creation. To change them, archive the credential and create a new one.

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



```python
client.beta.vaults.credentials.update(
    credential.id,
    vault_id=vault.id,
    auth={
        "type": "mcp_oauth",
        "access_token": "xoxp-new-...",
        "expires_at": "2099-12-31T23:59:59Z",
        "refresh": {"refresh_token": "xoxe-1-new-..."},
    },
)
```

## Credential lifecycle

Credentials are re-resolved periodically, both during a session and during the vault lifecycle. This ensures that credential rotation, archival, or deletion propagates to running sessions without a restart.

To be notified if a credential is archived, deleted, or fails to refresh, you can subscribe to the vault and credential [webhooks](managed-agents-webhooks.md) associated with those lifecycle changes.

| Event                             | Trigger                                                                                                              |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------|
| `vault.archived`                  | Vault archived. A `vault_credential.archived` event is also emitted for each underlying credential.                  |
| `vault.deleted`                   | Vault deleted. A `vault_credential.deleted` event is also emitted for each underlying credential.                    |
| `vault_credential.archived`       | Credential archived, either directly or as a result of vault archival.                                               |
| `vault_credential.deleted`        | Credential deleted, either directly or as a result of vault deletion.                                                |
| `vault_credential.refresh_failed` | An `mcp_oauth` credential cannot be refreshed (invalid refresh token, or irrecoverable error from the OAuth server). |



This is a non-exhaustive list of webhooks; see [Subscribe to webhooks](managed-agents-webhooks.md) for the complete list.

For `mcp_oauth` credentials, re-resolution also refreshes the access token if it has expired. If the refresh fails, a `vault_credential.refresh_failed` event is emitted.

### Diagnose an OAuth refresh failure

To diagnose why a refresh failed, call `POST /v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate` (or `client.beta.vaults.credentials.mcp_oauth_validate(...)` in the SDK). This lets you decide how to handle the failure; the right action depends on the error type.

The top-level `status` tells you what to do next:

- `valid`: the token works; no action needed.
- `invalid`: the grant is gone or the OAuth server rejected the refresh with a 4xx. Prompt the end user to re-authorize.
- `unknown`: a transient error (5xx, 429, or network failure). Wait and retry.

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



```python
validation = client.beta.vaults.credentials.mcp_oauth_validate(
    credential.id,
    vault_id=vault.id,
)
print(validation.status)  # "valid", "invalid", or "unknown"
```

The response is a `vault_credential_validation` object. `mcp_probe` includes the failed MCP handshake step; `refresh` includes the outcome of the attempted refresh.

```python
{
  "type": "vault_credential_validation",
  "credential_id": "vcrd_01ABC...",
  "vault_id": "vlt_01XYZ...",
  "validated_at": "2026-04-29T17:12:00Z",
  "has_refresh_token": false,
  "status": "invalid",
  "mcp_probe": {
    "method": "initialize",
    "http_response": {
      "status_code": 401,
      "content_type": "application/json",
      "body": "{\"error\":\"invalid_token\"}",
      "body_truncated": false
    }
  },
  "refresh": {
    "status": "no_refresh_token",
    "http_response": null
  }
}
```



## Other operations

- **List vaults or credentials:** Paginated, newest first. Archived records are excluded by default (pass `include_archived=true` to include them).
- **Archive a vault:** `POST /v1/vaults/{id}/archive`. Cascades to all credentials. Secrets are purged; records are retained for auditing. Future sessions referencing this vault fail; running sessions continue.
- **Archive a credential:** `POST /v1/vaults/{id}/credentials/{cred_id}/archive`. Purges the secret payload; the credential key (`mcp_server_url` or `secret_name`) remains visible and is freed for a replacement credential.
- **Delete a vault or credential:** Hard delete. The record is not retained. Use archive if you need an audit trail.
