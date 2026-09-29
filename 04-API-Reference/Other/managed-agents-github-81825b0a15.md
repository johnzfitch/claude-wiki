---
title: "Accessing GitHub - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/github"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:40Z"
tags: ["api", "git", "github", "mcp"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fgithub)





SearchCtrlK

First steps

[Overview](/docs/en/managed-agents/overview)[Quickstart](/docs/en/managed-agents/quickstart)[Build in Console](/docs/en/managed-agents/onboarding)[Migration](/docs/en/managed-agents/migration)

Define your agent

[Agent setup](/docs/en/managed-agents/agent-setup)[Tools](/docs/en/managed-agents/tools)[MCP connector](/docs/en/managed-agents/mcp-connector)[Permission policies](/docs/en/managed-agents/permission-policies)[Agent Skills](/docs/en/managed-agents/skills)

Configure agent environment

[Cloud environment setup](/docs/en/managed-agents/environments)[Cloud sandbox reference](/docs/en/managed-agents/cloud-sandboxes-reference)

[Self-hosted sandboxes](/docs/en/managed-agents/self-hosted-sandboxes)

Delegate work to your agent

[Start a session](/docs/en/managed-agents/sessions)[Session operations](/docs/en/managed-agents/session-operations)[Session event stream](/docs/en/managed-agents/events-and-streaming)[Session budgets](/docs/en/managed-agents/budgets)[Subscribe to webhooks](/docs/en/managed-agents/webhooks)[Define outcomes](/docs/en/managed-agents/define-outcomes)[Authenticate with vaults](/docs/en/managed-agents/vaults)

Manage agent context

[Access GitHub](/docs/en/managed-agents/github)[Attach and download files](/docs/en/managed-agents/files)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](/docs/en/managed-agents/multiagent-orchestration)[Scheduled deployments](/docs/en/managed-agents/scheduled-deployments)

Reference

[Managed Agents reference](/docs/en/managed-agents/reference)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

[Images and vision](/docs/en/build-with-claude/vision)

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)

[MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview)

Claude on cloud platforms

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)

[Console](/)

[Managed Agents](/docs/en/managed-agents/overview)Manage agent context

# Accessing GitHub

Copy page



Connect your agent to GitHub repositories for cloning, reading, and creating pull requests.

Copy page



[Managed Agents](/docs/en/managed-agents/overview)

[Beta](/docs/en/build-with-claude/overview#feature-availability)

[Beta header](/docs/en/api/beta-headers)

managed-agents-2026-04-01

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
  - type: mcp_toolset
    mcp_server_name: github
---

You are a code review assistant with access to GitHub.
```

Then create a session that mounts the GitHub repository:

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
            "type": "github_repository",
            "url": "https://github.com/org/repo",
            "mount_path": "/workspace/repo",
            "authorization_token": "ghp_your_github_token",
        },
    ],
)
```

A `github_repository` resource accepts the following fields:

| Field                 | Description                                                                                                                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`                | Required. Must be `"github_repository"`.                                                                                                                                                      |
| `url`                 | Required. The repository's HTTPS URL in the form `https://github.com/<owner>/<repo>`, without a `.git` suffix. Other forms, including SSH URLs, are rejected with an `invalid_request_error`. |
| `authorization_token` | Required. The GitHub token used to clone the repository. It is not echoed in API responses. See [Token permissions](#token-permissions).                                                      |
| `mount_path`          | Optional. The directory under `/workspace` to clone the repository into. Defaults to `/workspace/<repo-name>`.                                                                                |
| `checkout`            | Optional. A branch (`{"type": "branch", "name": "main"}`) or commit (`{"type": "commit", "sha": "..."}`) to check out. Defaults to the repository's default branch.                           |

Mounting a repository also loads any skills stored in its root `.claude/skills` directory. Skills are discovered once per session, from the repository state checked out at session start. See [Load skills from a GitHub repository](/docs/en/managed-agents/skills#load-skills-from-a-github-repository).

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

After a session is created, you can list its repository resources and rotate their authorization tokens. Each resource has an `id` returned at session creation time (or through `resources.list`) that you use for updates. Repositories are attached for the lifetime of the session; to change which repositories are mounted, create a new session.

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

[Session event stream](/docs/en/managed-agents/events-and-streaming)

Stream events and steer the agent while it opens the pull request



[MCP connector](/docs/en/managed-agents/mcp-connector)

Connect more MCP servers to give the agent additional tools



[Adding files](/docs/en/managed-agents/files)

Mount files in the sandbox alongside your repositories
