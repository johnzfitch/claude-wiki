---
title: "Api Cli Beta Files Delete C02F26C521"
source_url: "https://platform.claude.com/docs/en/api/cli/beta/files/delete.md"
category: "Other"
fetched_at: "2026-04-26T00:00:00Z"
tags: ["api", "cli"]
---

## Delete

`$ ant beta:files delete`

**delete** `/v1/files/{file_id}`

Delete File

### Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `deleted_file: object { id, type }`

  - `id: string`

    ID of the deleted file.

  - `type: optional "file_deleted"`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"`

### Example

```cli
ant beta:files delete \
  --api-key my-anthropic-api-key \
  --file-id file_id
```
