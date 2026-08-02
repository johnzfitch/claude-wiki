---
title: "Adding files - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/files"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:41:18Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


First steps

[Overview](/docs/en/managed-agents/overview)[Quickstart](/docs/en/managed-agents/quickstart)[Prototype in Console](/docs/en/managed-agents/onboarding)[Migration](/docs/en/managed-agents/migration)

Define your agent

[Agent setup](/docs/en/managed-agents/agent-setup)[Tools](/docs/en/managed-agents/tools)[MCP connector](/docs/en/managed-agents/mcp-connector)[Permission policies](/docs/en/managed-agents/permission-policies)[Agent Skills](/docs/en/managed-agents/skills)

Configure agent environment

[Cloud environment setup](/docs/en/managed-agents/environments)[Cloud sandbox reference](/docs/en/managed-agents/cloud-sandboxes-reference)

Self-hosted sandboxes

Delegate work to your agent

[Start a session](/docs/en/managed-agents/sessions)[Session operations](/docs/en/managed-agents/session-operations)[Session event stream](/docs/en/managed-agents/events-and-streaming)[Subscribe to webhooks](/docs/en/managed-agents/webhooks)[Define outcomes](/docs/en/managed-agents/define-outcomes)[Authenticate with vaults](/docs/en/managed-agents/vaults)

Manage agent context

[Access GitHub](/docs/en/managed-agents/github)[Attach and download files](/docs/en/managed-agents/files)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](/docs/en/managed-agents/multiagent-orchestration)[Scheduled deployments](/docs/en/managed-agents/scheduled-deployments)

Reference

[Managed Agents reference](/docs/en/managed-agents/reference)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

Images and vision

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)

MCP tunnels

Claude on cloud platforms

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)

[](/login)




Managed Agents

Attach and download files

Managed Agents/Manage agent context

# Adding files




Upload files and mount them in your sandbox for reading and processing.




You can provide files to your agent by uploading them through the Files API and mounting them in the session's sandbox.



Managed Agents API requests require the `managed-agents-2026-04-01` beta header, except memory store endpoints, which use `agent-memory-2026-07-22` instead. The SDK sets the correct beta header automatically. See [Beta headers](/docs/en/api/beta-headers#endpoint-specific-headers).




Uploading files

First, upload a file using the [Files API](/docs/en/build-with-claude/files):

curl

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
file = client.beta.files.upload(file=Path("data.csv"))
print(f"File ID: {file.id}")
```




Mounting files in a session

Mount uploaded files into the sandbox by adding them to the `resources` array when creating a session:



The `mount_path` is optional, but make sure the uploaded file has a descriptive name so the agent can identify it.

curl

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

A new `file_id` is created that references the instance of the file in the session. These copies do not count against your [storage limits](/docs/en/build-with-claude/files).




Multiple files

Mount multiple files by adding entries to the `resources` array:

curl

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




Managing files on a running session

You can add or remove files from a session after creation using the session resources API. Each resource has an `id` returned when it is added (or listed), which you use for deletes.

curl

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

curl

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




Listing and downloading session files

Use the [Files API](/docs/en/build-with-claude/files) to list files scoped to a session and download them.

curl

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
content = client.beta.files.download(files.data[0].id)
content.write_to_file("output.txt")
```




Supported file types

The agent can work with any file type, including:

- Source code (`.py`, `.js`, `.ts`, `.go`, `.rs`, and others)
- Data files (`.csv`, `.json`, `.xml`, `.yaml`)
- Documents (`.txt`, `.md`)
- Archives (`.zip`, `.tar.gz`) - the agent can extract these using bash
- Binary files - the agent can process these with appropriate tools




File paths



Files mounted in the sandbox are read-only copies. The agent can read them but cannot modify the original uploaded file. To work with modified versions, the agent writes to new paths within the sandbox.

- The path you specify is rooted under the session's uploads directory: a `mount_path` of `/data.csv` places the file at `/mnt/session/uploads/data.csv` in the sandbox
- If you omit `mount_path`, the file is placed at `/mnt/session/uploads/<file_id>`
- Parent directories are created automatically
- Paths should be absolute (starting with `/`)
