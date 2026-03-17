# Complete Slash Command Reference -- Claude Code 2.1.59

Every slash command registered in the binary, organized by category.
Extracted from the `pdA` command aggregation array and bundled skill registry.

---

## Navigation & Session

| Command | Description | Notes |
|---------|-------------|-------|
| `/clear` | Clear conversation history and free up context | aliases: `reset`, `new` |
| `/compact` | Clear history but keep summary in context | env-gated: `DISABLE_COMPACT` |
| `/context` | Show current context usage as a colored grid | hidden in non-interactive |
| `/continue` | alias for `/resume` | |
| `/cost` | Show total cost and duration of current session | hidden in first-party |
| `/desktop` | Continue session in Claude Desktop | alias: `app`; hidden when unavailable |
| `/exit` | Exit the REPL | alias: `quit` |
| `/export` | Export conversation to file or clipboard | |
| `/files` | List all files currently in context | DISABLED (flag-gated) |
| `/fork` | Create a fork of the conversation at this point | |
| `/rename` | Rename the current conversation | |
| `/resume` | Resume a previous conversation | alias: `continue` |
| `/session` | Show remote session URL and QR code | hidden when not remote |
| `/tag` | Toggle a searchable tag on the session | DISABLED |
| `/tasks` | List and manage background tasks | alias: `bashes`; hidden |

## Model & Mode

| Command | Description | Notes |
|---------|-------------|-------|
| `/fast` | Toggle fast mode (Opus 4.6 only) | hidden when `ND()` is false |
| `/model` | Set the AI model | |
| `/output-style` | Set output style (Explanatory, Learning, custom) | |
| `/plan` | Enable plan mode or view session plan | |
| `/vim` | Toggle Vim / Normal editing modes | |

## Configuration

| Command | Description | Notes |
|---------|-------------|-------|
| `/agents` | Manage agent configurations | aliases: `plugins`, `marketplace` |
| `/chrome` | Claude in Chrome (Beta) settings | hidden in interactive mode |
| `/color` | Set prompt bar color for this session | |
| `/config` | Open config panel | alias: `settings` |
| `/hooks` | Manage hook configurations for tool events | |
| `/keybindings` | Open/create keybindings config file | gated: `tengu_keybinding_customization_release` |
| `/mcp` | Manage MCP servers | |
| `/memory` | Edit Claude memory files | |
| `/permissions` | Manage allow & deny tool permission rules | alias: `allowed-tools` |
| `/plugin` | Manage Claude Code plugins | aliases: `plugins`, `marketplace` |
| `/privacy-settings` | View and update privacy settings | |
| `/statusline` | Set up Claude Code's status line UI | bundled skill |
| `/theme` | Change the theme | |

## Git & Code

| Command | Description | Notes |
|---------|-------------|-------|
| `/commit` | Create a git commit | bundled skill (prompt type) |
| `/commit-push-pr` | Commit, push, and open a PR | bundled skill (prompt type) |
| `/diff` | View uncommitted changes and per-turn diffs | |
| `/init` | Initialize a new CLAUDE.md file | bundled skill |
| `/init-verifiers` | Create verifier skill(s) for automated verification | bundled skill |
| `/pr-comments` | Get comments from a GitHub pull request | bundled skill |
| `/review` | Review a pull request | bundled skill |
| `/rewind` | Restore code and/or conversation to a previous point | alias: `checkpoint` |
| `/security-review` | Security review of pending changes on current branch | bundled skill |

## Info & Diagnostics

| Command | Description | Notes |
|---------|-------------|-------|
| `/copy` | Copy last response or code block to clipboard | |
| `/debug` | Debug session by reading the session debug log | bundled skill |
| `/doctor` | Diagnose and verify installation and settings | env-gated: `DISABLE_DOCTOR_COMMAND` |
| `/explain_command` | Explain a shell command | tool-type command |
| `/feedback` | Submit feedback about Claude Code | alias: `bug`; env-gated |
| `/help` | Show help and available commands | |
| `/insights` | Generate report analyzing Claude Code sessions | bundled skill |
| `/release-notes` | Show release notes | |
| `/sandbox` | Show sandbox information | |
| `/skills` | List available skills | |
| `/stats` | Show usage statistics and activity | |
| `/status` | Show version, model, account, API connectivity, tools | |
| `/terminal-setup` | Terminal setup assistance | |
| `/usage` | Show plan usage limits | |

## Account & Auth

| Command | Description | Notes |
|---------|-------------|-------|
| `/extra-usage` | Configure extra usage when limits are hit | hidden in non-interactive |
| `/install` | Install Claude Code native build | |
| `/install-github-app` | Set up Claude GitHub Actions for a repository | env-gated |
| `/install-slack-app` | Install the Claude Slack app | |
| `/login` | Sign in to Anthropic account | env-gated: `DISABLE_LOGIN_COMMAND` |
| `/logout` | Sign out from Anthropic account | env-gated: `DISABLE_LOGOUT_COMMAND` |
| `/rate-limit-options` | Show options when rate limit is reached | HIDDEN, auto-shown |
| `/upgrade` | Upgrade to Max for higher rate limits | env-gated |

## Voice & Media

| Command | Description | Notes |
|---------|-------------|-------|
| `/voice` | Toggle voice mode | gated: `tengu_amber_quartz` + OAuth |

## Fun & Misc

| Command | Description | Notes |
|---------|-------------|-------|
| `/btw` | Side question without interrupting conversation | env: `ENABLE_BTW=true`; HIDDEN |
| `/mobile` | Show QR code for Claude mobile app | aliases: `ios`, `android` |
| `/passes` | (undocumented) | |
| `/remote-control` | Connect terminal for remote-control sessions | alias: `rc`; hidden |
| `/remote-env` | Configure default remote environment | hidden when unavailable |
| `/stickers` | Order Claude Code stickers | |
| `/think-back` | 2025 Claude Code Year in Review | gated: `tengu_thinkback` |
| `/thinkback-play` | Play the thinkback animation | HIDDEN |
| `/todos` | List current todo items | |

## Tool-Type Commands (internal)

| Command | Notes |
|---------|-------|
| `/web_search` | Registered as tool-type, not user-invocable |
| `/explain_command` | Registered as tool-type |

---

## Stub Commands (disabled/placeholder)

These commands exist in the binary as disabled stubs. They are remnants of commands
that were either removed, gated behind unreleased features, or moved to skills.

| Stub Variable | Previously Was | Status |
|---------------|---------------|--------|
| `oQI`, `sQI` | near `/add-dir` | Disabled duplicates |
| `ouD`, `suD` | near `/btw` | Disabled duplicates |
| `ipD` | near `/diff` | Disabled duplicate |
| `GdD` | `/doctor` | Disabled duplicate |
| `LlD` | `/install-slack-app` | Disabled duplicate |
| `ZrD` | `/mobile` | Disabled duplicate |
| `_oD` | `/session` | Disabled duplicate |
| `soD` | `/tasks` | Disabled duplicate |
| `IHB`, `BHB`, `EHB`, `GHB`, `FHB` | `/rewind` variants | 5 disabled slots near rewind |
| `rHB` | unknown | Generic stub |
| `vAB`, `bAB`, `uAB` | `/insights` | 3 disabled slots for insights |
| `p$B` | unknown | Generic stub |

**Pattern:** Many commands have 2-3 stub slots alongside them, suggesting they were
refactored from multiple implementations (e.g., separate "view", "manage", "create"
subcommands) into a single unified command.

---

## Concurrent-Safe Commands (cdA set)

These 17 commands can run concurrently without disrupting the main conversation loop:

```
/session  /exit  /clear  /help  /theme  /color  /vim  /cost  /usage
/copy  /btw  /feedback  /plan  /keybindings  /statusline  /stickers  /mobile
```

---

## The `/private` Mystery -- RESOLVED

The grep hits for `"/private"` in the binary are **not slash commands**. They are macOS
path normalization logic in `A5$()`:

```js
if (A.startsWith("/tmp/") && L === "/private" + A) return false;
if (A.startsWith("/var/") && L === "/private" + A) return false;
if (A.startsWith("/private/tmp/") && L === A) return false;
if (A.startsWith("/private/var/") && L === A) return false;
```

macOS symlinks `/tmp` to `/private/tmp` and `/var` to `/private/var`. This function
(`A5$`, a path ancestry checker) handles both forms to avoid false positives when
checking if a path is a parent of another.

Similarly, `jt0()` handles `$TMPDIR` paths like `/private/var/folders/xx/xxx/T/` for
sandbox temp directory allowlisting.

No `/private` slash command exists.
