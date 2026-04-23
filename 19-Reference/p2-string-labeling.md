---
title: "Phase 2 — String-Based Labeling: 2.1.59 → 2.1.70"
category: "19-Reference"
---

# Phase 2 — String-Based Labeling: 2.1.59 → 2.1.70

**Logs:** [../logs/p2a-batch_search_strings.json](../logs/p2a-batch_search_strings.json)

## Method

`batch_search_strings` timed out on fast-profile binaries (>60s). String analysis was
performed via two complementary methods:

1. **`.rodata` deep scan** — `search_strings_deep` on the native binary `.rodata` section
   (43.2MB in 2.1.70). Covers Bun runtime strings, Rust crate paths, engine internals.

2. **BunFS JS payload diff** — extracted `cli.js` from both versions and performed:
   - Line-level unified diff (6,882 added / 5,688 removed raw diff lines)
   - Unique string literal extraction: 37,734 new strings in 2.1.70 vs 36,244 removed
   - Identifier frequency analysis on new lines
   - Environment variable enumeration (new: 27 new `process.env.*` references)

## Runtime Version Delta

| Property | 2.1.59 | 2.1.70 |
|----------|--------|--------|
| Bun version | 1.3.10 | **1.3.11** |
| Source | `.rodata:0x0033a115` | `.rodata:0x003caa3e` |
| JS payload lines | 11,832 | **13,026** (+1,194) |

## New BunFS Artifacts (net-new in 2.1.70)

| File | Size | Role |
|------|------|------|
| `audio-capture.js` | 2.6K | Native module loader |
| `audio-capture.node` | **483K** | **NEW**: Real-time audio capture (C++ native addon) |

All other artifacts unchanged between versions (same SHA: color-diff, file-index,
image-processor, resvg, ripgrep, tree-sitter, tree-sitter-bash).

## New Provider: Microsoft Foundry

A third enterprise provider added alongside AWS Bedrock and Google Vertex AI:

| Property | Value |
|----------|-------|
| Provider name | Microsoft Foundry (Azure-hosted Claude) |
| Env var | `CLAUDE_CODE_USE_FOUNDRY` |
| API key | `ANTHROPIC_FOUNDRY_API_KEY` |
| Base URL | `ANTHROPIC_FOUNDRY_BASE_URL` |
| Auth | `DefaultAzureCredential` (Azure AD) |
| Client class | `FoundryClient` (extends base Anthropic client) |
| Skip auth | `CLAUDE_CODE_SKIP_FOUNDRY_AUTH` |

## New Model Routing Slots

| Slot | 2.1.59 | 2.1.70 |
|------|--------|--------|
| haiku35 | ✓ | ✓ |
| haiku45 | ✓ | ✓ |
| sonnet35 | ✓ | ✓ |
| sonnet37 | ✓ | ✓ |
| sonnet40 | ✓ | ✓ |
| sonnet45 | — | **NEW** |
| sonnet46 | — | **NEW** |
| opus40 | ✓ | ✓ |
| opus41 | — | **NEW** |
| opus45 | — | **NEW** |
| opus46 | — | **NEW** |

Note: Each slot maps to 4 provider variants: `firstParty`, `bedrock`, `vertex`, `foundry`.

## New Environment Variables (27 new)

### Provider Control
| Var | Purpose |
|-----|---------|
| `CLAUDE_CODE_USE_FOUNDRY` | Enable Microsoft Foundry provider |
| `ANTHROPIC_FOUNDRY_API_KEY` | Foundry API key |
| `ANTHROPIC_FOUNDRY_BASE_URL` | Foundry endpoint |
| `ANTHROPIC_FOUNDRY_RESOURCE` | Azure resource name |
| `ANTHROPIC_BEDROCK_BASE_URL` | Custom Bedrock endpoint |
| `CLAUDE_CODE_SKIP_BEDROCK_AUTH` | Skip Bedrock auth |
| `CLAUDE_CODE_SKIP_FOUNDRY_AUTH` | Skip Foundry auth |
| `AWS_BEARER_TOKEN_BEDROCK` | Token-based Bedrock auth |

### Remote Control
| Var | Purpose |
|-----|---------|
| `CLAUDE_CODE_REMOTE` | Enable remote control mode |
| `CLAUDE_CODE_REMOTE_SESSION_ID` | Remote session identifier |
| `CLAUDE_CODE_REMOTE_MEMORY_DIR` | Remote memory directory |
| `CLAUDE_CODE_REMOTE_SEND_KEEPALIVES` | Enable keepalive heartbeats |

### Model & Behavior
| Var | Purpose |
|-----|---------|
| `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS` | Suppress git instructions in prompt |
| `CLAUDE_CODE_DISABLE_LEGACY_MODEL_REMAP` | Disable model alias remapping |
| `CLAUDE_CODE_DISABLE_PRECOMPACT_SKIP` | Force compaction |
| `CLAUDE_CODE_ALWAYS_ENABLE_EFFORT` | Always enable effort tracking |
| `CLAUDE_CODE_GB_BASE_URL` | Generic/global backend URL |
| `CLAUDE_CODE_MCP_INSTR_DELTA` | MCP instruction delta mode |

### Features
| Var | Purpose |
|-----|---------|
| `CLAUDE_CODE_PLUGIN_SEED_DIR` | Plugin seed directory |
| `CLAUDE_CODE_QUESTION_PREVIEW_FORMAT` | Question preview format |
| `CLAUDE_CODE_SEARCH_HINTS_IN_LIST` | Show search hints in list view |
| `CLAUDE_CODE_STALL_TIMEOUT_MS_FOR_TESTING` | Test stall timeout |
| `CLAUDE_COWORK_MEMORY_PATH_OVERRIDE` | CoWork team memory path |
| `CLI_WIDTH` | Terminal width override |
| `VCR_RECORD` | HTTP VCR cassette recording (test) |
| `CLAUBBIT` | Internal dev mode flag |
| `SESSION_INGRESS_*` | Remote session ingress config |

## Subsystem String Evidence

### Auth/Identity (`confidence: high`)
- `OAuth authentication failed` — MCP OAuth error handler (new)
- `MCP OAuth server cleaned up` — MCP OAuth lifecycle (new)
- `tengu_grove_oauth_401_received` — telemetry event (new)
- `tengu_mcp_oauth_refresh_failure` / `tengu_mcp_oauth_refresh_success` — token refresh (new)
- `apiKeyOrOAuthToken` — unified auth token field (new)

### Remote Session (`confidence: high`)
- `remote session returned an error` — error handler string (new)
- `remote session exceeded 30 minutes` — session limit enforcement (new)
- `is_claude_code_remote` — session metadata field (new)
- `CLAUDE_CODE_REMOTE_SESSION_ID` / `SESSION_INGRESS_` — remote routing (new)
- `remoteControlAtStartup` — startup config (new)
- `Strict sandbox mode ${_}` — sandbox constraint messaging (new)

### Voice/Audio (`confidence: high`)
- `audio-capture.node` — native audio capture module (net-new binary artifact)
- `voiceError` — voice state error field (new)
- `onTranscript` — transcript callback (new)
- `transcript_share_submitted` — telemetry for transcript sharing (new)
- `is_session_transcript` — session type flag (new)

### Team/CoWork (`confidence: high`)
- `tengu_team_mem_sync_started` — team memory sync telemetry (new)
- `teammate_id` — team member identifier (new)
- `CLAUDE_COWORK_MEMORY_PATH_OVERRIDE` — shared memory path (new)

### Model Recovery (`confidence: high`)
- `max_output_tokens_recovery` — auto-retry on output token exhaustion (new)

---
*Generated: 2026-03-06 | Reference: 2.1.59 → 2.1.70 | Method: JS payload diff + .rodata scan*
