---
title: "Cloud sandbox reference - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/cloud-sandboxes-reference"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:47Z"
tags: ["api"]
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fcloud-sandboxes-reference)

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

[Managed Agents](/docs/en/managed-agents/overview)Configure agent environment

# Cloud sandbox reference

Copy page



Pre-installed packages, databases, and utilities available in cloud sandboxes.

Copy page



[Managed Agents](/docs/en/managed-agents/overview)

[Beta](/docs/en/build-with-claude/overview#feature-availability)

[Beta header](/docs/en/api/beta-headers)

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
| Network          | API-created environments default to [`unrestricted` networking](/docs/en/managed-agents/environments#networking); sandboxes provisioned through Claude Studio default to `limited` |
