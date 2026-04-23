---
title: "Claude Code Environment Variables - Deep Implementation Guide"
category: "19-Reference"
tags: ["agents", "claude-code", "desktop", "git", "mcp", "plugins", "rag", "security"]
---

# Claude Code Environment Variables - Deep Implementation Guide
## What Each Setting Actually Does

**Generated**: 2026-03-07
**Binary**: 2.1.70 (Bun 1.3.11, 68,960 functions)

This document explains the **actual implementation behavior** of each environment variable, not just its name. Each entry includes:
- **What it does** (implementation details)
- **When to use it** (practical scenarios)
- **What it affects** (downstream impacts)
- **Default behavior** (when unset)

---

## TABLE OF CONTENTS

1. [CoWork & Desktop Mode](#cowork--desktop-mode)
2. [Remote Sessions & Control](#remote-sessions--control)
3. [Memory & Storage](#memory--storage)
4. [Model & Effort Configuration](#model--effort-configuration)
5. [Context Management](#context-management)
6. [MCP (Model Context Protocol)](#mcp-model-context-protocol)
7. [Tools & Execution](#tools--execution)
8. [UI & Terminal](#ui--terminal)
9. [Tasks & Agents](#tasks--agents)
10. [Plugins](#plugins)
11. [Git Integration](#git-integration)
12. [Security & Permissions](#security--permissions)

---

## COWORK & DESKTOP MODE

### `CLAUDE_CODE_IS_COWORK`

**What it does**:
```javascript
// Forces eager flush behavior
if (CLAUDE_CODE_EAGER_FLUSH || CLAUDE_CODE_IS_COWORK) {
  await flushLogsImmediately();
}
```

**Implementation**:
- Immediately writes session data to disk after every turn (no buffering)
- Used in Electron desktop app (not CLI)
- Triggers same flush behavior as `CLAUDE_CODE_EAGER_FLUSH`

**When to use**:
- Desktop/Electron environments where buffered writes could be lost on crash
- Multi-process architectures where session state must be immediately persisted
- **Don't set manually** - auto-detected by desktop app

**Affects**:
- Log flush timing
- Session persistence behavior
- Memory write-through vs write-back strategy

---

### `CLAUDE_CODE_USE_COWORK_PLUGINS`

**What it does**:
```javascript
function getPluginDir() {
  if (isDesktopMode() || CLAUDE_CODE_USE_COWORK_PLUGINS) {
    return "cowork_plugins";  // Separate plugin directory
  }
  return "plugins";  // Normal CLI plugins
}

function getSettingsFile() {
  if (isDesktopMode() || CLAUDE_CODE_USE_COWORK_PLUGINS) {
    return "cowork_settings.json";  // Separate settings file
  }
  return "settings.json";
}
```

**Implementation**:
- Changes plugin directory from `~/.claude/plugins` → `~/.claude/cowork_plugins`
- Changes settings file from `settings.json` → `cowork_settings.json`
- Allows desktop and CLI to have separate plugin ecosystems
- No cross-contamination between CoWork (desktop) and CLI environments

**When to use**:
- Running both desktop app and CLI simultaneously
- Need to maintain separate plugin configurations
- Testing plugin compatibility across environments

**Affects**:
- Plugin discovery path
- Settings persistence location
- Plugin version management

---

## REMOTE SESSIONS & CONTROL

### `CLAUDE_CODE_REMOTE`

**What it does**:
```javascript
function isAutoMemoryEnabled() {
  // Remote mode DISABLES auto-memory by default
  if (CLAUDE_CODE_REMOTE && !CLAUDE_CODE_REMOTE_MEMORY_DIR) {
    return false;
  }
  return true;
}

// 30-minute timeout enforcement
if (session.status === "running" &&
    Date.now() - session.startTime > 30 * 60 * 1000) {
  failSession(sessionId, "remote session exceeded 30 minutes");
}

// Sandbox restrictions
if (CLAUDE_CODE_REMOTE) {
  enableStrictSandbox();
}
```

**Implementation**:
1. **Disables auto-memory** unless `CLAUDE_CODE_REMOTE_MEMORY_DIR` is explicitly set
2. **30-minute session timeout** - hard-coded, non-configurable
3. **Strict sandbox mode** - additional process restrictions
4. **Adds headers**: `x-claude-remote-session-id`, `x-claude-remote-container-id`
5. **Session lifecycle tracking** - monitors for stalls on permission prompts

**When to use**:
- CI/CD pipelines (GitHub Actions, GitLab CI)
- Codespaces/cloud development environments
- Ephemeral compute (AWS Lambda, Cloud Run)
- Multi-tenant deployments where sessions must be time-boxed

**Affects**:
- Auto-memory (disabled by default)
- Session timeout (30 min hard limit)
- Sandbox restrictions (stricter than normal)
- HTTP headers sent to API
- Permission prompt handling

**⚠️ Critical**: Remote mode assumes ephemeral environment. Don't use for long-running sessions.

---

### `CLAUDE_CODE_REMOTE_SESSION_ID`

**What it does**:
```javascript
headers: {
  "x-claude-remote-session-id": CLAUDE_CODE_REMOTE_SESSION_ID,
  "x-claude-remote-container-id": CLAUDE_CODE_CONTAINER_ID,
}
```

**Implementation**:
- Sent as HTTP header on every API request
- Used for session routing and telemetry
- Correlates requests across distributed systems

**When to use**:
- Multi-tenant environments (unique ID per tenant)
- Session tracking in load-balanced deployments
- Debugging distributed sessions

**Format**: `tenant-${TENANT_ID}-${SESSION_ID}` or any unique identifier

---

### `CLAUDE_CODE_REMOTE_MEMORY_DIR`

**What it does**:
```javascript
function getMemoryDir() {
  if (CLAUDE_CODE_REMOTE_MEMORY_DIR) {
    return CLAUDE_CODE_REMOTE_MEMORY_DIR;
  }
  return defaultMemoryDir();
}

// Enables auto-memory in remote mode
if (CLAUDE_CODE_REMOTE && CLAUDE_CODE_REMOTE_MEMORY_DIR) {
  autoMemoryEnabled = true;  // Override remote mode default
}
```

**Implementation**:
- Overrides default memory directory
- **Re-enables auto-memory in remote mode** (normally disabled)
- Must be absolute path, >3 characters, not a drive root

**When to use**:
- Remote sessions that need persistent memory
- Shared memory across ephemeral containers (mount persistent volume)
- Custom memory isolation per tenant

**Example**:
```bash
# CI/CD with persistent memory
CLAUDE_CODE_REMOTE=1
CLAUDE_CODE_REMOTE_MEMORY_DIR=/mnt/persistent/memory/${CI_JOB_ID}
```

---

### `CLAUDE_CODE_REMOTE_SEND_KEEPALIVES`

**What it does**:
```javascript
if (CLAUDE_CODE_REMOTE_SEND_KEEPALIVES) {
  setInterval(() => {
    sendKeepAliveHeartbeat();
  }, KEEPALIVE_INTERVAL);
}
```

**Implementation**:
- Sends periodic keepalive heartbeats to prevent session timeout
- Keeps connection alive in long-running remote sessions
- Prevents idle disconnects in cloud environments

**When to use**:
- Remote sessions with intermittent activity
- Cloud environments with aggressive idle timeouts
- Load balancers that drop idle connections

---

### `SESSION_INGRESS_URL`

**What it does**:
```javascript
function getSessionIngressURL(sessionId) {
  return buildURL(SESSION_INGRESS_URL, sessionId);
}
```

**Implementation**:
- Endpoint for remote session routing
- Used to proxy requests to remote containers
- Supports multi-region deployments

**When to use**:
- Multi-region session routing
- Custom ingress/gateway architectures
- Load balancing across remote sessions

---

## MEMORY & STORAGE

### `CLAUDE_CODE_DISABLE_AUTO_MEMORY`

**What it does**:
```javascript
function isAutoMemoryEnabled() {
  if (CLAUDE_CODE_DISABLE_AUTO_MEMORY) return false;
  if (CLAUDE_CODE_REMOTE && !CLAUDE_CODE_REMOTE_MEMORY_DIR) return false;
  return settings.autoMemoryEnabled ?? true;
}
```

**Implementation**:
- **Hard disable** - overrides all other settings
- Prevents reading from or writing to `~/.claude/memory/MEMORY.md`
- Claude doesn't persist or recall context across sessions

**When to use**:
- Stateless environments (every session is fresh)
- Privacy/compliance (no persistent user data)
- Testing (isolated sessions)

**⚠️ Note**: This is different from project-level `autoMemoryEnabled` in settings.json.

---

### `CLAUDE_COWORK_MEMORY_PATH_OVERRIDE`

**What it does**:
```javascript
function getCoworkMemoryPath() {
  let path = CLAUDE_COWORK_MEMORY_PATH_OVERRIDE;
  if (!path) return null;

  // Validates: absolute path, >3 chars, not drive root, not UNC
  path = normalize(path).replace(/[/\\]+$/, "");
  if (!isAbsolute(path) || path.length < 3 ||
      /^[A-Za-z]:$/.test(path) || path.startsWith("\\\\")) {
    return null;
  }
  return path;
}
```

**Implementation**:
- Shared memory directory for agent teams
- Each teammate reads/writes to same memory location
- `teammate_id` tracks individual team members
- Telemetry: `tengu_team_mem_sync_started`

**When to use**:
- Multi-agent teams (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`)
- Shared context across multiple sessions
- Team collaboration on same task

**Validation**:
- Must be absolute path
- Must be >3 characters
- Can't be drive root (`C:`, `D:`)
- Can't be UNC path (`\\server\share`)

---

## MODEL & EFFORT CONFIGURATION

### `CLAUDE_CODE_ALWAYS_ENABLE_EFFORT`

**What it does**:
```javascript
function shouldEnableEffort(modelName) {
  if (CLAUDE_CODE_ALWAYS_ENABLE_EFFORT) return true;

  // Auto-enabled for these models
  if (modelName.includes("opus-4-6") ||
      modelName.includes("sonnet-4-6")) return true;

  // Disabled for haiku/sonnet/opus (unless above)
  if (modelName.includes("haiku") ||
      modelName.includes("sonnet") ||
      modelName.includes("opus")) return false;

  // Enabled for firstParty provider by default
  return getProvider() === "firstParty";
}
```

**Implementation**:
- **Effort** = API parameter that controls thinking/reasoning depth
- Default: Only enabled for Opus 4.6, Sonnet 4.6, or firstParty provider
- This flag forces it on for all models
- Maps to `effort` field in API request body

**When to use**:
- Need extended reasoning on non-Opus models
- Forcing quality on Haiku/Sonnet
- Testing effort levels across model families

**API impact**:
```json
{
  "model": "claude-sonnet-4-0",
  "effort": 3  // Sent if CLAUDE_CODE_ALWAYS_ENABLE_EFFORT=1
}
```

---

### `CLAUDE_CODE_DISABLE_LEGACY_MODEL_REMAP`

**What it does**:
```javascript
function remapLegacyModel(modelName) {
  if (CLAUDE_CODE_DISABLE_LEGACY_MODEL_REMAP) {
    return modelName;  // No remapping
  }

  // Auto-upgrade legacy names
  if (modelName === "opus-3") return "opus-4";
  if (modelName === "sonnet-3.5") return "sonnet-4";
  return modelName;
}
```

**Implementation**:
- Prevents automatic model version upgrades
- Allows pinning to specific legacy model versions
- Useful when new models have breaking changes

**When to use**:
- Reproducible builds (pin exact model version)
- Testing compatibility across versions
- Avoiding automatic upgrades

---

### `CLAUDE_CODE_DISABLE_1M_CONTEXT`

**What it does**:
```javascript
function canUse1MContext() {
  if (CLAUDE_CODE_DISABLE_1M_CONTEXT) return false;
  return true;
}

function hasFlag1M(modelName) {
  if (CLAUDE_CODE_DISABLE_1M_CONTEXT) return false;
  return /\[1m\]/i.test(modelName);  // Checks for [1m] flag in name
}

function supports1M(modelName) {
  if (CLAUDE_CODE_DISABLE_1M_CONTEXT) return false;

  let lower = modelName.toLowerCase();
  return lower.includes("claude-sonnet-4") ||
         lower.includes("opus-4-6");
}
```

**Implementation**:
- Prevents using models with 1 million token context windows
- Falls back to standard context models
- Affects model selection logic

**When to use**:
- Cost control (1M context is more expensive)
- API quotas (1M context counts differently)
- Testing with standard context limits

**Models affected** (2.1.70):
- `claude-sonnet-4*` (all Claude 4 Sonnets)
- `opus-4-6`

---

## CONTEXT MANAGEMENT

### `CLAUDE_CODE_DISABLE_PRECOMPACT_SKIP`

**What it does**:
```javascript
// Forces compaction to run even if skipped previously
if (CLAUDE_CODE_DISABLE_PRECOMPACT_SKIP) {
  runCompaction();  // Never skip
} else {
  if (shouldSkipPrecompact()) {
    return;  // Skip compaction
  }
  runCompaction();
}
```

**Implementation**:
- **Replaces**: `CLAUDE_CODE_SKIP_PRECOMPACT_LOAD` (removed in 2.1.70)
- Forces compaction to run
- Prevents optimization that skips compaction when not needed

**When to use**:
- Aggressive memory management
- Testing compaction behavior
- Debugging context window issues

**⚠️ Note**: Name is confusing - "DISABLE_PRECOMPACT_SKIP" means "disable the skip, force compaction".

---

### `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE`

**Default**: ~95%

**What it does**:
```javascript
function shouldAutoCompact(currentTokens, maxTokens) {
  let threshold = CLAUDE_AUTOCOMPACT_PCT_OVERRIDE || 95;
  return (currentTokens / maxTokens) >= (threshold / 100);
}
```

**Implementation**:
- Triggers compaction at X% of context window
- Lower = compact earlier (more aggressive)
- Higher = compact later (use more context)

**Examples**:
```bash
# Aggressive (compact at 70% full)
CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=70

# Conservative (compact at 98% full)
CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=98

# Default (compact at 95% full)
# (unset or 95)
```

**When to use**:
- Low value (70-80): CI/CD, short sessions, aggressive memory management
- High value (95-98): Research, long sessions, maximize context usage

---

## MCP (MODEL CONTEXT PROTOCOL)

### `CLAUDE_CODE_MCP_INSTR_DELTA`

**What it does**:
```javascript
function useMCPDelta() {
  if (CLAUDE_CODE_MCP_INSTR_DELTA !== undefined) {
    return CLAUDE_CODE_MCP_INSTR_DELTA === "1";
  }
  return featureFlag("tengu_basalt_3kr", false);
}

function getMCPInstructions(previousTools, currentTools) {
  if (!useMCPDelta()) {
    return fullToolSchema(currentTools);  // Send all tools
  }

  // Only send delta (added/removed tools)
  return {
    type: "mcp_instructions_delta",
    added: currentTools.filter(t => !previousTools.includes(t)),
    removed: previousTools.filter(t => !currentTools.includes(t))
  };
}
```

**Implementation**:
- **Delta mode**: Only send tool schema changes, not full schema every turn
- Reduces prompt overhead when MCP tool definitions change
- More efficient for large tool sets

**Example**:
```javascript
// Without delta (sends ~10KB every turn)
{
  "tools": [/* all 50 tools */]
}

// With delta (sends ~500B)
{
  "mcp_instructions_delta": {
    "added": [/* 1 new tool */],
    "removed": []
  }
}
```

**When to use**:
- Large MCP tool sets (>20 tools)
- Frequently changing tool availability
- Token optimization

**Default**: Feature-flagged (`tengu_basalt_3kr`), may not be enabled for all users.

---

### `MCP_TIMEOUT`

**Default**: 30000 ms (30 seconds)

**What it does**:
```javascript
const timeout = parseInt(MCP_TIMEOUT) || 30000;
await Promise.race([
  mcpServer.start(),
  sleep(timeout).then(() => { throw new Error("MCP timeout") })
]);
```

**Implementation**:
- Startup timeout for MCP servers
- If server doesn't respond within timeout, connection fails

**When to use**:
```bash
# Slow MCP servers (database, network)
MCP_TIMEOUT=120000  # 2 minutes

# Fast local servers
MCP_TIMEOUT=5000  # 5 seconds
```

---

### `MCP_TOOL_TIMEOUT`

**Default**: 100000000 ms (effectively infinite)

**What it does**:
```javascript
const timeout = parseInt(MCP_TOOL_TIMEOUT) || 100000000;
await Promise.race([
  mcpTool.execute(),
  sleep(timeout).then(() => { throw new Error("Tool timeout") })
]);
```

**Implementation**:
- Per-tool execution timeout
- Default is ~27 hours (effectively no limit)

**When to use**:
```bash
# Strict timeouts for production
MCP_TOOL_TIMEOUT=60000  # 1 minute per tool

# Long-running analysis
MCP_TOOL_TIMEOUT=300000  # 5 minutes
```

---

### `MCP_CONNECTION_NONBLOCKING`

**What it does**:
```javascript
if (MCP_CONNECTION_NONBLOCKING) {
  // Don't wait for connection, continue startup
  mcpServer.connect().catch(err => log(err));
} else {
  // Block until connected
  await mcpServer.connect();
}
```

**Implementation**:
- **Blocking** (default): Waits for MCP connection before starting
- **Non-blocking**: Starts immediately, MCP connects in background

**When to use**:
- Non-blocking: Fast startup, MCP not critical
- Blocking: MCP required for session to work

---

## TOOLS & EXECUTION

### `CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY`

**Default**: 10

**What it does**:
```javascript
function getConcurrencyLimit() {
  return parseInt(CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY || "10");
}

// Executes tools in parallel up to limit
for (let {isConcurrencySafe, blocks} of toolBlocks) {
  if (isConcurrencySafe) {
    let running = {};
    for await (let result of executeParallel(blocks, getConcurrencyLimit())) {
      // Process results
    }
  }
}
```

**Implementation**:
- Maximum number of tool calls to execute in parallel
- Only applies to "concurrency-safe" tools
- Unsafe tools (file writes, state changes) run sequentially

**When to use**:
```bash
# High parallelism (faster, more load)
CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY=20

# Conservative (slower, less load)
CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY=3

# Strictly sequential (debugging)
CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY=1
```

**⚠️ Trade-off**: Higher concurrency = faster execution but more system load.

---

### `CLAUDE_CODE_GLOB_HIDDEN`

**Default**: `true`

**What it does**:
```javascript
let includeHidden = CLAUDE_CODE_GLOB_HIDDEN !== "false";
let args = ["--files", "--glob", pattern];
if (includeHidden) {
  args.push("--hidden");
}
```

**Implementation**:
- Controls whether Glob tool includes hidden files (`.gitignore`, `.env`, etc.)
- Default: **Include** hidden files
- Set to `"false"` (string) to exclude

**When to use**:
```bash
# Security: exclude hidden files
CLAUDE_CODE_GLOB_HIDDEN=false

# Default: include hidden files
CLAUDE_CODE_GLOB_HIDDEN=true
# or unset
```

---

### `CLAUDE_CODE_GLOB_NO_IGNORE`

**Default**: `true`

**What it does**:
```javascript
let ignoreGitignore = CLAUDE_CODE_GLOB_NO_IGNORE !== "false";
let args = ["--files", "--glob", pattern];
if (ignoreGitignore) {
  args.push("--no-ignore");  // Ignore .gitignore rules
}
```

**Implementation**:
- Controls whether Glob tool respects `.gitignore` files
- Default: **Ignore** `.gitignore` (search all files)
- Set to `"false"` to respect `.gitignore`

**When to use**:
```bash
# Respect .gitignore (exclude node_modules, build/, etc.)
CLAUDE_CODE_GLOB_NO_IGNORE=false

# Default: ignore .gitignore, search everything
CLAUDE_CODE_GLOB_NO_IGNORE=true
# or unset
```

---

## UI & TERMINAL

### `CLAUDE_CODE_SIMPLE`

**What it does**:
```javascript
function isSimpleMode() {
  return CLAUDE_CODE_SIMPLE === "1";
}

// Disables attachments in simple mode
if (CLAUDE_CODE_DISABLE_ATTACHMENTS || CLAUDE_CODE_SIMPLE) {
  return [];  // No attachments
}

// Disables CLAUDE.md loading in simple mode
if (CLAUDE_CODE_SIMPLE) {
  return null;  // Don't load CLAUDE.md
}

// Disables dynamic skill discovery
if (!CLAUDE_CODE_SIMPLE) {
  let skills = await discoverSkills(paths);
  // ...
}
```

**Implementation**:
- Simplified UI mode
- **Disables**:
  - File attachments
  - CLAUDE.md loading
  - Dynamic skill discovery
  - Various UI enhancements

**When to use**:
- Minimal/stripped-down experience
- Debugging UI issues
- Headless/automated environments
- Low-bandwidth connections

---

### `CLAUDE_CODE_ACCESSIBILITY`

**What it does**:
```javascript
if (stdout.isTTY && !CLAUDE_CODE_ACCESSIBILITY) {
  // Enable terminal features
  stdout.write(ENABLE_ALTERNATE_SCREEN);
}

if (!CLAUDE_CODE_ACCESSIBILITY) {
  stdout.write(ENABLE_MOUSE_REPORTING);
}
```

**Implementation**:
- Disables terminal features that break screen readers
- **Disables**:
  - Alternate screen buffer
  - Mouse reporting
  - Cursor positioning
  - Visual shimmer effects

**When to use**:
- Screen reader users
- Terminal accessibility requirements
- Text-only output

---

### `CLAUDE_CODE_DISABLE_TERMINAL_TITLE`

**What it does**:
```javascript
if (!CLAUDE_CODE_DISABLE_TERMINAL_TITLE) {
  setTerminalTitle("Claude Code");

  // Update title during execution
  setTerminalTitle(`Claude Code - ${taskDescription}`);
}
```

**Implementation**:
- Prevents updating terminal window title
- Useful when terminal title is managed externally

**When to use**:
- Tmux/screen sessions (preserve session names)
- Terminal multiplexers
- Custom terminal title management

---

### `CLI_WIDTH`

**What it does**:
```javascript
function getTerminalWidth() {
  if (CLI_WIDTH) {
    return parseInt(CLI_WIDTH);
  }
  return process.stdout.columns || 80;
}
```

**Implementation**:
- Overrides terminal width detection
- Affects text wrapping, table formatting, progress bars

**When to use**:
```bash
# Wide terminals
CLI_WIDTH=200

# Narrow terminals
CLI_WIDTH=80

# Debugging layout
CLI_WIDTH=120
```

---

### `CLAUDE_CODE_STREAMING_TEXT`

**What it does**:
```javascript
function shouldStreamText() {
  if (CLAUDE_CODE_STREAMING_TEXT !== undefined) {
    return CLAUDE_CODE_STREAMING_TEXT === "1";
  }
  return featureFlag("tengu_streaming_text", false);
}

if (shouldStreamText()) {
  // Stream text as it arrives
  for await (let chunk of streamResponse()) {
    process.stdout.write(chunk);
  }
} else {
  // Wait for full response
  let fullText = await getFullResponse();
  process.stdout.write(fullText);
}
```

**Implementation**:
- Enables token-by-token streaming output
- Text appears as model generates it
- More responsive UX

---

## TASKS & AGENTS

### `CLAUDE_CODE_TASK_LIST_ID`

**What it does**:
```javascript
function getTaskListID() {
  if (CLAUDE_CODE_TASK_LIST_ID) {
    return CLAUDE_CODE_TASK_LIST_ID;
  }

  let team = getCurrentTeam();
  if (team) return team.teamName;

  return getProjectID() || getSessionID();
}
```

**Implementation**:
- Shared task list ID across multiple sessions
- Sessions with same ID share same task queue
- Enables distributed task execution

**When to use**:
```bash
# Share tasks across CI jobs
CLAUDE_CODE_TASK_LIST_ID=build-${BUILD_NUMBER}

# Team task list
CLAUDE_CODE_TASK_LIST_ID=team-frontend

# Isolated per session (default)
# (unset)
```

---

### `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS`

**What it does**:
```javascript
function canBackgroundTasks() {
  if (CLAUDE_CODE_DISABLE_BACKGROUND_TASKS) {
    return false;
  }
  return true;
}

// Removes background task option from UI
if (CLAUDE_CODE_DISABLE_BACKGROUND_TASKS) {
  return null;  // Don't show Ctrl+B hint
}
```

**Implementation**:
- Disables `run_in_background` parameter on Agent tool
- Tasks must run in foreground
- User can't background long-running tasks

**When to use**:
- Debugging task execution
- Strict sequential execution
- Environments where background tasks cause issues

---

### `CLAUDE_AUTO_BACKGROUND_TASKS`

**What it does**:
```javascript
if (CLAUDE_AUTO_BACKGROUND_TASKS) {
  // Automatically background long-running tasks
  if (estimatedDuration > threshold) {
    agent.runInBackground = true;
  }
}
```

**Implementation**:
- Automatically backgrounds tasks that exceed duration threshold
- User doesn't need to explicitly request backgrounding

**When to use**:
- Long-running analysis tasks
- Multi-task workflows
- Maximize parallelism

---

### `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`

**What it does**:
```javascript
function isAgentTeamsEnabled() {
  // Requires env var OR --agent-teams flag
  if (!CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS &&
      !process.argv.includes("--agent-teams")) {
    return false;
  }

  // Requires feature flag
  if (!featureFlag("tengu_amber_flint", true)) {
    return false;
  }

  return true;
}
```

**Implementation**:
- Enables multi-agent team mode
- Requires **both**:
  1. Env var or CLI flag
  2. Feature flag `tengu_amber_flint`
- Unlocks `spawnTeam` command
- Enables `teammate_id` tracking

**When to use**:
- Complex multi-step workflows
- Parallel task execution by specialized agents
- Team collaboration simulations

**⚠️ Note**: Experimental feature, may have stability issues.

---

## PLUGINS

### `CLAUDE_CODE_PLUGIN_CACHE_DIR`

**What it does**:
```javascript
function getPluginCacheDir() {
  if (CLAUDE_CODE_PLUGIN_CACHE_DIR) {
    return CLAUDE_CODE_PLUGIN_CACHE_DIR;
  }

  let pluginType = isCoworkMode() ? "cowork_plugins" : "plugins";
  return join(configDir(), pluginType);
}
```

**Implementation**:
- Overrides plugin cache directory
- Default: `~/.claude/plugins` or `~/.claude/cowork_plugins`

**When to use**:
```bash
# Custom plugin location
CLAUDE_CODE_PLUGIN_CACHE_DIR=/mnt/shared/plugins

# Per-user plugin cache
CLAUDE_CODE_PLUGIN_CACHE_DIR=/home/${USER}/.local/claude/plugins
```

---

### `CLAUDE_CODE_PLUGIN_SEED_DIR`

**What it does**:
```javascript
function getPluginSeedDir() {
  return CLAUDE_CODE_PLUGIN_SEED_DIR || undefined;
}

// Pre-seed plugins from directory
if (seedDir = getPluginSeedDir()) {
  for (let plugin of readdir(seedDir)) {
    installPlugin(plugin);
  }
}
```

**Implementation**:
- Directory containing pre-installed plugins
- Plugins copied to cache on first run
- Useful for offline installations or corporate deployments

**When to use**:
```bash
# Offline plugin distribution
CLAUDE_CODE_PLUGIN_SEED_DIR=/opt/claude/plugins

# Docker image with bundled plugins
CLAUDE_CODE_PLUGIN_SEED_DIR=/app/bundled-plugins
```

---

### `CLAUDE_CODE_PLUGIN_USE_ZIP_CACHE`

**What it does**:
```javascript
if (CLAUDE_CODE_PLUGIN_USE_ZIP_CACHE) {
  // Cache plugins as ZIP files
  await cachePluginAsZip(plugin);
} else {
  // Extract plugin files
  await extractPluginFiles(plugin);
}
```

**Implementation**:
- Stores plugins as compressed ZIP files instead of extracted directories
- Faster cold starts (less filesystem overhead)
- Reduced disk usage

**When to use**:
- Many plugins installed
- Network filesystems (NFS, EFS)
- Docker containers (fewer layers)

---

### `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS`

**What it does**:
```javascript
const timeout = parseInt(CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS) || 30000;

await Promise.race([
  git.clone(pluginRepo),
  sleep(timeout).then(() => { throw new Error("Git timeout") })
]);
```

**Implementation**:
- Timeout for git operations during plugin installation
- Default: 30000 ms (30 seconds)

**When to use**:
```bash
# Slow networks
CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS=120000  # 2 minutes

# Fast local mirror
CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS=5000  # 5 seconds
```

---

## GIT INTEGRATION

### `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS`

**What it does**:
```javascript
function shouldIncludeGitInstructions() {
  if (CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS) return false;
  return settings.includeGitInstructions ?? true;
}

function getSystemPrompt() {
  let prompt = basePrompt;

  if (!shouldIncludeGitInstructions()) {
    return prompt;  // No git instructions
  }

  prompt += `
Only create commits when requested by the user. If unclear, ask first.
When the user asks you to create a new git commit, follow these steps carefully:
1. Review changed files with git status
2. Stage appropriate files with git add
3. Create commit with descriptive message
...
  `;

  return prompt;
}
```

**Implementation**:
- **Removes git workflow instructions from system prompt**
- Claude won't proactively suggest git commands
- Useful for non-git workflows (Perforce, SVN, Mercurial)

**When to use**:
- Non-git version control systems
- Environments where git commits are automated
- Reducing prompt size

**Default**: Includes git instructions unless explicitly disabled.

---

## SECURITY & PERMISSIONS

### `CLAUDE_CODE_ADDITIONAL_PROTECTION`

**What it does**:
```javascript
if (CLAUDE_CODE_ADDITIONAL_PROTECTION) {
  enableAdditionalSecurityChecks();
}
```

**Implementation**:
- Enables extra security validation
- Stricter input sanitization
- Additional permission checks

**When to use**:
- High-security environments
- Multi-tenant deployments
- Untrusted user input

---

### `CLAUDE_CODE_BUBBLEWRAP`

**What it does**:
```javascript
if (CLAUDE_CODE_BUBBLEWRAP) {
  // Use bubblewrap for sandboxing
  command = ["bwrap", "--ro-bind", "/", "/", ...command];
}
```

**Implementation**:
- Enables Bubblewrap sandboxing (Linux only)
- Isolates bash commands in restricted environment
- Requires `bubblewrap` package installed

**When to use**:
- Linux environments
- Untrusted code execution
- Defense-in-depth security

**Requirements**: `apt install bubblewrap` or `dnf install bubblewrap`

---

### `IS_SANDBOX`

**What it does**:
```javascript
if (IS_SANDBOX) {
  enableStrictSandboxMode();
  disableNetworkAccess();
  restrictFileSystemAccess();
}
```

**Implementation**:
- Indicates running in sandboxed environment
- Auto-detected in most cloud environments
- Triggers additional restrictions

**⚠️ Note**: Usually auto-detected, don't set manually unless you know what you're doing.

---

## ADVANCED CONFIGURATION

### `CLAUDE_CODE_RESUME_INTERRUPTED_TURN`

**What it does**:
```javascript
if (CLAUDE_CODE_RESUME_INTERRUPTED_TURN && interruptedTurn) {
  console.log(`Auto-resuming interrupted turn (kind: ${interruptedTurn.kind})`);
  sendMessage(interruptedTurn.message);
}
```

**Implementation**:
- Auto-resumes turns interrupted by connection loss
- Picks up where it left off after reconnect
- Useful for unstable connections

**When to use**:
- Mobile/flaky connections
- Cloud environments with occasional disconnects
- Long-running sessions

---

### `CLAUDE_CODE_EAGER_FLUSH`

**What it does**:
```javascript
if (CLAUDE_CODE_EAGER_FLUSH || CLAUDE_CODE_IS_COWORK) {
  await flushSessionData();  // Immediate write
}
```

**Implementation**:
- Forces immediate disk writes (no buffering)
- Same behavior as `CLAUDE_CODE_IS_COWORK`
- Prevents data loss on crashes

**When to use**:
- Crash-prone environments
- Critical session data
- Debugging data loss issues

**⚠️ Trade-off**: Slower performance due to frequent I/O.

---

### `VCR_RECORD`

**What it does**:
```javascript
if (VCR_RECORD === "all") {
  recordAllHTTPInteractions();
} else if (VCR_RECORD === "new_episodes") {
  recordOnlyNewInteractions();
} else if (VCR_RECORD === "none") {
  playbackRecordedInteractions();
}
```

**Implementation**:
- HTTP VCR cassette recording for testing
- Records/replays API interactions

**Values**:
- `all` - Record all HTTP requests
- `new_episodes` - Record only new requests
- `none` - Only playback, don't record

**When to use**:
- Testing without live API calls
- Reproducible integration tests
- Debugging API interactions

---

## DEBUGGING & PROFILING

### `CLAUDE_CODE_PROFILE_STARTUP`

**What it does**:
```javascript
if (CLAUDE_CODE_PROFILE_STARTUP) {
  console.time("startup");

  console.time("load-config");
  loadConfig();
  console.timeEnd("load-config");

  console.time("init-mcp");
  initMCP();
  console.timeEnd("init-mcp");

  console.timeEnd("startup");
}
```

**Implementation**:
- Profiles startup performance
- Measures time for each initialization phase
- Outputs timing to stderr

---

### `CLAUDE_CODE_SLOW_OPERATION_THRESHOLD_MS`

**What it does**:
```javascript
const threshold = parseInt(CLAUDE_CODE_SLOW_OPERATION_THRESHOLD_MS) || 1000;

console.time("operation");
await operation();
let duration = console.timeEnd("operation");

if (duration > threshold) {
  console.warn(`Slow operation: ${duration}ms`);
}
```

**Implementation**:
- Warns when operations exceed threshold
- Helps identify performance bottlenecks

**When to use**:
```bash
# Strict performance monitoring
CLAUDE_CODE_SLOW_OPERATION_THRESHOLD_MS=100

# Relaxed (only warn on very slow ops)
CLAUDE_CODE_SLOW_OPERATION_THRESHOLD_MS=5000
```

---

### `CLAUDE_DEBUG`

**What it does**:
```javascript
if (CLAUDE_DEBUG) {
  enableDebugLogging();
  logAllAPIRequests();
  logToolExecutions();
}
```

**Implementation**:
- Enables verbose debug output
- Logs internal state changes
- Helps troubleshoot issues

---

## MIGRATION GUIDE: 2.1.59 → 2.1.70

### Removed Variables

```bash
# ❌ REMOVED - Use CLAUDE_CODE_DISABLE_PRECOMPACT_SKIP instead
CLAUDE_CODE_SKIP_PRECOMPACT_LOAD=1

# ✅ NEW - Replacement
CLAUDE_CODE_DISABLE_PRECOMPACT_SKIP=1


# ❌ REMOVED - No replacement
CLAUDE_CODE_PROFILE_QUERY=1  # Profiling consolidated

# ❌ REMOVED - No replacement
CLAUDE_CODE_TST_NAMES_IN_MESSAGES=1  # Test-only flag
```

### Renamed Variables

```bash
# ❌ OLD
BEDROCK_BASE_URL=https://...

# ✅ NEW
ANTHROPIC_BEDROCK_BASE_URL=https://...
```

---

**Last Updated**: 2026-03-07
**Binary**: 2.1.70 (68,960 functions, 1,348,312 symbols)
**Methodology**: Direct source code analysis of extracted JS payload
