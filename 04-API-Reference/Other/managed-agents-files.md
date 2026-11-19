---
title: "Adding files - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/files"
category: "04-API-Reference/Other"
fetched_at: "2026-11-13T06:35:08Z"
tags: ["api"]
---

# Adding files

Copy page



Upload files and mount them in your sandbox for reading and processing.

Copy page



[Managed Agents](managed-agents-overview.md)

Beta

[Models](managed-agents-overview.md#feature-availability)  
- All models

[Cloud platforms](managed-agents-overview.md#feature-availability)  
- Claude API
- Claude Platform on AWS
- Claude Models on Google CloudAnthropic managed

[Beta header](managed-agents-overview.md#feature-availability)  
- 
  Copy`managed-agents-2026-04-01`

[Data handling](managed-agents-overview.md#feature-data-handling)  
ZDRNot ZDR eligibleHIPAANot HIPAA eligible

You can provide files to your agent by uploading them through the Files API and mounting them in the session’s sandbox.

## Uploading files

First, upload a file using the [Files API](../Guides/build-with-claude-files.md):

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
file = client.files.upload(file=Path("data.csv"))
print(f"File ID: {file.id}")
```

## Mounting files in a session

Mount uploaded files into the sandbox by adding them to the `resources` array when creating a session:



The `mount_path` is optional, but make sure the uploaded file has a descriptive name so the agent can identify it.

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
    resources=[
        {
            "type": "file",
            "file_id": file.id,
            "mount_path": "/data.csv",
        },
    ],
)
```

With the preceding `mount_path`, the agent reads the file at `/mnt/session/uploads/data.csv` (see [File paths](#file-paths)).

A new `file_id` is created that references the instance of the file in the session. These copies do not count against your [storage limits](../Guides/build-with-claude-files.md).

## Multiple files

Mount multiple files by adding entries to the `resources` array:

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
resources = [
    {"type": "file", "file_id": "file_abc123", "mount_path": "/data.csv"},
    {"type": "file", "file_id": "file_def456", "mount_path": "/config.json"},
    {"type": "file", "file_id": "file_ghi789", "mount_path": "/src/main.py"},
]
```

A maximum of 500 files is supported for each session.

## Managing files on a running session

You can add or remove files from a session after creation using the session resources API. Each resource has an `id` returned when it is added (or listed), which you use for deletes.

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
resource = client.beta.sessions.resources.add(
    session.id,
    type="file",
    file_id=file.id,
)
print(resource.id)  # "sesrsc_01ABC..."
```

List all resources on a session with `client.beta.sessions.resources.list()`. To remove a file, call `client.beta.sessions.resources.delete()` with the resource ID:

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
listed = client.beta.sessions.resources.list(session.id)
for entry in listed.data:
    print(entry.id, entry.type)

client.beta.sessions.resources.delete(resource.id, session_id=session.id)
```

## Listing and downloading session files

Use the [Files API](../Guides/build-with-claude-files.md) to list files scoped to a session and download them. Files the agent writes to `/mnt/session/outputs/` appear in the list shortly after the agent finishes writing them, sometimes a few seconds after the session goes idle. If an output file you expect is missing, list again after a short delay; once it appears in the list, its upload is complete.

Filtering by `scope_id` requires the `managed-agents-2026-04-01` beta header, so the list examples call `client.beta.files.list()` and pass that header explicitly.

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
# List files associated with a session
files = client.beta.files.list(
    scope_id="sesn_abc123",
    betas=["managed-agents-2026-04-01"],
)
for file in files:
    print(file.id, file.filename)

# Download a file
content = client.files.download(files.data[0].id)
content.write_to_file("output.txt")
```

## Supported file types

The agent can work with any file type, including:

- Source code (`.py`, `.js`, `.ts`, `.go`, `.rs`, and others)
- Data files (`.csv`, `.json`, `.xml`, `.yaml`)
- Documents (`.txt`, `.md`)
- Archives (`.zip`, `.tar.gz`) - the agent can extract these using bash
- Binary files - the agent can process these with appropriate tools

## File paths



Files mounted in the sandbox are read-only copies. The agent can read them but cannot modify the original uploaded file. To work with modified versions, the agent writes to new paths within the sandbox.

- The path you specify is rooted under the session’s uploads directory: a `mount_path` of `/data.csv` places the file at `/mnt/session/uploads/data.csv` in the sandbox.
- If you omit `mount_path`, the file is placed at `/mnt/session/uploads/<file_id>`.
- Parent directories are created automatically.
- Paths should be absolute (starting with `/`).
- Files the agent writes to `/mnt/session/outputs/` become available through the Files API, scoped to the session; see [Listing and downloading session files](#listing-and-downloading-session-files).
