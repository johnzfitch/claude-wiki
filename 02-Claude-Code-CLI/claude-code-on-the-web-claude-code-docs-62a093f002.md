---
category: "02-Claude-Code-CLI"
fetched_at: "2026-02-23T00:45:39Z"
source_url: "https://code.claude.com/docs/en/claude-code-on-the-web"
title: "Claude Code on the web - Claude Code Docs"
---

[Skip to main content](#content-area)

[Claude Code Docs home page](/docs)

English

Search...

⌘K

Ask AI

- [Claude Developer Platform](https://platform.claude.com/)
- [Claude Code on the Web](https://claude.ai/code)
- [](https://claude.ai/code)
  Claude Code on the Web

Search...

Navigation

Platforms and integrations

Claude Code on the web

[Getting started](/docs/en/overview)

[Build with Claude Code](/docs/en/sub-agents)

[Deployment](/docs/en/third-party-integrations)

[Administration](/docs/en/setup)

[Configuration](/docs/en/settings)

[Reference](/docs/en/cli-reference)

[Resources](/docs/en/legal-and-compliance)

##### Getting started

- [](/docs/en/overview)
  Overview
- [](/docs/en/quickstart)
  Quickstart
- [](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
  Changelog

##### Core concepts

- [](/docs/en/how-claude-code-works)
  How Claude Code works
- [](/docs/en/features-overview)
  Extend Claude Code
- [](/docs/en/common-workflows)
  Common workflows
- [](/docs/en/best-practices)
  Best practices

##### Platforms and integrations

- [](/docs/en/claude-code-on-the-web)
  Claude Code on the web

- Claude Code on desktop

- [](/docs/en/chrome)
  Chrome extension (beta)

- [](/docs/en/vs-code)
  Visual Studio Code

- [](/docs/en/jetbrains)
  JetBrains IDEs

- [](/docs/en/github-actions)
  GitHub Actions

- [](/docs/en/gitlab-ci-cd)
  GitLab CI/CD

- [](/docs/en/slack)
  Claude Code in Slack

On this page

- [What is Claude Code on the web?](#what-is-claude-code-on-the-web)
- [Who can use Claude Code on the web?](#who-can-use-claude-code-on-the-web)
- [Getting started](#getting-started)
- [How it works](#how-it-works)
- [Review changes with diff view](#review-changes-with-diff-view)
- [Moving tasks between web and terminal](#moving-tasks-between-web-and-terminal)
- [From terminal to web](#from-terminal-to-web)
- [Tips for background tasks](#tips-for-background-tasks)
- [From web to terminal](#from-web-to-terminal)
- [Requirements for teleporting](#requirements-for-teleporting)
- [Sharing sessions](#sharing-sessions)
- [Sharing from an Enterprise or Teams account](#sharing-from-an-enterprise-or-teams-account)
- [Sharing from a Max or Pro account](#sharing-from-a-max-or-pro-account)
- [Cloud environment](#cloud-environment)
- [Default image](#default-image)
- [Checking available tools](#checking-available-tools)
- [Language-specific setups](#language-specific-setups)
- [Databases](#databases)
- [Environment configuration](#environment-configuration)
- [Dependency management](#dependency-management)
- [Persist environment variables](#persist-environment-variables)
- [Dependency management limitations](#dependency-management-limitations)
- [Network access and security](#network-access-and-security)
- [Network policy](#network-policy)
- [GitHub proxy](#github-proxy)
- [Security proxy](#security-proxy)
- [Access levels](#access-levels)
- [Default allowed domains](#default-allowed-domains)
- [Anthropic Services](#anthropic-services)
- [Version Control](#version-control)
- [Container Registries](#container-registries)
- [Cloud Platforms](#cloud-platforms)
- [Package Managers - JavaScript/Node](#package-managers-javascript%2Fnode)
- [Package Managers - Python](#package-managers-python)
- [Package Managers - Ruby](#package-managers-ruby)
- [Package Managers - Rust](#package-managers-rust)
- [Package Managers - Go](#package-managers-go)
- [Package Managers - JVM](#package-managers-jvm)
- [Package Managers - Other Languages](#package-managers-other-languages)
- [Linux Distributions](#linux-distributions)
- [Development Tools & Platforms](#development-tools-%26-platforms)
- [Cloud Services & Monitoring](#cloud-services-%26-monitoring)
- [Content Delivery & Mirrors](#content-delivery-%26-mirrors)
- [Schema & Configuration](#schema-%26-configuration)
- [Model Context Protocol](#model-context-protocol)
- [Security best practices for customized network access](#security-best-practices-for-customized-network-access)
- [Security and isolation](#security-and-isolation)
- [Pricing and rate limits](#pricing-and-rate-limits)
- [Limitations](#limitations)
- [Best practices](#best-practices)
- [Related resources](#related-resources)

Platforms and integrations

# Claude Code on the web

Copy page

Run Claude Code tasks asynchronously on secure cloud infrastructure

Copy page

Claude Code on the web is currently in research preview.

## 

[​](#what-is-claude-code-on-the-web)

What is Claude Code on the web?

Claude Code on the web lets developers kick off Claude Code from the Claude app. This is perfect for:

- **Answering questions**: Ask about code architecture and how features are implemented
- **Bug fixes and routine tasks**: Well-defined tasks that don’t require frequent steering
- **Parallel work**: Tackle multiple bug fixes in parallel
- **Repositories not on your local machine**: Work on code you don’t have checked out locally
- **Backend changes**: Where Claude Code can write tests and then write code to pass those tests

Claude Code is also available on the Claude iOS app for kicking off tasks on the go and monitoring work in progress. You can move between local and remote development: [send tasks from your terminal to run on the web](#from-terminal-to-web) with the `&` prefix, or [teleport web sessions back to your terminal](#from-web-to-terminal) to continue locally.

## 

[​](#who-can-use-claude-code-on-the-web)

Who can use Claude Code on the web?

Claude Code on the web is available in research preview to:

- **Pro users**
- **Max users**
- **Team users**
- **Enterprise users** with premium seats or Chat + Claude Code seats

## 

[​](#getting-started)

Getting started

1.  Visit [claude.ai/code](https://claude.ai/code)
2.  Connect your GitHub account
3.  Install the Claude GitHub app in your repositories
4.  Select your default environment
5.  Submit your coding task
6.  Review changes in diff view, iterate with comments, then create a pull request

## 

[​](#how-it-works)

How it works

When you start a task on Claude Code on the web:

1.  **Repository cloning**: Your repository is cloned to an Anthropic-managed virtual machine
2.  **Environment setup**: Claude prepares a secure cloud environment with your code
3.  **Network configuration**: Internet access is configured based on your settings
4.  **Task execution**: Claude analyzes code, makes changes, runs tests, and checks its work
5.  **Completion**: You’re notified when finished and can create a PR with the changes
6.  **Results**: Changes are pushed to a branch, ready for pull request creation

## 

[​](#review-changes-with-diff-view)

Review changes with diff view

Diff view lets you see exactly what Claude changed before creating a pull request. Instead of clicking “Create PR” to review changes in GitHub, view the diff directly in the app and iterate with Claude until the changes are ready. When Claude makes changes to files, a diff stats indicator appears showing the number of lines added and removed (for example, `+12 -1`). Select this indicator to open the diff viewer, which displays a file list on the left and the changes for each file on the right. From the diff view, you can:

- Review changes file by file
- Comment on specific changes to request modifications
- Continue iterating with Claude based on what you see

This lets you refine changes through multiple rounds of feedback without creating draft PRs or switching to GitHub.

## 

[​](#moving-tasks-between-web-and-terminal)

Moving tasks between web and terminal

You can start tasks on the web and continue them in your terminal, or send tasks from your terminal to run on the web. Web sessions persist even if you close your laptop, and you can monitor them from anywhere including the Claude iOS app.

Session handoff is one-way: you can pull web sessions into your terminal, but you can’t push an existing terminal session to the web. The [`&` prefix](#from-terminal-to-web) creates a *new* web session with your current conversation context.

### 

[​](#from-terminal-to-web)

From terminal to web

Start a message with `&` inside Claude Code to send a task to run on the web:

Report incorrect code

Copy

Ask AI

``` shiki
& Fix the authentication bug in src/auth/login.ts
```

This creates a new web session on claude.ai with your current conversation context. The task runs in the cloud while you continue working locally. Use `/tasks` to check progress, or open the session on claude.ai or the Claude iOS app to interact directly. From there you can steer Claude, provide feedback, or answer questions just like any other conversation. You can also start a web session directly from the command line:

Report incorrect code

Copy

Ask AI

``` shiki
claude --remote "Fix the authentication bug in src/auth/login.ts"
```

#### 

[​](#tips-for-background-tasks)

Tips for background tasks

**Plan locally, execute remotely**: For complex tasks, start Claude in plan mode to collaborate on the approach before sending work to the web:

Report incorrect code

Copy

Ask AI

``` shiki
claude --permission-mode plan
```

In plan mode, Claude can only read files and explore the codebase. Once you’re satisfied with the plan, send it to the web for autonomous execution:

Report incorrect code

Copy

Ask AI

``` shiki
& Execute the migration plan we discussed
```

This pattern gives you control over the strategy while letting Claude execute autonomously in the cloud. **Run tasks in parallel**: Each `&` command creates its own web session that runs independently. You can kick off multiple tasks and they’ll all run simultaneously in separate sessions:

Report incorrect code

Copy

Ask AI

``` shiki
& Fix the flaky test in auth.spec.ts
& Update the API documentation
& Refactor the logger to use structured output
```

Monitor all sessions with `/tasks`. When a session completes, you can create a PR from the web interface or [teleport](#from-web-to-terminal) the session to your terminal to continue working.

### 

[​](#from-web-to-terminal)

From web to terminal

There are several ways to pull a web session into your terminal:

- **Using `/teleport`**: From within Claude Code, run `/teleport` (or `/tp`) to see an interactive picker of your web sessions. If you have uncommitted changes, you’ll be prompted to stash them first.
- **Using `--teleport`**: From the command line, run `claude --teleport` for an interactive session picker, or `claude --teleport <session-id>` to resume a specific session directly.
- **From `/tasks`**: Run `/tasks` to see your background sessions, then press `t` to teleport into one
- **From the web interface**: Click “Open in CLI” to copy a command you can paste into your terminal

When you teleport a session, Claude verifies you’re in the correct repository, fetches and checks out the branch from the remote session, and loads the full conversation history into your terminal.

#### 

[​](#requirements-for-teleporting)

Requirements for teleporting

Teleport checks these requirements before resuming a session. If any requirement isn’t met, you’ll see an error or be prompted to resolve the issue.

| Requirement | Details |
|----|----|
| Clean git state | Your working directory must have no uncommitted changes. Teleport prompts you to stash changes if needed. |
| Correct repository | You must run `--teleport` from a checkout of the same repository, not a fork. |
| Branch available | The branch from the web session must have been pushed to the remote. Teleport automatically fetches and checks it out. |
| Same account | You must be authenticated to the same Claude.ai account used in the web session. |

### 

[​](#sharing-sessions)

Sharing sessions

To share a session, toggle its visibility according to the account types below. After that, share the session link as-is. Recipients who open your shared session will see the latest state of the session upon load, but the recipient’s page will not update in real time.

#### 

[​](#sharing-from-an-enterprise-or-teams-account)

Sharing from an Enterprise or Teams account

For Enterprise and Teams accounts, the two visibility options are **Private** and **Team**. Team visibility makes the session visible to other members of your Claude.ai organization. Repository access verification is enabled by default, based on the GitHub account connected to the recipient’s account. Your account’s display name is visible to all recipients with access. [Claude in Slack](/docs/en/slack) sessions are automatically shared with Team visibility.

#### 

[​](#sharing-from-a-max-or-pro-account)

Sharing from a Max or Pro account

For Max and Pro accounts, the two visibility options are **Private** and **Public**. Public visibility makes the session visible to any user logged into claude.ai. Check your session for sensitive content before sharing. Sessions may contain code and credentials from private GitHub repositories. Repository access verification is not enabled by default. Enable repository access verification and/or withhold your name from your shared sessions by going to Settings \> Claude Code \> Sharing settings.

## 

[​](#cloud-environment)

Cloud environment

### 

[​](#default-image)

Default image

We build and maintain a universal image with common toolchains and language ecosystems pre-installed. This image includes:

- Popular programming languages and runtimes
- Common build tools and package managers
- Testing frameworks and linters

#### 

[​](#checking-available-tools)

Checking available tools

To see what’s pre-installed in your environment, ask Claude Code to run:

Report incorrect code

Copy

Ask AI

``` shiki
check-tools
```

This command displays:

- Programming languages and their versions
- Available package managers
- Installed development tools

#### 

[​](#language-specific-setups)

Language-specific setups

The universal image includes pre-configured environments for:

- **Python**: Python 3.x with pip, poetry, and common scientific libraries
- **Node.js**: Latest LTS versions with npm, yarn, pnpm, and bun
- **Ruby**: Versions 3.1.6, 3.2.6, 3.3.6 (default: 3.3.6) with gem, bundler, and rbenv for version management
- **PHP**: Version 8.4.14
- **Java**: OpenJDK with Maven and Gradle
- **Go**: Latest stable version with module support
- **Rust**: Rust toolchain with cargo
- **C++**: GCC and Clang compilers

#### 

[​](#databases)

Databases

The universal image includes the following databases:

- **PostgreSQL**: Version 16
- **Redis**: Version 7.0

### 

[​](#environment-configuration)

Environment configuration

When you start a session in Claude Code on the web, here’s what happens under the hood:

1.  **Environment preparation**: We clone your repository and run any configured Claude hooks for initialization. The repo will be cloned with the default branch on your GitHub repo. If you would like to check out a specific branch, you can specify that in the prompt.
2.  **Network configuration**: We configure internet access for the agent. Internet access is limited by default, but you can configure the environment to have no internet or full internet access based on your needs.
3.  **Claude Code execution**: Claude Code runs to complete your task, writing code, running tests, and checking its work. You can guide and steer Claude throughout the session via the web interface. Claude respects context you’ve defined in your `CLAUDE.md`.
4.  **Outcome**: When Claude completes its work, it will push the branch to remote. You will be able to create a PR for the branch.

Claude operates entirely through the terminal and CLI tools available in the environment. It uses the pre-installed tools in the universal image and any additional tools you install through hooks or dependency management.

**To add a new environment:** Select the current environment to open the environment selector, and then select “Add environment”. This will open a dialog where you can specify the environment name, network access level, and any environment variables you want to set. **To update an existing environment:** Select the current environment, to the right of the environment name, and select the settings button. This will open a dialog where you can update the environment name, network access, and environment variables. **To select your default environment from the terminal:** If you have multiple environments configured, run `/remote-env` to choose which one to use when starting web sessions from your terminal with `&` or `--remote`. With a single environment, this command shows your current configuration.

Environment variables must be specified as key-value pairs, in [`.env` format](https://www.dotenv.org/). For example:

Report incorrect code

Copy

Ask AI

``` shiki
API_KEY=your_api_key
DEBUG=true
```

### 

[​](#dependency-management)

Dependency management

Custom environment images and snapshots are not yet supported. As a workaround, you can use [SessionStart hooks](/docs/en/hooks#sessionstart) to install packages when a session starts. This approach has [known limitations](#dependency-management-limitations). To configure automatic dependency installation, add a SessionStart hook to your repository’s `.claude/settings.json` file:

Report incorrect code

Copy

Ask AI

``` shiki
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/scripts/install_pkgs.sh"
          }
        ]
      }
    ]
  }
}
```

Create the corresponding script at `scripts/install_pkgs.sh`:

Report incorrect code

Copy

Ask AI

``` shiki
#!/bin/bash

# Only run in remote environments
if [ "$CLAUDE_CODE_REMOTE" != "true" ]; then
  exit 0
fi

npm install
pip install -r requirements.txt
exit 0
```

Make it executable: `chmod +x scripts/install_pkgs.sh`

#### 

[​](#persist-environment-variables)

Persist environment variables

SessionStart hooks can persist environment variables for subsequent Bash commands by writing to the file specified in the `CLAUDE_ENV_FILE` environment variable. For details, see [SessionStart hooks](/docs/en/hooks#sessionstart) in the hooks reference.

#### 

[​](#dependency-management-limitations)

Dependency management limitations

- **Hooks fire for all sessions**: SessionStart hooks run in both local and remote environments. There is no hook configuration to scope a hook to remote sessions only. To skip local execution, check the `CLAUDE_CODE_REMOTE` environment variable in your script as shown above.
- **Requires network access**: Install commands need network access to reach package registries. If your environment is configured with “No internet” access, these hooks will fail. Use “Limited” (the default) or “Full” network access. The [default allowlist](#default-allowed-domains) includes common registries like npm, PyPI, RubyGems, and crates.io.
- **Proxy compatibility**: All outbound traffic in remote environments passes through a [security proxy](#security-proxy). Some package managers do not work correctly with this proxy. Bun is a known example.
- **Runs on every session start**: Hooks run each time a session starts or resumes, adding startup latency. Keep install scripts fast by checking whether dependencies are already present before reinstalling.

## 

[​](#network-access-and-security)

Network access and security

### 

[​](#network-policy)

Network policy

#### 

[​](#github-proxy)

GitHub proxy

For security, all GitHub operations go through a dedicated proxy service that transparently handles all git interactions. Inside the sandbox, the git client authenticates using a custom-built scoped credential. This proxy:

- Manages GitHub authentication securely - the git client uses a scoped credential inside the sandbox, which the proxy verifies and translates to your actual GitHub authentication token
- Restricts git push operations to the current working branch for safety
- Enables seamless cloning, fetching, and PR operations while maintaining security boundaries

#### 

[​](#security-proxy)

Security proxy

Environments run behind an HTTP/HTTPS network proxy for security and abuse prevention purposes. All outbound internet traffic passes through this proxy, which provides:

- Protection against malicious requests
- Rate limiting and abuse prevention
- Content filtering for enhanced security

### 

[​](#access-levels)

Access levels

By default, network access is limited to [allowlisted domains](#default-allowed-domains). You can configure custom network access, including disabling network access.

### 

[​](#default-allowed-domains)

Default allowed domains

When using “Limited” network access, the following domains are allowed by default:

#### 

[​](#anthropic-services)

Anthropic Services

- api.anthropic.com
- statsig.anthropic.com
- platform.claude.com
- code.claude.com
- claude.ai

#### 

[​](#version-control)

Version Control

- github.com
- [www.github.com](http://www.github.com)
- api.github.com
- npm.pkg.github.com
- raw.githubusercontent.com
- pkg-npm.githubusercontent.com
- objects.githubusercontent.com
- codeload.github.com
- avatars.githubusercontent.com
- camo.githubusercontent.com
- gist.github.com
- gitlab.com
- [www.gitlab.com](http://www.gitlab.com)
- registry.gitlab.com
- bitbucket.org
- [www.bitbucket.org](http://www.bitbucket.org)
- api.bitbucket.org

#### 

[​](#container-registries)

Container Registries

- registry-1.docker.io
- auth.docker.io
- index.docker.io
- hub.docker.com
- [www.docker.com](http://www.docker.com)
- production.cloudflare.docker.com
- download.docker.com
- gcr.io
- \*.gcr.io
- ghcr.io
- mcr.microsoft.com
- \*.data.mcr.microsoft.com
- public.ecr.aws

#### 

[​](#cloud-platforms)

Cloud Platforms

- cloud.google.com
- accounts.google.com
- gcloud.google.com
- \*.googleapis.com
- storage.googleapis.com
- compute.googleapis.com
- container.googleapis.com
- azure.com
- portal.azure.com
- microsoft.com
- [www.microsoft.com](http://www.microsoft.com)
- \*.microsoftonline.com
- packages.microsoft.com
- dotnet.microsoft.com
- dot.net
- visualstudio.com
- dev.azure.com
- \*.amazonaws.com
- \*.api.aws
- oracle.com
- [www.oracle.com](http://www.oracle.com)
- java.com
- [www.java.com](http://www.java.com)
- java.net
- [www.java.net](http://www.java.net)
- download.oracle.com
- yum.oracle.com

#### 

[​](#package-managers-javascript/node)

Package Managers - JavaScript/Node

- registry.npmjs.org
- [www.npmjs.com](http://www.npmjs.com)
- [www.npmjs.org](http://www.npmjs.org)
- npmjs.com
- npmjs.org
- yarnpkg.com
- registry.yarnpkg.com

#### 

[​](#package-managers-python)

Package Managers - Python

- pypi.org
- [www.pypi.org](http://www.pypi.org)
- files.pythonhosted.org
- pythonhosted.org
- test.pypi.org
- pypi.python.org
- pypa.io
- [www.pypa.io](http://www.pypa.io)

#### 

[​](#package-managers-ruby)

Package Managers - Ruby

- rubygems.org
- [www.rubygems.org](http://www.rubygems.org)
- api.rubygems.org
- index.rubygems.org
- ruby-lang.org
- [www.ruby-lang.org](http://www.ruby-lang.org)
- rubyforge.org
- [www.rubyforge.org](http://www.rubyforge.org)
- rubyonrails.org
- [www.rubyonrails.org](http://www.rubyonrails.org)
- rvm.io
- get.rvm.io

#### 

[​](#package-managers-rust)

Package Managers - Rust

- crates.io
- [www.crates.io](http://www.crates.io)
- index.crates.io
- static.crates.io
- rustup.rs
- static.rust-lang.org
- [www.rust-lang.org](http://www.rust-lang.org)

#### 

[​](#package-managers-go)

Package Managers - Go

- proxy.golang.org
- sum.golang.org
- index.golang.org
- golang.org
- [www.golang.org](http://www.golang.org)
- goproxy.io
- pkg.go.dev

#### 

[​](#package-managers-jvm)

Package Managers - JVM

- maven.org
- repo.maven.org
- central.maven.org
- repo1.maven.org
- jcenter.bintray.com
- gradle.org
- [www.gradle.org](http://www.gradle.org)
- services.gradle.org
- plugins.gradle.org
- kotlin.org
- [www.kotlin.org](http://www.kotlin.org)
- spring.io
- repo.spring.io

#### 

[​](#package-managers-other-languages)

Package Managers - Other Languages

- packagist.org (PHP Composer)
- [www.packagist.org](http://www.packagist.org)
- repo.packagist.org
- nuget.org (.NET NuGet)
- [www.nuget.org](http://www.nuget.org)
- api.nuget.org
- pub.dev (Dart/Flutter)
- api.pub.dev
- hex.pm (Elixir/Erlang)
- [www.hex.pm](http://www.hex.pm)
- cpan.org (Perl CPAN)
- [www.cpan.org](http://www.cpan.org)
- metacpan.org
- [www.metacpan.org](http://www.metacpan.org)
- api.metacpan.org
- cocoapods.org (iOS/macOS)
- [www.cocoapods.org](http://www.cocoapods.org)
- cdn.cocoapods.org
- haskell.org
- [www.haskell.org](http://www.haskell.org)
- hackage.haskell.org
- swift.org
- [www.swift.org](http://www.swift.org)

#### 

[​](#linux-distributions)

Linux Distributions

- archive.ubuntu.com
- security.ubuntu.com
- ubuntu.com
- [www.ubuntu.com](http://www.ubuntu.com)
- \*.ubuntu.com
- ppa.launchpad.net
- launchpad.net
- [www.launchpad.net](http://www.launchpad.net)

#### 

[​](#development-tools-&-platforms)

Development Tools & Platforms

- dl.k8s.io (Kubernetes)
- pkgs.k8s.io
- k8s.io
- [www.k8s.io](http://www.k8s.io)
- releases.hashicorp.com (HashiCorp)
- apt.releases.hashicorp.com
- rpm.releases.hashicorp.com
- archive.releases.hashicorp.com
- hashicorp.com
- [www.hashicorp.com](http://www.hashicorp.com)
- repo.anaconda.com (Anaconda/Conda)
- conda.anaconda.org
- anaconda.org
- [www.anaconda.com](http://www.anaconda.com)
- anaconda.com
- continuum.io
- apache.org (Apache)
- [www.apache.org](http://www.apache.org)
- archive.apache.org
- downloads.apache.org
- eclipse.org (Eclipse)
- [www.eclipse.org](http://www.eclipse.org)
- download.eclipse.org
- nodejs.org (Node.js)
- [www.nodejs.org](http://www.nodejs.org)

#### 

[​](#cloud-services-&-monitoring)

Cloud Services & Monitoring

- statsig.com
- [www.statsig.com](http://www.statsig.com)
- api.statsig.com
- sentry.io
- \*.sentry.io
- http-intake.logs.datadoghq.com
- \*.datadoghq.com
- \*.datadoghq.eu

#### 

[​](#content-delivery-&-mirrors)

Content Delivery & Mirrors

- sourceforge.net
- \*.sourceforge.net
- packagecloud.io
- \*.packagecloud.io

#### 

[​](#schema-&-configuration)

Schema & Configuration

- json-schema.org
- [www.json-schema.org](http://www.json-schema.org)
- json.schemastore.org
- [www.schemastore.org](http://www.schemastore.org)

#### 

[​](#model-context-protocol)

Model Context Protocol

- \*.modelcontextprotocol.io

Domains marked with `*` indicate wildcard subdomain matching. For example, `*.gcr.io` allows access to any subdomain of `gcr.io`.

### 

[​](#security-best-practices-for-customized-network-access)

Security best practices for customized network access

1.  **Principle of least privilege**: Only enable the minimum network access required
2.  **Audit regularly**: Review allowed domains periodically
3.  **Use HTTPS**: Always prefer HTTPS endpoints over HTTP

## 

[​](#security-and-isolation)

Security and isolation

Claude Code on the web provides strong security guarantees:

- **Isolated virtual machines**: Each session runs in an isolated, Anthropic-managed VM
- **Network access controls**: Network access is limited by default, and can be disabled

When running with network access disabled, Claude Code is allowed to communicate with the Anthropic API which may still allow data to exit the isolated Claude Code VM.

- **Credential protection**: Sensitive credentials (such as git credentials or signing keys) are never inside the sandbox with Claude Code. Authentication is handled through a secure proxy using scoped credentials
- **Secure analysis**: Code is analyzed and modified within isolated VMs before creating PRs

## 

[​](#pricing-and-rate-limits)

Pricing and rate limits

Claude Code on the web shares rate limits with all other Claude and Claude Code usage within your account. Running multiple tasks in parallel will consume more rate limits proportionately.

## 

[​](#limitations)

Limitations

- **Repository authentication**: You can only move sessions from web to local when you are authenticated to the same account
- **Platform restrictions**: Claude Code on the web only works with code hosted in GitHub. GitLab and other non-GitHub repositories cannot be used with cloud sessions

## 

[​](#best-practices)

Best practices

1.  **Use Claude Code hooks**: Configure [SessionStart hooks](/docs/en/hooks#sessionstart) to automate environment setup and dependency installation.
2.  **Document requirements**: Clearly specify dependencies and commands in your `CLAUDE.md` file. If you have an `AGENTS.md` file, you can source it in your `CLAUDE.md` using `@AGENTS.md` to maintain a single source of truth.

## 

[​](#related-resources)

Related resources

- [Hooks configuration](/docs/en/hooks)
- [Settings reference](/docs/en/settings)
- [Security](/docs/en/security)
- [Data usage](/docs/en/data-usage)

Was this page helpful?

Yes

No

[Best practices](/docs/en/best-practices)[Get started](/docs/en/desktop-quickstart)

[Claude Code Docs home page](/docs)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

Company

[Anthropic](https://www.anthropic.com/company)[Careers](https://www.anthropic.com/careers)[Economic Futures](https://www.anthropic.com/economic-futures)[Research](https://www.anthropic.com/research)[News](https://www.anthropic.com/news)[Trust center](https://trust.anthropic.com/)[Transparency](https://www.anthropic.com/transparency)

Help and security

[Availability](https://www.anthropic.com/supported-countries)[Status](https://status.anthropic.com/)[Support center](https://support.claude.com/)

Learn

[Courses](https://www.anthropic.com/learn)[MCP connectors](https://claude.com/partners/mcp)[Customer stories](https://www.claude.com/customers)[Engineering blog](https://www.anthropic.com/engineering)[Events](https://www.anthropic.com/events)[Powered by Claude](https://claude.com/partners/powered-by-claude)[Service partners](https://claude.com/partners/services)[Startups program](https://claude.com/programs/startups)

Terms and policies

[Privacy policy](https://www.anthropic.com/legal/privacy)[Disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)[Usage policy](https://www.anthropic.com/legal/aup)[Commercial terms](https://www.anthropic.com/legal/commercial-terms)[Consumer terms](https://www.anthropic.com/legal/consumer-terms)

Assistant

Responses are generated using AI and may contain mistakes.
