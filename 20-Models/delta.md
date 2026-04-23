---
title: "DELTA: Claude Code 2.1.59 → 2.1.70"
category: "20-Models"
tags: ["claude-code"]
---

# DELTA: Claude Code 2.1.59 → 2.1.70

**Analysis date:** 2026-03-06
**Reference:** 2.1.59 (`7a4a653982b07e0a`) → 2.1.70 (`1e5c1011ec899ef0`)

---

## Executive Summary

Claude Code 2.1.70 is the most significant release since the voice/audio addition in 2.1.59.
The binary grew by **12 MB** (218 → 230 MB), with **+8,660 new functions** (+14.4%), driven
by major new enterprise platform integrations, a new remote control system, expanded model
routing, and enhanced audio/voice infrastructure.

| Metric | 2.1.59 | 2.1.70 | Delta |
|--------|--------|--------|-------|
| Functions | 60,300 | 68,960 | **+8,660** |
| Binary size | 218 MB | 230 MB | +12 MB |
| `.text` | 60.9 MB | 65.2 MB | +4.3 MB |
| `.rodata` | 41.7 MB | 43.2 MB | +1.5 MB |
| JS payload lines | 11,832 | 13,026 | **+1,194** |
| ELF sections | 39 | 44 | +5 |
| Bun version | 1.3.10 | 1.3.11 | patch |
| New env vars | — | — | **+27** |
| New model slots | — | — | **+5** |

---

## New Features

### 1. Microsoft Foundry Provider (Enterprise — NEW)

A third enterprise provider added alongside AWS Bedrock and Google Vertex AI.

- **Provider:** Azure-hosted Claude via Microsoft Foundry
- **Auth:** `DefaultAzureCredential` (Azure AD / Entra ID)
- **Env vars:** `CLAUDE_CODE_USE_FOUNDRY`, `ANTHROPIC_FOUNDRY_API_KEY`, `ANTHROPIC_FOUNDRY_BASE_URL`, `ANTHROPIC_FOUNDRY_RESOURCE`
- **Skip auth:** `CLAUDE_CODE_SKIP_FOUNDRY_AUTH`
- **Client class:** `FoundryClient` extending base Anthropic client
- **Fast mode:** Unavailable on Foundry (same as Bedrock/Vertex)
- Telemetry/feedback/bug reporting disabled when Foundry active

### 2. Remote Control Mode (NEW)

A new operational mode that exposes the Claude CLI session via a network interface.

- **Env var:** `CLAUDE_CODE_REMOTE`
- **Session ID:** `CLAUDE_CODE_REMOTE_SESSION_ID` / `SESSION_INGRESS_*`
- **Time limit:** 30-minute session cap enforced
- **Restrictions:** `acceptEdits` and `plan` only in remote mode; destructive tools blocked
- **Memory:** `CLAUDE_CODE_REMOTE_MEMORY_DIR` — separate memory dir for remote sessions
- **Keepalives:** `CLAUDE_CODE_REMOTE_SEND_KEEPALIVES`
- **Sandbox:** "Strict sandbox mode" messaging for remote sessions
- **GitHub:** Forces HTTPS clone URL in remote mode (vs SSH locally)

### 3. Audio Capture Native Module (Voice — EXPANDED)

New BunFS artifact `audio-capture.node` (483 KB native C++ addon) added.

- **File:** `audio-capture.node` — real-time audio capture
- **Loader:** `audio-capture.js` — BunFS loader stub
- **State:** `voiceError` field in voice session state
- **Callbacks:** `onTranscript` — streaming transcription events
- **Telemetry:** `transcript_share_submitted`, `is_session_transcript`
- Previously the voice module may have used a different capture path; native capture is now a dedicated first-class artifact

### 4. MCP OAuth Token Manager (Auth — NEW)

Full OAuth lifecycle management for MCP servers.

- OAuth authentication, 401 handling, token refresh
- Telemetry events: `tengu_grove_oauth_401_received`, `tengu_mcp_oauth_refresh_failure`, `tengu_mcp_oauth_refresh_success`
- Cleanup on shutdown: "MCP OAuth server cleaned up"
- `apiKeyOrOAuthToken` — unified auth field (API key OR OAuth token)

### 5. Team CoWork Memory Sync (Teams — NEW)

Team collaboration feature with shared memory.

- `teammate_id` — team member identification
- `tengu_team_mem_sync_started` — sync telemetry
- `CLAUDE_COWORK_MEMORY_PATH_OVERRIDE` — override shared memory location
- Enables shared context across team sessions

### 6. Max Output Token Recovery (Worker — NEW)

Auto-retry when max output tokens is reached mid-turn.

- New transition reason: `max_output_tokens_recovery`
- Increments attempt counter and continues the turn loop
- Prevents hard failures on long-output tasks

### 7. AWS Bedrock Expanded

Major expansion of Bedrock capabilities beyond the existing integration:

| New Capability | Detail |
|---------------|--------|
| Reranking model | `BEDROCK_RERANKING_MODEL`, `VectorSearchBedrockRerankingConfiguration` |
| Inference profiles | `ListInferenceProfilesCommand`, `GetInferenceProfileCommand` |
| FIPS endpoints | `https://bedrock-fips.{Region}.{PartitionResult#dnsSuffix}` |
| Guardrails | `X-Amzn-Bedrock-GuardrailIdentifier`, `X-Amzn-Bedrock-GuardrailVersion` |
| Service tier | `X-Amzn-Bedrock-Service-Tier` header |
| Prompt routers | `paginateListPromptRouters` |
| Provisioned throughput | `paginateListProvisionedModelThroughputs` |
| Bearer token auth | `AWS_BEARER_TOKEN_BEDROCK` (simpler auth for dev) |

---

## Model Routing Changes

### New Model Slots (Claude 4.x family)

| New Slot | Maps to | Providers |
|----------|---------|-----------|
| `sonnet45` | claude-sonnet-4-5 | firstParty, bedrock, vertex, foundry |
| `sonnet46` | claude-sonnet-4-6 | firstParty, bedrock, vertex, foundry |
| `opus41` | claude-opus-4-1 | firstParty, bedrock, vertex, foundry |
| `opus45` | claude-opus-4-5 | firstParty, bedrock, vertex, foundry |
| `opus46` | claude-opus-4-6 | firstParty, bedrock, vertex, foundry |

Full model table now: `haiku35`, `haiku45`, `sonnet35`, `sonnet37`, `sonnet40`,
`sonnet45`, `sonnet46`, `opus40`, `opus41`, `opus45`, `opus46`.

### New Model Behavior Flags

| Env Var | Effect |
|---------|--------|
| `CLAUDE_CODE_DISABLE_LEGACY_MODEL_REMAP` | Disable auto-remapping of old model IDs |
| `CLAUDE_CODE_ALWAYS_ENABLE_EFFORT` | Force effort tracking on all models |

---

## Runtime Changes

### ELF Structural Changes

| Change | Detail |
|--------|--------|
| +5 new sections | `.gcc_except_table`, `.debug_gdb_scripts`, `.eh_frame_hdr`, `.eh_frame`, `.iplt` |
| Exception handling | 1.85 MB of new C++ exception tables — enabled for first time |
| Debug flag | `has_debug: true` (via `.debug_gdb_scripts` + eh_frame presence) |
| Init array | +7 new static initializers at startup |
| GOT doubled | `.got` grew from 6.8KB to 14.2KB — many new dynamic symbol resolutions |

### Bun Upgrade: 1.3.10 → 1.3.11

Patch-level upgrade. Same JavaScriptCore engine, same Rust crate versions, same crate
registry hash. No breaking changes expected.

---

## Subsystem Impact Summary

| Subsystem | Status | Evidence strength |
|-----------|--------|------------------|
| model-routing | Major expansion | High (new providers + 5 model slots) |
| auth | New OAuth system | High (string evidence) |
| session | New remote mode | High (string + env var evidence) |
| voice | Native audio module | High (binary artifact) |
| worker | Token recovery | High (string evidence) |
| mcp | OAuth lifecycle | High (string evidence) |
| runtime | Bun upgrade + exceptions | High (section analysis) |
| telemetry | New events | High (tengu_* strings) |
| team | CoWork memory | High (string evidence) |

---

## New Environment Variables (27 total)

See [p2-string-labeling.md](p2-string-labeling.md) for full table with descriptions.

Key additions by category:
- **Provider control:** `CLAUDE_CODE_USE_FOUNDRY`, `ANTHROPIC_FOUNDRY_*` (4 vars)
- **Remote mode:** `CLAUDE_CODE_REMOTE*` (4 vars)
- **Bedrock auth:** `CLAUDE_CODE_SKIP_BEDROCK_AUTH`, `AWS_BEARER_TOKEN_BEDROCK`
- **Model control:** `CLAUDE_CODE_DISABLE_LEGACY_MODEL_REMAP`, `CLAUDE_CODE_ALWAYS_ENABLE_EFFORT`
- **Dev/Test:** `VCR_RECORD`, `CLAUBBIT`, `CLAUDE_CODE_STALL_TIMEOUT_MS_FOR_TESTING`
- **Features:** `CLAUDE_COWORK_MEMORY_PATH_OVERRIDE`, `CLAUDE_CODE_PLUGIN_SEED_DIR`, `CLAUDE_CODE_MCP_INSTR_DELTA`

---

## Phase Reports

| Phase | Report | Status |
|-------|--------|--------|
| P1: Symbol diff | [p1-symbol-diff.md](p1-symbol-diff.md) | Complete |
| P2: String labeling | [p2-string-labeling.md](p2-string-labeling.md) | Complete |
| P3: Structural clustering | (skipped — fast-profile only) | N/A |
| P4: Decompile targets | (skipped — fast-profile only) | N/A |
| P5: Runtime analysis | [p5-runtime.md](p5-runtime.md) | Complete |
| P6: Graph index | [index.json](index.json) | Complete |

### Phase 3/4 Notes

Structural clustering and decompile phases require a fully-analyzed binary (complete profile).
The fast-profile binaries (`2.1.59-7a4a6539`, `2.1.70-1e5c1011`) do not enumerate functions
via Ghidra analysis. To proceed with Phases 3/4:
- Re-import 2.1.70 with `analyze_binary` (estimated 60-90 min for 68,960 functions)
- Then use `list_functions(sort_by="refs_in")` to identify hot-path functions
- Use `batch_decompile` on top-N `no-callers` functions

---

## Key Open Questions

1. **Remote Control protocol**: What transport does remote mode use? TCP socket? HTTP/SSE? Unix socket?
2. **Foundry model names**: What are the exact model IDs for Foundry-hosted Claude endpoints?
3. **Audio capture format**: PCM? Opus? What sample rate? Who transcribes (local vs API)?
4. **Team memory format**: Is `CLAUDE_COWORK_MEMORY_PATH_OVERRIDE` a directory of MEMORY.md files?
5. **`.gcc_except_table`**: Which new C++ classes trigger exceptions? Audio capture? Foundry client?

---

*Analysis method: BunFS extraction + JS payload diff + .rodata string scan + ELF section analysis*
*Fast-profile binary: function-level addresses not available without full Ghidra analysis*
