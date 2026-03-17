# Claude Code 2.1.76 — Complete Telemetry & Observability Report (v2)

## Executive Summary

Claude Code 2.1.76 has **six distinct telemetry surfaces**, not just OTEL. The first report missed three significant ones. This is the corrected, exhaustive enumeration.

| # | Surface | Backend | Gate | User-accessible? |
|---|---------|---------|------|-------------------|
| 1 | **OpenTelemetry** (traces/metrics/logs) | User-configured OTLP endpoint | `CLAUDE_CODE_ENABLE_TELEMETRY` | Yes |
| 2 | **1P Event Logging** (Anthropic internal) | OTEL LoggerProvider → Anthropic pipeline | `is1PEventLoggingEnabled()` | Partially (via OTEL export) |
| 3 | **Segment.io Analytics** | `api.segment.io/v1/batch` | `tengu_log_segment_events` Statsig gate | No (hardcoded write key) |
| 4 | **DataDog Logs** | `https://http-intake.logs.us5.datadoghq.com/api/v2/logs` | `tengu_log_datadog_events` Statsig gate | No (hardcoded API key) |
| 5 | **Perfetto Tracing** | Local `.pftrace` file | `CLAUDE_CODE_PERFETTO_TRACE` env var | Yes |
| 6 | **Beta Tracing** (detailed OTEL) | `BETA_TRACING_ENDPOINT` | `ENABLE_BETA_TRACING_DETAILED` + `tengu_trace_lantern` | Yes (if you set the env vars) |

Plus:
- **Local debug logging** (`CLAUDE_CODE_DEBUG_LOGS_DIR`)
- **Startup performance profiling** (`perf_hooks` marks)
- **Headless profiler** (SDK/headless latency metrics)
- **Process metrics** (RSS, heap, CPU, sent with events)
- **Attribution header** (billing metadata on every API call)
- **Heap dump tool** (built-in `/heapdump` command)
- **Error reporting** (ring buffer, `logError`/`logMCPError`/`logMCPDebug`, `DISABLE_ERROR_REPORTING`)
- **Grove privacy system** (data retention toggle, `grove_enabled` API)
- **Auto-mode security classifier** (separate LLM call for tool safety)
- **Speculation system** (speculative tool execution telemetry)
- **Post-sampling hooks** (`Zif()` fires after each LLM call)
- **Cost tracking** (`total_cost_usd`, threshold warnings)
- **Feedback & bug reports** (survey, accept/reject, bug submission)
- **Enterprise OTEL auth** (`otelHeadersHelper` dynamic token script)

---

## 1. OpenTelemetry (OTEL) — User-Facing Telemetry

### Architecture
- **SDK**: Full `@opentelemetry/sdk-node` (traces, metrics, logs)
- **Exporters**: `OTLPTraceExporter`, `OTLPMetricExporter`, `OTLPLogExporter`
- **Processor**: `BatchSpanProcessor` (configurable)
- **Tracer name**: `com.anthropic.claude_code.tracing` v1.0.0
- **Service name**: `claude-code`
- **Init function**: `xX6()` — called during startup

### Master Enable/Disable

```
CLAUDE_CODE_ENABLE_TELEMETRY=true   → enables 3P OTEL export to your endpoint
DISABLE_TELEMETRY=true              → kills ALL non-essential telemetry (Segment, DD, 1P, OTEL)
CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=true → same as DISABLE_TELEMETRY
```

**Bedrock/Vertex/Foundry users**: Telemetry is **automatically disabled** via `GN()`:
```javascript
function GN() {
  return CLAUDE_CODE_USE_BEDROCK || CLAUDE_CODE_USE_VERTEX ||
         CLAUDE_CODE_USE_FOUNDRY || DISABLE_TELEMETRY ||
         CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC;
}
```

### Span Hierarchy

```
claude_code.interaction          ← top-level user turn
├── claude_code.llm_request      ← API call to Claude
├── claude_code.tool             ← tool invocation
│   ├── claude_code.tool.blocked_on_user  ← permission prompt
│   └── claude_code.tool.execution        ← actual execution
└── claude_code.hook             ← hook system call
```

### Span Attributes (Complete)

#### `claude_code.interaction`
| Attribute | Type | Notes |
|-----------|------|-------|
| `span.type` | "interaction" | constant |
| `user_prompt` | string | **REDACTED** unless `OTEL_LOG_USER_PROMPTS=true` |
| `user_prompt_length` | int | always present |
| `interaction.sequence` | int | incremental counter per session |
| `interaction.duration_ms` | int | set on span end |

#### `claude_code.llm_request`
| Attribute | Type | Notes |
|-----------|------|-------|
| `model` | string | e.g., "claude-sonnet-4-5" |
| `llm_request.context` | "interaction" \| "standalone" | whether inside interaction span |
| `speed` | "fast" \| "normal" | fast mode toggle |
| `query_source` | string | optional metadata |
| `duration_ms` | int | total request time |
| `input_tokens` | int | prompt tokens |
| `output_tokens` | int | completion tokens |
| `cache_read_tokens` | int | prompt cache hits |
| `cache_creation_tokens` | int | new cache entries |
| `success` | bool | |
| `status_code` | int | HTTP status |
| `error` | string | error message if failed |
| `attempt` | int | retry count |
| `response.has_tool_call` | bool | |
| `ttft_ms` | int | time-to-first-token |

#### `claude_code.tool`
| Attribute | Type | Notes |
|-----------|------|-------|
| `tool_name` | string | e.g., "Read", "Bash", "Write" |
| `span.type` | "tool" | constant |
| `duration_ms` | int | |
| `result_tokens` | int | token count of tool result |
| `success` | bool | |

#### `claude_code.tool.blocked_on_user`
| Attribute | Type | Notes |
|-----------|------|-------|
| `decision` | string | "approve", "deny", etc. |
| `source` | string | "permission_prompt", etc. |
| `duration_ms` | int | user wait time |

#### `claude_code.tool.execution`
| Attribute | Type | Notes |
|-----------|------|-------|
| `success` | bool | |
| `error` | string | |
| `duration_ms` | int | |

#### `claude_code.hook`
| Attribute | Type | Notes |
|-----------|------|-------|
| `hook_event` | string | "PreToolUse", "PostToolUse", etc. |
| `hook_name` | string | script name |
| `num_hooks` | int | total hooks for event |
| `hook_definitions` | string | JSON config |
| `num_success` | int | |
| `num_blocking` | int | |
| `num_non_blocking_error` | int | |
| `num_cancelled` | int | |
| `duration_ms` | int | |

### OTEL Environment Variables (Complete)

#### Export Control
| Variable | Default | Description |
|----------|---------|-------------|
| `CLAUDE_CODE_ENABLE_TELEMETRY` | false | Master switch for user-configured OTLP export |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | — | OTLP collector URL |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | http/protobuf | `grpc` \| `http/protobuf` \| `http/json` |
| `OTEL_EXPORTER_OTLP_HEADERS` | — | Auth headers |
| `OTEL_EXPORTER_OTLP_TRACES_HEADERS` | — | Trace-specific override |
| `OTEL_EXPORTER_OTLP_METRICS_HEADERS` | — | Metric-specific override |
| `OTEL_EXPORTER_OTLP_LOGS_HEADERS` | — | Log-specific override |
| `OTEL_EXPORTER_OTLP_TRACES_PROTOCOL` | — | Protocol override for traces |
| `OTEL_EXPORTER_OTLP_METRICS_PROTOCOL` | — | Protocol override for metrics |
| `OTEL_EXPORTER_OTLP_LOGS_PROTOCOL` | — | Protocol override for logs |
| `OTEL_EXPORTER_OTLP_METRICS_CLIENT_CERTIFICATE` | — | mTLS cert for metrics |
| `OTEL_EXPORTER_OTLP_METRICS_CLIENT_KEY` | — | mTLS key for metrics |

#### Exporter Types
| Variable | Default | Values |
|----------|---------|--------|
| `OTEL_LOGS_EXPORTER` | — | `otlp`, `console`, `none` |
| `OTEL_METRICS_EXPORTER` | — | `otlp`, `console`, `prometheus`, `none` |

#### Intervals
| Variable | Default | Description |
|----------|---------|-------------|
| `OTEL_LOGS_EXPORT_INTERVAL` | 10000ms | Log batch flush interval |
| `OTEL_METRIC_EXPORT_INTERVAL` | 60000ms | Metric flush interval |

#### Privacy / Content Controls
| Variable | Default | Description |
|----------|---------|-------------|
| `OTEL_LOG_USER_PROMPTS` | false | Include raw user prompts in spans (**PII RISK**) |
| `OTEL_LOG_TOOL_CONTENT` | false | Include tool I/O in span events (**PII RISK**) |

#### Metric Dimensions
| Variable | Default | Description |
|----------|---------|-------------|
| `OTEL_METRICS_INCLUDE_SESSION_ID` | true | Add `session.id` to metrics |
| `OTEL_METRICS_INCLUDE_VERSION` | false | Add `service.version` |
| `OTEL_METRICS_INCLUDE_ACCOUNT_UUID` | true | Add account UUID (**PII RISK**) |

#### Resource
| Variable | Default | Description |
|----------|---------|-------------|
| `OTEL_RESOURCE_ATTRIBUTES` | — | `key=value,key=value` pairs |
| `OTEL_SERVICE_NAME` | — | Overrides `service.name` |

#### Batch Processor Tuning
| Variable | Default | Description |
|----------|---------|-------------|
| `OTEL_BLRP_MAX_EXPORT_BATCH_SIZE` | 512 | Max logs per batch |
| `OTEL_BLRP_MAX_QUEUE_SIZE` | 2048 | Max queue before drop |
| `OTEL_BLRP_SCHEDULE_DELAY` | 5000ms | Batch schedule delay |
| `OTEL_BLRP_EXPORT_TIMEOUT` | 30000ms | Export timeout |

#### Log Record Limits
| Variable | Default | Description |
|----------|---------|-------------|
| `OTEL_LOGRECORD_ATTRIBUTE_VALUE_LENGTH_LIMIT` | — | Max attribute value length |
| `OTEL_LOGRECORD_ATTRIBUTE_COUNT_LIMIT` | 128 | Max attributes per log record |
| `OTEL_ATTRIBUTE_COUNT_LIMIT` | — | Global attribute count limit |
| `OTEL_ATTRIBUTE_VALUE_LENGTH_LIMIT` | — | Global attribute value length limit |

### Auto-Detected Resource Attributes
| Attribute | Source |
|-----------|--------|
| `host.name` | `os.hostname()` |
| `host.arch` | `os.arch()` |
| `host.id` | machine ID |
| `os.type` | platform |
| `os.version` | kernel version |
| `service.instance.id` | random UUID |
| `telemetry.sdk.name` | "opentelemetry" |
| `telemetry.sdk.language` | "nodejs" |
| `telemetry.sdk.version` | SDK version |

---

## 2. 1P Event Logging (Anthropic First-Party)

### Architecture
- **Logger**: `com.anthropic.claude_code.events` (OTEL LoggerProvider)
- **Variable**: `qAH` (logger instance), `KAH` (provider)
- **Enabled**: `bqH()` — checks internal auth state (firstParty users only)
- **Kill switch**: `tengu_frond_boric` GrowthBook config (per-surface kill)

### Event Pipeline
```
Q("tengu_event_name", metadata)
  → nD_() / iD_() (sync/async)
    → shouldSampleEvent(eventName) — checks tengu_event_sampling_config
    → IF gate tengu_log_segment_events → GyA() (Segment.io track)
    → IF gate tengu_log_datadog_events → aVA() (DataDog log)
    → NWH() (1P OTEL log emit)
```

### Event Sampling
- Config: `tengu_event_sampling_config` (GrowthBook dynamic config)
- Per-event `sample_rate` (0.0–1.0), `null` = no sampling (send all)
- `um$(eventName)` returns sample rate or 0 (skip)

### Batch Config
- `tengu_1p_event_batch_config` (GrowthBook)
- `scheduledDelayMillis`: 10000 (default)
- `maxExportBatchSize`: 200
- `maxQueueSize`: 8192

### Complete Event Catalog (400+ events)

All events use `Q("tengu_<name>", metadata)`. Full list extracted:

**Startup & Init**: `tengu_started`, `tengu_startup_perf`, `tengu_startup_telemetry`, `tengu_init`, `tengu_began_setup`, `tengu_startup_manual_model_config`

**API & LLM**: `tengu_api_query`, `tengu_api_success`, `tengu_api_error`, `tengu_api_retry`, `tengu_api_before_normalize`, `tengu_api_after_normalize`, `tengu_api_cache_breakpoints`, `tengu_api_custom_529_overloaded_error`, `tengu_api_opus_fallback_triggered`, `tengu_max_tokens_context_overflow_adjustment`, `tengu_max_tokens_reached`, `tengu_streaming_error`, `tengu_streaming_stall`, `tengu_streaming_stall_summary`, `tengu_streaming_idle_timeout`, `tengu_streaming_fallback_to_non_streaming`, `tengu_stream_no_events`, `tengu_model_fallback_triggered`, `tengu_model_whitespace_response`, `tengu_refusal_api_response`, `tengu_off_switch_query`, `tengu_context_size`, `tengu_context_window_exceeded`

**Tool Use**: `tengu_tool_use_success`, `tengu_tool_use_error`, `tengu_tool_use_cancelled`, `tengu_tool_use_progress`, `tengu_tool_use_show_permission_request`, `tengu_tool_use_granted_in_config`, `tengu_tool_use_denied_in_config`, `tengu_tool_use_granted_by_classifier`, `tengu_tool_use_granted_by_permission_hook`, `tengu_tool_use_rejected_in_prompt`, `tengu_tool_use_can_use_tool_allowed`, `tengu_tool_use_can_use_tool_rejected`, `tengu_tool_use_diff_computed`, `tengu_tool_use_tool_result_mismatch_error`, `tengu_tool_empty_result`, `tengu_tool_result_persisted`, `tengu_tool_result_persisted_message_budget`, `tengu_tool_result_pairing_repaired`, `tengu_tool_search_outcome`, `tengu_tool_search_mode_decision`, `tengu_tool_input_alias_applied`, `tengu_deferred_tool_schema_not_sent`, `tengu_deferred_tools_pool_change`

**Bash / Shell**: `tengu_bash_tool_command_executed`, `tengu_bash_tool_reset_to_original_dir`, `tengu_bash_tool_simple_echo`, `tengu_bash_command_explicitly_backgrounded`, `tengu_bash_ast_too_complex`, `tengu_bash_security_check_triggered` (15+ variants), `tengu_shell_set_cwd`, `tengu_shell_snapshot_failed`, `tengu_shell_snapshot_error`, `tengu_shell_unknown_error`

**Files & IO**: `tengu_file_operation`, `tengu_file_changed`, `tengu_file_read_limits_override`, `tengu_file_suggestions_query`, `tengu_file_suggestions_git_ls_files`, `tengu_file_suggestions_ripgrep`, `tengu_session_file_read`, `tengu_binary_content_persisted`, `tengu_atomic_write_error`, `tengu_repo_text_file_size`, `tengu_watched_file_compression_failed`

**Compact / Memory**: `tengu_compact`, `tengu_compact_failed`, `tengu_compact_cache_sharing_success`, `tengu_compact_cache_sharing_fallback`, `tengu_compact_streaming_retry`, `tengu_partial_compact`, `tengu_partial_compact_failed`, `tengu_auto_compact_succeeded`, `tengu_post_autocompact_turn`, `tengu_auto_compact_setting_changed`

**MCP**: `tengu_mcp_start`, `tengu_mcp_add`, `tengu_mcp_delete`, `tengu_mcp_get`, `tengu_mcp_list`, `tengu_mcp_list_changed`, `tengu_mcp_servers`, `tengu_mcp_tools_commands_loaded`, `tengu_mcp_instructions_pool_change`, `tengu_mcp_server_connection_failed`, `tengu_mcp_server_connection_succeeded`, `tengu_mcp_server_needs_auth`, `tengu_mcp_session_expired`, `tengu_mcp_dialog_choice`, `tengu_mcp_multidialog_choice`, `tengu_mcp_oauth_flow_start/success/error`, `tengu_mcp_auth_config_authenticate/clear`, `tengu_mcp_elicitation_shown/response`, `tengu_mcp_tool_call_auth_error`, `tengu_mcp_ide_server_connection_*`, `tengu_mcp_claudeai_proxy_401`, `tengu_mcp_headersHelper_missing_trust`

**OAuth & Auth**: `tengu_oauth_flow_start`, `tengu_oauth_success`, `tengu_oauth_error`, `tengu_oauth_token_refresh_*` (12+ variants), `tengu_oauth_api_key`, `tengu_oauth_storage_warning`, `tengu_oauth_401_recovered_from_keychain`, `tengu_config_auth_loss_prevented`

**Hooks**: `tengu_run_hook`, `tengu_hooks_command`, `tengu_pre_tool_hook_error`, `tengu_pre_tool_hooks_cancelled`, `tengu_post_tool_hook_error`, `tengu_post_tool_hooks_cancelled`, `tengu_post_tool_failure_hook_error`, `tengu_post_tool_failure_hooks_cancelled`, `tengu_pre_stop_hooks_cancelled`, `tengu_stop_hook_error`, `tengu_repl_hook_finished`

**Sessions & Resume**: `tengu_session_resumed`, `tengu_session_persistence_failed`, `tengu_session_renamed`, `tengu_session_memory_*`, `tengu_session_tagged`, `tengu_session_linked_to_pr`, `tengu_conversation_forked`, `tengu_conversation_rewind`

**Memory**: `tengu_memdir_loaded`, `tengu_memdir_accessed`, `tengu_memdir_disabled`, `tengu_memdir_file_read/write/edit`, `tengu_auto_memory_toggled`, `tengu_extract_memories_*`, `tengu_claudemd__initial_load`, `tengu_claude_md_permission_error`

**Agent / Teams**: `tengu_agent_created`, `tengu_agent_tool_selected/completed/terminated`, `tengu_agent_stop_hook_*`, `tengu_agent_flag`, `tengu_at_mention_agent_*`, `tengu_subagent_at_mention`, `tengu_teammate_mode_changed`, `tengu_team_created/deleted`, `tengu_team_mem_*`

**Bridge / CoWork**: `tengu_bridge_started/shutdown`, `tengu_bridge_session_started/done/timeout`, `tengu_bridge_command`, `tengu_bridge_message_received`, `tengu_bridge_reconnected`, `tengu_bridge_fatal_error`, `tengu_bridge_repl_*` (20+ variants)

**UI & Input**: `tengu_input_prompt`, `tengu_input_command`, `tengu_input_bash`, `tengu_input_slash_*`, `tengu_cancel`, `tengu_continue`, `tengu_copy`, `tengu_flicker`, `tengu_help_toggled`, `tengu_thinking_toggled`, `tengu_brief_mode_toggled`, `tengu_fast_mode_toggled/picker_shown`, `tengu_mode_cycle`, `tengu_model_command_*`, `tengu_model_picker_hotkey`, `tengu_editor_mode_changed`, `tengu_keybinding_fallback_used`, `tengu_custom_keybindings_loaded`

**Plan Mode**: `tengu_plan_enter`, `tengu_plan_exit`, `tengu_plan_external_editor_used`, `tengu_exit_plan_mode_called_outside_plan`

**Auto Mode**: `tengu_auto_mode_decision`, `tengu_auto_mode_outcome`, `tengu_auto_mode_denial_limit_exceeded`, `tengu_auto_mode_malformed_tool_input`, `tengu_auto_mode_opt_in_dialog_*`

**Plugins**: `tengu_plugins_loaded`, `tengu_plugin_installed/uninstalled/enabled/disabled_cli`, `tengu_plugin_*_command`, `tengu_skill_loaded/tool_invocation/file_changed`, `tengu_dynamic_skills_changed`

**Updates & Install**: `tengu_auto_updater_*`, `tengu_native_auto_updater_*`, `tengu_native_install_*`, `tengu_binary_download_*`, `tengu_version_check_*`, `tengu_version_lock_*`, `tengu_update_check`

**Images & Media**: `tengu_image_api_validation_failed`, `tengu_image_resize_failed/fallback`, `tengu_image_compress_failed`, `tengu_paste_image/text`, `tengu_pasted_image_resize_attempt`, `tengu_voice_recording_started/completed`, `tengu_voice_toggled`, `tengu_voice_stream_early_retry`

**PDF**: `tengu_pdf_page_extraction`, `tengu_pdf_reference_attachment`

**Security**: `tengu_bash_security_check_triggered` (15+ categories), `tengu_tree_sitter_security_divergence`, `tengu_trust_dialog_accept/shown`, `tengu_managed_settings_security_dialog_*`, `tengu_bypass_permissions_mode_dialog_*`

**Config**: `tengu_config_changed`, `tengu_config_model_changed`, `tengu_config_parse_error`, `tengu_config_cache_stats`, `tengu_config_lock_contention`, `tengu_config_stale_write`

**Errors**: `tengu_uncaught_exception`, `tengu_unhandled_rejection`, `tengu_query_error`, `tengu_node_warning`

**Diagnostics**: `tengu_heap_dump`, `tengu_doctor_command`

**Worktrees**: `tengu_worktree_created/removed/kept/cleanup/detection`

**Claude.ai Integration**: `tengu_claudeai_limits_status_changed`, `tengu_claudeai_mcp_*`, `tengu_claude_in_chrome_*`

**SWE-Bench**: Events include `sweBenchRunId`, `sweBenchInstanceId`, `sweBenchTaskId` from env vars

---

## 3. Segment.io Analytics (NEW — missed in v1)

### Architecture
- **SDK**: `analytics-node` (Segment server-side SDK)
- **Endpoint**: `https://api.segment.io/v1/batch`
- **Write Key (production)**: `LKJN8LsLERHEOXkw487o7qCTFOrGPimI`
- **Write Key (development)**: `b64sf1kxwDGe1PiSAlv5ixuH0f509RKK`
- **Batch config**: `flushAt: 50`, `flushInterval: 10000ms`
- **Gate**: `tengu_log_segment_events` Statsig gate
- **Kill switch**: `tengu_frond_boric.segment = true` (via GrowthBook)

### Data Sent
```javascript
// track() call
{
  anonymousId: KT$(),           // anonymous ID
  userId: deviceId,             // if authenticated
  event: "tengu_event_name",
  properties: {
    ...eventMetadata,           // event-specific data
    model: "claude-sonnet-4-5",
    sessionId: "...",
    userType: "external",
    entrypoint: "cli",
    isInteractive: "true",
    clientType: "...",
    subscriptionType: "...",
    env: { platform, os, ... },
    process: { rss, heapUsed, cpuPercent, uptime, ... },
    surface: "claude-code",
    accountUuid: "...",         // if authenticated
    organizationUuid: "...",   // if authenticated
  }
}
```

### identify() calls
- `kXf(traits)` — sends user traits to Segment
- Includes `anonymousId` and `userId` (deviceId)

### Disabled when
- `GN()` returns true (Bedrock/Vertex/Foundry/DISABLE_TELEMETRY)
- `tengu_frond_boric.segment` kill switch active
- `tengu_log_segment_events` gate is false

---

## 4. DataDog Logs (NEW — missed in v1)

### Architecture
- **Endpoint**: `https://http-intake.logs.us5.datadoghq.com/api/v2/logs`
- **API Key**: `pubbbf48e6d78dae54bceaa4acf463299bf` (hardcoded, public intake key)
- **Flush interval**: `CLAUDE_CODE_DATADOG_FLUSH_INTERVAL_MS` || 15000ms
- **Max batch**: 100 events
- **Timeout**: 5000ms
- **Gate**: `tengu_log_datadog_events` Statsig gate
- **Kill switch**: `tengu_frond_boric.datadog = true`

### DataDog Event Properties
- Subset of events in `t16` allowlist (curated list of ~30 event names):
  - `tengu_flicker`, `tengu_init`, `tengu_started`
  - `tengu_model_fallback_triggered`
  - `tengu_oauth_*` (select events)
  - `tengu_query_error`, `tengu_repo_text_file_size`
  - `tengu_tool_use_error/success`
  - `tengu_uncaught_exception`, `tengu_unhandled_rejection`
  - `tengu_voice_*`, `tengu_team_mem_sync_*`

### DataDog Tags (Indexed Dimensions)
`s16` defines the facet fields:
```
arch, clientType, errorType, http_status_range, http_status,
kairosActive, model, platform, provider, subscriptionType,
toolName, userBucket, userType, version, versionBase
```

### DataDog Event Structure
```javascript
{
  ...eventMetadata,
  ...envContext,             // platform, os, etc.
  userBucket: A66(),         // user cohort bucket
  // posted as JSON array to DataDog HTTP intake
}
```

---

## 5. Perfetto Tracing

### Activation
```bash
export CLAUDE_CODE_PERFETTO_TRACE=/path/to/session.pftrace
```

### Span Types (mapped 1:1 from OTEL spans)
- `p8f(prompt)` / `U8f(id)` — interaction
- `C8f({model, querySource, messageId})` / `u8f(id, meta)` — LLM request
- `b8f(toolName, meta)` / `x8f(id, {success, resultTokens})` — tool
- `m8f(type)` / `B8f(id, {decision, source})` — permission

### Perfetto-Specific Metadata (LLM spans)
```
ttftMs, ttltMs, promptTokens, outputTokens,
cacheReadTokens, cacheCreationTokens,
success, error, requestSetupMs, attemptStartTimes[]
```

---

## 6. Beta Tracing (Detailed OTEL)

### Activation
```bash
export ENABLE_BETA_TRACING_DETAILED=true
export BETA_TRACING_ENDPOINT=http://your-collector:4318
```

### How it works
- `WO()` checks: `ENABLE_BETA_TRACING_DETAILED` AND `BETA_TRACING_ENDPOINT` set
- Plus: must be headless (`LD()`) OR `tengu_trace_lantern` flag is true
- Sets up **its own** TraceProvider and LoggerProvider pointing at `BETA_TRACING_ENDPOINT`
- Creates the same `com.anthropic.claude_code.events` logger
- Independent from `CLAUDE_CODE_ENABLE_TELEMETRY` — this is a separate pipeline

### What it adds
- All hook spans (`claude_code.hook`) only fire when `WO()` is true
- Enhanced span creation — `JC()` returns true if `hkA() || WO()`

---

## 7. Local Debug Logging

### Configuration
```bash
export CLAUDE_CODE_DEBUG_LOGS_DIR=/path/to/logs/   # custom dir
export CLAUDE_CODE_DEBUG_LOG_LEVEL=verbose          # verbose|debug|info|warn|error
```

### Default location
```
~/.claude/debug/<session-id>.txt
```

### Log function
```javascript
function v(message, { level } = { level: "debug" }) {
  // writes to debug log file
  // respects CLAUDE_CODE_DEBUG_LOG_LEVEL
}
```

### Memory tracking
- If `CvH` flag set, `process.memoryUsage()` captured with each `T8()` mark
- RSS, heap used printed alongside performance marks

---

## 8. Startup Performance Profiler

### Implementation
- Uses `perf_hooks.performance` marks
- Function: `T8(markName)` — places a mark
- Function: `ZF$(value)` — formats timing to 3 decimal places

### Known marks
```
1p_event_logging_start
1p_event_after_growthbook_config
init_after_1p_event_logging
init_after_oauth_populate
telemetry_init_start
```

### Output
- `Q("tengu_startup_perf", metrics)` — logs startup timing to 1P events
- Includes duration between marks, memory snapshots

---

## 9. Headless Profiler

### Activation
- Only runs when `LD()` returns true (headless/print mode)
- Additional sampling: `zR6 = 0.05` (5% of sessions)

### What it captures per turn
```javascript
{
  turn_total_ms,              // total turn duration
  query_overhead_ms,          // time before API call
  checkpoint_count,           // number of checkpoints
  entrypoint: "sdk-ts",       // CLAUDE_CODE_ENTRYPOINT
}
```

### Output
- `Q("tengu_headless_latency", metrics)` — sent as 1P event

---

## 10. Process Metrics (sent with every event)

### Function: `yL_()`
```javascript
{
  uptime: process.uptime(),
  rss: memoryUsage.rss,
  heapTotal: memoryUsage.heapTotal,
  heapUsed: memoryUsage.heapUsed,
  external: memoryUsage.external,
  arrayBuffers: memoryUsage.arrayBuffers,
  constrainedMemory: process.constrainedMemory(),
  cpuUsage: { user, system },
  cpuPercent: calculatedPercent,
}
```

### Where it's sent
- Included as `processMetrics` in `mJH()` context
- Attached to Segment `track()` calls as `process` property
- Attached to DataDog events

---

## 11. Attribution Header

### Format
```
x-anthropic-billing-header: cc_version=2.1.76.N; cc_entrypoint=cli; cch=944e0; cc_workload=TAG;
```

### Components
| Field | Source |
|-------|--------|
| `cc_version` | `VERSION.turnCount` |
| `cc_entrypoint` | `CLAUDE_CODE_ENTRYPOINT` |
| `cch` | Static hash ("944e0") |
| `cc_workload` | `--workload` CLI flag |

### Control
- `tengu_attribution_header` GrowthBook flag (default: true)
- `CLAUDE_CODE_ATTRIBUTION_HEADER=false` to disable

---

## 12. Heap Dump Tool

### Built-in command
- Tool name: `heapdump`
- Event: `Q("tengu_heap_dump", { success, size, path, error })`
- Creates V8 heap snapshot for memory debugging

---

## 13. Feature Flags & Experiments

### GrowthBook (Feature Flags)
- **SDK**: Full GrowthBook JS SDK
- **Functions**: `_A(key, default)`, `AE(key, default)` — sync value getters
- **Refresh**: Periodic polling + auth-change triggers
- **State**: `cachedGrowthBookFeatures` in local store

### Statsig (Gates)
- **Functions**: `MM(key)` (sync/cached), `liA(key)` (async/fresh)
- **State**: `cachedStatsigGates` in local store
- **Fallback**: Statsig → GrowthBook if gate not found

### Kill Switch System
- `tengu_frond_boric` (GrowthBook config object)
  - `.firstParty = true` → kills 1P event logging
  - `.segment = true` → kills Segment analytics
  - `.datadog = true` → kills DataDog logging
- `uqH(surface)` → checks kill switch per surface

### Event Sampling System
- `tengu_event_sampling_config` (GrowthBook config object)
- Per-event-name `sample_rate` (0.0–1.0)
- `um$(eventName)` → returns rate if sampled, 0 if dropped, null if no config

### Complete Feature Flag List (2.1.76)

| Flag | Default | Purpose |
|------|---------|---------|
| `enhanced_telemetry_beta` | false | Enhanced internal telemetry |
| `tengu_tst_kx7` | — | Tool search experiment |
| `tengu_defer_all_bn4` | true | Defer all tool schemas |
| `tengu_tst_hint_m7r` | false | Tool search hint |
| `tengu_plan_mode_interview_phase` | false | Plan mode interview |
| `tengu_auto_mode_config` | {} | Auto mode config (enabled, twoStageClassifier) |
| `tengu_mcp_elicitation` | false | MCP elicitation |
| `tengu_attribution_header` | true | Billing attribution header |
| `tengu_trace_lantern` | false | Beta tracing (headless) |
| `tengu_pid_based_version_locking` | false | PID version locking |
| `tengu_keybinding_customization_release` | false | Custom keybindings |
| `tengu_1p_event_batch_config` | {} | 1P event batch settings |
| `tengu_event_sampling_config` | {} | Per-event sampling rates |
| `tengu_frond_boric` | {} | Kill switches per telemetry surface |
| `tengu_log_segment_events` | false | Gate: Segment analytics |
| `tengu_log_datadog_events` | false | Gate: DataDog logging |
| `tengu_amber_flint` | true | Unknown |
| `tengu_marble_anvil` | false | Unknown |
| `tengu_turtle_carbon` | true | Unknown |
| `tengu_grey_step2` | — | Unknown |
| `tengu_granite_whisper` | false | Unknown |
| `tengu_penguins_off` | — | Unknown |
| `tengu_marble_sandcastle` | false | Unknown |
| `tengu_herring_clock` | false | Unknown |
| `tengu_coral_fern` | false | Unknown |
| `tengu_swinburne_dune` | false | Unknown |
| `tengu_passport_quail` | false | Unknown |
| `tengu_paper_halyard` | false | Unknown |
| `tengu_amber_quartz_disabled` | false | Unknown |
| `tengu_lean_cast` | false | Unknown |
| `tengu_amber_wren` | {} | Unknown |
| `tengu_hawthorn_window` | — | Unknown |
| `tengu_hawthorn_steeple` | false | Unknown |
| `tengu_pewter_ledger` | — | Unknown |
| `tengu_pewter_gull` | false | Unknown |
| `tengu_glacier_2xr` | false | Unknown |
| `tengu_tight_weave` | true | Unknown |
| `tengu_orchid_trellis` | false | Unknown |
| `tengu_marble_whisper2` | false | Unknown |
| `tengu_kairos_brief` | false | Unknown |

---

## 14. Entrypoint-Specific Behavior

### Known Entrypoints (`CLAUDE_CODE_ENTRYPOINT`)
| Value | Surface |
|-------|---------|
| `cli` | Default CLI |
| `claude-desktop` | Claude Desktop (Electron) |
| `sdk-ts` | TypeScript Agent SDK |
| `sdk-py` | Python Agent SDK |
| `sdk-cli` | SDK CLI wrapper |
| `electron` | Generic Electron embedding |

### Claude Desktop Specifics
- `CLAUDE_CODE_ENTRYPOINT=claude-desktop` set by Desktop app
- `add-from-claude-desktop` CLI subcommand exists
- Embedded search tools disabled for SDK entrypoints
- All telemetry flows are **identical** — Desktop uses the same binary
- Desktop does NOT have separate Electron-level telemetry within the CLI binary
- Desktop may have its own telemetry in its Electron shell (not in this binary)

### SDK Entrypoints
- Headless profiler active (`LD()` true)
- Some tools disabled (embedded search)
- `CLAUDE_AGENT_SDK_VERSION` and `CLAUDE_AGENT_SDK_CLIENT_APP` sent with events

---

## 15. What's NOT in the Binary

### Not present (confirmed absent)
- **No Sentry SDK** — only token regex patterns for secret scanning
- **No Amplitude** — only GrowthBook `minAmplitude` config (experiment stats)
- **No PostHog, Mixpanel, LaunchDarkly, Heap** — none found
- **No alignment/interpretability infrastructure**
- **No model behavior analysis hooks**
- **No red-teaming signals**
- **No Constitutional AI markers**
- **No RLHF references**

### Claude Desktop (Electron shell) — outside scope
The Desktop app's Electron wrapper likely has its own telemetry (crash reporting, app analytics), but that code lives in the Desktop app binary, not in the Claude Code CLI binary analyzed here. The CLI binary is the same binary used by both.

---

## 16. Privacy Impact Summary

### What Anthropic receives (1P users, default config)
1. **All 400+ tengu_* events** with metadata (model, session, platform, entrypoint)
2. **Process metrics** (RSS, heap, CPU, uptime)
3. **GrowthBook experiment evaluations**
4. **Attribution header** on every API call (version, entrypoint, workload)

### What Anthropic receives if gates are on
5. **Segment.io** — same events + anonymous/user IDs + account/org UUIDs
6. **DataDog** — curated subset (~30 events) + indexed tags

### What you can capture yourself
7. **OTEL traces** — full span hierarchy with all attributes (via your endpoint)
8. **Perfetto traces** — local performance analysis files
9. **Beta traces** — detailed spans including hooks (via your endpoint)
10. **Debug logs** — local text logs with timestamps

### Data retention (Grove privacy)
- **Opted in** (`grove_enabled=true`): 5-year retention, data may train models
- **Opted out** (`grove_enabled=false`): 30-day retention, safety-only
- Toggle: settings UI or `PATCH /api/oauth/account/settings { grove_enabled }`

### What you can block
```bash
# Nuclear: disable ALL non-essential telemetry
export DISABLE_TELEMETRY=true

# Or equivalently:
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=true

# Selective: disable only 3P OTEL export
# (just don't set CLAUDE_CODE_ENABLE_TELEMETRY)

# Selective: disable attribution header
export CLAUDE_CODE_ATTRIBUTION_HEADER=false

# Selective: disable error reporting
export DISABLE_ERROR_REPORTING=true

# Selective: disable cost warnings
export DISABLE_COST_WARNINGS=true

# Selective: disable user-facing feedback/bug commands
export DISABLE_BUG_COMMAND=true
export DISABLE_FEEDBACK_COMMAND=true
```

### PII exposure vectors
| Vector | Env Var | Default |
|--------|---------|---------|
| User prompts in OTEL spans | `OTEL_LOG_USER_PROMPTS` | false |
| Tool content in OTEL events | `OTEL_LOG_TOOL_CONTENT` | false |
| Account UUID in metrics | `OTEL_METRICS_INCLUDE_ACCOUNT_UUID` | **true** |
| Device ID in Segment | always sent | always |
| Account/org UUID in Segment | if authenticated | always |

---

## 17. Practical Setup for Maximum Observability

### Everything-on configuration
```bash
# 1. Your OTEL collector
export CLAUDE_CODE_ENABLE_TELEMETRY=true
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
export OTEL_SERVICE_NAME=claude-code
export OTEL_RESOURCE_ATTRIBUTES="service.version=2.1.76,env=research"

# 2. Content logging (PII risk — research only)
export OTEL_LOG_USER_PROMPTS=true
export OTEL_LOG_TOOL_CONTENT=true

# 3. Perfetto trace
export CLAUDE_CODE_PERFETTO_TRACE=$HOME/traces/$(date +%s).pftrace

# 4. Beta tracing (gets hook spans too)
export ENABLE_BETA_TRACING_DETAILED=true
export BETA_TRACING_ENDPOINT=http://localhost:4318

# 5. Enhanced telemetry
export CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=true

# 6. Debug logs
export CLAUDE_CODE_DEBUG_LOGS_DIR=$HOME/claude-debug-logs/
export CLAUDE_CODE_DEBUG_LOG_LEVEL=verbose
```

### Minimal privacy-safe setup
```bash
export CLAUDE_CODE_ENABLE_TELEMETRY=true
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
export OTEL_SERVICE_NAME=claude-code
export OTEL_LOG_USER_PROMPTS=false
export OTEL_LOG_TOOL_CONTENT=false
export OTEL_METRICS_INCLUDE_ACCOUNT_UUID=false
```

### Maximum privacy (block everything)
```bash
export DISABLE_TELEMETRY=true
export CLAUDE_CODE_ATTRIBUTION_HEADER=false
export DISABLE_ERROR_REPORTING=true
export DISABLE_COST_WARNINGS=true
export DISABLE_BUG_COMMAND=true
export DISABLE_FEEDBACK_COMMAND=true
export DISABLE_AUTOUPDATER=true
```

---

## 18. Key Function Reference

| Function | Purpose |
|----------|---------|
| `Q(name, meta)` | Log event to all active surfaces |
| `NWH(name, meta)` | Log event to 1P OTEL logger only |
| `GyA(name, meta)` | Log event to Segment.io |
| `aVA(name, meta)` | Log event to DataDog |
| `BVf()` | Is 3P OTEL enabled? |
| `GN()` | Is telemetry globally disabled? |
| `VL$()` | Is nonessential traffic disabled? |
| `hkA()` | Is enhanced telemetry enabled? |
| `WO()` | Is beta tracing enabled? |
| `JC()` | Should OTEL spans be created? |
| `LD()` | Is headless mode? |
| `bqH()` | Is 1P event logging enabled? |
| `DY8()` | Is Segment gate on? |
| `fY8()` | Is DataDog gate on? |
| `uqH(surface)` | Is kill switch active for surface? |
| `um$(name)` | Sample rate for event name |
| `_A(key, def)` | GrowthBook feature value (sync) |
| `MM(key)` | Statsig gate (sync/cached) |
| `v(msg, opts)` | Write to debug log file |
| `T8(mark)` | Performance mark |
| `F8f(prompt)` | Start interaction span |
| `c8f(model, ...)` | Start LLM span |
| `Q8f(tool, ...)` | Start tool span |
| `r8f(event, ...)` | Start hook span |
| `mJH(opts)` | Build event context (model, env, process metrics) |
| `yL_()` | Capture process metrics snapshot |
| `fH(error)` | Report error to ring buffer + logError |
| `eY()` | Get total session cost (USD) |
| `OT$(bool)` | Toggle grove privacy (PATCH to API) |
| `Zif(msgs, ...)` | Post-sampling hook (fires after each LLM call) |

---

## 19. Error Reporting System

### Architecture
- **Function**: `fH(error)` — main entry point
- **Ring buffer**: `BA` array, max 100 entries (`uA9()` manages)
- **Backend**: `ZS.logError(error)` — sends to Anthropic error pipeline
- **MCP variants**: `logMCPError(error)`, `logMCPDebug(msg)` — MCP-specific reporting
- **Gate**: `DISABLE_ERROR_REPORTING` env var (disables entirely)

### What it captures
- Error message, stack trace, error type
- Ring buffer prevents duplicate/rapid-fire reporting (deduplication by error signature)
- Errors from MCP server connections get separate `logMCPError` path

### Env Var
```bash
export DISABLE_ERROR_REPORTING=true   # suppress all error reporting
```

### Events
- `tengu_uncaught_exception` — unhandled exceptions
- `tengu_unhandled_rejection` — unhandled promise rejections
- `tengu_query_error` — API query errors
- `tengu_node_warning` — Node.js runtime warnings

---

## 20. Grove Privacy / Data Retention System

### Architecture
- **Toggle function**: `OT$(enabled)` — sends to Anthropic API
- **API call**: `PATCH /api/oauth/account/settings` with body `{ grove_enabled: bool }`
- **Auth**: Uses OAuth headers from `Rw()` (Bearer token + anthropic-version)
- **UI**: "Help improve Claude" dialog in settings

### Privacy Modes
| Mode | `grove_enabled` | Data Retention | Description |
|------|-----------------|----------------|-------------|
| Opted **in** | `true` | 5 years | Conversations may be used to improve Claude |
| Opted **out** | `false` | 30 days | Conversations stored for safety only, then deleted |

### Events
- `tengu_grove_policy_accepted` — user opted in
- `tengu_grove_policy_rejected` — user opted out
- `tengu_grove_policy_shown` — dialog was displayed
- `tengu_grove_policy_dismissed` — dialog dismissed without action

### Trust Dialog
- Managed settings: `tengu_managed_settings_security_dialog_shown/accepted/rejected`
- Bypass permissions: `tengu_bypass_permissions_mode_dialog_shown/accepted/rejected`
- Trust dialog: `tengu_trust_dialog_accept/shown`

---

## 21. Auto-Mode Security Classifier

### Architecture
- Separate LLM call using `claude-sonnet-4-6` (not the main conversation model)
- Structured output via `classify_result` tool definition
- Two-stage classifier available: `tengu_auto_mode_config.twoStageClassifier`

### Classifier Output
```javascript
{
  thinking: string,      // reasoning about safety
  shouldBlock: boolean,  // whether to block the tool use
  reason: string         // explanation for blocking
}
```

### Events
- `tengu_auto_mode_decision` — classifier invoked with decision context
- `tengu_auto_mode_outcome` — final result (allowed/blocked/error)
- `tengu_auto_mode_denial_limit_exceeded` — too many consecutive denials
- `tengu_auto_mode_malformed_tool_input` — classifier returned bad format
- `tengu_auto_mode_opt_in_dialog_shown/accepted/rejected` — user opt-in flow

### Error Dumps
- On classifier errors, writes debug dump files to local filesystem
- Contains the failed classifier input/output for debugging

---

## 22. Speculation System

### Architecture
- Speculative tool execution: starts executing likely-needed tools before the model confirms
- Tracked per speculation attempt with unique `speculation_id`

### Event: `tengu_speculation`
```javascript
{
  speculation_id: string,          // unique ID
  outcome: string,                 // "hit" | "miss" | "partial" | "error"
  duration_ms: number,             // execution time
  suggestion_length: number,       // length of speculated content
  tools_executed: number,          // how many tools ran speculatively
  completed: boolean,              // whether speculation finished before needed
  boundary_type: string,           // what ended speculation
  boundary_tool: string,           // tool that triggered boundary
  boundary_detail: string          // additional boundary info
}
```

### Related Events
- `tengu_streaming_tool_execution_used` — streaming tool execution was utilized
- `tengu_streaming_tool_execution_not_used` — streaming execution available but not used

---

## 23. Post-Sampling Hooks

### Function: `Zif()`
```javascript
Zif(messages, systemPrompt, userContext, systemContext, toolUseContext, querySource)
```

### When it fires
- After **every** LLM sampling call completes
- Has access to the full conversation state at that point
- Can inspect messages, system prompt, and all context layers

### Purpose
- Internal instrumentation point for post-response analysis
- Enables automated quality checks or content monitoring
- Not user-configurable — hardcoded in the binary

---

## 24. Cost Tracking

### Architecture
- **Accumulator**: `T$.totalCostUSD` — running total for the session
- **Getter**: `eY()` — returns current `totalCostUSD`
- **Per-event**: `total_cost_usd` included in result events

### Threshold Warnings
- `tengu_cost_threshold_reached` — session cost exceeded a configured threshold
- `tengu_cost_threshold_acknowledged` — user acknowledged the warning

### Control
```bash
export DISABLE_COST_WARNINGS=true   # suppress cost threshold notifications
```

---

## 25. Feedback & Bug Reports

### Feedback Survey
- **Setting**: `feedbackSurveyRate` (0.0–1.0 probability)
- **Event**: `tengu_feedback_survey_event` — survey was shown
- Random sampling: `Math.random() < feedbackSurveyRate`

### Accept/Reject Feedback
- `tengu_accept_submitted` — user accepted a tool result with optional feedback
- `tengu_reject_submitted` — user rejected a tool result with feedback metadata
- Includes: `{ feedback, tool_name, model, session_id }`

### Bug Reports
- `tengu_bug_report_submitted` — user submitted a bug report via `/bug` command
- `tengu_bug_report_description` — sent to 1P logging with description text
- **Gate**: `DISABLE_BUG_COMMAND=true` disables the `/bug` command

### Control
```bash
export DISABLE_BUG_COMMAND=true       # disable /bug command
export DISABLE_FEEDBACK_COMMAND=true  # disable /feedback command
```

---

## 26. Enterprise OTEL Auth (`otelHeadersHelper`)

### Architecture
- **Setting**: `otelHeadersHelper` in enterprise managed settings
- **Purpose**: Path to a script that outputs OTEL authentication headers dynamically
- **Use case**: Enterprise deployments where OTEL auth tokens rotate (e.g., short-lived OIDC tokens)

### How it works
1. Enterprise admin sets `otelHeadersHelper: "/path/to/token-script.sh"` in managed settings
2. Before each OTEL export, Claude Code executes the script
3. Script stdout is parsed as headers and merged into OTEL exporter config
4. Requires trust dialog acceptance: `tengu_mcp_headersHelper_missing_trust`

### Security
- Only available via managed settings (not user-configurable)
- Trust dialog must be accepted before script execution
- Script runs with Claude Code's user permissions

---

## 27. Additional Environment Variables (Discovered)

| Variable | Default | Description |
|----------|---------|-------------|
| `DISABLE_ERROR_REPORTING` | false | Suppress error reporting to Anthropic |
| `DISABLE_BUG_COMMAND` | false | Disable `/bug` command |
| `DISABLE_FEEDBACK_COMMAND` | false | Disable `/feedback` command |
| `DISABLE_COST_WARNINGS` | false | Suppress cost threshold warnings |
| `DISABLE_AUTOUPDATER` | false | Disable auto-update checks |
| `CLAUDE_CODE_DATADOG_FLUSH_INTERVAL_MS` | 15000 | DataDog batch flush interval |
| `DISABLE_TELEMETRY` | false | Kill ALL non-essential telemetry |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | false | Alias for `DISABLE_TELEMETRY` |
| `CLAUDE_CODE_ATTRIBUTION_HEADER` | true | Enable billing attribution header |
| `CLAUDE_CODE_PERFETTO_TRACE` | unset | Path for Perfetto trace output |
| `ENABLE_BETA_TRACING_DETAILED` | false | Enable beta tracing pipeline |
| `BETA_TRACING_ENDPOINT` | unset | Endpoint for beta traces |
| `CLAUDE_CODE_DEBUG_LOGS_DIR` | `~/.claude/debug/` | Debug log directory |
| `CLAUDE_CODE_DEBUG_LOG_LEVEL` | debug | Log level filter |
