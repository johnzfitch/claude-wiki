---
title: "Troubleshoot installation and login - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/troubleshoot-install"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-30T06:30:43Z"
tags: ["claude-code"]
---

## On this page

- [Find your error](#find-your-error)
- [Run diagnostic checks](#run-diagnostic-checks)
  - [Check network connectivity](#check-network-connectivity)
  - [Verify your PATH](#verify-your-path)
  - [Check for conflicting installations](#check-for-conflicting-installations)
  - [Check directory permissions](#check-directory-permissions)
  - [Verify the binary works](#verify-the-binary-works)
- [Common installation issues](#common-installation-issues)
  - [Install script returns HTML instead of a shell script](#install-script-returns-html-instead-of-a-shell-script)
  - [command not found: claude after installation](#command-not-found-claude-after-installation)
  - [curl: (56) Failure writing output to destination](#curl-56-failure-writing-output-to-destination)
  - [Homebrew cask unavailable or outdated](#homebrew-cask-unavailable-or-outdated)
  - [TLS or SSL connection errors](#tls-or-ssl-connection-errors)
  - [Failed to fetch version from downloads.claude.ai](#failed-to-fetch-version-from-downloads-claude-ai)
  - [Wrong install command on Windows](#wrong-install-command-on-windows)
  - [running scripts is disabled on this system](#running-scripts-is-disabled-on-this-system)
  - [The process cannot access the file during Windows install](#the-process-cannot-access-the-file-during-windows-install)
  - [claude.exe missing after an update on Windows](#claude-exe-missing-after-an-update-on-windows)
  - [Install killed on low-memory Linux servers](#install-killed-on-low-memory-linux-servers)
  - [Install hangs in Docker](#install-hangs-in-docker)
  - [Raw mode is not supported during install](#raw-mode-is-not-supported-during-install)
  - [claude update or claude doctor hangs](#claude-update-or-claude-doctor-hangs)
  - [Claude Desktop overrides the claude command on Windows](#claude-desktop-overrides-the-claude-command-on-windows)
  - [Claude Code on Windows requires either Git for Windows (for bash) or PowerShell](#claude-code-on-windows-requires-either-git-for-windows-for-bash-or-powershell)
  - [Claude Code does not support 32-bit Windows](#claude-code-does-not-support-32-bit-windows)
  - [Linux musl or glibc binary mismatch](#linux-musl-or-glibc-binary-mismatch)
  - [Illegal instruction](#illegal-instruction)
  - [dyld: cannot load on macOS](#dyld-cannot-load-on-macos)
  - [Exec format error on WSL1](#exec-format-error-on-wsl1)
  - [npm install errors in WSL](#npm-install-errors-in-wsl)
  - [Permission errors during installation](#permission-errors-during-installation)
  - [Native binary not found after npm install](#native-binary-not-found-after-npm-install)
  - [npm ENOTEMPTY error during update or reinstall](#npm-enotempty-during-update-or-reinstall)
- [Login and authentication](#login-and-authentication)
  - [Reset your login](#reset-your-login)
  - [OAuth error: Invalid code](#oauth-error-invalid-code)
  - [403 Forbidden after login](#403-forbidden-after-login)
  - [Claude Code access has not been granted for this account](#claude-code-access-has-not-been-granted-for-this-account)
  - [This organization has been disabled with an active subscription](#this-organization-has-been-disabled-with-an-active-subscription)
  - [OAuth login fails in WSL2, SSH, or containers](#oauth-login-fails-in-wsl2-ssh-or-containers)
  - [Not logged in or token expired](#not-logged-in-or-token-expired)
  - [Bedrock, Agent Platform, or Foundry credentials not loading](#bedrock-agent-platform-or-foundry-credentials-not-loading)
- [Still stuck](#still-stuck)

Troubleshooting

# Troubleshoot installation and login

Copy pageCopy page

Fix command not found, PATH, permission, network, and authentication errors when installing or signing in to Claude Code.

Copy pageCopy page

If installation fails or you can’t sign in, find your error below. For runtime issues after Claude Code is working, see [Troubleshooting](troubleshooting.md). For configuration problems such as settings not applying or hooks not firing, see [Debug your configuration](debug-your-config.md).


[​](#find-your-error)

Find your error

Match the error message or symptom you’re seeing to a fix:

| What you see                                                                                               | Solution                                                                                                                                      |
|:-----------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| `command not found: claude` or `'claude' is not recognized`                                                | [Fix your PATH](#command-not-found-claude-after-installation)                                                                                 |
| `syntax error near unexpected token '<'`                                                                   | [Install script returns HTML](#install-script-returns-html-instead-of-a-shell-script)                                                         |
| `curl: (22) The requested URL returned error: 403`                                                         | [Install script returned 403](#install-script-returns-html-instead-of-a-shell-script)                                                         |
| `curl: (23)` or `curl: (56) Failure writing output to destination`                                         | [Check connectivity or use an alternative installer](#curl-56-failure-writing-output-to-destination)                                          |
| `Killed` during install on Linux, or `Installation was killed before it could finish (exit code 137)`      | [Free memory or add swap space](#install-killed-on-low-memory-linux-servers)                                                                  |
| `Raw mode is not supported` during install                                                                 | [Rerun the installer](#raw-mode-is-not-supported-during-install)                                                                              |
| `TLS connect error` or `SSL/TLS secure channel`                                                            | [Update CA certificates](#tls-or-ssl-connection-errors)                                                                                       |
| `Failed to fetch version` or can’t reach download server                                                   | [Check network and proxy settings](#check-network-connectivity)                                                                               |
| `irm is not recognized` or `The token '&&' is not a valid statement separator`                             | [Use the right command for your shell](#wrong-install-command-on-windows)                                                                     |
| `Cask 'claude-code' is unavailable: No Cask with this name exists`                                         | [Update Homebrew](#homebrew-cask-unavailable-or-outdated)                                                                                     |
| `'bash' is not recognized as the name of a cmdlet`                                                         | [Use the Windows installer command](#wrong-install-command-on-windows)                                                                        |
| `A parameter cannot be found that matches parameter name 'fsSL'`                                           | [Use the Windows installer command](#wrong-install-command-on-windows)                                                                        |
| `Claude Code on Windows requires either Git for Windows (for bash) or PowerShell`                          | [Install a shell](#claude-code-on-windows-requires-either-git-for-windows-for-bash-or-powershell)                                             |
| `Claude Code does not support 32-bit Windows`                                                              | [Open Windows PowerShell, not the x86 entry](#claude-code-does-not-support-32-bit-windows)                                                    |
| `The process cannot access the file ... because it is being used by another process`                       | [Clear the downloads folder and retry](#the-process-cannot-access-the-file-during-windows-install)                                            |
| `Error loading shared library`                                                                             | [Wrong binary variant for your system](#linux-musl-or-glibc-binary-mismatch)                                                                  |
| `Illegal instruction`                                                                                      | [Architecture or CPU instruction set mismatch](#illegal-instruction)                                                                          |
| `cannot execute binary file: Exec format error` in WSL                                                     | [WSL1 native-binary regression](#exec-format-error-on-wsl1)                                                                                   |
| PowerShell installer completes but `claude` is not found or shows an old version                           | [Add the install directory to your PATH](#verify-your-path), then open a new terminal                                                         |
| `dyld: Symbol not found`, `dyld: cannot load`, or `Abort trap` on macOS                                    | [Binary incompatibility](#dyld-cannot-load-on-macos)                                                                                          |
| `claude update` hangs after `Checking for updates`, or `claude doctor` hangs with no output                | [Move the directory at a shell config path](#claude-update-or-claude-doctor-hangs)                                                            |
| `Invoke-Expression` or `iex` parse errors quoting HTML tags or CSS, or `ParserError` with `ParseException` | [Install script returns HTML](#install-script-returns-html-instead-of-a-shell-script)                                                         |
| `running scripts is disabled on this system` or `PSSecurityException`                                      | [Allow the npm shims to run](#running-scripts-is-disabled-on-this-system)                                                                     |
| `Error: claude native binary not installed`                                                                | [Complete the npm install](#native-binary-not-found-after-npm-install)                                                                        |
| `npm error code ENOTEMPTY` during update or reinstall                                                      | [Remove the leftover package directory](#npm-enotempty-during-update-or-reinstall)                                                            |
| `'claude' is not recognized` right after an update on Windows                                              | [Restore `claude.exe` from its backup](#claude-exe-missing-after-an-update-on-windows)                                                        |
| On Windows, the install command prints script text and nothing installs                                    | [Run the complete install command](#wrong-install-command-on-windows)                                                                         |
| `App unavailable in region`                                                                                | Claude Code is not available in your country. See [supported countries](https://www.anthropic.com/supported-countries).                       |
| `unable to get local issuer certificate`                                                                   | [Configure corporate CA certificates](#tls-or-ssl-connection-errors)                                                                          |
| `OAuth error` or `403 Forbidden`                                                                           | [Fix authentication](#login-and-authentication)                                                                                               |
| `Claude Code access has not been granted for this account`                                                 | [Get a role that includes Claude Code](#claude-code-access-has-not-been-granted-for-this-account)                                             |
| `Unable to connect to Anthropic services` during setup                                                     | See [Unable to connect to Anthropic services](errors.md#unable-to-connect-to-anthropic-services) in the Error reference                 |
| `Could not load the default credentials` or `Could not load credentials from any providers`                | [Amazon Bedrock, Google Cloud’s Agent Platform, or Microsoft Foundry credentials](#bedrock-agent-platform-or-foundry-credentials-not-loading) |
| `ChainedTokenCredential authentication failed` or `CredentialUnavailableError`                             | [Amazon Bedrock, Google Cloud’s Agent Platform, or Microsoft Foundry credentials](#bedrock-agent-platform-or-foundry-credentials-not-loading) |
| `API Error: 500`, `529 Overloaded`, `429`, or other 4xx and 5xx errors not listed above                    | See the [Error reference](errors.md)                                                                                                    |

If your issue isn’t listed, work through the diagnostic checks below to narrow down the cause.

If you’d rather skip the terminal entirely, the [Claude Code Desktop app](../16-Mobile-Desktop/desktop-quickstart.md) lets you install and use Claude Code through a graphical interface. Download it for [macOS](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect?utm_source=claude_code&utm_medium=docs) or [Windows](https://claude.com/download?utm_source=claude_code&utm_medium=docs) and start coding without any command-line setup. On Linux, install the app with apt by following the [Linux install instructions](../16-Mobile-Desktop/desktop-linux.md).


[​](#run-diagnostic-checks)

Run diagnostic checks


[​](#check-network-connectivity)

Check network connectivity

The installer downloads from `downloads.claude.ai`. Verify you can reach it:

- macOS/Linux

- Windows PowerShell

```python
curl -sI https://downloads.claude.ai/claude-code-releases/latest
```

```python
curl.exe -sI https://downloads.claude.ai/claude-code-releases/latest
```

PowerShell aliases `curl` to `Invoke-WebRequest`, which rejects the `-sI` flags, so call `curl.exe` explicitly.

You reached the server if the first line shows a `200` status. You see `HTTP/2 200` on macOS and Linux, and `HTTP/1.1 200 OK` from the `curl.exe` included with Windows. Other results point to the cause:

- `403`: usually a proxy or network filter blocking the host, or Claude Code is [not available in your region](https://www.anthropic.com/supported-countries)
- `5xx`: usually a temporary service issue; wait a few minutes and retry

If you see no output, `Could not resolve host`, or a connection timeout, your network is blocking the connection. Common causes:

- Corporate firewalls or proxies blocking `downloads.claude.ai`
- Regional network restrictions: try a VPN or alternative network
- TLS/SSL issues: update your system’s CA certificates, or check if `HTTPS_PROXY` is configured

If you’re behind a corporate proxy, set `HTTPS_PROXY` and `HTTP_PROXY` to your proxy’s address before installing. Ask your IT team for the proxy URL if you don’t know it, or check your browser’s proxy settings. This example sets both proxy variables, then runs the installer through your proxy:

- macOS/Linux

- Windows PowerShell

```python
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080
curl -fsSL https://claude.ai/install.sh | bash
```

```python
$env:HTTP_PROXY = 'http://proxy.example.com:8080'
$env:HTTPS_PROXY = 'http://proxy.example.com:8080'
irm https://claude.ai/install.ps1 | iex
```


[​](#verify-your-path)

Verify your PATH

If installation succeeded but you get a `command not found` or `not recognized` error when running `claude`, the install directory isn’t in your PATH. Your shell searches for programs in directories listed in PATH, and the installer places `claude` at `~/.local/bin/claude` on macOS/Linux or `%USERPROFILE%\.local\bin\claude.exe` on Windows.

The [VS Code extension](../03-IDE-Integrations/vs-code.md) does not place `claude` at this location. It bundles a private copy of the CLI inside the extension directory for its own chat panel and does not add it to PATH. If you have only installed the extension, `~/.local/bin/claude` will not exist. Run the [standalone install](../01-Getting-Started/setup.md) to use `claude` from a terminal, then continue below.

Check if the install directory is in your PATH by listing your PATH entries and filtering for `local/bin`:

- macOS/Linux

- Windows PowerShell

- Windows CMD

```python
echo $PATH | tr ':' '\n' | grep -Fx "$HOME/.local/bin"
```

If this prints `/Users/you/.local/bin` or `/home/you/.local/bin`, the directory is in your PATH and you can skip to [Check for conflicting installations](#check-for-conflicting-installations). If there’s no output, add it to your shell configuration.For Zsh, the default on macOS:

```python
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

For Bash on Linux, where it’s the default on most distributions:

```python
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

For Bash on macOS, add the line to `~/.bash_profile` instead. Terminal on macOS starts Bash as a login shell, which ignores `~/.bashrc` and reads only the first of `~/.bash_profile`, `~/.bash_login`, or `~/.profile` that exists. If you already have a `~/.bash_login` or `~/.profile` and no `~/.bash_profile`, put the line in that file rather than creating `~/.bash_profile`:

```python
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
```

Alternatively, close and reopen your terminal.For other shells such as fish or Nushell, add `~/.local/bin` to your PATH using your shell’s own configuration syntax, then restart your terminal.Verify the fix worked:

```python
claude --version
```

```python
$env:PATH -split ';' | Select-String '\.local\\bin'
```

If there’s no output, add the install directory to your User PATH:

```python
$currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
[Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')
```

Restart your terminal for the change to take effect.Verify the fix worked:

```python
claude --version
```

```python
echo %PATH% | findstr /i "local\bin"
```

If there’s no output, open System Settings, go to Environment Variables, and add `%USERPROFILE%\.local\bin` to your User PATH variable. Restart your terminal.Verify the fix worked:

```python
claude --version
```


[​](#check-for-conflicting-installations)

Check for conflicting installations

Multiple Claude Code installations can cause version mismatches or unexpected behavior. Check what’s installed:

- macOS/Linux

- Windows PowerShell

List all `claude` binaries found in your PATH:

```python
which -a claude
```

If this prints nothing, no `claude` is on your PATH yet. Go back to [Verify your PATH](#verify-your-path).Check the three locations a `claude` binary can come from. `~/.local/bin/claude` is the native installer, `~/.claude/local/` is a legacy local npm install created by older versions of Claude Code, and the npm global list shows a `-g` install:

```python
ls -la ~/.local/bin/claude
```

A native install shows a symlink into `~/.local/share/claude/versions/`. A script or a symlink you created yourself at this path is a custom launcher, which [auto-update leaves in place](../01-Getting-Started/setup.md#auto-updates).If either `ls` command prints `No such file or directory`, that’s not an error. It means nothing is installed at that location, so move on to the next check.

```python
ls -la ~/.claude/local/
```

```python
npm -g ls @anthropic-ai/claude-code 2>/dev/null
```

List all `claude` binaries found in your PATH:

```python
where.exe claude
```

Check whether the native installer placed a binary:

```python
Test-Path "$env:USERPROFILE\.local\bin\claude.exe"
```

If you find multiple installations, keep only one. The native install at `~/.local/bin/claude` on macOS/Linux or `%USERPROFILE%\.local\bin\claude.exe` on Windows is recommended. Remove the extras: Uninstall an npm global install:

```python
npm uninstall -g @anthropic-ai/claude-code
```

Remove the legacy local npm install:

- macOS/Linux

- Windows PowerShell

```python
rm -rf ~/.claude/local
```

```python
Remove-Item -Recurse -Force "$env:USERPROFILE\.claude\local"
```

Remove a Homebrew install on macOS. If you installed the `claude-code@latest` cask, substitute that name:

```python
brew uninstall --cask claude-code
```

Remove a WinGet install on Windows:

```python
winget uninstall Anthropic.ClaudeCode
```


[​](#check-directory-permissions)

Check directory permissions

The installer needs write access to `~/.local/bin/` and `~/.claude/` on macOS and Linux. On Windows the install location is under `%USERPROFILE%`, which is writable by your user by default, so this section rarely applies there. Check whether the directories are writable:

```python
test -w ~/.local/bin && echo "writable" || echo "not writable"
test -w ~/.claude && echo "writable" || echo "not writable"
```

If either directory isn’t writable, create the install directory and set your user as the owner:

```python
sudo mkdir -p ~/.local/bin
sudo chown -R $(whoami) ~/.local
```


[​](#verify-the-binary-works)

Verify the binary works

If `claude --version` prints a version but `claude` crashes or hangs on startup, run these checks to narrow down the cause. If `claude --version` says command not found, go to [Verify your PATH](#verify-your-path) first; the commands below assume `claude` is on your PATH. Confirm the binary exists and is executable:

- macOS/Linux

- Windows PowerShell

```python
ls -la "$(command -v claude)"
```

```python
Get-Command claude | Select-Object Source
```

On Linux, check for missing shared libraries. If `ldd` shows missing libraries, you may need to install system packages. On Alpine Linux and other musl-based distributions, see [Alpine Linux setup](../01-Getting-Started/setup.md#alpine-linux-and-musl-based-distributions).

```python
ldd "$(command -v claude)" | grep "not found"
```

Confirm the binary can execute:

```python
claude --version
```


[​](#common-installation-issues)

Common installation issues

These are the most frequently encountered installation problems and their solutions.


[​](#install-script-returns-html-instead-of-a-shell-script)

Install script returns HTML instead of a shell script

When running the install command, you may see one of these errors:

```python
bash: line 1: syntax error near unexpected token `<'
bash: line 1: `<!DOCTYPE html>'
```

On PowerShell, the same problem appears as parse errors pointing into the returned page, with `iex` trying to run HTML and CSS as PowerShell:

```python
iex : At line:1 char:2310
+ ... igin="anonymous"/><script type="text/javascript">!function(o,c){var n ...
Missing argument in parameter list.
...
```

The wording varies with the PowerShell version and system language: you may see `Missing expression after unary operator '--'` or a `ParserError` with `ParseException` instead. HTML tags or CSS in the quoted text identify this failure. If you download with `-OutFile install.ps1` instead, the saved file is the same web page, so that doesn’t help either. Depending on how the request was routed, you may instead see a 403 with no HTML body:

```python
curl: (22) The requested URL returned error: 403
```

These all mean the install URL returned an HTML page or an error status instead of the install script. If the HTML page says “App unavailable in region,” Claude Code is not available in your country. See [supported countries](https://www.anthropic.com/supported-countries). A bare 403 with no body often has the same cause, but it can also come from a corporate proxy or firewall blocking the download. If you are in a supported country and still see the 403, work through [Check network connectivity](#check-network-connectivity) before trying the alternative installers below, since those reach the same hosts. Otherwise, this can happen due to network issues, regional routing, or a temporary service disruption. **Solutions:**

1.  **Use an alternative install method**: On macOS, install via Homebrew:

    ``` shiki
    brew install --cask claude-code
    ```

    On Windows, install via WinGet:

    ``` shiki
    winget install Anthropic.ClaudeCode
    ```

    Then run `claude --version` to confirm: the command prints a version number such as `2.1.211 (Claude Code)`. If the shell reports `claude` isn’t found, open a new terminal window and retry: the session you installed from keeps its old `PATH`.
2.  **Retry after a few minutes**: the issue is often temporary. Wait and try the original command again.


[​](#command-not-found-claude-after-installation)

`command not found: claude` after installation

The install finished but `claude` doesn’t work. The exact error varies by platform:

| Platform    | Error message                                                          |
|:------------|:-----------------------------------------------------------------------|
| macOS       | `zsh: command not found: claude`                                       |
| Linux       | `bash: claude: command not found`                                      |
| Windows CMD | `'claude' is not recognized as an internal or external command`        |
| PowerShell  | `claude : The term 'claude' is not recognized as the name of a cmdlet` |

This means the install directory isn’t in your shell’s search path. See [Verify your PATH](#verify-your-path) for the fix on each platform.


[​](#curl-56-failure-writing-output-to-destination)

`curl: (56) Failure writing output to destination`

The `curl ... | bash` command downloads the script and pipes it to Bash for execution. This error, and the related `curl: (23) Failure writing output to destination`, means Bash did not receive the complete script. Exit code 56 indicates the download itself was interrupted, and exit code 23 indicates curl could not write what it received to the pipe, usually because Bash exited early. Test that you can reach `downloads.claude.ai` with the check in [Check network connectivity](#check-network-connectivity). If you reached the server, the original failure was likely intermittent; retry the install command. You can also [try an alternative install method](../01-Getting-Started/setup.md#install-claude-code).


[​](#homebrew-cask-unavailable-or-outdated)

Homebrew cask unavailable or outdated

Homebrew reports `Error: Cask 'claude-code' is unavailable: No Cask with this name exists` when your local copy of the Homebrew cask index predates the cask’s publication. Refresh the index and retry:

```python
brew update
brew install --cask claude-code
```

If Homebrew installs an older Claude Code version than you expect, the same stale index is usually the cause. The `claude-code` cask tracks the stable channel and is typically about one week behind the latest release; for the newest version run `brew install --cask claude-code@latest` instead. See [Configure release channel](../01-Getting-Started/setup.md#configure-release-channel) for the difference between the two casks.


[​](#tls-or-ssl-connection-errors)

TLS or SSL connection errors

Errors such as these mean the TLS handshake failed:

- `curl: (35) TLS connect error`
- `schannel: next InitializeSecurityContext failed`
- PowerShell’s `Could not create SSL/TLS secure channel`
- PowerShell’s `Could not establish trust relationship for the SSL/TLS secure channel`

**Solutions:**

1.  **Update your system CA certificates**: On Ubuntu/Debian:

    ``` shiki
    sudo apt-get update && sudo apt-get install ca-certificates
    ```

    On macOS, the system curl uses the Keychain trust store; updating macOS itself updates the root certificates.
2.  **On Windows, enable TLS 1.2** in PowerShell before running the installer:

    ``` shiki
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    irm https://claude.ai/install.ps1 | iex
    ```
3.  **Check for proxy or firewall interference**: corporate proxies that perform TLS inspection can cause these errors, including `unable to get local issuer certificate` and `SELF_SIGNED_CERT_IN_CHAIN`. For the install step, make the install download trust your corporate proxy’s CA:
    - macOS/Linux

    - Windows PowerShell

    ``` shiki
    curl --cacert /path/to/corporate-ca.pem -fsSL https://claude.ai/install.sh | bash
    ```

    The PowerShell installer downloads through .NET, which validates TLS against the Windows certificate store. Ask your IT team to add the proxy’s CA certificate to the Windows store if it isn’t already there, then run the installer:

    ``` shiki
    irm https://claude.ai/install.ps1 | iex
    ```

    For Claude Code itself once installed, set `NODE_EXTRA_CA_CERTS` so API requests trust the same bundle:
    - macOS/Linux

    - Windows PowerShell

    ``` shiki
    export NODE_EXTRA_CA_CERTS=/path/to/corporate-ca.pem
    ```

    ``` shiki
    $env:NODE_EXTRA_CA_CERTS = 'C:\path\to\corporate-ca.pem'
    ```

    Ask your IT team for the certificate file if you don’t have it. You can also try on a direct connection to confirm the proxy is the cause.
4.  **On Windows, work around blocked revocation checks**. The errors `CRYPT_E_NO_REVOCATION_CHECK (0x80092012)` and `CRYPT_E_REVOCATION_OFFLINE (0x80092013)` mean curl reached the server but your network blocks the certificate revocation lookup, which is common behind corporate firewalls. If the failing command is the `curl` that downloads `install.cmd`, rerun it from a Command Prompt with `--ssl-revoke-best-effort` added:

    ``` shiki
    curl --ssl-revoke-best-effort -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
    ```

    When the script’s own downloads hit the same errors, it retries them with best-effort revocation checking automatically, so the flag is only needed on the command you run yourself. Best-effort checking tolerates an unreachable revocation server but still rejects a certificate that is known to be revoked, matching how browsers handle revocation. You can also avoid curl’s revocation check entirely by running the PowerShell installer from PowerShell, which downloads through .NET and doesn’t fail when the revocation server is unreachable:

    ``` shiki
    irm https://claude.ai/install.ps1 | iex
    ```

    You can also install with `winget install Anthropic.ClaudeCode`, which avoids curl entirely.


[​](#failed-to-fetch-version-from-downloads-claude-ai)

`Failed to fetch version from downloads.claude.ai`

The installer couldn’t reach the download server. This typically means `downloads.claude.ai` is blocked on your network. See [Check network connectivity](#check-network-connectivity).


[​](#wrong-install-command-on-windows)

Wrong install command on Windows

If you see `'irm' is not recognized`, `The token '&&' is not a valid statement separator`, `A parameter cannot be found that matches parameter name 'fsSL'`, or `'bash' is not recognized as the name of a cmdlet`, you copied the install command for a different shell or operating system. If the command prints the script’s text instead of installing anything, you ran only part of it.

- **`irm` not recognized**: you’re in CMD, not PowerShell. You have two options: Open PowerShell by searching for “PowerShell” in the Start menu, then run the original install command:

  ``` shiki
  irm https://claude.ai/install.ps1 | iex
  ```

  Or stay in CMD and use the CMD installer instead:

  ``` shiki
  curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
  ```
- **`&&` not a valid statement separator**: you’re in PowerShell but ran the CMD installer command. Use the PowerShell installer:

  ``` shiki
  irm https://claude.ai/install.ps1 | iex
  ```
- **`A parameter cannot be found that matches parameter name 'fsSL'`**: you ran the macOS/Linux `curl -fsSL ... | bash` installer in Windows PowerShell, where `curl` is an alias for `Invoke-WebRequest` and rejects the `-fsSL` flags. Use the PowerShell installer instead:

  ``` shiki
  irm https://claude.ai/install.ps1 | iex
  ```
- **`bash` not recognized**: you ran the macOS/Linux installer on Windows. Use the PowerShell installer instead:

  ``` shiki
  irm https://claude.ai/install.ps1 | iex
  ```
- **The command prints script text instead of installing**: you ran the download half of the command without the part that executes it. `irm https://claude.ai/install.ps1` on its own prints the downloaded script to the terminal. Pipe it to `iex` to run it:

  ``` shiki
  irm https://claude.ai/install.ps1 | iex
  ```

  In CMD, `curl -fsSL https://claude.ai/install.cmd` without `-o` prints the batch script instead of saving it. Run the complete command:

  ``` shiki
  curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
  ```

Whichever installer you use, confirm it worked: open a new terminal and run `claude --version`, which prints a version number such as `2.1.211 (Claude Code)`.


[​](#running-scripts-is-disabled-on-this-system)

`running scripts is disabled on this system`

Installing or running Claude Code through npm on Windows can fail with a `SecurityError`:

```python
npm : File C:\Program Files\nodejs\npm.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
...
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
```

The same error names `claude.ps1` when you run `claude` after an npm install. PowerShell’s execution policy is blocking the `.ps1` launcher scripts that npm creates for its commands. The policy applies to script files, so it doesn’t affect the PowerShell installer `irm https://claude.ai/install.ps1 | iex`, which runs the downloaded text directly. **Solutions:**

1.  **Allow locally created scripts for your user**, then retry:

    ``` shiki
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
2.  **Call the `.cmd` launcher instead**: `npm.cmd` and `claude.cmd` do the same job, and the policy doesn’t cover them.
3.  **Use the [PowerShell installer](../01-Getting-Started/setup.md#install-claude-code)** instead of npm. It installs a binary rather than a `.ps1` script.


[​](#the-process-cannot-access-the-file-during-windows-install)

`The process cannot access the file` during Windows install

If the PowerShell installer fails with `Failed to download binary: The process cannot access the file ... because it is being used by another process`, the installer couldn’t write to `%USERPROFILE%\.claude\downloads`. This usually means a previous install attempt is still running, or antivirus software is scanning a partially downloaded binary in that folder. Close any other PowerShell windows running the installer and wait for antivirus scans to release the file. Then delete the downloads folder and run the installer again:

```python
Remove-Item -Recurse -Force "$env:USERPROFILE\.claude\downloads"
irm https://claude.ai/install.ps1 | iex
```


[​](#claude-exe-missing-after-an-update-on-windows)

`claude.exe` missing after an update on Windows

If your terminal reports `'claude' is not recognized` right after Claude Code updated on Windows, check whether `%USERPROFILE%\.local\bin` still contains `claude.exe`. If that directory isn’t on your PATH at all, see [Fix your PATH](#command-not-found-claude-after-installation) instead. To update on Windows, Claude Code renames the existing `claude.exe` aside to a backup and moves the new version into its place. If moving the new version into place fails and Claude Code can’t rename the backup back either, the directory keeps the backup but has no `claude.exe`. The backup is a file in the same directory whose name begins with `claude.exe.old.` followed by a numeric timestamp. Run the following in PowerShell to rename the newest backup back to `claude.exe`:

```python
Get-ChildItem "$env:USERPROFILE\.local\bin\claude.exe.old.*" | Sort-Object Name | Select-Object -Last 1 | Rename-Item -NewName claude.exe
```

Then run `claude --version` to confirm the fix. A restored `claude.exe` prints a version number. If there’s no `claude.exe.old.*` file, or `claude` still fails after the rename, reinstall instead:

```python
irm https://claude.ai/install.ps1 | iex
```

Before v2.1.281, Claude Code could delete the backup while `claude.exe` was still missing.


[​](#install-killed-on-low-memory-linux-servers)

Install killed on low-memory Linux servers

A `Killed` message during install usually means the Linux out-of-memory (OOM) killer terminated the `claude install` step because the system ran out of free memory. This is common on small VPS and cloud instances. The install script reports the cause and exits with code 137. In this example, the line number and process ID vary by release and run:

```python
Setting up Claude Code...
bash: line 183: 34803 Killed    "$binary_path" install ${TARGET:+"$TARGET"}
Installation was killed before it could finish (exit code 137). This usually means the system ran out of memory.
Claude Code needs roughly 512MB of free memory to install. Free up memory, then run this script again.
```

Installing needs roughly 512 MB of free memory, and running Claude Code needs more. See the [system requirements](../01-Getting-Started/setup.md#system-requirements). **Solutions:**

1.  **Add swap space** if your server has limited RAM. Swap uses disk space as overflow memory, letting the install complete even with low physical RAM. Create a 2 GB swap file and enable it:

    ``` shiki
    sudo fallocate -l 2G /swapfile
    sudo chmod 600 /swapfile
    sudo mkswap /swapfile
    sudo swapon /swapfile
    ```

    Then retry the installation:

    ``` shiki
    curl -fsSL https://claude.ai/install.sh | bash
    ```
2.  **Close other processes** to free memory before installing.
3.  **Use a larger instance** if possible. Claude Code requires at least 4 GB of RAM.


[​](#install-hangs-in-docker)

Install hangs in Docker

When installing Claude Code in a Docker container, installing as root into `/` can cause hangs. **Solutions:**

1.  **Set a working directory** before running the installer. When run from `/`, the installer scans the entire filesystem, which causes excessive memory usage. Setting `WORKDIR` limits the scan to a small directory:

    ``` shiki
    WORKDIR /tmp
    RUN curl -fsSL https://claude.ai/install.sh | bash
    ```
2.  **Give Docker more memory** if using Docker Desktop. Build containers share the memory allocated to the Docker Desktop virtual machine, so open **Settings \> Resources** in Docker Desktop, raise the memory limit, and rerun the build.


[​](#raw-mode-is-not-supported-during-install)

`Raw mode is not supported` during install

When your organization’s [server-managed settings](../13-Enterprise-Admin/server-managed-settings.md) include changes that need [security approval](../13-Enterprise-Admin/server-managed-settings.md#security-approval-dialogs), Claude Code versions before 2.1.246 try to show the approval dialog during `claude install`. The dialog needs a terminal on stdin. When the installer runs `claude install` from a pipe, as `curl -fsSL https://claude.ai/install.sh | bash` does, stdin is the pipe rather than a terminal, so the install fails with an error containing `Raw mode is not supported`. Claude Code v2.1.246 and later don’t show the dialog during `claude install` or `claude update`. The command runs with the settings you last approved, and Claude Code shows the dialog in your next interactive session. If your organization’s startup configuration [waits for the settings fetch](../13-Enterprise-Admin/server-managed-settings.md#enforce-fail-closed-startup), such as when it sets `forceRemoteSettingsRefresh`, the dialog still appears during these commands, and an install run from a pipe still fails. In every other configuration, rerunning the installer gets past this error, because the script runs the latest release’s `install` command even when you ask it to install an older version. Rerun the command for your platform:

- macOS/Linux

- Windows PowerShell

```python
curl -fsSL https://claude.ai/install.sh | bash
```

```python
irm https://claude.ai/install.ps1 | iex
```

`claude --version` prints the version the rerun installed.


[​](#claude-update-or-claude-doctor-hangs)

`claude update` or `claude doctor` hangs

`claude update` and `claude doctor` scan your shell configuration files for an outdated `claude` alias: `~/.zshrc`, `~/.bashrc`, and `~/.config/fish/config.fish`, plus on macOS the first of `~/.bash_profile`, `~/.bash_login`, or `~/.profile` that exists. If you set `ZDOTDIR`, the Zsh file is `$ZDOTDIR/.zshrc` instead. When one of those paths is a directory, Claude Code skips it and both commands complete normally. Before v2.1.214, a directory at one of those paths made both commands hang and left the System diagnostics section of `/status` blank. `claude doctor` hung with no output; `claude update` hung right after printing `Checking for updates`. If you hit the hang on an earlier version, find the directory. In this command’s output, a line starting with `d` marks that path as a directory. A `No such file or directory` line means nothing exists at that path and isn’t the cause:

```python
ls -ld ~/.zshrc ~/.bashrc ~/.bash_profile ~/.bash_login ~/.profile ~/.config/fish/config.fish
```

Move the directory aside, or update to v2.1.214 or later. Since `claude update` hangs on the affected versions, update by rerunning the [install script](../01-Getting-Started/setup.md#install-claude-code) instead.


[​](#claude-desktop-overrides-the-claude-command-on-windows)

Claude Desktop overrides the `claude` command on Windows

If you installed an older version of Claude Desktop, it may register a `Claude.exe` in the `WindowsApps` directory that takes PATH priority over Claude Code CLI. Running `claude` opens the Desktop app instead of the CLI. Update Claude Desktop to the latest version to fix this issue.


[​](#claude-code-on-windows-requires-either-git-for-windows-for-bash-or-powershell)

Claude Code on Windows requires either Git for Windows (for bash) or PowerShell

Git for Windows is optional. Claude Code uses the [PowerShell tool](tools-reference.md#powershell-tool) when Git Bash is absent, so this error means neither shell was found. **If PowerShell is missing from your PATH**, its default location is `C:\Windows\System32\WindowsPowerShell\v1.0\`. Add that directory to your `PATH`, or install [PowerShell 7](https://aka.ms/powershell), which provides `pwsh`. **To install Git for Windows instead**, download it from [git-scm.com/downloads/win](https://git-scm.com/downloads/win). During setup, select “Add to PATH.” Restart your terminal after installing. Installing it enables the Bash tool, useful when working with Bash-based scripts and tooling. **If Git is already installed** but Claude Code can’t find it, compare its location against the places Claude Code checks. When `CLAUDE_CODE_GIT_BASH_PATH` isn’t set, Claude Code looks for `bash.exe` in this order:

1.  The default install locations `C:\Program Files\Git` and `C:\Program Files (x86)\Git`.
2.  The `git` on your `PATH`, using the `bin\bash.exe` from that Git installation.

In step 2, Claude Code skips a `git` that sits in the folder you launched Claude Code from, or below it in a path that contains `node_modules` or a virtual-environment folder such as `.venv` or `env`, for example `C:\dev\env\myproject\Git` when you launched from `C:\dev\env\myproject`. This keeps Claude Code from running an executable that a project placed there. If your Git is in a location like that, point `CLAUDE_CODE_GIT_BASH_PATH` at it. **To point Claude Code at a specific Git installation**, find it by running `where.exe git` in PowerShell, then set the `bin\bash.exe` path from that installation as `CLAUDE_CODE_GIT_BASH_PATH` in your [settings.json file](settings.md):

```python
{
  "env": {
    "CLAUDE_CODE_GIT_BASH_PATH": "C:\\Program Files\\Git\\bin\\bash.exe"
  }
}
```

**If `CLAUDE_CODE_GIT_BASH_PATH` is set to the correct path and the file exists** but Claude Code still doesn’t use it, check the file’s name first. Claude Code accepts only a file named `bash.exe`, `sh.exe`, `bash`, or `sh`; with any other name, such as Git for Windows’ `git-bash.exe` launcher, it ignores the variable and auto-detects Git Bash as if it were unset, logging a warning visible with `--debug`. A path that doesn’t exist gets the same fallback and warning. Before v2.1.219, Claude Code used any existing file as the shell without checking its name, and exited at startup with `Claude Code was unable to find CLAUDE_CODE_GIT_BASH_PATH path` when the path didn’t exist. If the file’s name is right, endpoint security software such as AppLocker, Group Policy software restriction policies, or EDR agents may be interfering. Ask your IT team to allowlist `claude.exe` and the processes it spawns, including `cmd.exe` and `bash.exe`, in your endpoint protection policy.


[​](#claude-code-does-not-support-32-bit-windows)

Claude Code does not support 32-bit Windows

Windows includes two PowerShell entries in the Start menu: `Windows PowerShell` and `Windows PowerShell (x86)`. The x86 entry runs as a 32-bit process and triggers this error even on a 64-bit machine. To check which case you’re in, run this in the same window that produced the error:

```python
[Environment]::Is64BitOperatingSystem
```

If this prints `True`, your operating system is fine. Close the window, open `Windows PowerShell` without the x86 suffix, and run the install command again. If this prints `False`, you are on a 32-bit edition of Windows. Claude Code requires a 64-bit operating system. See the [system requirements](../01-Getting-Started/setup.md#system-requirements).


[​](#linux-musl-or-glibc-binary-mismatch)

Linux musl or glibc binary mismatch

If you see errors about missing shared libraries like `libstdc++.so.6` or `libgcc_s.so.1` after installation, the installer may have downloaded the wrong binary variant for your system.

```python
Error loading shared library libstdc++.so.6: No such file or directory
```

This can happen on glibc-based systems that have musl cross-compilation packages installed, causing the installer to misdetect the system as musl. **Solutions:**

1.  **Check which libc your system uses**:

    ``` shiki
    ldd --version 2>&1 | head -1
    ```

    Output mentioning `GNU libc` or `GLIBC` means glibc. Output mentioning `musl` means musl.
2.  **If you’re on glibc but got the musl binary**, remove the installation and reinstall. You can also manually download the correct binary using the manifest at `https://downloads.claude.ai/claude-code-releases/{VERSION}/manifest.json`. File a [GitHub issue](https://github.com/anthropics/claude-code/issues) with the output of `ldd --version` and `ls /lib/libc.musl*`.
3.  **If you’re actually on musl**, such as Alpine Linux, install the required packages:

    ``` shiki
    apk add libgcc libstdc++ ripgrep
    ```

    On Alpine, `ripgrep` is in the community repository. If `apk` reports that the package is missing, see [Alpine Linux setup](../01-Getting-Started/setup.md#alpine-linux-and-musl-based-distributions).


[​](#illegal-instruction)

`Illegal instruction`

If running `claude` or the installer prints `Illegal instruction`, the native binary uses CPU instructions your processor doesn’t support. There are two distinct causes. **Architecture mismatch.** The installer downloaded the wrong binary, for example x86 on an ARM server. Check with `uname -m` on macOS or Linux, or `$env:PROCESSOR_ARCHITECTURE` in PowerShell. If the result doesn’t match the binary you received, [file a GitHub issue](https://github.com/anthropics/claude-code/issues) with the output. **Missing AVX instruction set.** If your architecture is correct but you still see `Illegal instruction`, your CPU likely lacks AVX or another instruction the binary requires. This affects roughly pre-2013 Intel and AMD processors, and virtual machines where the hypervisor does not pass AVX through to the guest. On a VPS or VM, run `grep -m1 -ow avx /proc/cpuinfo`; an empty result means AVX is not available to the guest. There is no native-binary workaround; track [issue \#50384](https://github.com/anthropics/claude-code/issues/50384) for status, and include your CPU model from `grep -m1 "model name" /proc/cpuinfo` on Linux or `sysctl -n machdep.cpu.brand_string` on macOS when reporting. Alternative install methods download the same native binary and won’t resolve either cause.


[​](#dyld-cannot-load-on-macos)

`dyld: cannot load` on macOS

If you see `dyld: Symbol not found`, `dyld: cannot load`, or `Abort trap: 6` during installation, the binary is incompatible with your macOS version or hardware. A `Symbol not found` error that references `libicucore` means your macOS version is older than the binary supports:

```python
dyld: Symbol not found: _ubrk_clone
  Referenced from: claude-darwin-x64 (which was built for Mac OS X 13.0)
  Expected in: /usr/lib/libicucore.A.dylib
```

The loader can instead reject the binary’s load commands, which also means your macOS version is too old:

```python
dyld: cannot load 'claude-2.1.42-darwin-x64' (load command 0x80000034 is unknown)
Abort trap: 6
```

**Solutions:**

1.  **Check your macOS version**: Claude Code requires macOS 13.0 or later. Open the Apple menu and select About This Mac to check your version.
2.  **Update macOS** if you’re on an older version. The binary uses load commands and system libraries that older macOS versions don’t support. Alternative install methods like Homebrew download the same binary and won’t resolve this error.


[​](#exec-format-error-on-wsl1)

`Exec format error` on WSL1

If running `claude` in WSL prints `cannot execute binary file: Exec format error`, you’re on WSL1 and hitting a known native-binary regression tracked in [issue \#38788](https://github.com/anthropics/claude-code/issues/38788). The binary’s program headers changed in a way WSL1’s loader can’t handle. The cleanest fix is to convert your distribution to WSL2 from PowerShell:

```python
wsl --set-version <DistroName> 2
```

If you need to stay on WSL1, invoke the binary through the dynamic linker. Add this function to `~/.bashrc` inside WSL, replacing the path if your home directory differs:

```python
claude() {
  /lib64/ld-linux-x86-64.so.2 "$(readlink -f "$HOME/.local/bin/claude")" "$@"
}
```

Then run `source ~/.bashrc` and retry `claude`.


[​](#npm-install-errors-in-wsl)

npm install errors in WSL

These issues apply if you installed Claude Code with `npm install -g` inside WSL. If you used the [native installer](../01-Getting-Started/setup.md), skip this section. **OS or platform detection issues.** If npm reports a platform mismatch during install, WSL is likely picking up the Windows `npm`. Run `npm config set os linux` first, then install with `npm install -g @anthropic-ai/claude-code --force`. Do not use `sudo`. **`exec: node: not found` when running `claude`.** Your WSL environment is likely using the Windows installation of Node.js. Confirm with `which npm` and `which node`: paths starting with `/mnt/c/` are Windows binaries, while Linux paths start with `/usr/`. To fix this, install Node via your Linux distribution’s package manager or via [`nvm`](https://github.com/nvm-sh/nvm). **nvm version conflicts.** If you have nvm installed in both WSL and Windows, switching Node versions in WSL may break because WSL imports the Windows PATH by default and the Windows nvm takes priority. The most common cause is that nvm isn’t loaded in your shell. Add the nvm loader to `~/.bashrc` or `~/.zshrc`:

```python
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

Or load it in your current session:

```python
source ~/.nvm/nvm.sh
```

If nvm is loaded but Windows paths still take priority, prepend your Linux Node path explicitly:

```python
export PATH="$HOME/.nvm/versions/node/$(node -v)/bin:$PATH"
```

Avoid disabling Windows PATH importing via `appendWindowsPath = false` as this breaks the ability to call Windows executables from WSL. Similarly, avoid uninstalling Node.js from Windows if you use it for Windows development.


[​](#permission-errors-during-installation)

Permission errors during installation

If the native installer fails with permission errors, the target directory may not be writable. See [Check directory permissions](#check-directory-permissions). If you previously installed with npm and are hitting npm-specific permission errors, switch to the native installer:

```python
curl -fsSL https://claude.ai/install.sh | bash
```


[​](#native-binary-not-found-after-npm-install)

Native binary not found after npm install

The `@anthropic-ai/claude-code` npm package downloads the native binary as a per-platform optional dependency, such as `@anthropic-ai/claude-code-darwin-arm64`. npm then runs the package’s postinstall script, which copies that binary into place as the `claude` command; until it runs, `claude` is a placeholder script. If either the download or the postinstall step is skipped, the placeholder stays in place, and running `claude` on macOS and Linux prints:

```python
Error: claude native binary not installed.

Either postinstall did not run (--ignore-scripts, some pnpm configs)
or the platform-native optional dependency was not downloaded
(--omit=optional).

Run the postinstall manually (adjust path for local vs global install):
  node node_modules/@anthropic-ai/claude-code/install.cjs

Or reinstall without --ignore-scripts / --omit=optional.
```

On Windows, `bin/claude.exe` is that same shell-script placeholder rather than a real executable, so PowerShell and CMD report that they can’t run the file instead of printing this message. Check the following causes:

- **Optional dependencies are disabled.** Remove `--omit=optional` from your npm install command, `--no-optional` from pnpm, or `--ignore-optional` from yarn, and check that `.npmrc` does not set `optional=false`. Then reinstall. The native binary is delivered only as an optional dependency, so there is no JavaScript fallback if it is skipped, and running `install.cjs` again can’t place a binary that was never downloaded.
- **Install scripts are disabled.** `--ignore-scripts` and some pnpm configurations skip the postinstall step but still download the platform package. Run `node node_modules/@anthropic-ai/claude-code/install.cjs` as the message suggests, or reinstall without the flag. If postinstall can’t run in your environment at all, `node node_modules/@anthropic-ai/claude-code/cli-wrapper.cjs` finds the downloaded package and launches it, at the cost of an extra Node process on each start. If the wrapper prints `Could not find native binary package` instead, the platform package was never downloaded, so fix the optional-dependencies cause above first.
- **Unsupported platform.** Prebuilt binaries are published for `darwin-arm64`, `darwin-x64`, `linux-x64`, `linux-arm64`, `linux-x64-musl`, `linux-arm64-musl`, `win32-x64`, and `win32-arm64`. Claude Code does not ship a binary for other platforms; see the [system requirements](../01-Getting-Started/setup.md#system-requirements). On FreeBSD, the installer reports the platform as unsupported. Before v2.1.205, it treated FreeBSD as Linux and downloaded a binary that couldn’t run.
- **Corporate npm mirror is missing the platform packages.** Ensure your registry mirrors all eight `@anthropic-ai/claude-code-*` platform packages in addition to the meta package.


[​](#npm-enotempty-during-update-or-reinstall)

npm `ENOTEMPTY` error during update or reinstall

When you run `npm install -g @anthropic-ai/claude-code` over an existing installation, npm can fail while moving the old package directory aside:

```python
npm error code ENOTEMPTY
npm error syscall rename
npm error path /home/you/.nvm/versions/node/v22.13.1/lib/node_modules/@anthropic-ai/claude-code
npm error dest /home/you/.nvm/versions/node/v22.13.1/lib/node_modules/@anthropic-ai/.claude-code-tVWAnUUt
npm error errno -39
npm error ENOTEMPTY: directory not empty, rename '...'
```

The `npm error path` line names the directory npm couldn’t move. Delete that directory and any leftover `.claude-code-*` directories next to it, which earlier interrupted runs can leave behind. The commands below find your global package directory with `npm root -g`; if the directory the `npm error path` line names is not under the directory `npm root -g` prints, for example because you switched Node versions with nvm, delete the directories the error names instead:

- macOS/Linux

- Windows PowerShell

```python
rm -rf "$(npm root -g)/@anthropic-ai/claude-code"
```

Then remove any leftover temp directories. If Zsh prints `no matches found`, there were none to remove:

```python
rm -rf "$(npm root -g)/@anthropic-ai/.claude-code-"*
```

```python
Remove-Item -Recurse -Force "$(npm root -g)/@anthropic-ai/claude-code", "$(npm root -g)/@anthropic-ai/.claude-code-*"
```

Then reinstall:

```python
npm install -g @anthropic-ai/claude-code
```

Confirm with `claude --version`, which prints a version number such as `2.1.211 (Claude Code)`.


[​](#login-and-authentication)

Login and authentication

These sections address login failures, OAuth errors, and token issues.


[​](#reset-your-login)

Reset your login

When login fails and the cause isn’t obvious, a clean re-authentication resolves most cases:

1.  Run `/logout` to sign out completely
2.  Close Claude Code
3.  Restart with `claude` and complete the authentication process again

If the browser doesn’t open automatically during login, press `c` to copy the OAuth URL to your clipboard, then paste it into a browser manually. This also works when the URL wraps across lines in a narrow or SSH terminal and can’t be clicked directly.


[​](#oauth-error-invalid-code)

OAuth error: Invalid code

If you see `OAuth error: Invalid code. Please make sure the full code was copied`, the login code expired or was truncated during copy-paste. **Solutions:**

- Press Enter to retry and complete the login quickly after the browser opens
- Type `c` to copy the full URL if the browser doesn’t open automatically
- If using a remote/SSH session, the browser may open on the wrong machine. Copy the URL displayed in the terminal and open it in your local browser instead.


[​](#403-forbidden-after-login)

403 Forbidden after login

If you see `API Error: 403 {"error":{"type":"forbidden","message":"Request not allowed"}}` after logging in:

- **Claude Pro/Max users**: verify your subscription is active at [claude.ai/settings](https://claude.ai/settings)
- **Anthropic Console users**: confirm your account has the “Claude Code” or “Developer” role. Admins assign this in the Anthropic Console under Settings → Members.
- **Behind a proxy**: corporate proxies can interfere with API requests. See [network configuration](../13-Enterprise-Admin/network-config.md) for proxy setup.


[​](#claude-code-access-has-not-been-granted-for-this-account)

Claude Code access has not been granted for this account

If the sign-in page shows `Authorization failed` with the message `Claude Code access has not been granted for this account. Contact your administrator.` after you log in from Claude Code, your Claude Enterprise organization has set your role to Custom and none of the [custom roles](../17-Billing-Plans/manage-custom-roles-on-enterprise-plans.md) assigned to your groups grants Claude Code. On the Custom role, you get access only from those custom roles, so nothing you change in Claude Code resolves this error. To get access:

1.  Ask an Owner of your Claude organization to assign a custom role that grants Claude Code access to one of your groups, or to change your role from Custom to a standard role such as User. Owners manage roles in the organization’s [role settings](https://claude.ai/admin-settings/roles).
2.  After the Owner makes the change, run `claude` and log in again.


[​](#this-organization-has-been-disabled-with-an-active-subscription)

This organization has been disabled with an active subscription

If you see `API Error: 400 ... "This organization has been disabled"` despite having an active Claude subscription, an `ANTHROPIC_API_KEY` environment variable is overriding your subscription. This commonly happens when an old API key from a previous employer or project is still set in your shell profile. When `ANTHROPIC_API_KEY` is present and you have approved it, Claude Code uses that key instead of your subscription’s OAuth credentials. In non-interactive mode with the `-p` flag, the key is always used when present. See [authentication precedence](../13-Enterprise-Admin/iam.md#authentication-precedence) for the full resolution order. To use your subscription instead, unset the environment variable and remove it from your shell profile:

- macOS/Linux

- Windows PowerShell

```python
unset ANTHROPIC_API_KEY
claude
```

```python
Remove-Item Env:ANTHROPIC_API_KEY
claude
```

Check `~/.zshrc`, `~/.bashrc`, or `~/.profile` for `export ANTHROPIC_API_KEY=...` lines and remove them to make the change permanent. On Windows, check your PowerShell profile at `$PROFILE` and your User environment variables for `ANTHROPIC_API_KEY`. Run `/status` inside Claude Code to confirm which authentication method is active.


[​](#oauth-login-fails-in-wsl2-ssh-or-containers)

OAuth login fails in WSL2, SSH, or containers

When Claude Code runs in WSL2, on a remote machine over SSH, or inside a container, the browser usually opens on a different host and its redirect can’t reach Claude Code’s local callback server. After you sign in, the browser shows a login code instead of redirecting back automatically. Paste that code into the terminal at the `Paste code here if prompted` prompt to complete login. If the browser doesn’t open at all from WSL2, set the `BROWSER` environment variable to your Windows browser path:

```python
export BROWSER="/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
claude
```

Alternatively, press `c` at the interactive login prompt to copy the OAuth URL, or copy the URL that `claude auth login` prints, and open it in a browser on your local machine. If pasting the code into the interactive prompt does nothing, your terminal’s paste binding likely isn’t reaching the input field. Try your terminal’s alternate paste shortcut, often right-click or Shift+Insert in Windows Terminal, or use `claude auth login` instead, which reads the pasted code from standard input:

```python
claude auth login
```

This fallback also applies on native Windows or any terminal where pasting into the interactive prompt fails.


[​](#not-logged-in-or-token-expired)

Not logged in or token expired

If Claude Code prompts you to log in again after a session, your OAuth token may have expired. Run `/login` to re-authenticate. If this happens frequently, check that your system clock is accurate, as token validation depends on correct timestamps. Parallel sessions on one machine share a saved login and coordinate its renewal so that only one process refreshes the token at a time. Before v2.1.211, waking the machine from sleep could cause two sessions to renew with the same token, which revoked the saved login and prompted every open session to log in again at once. On macOS, Claude Code saves credentials to the login Keychain. When the Keychain rejects the write, such as when it’s locked in an SSH session or its password is out of sync with your account password, Claude Code saves your login to the plaintext `~/.claude/.credentials.json` file instead. A Console login that creates an API key fails until the Keychain is writable again. To make the Keychain writable again and move your login back into the encrypted Keychain:

1

Check Keychain access

Run `claude doctor` to check Keychain access. When the Keychain rejects writes, the report lists a warning that starts with `macOS Keychain is not writable`, followed by a suggested fix. When the report lists no Keychain warning, the Keychain is writable and you can skip to the last step.

2

Unlock the Keychain

```python
security unlock-keychain ~/Library/Keychains/login.keychain-db
```

Enter your Keychain password when the command asks for it, then run `claude doctor` again. When the unlock worked, the report no longer lists the Keychain warning.

3

Resync the Keychain password if unlocking doesn't help

Open Keychain Access, select the `login` keychain, and choose **Edit \> Change Password for Keychain “login”** to resync it with your account password. Then run `claude doctor` again. Go on to the next step once the report no longer lists the Keychain warning.

4

Log out and back in

Once the Keychain is writable again, Claude Code moves the credentials back the next time it writes a credential. To force it now, run `/logout` and then `/login`. Logging out removes all stored credentials, including the plaintext file’s contents, saved MCP server logins, and plugin sensitive values, so expect to re-authorize MCP servers and re-enter plugin secrets afterwards. Logging in again stores your login in the Keychain.


[​](#bedrock-agent-platform-or-foundry-credentials-not-loading)

Bedrock, Agent Platform, or Foundry credentials not loading

If you configured Claude Code to use a cloud provider and see `Could not load credentials from any providers` on Amazon Bedrock, `Could not load the default credentials` on Google Cloud’s Agent Platform, or `ChainedTokenCredential authentication failed` on Microsoft Foundry, your cloud provider CLI is likely not authenticated in the current shell. For Amazon Bedrock, confirm your AWS credentials are valid:

```python
aws sts get-caller-identity
```

For Google Cloud’s Agent Platform, confirm `ANTHROPIC_VERTEX_PROJECT_ID` and `CLOUD_ML_REGION` are set in your shell, then set application default credentials:

```python
gcloud auth application-default login
```

For Microsoft Foundry, confirm `ANTHROPIC_FOUNDRY_API_KEY` is set, or sign in with the Azure CLI so the default credential chain can find your account:

```python
az login
```

If credentials work in your terminal but not in the VS Code or JetBrains extension, the IDE process likely didn’t inherit your shell environment. Set the provider environment variables in the IDE’s own settings, or launch the IDE from a terminal where they’re already exported. See [Amazon Bedrock](amazon-bedrock.md), [Google Cloud’s Agent Platform](google-vertex-ai.md), or [Microsoft Foundry](microsoft-foundry.md) for full provider setup.


[​](#still-stuck)

Still stuck

If none of the above resolves your issue:

1.  Check the [GitHub repository](https://github.com/anthropics/claude-code/issues) for known issues, or open a new one with your operating system, the install command you ran, and the full error output
2.  If `claude --version` works but something else is wrong, run `claude doctor` for an automated diagnostic report
3.  If you can start a session, use `/feedback` inside Claude Code to report the problem
4.  If the problem is with your account rather than the install, such as a login loop, a subscription that isn’t recognized, or a disabled organization, contact Anthropic support: sign in at [claude.ai](https://claude.ai) (Console users: [platform.claude.com](../04-API-Reference/Other/usage-limits.md)), click your initials in the lower left, and select **Get help**. See [How to get support](https://support.claude.com/en/articles/9015913-how-to-get-support) for the full flow.
