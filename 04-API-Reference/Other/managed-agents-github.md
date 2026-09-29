---
title: "Accessing GitHub - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/github"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:40Z"
tags: ["api", "git", "github", "mcp"]
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fgithub)

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

# Accessing GitHub

Copy page



Connect your agent to GitHub repositories for cloning, reading, and creating pull requests.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

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

Mounting a repository also loads any skills stored in its root `.claude/skills` directory. Skills are discovered once per session, from the repository state checked out at session start. See [Load skills from a GitHub repository](managed-agents-skills.md#load-skills-from-a-github-repository).

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

[Session event stream](managed-agents-events-and-streaming.md)

Stream events and steer the agent while it opens the pull request



[MCP connector](managed-agents-mcp-connector.md)

Connect more MCP servers to give the agent additional tools



[Adding files](managed-agents-files.md)

Mount files in the sandbox alongside your repositories
