---
title: "Adding files - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/files"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:39Z"
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Ffiles)





SearchCtrlK

First steps

[Overview](managed-agents-overview.md)[Quickstart](managed-agents-quickstart.md)[Build in Console](managed-agents-onboarding.md)[Migration](managed-agents-migration.md)

Define your agent

[Agent setup](managed-agents-agent-setup.md)[Tools](managed-agents-tools.md)[MCP connector](managed-agents-mcp-connector.md)[Permission policies](managed-agents-permission-policies.md)[Agent Skills](managed-agents-skills.md)

Configure agent environment

[Cloud environment setup](managed-agents-environments.md)[Cloud sandbox reference](managed-agents-cloud-sandboxes-reference.md)

[Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md)

Delegate work to your agent

[Start a session](managed-agents-sessions.md)[Session operations](managed-agents-session-operations.md)[Session event stream](managed-agents-events-and-streaming.md)[Session budgets](managed-agents-budgets.md)[Subscribe to webhooks](managed-agents-webhooks.md)[Define outcomes](managed-agents-define-outcomes.md)[Authenticate with vaults](managed-agents-vaults.md)

Manage agent context

[Access GitHub](managed-agents-github.md)[Attach and download files](managed-agents-files.md)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](managed-agents-multiagent-orchestration.md)[Scheduled deployments](managed-agents-scheduled-deployments.md)

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

[Console](usage-limits.md)

[Managed Agents](managed-agents-overview.md)Manage agent context

# Adding files

Copy page



Upload files and mount them in your sandbox for reading and processing.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

You can provide files to your agent by uploading them through the Files API and mounting them in the session's sandbox.

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



```python
resources = [
    {"type": "file", "file_id": "file_abc123", "mount_path": "/data.csv"},
    {"type": "file", "file_id": "file_def456", "mount_path": "/config.json"},
    {"type": "file", "file_id": "file_ghi789", "mount_path": "/src/main.py"},
]
```

A maximum of 500 files is supported per session.

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



```python
resource = client.beta.sessions.resources.add(
    session.id,
    type="file",
    file_id=file.id,
)
print(resource.id)  # "sesrsc_01ABC..."
```

List all resources on a session with `resources.list`. To remove a file, call `resources.delete` with the resource ID:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
listed = client.beta.sessions.resources.list(session.id)
for entry in listed.data:
    print(entry.id, entry.type)

client.beta.sessions.resources.delete(resource.id, session_id=session.id)
```

## Listing and downloading session files

Use the [Files API](../Guides/build-with-claude-files.md) to list files scoped to a session and download them. Files the agent writes to `/mnt/session/outputs/` appear in the list shortly after the agent finishes writing them, sometimes a few seconds after the session goes idle. If an output file you expect is missing, list again after a short delay; once it appears in the list, its upload has finished.

Filtering by `scope_id` requires the `managed-agents-2026-04-01` beta header, so the list examples use the `beta` files namespace and pass that header explicitly.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

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

- The path you specify is rooted under the session's uploads directory: a `mount_path` of `/data.csv` places the file at `/mnt/session/uploads/data.csv` in the sandbox
- If you omit `mount_path`, the file is placed at `/mnt/session/uploads/<file_id>`
- Parent directories are created automatically
- Paths should be absolute (starting with `/`)
- Files the agent writes to `/mnt/session/outputs/` become available through the Files API, scoped to the session; see [Listing and downloading session files](#listing-and-downloading-session-files)
