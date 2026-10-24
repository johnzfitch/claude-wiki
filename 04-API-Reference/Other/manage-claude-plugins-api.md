---
title: "Plugins API - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/plugins-api"
category: "04-API-Reference/Other"
fetched_at: "2026-10-17T06:26:29Z"
tags: ["api", "plugins"]
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


[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fplugins-api)





SearchCtrlK

Organization

[Admin API](manage-claude-admin-api.md)[User management](manage-claude-user-management.md)[Plugins API](manage-claude-plugins-api.md)[Workspaces](manage-claude-workspaces.md)

Authentication

[Overview](manage-claude-authentication.md)[Create an Admin API key](manage-claude-admin-api-keys.md)[App Attest](manage-claude-app-attest.md)[Workload Identity Federation](manage-claude-workload-identity-federation.md)[Manage WIF via API](manage-claude-wif-admin-api.md)[WIF reference](manage-claude-wif-reference.md)

Identity providers

Monitoring

[Usage and Cost API](manage-claude-usage-cost-api.md)[Rate Limits API](manage-claude-rate-limits-api.md)[Analytics APIs](manage-claude-analytics-api.md)[Claude Code Analytics API](manage-claude-claude-code-analytics-api.md)[Spend Limits API](manage-claude-spend-limits-api.md)

[OpenTelemetry](manage-claude-opentelemetry.md)

Data & compliance

[Data residency](manage-claude-data-residency.md)[API and data retention](manage-claude-api-and-data-retention.md)

[Access Transparency](manage-claude-access-transparency.md)

[Encryption keys (CMEK)](manage-claude-cmek.md)

[Inference hooks](manage-claude-inference-hooks.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](playground.md)

[Admin](manage-claude-admin-api.md)Organization

# Plugins API

Copy page



Inventory and manage the plugins in your Claude Enterprise organization: upload plugins and versions, choose the version members are served, control who can use each plugin, download plugin files for review, and validate a marketplace before you connect it.

Copy page



The Plugins API lets you inventory every plugin in your Claude Enterprise organization, publish plugins and new versions from your own pipelines, choose which version members are served, control who can use each plugin, download plugin files for review, and check a Git marketplace before you connect it.

For plugin *usage* reporting (which plugins and skills members use, and how often), see [Analytics APIs](manage-claude-analytics-api.md).



**Scoped Admin API key required**

These endpoints require an Admin API key with the `read:plugins` scope (for `GET` endpoints, including archive downloads) or the `write:plugins` scope (for `POST` and `DELETE` endpoints, except marketplace validation, which either scope allows); [Scopes](#scopes) has the details, including two other read scopes that also work. See [Create an Admin API key](manage-claude-admin-api-keys.md#create-a-key-for-a-claude-enterprise-organization) for where your primary owner creates one. Pass the key in the `x-api-key` header on every request, together with the [`anthropic-version`](../Endpoints/versioning.md) header and the beta header shown in the following note.



The Plugins API is in **beta** and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

Every request must include the [beta header](../Endpoints/beta-headers.md) `anthropic-beta: ce-plugins-2026-09-01` (the SDKs and the `ant` CLI send it for you). A request without it returns `404`, exactly as if the endpoint did not exist.

## Endpoints

The API exposes 18 endpoints across five resources:

[TABLE]

This release does not include standalone skills (skills a member writes in the skills editor or uploads as a single skill in claude.ai). They do not appear in the inventory and cannot be created here. Plugins that Anthropic publishes are not inventoried either; their usage is reported by the [Analytics APIs](manage-claude-analytics-api.md). Marketplaces are created, connected to repositories, and deleted in claude.ai, not through this API.

## Prerequisites

- Your organization must be on a Claude Enterprise plan.
- Your primary owner creates an Admin API key with the `read:plugins` scope, the `write:plugins` scope, or both in [claude.ai \> Organization settings \> API](https://claude.ai/admin-settings/api-access). See [Create an Admin API key](manage-claude-admin-api-keys.md#create-a-key-for-a-claude-enterprise-organization).
- Every request carries three headers: `x-api-key`, `anthropic-version: 2023-06-01`, and `anthropic-beta: ce-plugins-2026-09-01`.

The Python, TypeScript, C#, Go, Java, PHP, and Ruby SDKs expose these endpoints under `client.beta.organization`, and the [`ant` CLI](cli-sdks-libraries-cli-quickstart.md) under `ant beta:organization`; they send the `anthropic-version` and `anthropic-beta` headers for you. The examples on this page use each SDK's default client, which, like the CLI, reads the Admin API key from the `ANTHROPIC_API_KEY` environment variable; the curl examples read the key from the same variable and pass it in the `x-api-key` header. Where an SDK or the CLI fetches more pages for you, `limit` sets the page size, not the total (see [Pagination](#pagination)).

API keys belong to the organization and keep working after the person who created them leaves. Do not share them or check them into source control.

## Quick start

List the plugins in your organization's own marketplaces, newest first:

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
client = anthropic.Anthropic()

plugins = client.beta.organization.plugins.list(owner_type="organization", limit=20)

# Automatically fetches more pages as needed.
for plugin in plugins:
    print(f"{plugin.id}: {plugin.name}")
```

```python
{
  "data": [
    {
      "type": "plugin",
      "id": "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
      "name": "sales-toolkit",
      "display_name": "Sales Toolkit",
      "description": "Account research and call prep for the sales team.",
      "served_version_id": "pluginver_01Km7tL4pR9xF5sU2zV3jP6q",
      "served_version_pinned": true,
      "latest_version_id": "pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p",
      "manifest_version": "1.4.0",
      "owner": { "type": "organization" },
      "marketplace_id": "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r",
      "created_by": { "type": "api_actor", "api_key_id": "apikey_01Nq9vN6rT2zH7uW4bX5mR8s" },
      "organization_installation_preference": "available",
      "organization_installation_preference_inherited": true,
      "content_scan": { "status": "completed", "assessment": "pass", "reason": null },
      "components": [
        {
          "type": "skill",
          "name": "account-research",
          "description": "Researches a customer account before a call."
        },
        { "type": "mcp_server", "name": "crm", "description": null }
      ],
      "reach": "remote",
      "created_at": "2026-09-01T17:04:11Z",
      "updated_at": "2026-09-15T14:12:30Z"
    }
  ],
  "next_page": "page_xK9f2LqT7vNw3pRzBd8sHy"
}
```



In this example the plugin is pinned to an earlier version: a newer version (`latest_version_id`) is stored but not yet served.

## Scopes

| Scope                      | Grants                                                                                                                                                                                                                                                                                                                   |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `read:plugins`             | Every `GET` endpoint on this page, including archive downloads, plus marketplace validation.                                                                                                                                                                                                                             |
| `write:plugins`            | Every `POST` and `DELETE` endpoint on this page: create a plugin, create a version, change the served version, delete a plugin, set and remove installation settings, and set a marketplace's default, plus marketplace validation. It does not grant reads.                                                             |
| `read:org_audit`           | A read-only scope for security-audit integrations: every `GET` endpoint on this page, including archive downloads, plus the [user management](manage-claude-user-management.md) and [Compliance API](manage-claude-compliance-api.md) read endpoints. It does not grant marketplace validation or any write. |
| `read:compliance_org_data` | The Compliance API's scope for organization metadata (names, types, roles, and groups) and effective settings. Grants every `GET` endpoint on this page, exactly as `read:org_audit` does, so a Compliance Access Key can read plugins without a second key. It does not grant marketplace validation or any write.      |

A key can carry several scopes. An integration that uploads a plugin and then reads it back needs both `read:plugins` and `write:plugins`. Wherever this page says an endpoint requires the `read:plugins` scope, a key with `read:org_audit` or `read:compliance_org_data` works too.

### Access to members' plugin files

Each of these read scopes (`read:plugins`, `read:org_audit`, and `read:compliance_org_data`) can download the files of plugins in members' personal marketplaces, including files that claude.ai's admin settings do not show, and a `read:org_audit` or `read:compliance_org_data` key bound to your parent organization can do this in any organization under it that has access to this API, by passing `organization_id` (see [Reading another organization under the same parent](#reading-another-organization-under-the-same-parent)). Each such download records a `claude_plugin_archive_accessed` event on the [Compliance API Activity Feed](manage-claude-compliance-activity-feed.md), identifying the key, the plugin, the version, and the member (see [Activity Feed events](#activity-feed-events)). Downloads of organization-owned plugins are not recorded.

### Reading another organization under the same parent

`read:plugins` and `write:plugins` keys read and write only the organization they were created in. If your company has several Claude organizations linked under one parent organization, a `read:org_audit` or `read:compliance_org_data` key that the parent's primary owner created for all linked organizations (see [Create an Admin API key](manage-claude-admin-api-keys.md#create-a-key-for-a-claude-enterprise-organization)) can also read any of them that has access to this API: pass that organization's ID in the `organization_id` query parameter on any `GET` endpoint on this page. The ID is the organization UUID shown in claude.ai's settings (its `org_`-prefixed form is accepted too). Without the parameter, the key reads the organization it was created in. A `404` means the named organization is not under the key's parent or the API is not available to it; a value that is not a UUID or `org_` ID returns `400`. Any other key that names an organization other than its own gets `404`. Writes do not accept `organization_id`.

## Key concepts

### Plugins and components

A **plugin** is a package that extends Claude for your organization's members. It contains any combination of these components:

| Component  | What it is                                                                                               |
|------------|----------------------------------------------------------------------------------------------------------|
| Skill      | Instructions and files that Claude loads when a task calls for it.                                       |
| Command    | A saved prompt a member runs by typing `/` followed by the command's name.                               |
| Agent      | A helper assistant with its own instructions, to which Claude can hand part of a task.                   |
| Hook       | A command that runs automatically when an event happens in a session, such as before Claude uses a tool. |
| MCP server | A connection from Claude to tools and data in another system (Model Context Protocol).                   |
| CLI        | A command-line program that the plugin lets Claude run.                                                  |

Every plugin has a manifest at `.claude-plugin/plugin.json`. The manifest's `name` becomes the plugin's `name`: a lowercase identifier that is unique within its marketplace.

### Marketplaces

A **marketplace** is a container of plugins. Each marketplace has an owner and a source.

- **Owner.** The organization owns its marketplaces. Each member can also have personal marketplaces.
- **Source.** `manual` means plugins are uploaded, in claude.ai or, for an organization marketplace, through this API. `github`, `gitlab`, and `public_git` mean plugins are synchronized from a Git repository the owner connected. Nothing can be uploaded to a synchronized marketplace, and this API cannot delete its plugins, because the next synchronization would undo either change. Change the repository instead.

Your organization's **library marketplace** is the organization-owned `manual` marketplace that uploads go to when you do not name a marketplace. It is created the first time something is uploaded to it.

### Organization-owned and member-owned plugins

A plugin's `owner.type` says whose marketplace it lives in:

- `organization`: you can manage it through this API, except that a plugin in a marketplace synchronized from Git cannot receive uploads or be deleted here.
- `user`: it lives in one member's personal marketplace. You can read its details and download its files, and delete it if its marketplace is `manual`. Uploading versions and choosing the served version return `403`. Sharing is managed only by the member, in claude.ai.

Removing a member from the organization does not remove their plugins. They stay in the inventory under the member's `user_id`, and the `owner_user_id` filter still finds them, so you can review and remove a departed member's content. They are removed from the inventory when the member's account is deleted.

### Versions and the served version

Every upload creates a new, immutable **version**, whether it comes from this API, from claude.ai, or from a Git synchronization. A plugin has two pointers to its versions:

- `latest_version_id`: the newest version.
- `served_version_id`: the version members are served.

By default `served_version_pinned` is `false`: the served version normally follows the newest one. When content scanning is on, a version saved in claude.ai might **wait** for its content scan: it is stored but not served at once. This page uses "wait" only for a version saved in claude.ai, not for one that a member or an administrator publishes into a plugin. While scanning is on, a waiting version is served only after its scan completes with `pass` or `warn`. While a version waits, `served_version_id` names an earlier version than `latest_version_id`. Do not poll until the two IDs match: they might stay different, for example when the scan fails.

Choosing a version with `POST /v1/organizations/plugins/{plugin_id}` **pins** the plugin (`served_version_pinned: true`). So does an administrator choosing a version in claude.ai, or accepting a member's request to publish into the plugin. From then on, new uploads are stored and advance `latest_version_id`, but members keep the pinned version until you point `served_version_id` at another one. A plugin whose two pointers differ has a stored version that is not being served.

This lets a release pipeline upload each build, test it, and then promote it. To have your pipeline decide when each build is served, pin the plugin once by setting `served_version_id` to its current version; from then on, promote each build you want served. With content scanning on, that first pin returns `409 scan_pending` until the current version's scan completes, and `400 scan_failed` if the scan completed with `fail` or `unknown`, or errored (`warn` is accepted). A pinned plugin cannot currently be unpinned, here or in claude.ai.

To roll back, set `served_version_id` to an earlier version. Roll forward the same way.

These rules describe organization-owned plugins. A member-owned plugin's served version is controlled by its owner in claude.ai.

### Installation settings

**Installation settings** decide who can use an organization-owned plugin. Each setting has one of four values, carried in the fields named `installation_preference` (and, on the plugin and marketplace objects, `organization_installation_preference` and `default_installation_preference`):

| Value           | Members see                                    |
|-----------------|------------------------------------------------|
| `required`      | The plugin is installed and cannot be removed. |
| `auto_install`  | The plugin is installed and can be removed.    |
| `available`     | The plugin can be installed on request.        |
| `not_available` | The plugin is hidden.                          |

A plugin can hold an organization-wide setting and one setting per group (the role-based access control groups managed in [User management](manage-claude-user-management.md#groups)). A member gets a value by these rules:

1.  The organization-wide value is the plugin's own organization-wide setting if it has one, otherwise its marketplace's default, otherwise `not_available`. The plugin reports this value in `organization_installation_preference`, with `organization_installation_preference_inherited: true` while it comes from the marketplace default.
2.  A member who belongs to no group holding a setting for the plugin gets the organization-wide value.
3.  A member who belongs to one or more groups holding a setting gets the most permissive of those groups' settings instead, ranked `required`, `auto_install`, `available`, `not_available`.

A group's setting replaces the organization-wide value for its members; it does not add to it. For example, if the organization-wide value is `required` and the Pilot group holds `available`, Pilot members get `available`. When you move a plugin from a pilot group to the whole organization, set the organization-wide value and then remove the group's setting. Setting the organization-wide value stops the plugin from inheriting its marketplace default; [removing the organization-wide setting](#remove-an-installation-setting) returns the plugin to that default.

A plugin created through this API starts with no settings of its own, so it inherits its marketplace's default: `not_available` unless someone has set a default. Deleting a group removes its settings from every plugin.

### Shares

**Shares** decide who can use a member-owned plugin. The owner shares it in claude.ai with every member, with a group, or with named members. This API lists shares but cannot change them.

If your organization has turned off a kind of sharing in its claude.ai settings, shares of that kind still appear in the list but give no one access while that setting is off; the list itself does not show whether it is.

### Content scanning

Content scanning is an organization setting in claude.ai. When it is on, newly stored versions are scanned (claude.ai exempts a few) and the result is reported in `content_scan`; a version that was not scanned, for example one stored before scanning was turned on, has `content_scan: null`. Scanning is not offered to organizations that use customer-managed encryption keys or zero data retention.

While scanning is on, members are served a plugin only when its served version's scan is `completed` with `pass` or `warn`. While the scan runs, or after it fails, errors, or reaches no verdict, the plugin is withheld from members, and an earlier version is not served in its place. A version that was never scanned (`content_scan: null`) is served normally.

A version you upload through this API never waits for its content scan. When it becomes the served version, members lose the plugin until its scan passes, and stay without it if the scan fails. If members should keep the current version while a new one is scanned, pin the plugin first (see [Versions and the served version](#versions-and-the-served-version)).

While a version saved in claude.ai waits for its scan, the served version does not change. When your API upload becomes the served version, any wait ends: the waiting version is served only if someone chooses it. To see a waiting version's scan, read the version (see [List a plugin's versions](#list-a-plugins-versions)).

After an upload, `content_scan.status` is `processing` and the verdict arrives asynchronously. Read the version to see it; the plugin object shows only its served version's scan. Changing the served version to a version whose scan is still running returns `409 scan_pending`; to one whose scan failed, `400 scan_failed`.

### Reach

`reach` summarizes, in one value, how far a version reaches on members' machines and beyond:

| Value        | Meaning                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `remote`     | Declares an MCP server or a CLI, whatever else it declares.                                                                                                                                                                                                                                                                                                                                       |
| `privileged` | Declares no MCP server or CLI, but declares a hook, a monitor (a background command that keeps running during a session), an LSP (Language Server Protocol) server, or settings the plugin applies to the member's app, or contains a skill, command, or any other Markdown file whose frontmatter pre-approves tools (`allowed-tools`). These run, or take effect, on the member's own computer. |
| `contained`  | Declares no MCP server, CLI, hook, monitor, LSP server, or app settings, and none of its Markdown files pre-approves tools (for example, a plugin that holds only skills, commands, and agents, none with `allowed-tools`).                                                                                                                                                                       |

`reach` counts everything the version declares, including monitors, LSP servers, and app settings, which `components` does not list, so a version with an empty `components` list can still be `privileged`. It is `null` for a version stored before components were recorded, and for a version whose reach could not be determined because the `SKILL.md` of one of its skills, or one of its command files, could not be read; treat `null` as unclassified.

### Upload requirements

Uploads follow the same rules as plugin uploads in claude.ai, so the same archives are accepted in both places.

- The upload is either one `.zip` or `.plugin` archive, or a set of individual files. An archive may wrap everything in one top-level folder.
- It must contain exactly one manifest, at `.claude-plugin/plugin.json`, which must declare a `name`. A bare `SKILL.md` without a manifest is rejected.
- A top-level `SKILL.md` whose frontmatter declares plugin components is merged into the manifest; `plugin.json` wins wherever both set a value.
- `name` may contain lowercase letters (from any alphabet), digits, and hyphens, up to 64 characters. Uppercase letters, spaces, underscores, and other punctuation are rejected.
- `displayName` is at most 64 characters and `description` at most 500.
- Every `SKILL.md` needs valid YAML frontmatter with a `name` and `description`, neither containing XML tags such as `<example>`. Two skills, or two commands, cannot share a name.
- No file may be under a top-level `bin/` directory.
- No nested `.zip` files. Packaged MCP servers (`.mcpb`, `.dxt`) are allowed.
- File paths must be relative, contain no `..`, and use only letters, digits, spaces, and `_ . - / ( ) ,`.
- The request body and the uncompressed archive are each at most 200 MB; a request body over the limit returns `413` (`request_too_large`) rather than `400`. An upload has at most 5,000 files, a path depth of 12, paths of 472 characters, and file or folder names of 255 characters.
- ZIP archives must use DEFLATE or STORE compression, and cannot be encrypted or contain symbolic links.
- A marketplace holds at most 500 items, counting its plugins and any standalone skills members keep in it. This limit and the 5,000-file limit are current values that may be raised.

## Example workflows

### Publish each build from a release pipeline

Upload every tagged build from CI, and let the pipeline decide when a build is served.

1.  Find the marketplace to upload into with `GET /v1/organizations/plugin_marketplaces?owner_type=organization`, or omit `marketplace_id` to use the library marketplace.
2.  On the first release, [create the plugin](#create-a-plugin) with `POST /v1/organizations/plugins`. On every later release, record the plugin's `latest_version_id`, then [upload a version](#create-a-version) with `POST /v1/organizations/plugins/{plugin_id}/versions`. If the upload's response is lost, read the plugin and retry only if `latest_version_id` is unchanged (see [Retrying uploads](#retrying-uploads)).
3.  To keep members on the current version while each new build is checked, pin the plugin once by setting `served_version_id` to its current version. From then on each upload is stored without being served, and the pin cannot be undone: every build you want served needs step 5.
4.  When content scanning is on, poll `GET /v1/organizations/plugins/{plugin_id}/versions/{version}` until `content_scan.status` is no longer `processing`, and promote only when it is `completed` with `pass` or `warn`.
5.  [Promote the build](#change-the-served-version) with `POST /v1/organizations/plugins/{plugin_id}` and `{"served_version_id": "<the new version's ID>"}`. To roll back, send the previous version's ID the same way.

### Roll a plugin out to a pilot group, then to everyone

1.  Look up the pilot group's ID with `GET /v1/organizations/rbac_groups`. That call needs the `read:rbac_groups` scope, which requires a key created for all linked organizations (see [User management](manage-claude-user-management.md#groups)). The next steps need `write:plugins`, which acts only on the organization its key was created in, so in an enterprise with several linked organizations, create this key in the organization that holds the plugin and give it both scopes, or use a second key created there for those steps.

2.  [Give the group its own setting](#set-an-installation-setting), for example `auto_install`, with `POST /v1/organizations/plugins/{plugin_id}/installation_settings/{target}`, where `{target}` is the group's `rbac_group_` ID, while the organization-wide value stays `not_available`. Only the group's members get the plugin.

3.  When the pilot ends, set the organization-wide value with the following call, then remove the group's setting so the group follows the organization again. Setting the organization-wide value stops the plugin from inheriting its marketplace default; [removing the organization-wide setting](#remove-an-installation-setting) later returns the plugin to that default.

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

    ``` shiki
    client = anthropic.Anthropic()

    setting = client.beta.organization.plugins.installation_settings.set(
        "organization",
        plugin_id="plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
        installation_preference="required",
    )

    print(f"plugin_id: {setting.plugin_id}")
    print(f"installation_preference: {setting.installation_preference}")
    ```

    Then remove the group's setting with `DELETE /v1/organizations/plugins/{plugin_id}/installation_settings/{target}`, where `{target}` is the group's ID. A group's setting replaces the organization-wide value for its members rather than adding to it, so a leftover group setting of `available` would keep those members on `available`.

### Keep a security inventory in sync

Run a nightly job that flags plugins reaching outside the member's session or failing their content scan.

1.  Page through [`GET /v1/organizations/plugins?limit=100`](#list-plugins) until `next_page` is `null` (see [Pagination](#pagination)). Read each plugin's `reach` and `content_scan` from that list on every run: a scan verdict that arrives later does not move `updated_at`. `updated_at` normally tells you which plugins have new content or a new served version since the last run (worth a fresh archive download). A waiting version (see [Versions and the served version](#versions-and-the-served-version)) moves `updated_at` when it becomes the served version, not necessarily when it is stored. To notice one, compare `latest_version_id` with the value from your last run. The full re-list is also what catches removals, because a plugin removed by a Git synchronization or an account deletion disappears without an event.
2.  Flag each plugin whose `reach` is `remote` (it declares an MCP server or a CLI), or whose `content_scan.assessment` is `fail` or `unknown`. These fields describe the served version. To also check a newer version that is not served, list the plugin's versions when `latest_version_id` differs from `served_version_id` (see [List a plugin's versions](#list-a-plugins-versions)).
3.  For each flagged plugin, download the served version's archive for review with `GET /v1/organizations/plugins/{plugin_id}/versions/{served_version_id}/content` (see [Download a version's files](#download-a-versions-files)). Also download any unserved version that meets step 2's test, by its ID.
4.  To take a plugin away from members while you review it, see [Delete a plugin](#delete-a-plugin) for the reversible (organization-owned) and permanent options.

## Plugins

The plugin object describes a plugin in one of your organization's marketplaces or in a member's personal marketplace (the [Quick start](#quick-start) response shows a complete one). Its `display_name`, `description`, `manifest_version`, `content_scan`, `components`, and `reach` describe its **served** version, so one list call shows what members are being served.

| Field                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                                                                                     | Prefixed `plugin_`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `name`                                                                                   | From the manifest. Unique within its marketplace, not across the organization. Fixed for an organization-owned plugin; changes if a member renames their own plugin in claude.ai.                                                                                                                                                                                                                                                                                                                                                                               |
| `display_name`, `description`, `manifest_version`                                        | The served version's manifest `displayName`, `description`, and `version`; each is `null` when the manifest declares none. `manifest_version` is normalized for display: one leading `v` or `V` is dropped, so a manifest `version` of `"v1.4.0"` is returned as `"1.4.0"`. It is also `null` for a value that does not look like a version number, such as `"latest"`, and for a plugin version created before claude.ai began recording this field in August 2026. An upload is never refused because of its `version`, and `manifest_version` is not unique. |
| `served_version_id`, `latest_version_id`                                                 | Prefixed `pluginver_`: the version members are served, and the newest version. See [Versions and the served version](#versions-and-the-served-version).                                                                                                                                                                                                                                                                                                                                                                                                         |
| `served_version_pinned`                                                                  | `false` until the plugin is pinned (see [Versions and the served version](#versions-and-the-served-version)); `true` from then on.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `owner`                                                                                  | `{"type": "organization"}`, or `{"type": "user", "user_id": "user_..."}` for a member's personal marketplace.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `marketplace_id`                                                                         | Prefixed `marketplace_`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `created_by`                                                                             | Who created the plugin: `{"type": "user_actor", "user_id": "user_...", "email_address": "..."}` for a person in claude.ai (`email_address` may be `null`), or `{"type": "api_actor", "api_key_id": "apikey_..."}` for an API key. Other actor types may appear. `null` when no creator is recorded, such as for plugins synchronized from Git.                                                                                                                                                                                                                  |
| `organization_installation_preference`, `organization_installation_preference_inherited` | Organization-owned: the organization-wide value, and whether it comes from the marketplace's default (see [Installation settings](#installation-settings)). Member-owned: both `null`.                                                                                                                                                                                                                                                                                                                                                                          |
| `content_scan`                                                                           | The served version's scan result, an object with `status`, `assessment`, and `reason` (described after this table). `null` when it was never scanned.                                                                                                                                                                                                                                                                                                                                                                                                           |
| `components`                                                                             | The served version's components, each `{"type", "name", "description"}` with `type` one of `skill`, `mcp_server`, `command`, `agent`, `hook`, or `cli`, listed in that type order and then by name. For an MCP server, `name` is its key in the manifest; for a hook, the event it runs on; for a CLI, the executable's name. `description` is always `null` for MCP servers, hooks, and CLIs. `null` when not recorded.                                                                                                                                        |
| `reach`                                                                                  | `contained`, `privileged`, or `remote`. See [Reach](#reach).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `updated_at`                                                                             | Changes when the served version changes, when the plugin becomes pinned, and normally when a new version is stored. A waiting version (see [Versions and the served version](#versions-and-the-served-version)) changes it when it becomes the served version, not necessarily when it is stored. It does not change for installation settings, shares, or new scan results.                                                                                                                                                                                    |

The `content_scan` object:

| Field        | Description                                                                                                                                                                                                                                                                                                                                                        |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `status`     | `processing` while the scan runs, `completed` when it finished, or `errored` when it could not finish (or, occasionally, when its result could not be read for this response, in which case a later read may report it). Members are not served a version whose scan is `processing` or `errored`; uploading the content again as a new version gets a fresh scan. |
| `assessment` | Set when `status` is `completed`: `pass` (nothing found), `warn` (something found that does not block use), `fail` (something found that blocks use), or `unknown` (no verdict). Otherwise `null`.                                                                                                                                                                 |
| `reason`     | For `warn` and `fail`, the main concern, from the following list. Otherwise `null`, and also `null` on an older scan that predates reason recording.                                                                                                                                                                                                               |

### Content scan reason values

| `reason`                          | Meaning                                                                                                                       |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `covert-usage-telemetry`          | Tells Claude to send information about the member or their usage to an outside address without telling them.                  |
| `undisclosed-data-destination`    | Sends files, emails, documents, or other content to a fixed outside destination the member is not shown and does not control. |
| `remote-code-instruction-loader`  | Tells Claude to download and run, or follow instructions from, outside content that can change after the plugin is installed. |
| `credential-exposure`             | Contains live credentials, or collects credentials or tokens from the member's environment.                                   |
| `guardrail-tampering`             | Weakens the member's safeguards, for example by pre-approving every permission prompt.                                        |
| `system-prompt-spoofing`          | Imitates or tries to replace Claude's system instructions.                                                                    |
| `covert-record-tampering`         | Quietly changes, hides, or deletes information the member would otherwise see.                                                |
| `covert-behavior-override`        | Changes Claude's behavior beyond the plugin's purpose and hides the change from the member.                                   |
| `hidden-code-execution`           | Runs bundled code while telling Claude not to reveal what it does.                                                            |
| `undisclosed-promotion-injection` | Inserts undisclosed promotional content into Claude's output.                                                                 |
| `hidden-identity-gate`            | Changes or stops its behavior depending on which account runs it, without saying why.                                         |
| `destructive-persistence`         | Can delete or corrupt the member's files, or install programs that remain after the plugin.                                   |
| `unanalyzable-binary`             | Includes a compiled or unreadable program, so the scan could not verify what it does.                                         |
| `other`                           | Any other concern, including one newer than this list.                                                                        |

A `plugin_id` that lacks the `plugin_` prefix returns `400`. A `plugin_id` that carries the prefix but does not resolve, belongs to another organization, or refers to a standalone skill returns `404`.

### List plugins

`GET /v1/organizations/plugins` lists every plugin in your organization, in the organization's marketplaces and in members' personal marketplaces, ordered by `created_at` descending. Filter by `owner_type` (`organization` or `user`), `owner_user_id` (prefixed `user_`; a member's plugins, including after the member leaves the organization), `marketplace_id`, and `created_at[gte]`, `created_at[gt]`, `created_at[lte]`, `created_at[lt]` (RFC 3339 timestamps). Filters combine with AND. A `marketplace_id` or `owner_user_id` that matches nothing in your organization returns an empty page, not an error. The response has the shape shown in [Quick start](#quick-start). Requires the `read:plugins` scope.

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
client = anthropic.Anthropic()

plugins = client.beta.organization.plugins.list(owner_type="organization", limit=20)

# Automatically fetches more pages as needed.
for plugin in plugins:
    print(f"{plugin.id}: {plugin.name}")
```

### Create a plugin

`POST /v1/organizations/plugins` creates an organization-owned plugin and its first version in one call; the version becomes the served version. The body is `multipart/form-data`: `files[]` is either one `.zip` or `.plugin` archive, or one part per file, where each part's filename is the file's path within the plugin (for example `.claude-plugin/plugin.json`). Optional fields are `marketplace_id` (an organization-owned `manual` marketplace; defaults to your library marketplace, which is created on first use) and `release_notes` (up to 5,000 characters, shown in claude.ai's version history and returned on the version). The plugin's `name`, `display_name`, `description`, and `manifest_version` come from the uploaded manifest, and the upload must meet the [upload requirements](#upload-requirements). When content scanning is on, the response's `content_scan.status` is `processing` and the verdict arrives asynchronously. Returns the plugin. Requires the `write:plugins` scope.

Upload an archive:

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
client = anthropic.Anthropic()

with open("dist/sales-toolkit.zip", "rb") as archive:
    plugin = client.beta.organization.plugins.create(
        files=[archive],
        release_notes="First release",
    )

print(f"id: {plugin.id}")
print(f"served_version_id: {plugin.served_version_id}")
```

```python
{
  "type": "plugin",
  "id": "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  "name": "sales-toolkit",
  "display_name": "Sales Toolkit",
  "description": "Account research and call prep for the sales team.",
  "served_version_id": "pluginver_01Km7tL4pR9xF5sU2zV3jP6q",
  "served_version_pinned": false,
  "latest_version_id": "pluginver_01Km7tL4pR9xF5sU2zV3jP6q",
  "manifest_version": "1.4.0",
  "owner": { "type": "organization" },
  "marketplace_id": "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r",
  "created_by": { "type": "api_actor", "api_key_id": "apikey_01Nq9vN6rT2zH7uW4bX5mR8s" },
  "organization_installation_preference": "available",
  "organization_installation_preference_inherited": true,
  "content_scan": { "status": "processing", "assessment": null, "reason": null },
  "components": [
    {
      "type": "skill",
      "name": "account-research",
      "description": "Researches a customer account before a call."
    },
    { "type": "mcp_server", "name": "crm", "description": null }
  ],
  "reach": "remote",
  "created_at": "2026-09-01T17:04:11Z",
  "updated_at": "2026-09-01T17:04:11Z"
}
```



Upload individual files into a named marketplace. Attach each file under its path within the plugin (the `;filename=` suffix in the cURL example, the filename arguments in the SDK examples); a file sent under its base name alone means the manifest is not found. The TypeScript and Java SDKs and the `ant` CLI cannot yet attach files under a path, so those examples upload the plugin as one archive into the marketplace instead:

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
client = anthropic.Anthropic()

# A (filename, file) tuple keeps each file's path within the plugin;
# a bare file object would be sent under its base name only.
with (
    open(".claude-plugin/plugin.json", "rb") as manifest,
    open("skills/account-research/SKILL.md", "rb") as skill_md,
):
    plugin = client.beta.organization.plugins.create(
        files=[
            (".claude-plugin/plugin.json", manifest),
            ("skills/account-research/SKILL.md", skill_md),
        ],
        marketplace_id="marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r",
    )

print(f"id: {plugin.id}")
print(f"served_version_id: {plugin.served_version_id}")
```

Besides a `400` for an upload that breaks the [upload requirements](#upload-requirements) (`413` for a request body over 200 MB) and the shared responses (a `403` when `marketplace_id` is a member's personal marketplace; see [Error responses](#error-responses)), a create can fail with:

| Status                     | Cause                                                                                                    | What to do                                                                                                            |
|----------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 404                        | `marketplace_id` is not a marketplace of your organization.                                              | Take the ID from [List marketplaces](#list-marketplaces).                                                             |
| 400                        | The marketplace is synchronized from Git, or already holds 500 plugins and skills.                       | Upload to a `manual` marketplace, or change the repository instead.                                                   |
| 409 `plugin_name_taken`    | The name is taken in that marketplace.                                                                   | Continue with `details.plugin_id` (upload a version to it), or change the manifest `name`.                            |
| 409 `skill_name_taken`     | The plugin is going into the library marketplace and one of its skills has an organization skill's name. | Rename the skill, or remove the organization skill in claude.ai.                                                      |
| 409 (no `error_code`)      | Another upload with the same name to the same marketplace is still in progress.                          | Retry shortly.                                                                                                        |
| 503 `registration_pending` | The plugin was created but its registration did not complete.                                            | Do not resend; upload the same files as a version of `details.plugin_id` (see [Retrying uploads](#retrying-uploads)). |

### Get a plugin

`GET /v1/organizations/plugins/{plugin_id}` returns one plugin. Requires the `read:plugins` scope.

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
client = anthropic.Anthropic()

plugin = client.beta.organization.plugins.retrieve("plugin_01Hq3vX8kZcN2mB7pR4tY9wL")

print(f"id: {plugin.id}")
print(f"name: {plugin.name}")
```

### Change the served version

`POST /v1/organizations/plugins/{plugin_id}` changes which version of an organization-owned plugin members are served. Pass an earlier version to roll back, or a newer one to promote a build that was stored without being served. This pins the plugin, and a pinned plugin cannot currently be unpinned, here or in claude.ai (see [Versions and the served version](#versions-and-the-served-version)). The only updatable field is `served_version_id`, and it is required. The change reaches members before the response returns and does not create a version. When content scanning is on, the version must be one members can be served (see [Content scanning](#content-scanning)). Passing the version already served on a pinned plugin changes nothing; passing it on an unpinned plugin pins it there, so later uploads stop being served automatically. Pinning also ends any wait: a version that was waiting for its content scan stays stored, and is served only if someone chooses it. Returns the plugin. Requires the `write:plugins` scope.

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
client = anthropic.Anthropic()

plugin = client.beta.organization.plugins.update(
    "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
    served_version_id="pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p",
)

print(f"id: {plugin.id}")
print(f"served_version_id: {plugin.served_version_id}")
```

```python
{
  "type": "plugin",
  "id": "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  "name": "sales-toolkit",
  "display_name": "Sales Toolkit",
  "description": "Account research and call prep for the sales team.",
  "served_version_id": "pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p",
  "served_version_pinned": true,
  "latest_version_id": "pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p",
  "manifest_version": "1.5.0",
  "owner": { "type": "organization" },
  "marketplace_id": "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r",
  "created_by": { "type": "api_actor", "api_key_id": "apikey_01Nq9vN6rT2zH7uW4bX5mR8s" },
  "organization_installation_preference": "available",
  "organization_installation_preference_inherited": true,
  "content_scan": { "status": "completed", "assessment": "pass", "reason": null },
  "components": [
    {
      "type": "skill",
      "name": "account-research",
      "description": "Researches a customer account before a call."
    },
    { "type": "mcp_server", "name": "crm", "description": null },
    {
      "type": "command",
      "name": "call-prep",
      "description": "Builds a one-page brief for an upcoming call."
    }
  ],
  "reach": "remote",
  "created_at": "2026-09-01T17:04:11Z",
  "updated_at": "2026-09-16T10:02:45Z"
}
```



Besides the shared responses (a `403` for a member-owned plugin, and `409 scan_pending` or `400 scan_failed` for a version members cannot be served; see [Error responses](#error-responses)), the request can fail with:

| Status                 | Cause                                                                                                                                          | What to do                                                             |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| 400                    | The body omits `served_version_id`, sets it to `null`, or contains any other field; or the value lacks the `pluginver_` prefix or is `latest`. | Send exactly `{"served_version_id": "pluginver_…"}`.                   |
| 404                    | `served_version_id` is not a version of this plugin.                                                                                           | Take the ID from [List a plugin's versions](#list-a-plugins-versions). |
| 409 (no `error_code`)  | An upload to this plugin or another served-version change is still in progress.                                                                | Retry shortly.                                                         |
| 409 `skill_name_taken` | The plugin is in the library marketplace and the version has a skill whose name an organization skill now uses.                                | Choose another version, or rename one of the skills.                   |

### Delete a plugin

`DELETE /v1/organizations/plugins/{plugin_id}` permanently deletes a plugin and every version it holds, just as an administrator's delete in claude.ai does. It works on any plugin in a `manual` marketplace, including a member's plugin, even if that member has since left the organization. When the delete returns, the plugin, its versions, and their files are gone from every read, and members are no longer served it. An organization-owned plugin's installation settings are removed with it; a member-owned plugin's shares are withdrawn, and it disappears for its owner too. A plugin in a marketplace synchronized from Git returns `400`: remove it from the repository, or remove the marketplace in claude.ai. Requires the `write:plugins` scope.

Deletion cannot be undone, and there is no per-version delete. To withhold an organization-owned plugin reversibly instead, set its organization-wide installation setting to `not_available` (a plugin that was inheriting its marketplace's default gets a setting of its own, and [removing that organization-wide setting](#remove-an-installation-setting) later returns the plugin to the default), and remove (or set to `not_available`) every group setting that `GET /v1/organizations/plugins/{plugin_id}/installation_settings` lists, because a group's setting overrides the organization-wide value for its members. Send these writes one after another, not in parallel (see [Set an installation setting](#set-an-installation-setting)). A member-owned plugin cannot be withheld through this API except by deleting it, and only if its marketplace is `manual`.

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
client = anthropic.Anthropic()

deleted_plugin = client.beta.organization.plugins.delete(
    "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
)

print(f"id: {deleted_plugin.id}")
```

```python
{ "type": "plugin_deleted", "id": "plugin_01Hq3vX8kZcN2mB7pR4tY9wL" }
```



## Plugin versions

A plugin version is an immutable snapshot of a plugin's files from one upload (the [Create a version](#create-a-version) response shows a complete object). Its fields mirror the plugin's served-version fields (`display_name`, `description`, `manifest_version`, `content_scan`, `components`, `reach`) for this version, plus `release_notes` (as supplied with the upload; shown in claude.ai's version history) and `created_by` (who uploaded it).

A `{version}` that lacks the `pluginver_` prefix returns `400` (except the literal `latest` where noted). One that carries the prefix but does not identify a version of that plugin returns `404`.

### List a plugin's versions

`GET /v1/organizations/plugins/{plugin_id}/versions` lists a plugin's versions, ordered by `created_at` descending; the first item is the version `latest_version_id` identifies. `limit` is 1 to 1,000. Requires the `read:plugins` scope.

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
client = anthropic.Anthropic()

versions = client.beta.organization.plugins.versions.list(
    "plugin_01Hq3vX8kZcN2mB7pR4tY9wL", limit=50
)

# Automatically fetches more pages as needed.
for version in versions:
    print(f"{version.id}: {version.manifest_version}")
```

### Create a version

`POST /v1/organizations/plugins/{plugin_id}/versions` adds a version to an organization-owned plugin in a `manual` marketplace. The body is `multipart/form-data`, with the same `files[]` and `release_notes` fields, [upload requirements](#upload-requirements), and file, manifest, archive, and size errors as [Create a plugin](#create-a-plugin). The uploaded name (the manifest's `name`) must equal the plugin's `name`. If the plugin is not pinned, the new version is normally served as soon as it is stored; if it is pinned, the version is stored but not served until you change the served version to it. To check, compare the response's `id` with the plugin's `served_version_id`. Returns the version. Requires the `write:plugins` scope.

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
client = anthropic.Anthropic()

with open("dist/sales-toolkit.zip", "rb") as archive:
    version = client.beta.organization.plugins.versions.create(
        "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
        files=[archive],
        release_notes="Adds the call-prep command.",
    )

print(f"id: {version.id}")
print(f"manifest_version: {version.manifest_version}")
```

```python
{
  "type": "plugin_version",
  "id": "pluginver_01Jd5sK2nQ8wE4rT6yU1iO3p",
  "plugin_id": "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  "display_name": "Sales Toolkit",
  "description": "Account research and call prep for the sales team.",
  "manifest_version": "1.5.0",
  "release_notes": "Adds the call-prep command.",
  "created_by": { "type": "api_actor", "api_key_id": "apikey_01Nq9vN6rT2zH7uW4bX5mR8s" },
  "content_scan": { "status": "processing", "assessment": null, "reason": null },
  "components": [
    {
      "type": "skill",
      "name": "account-research",
      "description": "Researches a customer account before a call."
    },
    { "type": "mcp_server", "name": "crm", "description": null },
    {
      "type": "command",
      "name": "call-prep",
      "description": "Builds a one-page brief for an upcoming call."
    }
  ],
  "reach": "remote",
  "created_at": "2026-09-15T14:12:30Z"
}
```



Besides a `400` for an upload that breaks the [upload requirements](#upload-requirements) (`413` for a request body over 200 MB) and the shared responses (a `403` for a member-owned plugin; see [Error responses](#error-responses)), the request can fail with:

| Status                     | Cause                                                                                                    | What to do                                                                                                            |
|----------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 400                        | The plugin is in a marketplace synchronized from Git, or the uploaded name differs from the plugin's.    | Change the repository instead, or fix the manifest `name`.                                                            |
| 409 (no `error_code`)      | Another upload to this plugin, or a served-version change, is still in progress.                         | Retry shortly.                                                                                                        |
| 409 `skill_name_taken`     | The plugin is in the library marketplace and the version adds a skill with an organization skill's name. | Rename the skill, or remove the organization skill in claude.ai.                                                      |
| 503 `registration_pending` | The version was stored but its registration did not complete.                                            | Resend the same request when the response carries `x-should-retry: true` (see [Retrying uploads](#retrying-uploads)). |

### Get a version

`GET /v1/organizations/plugins/{plugin_id}/versions/{version}` returns one version. `{version}` is a version ID, or `latest` for the version `latest_version_id` identifies at the time of the request. Requires the `read:plugins` scope.

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
client = anthropic.Anthropic()

version = client.beta.organization.plugins.versions.retrieve(
    "latest",
    plugin_id="plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
)

print(f"id: {version.id}")
print(f"manifest_version: {version.manifest_version}")
```

### Download a version's files

`GET /v1/organizations/plugins/{plugin_id}/versions/{version}/content` downloads a version's files as the stored `.zip` archive (`Content-Type: application/zip`). The archive is returned whatever its content-scan result, so you can inspect versions withheld from members. It is served exactly as stored, so for an organization-owned plugin in a `manual` marketplace you can re-upload it unchanged as a new version, provided it meets the current upload requirements. `{version}` must be a version ID, not `latest`: read the plugin's `served_version_id` or `latest_version_id` first, or resolve `latest` with `GET /v1/organizations/plugins/{plugin_id}/versions/latest`. The `Content-Disposition` filename is derived from the plugin's name and is not unique; name saved files by plugin and version ID. Requires the `read:plugins` scope.

Downloading a **member-owned** plugin's archive records a `claude_plugin_archive_accessed` event on the Compliance API Activity Feed, identifying the key (as `api_actor`), the plugin and its marketplace, the version, and the owning member by ID; it carries no names. Downloading an organization-owned plugin's archive records nothing.

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
client = anthropic.Anthropic()

plugin_id = "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
version_id = "pluginver_01Km7tL4pR9xF5sU2zV3jP6q"

with client.beta.organization.plugins.versions.with_streaming_response.download(
    version_id,
    plugin_id=plugin_id,
) as response:
    response.stream_to_file(f"{plugin_id}_{version_id}.zip")
```

## Plugin installation settings

These endpoints apply to organization-owned plugins. They return `404` for a member-owned plugin, which has [shares](#plugin-shares) instead. `{target}` is the literal `organization` for the plugin's organization-wide setting, or a group's `rbac_group_` ID for that group's setting; any other value returns `400`. Group IDs come from `GET /v1/organizations/rbac_groups` (scope `read:rbac_groups`; see [User management](manage-claude-user-management.md#groups)). A setting has no `id` of its own: it is addressed by `(plugin_id, target)`, and no actor is recorded on it (the actor is on its `plugin_installation_preference_updated` activity event).

### List a plugin's installation settings

`GET /v1/organizations/plugins/{plugin_id}/installation_settings` lists the settings an organization-owned plugin holds, ordered by `created_at` descending: its own organization-wide setting (absent while it inherits its marketplace's default) and each group's setting. Filter by `target_type` (`organization` or `rbac_group`). Requires the `read:plugins` scope.

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
client = anthropic.Anthropic()

settings = client.beta.organization.plugins.installation_settings.list(
    "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
)

# Automatically fetches more pages as needed.
for setting in settings:
    print(f"{setting.plugin_id}: {setting.installation_preference}")
```

### Set an installation setting

`POST /v1/organizations/plugins/{plugin_id}/installation_settings/{target}` sets one target's installation setting for an organization-owned plugin, creating it or changing the value it already holds. The body's only field is `installation_preference` (`required`, `auto_install`, `available`, or `not_available`), and it is required. Setting the value the target already holds changes nothing. Setting the `organization` target stops the plugin inheriting its marketplace's default (`organization_installation_preference_inherited` becomes `false`), even when the value is the same as the default, so the plugin no longer follows later changes to the marketplace default. To return the plugin to its marketplace's default, [remove the organization-wide setting](#remove-an-installation-setting); group settings are unaffected. A group target must be a group your organization can see in `GET /v1/organizations/rbac_groups`, or the request returns `404`. The change does not alter the plugin's `updated_at`; it is recorded on the Activity Feed. Returns the setting. Requires the `write:plugins` scope.

Send a plugin's installation-setting writes one at a time. If several writes for the same plugin arrive at the same time, the server handles them one after another and can answer some of them with `503` instead of applying them. That `503` carries `x-should-retry: true`, and the write is safe to repeat: wait a second or two, then send it again.

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
client = anthropic.Anthropic()

setting = client.beta.organization.plugins.installation_settings.set(
    "rbac_group_01F3xQqQzXyWvUtSrQpOnMlK",
    plugin_id="plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
    installation_preference="available",
)

print(f"plugin_id: {setting.plugin_id}")
print(f"installation_preference: {setting.installation_preference}")
```

```python
{
  "type": "plugin_installation_setting",
  "plugin_id": "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  "target": { "type": "rbac_group", "rbac_group_id": "rbac_group_01F3xQqQzXyWvUtSrQpOnMlK" },
  "installation_preference": "available",
  "created_at": "2026-09-02T10:00:00Z",
  "updated_at": "2026-09-02T10:00:00Z"
}
```



### Remove an installation setting

`DELETE /v1/organizations/plugins/{plugin_id}/installation_settings/{target}` removes one target's installation setting for an organization-owned plugin. With `{target}` of `organization` it removes the plugin's own organization-wide setting. The plugin then inherits its marketplace's default again (`organization_installation_preference_inherited` becomes `true`) and follows later changes to that default; group settings are unaffected. With a group's `rbac_group_` ID it removes that group's setting: the group's members fall back to the organization-wide value, or to another of their groups' settings. A target that holds no setting of its own returns `404`; that includes the `organization` target of a plugin that already inherits its marketplace's default. The change does not alter the plugin's `updated_at`; it is recorded on the Activity Feed. The response carries the composite key in place of an `id`; for the `organization` target its `target` is `{"type": "organization"}`. Requires the `write:plugins` scope.

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
client = anthropic.Anthropic()

removed_setting = client.beta.organization.plugins.installation_settings.remove(
    "rbac_group_01F3xQqQzXyWvUtSrQpOnMlK",
    plugin_id="plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
)

print(f"plugin_id: {removed_setting.plugin_id}")
```

```python
{
  "type": "plugin_installation_setting_deleted",
  "plugin_id": "plugin_01Hq3vX8kZcN2mB7pR4tY9wL",
  "target": { "type": "rbac_group", "rbac_group_id": "rbac_group_01F3xQqQzXyWvUtSrQpOnMlK" }
}
```



## Plugin shares

Shares exist only on member-owned plugins and are read-only in this API (see [Shares](#shares)).

### List a plugin's shares

`GET /v1/organizations/plugins/{plugin_id}/shares` lists who the owner of a member-owned plugin has shared it with, ordered by `granted_at` descending: every member (`organization`), a group (`rbac_group`), or a named member (`organization_member`). Filter by `target_type`. A plugin its owner has not shared returns an empty list; an organization-owned plugin returns `404`. Shares are read-only on this API, and a listed share gives access only while that kind of sharing is turned on for your organization in claude.ai (see [Shares](#shares)). `granted_at` is when the share was given; if the owner later changes the share in claude.ai, it is the time of that change. Requires the `read:plugins` scope.

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
client = anthropic.Anthropic()

shares = client.beta.organization.plugins.shares.list("plugin_01Mr2wP7sU3aJ8vX5cY6nS9t")

# Automatically fetches more pages as needed.
for share in shares:
    print(f"plugin_id: {share.plugin_id}")
```

```python
{
  "data": [
    {
      "type": "plugin_share",
      "plugin_id": "plugin_01Mr2wP7sU3aJ8vX5cY6nS9t",
      "target": { "type": "organization_member", "user_id": "user_01WCz9BvGLdMYRUMmcAxMWvW" },
      "granted_at": "2026-08-20T15:12:00Z"
    }
  ],
  "next_page": null
}
```



## Plugin marketplaces

This API reads [marketplaces](#marketplaces) and sets an organization marketplace's default installation setting; marketplaces themselves are created, connected to a repository, and deleted in claude.ai.

```python
{
  "type": "plugin_marketplace",
  "id": "marketplace_01VbNcMxZaSdFgHjKlQwErTy",
  "name": "engineering-tools",
  "owner": { "type": "organization" },
  "source": "github",
  "sync_status": "success",
  "last_sync_ended_at": "2026-09-10T22:15:03Z",
  "last_sync_read_sha": "9fceb02d0ae598e95dc970b74767f19372d61af8",
  "default_installation_preference": "available",
  "created_at": "2026-06-12T08:45:00Z"
}
```



| Field                             | Description                                                                                                                                                                                                                                                       |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`                            | The marketplace's name. Fixed for its lifetime.                                                                                                                                                                                                                   |
| `owner`                           | Same shape as on the plugin.                                                                                                                                                                                                                                      |
| `source`                          | `manual`, `github`, `gitlab`, or `public_git`. See [Marketplaces](#marketplaces).                                                                                                                                                                                 |
| `sync_status`                     | Outcome of the most recent synchronization: `success`, `in_progress`, `failed_content`, `failed_transient`, `failed_auth`, or `failed_limits`. `null` until a synchronization is first attempted, which never happens for a marketplace whose source is `manual`. |
| `last_sync_ended_at`              | When the most recent synchronization attempt finished, whatever its outcome; for a connected repository that has not synchronized yet, when the marketplace was created. `null` for a marketplace that is not synchronized.                                       |
| `last_sync_read_sha`              | The commit the last synchronization read from the repository. Not necessarily the commit the served versions came from. `null` for a marketplace that is not synchronized.                                                                                        |
| `default_installation_preference` | Organization marketplaces: the organization-wide value for every plugin in it without its own setting (`not_available` if never set). Personal marketplaces: `null`.                                                                                              |

A `marketplace_id` that lacks the `marketplace_` prefix returns `400`. One that carries the prefix but does not resolve, or belongs to another organization, returns `404`.

### List marketplaces

`GET /v1/organizations/plugin_marketplaces` lists your organization's marketplaces and members' personal marketplaces, ordered by `created_at` descending. Use it to find a marketplace's ID, to filter the plugin list by it or to upload into it, before it holds any plugin. The library marketplace appears once something has first been created in it, in claude.ai or through this API. Filter by `owner_type` (`organization` or `user`) and `source`. `limit` is 1 to 1,000. Requires the `read:plugins` scope.

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
client = anthropic.Anthropic()

marketplaces = client.beta.organization.plugin_marketplaces.list(
    owner_type="organization"
)

# Automatically fetches more pages as needed.
for marketplace in marketplaces:
    print(f"{marketplace.id}: {marketplace.name}")
```

### Get a marketplace

`GET /v1/organizations/plugin_marketplaces/{marketplace_id}` returns one marketplace. Requires the `read:plugins` scope.

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
client = anthropic.Anthropic()

marketplace = client.beta.organization.plugin_marketplaces.retrieve(
    "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r"
)

print(f"id: {marketplace.id}")
print(f"name: {marketplace.name}")
```

### Set a marketplace's default installation setting

`POST /v1/organizations/plugin_marketplaces/{marketplace_id}` sets the default installation setting of an organization-owned marketplace. Every plugin in the marketplace without its own organization-wide setting reports this default as its `organization_installation_preference`, including plugins added later. It works for `manual` and synchronized marketplaces; a member's personal marketplace returns `403`. The only updatable field is `default_installation_preference`, and it is required. It cannot be set back to `null`: once a marketplace has a default, it keeps one, as in claude.ai. A change is recorded as one `marketplace_updated` event with no per-plugin events, and does not alter any plugin's `updated_at`. Setting the value already set changes nothing, with one exception: a marketplace whose default was never set reports `not_available` but holds no setting, so its first write (even `not_available`) counts as a change. Returns the marketplace. Requires the `write:plugins` scope.

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
client = anthropic.Anthropic()

marketplace = client.beta.organization.plugin_marketplaces.update(
    "marketplace_01Lp8uM5qS1yG6tV3aW4kQ7r",
    default_installation_preference="available",
)

print(f"id: {marketplace.id}")
print(f"default_installation_preference: {marketplace.default_installation_preference}")
```

### Validate marketplace content

Two endpoints report what a synchronization of the given marketplace content would do, without connecting or storing anything: `POST /v1/organizations/plugin_marketplaces/validate_repository` reads a public GitHub repository, and `POST /v1/organizations/plugin_marketplaces/validate_archive` reads a `.zip` of the marketplace directory that you upload. Both return the same report: whether `marketplace.json` is well-formed, which plugins would be skipped and why, and which plugins would synchronize with some contents left out. The checks are the ones a real synchronization runs. Problems with the content come back in the report, not as HTTP errors: the request succeeds with `valid: false`, even when the repository or archive cannot be read at all. A validation counts as a read, and the two endpoints together are additionally limited to 10 validations a minute per organization (see [Rate limiting](#rate-limiting)); they record nothing on the Activity Feed. A validation can take up to 120 seconds before it returns, so set your client's timeout above that. Both endpoints require the `read:plugins` or `write:plugins` scope (`read:org_audit` and `read:compliance_org_data` do not grant them).

The repository, and any plugin source outside it on GitHub, are read anonymously, so a private repository or private plugin source is reported as not found. Plugin sources on hosts other than GitHub are not fetched; such a plugin normally gets a `marketplace_validate_source_not_checked` warning and is checked when the marketplace actually synchronizes. If the repository is, or the archive names, a marketplace that Anthropic synchronizes into every organization, stricter rules apply: every plugin source outside the marketplace must be pinned to a full commit SHA, unpinned or unsupported-host sources are reported as plugin errors, and the branch read defaults to the one that marketplace synchronizes from.

`validate_repository` takes a JSON body with two fields: `repository_url`, the `https://` URL of a public repository on github.com (required), and `ref`, a branch name or a full 40-character commit SHA (optional; when it is omitted or `null`, the branch a synchronization would read, usually the repository's default branch). `validate_archive` takes `multipart/form-data` with exactly one part, `archive`, sent as a file part with a filename: a `.zip` of the marketplace directory, at most 32 MB, with its contents at the root or wrapped in one folder (as a Git host's download produces), DEFLATE or STORE compression only. No other form field is accepted.

Validate a public repository at a branch:

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
client = anthropic.Anthropic()

report = client.beta.organization.plugin_marketplaces.validate_repository(
    repository_url="https://github.com/example-org/claude-plugins",
    ref="release-candidate",
)

print(f"valid: {str(report.valid).lower()}")
print(f"total_plugin_count: {report.total_plugin_count}")
```

```python
{
  "type": "plugin_marketplace_validation_report",
  "valid": false,
  "ref": "release-candidate",
  "commit_sha": "9fceb02d0ae598e95dc970b74767f19372d61af8",
  "total_plugin_count": 3,
  "manifest_error": null,
  "manifest_error_code": null,
  "plugin_errors": [
    {
      "name": "deploy-helper",
      "error": "The plugin has a top-level bin/ directory.",
      "error_code": "marketplace_sync_bin_directory_not_allowed"
    }
  ],
  "plugin_warnings": [
    {
      "name": "release-notes",
      "warnings": [
        {
          "message": "plugin.json has unrecognized top-level keys: owners",
          "error_code": "marketplace_sync_plugin_unrecognized_keys"
        }
      ]
    }
  ]
}
```



| Field                                   | Description                                                                                                                                                                                                                                                 |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `valid`                                 | `true` when `marketplace.json` is well-formed and no plugin would be skipped. Warnings do not make it `false`.                                                                                                                                              |
| `ref`                                   | The branch that was read, by name; `null` when no branch was named and the default branch was read, for a commit SHA, or for an archive.                                                                                                                    |
| `commit_sha`                            | The commit that was validated. For an archive downloaded from a Git host, the commit the host recorded in the ZIP file's comment field, if any (not verified).                                                                                              |
| `total_plugin_count`                    | How many plugins `marketplace.json` declares; `0` when it could not be read.                                                                                                                                                                                |
| `manifest_error`, `manifest_error_code` | Set when nothing could be validated: the source could not be read, or `marketplace.json` is missing, malformed, or over a limit. Validation that did not finish within 120 seconds reports `manifest_error_code: "marketplace_validate_deadline_exceeded"`. |
| `plugin_errors`                         | One `{name, error, error_code}` per plugin a synchronization would skip.                                                                                                                                                                                    |
| `plugin_warnings`                       | One `{name, warnings: [{message, error_code}]}` per plugin that would synchronize with some contents left out.                                                                                                                                              |

Validate a local copy of the marketplace directory instead, as a `.zip`; the response is the same report:

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
client = anthropic.Anthropic()

with open("marketplace.zip", "rb") as archive:
    report = client.beta.organization.plugin_marketplaces.validate_archive(
        archive=archive
    )

print(f"valid: {str(report.valid).lower()}")
print(f"total_plugin_count: {report.total_plugin_count}")
```

Problems with the content never fail the request. Apart from the responses every endpoint shares (a `403` for a key that has only `read:org_audit` or `read:compliance_org_data`; see [Error responses](#error-responses) and [Rate limiting](#rate-limiting)), the request itself can fail with:

| Status | Cause                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | What to do                                                   |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| 400    | On `validate_repository`: the body is not a JSON object; `repository_url` is missing, is longer than 2,048 characters, carries credentials, or is not of the form `https://github.com/{owner}/{repo}` (a `.git` suffix is accepted; another host, a longer path such as a branch page's `/tree/main`, or a port other than 443 or 80 is not); `ref` is empty, is longer than 255 characters, contains `..`, or contains a character other than ASCII letters, digits, `.`, `_`, `-`, `+`, and `/`; or another field is present. A `ref` that passes these checks but names a branch the repository does not have is not refused: the request succeeds with `valid: false` and `manifest_error` says the branch was not found. On `validate_archive`: the body is not `multipart/form-data`, the `archive` part is missing, repeated, or not sent as a file part with a filename, or another form field is present. | Fix the request and resend.                                  |
| 413    | On `validate_archive`: the `archive` part, or the request's declared body length, exceeds 32 MB.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Validate the repository by URL instead, or trim the archive. |

#### Report codes

Each finding in a report has a stable code: `manifest_error_code` when nothing could be validated, `error_code` on each `plugin_errors` entry, and `error_code` on each warning. When a plugin has several problems, `error_code` is the first one's and `error` joins their messages. New codes may be added; an unrecognized `manifest_error_code` still means the content could not be validated, one on a `plugin_errors` entry still means the plugin would be skipped, and one on a warning still means the plugin would synchronize. These codes indicate transient conditions, so the same request may succeed later: `marketplace_host_rate_limited`, `marketplace_host_server_error`, `marketplace_host_timeout`, `marketplace_host_unreachable`, `marketplace_repo_access_denied`, `marketplace_sync_transient_fetch_budget_exhausted`, `marketplace_validate_network_error`, and usually `marketplace_validate_deadline_exceeded`.

## Unrecognized values

Every string value on this page (component types, `reach`, scan fields, marketplace `source`, error codes) may gain new values at any time. Treat a value you do not recognize as you would any unknown string rather than failing.

## Rate limiting

Read requests (every `GET` endpoint on this page) share a limit of **300 requests per minute** per organization, and write requests (creating a plugin or version, changing the served version, deleting, setting or removing an installation setting, and updating a marketplace) share a limit of **60 requests per minute** per organization. A marketplace validation (either endpoint) counts as a read, and validations are additionally limited to 10 a minute per organization across both endpoints; both limits are checked before the request body is read. These limits are counted across all of your organization's keys and are separate from your organization's other Admin API limits. Requests over a limit return **429 Too Many Requests** with a `retry-after` header. Responses include `anthropic-ratelimit-requests-*` headers for the limit that applies (on marketplace validation, its 10-per-minute limit; on a `429`, whichever limit refused the request).

An upload, a served-version change, or a validation can also return `429` with `retry-after` when the service briefly has no capacity for another one, and an upload returns `429` when your organization has exceeded its content-scan rate. Handle all of these the same way: wait for `retry-after`, then retry. Separately from these limits, send installation-setting writes for the same plugin one at a time: when several arrive at the same time, some can be answered with `503` and `x-should-retry: true`, and those are safe to send again after a second or two (see [Set an installation setting](#set-an-installation-setting)).

## Pagination

List endpoints use an **opaque cursor**. The first request returns up to `limit` rows plus a `next_page` cursor; pass the cursor unchanged as the `page` parameter on the next request, and repeat until `next_page` is `null`. Treat the cursor string as opaque: don't parse, modify, or construct it yourself. [List plugins](#list-plugins) can return a page with fewer than `limit` plugins, or none, while `next_page` is still set, so keep requesting pages until `next_page` is `null`. The Python, TypeScript, C#, Go, Java, and Ruby SDKs' list iterators and the CLI (except with `--format raw`) do that for you. They request the next page while `next_page` is set, so a short or empty page does not end them. In PHP and curl, request each page yourself and pass its `next_page` as `page`.

`limit` defaults to 20 and has a minimum of 1. The maximum is 100 for plugins, installation settings, and shares, and 1,000 for versions and marketplaces. Every list is ordered newest first.

## Error responses

Error responses follow the standard shape documented in [Errors](../Endpoints/errors.md). Quote the `request_id` from the response body when contacting support.

| Status | Meaning                                                                                                                                                                                                                                                                                                              |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 400    | Invalid input, or the operation does not apply to this plugin or marketplace (see each endpoint's section). Also returned for a query parameter the endpoint does not recognize, and for an organization that is not a Claude Enterprise organization (`this endpoint is not supported for this organization type`). |
| 401    | Missing `x-api-key` header, or the key is not recognized.                                                                                                                                                                                                                                                            |
| 403    | The key is missing the required scope, or the request uploads to, changes the served version of, or sets the default for a member's plugin or personal marketplace. (Deleting a member's plugin is allowed.)                                                                                                         |
| 404    | Resource not found. Also returned when the request omits the `anthropic-beta` value, or the API is not enabled for your organization, so that the endpoints read as nonexistent.                                                                                                                                     |
| 409    | A name is taken, a content scan is still running, or a conflicting upload is in progress.                                                                                                                                                                                                                            |
| 413    | The request body is over the size limit: 200 MB for an upload, 32 MB for marketplace validation.                                                                                                                                                                                                                     |
| 429    | Rate limit exceeded. See [Rate limiting](#rate-limiting).                                                                                                                                                                                                                                                            |
| 500    | Internal error.                                                                                                                                                                                                                                                                                                      |
| 503    | Temporary. Also returned when several installation-setting writes for one plugin arrive at the same time; send those one at a time. Retry with backoff, except `registration_pending` (see the following table).                                                                                                     |

When one status has several causes that you would handle differently, the error also carries `error.details.error_code`, and `error.details.plugin_id` or `error.details.plugin_version_id` when the cause involves one:

```python
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "...",
    "details": {
      "error_code": "plugin_name_taken",
      "plugin_id": "plugin_01Hq3vX8kZcN2mB7pR4tY9wL"
    }
  },
  "request_id": "req_018EeWyXxfu5pfWkrYcMdjWG"
}
```



| `error_code`                                    | Status | Meaning and what to do                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `plugin_name_taken`                             | 409    | A plugin with this name already exists in the marketplace. `details.plugin_id` is that plugin. If you are retrying a create whose response you lost, continue with that plugin. When `plugin_id` is absent, the name is held by a standalone skill: upload under another name, or delete the skill in claude.ai. |
| `skill_name_taken`                              | 409    | The plugin is in the library marketplace and one of its skills has the same name as an organization skill (a skill an administrator uploaded for the whole organization in claude.ai). `details.skill_name` names it. Rename or remove one of them.                                                              |
| `registration_pending`                          | 503    | The files were stored, but the plugin's skills could not yet be made available to members. See [Retrying uploads](#retrying-uploads).                                                                                                                                                                            |
| `scan_pending`                                  | 409    | The version's content scan is still running. Retry once it finishes.                                                                                                                                                                                                                                             |
| `scan_failed`                                   | 400    | The version's content scan failed, errored, or reached no verdict, so it cannot be served. Choose another version.                                                                                                                                                                                               |
| `cmek_key_disabled`, `cmek_key_network_blocked` | 400    | Your organization's customer-managed encryption key is unavailable. See [Customer-managed encryption keys](#customer-managed-encryption-keys).                                                                                                                                                                   |

New codes may be added. Treat a code you do not recognize the way you treat its status.

### Retrying uploads

No endpoint accepts an `Idempotency-Key`. Changing the served version, setting an installation setting, and setting a marketplace default are safe to repeat. A repeated delete, or a repeated removal of an installation setting, returns `404`.

An upload that returns an error stored nothing, with one exception: `503` with `error_code: "registration_pending"`. After storing an upload's files, the server registers the new version's skills with claude.ai, which is what makes them usable by members; `registration_pending` means the files were stored but that last step did not complete. Uploading the same files once more completes it (and stores one more, identical version):

- On `POST /v1/organizations/plugins`, the plugin *was* created, and the response carries `x-should-retry: false`: do not resend the create (a resend returns `409 plugin_name_taken`); instead upload the same files as a version of `details.plugin_id`.
- On `POST /v1/organizations/plugins/{plugin_id}/versions`, the version *was* stored (`details.plugin_version_id`); resend the same request when the response carries `x-should-retry: true`, and do not when it carries `false`.

If a create's response is lost, retry it: the retry returns `409 plugin_name_taken` with the plugin's ID in `details.plugin_id`, and you continue with that plugin. Retrying a version create whose response was lost stores a second, identical version. To avoid that, record the plugin's `latest_version_id` before each upload; if a response is lost, read the plugin and retry only if `latest_version_id` is unchanged.

## Activity Feed events

Every write through this API is recorded on your organization's [Compliance API Activity Feed](manage-claude-compliance-activity-feed.md), attributed to the API key as an `api_actor` carrying its `apikey_` ID. The same actor appears in `created_by` on the plugins and versions the key creates.

| Event                                    | Emitted when                                                                                                                                                                        |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `claude_plugin_created`                  | A plugin is created by an upload (here or in claude.ai) or by an accepted request to publish. A plugin created by a Git synchronization emits only `claude_plugin_version_created`. |
| `claude_plugin_version_created`          | A version is stored. Versions stored by a Git synchronization are attributed to a `system_actor`.                                                                                   |
| `claude_plugin_updated`                  | A new version is uploaded to an existing plugin.                                                                                                                                    |
| `claude_plugin_served_version_updated`   | The served version changes.                                                                                                                                                         |
| `claude_plugin_deleted`                  | A plugin is deleted on its own, here or in claude.ai.                                                                                                                               |
| `plugin_installation_preference_updated` | An installation setting is set or removed.                                                                                                                                          |
| `marketplace_created`                    | The first upload creates the library marketplace.                                                                                                                                   |
| `marketplace_updated`                    | A marketplace's default installation setting changes, or an administrator or owner starts a synchronization in claude.ai.                                                           |
| `marketplace_deleted`                    | A marketplace is deleted in claude.ai together with its plugins (no per-plugin events).                                                                                             |
| `claude_plugin_archive_accessed`         | A member-owned plugin's archive is downloaded.                                                                                                                                      |
| `claude_plugin_security_scan_completed`  | A content scan finishes.                                                                                                                                                            |

The plugin, version, and marketplace IDs in these events are the same IDs this API returns. `plugin_installation_preference_updated` identifies the plugin by its `name` and `marketplace_id` rather than its `id`.

Changing a marketplace's default records one `marketplace_updated` event and no per-plugin events, even though it changes the value of every plugin that inherits the default. Reads are not recorded, except downloads of a member-owned plugin's archive. A write that changes nothing records nothing.

Shares given or withdrawn in claude.ai appear on the feed as `role_assignment_granted` and `role_assignment_revoked` events. This API does not report deletions: a deleted plugin is simply absent from the next list. A plugin removed by a Git synchronization, by deleting its marketplace (one `marketplace_deleted` event), or by deleting a member's account or the organization emits no per-plugin event, so re-list the full inventory periodically to catch removals.

## Customer-managed encryption keys

If your organization uses a [customer-managed encryption key](manage-claude-cmek.md), a version's `description`, `release_notes`, `components`, and files are encrypted with it. While the key is unavailable:

- Reads and lists still succeed, with `description`, `release_notes`, and `components` returned as `null`.
- Archive downloads, creates, version creates, and served-version changes return `400` with `cmek_key_disabled` or `cmek_key_network_blocked`.
- Deleting a plugin in the library marketplace returns `400 cmek_key_disabled` and deletes nothing, because its skills must first be withdrawn from claude.ai and that needs the key. Other deletes, installation settings, and marketplace defaults work normally.

Restoring the key clears all of these.

## See also

[Create an Admin API key](manage-claude-admin-api-keys.md)

Where your primary owner creates a scoped key.

[User management](manage-claude-user-management.md)

The group endpoints that supply the `rbac_group_` IDs used in installation settings.

[Compliance API Activity Feed](manage-claude-compliance-activity-feed.md)

Where plugin writes and member-archive downloads are recorded.

[Analytics APIs](manage-claude-analytics-api.md)

Plugin and skill usage reporting for Claude Enterprise.
