---
title: "Cloud sandbox reference - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/cloud-sandboxes-reference"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:47Z"
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fcloud-sandboxes-reference)

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

[Managed Agents](managed-agents-overview.md)Configure agent environment

# Cloud sandbox reference

Copy page



Pre-installed packages, databases, and utilities available in cloud sandboxes.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

Cloud sandboxes run as isolated Linux containers on Anthropic-managed infrastructure. They come pre-installed with a comprehensive set of programming languages, databases, and utilities. The agent can use these immediately without any installation steps.

These specifications apply to `cloud` environments. Self-hosted sandboxes run on your infrastructure with whatever your worker provides.

## Programming languages

| Language | Version                     | Package manager      |
|----------|-----------------------------|----------------------|
| Python   | 3.10, 3.11, 3.12, and 3.13  | pip, uv, poetry      |
| Node.js  | 20, 21, and 22 (default)    | npm, yarn, pnpm, bun |
| Go       | 1.24 (default) and 1.25     | go modules           |
| Rust     | Stable toolchain (rustup)   | cargo                |
| Java     | OpenJDK 21                  | maven, gradle        |
| Ruby     | 3.1, 3.2, and 3.3 (default) | bundler, gem         |
| PHP      | 8.3                         | composer             |
| C/C++    | GCC 13 and Clang            | make, cmake, ninja   |

Common Python data and document libraries, including NumPy, pandas, Matplotlib, openpyxl, python-docx, python-pptx, and pypdf, are installed for the `python3` interpreter.

## Databases

| Database      | Description                                                                   |
|---------------|-------------------------------------------------------------------------------|
| PostgreSQL 16 | Server and `psql` client are installed. The server is not running by default. |
| Redis 7       | Server and `redis-cli` are installed. The server is not running by default.   |
| SQLite        | Available through language bindings, such as Python's `sqlite3` module.       |

## Utilities

### System tools

- `git` - Version control
- `curl`, `wget` - HTTP clients
- `jq`, `yq` - JSON and YAML processing
- `tar`, `zip`, `unzip` - Archive tools
- `tmux` - Terminal multiplexer

### Development tools

- `make`, `cmake` - Build systems
- `docker` - Container management (limited availability)
- `ripgrep` (`rg`) - Fast file search

### Text processing

- `sed`, `awk`, `grep` - Stream editors
- `vim`, `nano` - Text editors
- `diff`, `patch` - File comparison

### Document and media processing

- `ffmpeg` - Audio and video processing
- ImageMagick (`convert`, `identify`) - Image manipulation
- `pandoc` - Document conversion
- LibreOffice (headless) - Office document conversion
- Poppler utilities (`pdftotext`, `pdftoppm`) and `qpdf` - PDF processing
- `tesseract` - Optical character recognition (English language data)
- TeX Live (`pdflatex`, `xelatex`, `latexmk`) - Typesetting

### Browser automation

- Playwright (Python and Node.js) - Browser automation library
- Chromium (`/opt/pw-browsers/chromium`) - Browser used by Playwright, not on `PATH`

The sandbox sets `PLAYWRIGHT_BROWSERS_PATH` to `/opt/pw-browsers`, so the pre-installed Playwright packages find Chromium there without configuration. The Python package is installed for the `python3` interpreter. Use the pre-installed packages rather than installing another Playwright version, which would look for a browser build that is not present. Firefox and WebKit are not installed.

## Sandbox specifications

| Property         | Value                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Operating system | Ubuntu 24.04 LTS                                                                                                                                                                   |
| Architecture     | x86_64 (amd64)                                                                                                                                                                     |
| Memory           | Up to 8 GB                                                                                                                                                                         |
| Disk space       | Up to 10 GB                                                                                                                                                                        |
| Network          | API-created environments default to [`unrestricted` networking](managed-agents-environments.md#networking); sandboxes provisioned through Claude Studio default to `limited` |
