---
title: "Download Code Artifact Version Content - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/code/artifacts/retrieve_version"
category: "04-API-Reference/Admin"
fetched_at: "2026-10-23T06:28:36Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Fapps%2Fcode%2Fartifacts%2Fretrieve_version)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](../Endpoints/overview.md)[Beta headers](../Endpoints/beta-headers.md)[Errors](../Endpoints/errors.md)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores

Dreams


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Models


List Models


Get a Model


Organization


Get Current Organization

API Keys

External Keys

Federation

Invites

Service Accounts

Users

Workspaces

Rate Limits

Compliance Settings

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles

Plugins

Plugin Marketplaces

Telemetry Destinations

Webhooks


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Delete User Profile


Create Enrollment URL

Action URLs


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


Compliance API

Activities

Organizations

Groups

Apps

Chats

Projects

Artifacts

Sessions

Code

Artifacts


List Code Artifacts


Download Code Artifact Version Content


Download Code Artifact Content


Delete Code Artifact


Completions


Create a Text Completion Deprecated

OpenTelemetry

[Spans](../Endpoints/opentelemetry-spans.md)

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[AWS IAM actions](../Endpoints/claude-platform-on-aws-iam-actions.md)[Google Cloud IAM permissions](../Endpoints/claude-models-on-google-cloud-anthropic-managed-iam-permissions.md)[Versions](../Endpoints/versioning.md)[Migrating to API version 2026-10-21](../Endpoints/migration-2026-10-21.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/playground.md)

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



API version 2026-10-21

1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)
3.  [Apps](https://platform.claude.com/docs/en/api/http/compliance/apps)
4.  [Code](https://platform.claude.com/docs/en/api/http/compliance/apps/code)
5.  [Artifacts](https://platform.claude.com/docs/en/api/http/compliance/apps/code/artifacts)

# Download Code Artifact Version Content

Copy page



API version 2026-10-21

GET/v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}

Streams the content of one version of an Artifact as the response body, in chunks with no `Content-Length`. With `multi_file_format=zip`, a version with more than one file, other than a Claude Doc's (an Artifact whose `artifact_type` is `claude_docs`), comes back as a ZIP archive of its files.

Headers: `Content-Type` (`application/zip` for a ZIP archive, otherwise the stored MIME type), `Content-Disposition: attachment; filename*=utf-8''<name>` (RFC 5987), `Cache-Control: no-store, private` and, when available, `Content-MD5` (base64). `<name>` is `{artifact_id}-{version_id}.zip` for a ZIP archive, otherwise `{artifact_id}-{version_id}.txt`, whatever the content is. `Content-MD5` is only on a single file stored uncompressed, so it is never on a ZIP archive. Check the body against it when present.

Errors specific to this download:

- `404`: the Artifact doesn't exist or the API key cannot read it, or the version is no longer kept. Older versions are dropped as new ones are published, so list the Artifact's versions again. You also get this when the organization's customer-managed encryption key can't be used. Retry once the key can be used again.
- `503`: the content can't be served right now, for example because its upload is still in progress or was abandoned. Retry with backoff.
- `422` with `error.details.error_code` `multi_file_unavailable`: the version has more than one file. Add `multi_file_format=zip`. A Claude Doc's version with more than one file gets this error either way, because it holds only the web page that displays the Doc. Download the Doc's text with `GET /v1/compliance/apps/code/artifacts/{artifact_id}/content?multi_file_format=zip`.
- `422` with `file_set_unavailable`: the request sets `multi_file_format=zip`, the version has more than one file, and one of them has a path the API cannot export. Do not retry.

An error after the download has started stops the body early, with the `200` status already sent. For example, this happens to content stored compressed when it is over 16 MiB once decompressed. For a single file with no `Content-MD5`, the only sign is a transfer that aborts before its last chunk, so treat a download that aborts this way as failed.

A ZIP archive of a version's files holds one top-level folder, named for the Artifact and version. That folder holds a `files/` folder and an index, `files.json`. The index is written last, so treat an archive as incomplete if it cannot be opened or has no `files.json` in its top-level folder.

`files.json` has these fields:

- `artifact_id`: the Artifact ID, as in the request.
- `version_id`: the version ID, as in the request.
- `title`: the title of the version in the archive, or that version's ID when no title is kept.
- `created_at`: when the version was published (RFC 3339, UTC), or null when that is not known.
- `files`: one entry for each file under `files/`, with `original_path` (the file's path in the version), `exported_as` (its path in the archive), `sha256` (lowercase hex), `size_bytes` (before compression) and `mime_type`. `exported_as` is the top-level folder, then `files/`, then `original_path`. A name that could not be saved or opened safely on every operating system is changed. Use `exported_as`, not `original_path`, to find a file in the archive.
- `omitted_files`: the files left out of the archive, each with `original_path`, `sha256`, `size_bytes` and `mime_type`. They include files the version uses from another Artifact. They also include files copied from the Artifact type the Artifact was made from, such as the app that displays it, when another organization owns that type.

`files` and `omitted_files` together list at most 4,096 files, their `size_bytes` add up to at most 1 GiB, and no file is over 20 MiB.

##### Path parameters

artifact_id: string



The Artifact ID (tagged ID, e.g., cart_abc123)

version_id: string



Opaque version identifier from the Artifact's `versions` list

##### Query parameters

multi_file_format: optional string



Set to `zip`, its only value, to receive a version that has more than one file as a ZIP archive of its files with an index, `files.json`. A version with one file is returned as that file. A Claude Doc's version never comes back as a ZIP.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

"x-api-key": optional string



Download Code Artifact Version Content

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID/versions/$VERSION_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
