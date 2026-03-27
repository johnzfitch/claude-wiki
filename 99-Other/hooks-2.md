# Claude Code Hooks Documentation

## Installed Hooks

All hooks are installed in `~/.claude/hooks/` and configured in `~/.claude/settings.json`.

---

## 1. pre-tool-use

**Runs:** Before each tool execution
**Purpose:** Security validation + cost tracking

**Features:**

- Blocks destructive commands (`rm -rf`, `mkfs`, `dd`) with confirmation dialog
- Warns on sudo usage with critical notification
- Blocks network security commands (`iptables`, `firewalld`)
- Prevents editing sensitive files (`.env`, `credentials`, `.ssh/id_*`, `.aws/credentials`)
- Warns on system file edits (`/etc/`, `/usr/`, `/boot/`)
- Tracks all tool usage to `~/.claude/tool-usage.csv`
- Daily budget alerts (if `~/.claude/api-costs.log` exists)

**Example:**

```
Claude attempts: Edit ~/.ssh/id_rsa
Hook blocks: Blocked - Cannot modify sensitive file
```

---

## 2. post-tool-use

**Runs:** After each tool execution
**Purpose:** Auto-backup + remote sync + notifications

**Features:**

- Auto dura snapshots after Edit/Write operations
- Syncs NixOS configs to `adept:/tmp/nixos-deploy/` when `.nix` files are edited
- Queues web assets for deployment (`public/**/*.{css,js,png}`)
- Tracks icon usage from iconics library to `~/dev/iconics/.usage-log.csv`
- Notifies on long-running tasks (>30s)
- Plays completion sound for long tasks

**Example:**

```
Claude edits: ~/dev/digitaldelusion/nixos/configuration.nix
Hook syncs: NixOS config -> adept staging
Notification: "NixOS config synced to staging on adept"
```

---

## 3. user-prompt-submit

**Runs:** When user submits a prompt
**Purpose:** Context enhancement + TODO detection

**Features:**

- Shows current git branch and status
- Warns about uncommitted changes
- Shows stash count if any
- Detects project type (Node.js, Python, Rust) and displays project name
- Searches for related TODOs when keywords like "fix", "bug", "todo" are mentioned
- Warns if in production directory
- Checks SSHFS mount status when server-related keywords detected

**Example:**

```
User: "fix the login bug"
Hook adds:
  [Auto-context: main]
  [Warning: Uncommitted changes detected]
  [Project: my-app]
  [Related TODOs found in codebase:]
  src/auth.js:42:// TODO: Fix session timeout bug
```

---

## 4. session-start

**Runs:** At Claude session start
**Purpose:** Environment validation + session logging

**Features:**

- Logs session metadata to `~/.claude/session-log.txt`
- Checks SSHFS mount status (cPanel, Tier.net)
- Validates mise Python in venv projects
- Checks for required API keys
- Validates MCP server status (Google Workspace)
- Shows git status (uncommitted changes, ahead/behind remote)
- Warns if disk usage >90%
- Checks if dura auto-backup is running

**Example:**

```
Session starts in ~/dev/my-project
Hook reports:
  Info: cPanel mount not active
  Info: Branch is 2 commit(s) ahead of remote
  Info: Google Workspace MCP server not running
```

---

## 5. tool-error

**Runs:** When a tool fails
**Purpose:** Error logging + notifications

**Features:**

- Critical notification on tool failures
- Logs errors to `~/.claude/errors.log` (keeps last 1000)
- Provides helpful hints for common errors:
  - Permission denied -> Check sudo/permissions
  - Command not found -> Check installation/PATH
  - Read-only -> Check file permissions

**Example:**

```
Tool fails: Bash error "permission denied"
Hook logs: ~/.claude/errors.log
Notification: Bash failed - permission denied
Hint: May need sudo or file permissions check
```

---

## Log Files Created

| File | Purpose |
|------|---------|
| `~/.claude/tool-usage.csv` | All tool usage with timestamps |
| `~/.claude/api-costs.log` | API cost tracking (if you create it) |
| `~/.claude/session-log.txt` | Session start metadata |
| `~/.claude/errors.log` | Tool error history (last 1000) |
| `~/.claude/pending-deploys.txt` | Queued web asset deployments |
| `~/dev/iconics/.usage-log.csv` | Icon usage tracking |

---

## Testing Hooks

Test each hook:

```bash
# Test pre-tool-use (should show confirmation dialog)
claude -p "delete this file: rm -rf /tmp/test"

# Test post-tool-use (creates dura snapshot)
claude -p "create a test file" <<< "Edit test.txt with: hello world"

# Test user-prompt-submit (shows context)
cd ~/dev/some-git-repo
claude -p "fix the bug"

# Test session-start (check ~/.claude/session-log.txt)
claude

# Test tool-error (creates error log)
claude -p "run invalid command" <<< "Bash: invalidcommandxyz"
```

---

## Customization

Edit hooks in `~/.claude/hooks/` to customize behavior:

- **Add new security rules:** Edit `pre-tool-use`
- **Change sync destinations:** Edit `post-tool-use`
- **Modify context output:** Edit `user-prompt-submit`
- **Add environment checks:** Edit `session-start`
- **Customize error hints:** Edit `tool-error`

All hooks are bash scripts - make them executable after editing:

```bash
chmod +x ~/.claude/hooks/*
```

---

## Disabling Hooks

To disable a hook, set an empty array in `~/.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": []
  }
}
```

Or remove the entire `"hooks"` section.

---

## Log Redaction

- Treat logs as sensitive. Tool arguments can include secrets.
- Redact tokens, cookies, Authorization headers, and .env values before writing logs.
- Set log file permissions to owner-only (`chmod 600`).

---

## Documentation

Official docs: https://code.claude.com/docs/en/hooks
