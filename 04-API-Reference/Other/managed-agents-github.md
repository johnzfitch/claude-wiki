---
title: "Accessing GitHub - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/github"
category: "04-API-Reference/Other"
fetched_at: "2026-11-13T06:36:50Z"
tags: ["api", "git", "github", "mcp"]
---

# Accessing GitHub

Copy page



Connect your agent to GitHub repositories for cloning, reading, and creating pull requests.

Copy page




Beta

Feature of  
[Managed Agents](managed-agents-overview.md)

[Models](#feature-availability)  
- All models

[Cloud platforms](#feature-availability)  
- Claude API
- Claude Platform on AWS
- Claude Models on Google CloudAnthropic managed

[Beta header](#feature-availability)  
- 
  Copy`managed-agents-2026-04-01`

[Data handling](#feature-data-handling)  
ZDRNot ZDR eligibleHIPAANot HIPAA eligible

You can mount a GitHub repository to your session sandbox and connect to the GitHub MCP for making pull requests.


## GitHub MCP and session resources

First, create an agent that declares the GitHub MCP server. The agent definition holds the server URL but no authentication token:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

CLI



```python
ant apply code-reviewer.md
```

code-reviewer.md





```python
---
name: Code Reviewer
model: claude-opus-5-5
mcp_servers:
  - type: url
    name: github
    url: https://api.githubcopilot.com/mcp/
tools:
  - type: agent_toolset_20260401
    configs:
      - name: web_search
        enabled: false
      - name: web_fetch
        enabled: false
  - type: mcp_toolset
    mcp_server_name: github
---

You are a code review assistant with access to GitHub.
```

Then create a session that mounts the GitHub repository. With a `limited` [environment](managed-agents-environments.md#networking), session creation fails with a 400 error when the agent declares an MCP server whose host is not in `allowed_hosts`. Setting `allow_mcp_servers` to `true` in the environment’s networking turns this check off.

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
            "type": "github_repository",
            "url": "https://github.com/org/repo",
            "mount_path": "/workspace/repo",
            "authorization_token": "ghp_your_github_token",
        },
    ],
)
```

A `github_repository` resource accepts the following fields:

| Field | Description |
|----|----|
| `type` | Required. Must be `"github_repository"`. |
| `url` | Required. The repository’s HTTPS URL in the form `https://github.com/<owner>/<repo>`, without a `.git` suffix. Other forms, including SSH URLs, are rejected with an `invalid_request_error`. |
| `authorization_token` | Optional. The GitHub token used to clone the repository and to push to it. Without a token, a private repository fails to clone after the session is created. A public repository clones without a token, and the agent can commit in its clone, but `git push` fails. It is not echoed in API responses. See [Token permissions](#token-permissions). |
| `mount_path` | Optional. The directory under `/workspace` to clone the repository into. Defaults to `/workspace/<repo-name>`. |
| `checkout` | Optional. A branch (`{"type": "branch", "name": "main"}`) or commit (`{"type": "commit", "sha": "..."}`) to check out. Defaults to the repository’s default branch. |

Mounting a repository also loads any skills stored in its root `.claude/skills` directory. Skills are discovered once for each session, from the repository state checked out at session start. See [Load skills from a GitHub repository](managed-agents-skills.md#load-skills-from-a-github-repository).

## Token permissions

When providing a GitHub token, use the minimum required permissions:

| Action              | Required scopes                   |
|---------------------|-----------------------------------|
| Clone private repos | `repo`                            |
| Create PRs          | `repo`                            |
| Read issues         | `repo` (private) or `public_repo` |
| Create issues       | `repo` (private) or `public_repo` |



Use fine-grained personal access tokens with minimum required permissions. Avoid using tokens with broad access to your GitHub account.

## Multiple repositories

Mount multiple repositories by adding entries to the `resources` array:

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
    {
        "type": "github_repository",
        "url": "https://github.com/org/frontend",
        "mount_path": "/workspace/frontend",
        "authorization_token": "ghp_your_github_token",
    },
    {
        "type": "github_repository",
        "url": "https://github.com/org/backend",
        "mount_path": "/workspace/backend",
        "authorization_token": "ghp_your_github_token",
    },
]
```

## Managing repositories on a running session

After a session is created, you can list its repository resources and rotate their authorization tokens. Each resource has an `id` returned at session creation time (or through `client.beta.sessions.resources.list()`) that you use for updates. Repositories are attached for the lifetime of the session; to change which repositories are mounted, create a new session.

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
# List resources on the session
listed = client.beta.sessions.resources.list(session.id)
repo_resource_id = listed.data[0].id
print(repo_resource_id)  # "sesrsc_01ABC..."

# Rotate the authorization token
client.beta.sessions.resources.update(
    repo_resource_id,
    session_id=session.id,
    authorization_token="ghp_your_new_github_token",
)
```

## Creating pull requests

With the GitHub MCP server, the agent can create branches, commit changes, and push them:

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
client.beta.sessions.events.send(
    session.id,
    events=[
        {
            "type": "user.message",
            "content": [
                {
                    "type": "text",
                    "text": "Fix the type error in src/utils.ts, commit it to a new branch, and push it.",
                },
            ],
        },
    ],
)
```

## Next steps



[Session event stream](managed-agents-events-and-streaming.md)

Stream events and steer the agent while it opens the pull request



[MCP connector](managed-agents-mcp-connector.md)

Connect more MCP servers to give the agent additional tools



[Adding files](managed-agents-files.md)

Mount files in the sandbox alongside your repositories

## Availability


Cloud platform

Cloud platform: Claude API

Availability requirements for GitHub access are the same across all supported platforms.

Claude API

Status  
Beta

API  
- Managed Agents

Beta header  
Requires

managed-agents-2026-04-01

Models  
- All models

Claude Platform on AWS

Status  
Beta

API  
- Managed Agents

Beta header  
Requires

managed-agents-2026-04-01

Models  
- All models

Claude Models on Google Cloud (Anthropic managed)

Status  
Beta

API  
- Managed Agents

Beta header  
Requires

managed-agents-2026-04-01

Models  
- All models

### Data handling

[Data handling overview](manage-claude-api-and-data-retention.md#feature-eligibility)

Applicable endpoints

- `/v1/agents`
- `/v1/sessions`
- `/v1/environments`

Zero data retentionNot eligible

Not eligible for ZDR, except for self-hosted Managed Agents. Sessions are stateful resources; transcripts persist until you delete them. [Learn more](managed-agents-self-hosted-data-and-access.md#how-long-data-is-kept)

HIPAANot eligible

Not eligible for HIPAA. Applies to all Managed Agents sub-features.
