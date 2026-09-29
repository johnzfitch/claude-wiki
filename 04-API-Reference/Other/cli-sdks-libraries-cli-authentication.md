---
title: "CLI authentication options - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/cli-sdks-libraries/cli/authentication"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:38Z"
tags: ["api", "authentication", "cli"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fcli-sdks-libraries%2Fcli%2Fauthentication)





SearchCtrlK

CLI, SDKs, and libraries

[Overview](cli-sdks-libraries-overview.md)

ant CLI

[Quickstart](cli-sdks-libraries-cli-quickstart.md)[Authentication options](cli-sdks-libraries-cli-authentication.md)[Using the CLI](cli-sdks-libraries-cli-using.md)[Scripting and automation](cli-sdks-libraries-cli-scripting.md)[Manage resources as code](cli-sdks-libraries-cli-apply.md)[Connect to a Managed Agents session](cli-sdks-libraries-cli-sessions-connect.md)

Client SDKs

[Middleware](cli-sdks-libraries-middleware.md)[Python](cli-sdks-libraries-sdks-python.md)[TypeScript](cli-sdks-libraries-sdks-typescript.md)[C#](cli-sdks-libraries-sdks-csharp.md)[Go](cli-sdks-libraries-sdks-go.md)[Java](cli-sdks-libraries-sdks-java.md)[PHP](cli-sdks-libraries-sdks-php.md)[Ruby](cli-sdks-libraries-sdks-ruby.md)

Libraries and integrations

[Apple Foundation Models](cli-sdks-libraries-libraries-apple-foundation-models.md)[OpenAI SDK compatibility](cli-sdks-libraries-libraries-openai-sdk.md)

[Console](usage-limits.md)

[CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)ant CLI

# CLI authentication options

Copy page



Authenticate the ant CLI with interactive login, API keys, named profiles, and Workload Identity Federation.

Copy page



The `ant` CLI supports several credential sources. The [Quickstart](cli-sdks-libraries-cli-quickstart.md#authentication) covers the one-command happy path (`ant auth login`). This page covers every option in full.

## Interactive login

`ant auth login` lets you call the API without creating or managing an API key. It opens a browser-based OAuth flow against the Claude Console and stores the resulting credentials under `$ANTHROPIC_CONFIG_DIR` (see [Configuration directory](manage-claude-wif-reference.md#configuration-directory) for the OS-specific default). On a remote host or in any environment without a local browser, pass `--no-browser` to print the authorize URL and paste the returned code back into the terminal.

CLI



```python
ant auth login

# On a remote host without a browser:
ant auth login --no-browser

# Bind to a specific workspace and skip the browser picker:
ant auth login --workspace-id wrkspc_01...

# If the named profile you pass with --profile doesn't exist,
# a new named profile will be created with that name.
ant auth login --profile <profile-name>
```

During the browser flow, you select an organization and then a [workspace](manage-claude-workspaces.md). The issued token is [scoped to that workspace](manage-claude-workspaces.md#api-keys-and-resource-scoping), so the CLI can only see resources that belong to it. Pass `--workspace-id` to bind directly and skip the picker. To work in more than one workspace, see [Switch between workspaces](#switch-between-workspaces).

Interactive login is intended for local development and scripting on your own machine. For non-interactive workloads such as CI, servers, and containers, use [Workload Identity Federation](manage-claude-workload-identity-federation.md) instead.

Login writes credentials to `credentials/<profile>.json`. The first login for a profile also creates `configs/<profile>.json` and sets it as the active profile. To remove stored credentials, run `ant auth logout`, or `ant auth logout --all` to clear every profile.

## Admin access

By default, `ant auth login` requests a workspace-scoped token. To manage the resources documented on the [Admin API](manage-claude-admin-api.md) page, request the `org:admin` scope under a dedicated profile:

CLI



```python
ant auth login --profile admin --scope "org:admin"

# Print a bearer token for Authorization headers:
ant auth print-credentials --profile admin --access-token
```

The `org:admin` scope is granted only to organization members with the admin, owner, or primary owner role. The issued token has organization-wide access, and any workspace binding on the profile does not constrain it. Keep the admin profile separate from your day-to-day profile so routine commands never run with elevated access.

## API key

The CLI also reads your API key from the `ANTHROPIC_API_KEY` environment variable. Get a key from the [Claude Console](usage-limits.md).

zsh

bash

Windows

```python
echo 'export ANTHROPIC_API_KEY=sk-ant-api03-...' >> ~/.zshrc
source ~/.zshrc
```



To override the key for a single invocation, pass `--api-key`. To point at a different API host, set `ANTHROPIC_BASE_URL` or pass `--base-url`.

If you are using an API key scoped to multiple workspaces, such as a [personal or service account key](manage-claude-authentication.md#key-types), you must [specify the workspace](manage-claude-authentication.md#select-a-workspace) to run your command in. Do this by setting an `ANTHROPIC_WORKSPACE_ID` environment variable, which the CLI reads automatically, or by using the [`--workspace-id` flag](cli-sdks-libraries-cli-using.md#global-flags). The value must be a `wrkspc_...` ID; the literal `default` that the SDKs accept in `ANTHROPIC_WORKSPACE_ID` for [federated token exchange](manage-claude-wif-reference.md#environment-variables) isn't valid here.

CLI



```python
ant messages create \
  --workspace-id wrkspc_01... \
  --model claude-opus-5-5 \
  --max-tokens 1024 \
  --message '{role: user, content: "Hello, Claude"}'
```

## Check authentication status

`ant auth status` prints the credential source the CLI selected (API key environment variable, OAuth login, federation, or profile), the active profile, the workspace the active token is bound to, and the configuration directory paths. Use it to diagnose why a workload picked the wrong credential or workspace.

CLI



```python
ant auth status
```

``` inline-block
Active profile:  default
Config dir:      ~/.config/anthropic
Profile config:  ~/.config/anthropic/configs/default.json
Credentials:     ~/.config/anthropic/credentials/default.json

Credentials
  (active) * Profile (user_oauth) [via active_config]       sk-ant-oat01-EXA...
...

Workspace
  (active) * Workspace                                      wrkspc_01... (Engineering)
```



Read the `(active)` rows to see which credential source and workspace won. The command reports status rather than performing a health check, so don't script against the exit status. For the full ordering of credential sources, see [Credential precedence](manage-claude-wif-reference.md#credential-precedence).

## Switch between workspaces

An interactive-login token is bound to a single workspace. To use the CLI against more than one workspace, log in to each under its own named profile, then switch between them:

CLI



```python
# 1. Create the profile (interactive; pick the other workspace in the
#    browser, or pass --workspace-id to skip the picker):
# ant auth login --profile other-ws

# 2. Make it the default for subsequent commands:
ant profile activate other-ws

# 3. Or select it for a single command without changing the default:
ant --profile other-ws models list
ANTHROPIC_PROFILE=other-ws ant models list
```

Run [`ant auth status`](#check-authentication-status) to confirm which profile and workspace are active.



Profiles are only consulted when no API key is set. If `ANTHROPIC_API_KEY` is present in your environment, it overrides every profile and these commands all use that key's workspace (or, for a multi-workspace key, the workspace set with `ANTHROPIC_WORKSPACE_ID` or `--workspace-id`). Unset it before switching profiles.

## Manage profiles

The `ant profile` subcommands inspect and edit profile state directly:

CLI



```python
ant profile list
ant profile get --profile other-ws
ant profile set workspace_id wrkspc_01... --profile other-ws
```

The writable keys for `ant profile set` are `workspace_id`, `base_url`, `organization_id`, `scope`, `client_id`, and `console_url`. Setting `workspace_id` records the target workspace in the profile config but does not rebind credentials that were already issued; run `ant auth login` again under that profile to mint a token for the new workspace.

For the profile file schema and the federation block, see [Profile configuration file](manage-claude-wif-reference.md#profile-configuration-file). For Workload Identity Federation, see the [Authentication overview](manage-claude-authentication.md) and the [WIF reference](manage-claude-wif-reference.md).

## Next steps



[Using the CLI](cli-sdks-libraries-cli-using.md)

Command structure, output formats, GJSON transforms, and request bodies



[CLI scripting and automation](cli-sdks-libraries-cli-scripting.md)

Version-control API resources, scripting patterns, and use from Claude Code



[Workload Identity Federation](manage-claude-workload-identity-federation.md)

Non-interactive authentication for CI, servers, and containers
