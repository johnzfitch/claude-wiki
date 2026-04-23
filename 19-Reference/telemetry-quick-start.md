---
title: "Claude Code Telemetry — Quick Start Guide"
category: "19-Reference"
tags: ["claude-code", "search"]
---

# Claude Code Telemetry — Quick Start Guide

## TL;DR

Claude Code has **full OpenTelemetry support** but it's **disabled by default**. Enable it to track:
- User interactions & prompts
- LLM API calls (tokens, latency, cache hits)
- Tool executions (Read, Write, Bash, etc.)
- Hook system invocations
- Feature flag experiments

---

## 30-Second Setup (Local Jaeger)

```bash
# 1. Start Jaeger
docker run -d --name jaeger \
  -p 4318:4318 -p 16686:16686 \
  jaegertracing/all-in-one:latest

# 2. Enable telemetry
export CLAUDE_CODE_ENABLE_TELEMETRY=true
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
export OTEL_SERVICE_NAME=claude-code

# 3. Run Claude
claude

# 4. View traces at http://localhost:16686
```

---

## Privacy-Safe Configuration

**DO NOT** enable these in production without sanitization:

```bash
# ❌ DANGER: Logs raw user prompts (PII)
export OTEL_LOG_USER_PROMPTS=true

# ❌ DANGER: Logs tool outputs (file contents, shell output)
export OTEL_LOG_TOOL_CONTENT=true

# ❌ CAUTION: Includes account UUID in metrics
export OTEL_METRICS_INCLUDE_ACCOUNT_UUID=true
```

**Recommended safe settings**:

```bash
export OTEL_LOG_USER_PROMPTS=false
export OTEL_LOG_TOOL_CONTENT=false
export OTEL_METRICS_INCLUDE_ACCOUNT_UUID=false
export OTEL_METRICS_INCLUDE_SESSION_ID=true   # Safe: random session ID
export OTEL_METRICS_INCLUDE_VERSION=true      # Safe: version string
```

---

## Production Backends

### Honeycomb

```bash
export CLAUDE_CODE_ENABLE_TELEMETRY=true
export OTEL_EXPORTER_OTLP_ENDPOINT=https://api.honeycomb.io
export OTEL_EXPORTER_OTLP_HEADERS="x-honeycomb-team=YOUR_API_KEY"
export OTEL_SERVICE_NAME=claude-code
export OTEL_RESOURCE_ATTRIBUTES="service.version=2.1.76,env=prod"
```

### DataDog

```bash
export CLAUDE_CODE_ENABLE_TELEMETRY=true
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318  # DataDog Agent
export OTEL_SERVICE_NAME=claude-code
export OTEL_RESOURCE_ATTRIBUTES="env:prod,version:2.1.76"
```

### New Relic

```bash
export CLAUDE_CODE_ENABLE_TELEMETRY=true
export OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp.nr-data.net:4318
export OTEL_EXPORTER_OTLP_HEADERS="api-key=YOUR_LICENSE_KEY"
export OTEL_SERVICE_NAME=claude-code
```

### Grafana Cloud (Tempo)

```bash
export CLAUDE_CODE_ENABLE_TELEMETRY=true
export OTEL_EXPORTER_OTLP_ENDPOINT=https://tempo-<instance>.grafana.net:443
export OTEL_EXPORTER_OTLP_HEADERS="Authorization=Basic $(echo -n '<instance_id>:<api_key>' | base64)"
export OTEL_SERVICE_NAME=claude-code
```

---

## Perfetto Trace Capture

> **DISABLED in 2.1.78**: Perfetto tracing is dead code. The enable flag
> is never activated. Setting `CLAUDE_CODE_PERFETTO_TRACE` has no effect.
> Use OTEL traces or `CLAUDE_CODE_PROFILE_STARTUP=1` instead.

Perfetto gives you **single-file, shareable performance traces** (like Chrome DevTools).

```bash
# Set output path
export CLAUDE_CODE_PERFETTO_TRACE=$HOME/traces/session-$(date +%s).pftrace

# Run Claude session
claude

# View at https://ui.perfetto.dev (drag-drop the .pftrace file)
```

**Use Cases**:
- Performance regression hunting
- Timing analysis (TTFT, cache efficiency)
- Share traces with team (no backend required)

---

## What Gets Traced

### 1. Interactions (Top-Level)
```
claude_code.interaction
├── user_prompt: "<REDACTED>" (unless OTEL_LOG_USER_PROMPTS=true)
├── user_prompt_length: 145
├── interaction.sequence: 42
└── duration_ms: 3420
```

### 2. LLM Requests
```
claude_code.llm_request (parent: interaction)
├── model: "claude-sonnet-4-5"
├── speed: "normal"
├── input_tokens: 8234
├── output_tokens: 512
├── cache_read_tokens: 7800
├── cache_creation_tokens: 434
├── ttft_ms: 240
├── duration_ms: 2800
└── success: true
```

### 3. Tool Executions
```
claude_code.tool (parent: interaction)
├── tool_name: "Read"
├── result_tokens: 1234
├── duration_ms: 15
└── success: true

claude_code.tool.blocked_on_user
├── decision: "approve"
├── source: "permission_prompt"
└── duration_ms: 2500

claude_code.tool.execution
├── success: true
└── duration_ms: 150
```

### 4. Hooks (2.1.70+)
```
claude_code.hook
├── hook_event: "PreToolUse"
├── hook_name: "security-scanner.sh"
├── num_hooks: 3
├── num_success: 2
├── num_blocking: 1
└── duration_ms: 85
```

---

## Useful Queries

### Average TTFT by Model
```sql
-- Honeycomb
AVG(ttft_ms) WHERE span.type = "llm_request" GROUP BY model
```

### Cache Hit Rate
```sql
-- Calculate cache efficiency
SUM(cache_read_tokens) / SUM(input_tokens) WHERE span.type = "llm_request"
```

### Tool Success Rate
```sql
-- Tool reliability
COUNT(success = true) / COUNT(*) WHERE span.type = "tool" GROUP BY tool_name
```

### Permission Friction
```sql
-- How often users wait for permission prompts
P95(duration_ms) WHERE span.type = "tool.blocked_on_user"
```

---

## Feature Flags (For Experiments)

Claude Code uses **GrowthBook** internally. You can check which experiments you're in:

```bash
# Enable experiment logging
export CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=true

# Look for "growthbook_experiment" events in your traces
```

**Known interesting flags** (2.1.76):
- `tengu_tst_kx7` — Tool search experiment
- `tengu_defer_all_bn4` — Defer all tools (default: true)
- `tengu_mcp_elicitation` — MCP elicitation feature
- `tengu_trace_lantern` — Debug/trace mode
- `enhanced_telemetry_beta` — Enhanced internal telemetry

---

## Advanced: Custom OTEL Configuration

### Different Protocols
```bash
# gRPC (faster, binary)
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317

# HTTP/JSON (easier debugging)
export OTEL_EXPORTER_OTLP_PROTOCOL=http/json
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
```

### Separate Trace/Metric/Log Endpoints
```bash
export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://tempo:4318/v1/traces
export OTEL_EXPORTER_OTLP_METRICS_ENDPOINT=http://prometheus:4318/v1/metrics
export OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=http://loki:4318/v1/logs
```

### Batch Tuning (High-Volume)
```bash
# Larger batches, less frequent exports
export OTEL_BLRP_MAX_EXPORT_BATCH_SIZE=2048
export OTEL_BLRP_MAX_QUEUE_SIZE=8192
export OTEL_BLRP_SCHEDULE_DELAY=10000  # 10 seconds
export OTEL_METRIC_EXPORT_INTERVAL=120000  # 2 minutes
```

---

## Troubleshooting

### No traces appearing?

1. **Check if telemetry is enabled**:
   ```bash
   echo $CLAUDE_CODE_ENABLE_TELEMETRY
   # Should be "true" or "1"
   ```

2. **Verify endpoint is reachable**:
   ```bash
   curl -v $OTEL_EXPORTER_OTLP_ENDPOINT/v1/traces
   # Should get HTTP 405 (Method Not Allowed) — that's OK, means it's alive
   ```

3. **Check for export errors**:
   - Claude Code will log OTEL export failures to stderr
   - Look for "ExportResultCode.FAILED" in output

### Traces truncated or missing data?

- **User prompts redacted**: Set `OTEL_LOG_USER_PROMPTS=true` (PII risk!)
- **Tool outputs missing**: Set `OTEL_LOG_TOOL_CONTENT=true` (PII risk!)
- **No session ID**: `OTEL_METRICS_INCLUDE_SESSION_ID=true` (default)

### Performance impact?

- **Minimal** when disabled (default)
- **~1-5% overhead** when enabled with remote export
- **Negligible** with Perfetto (local file write)

**Batch tuning helps**:
```bash
# Reduce export frequency
export OTEL_BLRP_SCHEDULE_DELAY=30000  # 30 seconds
export OTEL_METRIC_EXPORT_INTERVAL=300000  # 5 minutes
```

---

## Research Use Cases

### 1. Prompt Caching Analysis
**Question**: How effective is prompt caching across sessions?

```sql
SELECT
  model,
  AVG(cache_read_tokens / NULLIF(input_tokens, 0)) as cache_hit_rate,
  COUNT(*) as request_count
FROM spans
WHERE span.type = 'llm_request'
  AND cache_read_tokens > 0
GROUP BY model
```

### 2. Tool Latency Distribution
**Question**: Which tools are slowest? Where should we optimize?

```sql
SELECT
  tool_name,
  P50(duration_ms) as p50,
  P95(duration_ms) as p95,
  P99(duration_ms) as p99
FROM spans
WHERE span.type = 'tool'
GROUP BY tool_name
ORDER BY p95 DESC
```

### 3. Retry Pattern Analysis
**Question**: What error codes trigger retries? How many attempts on average?

```sql
SELECT
  status_code,
  AVG(attempt) as avg_attempts,
  MAX(attempt) as max_attempts,
  COUNT(*) as occurrences
FROM spans
WHERE span.type = 'llm_request'
  AND attempt > 1
GROUP BY status_code
```

### 4. Feature Flag Impact
**Question**: Does `tengu_defer_all_bn4` change interaction latency?

```sql
-- Correlate growthbook_experiment events with interaction spans
-- Requires joining event data with span data (backend-specific)
```

---

## What's NOT Available

❌ **Model behavior analysis** (no activations, no interpretability)
❌ **Alignment signals** (no HHH scoring, no safety metrics)
❌ **Red-teaming infrastructure** (no jailbreak detection)
❌ **Constitutional AI markers** (no reward model scores)

This is **operational telemetry** only — it tells you if the system is working, not if the model is behaving correctly.

---

## Next Steps

1. **Start simple**: Run Jaeger locally, enable telemetry, see what you get
2. **Explore spans**: Look at the hierarchy (interaction → LLM → tool)
3. **Build dashboards**: Token usage, latency percentiles, error rates
4. **Hunt regressions**: Capture baseline traces, compare versions
5. **Share findings**: Perfetto traces are self-contained, easy to share

For production use, see the full report: `telemetry-observability-report.md`
