---
category: "02-Claude-Code-CLI"
fetched_at: "2026-03-14T10:17:00Z"
source_url: "https://code.claude.com/docs/en/settings"
title: "Claude Code settings - Claude Code Docs"
---

# Claude Code settings


Configure Claude Code with global and project-level settings, and environment variables.


Claude Code offers a variety of settings to configure its behavior to meet your needs. You can configure Claude Code by running the `/config` command when using the interactive REPL, which opens a tabbed Settings interface where you can view status information and modify configuration options.

## 

[​](#configuration-scopes)

Configuration scopes

Claude Code uses a **scope system** to determine where configurations apply and who they’re shared with. Understanding scopes helps you decide how to configure Claude Code for personal use, team collaboration, or enterprise deployment.

### 

[​](#available-scopes)

Available scopes

| Scope | Location | Who it affects | Shared with team? |
|:---|:---|:---|:---|
| **Managed** | Server-managed settings, plist / registry, or system-level `managed-settings.json` | All users on the machine | Yes (deployed by IT) |
| **User** | `~/.claude/` directory | You, across all projects | No |
| **Project** | `.claude/` in repository | All collaborators on this repository | Yes (committed to git) |
| **Local** | `.claude/settings.local.json` | You, in this repository only | No (gitignored) |

### 

[​](#when-to-use-each-scope)

When to use each scope

**Managed scope** is for:

- Security policies that must be enforced organization-wide
- Compliance requirements that can’t be overridden
- Standardized configurations deployed by IT/DevOps

**User scope** is best for:

- Personal preferences you want everywhere (themes, editor settings)
- Tools and plugins you use across all projects
- API keys and authentication (stored securely)

**Project scope** is best for:

- Team-shared settings (permissions, hooks, MCP servers)
- Plugins the whole team should have
- Standardizing tooling across collaborators

**Local scope** is best for:

- Personal overrides for a specific project
- Testing configurations before sharing with the team
- Machine-specific settings that won’t work for others

### 

[​](#how-scopes-interact)

How scopes interact

When the same setting is configured in multiple scopes, more specific scopes take precedence:

1.  **Managed** (highest) - can’t be overridden by anything
2.  **Command line arguments** - temporary session overrides
3.  **Local** - overrides project and user settings
4.  **Project** - overrides user settings
5.  **User** (lowest) - applies when nothing else specifies the setting

For example, if a permission is allowed in user settings but denied in project settings, the project setting takes precedence and the permission is blocked.

### 

[​](#what-uses-scopes)

What uses scopes

Scopes apply to many Claude Code features:

| Feature | User location | Project location | Local location |
|:---|:---|:---|:---|
| **Settings** | `~/.claude/settings.json` | `.claude/settings.json` | `.claude/settings.local.json` |
| **Subagents** | `~/.claude/agents/` | `.claude/agents/` | None |
| **MCP servers** | `~/.claude.json` | `.mcp.json` | `~/.claude.json` (per-project) |
| **Plugins** | `~/.claude/settings.json` | `.claude/settings.json` | `.claude/settings.local.json` |
| **CLAUDE.md** | `~/.claude/CLAUDE.md` | `CLAUDE.md` or `.claude/CLAUDE.md` | None |

------------------------------------------------------------------------

## 

[​](#settings-files)

Settings files

The `settings.json` file is the official mechanism for configuring Claude Code through hierarchical settings:

- **User settings** are defined in `~/.claude/settings.json` and apply to all projects.
- **Project settings** are saved in your project directory:
  - `.claude/settings.json` for settings that are checked into source control and shared with your team
  - `.claude/settings.local.json` for settings that are not checked in, useful for personal preferences and experimentation. Claude Code will configure git to ignore `.claude/settings.local.json` when it is created.
- **Managed settings**: For organizations that need centralized control, Claude Code supports multiple delivery mechanisms for managed settings. All use the same JSON format and cannot be overridden by user or project settings:
  - **Server-managed settings**: delivered from Anthropic’s servers via the Claude.ai admin console. See [server-managed settings](/docs/en/server-managed-settings).
  - **MDM/OS-level policies**: delivered through native device management on macOS and Windows:
    - macOS: `com.anthropic.claudecode` managed preferences domain (deployed via configuration profiles in Jamf, Kandji, or other MDM tools)
    - Windows: `HKLM\SOFTWARE\Policies\ClaudeCode` registry key with a `Settings` value (REG_SZ or REG_EXPAND_SZ) containing JSON (deployed via Group Policy or Intune)
    - Windows (user-level): `HKCU\SOFTWARE\Policies\ClaudeCode` (lowest policy priority, only used when no admin-level source exists)
  - **File-based**: `managed-settings.json` and `managed-mcp.json` deployed to system directories:
    - macOS: `/Library/Application Support/ClaudeCode/`
    - Linux and WSL: `/etc/claude-code/`
    - Windows: `C:\Program Files\ClaudeCode\`

    The legacy Windows path `C:\ProgramData\ClaudeCode\managed-settings.json` is no longer supported as of v2.1.75. Administrators who deployed settings to that location must migrate files to `C:\Program Files\ClaudeCode\managed-settings.json`.

  See [managed settings](/docs/en/permissions#managed-only-settings) and [Managed MCP configuration](/docs/en/mcp#managed-mcp-configuration) for details.

  Managed deployments can also restrict **plugin marketplace additions** using `strictKnownMarketplaces`. For more information, see [Managed marketplace restrictions](/docs/en/plugin-marketplaces#managed-marketplace-restrictions).
- **Other configuration** is stored in `~/.claude.json`. This file contains your preferences (theme, notification settings, editor mode), OAuth session, [MCP server](/docs/en/mcp) configurations for user and local scopes, per-project state (allowed tools, trust settings), and various caches. Project-scoped MCP servers are stored separately in `.mcp.json`.

Claude Code automatically creates timestamped backups of configuration files and retains the five most recent backups to prevent data loss.

Example settings.json

Report incorrect code

Copy


``` shiki
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test *)",
      "Read(~/.zshrc)"
    ],
    "deny": [
      "Bash(curl *)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  },
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp"
  },
  "companyAnnouncements": [
    "Welcome to Acme Corp! Review our code guidelines at docs.acme.com",
    "Reminder: Code reviews required for all PRs",
    "New security policy in effect"
  ]
}
```

The `$schema` line in the example above points to the [official JSON schema](https://json.schemastore.org/claude-code-settings.json) for Claude Code settings. Adding it to your `settings.json` enables autocomplete and inline validation in VS Code, Cursor, and any other editor that supports JSON schema validation.

### 

[​](#available-settings)

Available settings

`settings.json` supports a number of options:

[TABLE]

### 

[​](#worktree-settings)

Worktree settings

Configure how `--worktree` creates and manages git worktrees. Use these settings to reduce disk usage and startup time in large monorepos.

| Key | Description | Example |
|:---|:---|:---|
| `worktree.symlinkDirectories` | Directories to symlink from the main repository into each worktree to avoid duplicating large directories on disk. No directories are symlinked by default | `["node_modules", ".cache"]` |
| `worktree.sparsePaths` | Directories to check out in each worktree via git sparse-checkout (cone mode). Only the listed paths are written to disk, which is faster in large monorepos | `["packages/my-app", "shared/utils"]` |

### 

[​](#permission-settings)

Permission settings

| Keys | Description | Example |
|:---|:---|:---|
| `allow` | Array of permission rules to allow tool use. See [Permission rule syntax](#permission-rule-syntax) below for pattern matching details | `[ "Bash(git diff *)" ]` |
| `ask` | Array of permission rules to ask for confirmation upon tool use. See [Permission rule syntax](#permission-rule-syntax) below | `[ "Bash(git push *)" ]` |
| `deny` | Array of permission rules to deny tool use. Use this to exclude sensitive files from Claude Code access. See [Permission rule syntax](#permission-rule-syntax) and [Bash permission limitations](/docs/en/permissions#tool-specific-permission-rules) | `[ "WebFetch", "Bash(curl *)", "Read(./.env)", "Read(./secrets/**)" ]` |
| `additionalDirectories` | Additional [working directories](/docs/en/permissions#working-directories) that Claude has access to | `[ "../docs/" ]` |
| `defaultMode` | Default [permission mode](/docs/en/permissions#permission-modes) when opening Claude Code | `"acceptEdits"` |
| `disableBypassPermissionsMode` | Set to `"disable"` to prevent `bypassPermissions` mode from being activated. This disables the `--dangerously-skip-permissions` command-line flag. See [managed settings](/docs/en/permissions#managed-only-settings) | `"disable"` |

### 

[​](#permission-rule-syntax)

Permission rule syntax

Permission rules follow the format `Tool` or `Tool(specifier)`. Rules are evaluated in order: deny rules first, then ask, then allow. The first matching rule wins. Quick examples:

| Rule                           | Effect                                   |
|:-------------------------------|:-----------------------------------------|
| `Bash`                         | Matches all Bash commands                |
| `Bash(npm run *)`              | Matches commands starting with `npm run` |
| `Read(./.env)`                 | Matches reading the `.env` file          |
| `WebFetch(domain:example.com)` | Matches fetch requests to example.com    |

For the complete rule syntax reference, including wildcard behavior, tool-specific patterns for Read, Edit, WebFetch, MCP, and Agent rules, and security limitations of Bash patterns, see [Permission rule syntax](/docs/en/permissions#permission-rule-syntax).

### 

[​](#sandbox-settings)

Sandbox settings

Configure advanced sandboxing behavior. Sandboxing isolates bash commands from your filesystem and network. See [Sandboxing](/docs/en/sandboxing) for details.

| Keys | Description | Example |
|:---|:---|:---|
| `enabled` | Enable bash sandboxing (macOS, Linux, and WSL2). Default: false | `true` |
| `autoAllowBashIfSandboxed` | Auto-approve bash commands when sandboxed. Default: true | `true` |
| `excludedCommands` | Commands that should run outside of the sandbox | `["git", "docker"]` |
| `allowUnsandboxedCommands` | Allow commands to run outside the sandbox via the `dangerouslyDisableSandbox` parameter. When set to `false`, the `dangerouslyDisableSandbox` escape hatch is completely disabled and all commands must run sandboxed (or be in `excludedCommands`). Useful for enterprise policies that require strict sandboxing. Default: true | `false` |
| `filesystem.allowWrite` | Additional paths where sandboxed commands can write. Arrays are merged across all settings scopes: user, project, and managed paths are combined, not replaced. Also merged with paths from `Edit(...)` allow permission rules. See [path prefixes](#sandbox-path-prefixes) below. | `["//tmp/build", "~/.kube"]` |
| `filesystem.denyWrite` | Paths where sandboxed commands cannot write. Arrays are merged across all settings scopes. Also merged with paths from `Edit(...)` deny permission rules. | `["//etc", "//usr/local/bin"]` |
| `filesystem.denyRead` | Paths where sandboxed commands cannot read. Arrays are merged across all settings scopes. Also merged with paths from `Read(...)` deny permission rules. | `["~/.aws/credentials"]` |
| `network.allowUnixSockets` | Unix socket paths accessible in sandbox (for SSH agents, etc.) | `["~/.ssh/agent-socket"]` |
| `network.allowAllUnixSockets` | Allow all Unix socket connections in sandbox. Default: false | `true` |
| `network.allowLocalBinding` | Allow binding to localhost ports (macOS only). Default: false | `true` |
| `network.allowedDomains` | Array of domains to allow for outbound network traffic. Supports wildcards (e.g., `*.example.com`). | `["github.com", "*.npmjs.org"]` |
| `network.allowManagedDomainsOnly` | (Managed settings only) Only `allowedDomains` and `WebFetch(domain:...)` allow rules from managed settings are respected. Domains from user, project, and local settings are ignored. Non-allowed domains are blocked automatically without prompting the user. Denied domains are still respected from all sources. Default: false | `true` |
| `network.httpProxyPort` | HTTP proxy port used if you wish to bring your own proxy. If not specified, Claude will run its own proxy. | `8080` |
| `network.socksProxyPort` | SOCKS5 proxy port used if you wish to bring your own proxy. If not specified, Claude will run its own proxy. | `8081` |
| `enableWeakerNestedSandbox` | Enable weaker sandbox for unprivileged Docker environments (Linux and WSL2 only). **Reduces security.** Default: false | `true` |
| `enableWeakerNetworkIsolation` | (macOS only) Allow access to the system TLS trust service (`com.apple.trustd.agent`) in the sandbox. Required for Go-based tools like `gh`, `gcloud`, and `terraform` to verify TLS certificates when using `httpProxyPort` with a MITM proxy and custom CA. **Reduces security** by opening a potential data exfiltration path. Default: false | `true` |

#### 

[​](#sandbox-path-prefixes)

Sandbox path prefixes

Paths in `filesystem.allowWrite`, `filesystem.denyWrite`, and `filesystem.denyRead` support these prefixes:

| Prefix | Meaning | Example |
|:---|:---|:---|
| `//` | Absolute path from filesystem root | `//tmp/build` becomes `/tmp/build` |
| `~/` | Relative to home directory | `~/.kube` becomes `$HOME/.kube` |
| `/` | Relative to the settings file’s directory | `/build` becomes `$SETTINGS_DIR/build` |
| `./` or no prefix | Relative path (resolved by sandbox runtime) | `./output` |

**Configuration example:**

Report incorrect code

Copy


``` shiki
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "excludedCommands": ["docker"],
    "filesystem": {
      "allowWrite": ["//tmp/build", "~/.kube"],
      "denyRead": ["~/.aws/credentials"]
    },
    "network": {
      "allowedDomains": ["github.com", "*.npmjs.org", "registry.yarnpkg.com"],
      "allowUnixSockets": [
        "/var/run/docker.sock"
      ],
      "allowLocalBinding": true
    }
  }
}
```

**Filesystem and network restrictions** can be configured in two ways that are merged together:

- **`sandbox.filesystem` settings** (shown above): Control paths at the OS-level sandbox boundary. These restrictions apply to all subprocess commands (e.g., `kubectl`, `terraform`, `npm`), not just Claude’s file tools.
- **Permission rules**: Use `Edit` allow/deny rules to control Claude’s file tool access, `Read` deny rules to block reads, and `WebFetch` allow/deny rules to control network domains. Paths from these rules are also merged into the sandbox configuration.

### 

[​](#attribution-settings)

Attribution settings

Claude Code adds attribution to git commits and pull requests. These are configured separately:

- Commits use [git trailers](https://git-scm.com/docs/git-interpret-trailers) (like `Co-Authored-By`) by default, which can be customized or disabled
- Pull request descriptions are plain text

| Keys | Description |
|:---|:---|
| `commit` | Attribution for git commits, including any trailers. Empty string hides commit attribution |
| `pr` | Attribution for pull request descriptions. Empty string hides pull request attribution |

**Default commit attribution:**

Report incorrect code

Copy


``` shiki
🤖 Generated with [Claude Code](https://claude.com/claude-code)

   Co-Authored-By: Claude Sonnet 4.6 <[email protected]>
```

**Default pull request attribution:**

Report incorrect code

Copy


``` shiki
🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

**Example:**

Report incorrect code

Copy


``` shiki
{
  "attribution": {
    "commit": "Generated with AI\n\nCo-Authored-By: AI <[email protected]>",
    "pr": ""
  }
}
```

The `attribution` setting takes precedence over the deprecated `includeCoAuthoredBy` setting. To hide all attribution, set `commit` and `pr` to empty strings.

### 

[​](#file-suggestion-settings)

File suggestion settings

Configure a custom command for `@` file path autocomplete. The built-in file suggestion uses fast filesystem traversal, but large monorepos may benefit from project-specific indexing such as a pre-built file index or custom tooling.

Report incorrect code

Copy


``` shiki
{
  "fileSuggestion": {
    "type": "command",
    "command": "~/.claude/file-suggestion.sh"
  }
}
```

The command runs with the same environment variables as [hooks](/docs/en/hooks), including `CLAUDE_PROJECT_DIR`. It receives JSON via stdin with a `query` field:

Report incorrect code

Copy


``` shiki
{"query": "src/comp"}
```

Output newline-separated file paths to stdout (currently limited to 15):

Report incorrect code

Copy


``` shiki
src/components/Button.tsx
src/components/Modal.tsx
src/components/Form.tsx
```

**Example:**

Report incorrect code

Copy


``` shiki
#!/bin/bash
query=$(cat | jq -r '.query')
your-repo-file-index --query "$query" | head -20
```

### 

[​](#hook-configuration)

Hook configuration

These settings control which hooks are allowed to run and what HTTP hooks can access. The `allowManagedHooksOnly` setting can only be configured in [managed settings](#settings-files). The URL and env var allowlists can be set at any settings level and merge across sources. **Behavior when `allowManagedHooksOnly` is `true`:**

- Managed hooks and SDK hooks are loaded
- User hooks, project hooks, and plugin hooks are blocked

**Restrict HTTP hook URLs:** Limit which URLs HTTP hooks can target. Supports `*` as a wildcard for matching. When the array is defined, HTTP hooks targeting non-matching URLs are silently blocked.

Report incorrect code

Copy


``` shiki
{
  "allowedHttpHookUrls": ["https://hooks.example.com/*", "http://localhost:*"]
}
```

**Restrict HTTP hook environment variables:** Limit which environment variable names HTTP hooks can interpolate into header values. Each hook’s effective `allowedEnvVars` is the intersection of its own list and this setting.

Report incorrect code

Copy


``` shiki
{
  "httpHookAllowedEnvVars": ["MY_TOKEN", "HOOK_SECRET"]
}
```

### 

[​](#settings-precedence)

Settings precedence

Settings apply in order of precedence. From highest to lowest:

1.  **Managed settings** ([server-managed](/docs/en/server-managed-settings), [MDM/OS-level policies](#configuration-scopes), or [managed settings](/docs/en/settings#settings-files))
    - Policies deployed by IT through server delivery, MDM configuration profiles, registry policies, or managed settings files
    - Cannot be overridden by any other level, including command line arguments
    - Within the managed tier, precedence is: server-managed \> MDM/OS-level policies \> `managed-settings.json` \> HKCU registry (Windows only). Only one managed source is used; sources do not merge.
2.  **Command line arguments**
    - Temporary overrides for a specific session
3.  **Local project settings** (`.claude/settings.local.json`)
    - Personal project-specific settings
4.  **Shared project settings** (`.claude/settings.json`)
    - Team-shared project settings in source control
5.  **User settings** (`~/.claude/settings.json`)
    - Personal global settings

This hierarchy ensures that organizational policies are always enforced while still allowing teams and individuals to customize their experience. For example, if your user settings allow `Bash(npm run *)` but a project’s shared settings deny it, the project setting takes precedence and the command is blocked.

**Array settings merge across scopes.** When the same array-valued setting (such as `sandbox.filesystem.allowWrite` or `permissions.allow`) appears in multiple scopes, the arrays are **concatenated and deduplicated**, not replaced. This means lower-priority scopes can add entries without overriding those set by higher-priority scopes, and vice versa. For example, if managed settings set `allowWrite` to `["//opt/company-tools"]` and a user adds `["~/.kube"]`, both paths are included in the final configuration.

### 

[​](#verify-active-settings)

Verify active settings

Run `/status` inside Claude Code to see which settings sources are active and where they come from. The output shows each configuration layer (managed, user, project) along with its origin, such as `Enterprise managed settings (remote)`, `Enterprise managed settings (plist)`, `Enterprise managed settings (HKLM)`, or `Enterprise managed settings (file)`. If a settings file contains errors, `/status` reports the issue so you can fix it.

### 

[​](#key-points-about-the-configuration-system)

Key points about the configuration system

- **Memory files (`CLAUDE.md`)**: Contain instructions and context that Claude loads at startup
- **Settings files (JSON)**: Configure permissions, environment variables, and tool behavior
- **Skills**: Custom prompts that can be invoked with `/skill-name` or loaded by Claude automatically
- **MCP servers**: Extend Claude Code with additional tools and integrations
- **Precedence**: Higher-level configurations (Managed) override lower-level ones (User/Project)
- **Inheritance**: Settings are merged, with more specific settings adding to or overriding broader ones

### 

[​](#system-prompt)

System prompt

Claude Code’s internal system prompt is not published. To add custom instructions, use `CLAUDE.md` files or the `--append-system-prompt` flag.

### 

[​](#excluding-sensitive-files)

Excluding sensitive files

To prevent Claude Code from accessing files containing sensitive information like API keys, secrets, and environment files, use the `permissions.deny` setting in your `.claude/settings.json` file:

Report incorrect code

Copy


``` shiki
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)",
      "Read(./config/credentials.json)",
      "Read(./build)"
    ]
  }
}
```

This replaces the deprecated `ignorePatterns` configuration. Files matching these patterns are excluded from file discovery and search results, and read operations on these files are denied.

## 

[​](#subagent-configuration)

Subagent configuration

Claude Code supports custom AI subagents that can be configured at both user and project levels. These subagents are stored as Markdown files with YAML frontmatter:

- **User subagents**: `~/.claude/agents/` - Available across all your projects
- **Project subagents**: `.claude/agents/` - Specific to your project and can be shared with your team

Subagent files define specialized AI assistants with custom prompts and tool permissions. Learn more about creating and using subagents in the [subagents documentation](/docs/en/sub-agents).

## 

[​](#plugin-configuration)

Plugin configuration

Claude Code supports a plugin system that lets you extend functionality with skills, agents, hooks, and MCP servers. Plugins are distributed through marketplaces and can be configured at both user and repository levels.

### 

[​](#plugin-settings)

Plugin settings

Plugin-related settings in `settings.json`:

Report incorrect code

Copy


``` shiki
{
  "enabledPlugins": {
    "formatter@acme-tools": true,
    "deployer@acme-tools": true,
    "analyzer@security-plugins": false
  },
  "extraKnownMarketplaces": {
    "acme-tools": {
      "source": "github",
      "repo": "acme-corp/claude-plugins"
    }
  }
}
```

#### 

[​](#enabledplugins)

`enabledPlugins`

Controls which plugins are enabled. Format: `"plugin-name@marketplace-name": true/false` **Scopes**:

- **User settings** (`~/.claude/settings.json`): Personal plugin preferences
- **Project settings** (`.claude/settings.json`): Project-specific plugins shared with team
- **Local settings** (`.claude/settings.local.json`): Per-machine overrides (not committed)

**Example**:

Report incorrect code

Copy


``` shiki
{
  "enabledPlugins": {
    "code-formatter@team-tools": true,
    "deployment-tools@team-tools": true,
    "experimental-features@personal": false
  }
}
```

#### 

[​](#extraknownmarketplaces)

`extraKnownMarketplaces`

Defines additional marketplaces that should be made available for the repository. Typically used in repository-level settings to ensure team members have access to required plugin sources. **When a repository includes `extraKnownMarketplaces`**:

1.  Team members are prompted to install the marketplace when they trust the folder
2.  Team members are then prompted to install plugins from that marketplace
3.  Users can skip unwanted marketplaces or plugins (stored in user settings)
4.  Installation respects trust boundaries and requires explicit consent

**Example**:

Report incorrect code

Copy


``` shiki
{
  "extraKnownMarketplaces": {
    "acme-tools": {
      "source": {
        "source": "github",
        "repo": "acme-corp/claude-plugins"
      }
    },
    "security-plugins": {
      "source": {
        "source": "git",
        "url": "https://git.example.com/security/plugins.git"
      }
    }
  }
}
```

**Marketplace source types**:

- `github`: GitHub repository (uses `repo`)
- `git`: Any git URL (uses `url`)
- `directory`: Local filesystem path (uses `path`, for development only)
- `hostPattern`: regex pattern to match marketplace hosts (uses `hostPattern`)

#### 

[​](#strictknownmarketplaces)

`strictKnownMarketplaces`

**Managed settings only**: Controls which plugin marketplaces users are allowed to add. This setting can only be configured in [managed settings](/docs/en/settings#settings-files) and provides administrators with strict control over marketplace sources. **Managed settings file locations**:

- **macOS**: `/Library/Application Support/ClaudeCode/managed-settings.json`
- **Linux and WSL**: `/etc/claude-code/managed-settings.json`
- **Windows**: `C:\Program Files\ClaudeCode\managed-settings.json`

**Key characteristics**:

- Only available in managed settings (`managed-settings.json`)
- Cannot be overridden by user or project settings (highest precedence)
- Enforced BEFORE network/filesystem operations (blocked sources never execute)
- Uses exact matching for source specifications (including `ref`, `path` for git sources), except `hostPattern`, which uses regex matching

**Allowlist behavior**:

- `undefined` (default): No restrictions - users can add any marketplace
- Empty array `[]`: Complete lockdown - users cannot add any new marketplaces
- List of sources: Users can only add marketplaces that match exactly

**All supported source types**: The allowlist supports seven marketplace source types. Most sources use exact matching, while `hostPattern` uses regex matching against the marketplace host.

1.  **GitHub repositories**:

Report incorrect code

Copy


``` shiki
{ "source": "github", "repo": "acme-corp/approved-plugins" }
{ "source": "github", "repo": "acme-corp/security-tools", "ref": "v2.0" }
{ "source": "github", "repo": "acme-corp/plugins", "ref": "main", "path": "marketplace" }
```

Fields: `repo` (required), `ref` (optional: branch/tag/SHA), `path` (optional: subdirectory)

2.  **Git repositories**:

Report incorrect code

Copy


``` shiki
{ "source": "git", "url": "https://gitlab.example.com/tools/plugins.git" }
{ "source": "git", "url": "https://bitbucket.org/acme-corp/plugins.git", "ref": "production" }
{ "source": "git", "url": "ssh://[email protected]/plugins.git", "ref": "v3.1", "path": "approved" }
```

Fields: `url` (required), `ref` (optional: branch/tag/SHA), `path` (optional: subdirectory)

3.  **URL-based marketplaces**:

Report incorrect code

Copy


``` shiki
{ "source": "url", "url": "https://plugins.example.com/marketplace.json" }
{ "source": "url", "url": "https://cdn.example.com/marketplace.json", "headers": { "Authorization": "Bearer ${TOKEN}" } }
```

Fields: `url` (required), `headers` (optional: HTTP headers for authenticated access)

URL-based marketplaces only download the `marketplace.json` file. They do not download plugin files from the server. Plugins in URL-based marketplaces must use external sources (GitHub, npm, or git URLs) rather than relative paths. For plugins with relative paths, use a Git-based marketplace instead. See [Troubleshooting](/docs/en/plugin-marketplaces#plugins-with-relative-paths-fail-in-url-based-marketplaces) for details.

4.  **NPM packages**:

Report incorrect code

Copy


``` shiki
{ "source": "npm", "package": "@acme-corp/claude-plugins" }
{ "source": "npm", "package": "@acme-corp/approved-marketplace" }
```

Fields: `package` (required, supports scoped packages)

5.  **File paths**:

Report incorrect code

Copy


``` shiki
{ "source": "file", "path": "/usr/local/share/claude/acme-marketplace.json" }
{ "source": "file", "path": "/opt/acme-corp/plugins/marketplace.json" }
```

Fields: `path` (required: absolute path to marketplace.json file)

6.  **Directory paths**:

Report incorrect code

Copy


``` shiki
{ "source": "directory", "path": "/usr/local/share/claude/acme-plugins" }
{ "source": "directory", "path": "/opt/acme-corp/approved-marketplaces" }
```

Fields: `path` (required: absolute path to directory containing `.claude-plugin/marketplace.json`)

7.  **Host pattern matching**:

Report incorrect code

Copy


``` shiki
{ "source": "hostPattern", "hostPattern": "^github\\.example\\.com$" }
{ "source": "hostPattern", "hostPattern": "^gitlab\\.internal\\.example\\.com$" }
```

Fields: `hostPattern` (required: regex pattern to match against the marketplace host) Use host pattern matching when you want to allow all marketplaces from a specific host without enumerating each repository individually. This is useful for organizations with internal GitHub Enterprise or GitLab servers where developers create their own marketplaces. Host extraction by source type:

- `github`: always matches against `github.com`
- `git`: extracts hostname from the URL (supports both HTTPS and SSH formats)
- `url`: extracts hostname from the URL
- `npm`, `file`, `directory`: not supported for host pattern matching

**Configuration examples**: Example: allow specific marketplaces only:

Report incorrect code

Copy


``` shiki
{
  "strictKnownMarketplaces": [
    {
      "source": "github",
      "repo": "acme-corp/approved-plugins"
    },
    {
      "source": "github",
      "repo": "acme-corp/security-tools",
      "ref": "v2.0"
    },
    {
      "source": "url",
      "url": "https://plugins.example.com/marketplace.json"
    },
    {
      "source": "npm",
      "package": "@acme-corp/compliance-plugins"
    }
  ]
}
```

Example - Disable all marketplace additions:

Report incorrect code

Copy


``` shiki
{
  "strictKnownMarketplaces": []
}
```

Example: allow all marketplaces from an internal git server:

Report incorrect code

Copy


``` shiki
{
  "strictKnownMarketplaces": [
    {
      "source": "hostPattern",
      "hostPattern": "^github\\.example\\.com$"
    }
  ]
}
```

**Exact matching requirements**: Marketplace sources must match **exactly** for a user’s addition to be allowed. For git-based sources (`github` and `git`), this includes all optional fields:

- The `repo` or `url` must match exactly
- The `ref` field must match exactly (or both be undefined)
- The `path` field must match exactly (or both be undefined)

Examples of sources that **do NOT match**:

Report incorrect code

Copy


``` shiki
// These are DIFFERENT sources:
{ "source": "github", "repo": "acme-corp/plugins" }
{ "source": "github", "repo": "acme-corp/plugins", "ref": "main" }

// These are also DIFFERENT:
{ "source": "github", "repo": "acme-corp/plugins", "path": "marketplace" }
{ "source": "github", "repo": "acme-corp/plugins" }
```

**Comparison with `extraKnownMarketplaces`**:

| Aspect | `strictKnownMarketplaces` | `extraKnownMarketplaces` |
|----|----|----|
| **Purpose** | Organizational policy enforcement | Team convenience |
| **Settings file** | `managed-settings.json` only | Any settings file |
| **Behavior** | Blocks non-allowlisted additions | Auto-installs missing marketplaces |
| **When enforced** | Before network/filesystem operations | After user trust prompt |
| **Can be overridden** | No (highest precedence) | Yes (by higher precedence settings) |
| **Source format** | Direct source object | Named marketplace with nested source |
| **Use case** | Compliance, security restrictions | Onboarding, standardization |

**Format difference**: `strictKnownMarketplaces` uses direct source objects:

Report incorrect code

Copy


``` shiki
{
  "strictKnownMarketplaces": [
    { "source": "github", "repo": "acme-corp/plugins" }
  ]
}
```

`extraKnownMarketplaces` requires named marketplaces:

Report incorrect code

Copy


``` shiki
{
  "extraKnownMarketplaces": {
    "acme-tools": {
      "source": { "source": "github", "repo": "acme-corp/plugins" }
    }
  }
}
```

**Using both together**: `strictKnownMarketplaces` is a policy gate: it controls what users may add but does not register any marketplaces. To both restrict and pre-register a marketplace for all users, set both in `managed-settings.json`:

Report incorrect code

Copy


``` shiki
{
  "strictKnownMarketplaces": [
    { "source": "github", "repo": "acme-corp/plugins" }
  ],
  "extraKnownMarketplaces": {
    "acme-tools": {
      "source": { "source": "github", "repo": "acme-corp/plugins" }
    }
  }
}
```

With only `strictKnownMarketplaces` set, users can still add the allowed marketplace manually via `/plugin marketplace add`, but it is not available automatically. **Important notes**:

- Restrictions are checked BEFORE any network requests or filesystem operations
- When blocked, users see clear error messages indicating the source is blocked by managed policy
- The restriction applies only to adding NEW marketplaces; previously installed marketplaces remain accessible
- Managed settings have the highest precedence and cannot be overridden

See [Managed marketplace restrictions](/docs/en/plugin-marketplaces#managed-marketplace-restrictions) for user-facing documentation.

### 

[​](#managing-plugins)

Managing plugins

Use the `/plugin` command to manage plugins interactively:

- Browse available plugins from marketplaces
- Install/uninstall plugins
- Enable/disable plugins
- View plugin details (commands, agents, hooks provided)
- Add/remove marketplaces

Learn more about the plugin system in the [plugins documentation](/docs/en/plugins).

## 

[​](#environment-variables)

Environment variables

Environment variables let you control Claude Code behavior without editing settings files. Any variable can also be configured in [`settings.json`](#available-settings) under the `env` key to apply it to every session or roll it out to your team. See the [environment variables reference](/docs/en/env-vars) for the full list.

## 

[​](#tools-available-to-claude)

Tools available to Claude

Claude Code has access to a set of tools for reading, editing, searching, running commands, and orchestrating subagents. Tool names are the exact strings you use in permission rules and hook matchers. See the [tools reference](/docs/en/tools-reference) for the full list and Bash tool behavior details.

## 

[​](#see-also)

See also

- [Permissions](/docs/en/permissions): permission system, rule syntax, tool-specific patterns, and managed policies
- [Authentication](/docs/en/authentication): set up user access to Claude Code
- [Troubleshooting](/docs/en/troubleshooting): solutions for common configuration issues
