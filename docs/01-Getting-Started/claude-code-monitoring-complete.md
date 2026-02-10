# Claude Code API Monitoring - Complete Setup

## Overview

Your Claude Code CLI is now configured to route through MITMproxy with **real-time ping/pong visibility**. You'll see every API request and response as they happen, with detailed timing and token usage information.

## What's Configured

### 1. Enhanced API Logger
Location: `~/.local/bin/claude-api-logger.py`

**New Features:**
- **Request Tracking**: Each request gets a unique ID
- **PING/PONG Display**: Real-time console output showing:
  - → PING: Outgoing requests with model info
  - ← PONG: Responses with status, timing, and token usage
- **Response Time**: Measures exact milliseconds for each API call
- **Token Metrics**: Shows input/output token counts
- **Dual Logging**:
  - Detailed JSONL logs: `~/.claude/api-logs/session_*.jsonl`
  - Real-time log: `~/.claude/api-logs/realtime.log`

### 2. Antigravity Integration
Your existing setup at `/home/zack/dev/antigravityresearch/launch-claude-code.sh` routes Claude Code through MITMproxy using cgroups.

### 3. Terminal Viewer
Already running at http://localhost:3001 - now includes API call filtering.

## How to Use

### Start Monitoring

```bash
# Terminal 1: Start the monitoring proxy
start-claude-monitoring
```

This will show real-time output like:
```
[15:30:45.123] → PING #1 | POST /v1/messages | Model: claude-opus-4-20250514
[15:30:47.456] ← PONG #1 ✓ | 200 | 2333ms | Tokens: in:1234 out:5678
[15:30:50.789] → PING #2 | POST /v1/messages | Model: claude-sonnet-4-5-20250929
[15:30:51.012] ← PONG #2 ✓ | 200 | 223ms | Tokens: in:890 out:1234
```

### Launch Claude Code

```bash
# Terminal 2: Normal claude alias (already configured)
claude
```

Your alias runs `/home/zack/dev/antigravityresearch/launch-claude-code.sh` which:
1. Starts antigravity-proxy service if needed
2. Adds process to cgroup for transparent routing
3. Sets NODE_EXTRA_CA_CERTS for MITMproxy
4. Launches Claude Code

### View in Terminal Viewer

Open http://localhost:3001
- Filter by "API Calls Only"
- See full JSON request/response details
- Browse by timestamp

## Real-Time Output Format

### PING (Request)
```
→ PING #<id> | <METHOD> <PATH> | Model: <model-name>
```

Example:
```
→ PING #5 | POST /v1/messages | Model: claude-opus-4-20250514
```

### PONG (Response)
```
← PONG #<id> <status-icon> | <status-code> | <response-time>ms | Tokens: in:<input> out:<output>
```

Examples:
```
← PONG #5 ✓ | 200 | 1845ms | Tokens: in:2340 out:8721
← PONG #6 ✗ | 429 | 120ms
```

Status icons:
- ✓ = Success (200-399)
- ✗ = Error (400+)

## Log Files

### JSONL Logs (Detailed)
```bash
# Latest session
ls -ltr ~/.claude/api-logs/session_*.jsonl | tail -1

# View latest requests
tail -50 ~/.claude/api-logs/session_$(date +%Y%m%d)_*.jsonl | jq .
```

### Real-Time Log
```bash
# Watch live
tail -f ~/.claude/api-logs/realtime.log

# Today's traffic
cat ~/.claude/api-logs/realtime.log
```

## Example Session Output

```
[15:30:45.123] → PING #1 | POST /v1/messages | Model: claude-opus-4-20250514
[15:30:47.456] ← PONG #1 ✓ | 200 | 2333ms | Tokens: in:1234 out:5678

[15:30:50.789] → PING #2 | POST /v1/messages | Model: claude-opus-4-20250514
[15:30:52.901] ← PONG #2 ✓ | 200 | 2112ms | Tokens: in:5678 out:12340

[15:31:00.123] → PING #3 | POST /v1/messages | Model: claude-sonnet-4-5-20250929
[15:31:00.456] ← PONG #3 ✓ | 200 | 333ms | Tokens: in:1000 out:2000
```

## Understanding the Data

### Request ID
Sequential counter for matching requests to responses.

### Response Time
- Measured in milliseconds
- Starts when request is sent
- Ends when response is received
- Includes network latency + API processing time

### Token Usage
- **Input tokens**: Your prompt + context
- **Output tokens**: Claude's response
- Only shown for successful responses with usage data

## What You Can See

### 1. Model Selection
See which model (Opus, Sonnet, Haiku) is being used for each request.

### 2. API Patterns
- How often requests are made
- Which endpoints are called
- Request/response timing

### 3. Token Consumption
- Real-time token usage
- Compare token efficiency across models
- Track cumulative usage

### 4. Performance Metrics
- Response times per model
- Network latency
- API processing time

### 5. Error Patterns
- Rate limits (429)
- Authentication issues (401, 403)
- Server errors (500+)

## Advanced Usage

### Filter by Model in Logs

```bash
# Only Opus calls
grep "claude-opus" ~/.claude/api-logs/realtime.log

# Only Sonnet calls
grep "claude-sonnet" ~/.claude/api-logs/realtime.log
```

### Calculate Average Response Time

```bash
# Extract response times
grep "PONG" ~/.claude/api-logs/realtime.log | \
  grep -oP '\d+ms' | \
  sed 's/ms//' | \
  awk '{sum+=$1; count++} END {print "Average:", sum/count, "ms"}'
```

### Total Token Usage

```bash
# Parse JSONL for usage stats
cat ~/.claude/api-logs/session_*.jsonl | \
  jq -s '[.[] | select(.type=="response" and .body.usage) | .body.usage] | {
    total_input: map(.input_tokens) | add,
    total_output: map(.output_tokens) | add
  }'
```

## Troubleshooting

### No PING/PONG output?

1. Check proxy is running:
   ```bash
   ps aux | grep mitmdump
   ```

2. Check Claude is using proxy:
   ```bash
   ps aux | grep claude | grep -v grep
   # Should see process in cgroup
   ```

3. Check logs are being written:
   ```bash
   ls -ltr ~/.claude/api-logs/
   ```

### Logs but no real-time output?

Check console log file:
```bash
tail -f ~/.claude/api-logs/realtime.log
```

If file exists but terminal shows nothing, the output is being written to the log file but not stdout (this is normal in background mode).

### Timing seems off?

Response time is measured from when MITMproxy sees the request until it sees the response. This includes:
- Network latency to Anthropic servers
- API processing time
- Streaming delay (if applicable)

## Port Configuration

- **Terminal Viewer**: Port 3001
- **MITMproxy**: Port 8888 (isolated from normal web traffic)
- **Antigravity Service**: Uses cgroups for transparent routing

## Benefits of This Setup

1. **Complete Visibility**: See every API interaction
2. **Real-Time Feedback**: Immediate ping/pong display
3. **Performance Monitoring**: Track response times
4. **Token Tracking**: Monitor usage and costs
5. **Debugging**: Inspect full request/response details
6. **Architecture Understanding**: Learn Claude API patterns
7. **Model Comparison**: Compare Opus vs Sonnet performance

## Next Steps

1. **Start monitoring**: `start-claude-monitoring`
2. **Use Claude normally**: `claude`
3. **Watch the ping/pong**: See real-time API traffic
4. **Analyze patterns**: Review logs and metrics
5. **Optimize usage**: Use insights to improve efficiency

---

**Status**: ✅ Complete and ready
**Real-time logs**: `tail -f ~/.claude/api-logs/realtime.log`
**Web viewer**: http://localhost:3001
**Current model**: Check PING messages for model info

The setup is completely transparent - Claude Code works normally while you get full visibility into every API call!
