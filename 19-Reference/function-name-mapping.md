---
title: "2.1.74 Minified Function Name Mapping"
category: "19-Reference"
tags: ["security"]
---

# 2.1.74 Minified Function Name Mapping

**Quick reference for reverse engineering the Claude Code 2.1.74 JavaScript payload.**

## Core Infrastructure

| Minified | Real Name | Purpose | Category |
|----------|-----------|---------|----------|
| `SDH()` | `dispatchAnthropicRequest` | Routes API calls to Unix socket or HTTP proxy | Network |
| `jO()` | `validateUnixSocketAuth` | Enforces OAuth-only auth when socket mode active | Auth |
| `AoH()` | `stripCredentialsFromEnv` | Removes auth vars from subprocess environments | Security |
| `XA()` | `getFeatureFlag` | Reads tengu_* feature flags | Config |
| `tH()` | `parseBoolEnv` | Parses boolean environment variables | Config |
| `WL()` | `getSettings` | Reads settings.json | Config |
| `ZN()` | `getHttpProxy` | Reads HTTP_PROXY/HTTPS_PROXY env vars | Network |

## Hawthorn Budget System (Message-level tool result management)

| Minified | Real Name | Purpose | Category |
|----------|-----------|---------|----------|
| `Hb1()` | `getHawthornWindowSize` | Returns tool result budget per message | Budget |
| `MnD()` | `persistOversizedToolResult` | Saves large results to disk, returns stub | Budget |
| `BM$()` | `getHawthornReductionStrategy` | Returns "trim", "cut", or "cap" | Budget |
| `VGA()` | `persistAndReplaceToolResult` | Core persistence function | Budget |
| `_nD()` | `createHawthornTracker` | Returns new `{seenIds, replacements}` object | Budget |
| `$nD` | `DEFAULT_HAWTHORN_WINDOW` | Default budget constant (likely 150K+ chars) | Budget |
| `AnD` | `PERSISTED_RESULT_PREFIX` | Prefix for persisted result IDs | Budget |

## Plugin Marketplace

| Minified | Real Name | Purpose | Category |
|----------|-----------|---------|----------|
| `T6H()` | `isMarketplaceEnabled` | Checks tengu_orchid_trellis flag | Plugins |
| `Bff()` | `resolvePluginDependencies` | Validates dependency tree, detects cycles | Plugins |
| `yK()` | `getPluginMetadata` | Returns plugin info including marketplace | Plugins |

## Bash Security Classifier

| Minified | Real Name | Purpose | Category |
|----------|-----------|---------|----------|
| `ZQ()` | `classifyBashCommand` | Main security classifier (not fully traced) | Security |
| `VG6()` | `parseTimeoutFlags` | Validates timeout command flags | Security |
| `v58()` | `validateCommandChain` | Checks entire command including wrappers | Security |
| `oSf` | `TIMEOUT_ARG_REGEX` | Regex for timeout duration/signal args | Security |

## Other Tengu Features

| Minified | Real Name | Purpose | Category |
|----------|-----------|---------|----------|
| `Cs6()` | `mergeChatMessages` | Message merging (tengu_chair_sermon) | Chat |
| `s6H()` | `detectContentPattern` | Pattern detection v2 (tengu_marble_whisper2) | Safety |
| `hzf()` | `applyContentRegex` | Applies regex d96 for pattern matching | Safety |
| `kE6()` | `reportAutoModeState` | Reports in experiment_gates notification | Telemetry |
| `fnD()` | `handleEmptyToolResult` | Replaces empty results with message | Tools |

## Voice & Audio (Partial)

| Minified | Real Name | Purpose | Category |
|----------|-----------|---------|----------|
| *(voice loop)* | `retryVoiceStreamEarly` | 250ms retry on pre-transcript failure | Voice |
| *(voice loop)* | `reportRecordingCompleted` | Telemetry on recording completion | Voice |

## Feature Flag Reference

### Hawthorn Budget System
- `tengu_hawthorn_window` (number) — Tool result budget per message in characters
- `tengu_hawthorn_steeple` (boolean) — Enable persistence system
- `tengu_pewter_ledger` (string) — Reduction strategy: "trim" | "cut" | "cap"

### Plugin Marketplace
- `tengu_orchid_trellis` (boolean) — Enable MCP plugin marketplace

### Message & Content
- `tengu_chair_sermon` (unknown) — Message merging behavior
- `tengu_marble_whisper2` (unknown) — Content pattern detection v2
- `tengu_auto_mode_state` (boolean) — Report auto mode in telemetry
- `tengu_tool_empty_result` (boolean) — Replace empty results with message

### Voice
- `tengu_voice_stream_early_retry` (boolean) — Enable 250ms retry on stream failure
- `tengu_voice_recording_completed` (boolean) — Enable recording completion telemetry

### Planning (from earlier versions)
- `tengu_plan_mode_interview_phase` (boolean) — Plan mode interview phase
- `tengu_amber_flint` (boolean) — Agent teams feature

## Constants

| Minified | Likely Value | Purpose |
|----------|--------------|---------|
| `$nD` | ~150000 | Default Hawthorn window size (characters) |
| `NA_` | 1000 | Some timeout or interval (milliseconds) |
| `xz8` | 32 | Buffer size or chunk count |
| `bA_` | 80 | Column width or line length |

## Helper Function Patterns

| Pattern | Purpose | Example |
|---------|---------|---------|
| `*H()` | State getters | `Hb1()`, `T6H()` |
| `*$()` | Utilities/transformers | `BM$()`, `XA$()` |
| `*9$()` | SDK/external integrations | `u9$` (AWS SDK errors) |
| `*nD` | Constants | `$nD`, `_nD()` |
| `*GA()` | Core operations | `VGA()`, `NGA()` |

## Telemetry Events

| Event Name | Trigger | Category |
|------------|---------|----------|
| `tengu_tool_result_persisted_message_budget` | Individual tool result persisted | Hawthorn |
| `tengu_message_level_tool_result_budget_enforced` | Budget enforcement activated | Hawthorn |
| `tengu_grove_oauth_*` | OAuth lifecycle events | Auth |
| `experiment_gates` | Feature flag snapshot (includes auto mode) | Config |

## Network Architecture

### Unix Socket Mode Flow
```
┌─────────────────┐
│   SDH()         │ → Check ANTHROPIC_UNIX_SOCKET
└────────┬────────┘
         │
         ├─ Set? → { unix: "/path/to/socket" }
         │         (Bun native fetch routes to socket)
         │
         ├─ HTTP proxy? → { proxy: "http://..." }
         │
         └─ None → { } (standard HTTPS)

┌─────────────────┐
│   jO()          │ → Validate auth method
└────────┬────────┘
         │
         └─ Unix socket mode?
            └─ Require CLAUDE_CODE_OAUTH_TOKEN
            └─ Block API keys

┌─────────────────┐
│   AoH()         │ → Strip credentials from subprocess env
└────────┬────────┘
         │
         └─ Remove: ANTHROPIC_UNIX_SOCKET
                    ANTHROPIC_API_KEY
                    ANTHROPIC_AUTH_TOKEN
                    CLAUDE_CODE_OAUTH_TOKEN
            Preserve: All other env vars
```

## Source Locations (Approximate)

**File**: `2.1.74_bunfs_extracted/src/entrypoints/cli.js` (13,675 lines, single-line minified)

| Function | Line (approx) | Context |
|----------|---------------|---------|
| `SDH()` | 170 | HTTP client setup |
| `jO()` | 6825 | Auth validation |
| `AoH()` | 6915 | Subprocess spawn |
| `Hb1()`, `MnD()`, `BM$()` | Unknown | Chat message processing |
| `T6H()`, `Bff()` | Unknown | Plugin system |
| `VG6()`, `v58()` | Unknown | Bash security |

**Note**: Line numbers are approximate due to minification. Use pattern search for precise location.

## Extraction Commands

```bash
# Find ANTHROPIC_UNIX_SOCKET usage
python3 extract_functions_2174.py | grep -A20 "ANTHROPIC_UNIX_SOCKET"

# Find Hawthorn system
grep -o 'function [A-Za-z0-9_$]*.*tengu_hawthorn' 2.1.74_bunfs_extracted/src/entrypoints/cli.js

# Find all tengu flags
grep -oE 'tengu_[a-z_]+' 2.1.74_bunfs_extracted/src/entrypoints/cli.js | sort -u

# Extract function around line N
sed -n 'N,N+100p' 2.1.74_bunfs_extracted/src/entrypoints/cli.js | sed 's/;/;\n/g'
```

## pyghidra-lite Analysis

**Binary**: `2.1.74` (unit_id: `e5613610deee76cd`)
- **Fast profile**: 36,365 functions
- **Deep profile**: 68,720 functions

**ELF Imports**: Standard libc only (no custom IPC, networking, or security libraries)

**Native Functions**: All JavaScript function names (`SDH`, `jO`, `AoH`, etc.) are **embedded in the .rodata section** as part of the Bun-compiled JavaScript payload. They are not ELF symbols.

**To analyze native code**: Search for C++ Bun runtime functions, not JS function names.

---

**Last Updated**: 2026-03-13
**Tools Used**: pyghidra-lite, pattern extraction, manual JS analysis
