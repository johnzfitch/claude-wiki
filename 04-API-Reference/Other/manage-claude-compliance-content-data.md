---
title: "Retrieve and delete chats, files, and projects - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/compliance-content-data"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:34Z"
tags: ["api"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fcompliance-content-data)





SearchCtrlK

Organization

[Admin API](manage-claude-admin-api.md)[User management](manage-claude-user-management.md)[Workspaces](manage-claude-workspaces.md)

Authentication

[Overview](manage-claude-authentication.md)[Create an Admin API key](manage-claude-admin-api-keys.md)[App Attest](manage-claude-app-attest.md)[Workload Identity Federation](manage-claude-workload-identity-federation.md)[Manage WIF via API](manage-claude-wif-admin-api.md)[WIF reference](manage-claude-wif-reference.md)

Identity providers

Monitoring

[Usage and Cost API](manage-claude-usage-cost-api.md)[Rate Limits API](manage-claude-rate-limits-api.md)[Analytics APIs](manage-claude-analytics-api.md)[Claude Code Analytics API](manage-claude-claude-code-analytics-api.md)[Spend Limits API](manage-claude-spend-limits-api.md)

Data & compliance

[Data residency](../Guides/build-with-claude-data-residency.md)[API and data retention](manage-claude-api-and-data-retention.md)[Access Transparency](manage-claude-access-transparency.md)

[Encryption keys](manage-claude-cmek.md)

[Inference hooks](manage-claude-inference-hooks.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](usage-limits.md)

[Admin](manage-claude-admin-api.md)Compliance API

# Retrieve and delete chats, files, and projects

Copy page



Access chat content, file attachments, and projects for claude.ai organizations through the Compliance API.

Copy page





The endpoints on this page are available only to Claude Enterprise organizations. They retrieve and delete claude.ai chats, files, and projects; transcripts of sessions in apps such as Cowork and Claude Code are covered on [Retrieve session transcripts](manage-claude-compliance-sessions.md). See [Set up the Compliance API](manage-claude-compliance-api-access.md).



**Required scope:** `read:compliance_user_data` on the Compliance Access Key. The delete endpoints also require `delete:compliance_user_data`.

**Prerequisite:** None for listing chats organization-wide. To filter the chat list to specific users, you need user IDs from [List organization users](manage-claude-compliance-org-data.md#list-organization-users). The other endpoints on this page take resource IDs directly.

The endpoints on this page expose Claude Enterprise chat content, file uploads, projects, and project attachments to compliance reviewers. They support eDiscovery (electronic discovery) exports, data loss prevention (DLP) enforcement, and account-deletion responses. Chat, file, and project content is retained for as long as your organization's retention policy allows. When a user deletes a chat in claude.ai, its message content, attached files, tool-generated files, and artifacts are deleted with it. The Compliance API still lists the chat, with `deleted_at` populated and an empty `name`, and returns its messages without their content. Chats that have been hard-deleted (through the Compliance API itself, or after the organization's retention window expires) are not retrievable.

Both scopes are granted only on Compliance Access Keys (`sk-ant-api01-...`) created in claude.ai; see [Set up the Compliance API](manage-claude-compliance-api-access.md) to provision one. The `read:compliance_user_data` scope covers retrieval; `delete:compliance_user_data` is required only for the delete endpoints. The chat, file, project, and attachment endpoints are not available to Admin API keys (`sk-ant-admin01-...`); calls authenticated with an Admin API key return [403 Forbidden](manage-claude-compliance-errors.md#403-forbidden).

Endpoints on this page paginate two ways; see [Paginate results](manage-claude-compliance-activity-feed.md#paginate-results) for the full reference. Each section notes which scheme applies.

## Retrieve chats and messages

Use [List chats](../Admin/compliance-apps-chats-list.md) to page through chat metadata, then [Get chat messages](../Admin/compliance-apps-chats-messages-list.md) to fetch the full message content of one chat.

The chat list endpoint defaults to organization-wide scope: leave off `user_ids[]` to include every chat under your parent organization. Add `order_by=updated_at` to sort by last update time. This combination is the recommended way to export chats and keep an export current, because one paginated loop picks up new chats, chats with new messages, and chats deleted in claude.ai for every user without enumerating users first. The following request lists chats updated since a given date.

cURL



```python
curl --fail-with-body -sS -G \
  "https://api.anthropic.com/v1/compliance/apps/chats" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --header "anthropic-version: 2023-06-01" \
  --data-urlencode "order_by=updated_at" \
  --data-urlencode "updated_at.gte=2025-06-01T00:00:00Z" \
  --data-urlencode "limit=100"
```

Response



```python
{
  "data": [
    {
      "id": "claude_chat_01H5CWunD7RpVJ5bHa8RCkja",
      "name": "Product Requirements Discussion",
      "created_at": "2026-04-10T08:09:10Z",
      "updated_at": "2026-04-10T09:10:11Z",
      "deleted_at": null,
      "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789",
      "model": "claude-opus-5-5",
      "organization_uuid": "91012d09-e48b-438e-a489-1bebfd8fa6f9",
      "project_id": "claude_proj_01KGp4eZNug9ri4kE35RSppq",
      "user": {
        "id": "user_01XyDMpzjS89pFZXqSFUBDr6",
        "email_address": "user@example.com"
      }
    }
  ],
  "has_more": true,
  "first_id": "eyJrIjogInVwZGF0ZWRfYXQiLCAidCI6ICIyMDI2LTA0LTEwVDA5OjEwOjExKzAwOjAwIiwgImlkIjogImFiY2RlZjAxLS4uLiJ9",
  "last_id": "eyJrIjogInVwZGF0ZWRfYXQiLCAidCI6ICIyMDI2LTA0LTEwVDA5OjEwOjExKzAwOjAwIiwgImlkIjogImFiY2RlZjAxLS4uLiJ9"
}
```

Results sort ascending by the `order_by` field, oldest first, with ties broken by `id`. Pagination uses the standard `first_id`/`last_id`/`has_more` cursor fields described in [Paginate results](manage-claude-compliance-activity-feed.md#paginate-results). To walk forward toward newer chats, pass the response's `last_id` back as `after_id` on the next request.

That forward walk is also how you keep an export current across runs: persist the final page's `last_id` and resume from it as `after_id` on the next run. Because the list is ordered by `updated_at`, a chat reappears ahead of your saved cursor when it receives a new message, is moved into or out of a project, or is deleted in claude.ai. Each incremental run therefore returns both brand-new chats and older chats that have since changed in one of those ways. Other edits, such as a rename, are not guaranteed to make a chat reappear. Process results idempotently, keyed by chat `id`, to handle those reappearances. A chat that comes back with `deleted_at` populated has no content left to fetch, so treat it as deleted rather than updated.

A few constraints apply to these organization-wide queries. Cursors are opaque and bound to the sort key, so an `after_id` issued under one `order_by` value is rejected with a 400 error under the other. Time-filter bounds must match the sort key too: pair `updated_at.*` bounds with `order_by=updated_at`, and `created_at.*` bounds with the default `order_by=created_at`. Backward pagination with `before_id` is not supported, and the `project_ids[]` filter is not available. See [List chats](../Admin/compliance-apps-chats-list.md) for the full filter reference.

To scope the list to specific users instead (for example, a legal hold on named custodians), pass 1–10 `user_ids[]` values. Obtain the IDs from [List organization users](manage-claude-compliance-org-data.md#list-organization-users). User-filtered queries always sort by `created_at` (passing `order_by=updated_at` returns a 400 error) and support both `after_id` and `before_id`. Filtering by `project_ids[]` is only available in this user-filtered form. Combining `user_ids[]` with any `updated_at.*` bound is deprecated and will be rejected with a 400 error after 2026-09-22; to keep a custodian set current by update time, run the org-wide `order_by=updated_at` walk without `user_ids[]` and select the custodians' chats from its results, and keep the user-filtered listing for `created_at`-ordered exports.

cURL



```python
curl --fail-with-body -sS -G \
  "https://api.anthropic.com/v1/compliance/apps/chats" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --header "anthropic-version: 2023-06-01" \
  --data-urlencode "user_ids[]=user_01XyDMpzjS89pFZXqSFUBDr6" \
  --data-urlencode "created_at.gte=2025-06-01T00:00:00Z" \
  --data-urlencode "limit=100"
```

The list response carries chat metadata only. To pull the actual chat content, attached files, and inline artifacts (structured documents Claude generates inside a chat), follow up with the messages endpoint for each chat ID:

cURL



```python
chat_id="claude_chat_01H5CWunD7RpVJ5bHa8RCkja"

curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/apps/chats/$chat_id/messages" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --header "anthropic-version: 2023-06-01"
```

The messages endpoint returns the chat's metadata plus a `chat_messages` array sorted by `created_at`. When `limit` is omitted, the full message set is returned in one response; pass `limit`, `after_id`, or `before_id` to page through very long chats. The endpoint also accepts `created_at.*` and `updated_at.*` range bounds (`gt`, `gte`, `lt`, `lte`) and an `order` parameter (`asc` or `desc`). See [Get chat messages](../Admin/compliance-apps-chats-messages-list.md) for the full parameter list. For user messages, `created_at` is when the message was sent; for assistant messages, it is when Claude finished generating the message. Each message carries its text content and, when present, any uploaded files (typically on user messages), any tool-generated files, and any artifacts the assistant produced or updated (typically on assistant messages):

Response



```python
{
  "id": "claude_chat_01H5CWunD7RpVJ5bHa8RCkja",
  "name": "Product Requirements Discussion",
  "created_at": "2026-04-10T08:09:10Z",
  "updated_at": "2026-04-10T09:10:11Z",
  "deleted_at": null,
  "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789",
  "model": "claude-opus-5-5",
  "organization_uuid": "91012d09-e48b-438e-a489-1bebfd8fa6f9",
  "project_id": "claude_proj_01KGp4eZNug9ri4kE35RSppq",
  "user": {
    "id": "user_01XyDMpzjS89pFZXqSFUBDr6",
    "email_address": "user@example.com"
  },
  "chat_messages": [
    {
      "id": "claude_chat_msg_01VnBPkLmtj7YdW5QrXKEA8c",
      "role": "user",
      "created_at": "2026-04-10T08:09:10Z",
      "content": [
        {
          "type": "text",
          "text": "Can you help me draft requirements for our new dashboard feature?"
        }
      ],
      "files": [
        {
          "id": "claude_file_01UaT9wBcDfGhJkLmNpQrSv7",
          "filename": "dashboard_mockup_v1.pdf",
          "mime_type": "application/pdf",
          "size_bytes": 482133,
          "md5": "56367e4d2705cc9c025ad07424e944f0",
          "created_at": "2026-04-10T08:09:10Z"
        }
      ]
    },
    {
      "id": "claude_chat_msg_01M8tFcHwbQ2kY6NpEjRZv4D",
      "role": "assistant",
      "created_at": "2026-04-10T08:09:11Z",
      "content": [
        {
          "type": "text",
          "text": "I'd be happy to help you draft requirements for your dashboard feature..."
        }
      ],
      "generated_files": [
        {
          "id": "claude_gen_file_01TbR8wAcCeFhJkLnPqStUvX",
          "filename": "requirements_summary.csv",
          "mime_type": "text/csv",
          "size_bytes": 2048,
          "md5": "89968669461d95416549937168269d6b"
        }
      ],
      "artifacts": [
        {
          "id": "claude_artifact_01HqRsTuVwXyZa2BcDeFgH4J",
          "version_id": "claude_artifact_version_01KmNpQrSt3UvWxYz5AbCdEfG",
          "title": "Dashboard Requirements Draft",
          "artifact_type": "text/markdown"
        }
      ]
    }
  ],
  "has_more": false,
  "first_id": "eyJtc2dfdXVpZCI6ICIwZjcwYjA2Ni0uLi4ifQ==",
  "last_id": "eyJtc2dfdXVpZCI6ICJhNGUwYjE3Mi0uLi4ifQ=="
}
```

`files`, `generated_files`, and `artifacts` can each be `null` on a given message. `files` are the files and text attachments (for example, PDFs, images, spreadsheets, documents, and pasted text) the user attached to the message, as claude.ai stored them. `generated_files` are binary files the assistant created during the conversation through tool use (for example, PDFs, spreadsheets, or slide decks). `artifacts` are versioned documents (for example, code or markdown) the assistant generated or updated in its response; an artifact can be revised across multiple assistant turns in the same chat, and each revision appears as a new `version_id` under the same artifact `id`. Pass each entry's `id` (or `version_id` for artifacts) to the matching content endpoint in [Retrieve files and artifacts](#retrieve-files-and-artifacts) to download it.

## Retrieve files and artifacts

Files and artifacts are downloaded by ID, not listed independently. The IDs come from the chat messages endpoint in [Retrieve chats and messages](#retrieve-chats-and-messages) (the `files`, `generated_files`, and `artifacts` arrays on each message) or, for project-level uploads, from the [project attachments endpoint](#retrieve-projects-and-attachments).

Pick the endpoint that matches your ID type and the data you need. The same file content endpoint serves both chat files and project files.

| You have                       | You want                                | Use this endpoint                                                                               |
|--------------------------------|-----------------------------------------|-------------------------------------------------------------------------------------------------|
| `claude_file_*` ID             | The file's content                      | [Download file content](../Admin/compliance-apps-chats-files-download.md)                      |
| `claude_file_*` ID             | The file's metadata only                | [Get file metadata](../Admin/compliance-apps-chats-files-retrieve.md)                          |
| `claude_gen_file_*` ID         | A tool-generated file's binary content  | [Download a Claude-generated file](../Admin/compliance-apps-chats-generated-files-download.md) |
| `claude_gen_file_*` ID         | A tool-generated file's metadata only   | [Get generated-file metadata](../Admin/compliance-apps-chats-generated-files-retrieve.md)      |
| `claude_artifact_version_*` ID | One artifact version's text             | [Download artifact content](../Admin/compliance-apps-artifacts-download.md)                    |
| `claude_artifact_version_*` ID | The artifact version's metadata only    | [Get artifact metadata](../Admin/compliance-apps-artifacts-retrieve.md)                        |
| `claude_proj_doc_*` ID         | A project document's plain-text content | [Get project document content](../Admin/compliance-apps-projects-documents-retrieve.md)        |
| `claude_proj_doc_*` ID         | A project document's metadata only      | [Get project document metadata](../Admin/compliance-apps-projects-documents-metadata.md)       |

The file content endpoint streams the content that claude.ai stored for the file as a chunked binary response. That content is not always identical to the file the user uploaded. Images can be served as a processed copy rather than the uploaded bytes. Some documents attached to chats (for example, Word files, PowerPoint files, and some PDFs) are stored as the text claude.ai extracted from them. For these documents, the endpoint returns the extracted text under the original file name, and the original document is not available through the Compliance API. The `size_bytes` and `md5` fields describe the stored content rather than the uploaded file. The file name and `mime_type` can still name the uploaded document's format. Identify a file's format from the returned bytes, not from its name or declared type.

The response carries these headers:

- `Content-Disposition: attachment; filename*=utf-8''<percent-encoded filename>` carries the original upload file name in RFC 5987 extended form. The extended form is used for every file name, not only non-ASCII ones.
- `Content-Type` carries the MIME type recorded for the stored content, which for a document stored as extracted text can still name the original document format.
- `Content-MD5` carries the MD5 digest of the served bytes, base64-encoded as specified in RFC 1864.
- `Transfer-Encoding: chunked` is always set.

cURL



```python
file_id="claude_file_01UaT9wBcDfGhJkLmNpQrSv7"

curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/apps/chats/files/$file_id/content" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --header "anthropic-version: 2023-06-01" \
  --output "dashboard_mockup_v1.pdf"
```

In curl, the `--remote-header-name` (`-J`) option, which normally saves a download under the `Content-Disposition` file name, does not read the `filename*` form, so name the saved file yourself with `--output`. In a script, take the name from the file's `filename` field in the chat messages or [Get file metadata](../Admin/compliance-apps-chats-files-retrieve.md) response, or decode `filename*`. Either way, it is the name the user gave the upload, so treat it as untrusted before using it as an output path: keep only the base name, allow only characters that are safe on your filesystem, and refuse names that begin with `-` or `.`.

Unlike the file content endpoint, the artifact content endpoint returns a JSON object. Pass the `version_id` from one of the entries in an assistant message's `artifacts` array, not the artifact's stable `id`; each new version of an artifact has its own `version_id`. The response's `content` field holds exactly that version's text, and its `title` and `artifact_type` fields describe the artifact. [Get artifact metadata](../Admin/compliance-apps-artifacts-retrieve.md) computes `size_bytes` and `md5` over the UTF-8 encoding of that text, so compare them with the `content` value rather than the whole response body.

## Retrieve projects and attachments

Projects bundle related chats together with custom instructions, knowledge base content, and attached files or text documents. The Compliance API exposes project metadata, project details, and the list of attachments belonging to a project.

- [List projects](../Admin/compliance-apps-projects-list.md)
- [Get project details](../Admin/compliance-apps-projects-retrieve.md)
- [List project attachments](../Admin/compliance-apps-projects-attachments-list.md)
- [Get project document content](../Admin/compliance-apps-projects-documents-retrieve.md)

Project results are sorted by creation date ascending. Attachment results are sorted by `created_at` ascending, with ties broken by `id`. Project list and attachment list responses paginate with an opaque `next_page` page token instead of the `first_id`/`last_id` cursors used by chats and the Activity Feed. Pass the token back as the `page` query parameter on the next request.

### Project files versus project documents

A project attachment is one of two distinct shapes, identified by the `type` discriminator on each entry:

Entries with `type` of `project_file` are file uploads (PDFs, images, spreadsheets) whose IDs start with `claude_file_`; download them with [Download file content](../Admin/compliance-apps-chats-files-download.md). Entries with `type` of `project_doc` are plain-text documents (always `text/plain`) whose IDs start with `claude_proj_doc_`, including documents such as Word files that claude.ai converts to text when they are added to a project; fetch them with [Get project document content](../Admin/compliance-apps-projects-documents-retrieve.md).

A consumer that walks the attachment list must branch on `type` and call the matching content endpoint for each entry. The following request lists one page of attachments; paginate by passing `next_page` back as the `page` parameter until `has_more` is `false`.

cURL



```python
project_id="claude_proj_01KGp4eZNug9ri4kE35RSppq"

curl --fail-with-body -sS -G \
  "https://api.anthropic.com/v1/compliance/apps/projects/$project_id/attachments" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --header "anthropic-version: 2023-06-01"
```

Response



```python
{
  "data": [
    {
      "id": "claude_file_01UaT9wBcDfGhJkLmNpQrSv7",
      "created_at": "2026-04-10T08:09:10Z",
      "filename": "dashboard_mockup_v1.pdf",
      "mime_type": "application/pdf",
      "size_bytes": 482133,
      "md5": "56367e4d2705cc9c025ad07424e944f0",
      "type": "project_file"
    },
    {
      "id": "claude_proj_doc_01YnT8sBcWvUtXzQpMkRfDgH",
      "created_at": "2026-04-10T08:09:11Z",
      "filename": "requirements.md",
      "mime_type": "text/plain",
      "type": "project_doc"
    }
  ],
  "has_more": false,
  "next_page": null
}
```

## Delete content



Every successful delete is permanent and immediate. There is no recovery window.

The Compliance API exposes hard-delete endpoints for chats, files, project documents, and entire projects. A hard-deleted chat cannot be restored, and it stops appearing in list responses afterward.

- [Delete chat](../Admin/compliance-apps-chats-delete.md): also removes the chat's messages and any files attached to those messages.
- [Delete file](../Admin/compliance-apps-chats-files-delete.md): handles both chat files and project files.
- [Delete project document](../Admin/compliance-apps-projects-documents-delete.md): removes a single project document by ID.
- [Delete project](../Admin/compliance-apps-projects-delete.md): see [Detach chats before deleting a project](#detach-chats-before-deleting-a-project).

All four endpoints require the `delete:compliance_user_data` scope, which is granted separately from the read scope when the Compliance Access Key is created.

The following request deletes one chat. The same pattern applies to the other delete endpoints; only the URL changes.

cURL



```python
# WARNING: This operation PERMANENTLY deletes the chat, all of its messages,
# and any attached files. Deletion is immediate and cannot be undone. It
# requires the `delete:compliance_user_data` scope, which is granted separately
# from `read:compliance_user_data` when the Compliance Access Key is created.
# Ensure you have explicit authorization before running this.

chat_id="claude_chat_01H5CWunD7RpVJ5bHa8RCkja"

curl --fail-with-body -sS -X DELETE \
  "https://api.anthropic.com/v1/compliance/apps/chats/$chat_id" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --header "anthropic-version: 2023-06-01"
```

Response



```python
{
  "id": "claude_chat_01H5CWunD7RpVJ5bHa8RCkja",
  "type": "claude_chat_deleted"
}
```

Each successful delete returns a small confirmation envelope with an `id` and a `type` discriminator. The chat endpoint returns `claude_chat_deleted`; check the `type` field before treating the delete as confirmed. See the response schema on each delete endpoint's [API reference](../Admin/compliance-apps.md) page for the exact `type` value the other endpoints return.

### Detach chats before deleting a project

A project cannot be deleted while any chats remain attached to it. The API returns 409 with this body:

```python
{
  "error": {
    "type": "invalid_request_error",
    "message": "The \"claude_proj_01KGp4eZNug9ri4kE35RSppq\" project cannot be deleted as it has chats attached to it. Delete or detach all chats, and try deleting the project again."
  }
}
```



To resolve, list the project's chats with `GET /v1/compliance/apps/chats?user_ids[]={user_id}&project_ids[]={project_id}` (the `project_ids[]` filter requires at least one `user_ids[]` value; enumerate IDs through [List organization users](manage-claude-compliance-org-data.md#list-organization-users)), delete each one with `DELETE /v1/compliance/apps/chats/{claude_chat_id}` (or move it out of the project from claude.ai), and then retry the project delete.

## Next steps

[API reference](../Admin/compliance-apps.md)

The full request and response schema for every chat, file, project, and artifact endpoint.

[Retrieve session transcripts](manage-claude-compliance-sessions.md)

List the sessions your users run in Claude apps and agents, such as Cowork and Claude Code, and retrieve their transcripts.

[List organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)

Enumerate the people and teams associated with the chats and projects on this page.
