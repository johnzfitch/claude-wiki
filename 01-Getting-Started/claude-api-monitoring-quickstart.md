# Claude API Monitoring - Quick Start

## Installation Complete

All components have been configured:

1. **MITMproxy Logger**: `~/.local/bin/claude-api-logger.py`
   - Stealth mode enabled (read-only, no traffic modification)
   - Logs to: `~/.claude/api-logs/`
   - Redacts sensitive headers in logs

2. **Proxy Launcher**: `~/.local/bin/start-claude-proxy`
   - Runs on port 8888 by default (avoids interfering with normal web traffic)
   - Quiet mode for minimal output
   - Streams large bodies efficiently

3. **Monitoring Dashboard**: `~/.local/bin/start-claude-monitoring`
   - Starts both terminal viewer and proxy
   - One-command setup

4. **Terminal Viewer**: Updated at `/home/zack/dev/claude-terminal-viewer`
   - New "API Calls" filter
   - Orange badges for API logs
   - JSON-formatted display

## Quick Start (3 Steps)

### 1. Install MITMproxy CA Certificate

**First time only:**

```bash
# Start proxy to generate certificates
start-claude-proxy
# Press Ctrl+C after a few seconds

# Install certificate (Arch Linux)
sudo trust anchor --store ~/.mitmproxy/mitmproxy-ca-cert.pem

# Verify
trust list | grep -i mitmproxy
```

### 2. Start Monitoring

**Option A - All-in-one (recommended):**
```bash
start-claude-monitoring
```

**Option B - Individual components:**
```bash
# Terminal 1: Start viewer
cd ~/dev/claude-terminal-viewer && npm run dev -- --port 3001

# Terminal 2: Start proxy
start-claude-proxy
```

### 3. Configure Application to Use Proxy

**For Claude Desktop or any application:**

```bash
HTTP_PROXY=http://localhost:8888 \
HTTPS_PROXY=http://localhost:8888 \
NODE_EXTRA_CA_CERTS="$HOME/.mitmproxy/mitmproxy-ca-cert.pem" \
claude-desktop
```

**Or create a launcher script:**
```bash
#!/usr/bin/env bash
# ~/.local/bin/claude-desktop-monitored

export HTTP_PROXY="http://localhost:8888"
export HTTPS_PROXY="http://localhost:8888"
export NODE_EXTRA_CA_CERTS="$HOME/.mitmproxy/mitmproxy-ca-cert.pem"

exec /usr/bin/claude-desktop "$@"
```

Make it executable:
```bash
chmod +x ~/.local/bin/claude-desktop-monitored
```

## Viewing Logs

1. Open browser: http://localhost:3001
2. Select filter: "API Calls Only"
3. Click any API call to view full request/response

## Stealth Features

The setup is designed to be transparent:

- **No traffic modification**: Logs only, never alters requests/responses
- **Quiet operation**: Minimal console output
- **Sensitive data handling**: API keys redacted in logs (first 4 + last 4 chars)
- **Fail-safe**: Errors don't break connections
- **Efficient streaming**: Large responses handled properly

## Troubleshooting

### No logs appearing?

```bash
# Check proxy is running
netstat -tulpn | grep 8888

# Check log directory
ls -la ~/.claude/api-logs/

# Check if app is using proxy
ss -tunap | grep ESTABLISHED | grep 8888
```

### Certificate errors?

```bash
# Regenerate certificates
rm -rf ~/.mitmproxy
start-claude-proxy  # Run and stop with Ctrl+C
sudo trust anchor --store ~/.mitmproxy/mitmproxy-ca-cert.pem
```

### Terminal viewer not showing API logs?

```bash
# Restart viewer
cd ~/dev/claude-terminal-viewer
npm run dev -- --port 3001
```

## Architecture Analysis

Once running, you can:

1. **Inspect Request Structure**: See how Claude API requests are formatted
2. **Monitor Token Usage**: Track token consumption per request
3. **Debug API Issues**: View exact error responses
4. **Understand Session Flow**: See how conversations are maintained
5. **Rate Limit Monitoring**: Track API usage patterns

## Security Notes

- Logs contain API keys (redacted, but still sensitive)
- Set proper permissions: `chmod 600 ~/.claude/api-logs/*`
- Development use only
- Keep MITMproxy certificate secure

## Advanced Usage

### Custom Proxy Port

```bash
CLAUDE_PROXY_PORT=9090 start-claude-monitoring
```

### Verbose Logging

```bash
start-claude-proxy --set console_eventlog_verbosity=debug
```

### Filter Specific Endpoints

Edit `~/.local/bin/claude-api-logger.py` and modify the host check:

```python
if "api.anthropic.com" in flow.request.pretty_host:
    # Only log API calls, not web traffic
```

## Full Documentation

See: `/home/zack/dev/claude-api-monitoring-setup.md`

---

**Ready to monitor!** Run `start-claude-monitoring` to begin.
