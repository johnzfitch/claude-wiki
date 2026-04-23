---
title: "Claude Code Environment Variables - Complete Guide"
category: "19-Reference"
tags: ["claude-code", "security"]
---

# Claude Code Environment Variables - Complete Guide
## 2.1.42 → 2.1.59 → 2.1.70 Evolution

**Generated**: 2026-03-07
**Binaries Analyzed**: 2.1.42, 2.1.59, 2.1.70
**Total Variables**: 418 in 2.1.70

---

## Executive Summary

### Version History

| Version | Total Env Vars | Claude-Specific | Major Features |
|---------|----------------|-----------------|----------------|
| **2.1.42** | 383 | ~260 | Base feature set |
| **2.1.59** | 404 | ~274 | Voice/audio, MCP OAuth, CCR v2 |
| **2.1.70** | 418 | ~288 | Microsoft Foundry, Remote mode, CoWork teams |

### Changes by Version

#### 2.1.42 → 2.1.59 (+14 variables, -7 removed)

**Added**:
- `CLAUDE_AUTO_BACKGROUND_TASKS` — Automatic task backgrounding
- `CLAUDE_CODE_ACCOUNT_UUID` — Account identifier (internal)
- `CLAUDE_CODE_DISABLE_1M_CONTEXT` — Disable 1M context window models
- `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` — OAuth refresh token for MCP
- `CLAUDE_CODE_OAUTH_SCOPES` — Space-separated OAuth scopes
- `CLAUDE_CODE_ORGANIZATION_UUID` — Organization identifier (internal)
- `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS` — Git timeout for plugins
- `CLAUDE_CODE_PLUGIN_USE_ZIP_CACHE` — Use ZIP cache for plugins
- `CLAUDE_CODE_REMOTE_SEND_KEEPALIVES` — Keepalive heartbeats for remote sessions
- `CLAUDE_CODE_STREAMING_TEXT` — Enable streaming text output
- `CLAUDE_CODE_USER_EMAIL` — User email override (internal)
- `CLAUDE_CODE_USE_CCR_V2` — Use CCR v2 (internal routing)
- `CLAUDE_CODE_WORKER_EPOCH` — Worker epoch identifier (internal)
- `VOICE_STREAM_BASE_URL` — Voice streaming service URL

**Removed**:
- `CLAUDE_BASH_NO_LOGIN` → Removed (shell config simplified)
- `CLAUDE_CODE_BIRTHDAY_HAT` → Removed (Easter egg)
- `CLAUDE_CODE_SESSION_ID` → Removed (consolidated)
- `CLAUDE_CODE_SNIPPET_SAVE` → Removed (feature deprecated)
- `ENABLE_EXPERIMENTAL_MCP_CLI` → Removed (now stable)
- `ENABLE_MCP_CLI` → Removed (always enabled)
- `ENABLE_MCP_CLI_ENDPOINT` → Removed (consolidated)

#### 2.1.59 → 2.1.70 (+14 variables, -3 removed)

**Added**:
- `CLAUDE_BRIDGE_USE_CCR_V2` — Bridge CCR v2 support
- `CLAUDE_CODE_ALWAYS_ENABLE_EFFORT` — Always enable effort tracking
- `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS` — Suppress git instructions in prompt
- `CLAUDE_CODE_DISABLE_LEGACY_MODEL_REMAP` — Disable model alias remapping
- `CLAUDE_CODE_DISABLE_PRECOMPACT_SKIP` — Force compaction (replaces SKIP_PRECOMPACT_LOAD)
- `CLAUDE_CODE_GB_BASE_URL` — Generic backend URL (internal)
- `CLAUDE_CODE_MCP_INSTR_DELTA` — MCP instruction delta mode
- `CLAUDE_CODE_PLUGIN_SEED_DIR` — Plugin seed directory for pre-seeded installs
- `CLAUDE_CODE_QUESTION_PREVIEW_FORMAT` — Question preview UI format
- `CLAUDE_CODE_SEARCH_HINTS_IN_LIST` — Show search hints in list view
- `CLAUDE_CODE_STALL_TIMEOUT_MS_FOR_TESTING` — Test stall timeout
- `CLAUDE_COWORK_MEMORY_PATH_OVERRIDE` — CoWork team memory path
- `CLI_WIDTH` — Terminal width override
- `VCR_RECORD` — HTTP VCR cassette recording mode

**Removed**:
- `CLAUDE_CODE_PROFILE_QUERY` → Removed (profiling consolidated)
- `CLAUDE_CODE_SKIP_PRECOMPACT_LOAD` → Replaced by CLAUDE_CODE_DISABLE_PRECOMPACT_SKIP
- `CLAUDE_CODE_TST_NAMES_IN_MESSAGES` → Removed (test-only flag)

---

## NEW FEATURES IN 2.1.70

### 1. Microsoft Foundry (3rd Enterprise Provider)

Microsoft Foundry adds Azure-hosted Claude as a third enterprise deployment option alongside AWS Bedrock and Google Vertex AI.

```bash
# Enable Microsoft Foundry
CLAUDE_CODE_USE_FOUNDRY=1

# Foundry credentials
ANTHROPIC_FOUNDRY_API_KEY=your-foundry-api-key
ANTHROPIC_FOUNDRY_BASE_URL=https://your-foundry-endpoint.azure.com
ANTHROPIC_FOUNDRY_RESOURCE=your-azure-resource-name

# Skip Azure AD authentication (for API key auth)
CLAUDE_CODE_SKIP_FOUNDRY_AUTH=1
```

**Implementation Details**:
- Uses `DefaultAzureCredential` for Azure AD authentication
- Supports all standard Azure auth methods (client secret, cert, managed identity)
- Provider routing: `firstParty`, `bedrock`, `vertex`, `foundry`
- All model slots available across all providers

**Azure Authentication Environment Variables** (see AZURE section):
- `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`, `AZURE_TENANT_ID`
- `AZURE_CLIENT_CERTIFICATE_PATH`, `AZURE_FEDERATED_TOKEN_FILE`
- `AZURE_USERNAME`, `AZURE_PASSWORD`
- Full `DefaultAzureCredential` chain supported

---

### 2. Remote Control Mode

Enables secure remote session management with automatic lifecycle controls.

```bash
# Enable remote mode (30-minute session cap, sandbox restrictions)
CLAUDE_CODE_REMOTE=1

# Remote session routing
CLAUDE_CODE_REMOTE_SESSION_ID=unique-session-id

# Remote memory directory
CLAUDE_CODE_REMOTE_MEMORY_DIR=/path/to/remote/memory

# Enable keepalive heartbeats
CLAUDE_CODE_REMOTE_SEND_KEEPALIVES=1

# Session ingress endpoint
SESSION_INGRESS_URL=https://your-ingress.example.com
```

**Restrictions in Remote Mode**:
- 30-minute session timeout enforced
- Strict sandbox mode enabled
- Auto-memory disabled unless `CLAUDE_CODE_REMOTE_MEMORY_DIR` set
- Additional security protections applied

**Use Cases**:
- CI/CD environments
- Codespaces/remote development
- Multi-tenant deployments
- Ephemeral compute instances

---

### 3. MCP OAuth Token Lifecycle

Full OAuth token lifecycle management for MCP servers with automatic refresh.

```bash
# OAuth refresh token
CLAUDE_CODE_OAUTH_REFRESH_TOKEN=your-refresh-token

# OAuth scopes (space-separated)
CLAUDE_CODE_OAUTH_SCOPES="user:inference user:mcp_servers"

# MCP OAuth configuration
MCP_CLIENT_SECRET=your-client-secret
MCP_OAUTH_CALLBACK_PORT=8080
```

**Features**:
- Automatic token refresh before expiration
- Telemetry events: `tengu_mcp_oauth_refresh_success`, `tengu_mcp_oauth_refresh_failure`, `tengu_grove_oauth_401_received`
- Per-server OAuth configuration
- `apiKeyOrOAuthToken` unified auth field

---

### 4. CoWork Team Memory

Shared memory across teammates in multi-agent teams.

```bash
# Override team memory path
CLAUDE_COWORK_MEMORY_PATH_OVERRIDE=/path/to/team/memory
```

**Implementation**:
- Each teammate has a `teammate_id` identifier
- Shared memory synced across team members
- Telemetry: `tengu_team_mem_sync_started`
- Used in agent teams (requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`)

---

### 5. Enhanced Model Configuration

#### Effort Tracking
```bash
# Always enable effort tracking (even on non-Opus models)
CLAUDE_CODE_ALWAYS_ENABLE_EFFORT=1
```

**Logic**:
- Auto-enabled for Opus 4.6
- This flag forces effort tracking on other models
- Maps to API `effort` parameter

#### Legacy Model Remapping
```bash
# Disable automatic model alias remapping (e.g., opus-3 → opus-4)
CLAUDE_CODE_DISABLE_LEGACY_MODEL_REMAP=1
```

**Purpose**: Prevent automatic upgrades to newer model versions when using legacy model names.

#### Git Instructions Control
```bash
# Suppress git commit instructions from system prompt
CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=1
```

**Effect**: Removes git workflow instructions from the system prompt (useful for non-git workflows).

---

### 6. AWS Bedrock Enhancements

```bash
# Override Bedrock endpoint (replaces BEDROCK_BASE_URL)
ANTHROPIC_BEDROCK_BASE_URL=https://your-bedrock-endpoint.amazonaws.com

# Token-based Bedrock auth (alternative to IAM)
AWS_BEARER_TOKEN_BEDROCK=your-bearer-token

# Enable 1-hour prompt caching on Bedrock
ENABLE_PROMPT_CACHING_1H_BEDROCK=1
```

**New Bedrock Capabilities** (from string analysis):
- Reranking support
- Inference profiles
- FIPS endpoints
- Guardrails integration
- Bearer token authentication (no IAM required)

---

### 7. MCP Instruction Delta Mode

```bash
# Enable MCP instruction delta mode (efficient MCP prompt updates)
CLAUDE_CODE_MCP_INSTR_DELTA=1
```

**Purpose**: Reduces prompt overhead when MCP tool definitions change by sending only deltas instead of full tool schemas.

---

### 8. UI & Terminal Enhancements

```bash
# Override terminal width (columns)
CLI_WIDTH=120

# Question preview format customization
CLAUDE_CODE_QUESTION_PREVIEW_FORMAT="custom-format-string"

# Show search hints in list view
CLAUDE_CODE_SEARCH_HINTS_IN_LIST=1
```

---

### 9. Plugin System Improvements

```bash
# Plugin seed directory (pre-seeded plugin installs)
CLAUDE_CODE_PLUGIN_SEED_DIR=/path/to/plugin/seeds

# Plugin cache directory override
CLAUDE_CODE_PLUGIN_CACHE_DIR=/path/to/plugin/cache

# Use ZIP cache for faster plugin loading
CLAUDE_CODE_PLUGIN_USE_ZIP_CACHE=1

# Git timeout for plugin operations (ms)
CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS=60000
```

---

### 10. Context Management Updates

```bash
# Force compaction (replaces CLAUDE_CODE_SKIP_PRECOMPACT_LOAD)
CLAUDE_CODE_DISABLE_PRECOMPACT_SKIP=1

# Disable 1M context window models
CLAUDE_CODE_DISABLE_1M_CONTEXT=1
```

**Note**: `CLAUDE_CODE_SKIP_PRECOMPACT_LOAD` was removed and replaced by `CLAUDE_CODE_DISABLE_PRECOMPACT_SKIP`.

---

### 11. Testing & Development

```bash
# HTTP VCR cassette recording (testing)
VCR_RECORD=all          # Record all HTTP interactions
VCR_RECORD=none         # No recording
VCR_RECORD=new_episodes # Record only new interactions

# Test stall timeout (ms)
CLAUDE_CODE_STALL_TIMEOUT_MS_FOR_TESTING=30000

# Use staging OAuth endpoints
USE_STAGING_OAUTH=1
```

---

## REMOVED VARIABLES (2.1.42 → 2.1.70)

### No Longer Functional

These variables have been removed from the binary and no longer have any effect:

```bash
# REMOVED in 2.1.59
CLAUDE_BASH_NO_LOGIN                    # Shell config simplified
CLAUDE_CODE_BIRTHDAY_HAT                # Easter egg removed
CLAUDE_CODE_SESSION_ID                  # Consolidated into other session vars
CLAUDE_CODE_SNIPPET_SAVE                # Feature deprecated
ENABLE_EXPERIMENTAL_MCP_CLI             # MCP CLI now stable, always enabled
ENABLE_MCP_CLI                          # MCP CLI now stable, always enabled
ENABLE_MCP_CLI_ENDPOINT                 # Consolidated into other MCP vars

# REMOVED in 2.1.70
CLAUDE_CODE_PROFILE_QUERY               # Profiling consolidated
CLAUDE_CODE_SKIP_PRECOMPACT_LOAD        # Replaced by CLAUDE_CODE_DISABLE_PRECOMPACT_SKIP
CLAUDE_CODE_TST_NAMES_IN_MESSAGES       # Test-only flag removed
```

---

## MODEL SLOTS (2.1.70)

### New Model Slots in 2.1.70

All new slots support 4 provider variants: `firstParty`, `bedrock`, `vertex`, `foundry`

```
sonnet45  → claude-sonnet-4-5      (NEW)
sonnet46  → claude-sonnet-4-6      (NEW)
opus41    → claude-opus-4-1        (NEW)
opus45    → claude-opus-4-5        (NEW)
opus46    → claude-opus-4-6        (NEW)
```

### Existing Slots (2.1.59+)

```
haiku35   → claude-3-5-haiku
haiku45   → claude-4-5-haiku
sonnet35  → claude-3-5-sonnet
sonnet37  → claude-3-7-sonnet
sonnet40  → claude-4-0-sonnet
opus40    → claude-4-0-opus
```

**Provider Configuration**:
```bash
CLAUDE_CODE_USE_BEDROCK=1   # Enable AWS Bedrock
CLAUDE_CODE_USE_VERTEX=1    # Enable Google Vertex AI
CLAUDE_CODE_USE_FOUNDRY=1   # Enable Microsoft Foundry
```

---

## VOICE & AUDIO (2.1.59+)

### Native Audio Capture

**New in 2.1.59**: Real-time audio capture via `audio-capture.node` (483KB C++ native addon)

```bash
# Voice streaming service URL
VOICE_STREAM_BASE_URL=https://voice-stream.example.com
```

**BunFS Artifacts**:
- `audio-capture.js` (2.6K) — Native module loader
- `audio-capture.node` (483K) — C++ addon for real-time audio capture

**Telemetry Events**:
- `transcript_share_submitted`
- `is_session_transcript`
- Voice state fields: `voiceError`, `onTranscript`

---

## CRITICAL SECURITY NOTES

### Credential Variables (NEVER commit these)

```bash
# API Keys
ANTHROPIC_API_KEY
ANTHROPIC_FOUNDRY_API_KEY
AWS_BEARER_TOKEN_BEDROCK

# OAuth Tokens
CLAUDE_CODE_OAUTH_TOKEN
CLAUDE_CODE_OAUTH_REFRESH_TOKEN
CLAUDE_CODE_SESSION_ACCESS_TOKEN

# Cloud Credentials
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_SESSION_TOKEN
AZURE_CLIENT_SECRET
AZURE_PASSWORD
GOOGLE_APPLICATION_CREDENTIALS

# MCP
MCP_CLIENT_SECRET
```

### Privacy-Sensitive Variables

```bash
# Telemetry (can log user data if enabled)
OTEL_LOG_USER_PROMPTS=1          # WARNING: Logs prompts to OTel
OTEL_LOG_TOOL_CONTENT=1          # Logs tool inputs/outputs
OTEL_LOG_TOOL_DETAILS=1          # Logs tool details

# Account Identifiers (PII)
CLAUDE_CODE_ACCOUNT_UUID
CLAUDE_CODE_USER_EMAIL
CLAUDE_CODE_ORGANIZATION_UUID
```

### Dangerous Settings

```bash
# Disable security checks (NOT RECOMMENDED)
CLAUDE_CODE_DISABLE_COMMAND_INJECTION_CHECK=1  # ⚠️ Security risk
NODE_TLS_REJECT_UNAUTHORIZED=0                 # ⚠️ Disables TLS verification
```

---

## BEST PRACTICES

### Production Deployments

```bash
# Disable non-essential traffic
CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1

# Disable telemetry
DISABLE_TELEMETRY=1
DISABLE_ERROR_REPORTING=1

# Disable auto-updates
DISABLE_AUTOUPDATER=1

# Set explicit timeouts
API_TIMEOUT_MS=30000
MCP_TIMEOUT=30000
MCP_TOOL_TIMEOUT=120000
```

### CI/CD Environments

```bash
# Remote mode (30-min session cap)
CLAUDE_CODE_REMOTE=1

# Non-interactive mode
CLAUDE_CODE_EXIT_AFTER_STOP_DELAY=5000

# Disable UI features
CLAUDE_CODE_DISABLE_TERMINAL_TITLE=1
CLAUDE_CODE_SIMPLE=1

# Fast compaction
CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80
```

### Multi-Tenant / Shared Environments

```bash
# Sandbox mode
IS_SANDBOX=1
CLAUDE_CODE_BUBBLEWRAP=1

# Disable memory
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1

# Separate config per tenant
CLAUDE_CONFIG_DIR=/path/to/tenant-specific/config

# Unique session IDs
CLAUDE_CODE_REMOTE_SESSION_ID=tenant-${TENANT_ID}-${SESSION_ID}
```

### Enterprise (Foundry/Bedrock/Vertex)

```bash
# Use Foundry
CLAUDE_CODE_USE_FOUNDRY=1
ANTHROPIC_FOUNDRY_BASE_URL=https://your-foundry.azure.com
CLAUDE_CODE_SKIP_FOUNDRY_AUTH=1  # If using API key instead of Azure AD

# OR use Bedrock
CLAUDE_CODE_USE_BEDROCK=1
AWS_REGION=us-west-2
ANTHROPIC_BEDROCK_BASE_URL=https://bedrock-runtime.us-west-2.amazonaws.com

# OR use Vertex
CLAUDE_CODE_USE_VERTEX=1
ANTHROPIC_VERTEX_PROJECT_ID=your-gcp-project
GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
```

---

## COMPATIBILITY MATRIX

| Variable | 2.1.42 | 2.1.59 | 2.1.70 | Notes |
|----------|--------|--------|--------|-------|
| `ANTHROPIC_FOUNDRY_*` | ❌ | ❌ | ✅ | New in 2.1.70 |
| `CLAUDE_CODE_REMOTE` | ❌ | ✅ | ✅ | New in 2.1.59 |
| `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` | ❌ | ✅ | ✅ | New in 2.1.59 |
| `VOICE_STREAM_BASE_URL` | ❌ | ✅ | ✅ | New in 2.1.59 |
| `CLAUDE_COWORK_MEMORY_PATH_OVERRIDE` | ❌ | ❌ | ✅ | New in 2.1.70 |
| `CLAUDE_CODE_SKIP_PRECOMPACT_LOAD` | ✅ | ✅ | ❌ | Removed in 2.1.70 |
| `CLAUDE_CODE_SESSION_ID` | ✅ | ❌ | ❌ | Removed in 2.1.59 |
| `ENABLE_EXPERIMENTAL_MCP_CLI` | ✅ | ❌ | ❌ | Removed in 2.1.59 |

---

## REFERENCE FILES

- **Full env file**: `2.1.70/claude.env` — All 418 variables with inline documentation
- **Phase 2 report**: `2.1.70/reports/p2-string-labeling.md` — String analysis methodology
- **Delta report**: `2.1.70/reports/DELTA.md` — Complete 2.1.59 → 2.1.70 delta

---

## APPENDIX: DETECTION LOGIC

The binary checks many environment variables for auto-detection purposes. These are read-only checks and not configuration options:

### CI/CD Detection
`BUILDKITE`, `CIRCLECI`, `GITHUB_ACTIONS`, `GITLAB_CI`, `CODESPACES`

### Cloud Environment Detection
`AWS_LAMBDA_FUNCTION_NAME`, `GOOGLE_CLOUD_PROJECT`, `AZURE_FUNCTIONS_ENVIRONMENT`
`FLY_APP_NAME`, `DENO_DEPLOYMENT_ID`, `VERCEL`, `NETLIFY`, `RENDER`

### Terminal Detection
`TERM`, `TERM_PROGRAM`, `TMUX`, `STY`, `ALACRITTY_LOG`, `KITTY_WINDOW_ID`
`ITERM_SESSION_ID`, `GNOME_TERMINAL_SERVICE`, `VTE_VERSION`, `WT_SESSION`

These variables are **not configuration options** — they are detected by the binary to adjust behavior automatically.

---

**Last Updated**: 2026-03-07
**Binary Version**: 2.1.70 (Bun 1.3.11, 68,960 functions, 1,348,312 symbols)
