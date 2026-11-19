---
title: "Configuration reference - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/self-hosted/configuration-reference"
category: "04-API-Reference/Other"
fetched_at: "2026-11-13T06:34:13Z"
tags: ["agents", "api", "git", "mcp", "skills"]
---

# Configuration reference

Copy page



See where the settings of a self-hosted Claude Managed Agents server go, and look up each setting’s key, environment variable, default, and purpose.

Copy page





To request access to self-hosted Claude Managed Agents, contact your Anthropic account team.

This page shows where the settings of a self-hosted Claude Managed Agents server go, and lists them. To set up a feature, see [Single sign-on](managed-agents-self-hosted-configure.md), [Agent identity and credentials](managed-agents-self-hosted-agent-identity.md), and [Inference provider](managed-agents-self-hosted-inference-provider.md).

## Where settings go

The server reads its settings from one YAML file, and its credentials from its environment.

- **Docker Compose:** The file is `compose.config.yaml`, beside `docker-compose.yml` in the extracted archive. Edit it, then run `docker compose restart cma-server` from that directory.
- **Kubernetes:** The file is the `server.config` value of the server Helm chart. Edit it in your values file, run `helm upgrade`, and then restart the servers with `kubectl -n cma-server rollout restart deployment -l anthropic.com/role=server`. See [Deploy on Kubernetes](managed-agents-self-hosted-kubernetes.md).

If the server rejects a setting that the self-hosted pages show, [upgrade the server](managed-agents-self-hosted-upgrade.md). `cma-server.example.yaml`, at the top of the archive, annotates the common keys.

Credentials never go in the file. The server reads them from environment variables, or from the identity that your cloud attaches to the host.

### Pass a credential to the Compose stack

In the Compose stack, the server container receives only the variables in the `environment:` list of the `cma-server` service in `docker-compose.yml`. To pass another one:

1.  Add its name to that list, and set its value in `.env`.
2.  If the credential is a file, put the file beside `docker-compose.yml`, and add a line such as `- ./gcp-key.json:/etc/cma-server/gcp-key.json:ro` to the `x-server-mounts` list in `docker-compose.yml`. The path after the first colon is the file’s path inside the container. Use that path as the variable’s value in `.env`, or as the value of the setting that names the file.
3.  Run `docker compose up -d`. A restart doesn’t reread `.env`.

An upgrade replaces `docker-compose.yml`, so repeat these edits in the new release’s file before you start its stack.

## How to read the tables

Each setting has a key in the [settings file](#where-settings-go), and most settings also have an environment variable. A variable overrides the file, and the file overrides the default. The server doesn’t start if its settings file has an unknown key, and the error says where the key is.

- **Keys:** Each dot in a key is a level of nesting in the file. For example, `server.addr` is the `addr` key in the `server` section.
- **Variables:** A variable’s name is `CMA_` and then the key in capitals, with two underscores in place of each dot.
- **File only:** The setting has no variable.
- **Environment only:** The server doesn’t start if the setting is in the file.
- **`bedrock` only, and similar labels:** The setting works only with that provider, store, or secret manager. If you set it while you use a different one, the server doesn’t start.
- **Lists:** A list is a YAML list in the file, and a comma-separated string in a variable.
- **Durations:** A duration is a number with a unit, such as `30s`, `5m`, or `1h`.
- **Integers:** An integer is plain digits, with no sign, leading zero, or underscore.

At startup, the server logs the settings that you set and most defaults, each with where its value came from, such as `server.addr=0.0.0.0:8400 (file)`. It logs `***` in place of a secret, except a server API key that it generated itself.

## Server and logging

[TABLE]

## Database

Every setting in this table except `store.backend` applies only with `store.backend: postgres`.

[TABLE]

## Inference provider

To set up a provider, see [Inference provider](managed-agents-self-hosted-inference-provider.md).

[TABLE]

### Cloud providers

[TABLE]

### Model gateway

These settings apply only with `inference.provider: gateway`. See [Model gateway](managed-agents-self-hosted-inference-provider.md#model-gateway).

[TABLE]

### Short-lived gateway tokens

These settings apply only with `inference.credentials.supplier: oauth_exchange`. See [Short-lived tokens](managed-agents-self-hosted-inference-provider.md#short-lived-tokens). The `exchange` settings are optional as a group. Without them, the server sends the gateway what the callback returns.

[TABLE]

## Single sign-on

To set up sign-in, see [Single sign-on](managed-agents-self-hosted-configure.md).

[TABLE]

### Issuer entries

Each entry of `auth.issuers` takes these fields:

| Field | Default | Description |
|----|----|----|
| `name` | None | Required. A label for the issuer in log lines. The server also records it as part of the creator of each resource. |
| `issuer_url` | None | Required. The issuer’s URL, exactly as in the `iss` claim of its tokens. The server fetches signing keys from this host and from the `jwks_uri` host that the issuer’s discovery document names. If your network limits outbound connections, admit both hosts. |
| `audiences` | None | Required. The values that a token’s `aud` claim can carry. If applications forward tokens that they already hold, list each application’s client ID. |
| `roles` | None | A list of `group` and `role` pairs. A group matches exactly, or as a pattern in which `*` stands for any run of characters and `?` for one character. A role is `admin`, `developer`, or `user`. The highest matching role wins. Set `roles`, `default_role`, or both. |
| `default_role` | None | The role of a caller whose groups match no `roles` entry. Set it only if everyone who can get a token for this audience should have access. |
| `subject_claim` | `sub` | The claim that identifies the caller. A name that starts with `/` is a JSON Pointer into nested claims. |
| `stable_subject` | `false` | Applies only if `subject_claim` names a claim other than `sub` or `oid`. Set `true` to confirm that your provider never changes a person’s value of that claim and never gives it to someone else. The server doesn’t check this. With `false`, [agent tokens](#agent-identity) omit the `actor_sub` and `actor_iss` claims. |
| `groups_claim` | `groups` | The claim that lists the caller’s groups. A name that starts with `/` is a JSON Pointer into nested claims. |
| `jwks_file` | None | The path of a JSON Web Key Set file. The server reads signing keys from it and never contacts the issuer. |
| `login_client_id` | None | The client ID of the application that [terminal login](managed-agents-self-hosted-configure.md#let-developers-log-in-from-a-terminal) uses. Only one issuer can set it. |
| `login_scopes` | `[openid]` | The scopes that the login requests. This field needs `login_client_id`. |

## Secret manager

To set up a store, see [Secret manager](managed-agents-self-hosted-agent-identity.md#secret-manager).

[TABLE]

### HashiCorp Vault

These settings apply only with `secret_store.type: hashicorp_vault`. Set exactly one login method: `token_file`, `kubernetes`, or `approle`.

[TABLE]

## Agent identity

To set up agent tokens, see [Agent identity](managed-agents-self-hosted-agent-identity.md#agent-identity). Any setting in this table turns the feature on. The server then needs `agent_identity.issuer` and exactly one place for the signing key: `key_file`, `key_secret`, or `kms_key`.

[TABLE]

## Egress gateway

To set up the gateway, see [Environment variable credentials](managed-agents-self-hosted-agent-identity.md#environment-variable-credentials). Set the other settings in this table only with `egress.gateway_enabled: true`. Without it, the server doesn’t start if any of them is set.

[TABLE]

## MCP servers

See [MCP servers need an allowlist entry](managed-agents-self-hosted-differences.md#mcp-servers-need-an-allowlist-entry).

[TABLE]

## Git repositories

See [Git repositories need an allowlist entry](managed-agents-self-hosted-differences.md#git-repositories-need-an-allowlist-entry).

[TABLE]

These limits apply to Git repositories:

- **Protocols:** The server doesn’t support SSH or Git LFS, and it refuses redirects, such as the one for a renamed repository.
- **Tokens:** The Git host must accept the token as the password of HTTP Basic authentication, under the username `x-access-token`.
- **URLs:** A repository URL has one owner and one repository name, so you can’t use a repository in a GitLab subgroup.
- **Hosts:** For a URL on a host that `git.allowed_hostnames` doesn’t list, the server returns a `400`. The error message says that the URL must be on `github.com`, even if you list other hosts.
- **Pushes:** The server always refuses a push that deletes a branch, or that changes anything other than a branch, such as a tag.

## Web tools and skills

See [Web tools need a server setting](managed-agents-self-hosted-differences.md#web-tools-need-a-server-setting).

[TABLE]

## Limits, timeouts, and scheduling

[TABLE]

## Models and compaction

[TABLE]

### Model entries

Each entry of `models.settings` changes a model in the catalog or adds one. For a model in the catalog, a field that you leave out keeps its built-in value.

| Field | Description |
|----|----|
| `fast_supported` | Whether the model accepts `speed: "fast"`. Required for a model that you add. |
| `inference_geo_supported` | Whether the model accepts `inference_geo`. |
| `forced_tool_choice_supported` | Whether the model accepts a request that forces it to call one tool. The server sends such a request only to run a `web_search` or `web_fetch` call that was approved. With `false`, it never forces a tool on this model. |
| `effort_supported` | Whether the model accepts an effort level. |
| `effort_levels` | The effort levels that the model accepts, from `low`, `medium`, `high`, `xhigh`, and `max`. Required with `effort_supported: true` on a model with no built-in levels. |
| `effort_default` | The effort level of a session whose agent names none. It must be one of `effort_levels`. Required with `effort_supported: true` on a model with no built-in default. |
| `thinking` | The thinking mode that the server requests, `enabled` or `adaptive`. |
| `thinking_budget` | The thinking budget, in tokens, that the server sends with `thinking: enabled`. |
| `max_tokens` | The `max_tokens` value of each model call. |

## Console on your server

[TABLE]
