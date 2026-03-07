---
category: "02-Claude-Code-CLI"
fetched_at: "2026-03-07T01:05:51Z"
source_url: "https://code.claude.com/docs/en/setup"
title: "Advanced setup - Claude Code Docs"
---

# Advanced setup


System requirements, platform-specific installation, version management, and uninstallation for Claude Code.


This page covers system requirements, platform-specific installation details, updates, and uninstallation. For a guided walkthrough of your first session, see the [quickstart](/docs/en/quickstart). If you’ve never used a terminal before, see the [terminal guide](/docs/en/terminal-guide).

## 

[​](#system-requirements)

System requirements

Claude Code runs on the following platforms and configurations:

- **Operating system**:
  - macOS 13.0+
  - Windows 10 1809+ or Windows Server 2019+
  - Ubuntu 20.04+
  - Debian 10+
  - Alpine Linux 3.19+
- **Hardware**: 4 GB+ RAM
- **Network**: internet connection required. See [network configuration](/docs/en/network-config#network-access-requirements).
- **Shell**: Bash, Zsh, PowerShell, or CMD. On Windows, [Git for Windows](https://git-scm.com/downloads/win) is required.
- **Location**: [Anthropic supported countries](https://www.anthropic.com/supported-countries)

### 

[​](#additional-dependencies)

Additional dependencies

- **ripgrep**: usually included with Claude Code. If search fails, see [search troubleshooting](/docs/en/troubleshooting#search-and-discovery-issues).

## 

[​](#install-claude-code)

Install Claude Code

Prefer a graphical interface? The [Desktop app](/docs/en/desktop-quickstart) lets you use Claude Code without the terminal. Download it for [macOS](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect?utm_source=claude_code&utm_medium=docs) or [Windows](https://claude.ai/api/desktop/win32/x64/exe/latest/redirect?utm_source=claude_code&utm_medium=docs).New to the terminal? See the [terminal guide](/docs/en/terminal-guide) for step-by-step instructions.

To install Claude Code, use one of the following methods:

- Native Install (Recommended)

- Homebrew

- WinGet

**macOS, Linux, WSL:**

Report incorrect code

Copy


``` shiki
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**

Report incorrect code

Copy


``` shiki
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD:**

Report incorrect code

Copy


``` shiki
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

**Windows requires [Git for Windows](https://git-scm.com/downloads/win).** Install it first if you don’t have it.

Native installations automatically update in the background to keep you on the latest version.

Report incorrect code

Copy


``` shiki
brew install --cask claude-code
```

Homebrew installations do not auto-update. Run `brew upgrade claude-code` periodically to get the latest features and security fixes.

Report incorrect code

Copy


``` shiki
winget install Anthropic.ClaudeCode
```

WinGet installations do not auto-update. Run `winget upgrade Anthropic.ClaudeCode` periodically to get the latest features and security fixes.

After installation completes, open a terminal in the project you want to work in and start Claude Code:

Report incorrect code

Copy


``` shiki
claude
```

If you encounter any issues during installation, see the [troubleshooting guide](/docs/en/troubleshooting).

### 

[​](#set-up-on-windows)

Set up on Windows

Claude Code on Windows requires [Git for Windows](https://git-scm.com/downloads/win) or WSL. You can launch `claude` from PowerShell, CMD, or Git Bash. Claude Code uses Git Bash internally to run commands. You do not need to run PowerShell as Administrator. **Option 1: Native Windows with Git Bash** Install [Git for Windows](https://git-scm.com/downloads/win), then run the install command from PowerShell or CMD. If Claude Code can’t find your Git Bash installation, set the path in your [settings.json file](/docs/en/settings):

Report incorrect code

Copy


``` shiki
{
  "env": {
    "CLAUDE_CODE_GIT_BASH_PATH": "C:\\Program Files\\Git\\bin\\bash.exe"
  }
}
```

**Option 2: WSL** Both WSL 1 and WSL 2 are supported. WSL 2 supports [sandboxing](/docs/en/sandboxing) for enhanced security. WSL 1 does not support sandboxing.

### 

[​](#alpine-linux-and-musl-based-distributions)

Alpine Linux and musl-based distributions

The native installer on Alpine and other musl/uClibc-based distributions requires `libgcc`, `libstdc++`, and `ripgrep`. Install these using your distribution’s package manager, then set `USE_BUILTIN_RIPGREP=0`. This example installs the required packages on Alpine:

Report incorrect code

Copy


``` shiki
apk add libgcc libstdc++ ripgrep
```

Then set `USE_BUILTIN_RIPGREP` to `0` in your [settings.json file](/docs/en/settings#environment-variables):

Report incorrect code

Copy


``` shiki
{
  "env": {
    "USE_BUILTIN_RIPGREP": "0"
  }
}
```

## 

[​](#verify-your-installation)

Verify your installation

After installing, confirm Claude Code is working:

Report incorrect code

Copy


``` shiki
claude --version
```

For a more detailed check of your installation and configuration, run [`claude doctor`](/docs/en/troubleshooting#get-more-help):

Report incorrect code

Copy


``` shiki
claude doctor
```

## 

[​](#authenticate)

Authenticate

Claude Code requires a Pro, Max, Teams, Enterprise, or Console account. The free Claude.ai plan does not include Claude Code access. You can also use Claude Code with a third-party API provider like [Amazon Bedrock](/docs/en/amazon-bedrock), [Google Vertex AI](/docs/en/google-vertex-ai), or [Microsoft Foundry](/docs/en/microsoft-foundry). After installing, log in by running `claude` and following the browser prompts. See [Authentication](/docs/en/authentication) for all account types and team setup options.

## 

[​](#update-claude-code)

Update Claude Code

Native installations automatically update in the background. You can [configure the release channel](#configure-release-channel) to control whether you receive updates immediately or on a delayed stable schedule, or [disable auto-updates](#disable-auto-updates) entirely. Homebrew and WinGet installations require manual updates.

### 

[​](#auto-updates)

Auto-updates

Claude Code checks for updates on startup and periodically while running. Updates download and install in the background, then take effect the next time you start Claude Code.

Homebrew and WinGet installations do not auto-update. Use `brew upgrade claude-code` or `winget upgrade Anthropic.ClaudeCode` to update manually.**Known issue:** Claude Code may notify you of updates before the new version is available in these package managers. If an upgrade fails, wait and try again later.Homebrew keeps old versions on disk after upgrades. Run `brew cleanup claude-code` periodically to reclaim disk space.

### 

[​](#configure-release-channel)

Configure release channel

Control which release channel Claude Code follows for auto-updates and `claude update` with the `autoUpdatesChannel` setting:

- `"latest"`, the default: receive new features as soon as they’re released
- `"stable"`: use a version that is typically about one week old, skipping releases with major regressions

Configure this via `/config` → **Auto-update channel**, or add it to your [settings.json file](/docs/en/settings):

Report incorrect code

Copy


``` shiki
{
  "autoUpdatesChannel": "stable"
}
```

For enterprise deployments, you can enforce a consistent release channel across your organization using [managed settings](/docs/en/permissions#managed-settings).

### 

[​](#disable-auto-updates)

Disable auto-updates

Set `DISABLE_AUTOUPDATER` to `"1"` in the `env` key of your [settings.json file](/docs/en/settings#environment-variables):

Report incorrect code

Copy


``` shiki
{
  "env": {
    "DISABLE_AUTOUPDATER": "1"
  }
}
```

### 

[​](#update-manually)

Update manually

To apply an update immediately without waiting for the next background check, run:

Report incorrect code

Copy


``` shiki
claude update
```

## 

[​](#advanced-installation-options)

Advanced installation options

These options are for version pinning, migrating from npm, and verifying binary integrity.

### 

[​](#install-a-specific-version)

Install a specific version

The native installer accepts either a specific version number or a release channel (`latest` or `stable`). The channel you choose at install time becomes your default for auto-updates. See [configure release channel](#configure-release-channel) for more information. To install the latest version (default):

- macOS, Linux, WSL

- Windows PowerShell

- Windows CMD

Report incorrect code

Copy


``` shiki
curl -fsSL https://claude.ai/install.sh | bash
```

Report incorrect code

Copy


``` shiki
irm https://claude.ai/install.ps1 | iex
```

Report incorrect code

Copy


``` shiki
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

To install the stable version:

- macOS, Linux, WSL

- Windows PowerShell

- Windows CMD

Report incorrect code

Copy


``` shiki
curl -fsSL https://claude.ai/install.sh | bash -s stable
```

Report incorrect code

Copy


``` shiki
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) stable
```

Report incorrect code

Copy


``` shiki
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd stable && del install.cmd
```

To install a specific version number:

- macOS, Linux, WSL

- Windows PowerShell

- Windows CMD

Report incorrect code

Copy


``` shiki
curl -fsSL https://claude.ai/install.sh | bash -s 1.0.58
```

Report incorrect code

Copy


``` shiki
& ([scriptblock]::Create((irm https://claude.ai/install.ps1))) 1.0.58
```

Report incorrect code

Copy


``` shiki
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd 1.0.58 && del install.cmd
```

### 

[​](#deprecated-npm-installation)

Deprecated npm installation

npm installation is deprecated. The native installer is faster, requires no dependencies, and auto-updates in the background. Use the [native installation](#install-claude-code) method when possible.

#### 

[​](#migrate-from-npm-to-native)

Migrate from npm to native

If you previously installed Claude Code with npm, switch to the native installer:

Report incorrect code

Copy


``` shiki
# Install the native binary
curl -fsSL https://claude.ai/install.sh | bash

# Remove the old npm installation
npm uninstall -g @anthropic-ai/claude-code
```

You can also run `claude install` from an existing npm installation to install the native binary alongside it, then remove the npm version.

#### 

[​](#install-with-npm)

Install with npm

If you need npm installation for compatibility reasons, you must have [Node.js 18+](https://nodejs.org/en/download) installed. Install the package globally:

Report incorrect code

Copy


``` shiki
npm install -g @anthropic-ai/claude-code
```

Do NOT use `sudo npm install -g` as this can lead to permission issues and security risks. If you encounter permission errors, see [troubleshooting permission errors](/docs/en/troubleshooting#permission-errors-during-installation).

### 

[​](#binary-integrity-and-code-signing)

Binary integrity and code signing

You can verify the integrity of Claude Code binaries using SHA256 checksums and code signatures.

- SHA256 checksums for all platforms are published in the release manifests at `https://storage.googleapis.com/claude-code-dist-86c565f3-f756-42ad-8dfa-d59b1c096819/claude-code-releases/{VERSION}/manifest.json`. Replace `{VERSION}` with a version number such as `2.0.30`.
- Signed binaries are distributed for the following platforms:
  - **macOS**: signed by “Anthropic PBC” and notarized by Apple
  - **Windows**: signed by “Anthropic, PBC”

## 

[​](#uninstall-claude-code)

Uninstall Claude Code

To remove Claude Code, follow the instructions for your installation method.

### 

[​](#native-installation)

Native installation

Remove the Claude Code binary and version files:

- macOS, Linux, WSL

- Windows PowerShell

Report incorrect code

Copy


``` shiki
rm -f ~/.local/bin/claude
rm -rf ~/.local/share/claude
```

Report incorrect code

Copy


``` shiki
Remove-Item -Path "$env:USERPROFILE\.local\bin\claude.exe" -Force
Remove-Item -Path "$env:USERPROFILE\.local\share\claude" -Recurse -Force
```

### 

[​](#homebrew-installation)

Homebrew installation

Remove the Homebrew cask:

Report incorrect code

Copy


``` shiki
brew uninstall --cask claude-code
```

### 

[​](#winget-installation)

WinGet installation

Remove the WinGet package:

Report incorrect code

Copy


``` shiki
winget uninstall Anthropic.ClaudeCode
```

### 

[​](#npm)

npm

Remove the global npm package:

Report incorrect code

Copy


``` shiki
npm uninstall -g @anthropic-ai/claude-code
```

### 

[​](#remove-configuration-files)

Remove configuration files

Removing configuration files will delete all your settings, allowed tools, MCP server configurations, and session history.

To remove Claude Code settings and cached data:

- macOS, Linux, WSL

- Windows PowerShell

Report incorrect code

Copy


``` shiki
# Remove user settings and state
rm -rf ~/.claude
rm ~/.claude.json

# Remove project-specific settings (run from your project directory)
rm -rf .claude
rm -f .mcp.json
```

Report incorrect code

Copy


``` shiki
# Remove user settings and state
Remove-Item -Path "$env:USERPROFILE\.claude" -Recurse -Force
Remove-Item -Path "$env:USERPROFILE\.claude.json" -Force

# Remove project-specific settings (run from your project directory)
Remove-Item -Path ".claude" -Recurse -Force
Remove-Item -Path ".mcp.json" -Force
```
