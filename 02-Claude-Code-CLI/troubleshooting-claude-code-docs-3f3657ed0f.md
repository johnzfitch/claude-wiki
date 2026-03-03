---
category: "02-Claude-Code-CLI"
fetched_at: "2026-03-03T15:08:36Z"
source_url: "https://code.claude.com/docs/en/troubleshooting"
title: "Troubleshooting - Claude Code Docs"
---

# Troubleshooting


Discover solutions to common issues with Claude Code installation and usage.


## 

[​](#troubleshoot-installation-issues)

Troubleshoot installation issues

If you’d rather skip the terminal entirely, the [Claude Code Desktop app](/docs/en/desktop-quickstart) lets you install and use Claude Code through a graphical interface. Download it for [macOS](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect?utm_source=claude_code&utm_medium=docs) or [Windows](https://claude.ai/api/desktop/win32/x64/exe/latest/redirect?utm_source=claude_code&utm_medium=docs) and start coding without any command-line setup.

Find the error message or symptom you’re seeing:

| What you see | Solution |
|:---|:---|
| `command not found: claude` or `'claude' is not recognized` | [Fix your PATH](#command-not-found-claude-after-installation) |
| `syntax error near unexpected token '<'` | [Install script returns HTML](#install-script-returns-html-instead-of-a-shell-script) |
| `curl: (56) Failure writing output to destination` | [Download script first, then run it](#curl-56-failure-writing-output-to-destination) |
| `Killed` during install on Linux | [Add swap space for low-memory servers](#install-killed-on-low-memory-linux-servers) |
| `TLS connect error` or `SSL/TLS secure channel` | [Update CA certificates](#tls-or-ssl-connection-errors) |
| `Failed to fetch version` or can’t reach download server | [Check network and proxy settings](#check-network-connectivity) |
| `irm is not recognized` or `&& is not valid` | [Use the right command for your shell](#windows-irm-or--not-recognized) |
| `Claude Code on Windows requires git-bash` | [Install or configure Git Bash](#windows-claude-code-on-windows-requires-git-bash) |
| `Error loading shared library` | [Wrong binary variant for your system](#linux-wrong-binary-variant-installed-muslglibc-mismatch) |
| `Illegal instruction` on Linux | [Architecture mismatch](#illegal-instruction-on-linux) |
| `dyld: cannot load` or `Abort trap` on macOS | [Binary incompatibility](#dyld-cannot-load-on-macos) |
| `Invoke-Expression: Missing argument in parameter list` | [Install script returns HTML](#install-script-returns-html-instead-of-a-shell-script) |
| `App unavailable in region` | Claude Code is not available in your country. See [supported countries](https://www.anthropic.com/supported-countries). |
| `unable to get local issuer certificate` | [Configure corporate CA certificates](#tls-or-ssl-connection-errors) |
| `OAuth error` or `403 Forbidden` | [Fix authentication](#authentication-issues) |

If your issue isn’t listed, work through these diagnostic steps.

## 

[​](#debug-installation-problems)

Debug installation problems

### 

[​](#check-network-connectivity)

Check network connectivity

The installer downloads from `storage.googleapis.com`. Verify you can reach it:

Report incorrect code

Copy


``` shiki
curl -sI https://storage.googleapis.com
```

If this fails, your network may be blocking the connection. Common causes:

- Corporate firewalls or proxies blocking Google Cloud Storage
- Regional network restrictions: try a VPN or alternative network
- TLS/SSL issues: update your system’s CA certificates, or check if `HTTPS_PROXY` is configured

If you’re behind a corporate proxy, set `HTTPS_PROXY` and `HTTP_PROXY` to your proxy’s address before installing. Ask your IT team for the proxy URL if you don’t know it, or check your browser’s proxy settings. This example sets both proxy variables, then runs the installer through your proxy:

Report incorrect code

Copy


``` shiki
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080
curl -fsSL https://claude.ai/install.sh | bash
```

### 

[​](#verify-your-path)

Verify your PATH

If installation succeeded but you get a `command not found` or `not recognized` error when running `claude`, the install directory isn’t in your PATH. Your shell searches for programs in directories listed in PATH, and the installer places `claude` at `~/.local/bin/claude` on macOS/Linux or `%USERPROFILE%\.local\bin\claude.exe` on Windows. Check if the install directory is in your PATH by listing your PATH entries and filtering for `local/bin`:

- macOS/Linux

- Windows PowerShell

- Windows CMD

Report incorrect code

Copy


``` shiki
echo $PATH | tr ':' '\n' | grep local/bin
```

If there’s no output, the directory is missing. Add it to your shell configuration:

Report incorrect code

Copy


``` shiki
# Zsh (macOS default)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Bash (Linux default)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Alternatively, close and reopen your terminal.Verify the fix worked:

Report incorrect code

Copy


``` shiki
claude --version
```

Report incorrect code

Copy


``` shiki
$env:PATH -split ';' | Select-String 'local\\bin'
```

If there’s no output, add the install directory to your User PATH:

Report incorrect code

Copy


``` shiki
$currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
[Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')
```

Restart your terminal for the change to take effect.Verify the fix worked:

Report incorrect code

Copy


``` shiki
claude --version
```

Report incorrect code

Copy


``` shiki
echo %PATH% | findstr /i "local\bin"
```

If there’s no output, open System Settings, go to Environment Variables, and add `%USERPROFILE%\.local\bin` to your User PATH variable. Restart your terminal.Verify the fix worked:

Report incorrect code

Copy


``` shiki
claude --version
```

### 

[​](#check-for-conflicting-installations)

Check for conflicting installations

Multiple Claude Code installations can cause version mismatches or unexpected behavior. Check what’s installed:

- macOS/Linux

- Windows PowerShell

List all `claude` binaries found in your PATH:

Report incorrect code

Copy


``` shiki
which -a claude
```

Check whether the native installer and npm versions are present:

Report incorrect code

Copy


``` shiki
ls -la ~/.local/bin/claude
```

Report incorrect code

Copy


``` shiki
ls -la ~/.claude/local/
```

Report incorrect code

Copy


``` shiki
npm -g ls @anthropic-ai/claude-code 2>/dev/null
```

Report incorrect code

Copy


``` shiki
where.exe claude
Test-Path "$env:LOCALAPPDATA\Claude Code\claude.exe"
```

If you find multiple installations, keep only one. The native install at `~/.local/bin/claude` is recommended. Remove any extra installations: Uninstall an npm global install:

Report incorrect code

Copy


``` shiki
npm uninstall -g @anthropic-ai/claude-code
```

Remove a Homebrew install on macOS:

Report incorrect code

Copy


``` shiki
brew uninstall --cask claude-code
```

### 

[​](#check-directory-permissions)

Check directory permissions

The installer needs write access to `~/.local/bin/` and `~/.claude/`. If installation fails with permission errors, check whether these directories are writable:

Report incorrect code

Copy


``` shiki
test -w ~/.local/bin && echo "writable" || echo "not writable"
test -w ~/.claude && echo "writable" || echo "not writable"
```

If either directory isn’t writable, create the install directory and set your user as the owner:

Report incorrect code

Copy


``` shiki
sudo mkdir -p ~/.local/bin
sudo chown -R $(whoami) ~/.local
```

### 

[​](#verify-the-binary-works)

Verify the binary works

If `claude` is installed but crashes or hangs on startup, run these checks to narrow down the cause. Confirm the binary exists and is executable:

Report incorrect code

Copy


``` shiki
ls -la $(which claude)
```

On Linux, check for missing shared libraries. If `ldd` shows missing libraries, you may need to install system packages. On Alpine Linux and other musl-based distributions, see [Alpine Linux setup](/docs/en/setup#alpine-linux-and-musl-based-distributions).

Report incorrect code

Copy


``` shiki
ldd $(which claude) | grep "not found"
```

Run a quick sanity check that the binary can execute:

Report incorrect code

Copy


``` shiki
claude --version
```

## 

[​](#common-installation-issues)

Common installation issues

These are the most frequently encountered installation problems and their solutions.

### 

[​](#install-script-returns-html-instead-of-a-shell-script)

Install script returns HTML instead of a shell script

When running the install command, you may see one of these errors:

Report incorrect code

Copy


``` shiki
bash: line 1: syntax error near unexpected token `<'
bash: line 1: `<!DOCTYPE html>'
```

On PowerShell, the same problem appears as:

Report incorrect code

Copy


``` shiki
Invoke-Expression: Missing argument in parameter list.
```

This means the install URL returned an HTML page instead of the install script. If the HTML page says “App unavailable in region,” Claude Code is not available in your country. See [supported countries](https://www.anthropic.com/supported-countries). Otherwise, this can happen due to network issues, regional routing, or a temporary service disruption. **Solutions:**

1.  **Use an alternative install method**: On macOS or Linux, install via Homebrew:
    Report incorrect code

    Copy


    ``` shiki
    brew install --cask claude-code
    ```

    On Windows, install via WinGet:
    Report incorrect code

    Copy


    ``` shiki
    winget install Anthropic.ClaudeCode
    ```
2.  **Retry after a few minutes**: the issue is often temporary. Wait and try the original command again.

### 

[​](#command-not-found-claude-after-installation)

`command not found: claude` after installation

The install finished but `claude` doesn’t work. The exact error varies by platform:

| Platform | Error message |
|:---|:---|
| macOS | `zsh: command not found: claude` |
| Linux | `bash: claude: command not found` |
| Windows CMD | `'claude' is not recognized as an internal or external command` |
| PowerShell | `claude : The term 'claude' is not recognized as the name of a cmdlet` |

This means the install directory isn’t in your shell’s search path. See [Verify your PATH](#verify-your-path) for the fix on each platform.

### 

[​](#curl-56-failure-writing-output-to-destination)

`curl: (56) Failure writing output to destination`

The `curl ... | bash` command downloads the script and passes it directly to Bash for execution using a pipe (`|`). This error means the connection broke before the script finished downloading. Common causes include network interruptions, the download being blocked mid-stream, or system resource limits. **Solutions:**

1.  **Check network stability**: Claude Code binaries are hosted on Google Cloud Storage. Test that you can reach it:
    Report incorrect code

    Copy


    ``` shiki
    curl -fsSL https://storage.googleapis.com -o /dev/null
    ```

    If the command completes silently, your connection is fine and the issue is likely intermittent. Retry the install command. If you see an error, your network may be blocking the download.
2.  **Try an alternative install method**: On macOS or Linux:
    Report incorrect code

    Copy


    ``` shiki
    brew install --cask claude-code
    ```

    On Windows:
    Report incorrect code

    Copy


    ``` shiki
    winget install Anthropic.ClaudeCode
    ```

### 

[​](#tls-or-ssl-connection-errors)

TLS or SSL connection errors

Errors like `curl: (35) TLS connect error`, `schannel: next InitializeSecurityContext failed`, or PowerShell’s `Could not establish trust relationship for the SSL/TLS secure channel` indicate TLS handshake failures. **Solutions:**

1.  **Update your system CA certificates**: On Ubuntu/Debian:
    Report incorrect code

    Copy


    ``` shiki
    sudo apt-get update && sudo apt-get install ca-certificates
    ```

    On macOS via Homebrew:
    Report incorrect code

    Copy


    ``` shiki
    brew install ca-certificates
    ```
2.  **On Windows, enable TLS 1.2** in PowerShell before running the installer:
    Report incorrect code

    Copy


    ``` shiki
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    irm https://claude.ai/install.ps1 | iex
    ```
3.  **Check for proxy or firewall interference**: corporate proxies that perform TLS inspection can cause these errors, including `unable to get local issuer certificate`. Set `NODE_EXTRA_CA_CERTS` to your corporate CA certificate bundle:
    Report incorrect code

    Copy


    ``` shiki
    export NODE_EXTRA_CA_CERTS=/path/to/corporate-ca.pem
    ```

    Ask your IT team for the certificate file if you don’t have it. You can also try on a direct connection to confirm the proxy is the cause.

### 

[​](#failed-to-fetch-version-from-storage-googleapis-com)

`Failed to fetch version from storage.googleapis.com`

The installer couldn’t reach the download server. This typically means `storage.googleapis.com` is blocked on your network. **Solutions:**

1.  **Test connectivity directly**:
    Report incorrect code

    Copy


    ``` shiki
    curl -sI https://storage.googleapis.com
    ```
2.  **If behind a proxy**, set `HTTPS_PROXY` so the installer can route through it. See [proxy configuration](/docs/en/network-config#proxy-configuration) for details.
    Report incorrect code

    Copy


    ``` shiki
    export HTTPS_PROXY=http://proxy.example.com:8080
    curl -fsSL https://claude.ai/install.sh | bash
    ```
3.  **If on a restricted network**, try a different network or VPN, or use an alternative install method: On macOS or Linux:
    Report incorrect code

    Copy


    ``` shiki
    brew install --cask claude-code
    ```

    On Windows:
    Report incorrect code

    Copy


    ``` shiki
    winget install Anthropic.ClaudeCode
    ```

### 

[​](#windows-irm-or-&&-not-recognized)

Windows: `irm` or `&&` not recognized

If you see `'irm' is not recognized` or `The token '&&' is not valid`, you’re running the wrong command for your shell.

- **`irm` not recognized**: you’re in CMD, not PowerShell. You have two options: Open PowerShell by searching for “PowerShell” in the Start menu, then run the original install command:
  Report incorrect code

  Copy


  ``` shiki
  irm https://claude.ai/install.ps1 | iex
  ```

  Or stay in CMD and use the CMD installer instead:
  Report incorrect code

  Copy


  ``` shiki
  curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
  ```
- **`&&` not valid**: you’re in PowerShell but ran the CMD installer command. Use the PowerShell installer:
  Report incorrect code

  Copy


  ``` shiki
  irm https://claude.ai/install.ps1 | iex
  ```

### 

[​](#install-killed-on-low-memory-linux-servers)

Install killed on low-memory Linux servers

If you see `Killed` during installation on a VPS or cloud instance:

Report incorrect code

Copy


``` shiki
Setting up Claude Code...
Installing Claude Code native build latest...
bash: line 142: 34803 Killed    "$binary_path" install ${TARGET:+"$TARGET"}
```

The Linux OOM killer terminated the process because the system ran out of memory. Claude Code requires at least 4 GB of available RAM. **Solutions:**

1.  **Add swap space** if your server has limited RAM. Swap uses disk space as overflow memory, letting the install complete even with low physical RAM. Create a 2 GB swap file and enable it:
    Report incorrect code

    Copy


    ``` shiki
    sudo fallocate -l 2G /swapfile
    sudo chmod 600 /swapfile
    sudo mkswap /swapfile
    sudo swapon /swapfile
    ```

    Then retry the installation:
    Report incorrect code

    Copy


    ``` shiki
    curl -fsSL https://claude.ai/install.sh | bash
    ```
2.  **Close other processes** to free memory before installing.
3.  **Use a larger instance** if possible. Claude Code requires at least 4 GB of RAM.

### 

[​](#install-hangs-in-docker)

Install hangs in Docker

When installing Claude Code in a Docker container, installing as root into `/` can cause hangs. **Solutions:**

1.  **Set a working directory** before running the installer. When run from `/`, the installer scans the entire filesystem, which causes excessive memory usage. Setting `WORKDIR` limits the scan to a small directory:
    Report incorrect code

    Copy


    ``` shiki
    WORKDIR /tmp
    RUN curl -fsSL https://claude.ai/install.sh | bash
    ```
2.  **Increase Docker memory limits** if using Docker Desktop:
    Report incorrect code

    Copy


    ``` shiki
    docker build --memory=4g .
    ```

### 

[​](#windows-claude-desktop-overrides-claude-cli-command)

Windows: Claude Desktop overrides `claude` CLI command

If you installed an older version of Claude Desktop, it may register a `Claude.exe` in the `WindowsApps` directory that takes PATH priority over Claude Code CLI. Running `claude` opens the Desktop app instead of the CLI. Update Claude Desktop to the latest version to fix this issue.

### 

[​](#windows-“claude-code-on-windows-requires-git-bash”)

Windows: “Claude Code on Windows requires git-bash”

Claude Code on native Windows needs [Git for Windows](https://git-scm.com/downloads/win), which includes Git Bash. **If Git is not installed**, download and install it from [git-scm.com/downloads/win](https://git-scm.com/downloads/win). During setup, select “Add to PATH.” Restart your terminal after installing. **If Git is already installed** but Claude Code still can’t find it, set the path in your [settings.json file](/docs/en/settings):

Report incorrect code

Copy


``` shiki
{
  "env": {
    "CLAUDE_CODE_GIT_BASH_PATH": "C:\\Program Files\\Git\\bin\\bash.exe"
  }
}
```

If your Git is installed somewhere else, find the path by running `where.exe git` in PowerShell and use the `bin\bash.exe` path from that directory.

### 

[​](#linux-wrong-binary-variant-installed-musl/glibc-mismatch)

Linux: wrong binary variant installed (musl/glibc mismatch)

If you see errors about missing shared libraries like `libstdc++.so.6` or `libgcc_s.so.1` after installation, the installer may have downloaded the wrong binary variant for your system.

Report incorrect code

Copy


``` shiki
Error loading shared library libstdc++.so.6: No such file or directory
```

This can happen on glibc-based systems that have musl cross-compilation packages installed, causing the installer to misdetect the system as musl. **Solutions:**

1.  **Check which libc your system uses**:
    Report incorrect code

    Copy


    ``` shiki
    ldd /bin/ls | head -1
    ```

    If it shows `linux-vdso.so` or references to `/lib/x86_64-linux-gnu/`, you’re on glibc. If it shows `musl`, you’re on musl.
2.  **If you’re on glibc but got the musl binary**, remove the installation and reinstall. You can also manually download the correct binary from the GCS bucket at `https://storage.googleapis.com/claude-code-dist-86c565f3-f756-42ad-8dfa-d59b1c096819/claude-code-releases/{VERSION}/manifest.json`. File a [GitHub issue](https://github.com/anthropics/claude-code/issues) with the output of `ldd /bin/ls` and `ls /lib/libc.musl*`.
3.  **If you’re actually on musl** (Alpine Linux), install the required packages:
    Report incorrect code

    Copy


    ``` shiki
    apk add libgcc libstdc++ ripgrep
    ```

### 

[​](#illegal-instruction-on-linux)

`Illegal instruction` on Linux

If the installer prints `Illegal instruction` instead of the OOM `Killed` message, the downloaded binary doesn’t match your CPU architecture. This commonly happens on ARM servers that receive an x86 binary, or on older CPUs that lack required instruction sets.

Report incorrect code

Copy


``` shiki
bash: line 142: 2238232 Illegal instruction    "$binary_path" install ${TARGET:+"$TARGET"}
```

**Solutions:**

1.  **Verify your architecture**:
    Report incorrect code

    Copy


    ``` shiki
    uname -m
    ```

    `x86_64` means 64-bit Intel/AMD, `aarch64` means ARM64. If the binary doesn’t match, [file a GitHub issue](https://github.com/anthropics/claude-code/issues) with the output.
2.  **Try an alternative install method** while the architecture issue is resolved:
    Report incorrect code

    Copy


    ``` shiki
    brew install --cask claude-code
    ```

### 

[​](#dyld-cannot-load-on-macos)

`dyld: cannot load` on macOS

If you see `dyld: cannot load` or `Abort trap: 6` during installation, the binary is incompatible with your macOS version or hardware.

Report incorrect code

Copy


``` shiki
dyld: cannot load 'claude-2.1.42-darwin-x64' (load command 0x80000034 is unknown)
Abort trap: 6
```

**Solutions:**

1.  **Check your macOS version**: Claude Code requires macOS 13.0 or later. Open the Apple menu and select About This Mac to check your version.
2.  **Update macOS** if you’re on an older version. The binary uses load commands that older macOS versions don’t support.
3.  **Try Homebrew** as an alternative install method:
    Report incorrect code

    Copy


    ``` shiki
    brew install --cask claude-code
    ```

### 

[​](#windows-installation-issues-errors-in-wsl)

Windows installation issues: errors in WSL

You might encounter the following issues in WSL: **OS/platform detection issues**: if you receive an error during installation, WSL may be using Windows `npm`. Try:

- Run `npm config set os linux` before installation
- Install with `npm install -g @anthropic-ai/claude-code --force --no-os-check`. Do not use `sudo`.

**Node not found errors**: if you see `exec: node: not found` when running `claude`, your WSL environment may be using a Windows installation of Node.js. You can confirm this with `which npm` and `which node`, which should point to Linux paths starting with `/usr/` rather than `/mnt/c/`. To fix this, try installing Node via your Linux distribution’s package manager or via [`nvm`](https://github.com/nvm-sh/nvm). **nvm version conflicts**: if you have nvm installed in both WSL and Windows, you may experience version conflicts when switching Node versions in WSL. This happens because WSL imports the Windows PATH by default, causing Windows nvm/npm to take priority over the WSL installation. You can identify this issue by:

- Running `which npm` and `which node` - if they point to Windows paths (starting with `/mnt/c/`), Windows versions are being used
- Experiencing broken functionality after switching Node versions with nvm in WSL

To resolve this issue, fix your Linux PATH to ensure the Linux node/npm versions take priority: **Primary solution: Ensure nvm is properly loaded in your shell** The most common cause is that nvm isn’t loaded in non-interactive shells. Add the following to your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.):

Report incorrect code

Copy


``` shiki
# Load nvm if it exists
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

Or run directly in your current session:

Report incorrect code

Copy


``` shiki
source ~/.nvm/nvm.sh
```

**Alternative: Adjust PATH order** If nvm is properly loaded but Windows paths still take priority, you can explicitly prepend your Linux paths to PATH in your shell configuration:

Report incorrect code

Copy


``` shiki
export PATH="$HOME/.nvm/versions/node/$(node -v)/bin:$PATH"
```

Avoid disabling Windows PATH importing via `appendWindowsPath = false` as this breaks the ability to call Windows executables from WSL. Similarly, avoid uninstalling Node.js from Windows if you use it for Windows development.

### 

[​](#wsl2-sandbox-setup)

WSL2 sandbox setup

[Sandboxing](/docs/en/sandboxing) is supported on WSL2 but requires installing additional packages. If you see an error like “Sandbox requires socat and bubblewrap” when running `/sandbox`, install the dependencies:

- Ubuntu/Debian

- Fedora

Report incorrect code

Copy


``` shiki
sudo apt-get install bubblewrap socat
```

Report incorrect code

Copy


``` shiki
sudo dnf install bubblewrap socat
```

WSL1 does not support sandboxing. If you see “Sandboxing requires WSL2”, you need to upgrade to WSL2 or run Claude Code without sandboxing.

### 

[​](#permission-errors-during-installation)

Permission errors during installation

If the native installer fails with permission errors, the target directory may not be writable. See [Check directory permissions](#check-directory-permissions). If you previously installed with npm and are hitting npm-specific permission errors, switch to the native installer:

Report incorrect code

Copy


``` shiki
curl -fsSL https://claude.ai/install.sh | bash
```

## 

[​](#permissions-and-authentication)

Permissions and authentication

These sections address login failures, token issues, and permission prompt behavior.

### 

[​](#repeated-permission-prompts)

Repeated permission prompts

If you find yourself repeatedly approving the same commands, you can allow specific tools to run without approval using the `/permissions` command. See [Permissions docs](/docs/en/permissions#manage-permissions).

### 

[​](#authentication-issues)

Authentication issues

If you’re experiencing authentication problems:

1.  Run `/logout` to sign out completely
2.  Close Claude Code
3.  Restart with `claude` and complete the authentication process again

If the browser doesn’t open automatically during login, press `c` to copy the OAuth URL to your clipboard, then paste it into your browser manually.

### 

[​](#oauth-error-invalid-code)

OAuth error: Invalid code

If you see `OAuth error: Invalid code. Please make sure the full code was copied`, the login code expired or was truncated during copy-paste. **Solutions:**

- Press Enter to retry and complete the login quickly after the browser opens
- Type `c` to copy the full URL if the browser doesn’t open automatically
- If using a remote/SSH session, the browser may open on the wrong machine. Copy the URL displayed in the terminal and open it in your local browser instead.

### 

[​](#403-forbidden-after-login)

403 Forbidden after login

If you see `API Error: 403 {"error":{"type":"forbidden","message":"Request not allowed"}}` after logging in:

- **Claude Pro/Max users**: verify your subscription is active at [claude.ai/settings](https://claude.ai/settings)
- **Console users**: confirm your account has the “Claude Code” or “Developer” role assigned by your admin
- **Behind a proxy**: corporate proxies can interfere with API requests. See [network configuration](/docs/en/network-config) for proxy setup.

### 

[​](#oauth-login-fails-in-wsl2)

OAuth login fails in WSL2

Browser-based login in WSL2 may fail if WSL can’t open your Windows browser. Set the `BROWSER` environment variable:

Report incorrect code

Copy


``` shiki
export BROWSER="/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
claude
```

Or copy the URL manually: when the login prompt appears, press `c` to copy the OAuth URL, then paste it into your Windows browser.

### 

[​](#”not-logged-in”-or-token-expired)

”Not logged in” or token expired

If Claude Code prompts you to log in again after a session, your OAuth token may have expired. Run `/login` to re-authenticate. If this happens frequently, check that your system clock is accurate, as token validation depends on correct timestamps.

## 

[​](#configuration-file-locations)

Configuration file locations

Claude Code stores configuration in several locations:

| File | Purpose |
|:---|:---|
| `~/.claude/settings.json` | User settings (permissions, hooks, model overrides) |
| `.claude/settings.json` | Project settings (checked into source control) |
| `.claude/settings.local.json` | Local project settings (not committed) |
| `~/.claude.json` | Global state (theme, OAuth, MCP servers) |
| `.mcp.json` | Project MCP servers (checked into source control) |
| `managed-mcp.json` | [Managed MCP servers](/docs/en/mcp#managed-mcp-configuration) |
| Managed settings | [Managed settings](/docs/en/settings#settings-files) (server-managed, MDM/OS-level policies, or file-based) |

On Windows, `~` refers to your user home directory, such as `C:\Users\YourName`. For details on configuring these files, see [Settings](/docs/en/settings) and [MCP](/docs/en/mcp).

### 

[​](#resetting-configuration)

Resetting configuration

To reset Claude Code to default settings, you can remove the configuration files:

Report incorrect code

Copy


``` shiki
# Reset all user settings and state
rm ~/.claude.json
rm -rf ~/.claude/

# Reset project-specific settings
rm -rf .claude/
rm .mcp.json
```

This will remove all your settings, MCP server configurations, and session history.

## 

[​](#performance-and-stability)

Performance and stability

These sections cover issues related to resource usage, responsiveness, and search behavior.

### 

[​](#high-cpu-or-memory-usage)

High CPU or memory usage

Claude Code is designed to work with most development environments, but may consume significant resources when processing large codebases. If you’re experiencing performance issues:

1.  Use `/compact` regularly to reduce context size
2.  Close and restart Claude Code between major tasks
3.  Consider adding large build directories to your `.gitignore` file

### 

[​](#command-hangs-or-freezes)

Command hangs or freezes

If Claude Code seems unresponsive:

1.  Press Ctrl+C to attempt to cancel the current operation
2.  If unresponsive, you may need to close the terminal and restart

### 

[​](#search-and-discovery-issues)

Search and discovery issues

If Search tool, `@file` mentions, custom agents, and custom skills aren’t working, install system `ripgrep`:

Report incorrect code

Copy


``` shiki
# macOS (Homebrew)  
brew install ripgrep

# Windows (winget)
winget install BurntSushi.ripgrep.MSVC

# Ubuntu/Debian
sudo apt install ripgrep

# Alpine Linux
apk add ripgrep

# Arch Linux
pacman -S ripgrep
```

Then set `USE_BUILTIN_RIPGREP=0` in your [environment](/docs/en/settings#environment-variables).

### 

[​](#slow-or-incomplete-search-results-on-wsl)

Slow or incomplete search results on WSL

Disk read performance penalties when [working across file systems on WSL](https://learn.microsoft.com/en-us/windows/wsl/filesystems) may result in fewer-than-expected matches when using Claude Code on WSL. Search still functions, but returns fewer results than on a native filesystem.

`/doctor` will show Search as OK in this case.

**Solutions:**

1.  **Submit more specific searches**: reduce the number of files searched by specifying directories or file types: “Search for JWT validation logic in the auth-service package” or “Find use of md5 hash in JS files”.
2.  **Move project to Linux filesystem**: if possible, ensure your project is located on the Linux filesystem (`/home/`) rather than the Windows filesystem (`/mnt/c/`).
3.  **Use native Windows instead**: consider running Claude Code natively on Windows instead of through WSL, for better file system performance.

## 

[​](#ide-integration-issues)

IDE integration issues

If Claude Code does not connect to your IDE or behaves unexpectedly within an IDE terminal, try the solutions below.

### 

[​](#jetbrains-ide-not-detected-on-wsl2)

JetBrains IDE not detected on WSL2

If you’re using Claude Code on WSL2 with JetBrains IDEs and getting “No available IDEs detected” errors, this is likely due to WSL2’s networking configuration or Windows Firewall blocking the connection.

#### 

[​](#wsl2-networking-modes)

WSL2 networking modes

WSL2 uses NAT networking by default, which can prevent IDE detection. You have two options: **Option 1: Configure Windows Firewall** (recommended)

1.  Find your WSL2 IP address:
    Report incorrect code

    Copy


    ``` shiki
    wsl hostname -I
    # Example output: 172.21.123.45
    ```
2.  Open PowerShell as Administrator and create a firewall rule:
    Report incorrect code

    Copy


    ``` shiki
    New-NetFirewallRule -DisplayName "Allow WSL2 Internal Traffic" -Direction Inbound -Protocol TCP -Action Allow -RemoteAddress 172.21.0.0/16 -LocalAddress 172.21.0.0/16
    ```

    Adjust the IP range based on your WSL2 subnet from step 1.
3.  Restart both your IDE and Claude Code

**Option 2: Switch to mirrored networking** Add to `.wslconfig` in your Windows user directory:

Report incorrect code

Copy


``` shiki
[wsl2]
networkingMode=mirrored
```

Then restart WSL with `wsl --shutdown` from PowerShell.

These networking issues only affect WSL2. WSL1 uses the host’s network directly and doesn’t require these configurations.

For additional JetBrains configuration tips, see the [JetBrains IDE guide](/docs/en/jetbrains#plugin-settings).

### 

[​](#report-windows-ide-integration-issues)

Report Windows IDE integration issues

If you’re experiencing IDE integration problems on Windows, [create an issue](https://github.com/anthropics/claude-code/issues) with the following information:

- Environment type: native Windows (Git Bash) or WSL1/WSL2
- WSL networking mode, if applicable: NAT or mirrored
- IDE name and version
- Claude Code extension/plugin version
- Shell type: Bash, Zsh, PowerShell, etc.

### 

[​](#escape-key-not-working-in-jetbrains-ide-terminals)

Escape key not working in JetBrains IDE terminals

If you’re using Claude Code in JetBrains terminals and the `Esc` key doesn’t interrupt the agent as expected, this is likely due to a keybinding clash with JetBrains’ default shortcuts. To fix this issue:

1.  Go to Settings → Tools → Terminal
2.  Either:
    - Uncheck “Move focus to the editor with Escape”, or
    - Click “Configure terminal keybindings” and delete the “Switch focus to Editor” shortcut
3.  Apply the changes

This allows the `Esc` key to properly interrupt Claude Code operations.

## 

[​](#markdown-formatting-issues)

Markdown formatting issues

Claude Code sometimes generates markdown files with missing language tags on code fences, which can affect syntax highlighting and readability in GitHub, editors, and documentation tools.

### 

[​](#missing-language-tags-in-code-blocks)

Missing language tags in code blocks

If you notice code blocks like this in generated markdown:

Report incorrect code

Copy


```` shiki
```
function example() {
  return "hello";
}
```text
````

Instead of properly tagged blocks like:

Report incorrect code

Copy


``` shiki
```javascript
function example() {
  return "hello";
}
```text
```

**Solutions:**

1.  **Ask Claude to add language tags**: request “Add appropriate language tags to all code blocks in this markdown file.”
2.  **Use post-processing hooks**: set up automatic formatting hooks to detect and add missing language tags. See [Auto-format code after edits](/docs/en/hooks-guide#auto-format-code-after-edits) for an example of a PostToolUse formatting hook.
3.  **Manual verification**: after generating markdown files, review them for proper code block formatting and request corrections if needed.

### 

[​](#inconsistent-spacing-and-formatting)

Inconsistent spacing and formatting

If generated markdown has excessive blank lines or inconsistent spacing: **Solutions:**

1.  **Request formatting corrections**: ask Claude to “Fix spacing and formatting issues in this markdown file.”
2.  **Use formatting tools**: set up hooks to run markdown formatters like `prettier` or custom formatting scripts on generated markdown files.
3.  **Specify formatting preferences**: include formatting requirements in your prompts or project [memory](/docs/en/memory) files.

### 

[​](#reduce-markdown-formatting-issues)

Reduce markdown formatting issues

To minimize formatting issues:

- **Be explicit in requests**: ask for “properly formatted markdown with language-tagged code blocks”
- **Use project conventions**: document your preferred markdown style in [`CLAUDE.md`](/docs/en/memory)
- **Set up validation hooks**: use post-processing hooks to automatically verify and fix common formatting issues

## 

[​](#get-more-help)

Get more help

If you’re experiencing issues not covered here:

1.  Use the `/bug` command within Claude Code to report problems directly to Anthropic
2.  Check the [GitHub repository](https://github.com/anthropics/claude-code) for known issues
3.  Run `/doctor` to diagnose issues. It checks:
    - Installation type, version, and search functionality
    - Auto-update status and available versions
    - Invalid settings files (malformed JSON, incorrect types)
    - MCP server configuration errors
    - Keybinding configuration problems
    - Context usage warnings (large CLAUDE.md files, high MCP token usage, unreachable permission rules)
    - Plugin and agent loading errors
4.  Ask Claude directly about its capabilities and features - Claude has built-in access to its documentation
