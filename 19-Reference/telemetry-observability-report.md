---
title: "Claude Code 2.1.76 — Telemetry & Observability Report"
category: "19-Reference"
tags: ["claude-code", "sdk", "search", "security"]
---

# Claude Code 2.1.76 — Telemetry & Observability Report

## Executive Summary

Claude Code 2.1.76 contains comprehensive telemetry infrastructure built on **OpenTelemetry** (OTEL) with **GrowthBook** (feature flags), **Statsig** (gates), and **Perfetto** tracing integration. The system tracks interactions, LLM requests, tool executions, and hook calls with structured spans, metrics, and events.

---

## 1. OpenTelemetry (OTEL) SDK

### Core Architecture
- **SDK**: Full OTEL JS SDK embedded (traces, metrics, logs)
- **Exporters**: OTLPTraceExporter, OTLPMetricExporter, OTLPLogExporter
- **Processors**: BatchSpanProcessor (configurable batch size, schedule delay)
- **Context**: AsyncLocalStorage-based span context propagation
- **Tracer**: `com.anthropic.claude_code.tracing` v1.0.0

### Span Types & Attributes

#### 1. `claude_code.interaction`
**Span Type**: Top-level user interaction
**Attributes**:
- `user_prompt` (string, redacted unless OTEL_LOG_USER_PROMPTS=true)
- `user_prompt_length` (int)
- `interaction.sequence` (int, incremental counter)
- `interaction.duration_ms` (int, set on end)
- `span.type` = "interaction"

**Lifecycle**:
- Start: `F8f(userPrompt)` — triggered by user input
- End: `JgH()` — sets duration, closes span
- Perfetto integration: `p8f()` creates corresponding Perfetto span

#### 2. `claude_code.llm_request`
**Span Type**: LLM API call (streaming or non-streaming)
**Attributes**:
- `model` (string, e.g., "claude-sonnet-4-5")
- `llm_request.context` ("interaction" | "standalone")
- `speed` ("fast" | "normal")
- `query_source` (optional, from request metadata)
- `duration_ms` (int)
- `input_tokens`, `output_tokens` (int)
- `cache_read_tokens`, `cache_creation_tokens` (int)
- `success` (bool)
- `status_code` (int, HTTP status)
- `error` (string, if failed)
- `attempt` (int, retry count)
- `response.has_tool_call` (bool)
- `ttft_ms` (int, time-to-first-token)

**Lifecycle**:
- Start: `c8f(model, metadata, ?, isFast)` — before API call
- End: `SkA(span, results)` — after response completes
- Parent: interaction span (if exists)

#### 3. `claude_code.tool`
**Span Type**: Tool invocation (Read, Write, Bash, etc.)
**Attributes**:
- `tool_name` (string)
- `span.type` = "tool"
- `duration_ms` (int)
- `result_tokens` (int, token count of result)
- `success` (bool)
- **Tool-specific attributes** (via `V8f()` — maps tool name to custom attributes)

**Lifecycle**:
- Start: `Q8f(toolName, attrs, ?)`
- End: `L2$(metadata, resultTokens)`
- Parent: interaction span
- Events: `i8f(eventName, attrs)` for tool output logging (if OTEL_LOG_TOOL_CONTENT=true)

#### 4. `claude_code.tool.blocked_on_user`
**Span Type**: Permission prompt / user input required
**Attributes**:
- `span.type` = "tool.blocked_on_user"
- `duration_ms` (int)
- `decision` (string, e.g., "approve", "deny")
- `source` (string, e.g., "permission_prompt")

**Lifecycle**:
- Start: `l8f()` — when tool blocked
- End: `RkA(decision, source)` — after user responds

#### 5. `claude_code.tool.execution`
**Span Type**: Actual tool execution (after approval)
**Attributes**:
- `span.type` = "tool.execution"
- `duration_ms` (int)
- `success` (bool)
- `error` (string, if failed)

**Lifecycle**:
- Start: `n8f()` — tool starts executing
- End: `CkA(metadata)` — execution completes

#### 6. `claude_code.hook`
**Span Type**: Hook system invocation (new in 2.1.70)
**Attributes**:
- `hook_event` (string, e.g., "PreToolUse", "PostToolUse", "InstructionsLoaded")
- `hook_name` (string, script name)
- `num_hooks` (int, total hooks for this event)
- `hook_definitions` (JSON string, hook config)
- `duration_ms` (int)
- `num_success` (int)
- `num_blocking` (int)
- `num_non_blocking_error` (int)
- `num_cancelled` (int)

**Lifecycle**:
- Start: `r8f(event, name, numHooks, defs)`
- End: `o8f(span, stats)`

---

## 2. Environment Variables

### Telemetry Control

| Variable | Type | Default | Purpose |
|----------|------|---------|---------|
| `CLAUDE_CODE_ENABLE_TELEMETRY` | bool | false | Master switch for 3rd-party OTEL export |
| `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA` | bool | false | Enhanced internal telemetry (alias: `ENABLE_ENHANCED_TELEMETRY_BETA`) |
| `CLAUDE_CODE_PERFETTO_TRACE` | string | unset | Path to Perfetto trace file (enables Perfetto export) |
| `OTEL_LOG_USER_PROMPTS` | bool | false | Include raw user prompts in spans (PII risk) |
| `OTEL_LOG_TOOL_CONTENT` | bool | false | Include tool output in span events (PII risk) |

### OTEL Configuration (Standard OTEL Env Vars)

| Variable | Default | Description |
|----------|---------|-------------|
| `OTEL_EXPORTER_OTLP_ENDPOINT` | - | Base OTLP endpoint URL |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | http/protobuf | grpc \| http/protobuf \| http/json |
| `OTEL_EXPORTER_OTLP_HEADERS` | - | Auth headers (e.g., `x-api-key=...`) |
| `OTEL_EXPORTER_OTLP_TRACES_HEADERS` | - | Trace-specific headers |
| `OTEL_EXPORTER_OTLP_METRICS_HEADERS` | - | Metric-specific headers |
| `OTEL_EXPORTER_OTLP_LOGS_HEADERS` | - | Log-specific headers |
| `OTEL_LOGS_EXPORTER` | - | Exporter type (otlp, console, none) |
| `OTEL_LOGS_EXPORT_INTERVAL` | 10000 | Log batch export interval (ms) |
| `OTEL_METRICS_EXPORTER` | - | Exporter type (otlp, console, prometheus, none) |
| `OTEL_METRIC_EXPORT_INTERVAL` | 60000 | Metric export interval (ms) |
| `OTEL_RESOURCE_ATTRIBUTES` | - | Resource attrs (e.g., `service.name=claude-code`) |
| `OTEL_SERVICE_NAME` | - | Service name (overrides resource attrs) |

### Metric Attributes (Custom)

| Variable | Type | Default | Effect |
|----------|------|---------|--------|
| `OTEL_METRICS_INCLUDE_SESSION_ID` | bool | true | Add `session.id` to metrics |
| `OTEL_METRICS_INCLUDE_VERSION` | bool | false | Add `service.version` to metrics |
| `OTEL_METRICS_INCLUDE_ACCOUNT_UUID` | bool | true | Add account UUID to metrics |

### OTEL Batch Processor Config

| Variable | Default | Description |
|----------|---------|-------------|
| `OTEL_BLRP_MAX_EXPORT_BATCH_SIZE` | 512 | Max logs per batch |
| `OTEL_BLRP_MAX_QUEUE_SIZE` | 2048 | Max queue size before drop |
| `OTEL_BLRP_SCHEDULE_DELAY` | 5000 | Batch export delay (ms) |
| `OTEL_BLRP_EXPORT_TIMEOUT` | 30000 | Export timeout (ms) |

---

## 3. Metrics & Events

### 1P Event Logging
- **Logger**: `com.anthropic.claude_code.events` (via `qAH`)
- **Backend**: Anthropic 1st-party event pipeline (batch processor)
- **Config**: `tengu_1p_event_batch_config` (GrowthBook dynamic config)
- **Enabled**: `is1PEventLoggingEnabled()` checks internal auth state
- **Batch Settings**:
  - `scheduledDelayMillis`: 10000 (default)
  - `maxExportBatchSize`: 200
  - `maxQueueSize`: 8192

### Event Types
1. **`growthbook_experiment`**
   - Logged when GrowthBook experiment evaluated
   - Attributes: `experiment_key`, `variation_id`, `in_experiment`
   - Function: `logGrowthBookExperimentTo1P()`

2. **`claude_code.<custom>`**
   - Generic event emitter: `A.emit({ body: `claude_code.${eventName}`, attributes })`
   - Used for ad-hoc instrumentation

### Resource Attributes (Auto-Detected)
- `host.name` (hostname)
- `host.arch` (x86_64, arm64, etc.)
- `host.id` (machine ID)
- `os.type` (Linux, Darwin, Windows)
- `os.version` (kernel version)
- `service.instance.id` (random UUID per process)
- `telemetry.sdk.name` = "opentelemetry"
- `telemetry.sdk.language` = "nodejs"
- `telemetry.sdk.version` (OTEL SDK version)

---

## 4. Feature Flags & Experiments

### GrowthBook
- **SDK**: Full GrowthBook JS SDK embedded
- **Backend**: `https://cdn.growthbook.io` (or custom `apiHost`)
- **Storage**: `cachedGrowthBookFeatures` in local state
- **Functions**:
  - `_A(featureKey, defaultValue)` — sync feature value getter
  - `AE(featureKey, defaultValue)` — alias for `_A()`
  - `evalFeature(key)` — returns `{on, off, value, source}`
  - `getFeatureValue(key, default)` — extracts value
  - `isOn(key)` / `isOff(key)` — boolean checks
  - `triggerExperiment(key)` — force experiment run
- **Tracking**: `trackedExperiments` Set (deduplicates logged experiments)
- **Refresh**: Periodic polling + auth change triggers

### Statsig
- **Storage**: `cachedStatsigGates` in local state
- **Functions**:
  - `MM(gateKey)` — sync gate check (CACHED, MAY BE STALE)
  - `liA(gateKey)` — async gate check (fresh)
- **Fallback**: If Statsig gate not found, checks GrowthBook feature

### Known Feature Flags (2.1.76)

| Flag | Type | Description |
|------|------|-------------|
| `enhanced_telemetry_beta` | bool | Enhanced internal telemetry |
| `tengu_tst_kx7` | ? | Tool search experiment |
| `tengu_plan_mode_interview_phase` | bool | Plan mode interview |
| `tengu_pewter_ledger` | ? | Unknown |
| `tengu_amber_flint` | bool | Unknown |
| `tengu_marble_anvil` | bool | Unknown |
| `tengu_turtle_carbon` | bool | Unknown |
| `tengu_grey_step2` | ? | Unknown |
| `tengu_attribution_header` | bool | Attribution header toggle |
| `tengu_granite_whisper` | bool | Unknown |
| `tengu_penguins_off` | ? | Unknown |
| `tengu_marble_sandcastle` | bool | Unknown |
| `tengu_mcp_elicitation` | bool | MCP elicitation feature |
| `tengu_herring_clock` | bool | Unknown |
| `tengu_coral_fern` | bool | Unknown |
| `tengu_swinburne_dune` | bool | Unknown |
| `tengu_passport_quail` | bool | Unknown |
| `tengu_paper_halyard` | bool | Unknown |
| `tengu_amber_quartz_disabled` | bool | Unknown |
| `tengu_lean_cast` | bool | Unknown |
| `tengu_amber_wren` | object | Unknown |
| `tengu_hawthorn_window` | ? | Unknown |
| `tengu_hawthorn_steeple` | bool | Unknown |
| `tengu_keybinding_customization_release` | bool | Keybinding customization |
| `tengu_pewter_gull` | bool | Unknown |
| `tengu_glacier_2xr` | bool | Unknown |
| `tengu_defer_all_bn4` | bool | Defer all (tool search?) |
| `tengu_tst_hint_m7r` | bool | Unknown |
| `tengu_trace_lantern` | bool | Trace/debug mode |
| `tengu_tight_weave` | bool | Unknown |
| `tengu_orchid_trellis` | bool | Unknown |
| `tengu_marble_whisper2` | bool | Unknown |
| `tengu_kairos_brief` | bool | Unknown |
| `tengu_pid_based_version_locking` | bool | PID-based version locking |
| `tengu_auto_mode_config` | object | Auto mode configuration |
| `tengu_1p_event_batch_config` | object | 1P event batch settings |

---

## 5. Perfetto Integration

### Activation
- **Env Var**: `CLAUDE_CODE_PERFETTO_TRACE=/path/to/trace.pftrace`
- **Detection**: `Sc()` function checks if Perfetto enabled
- **Format**: Perfetto protobuf trace format

### Span Mapping
- Each OTEL span gets a corresponding `perfettoSpanId`
- Stored in span context: `{span, attributes, perfettoSpanId}`
- Functions:
  - `p8f(prompt)` — create Perfetto interaction span
  - `U8f(spanId)` — end interaction span
  - `C8f({model, querySource, messageId})` — create LLM span
  - `u8f(spanId, metadata)` — end LLM span with tokens/timing
  - `b8f(toolName, metadata)` — create tool span
  - `x8f(spanId, {success, resultTokens})` — end tool span
  - `m8f(type)` — create permission span
  - `B8f(spanId, {decision, source})` — end permission span

### Perfetto Metadata
- **LLM spans**:
  - `ttftMs` (time-to-first-token)
  - `ttltMs` (time-to-last-token)
  - `promptTokens`, `outputTokens`
  - `cacheReadTokens`, `cacheCreationTokens`
  - `success`, `error`
  - `requestSetupMs`
  - `attemptStartTimes` (retry timing array)

---

## 6. Observability Signals — NO ALIGNMENT/INTERPRETABILITY

### What Exists
- ✅ Request/response tracing (LLM calls)
- ✅ Tool execution tracking
- ✅ Performance metrics (latency, tokens, cache hits)
- ✅ Error tracking (failures, retries)
- ✅ Feature flag evaluation logs
- ✅ User interaction flows

### What's MISSING
- ❌ **No alignment testing infrastructure** in binary
- ❌ **No interpretability hooks** (no SAE, probes, attribution)
- ❌ **No red-teaming signals** (no jailbreak detection, safety metrics)
- ❌ **No constitutional AI markers** (no HHH scoring, harmlessness checks)
- ❌ **No RLHF references** (reward models, preference data)
- ❌ **No model behavior analysis** (no activation logging, circuit analysis)

**Conclusion**: The telemetry is **purely operational** — it tracks system performance, not model behavior or alignment properties.

---

## 7. Practical Observability Access

### For Users (External Observability)

#### Minimal Setup (Jaeger)
```bash
# 1. Run Jaeger all-in-one
docker run -d --name jaeger \
  -p 4318:4318 \
  -p 16686:16686 \
  jaegertracing/all-in-one:latest

# 2. Configure Claude Code
export CLAUDE_CODE_ENABLE_TELEMETRY=true
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
export OTEL_SERVICE_NAME=claude-code
export OTEL_LOG_USER_PROMPTS=false  # Privacy: keep false
export OTEL_LOG_TOOL_CONTENT=false  # Privacy: keep false

# 3. Run Claude
claude

# 4. View traces
open http://localhost:16686
```

#### Production Setup (Honeycomb, DataDog, etc.)
```bash
export CLAUDE_CODE_ENABLE_TELEMETRY=true
export OTEL_EXPORTER_OTLP_ENDPOINT=https://api.honeycomb.io
export OTEL_EXPORTER_OTLP_HEADERS="x-honeycomb-team=YOUR_API_KEY"
export OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
export OTEL_SERVICE_NAME=claude-code
export OTEL_RESOURCE_ATTRIBUTES="service.version=2.1.76,deployment.environment=prod"
```

### For Research (Perfetto)
```bash
# Enable Perfetto trace capture
export CLAUDE_CODE_PERFETTO_TRACE=$HOME/claude-traces/session-$(date +%s).pftrace

# Run session
claude

# View in Perfetto UI
open https://ui.perfetto.dev
# Drag-drop the .pftrace file
```

---

## 8. Key Telemetry Functions (For Analysis)

### Enablement Checks
```javascript
// Master switch
BVf() → process.env.CLAUDE_CODE_ENABLE_TELEMETRY === "true"

// Enhanced telemetry (internal)
hkA() → CLAUDE_CODE_ENHANCED_TELEMETRY_BETA || enhanced_telemetry_beta flag

// Span creation enabled
JC() → hkA() || WO()  // WO() = enhanced mode check

// Tool content logging
sr1() → OTEL_LOG_TOOL_CONTENT === "true"

// User prompt logging (PII)
pr1() → OTEL_LOG_USER_PROMPTS === "true"
```

### Span Lifecycle
```javascript
// Interaction
F8f(prompt) → startInteractionSpan
JgH() → endInteractionSpan

// LLM
c8f(model, metadata, ?, isFast) → startLlmSpan
SkA(span, results) → endLlmSpan

// Tool
Q8f(toolName, attrs, ?) → startToolSpan
L2$(metadata, resultTokens) → endToolSpan

// Hook (2.1.70+)
r8f(event, name, numHooks, defs) → startHookSpan
o8f(span, stats) → endHookSpan
```

---

## 9. Research Opportunities

### Timing Analysis
- **TTFT (Time-To-First-Token)**: Measure streaming latency
- **Cache Efficiency**: Compare `cache_read_tokens` vs `input_tokens`
- **Retry Patterns**: Analyze `attemptStartTimes` for failure modes

### Tool Usage Patterns
- **Most-used tools**: Aggregate `tool_name` frequencies
- **Success rates**: `success=true` vs `success=false`
- **Permission friction**: Count `tool.blocked_on_user` spans

### Feature Flag Impact
- **Experiment correlation**: Join `growthbook_experiment` events with performance metrics
- **A/B test analysis**: Compare span durations across feature flag cohorts

### Performance Regression Detection
- **Baseline**: Capture traces on version N
- **Diff**: Compare span durations on version N+1
- **Alert**: Automated regression detection via span duration percentiles

---

## 10. Privacy & Security Notes

### PII Risk Vectors
1. **User Prompts**: Full text logged if `OTEL_LOG_USER_PROMPTS=true`
2. **Tool Outputs**: File contents, shell output if `OTEL_LOG_TOOL_CONTENT=true`
3. **File Paths**: Tool attributes may include absolute paths
4. **Account UUID**: Included in metrics if `OTEL_METRICS_INCLUDE_ACCOUNT_UUID=true`

### Recommended Settings (Production)
```bash
# Strict privacy
export OTEL_LOG_USER_PROMPTS=false
export OTEL_LOG_TOOL_CONTENT=false
export OTEL_METRICS_INCLUDE_ACCOUNT_UUID=false

# Safe observability
export CLAUDE_CODE_ENABLE_TELEMETRY=true
export OTEL_EXPORTER_OTLP_ENDPOINT=<internal-collector>
export OTEL_SERVICE_NAME=claude-code
```

---

## 11. Summary

**Strengths**:
- Full OTEL SDK with production-grade exporters
- Structured span hierarchy (interaction → LLM → tool → hook)
- GrowthBook + Statsig for dynamic feature control
- Perfetto integration for deep performance analysis
- Rich metadata (tokens, cache hits, retries, timing)

**Limitations**:
- No alignment/interpretability signals
- No model behavior analysis hooks
- PII exposure if logging enabled
- Default: telemetry **disabled** (requires opt-in)

**Bottom Line**: This is **operational telemetry**, not research infrastructure. It answers "Is the system working?" not "Is the model behaving correctly?"
