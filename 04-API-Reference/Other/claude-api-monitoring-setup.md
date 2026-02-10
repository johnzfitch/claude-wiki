# Claude API Monitoring Setup Guide

This guide will help you set up monitoring for Claude Opus API calls using MITMproxy and view them in your terminal viewer at localhost:3001.

## Overview

The setup consists of:
1. **MITMproxy** - Intercepts HTTPS traffic to capture API calls
2. **Claude API Logger** - Python addon that logs API requests/responses
3. **Terminal Viewer** - Web interface at localhost:3001 to view logs
4. **SSL Certificate** - Required for HTTPS interception

## Components

### 1. MITMproxy Addon Script
Location: `~/.local/bin/claude-api-logger.py`

This script intercepts all traffic to `api.anthropic.com` and `claude.ai`, logging:
- Request method, URL, headers, and body
- Response status, headers, and body
- Timestamps for all interactions

Logs are written to: `~/.claude/api-logs/session_YYYYMMDD_HHMMSS.jsonl`

### 2. Proxy Launcher
Location: `~/.local/bin/start-claude-proxy`

Usage:
```bash
# Start the proxy (runs on port 8888 by default)
start-claude-proxy

# Use a custom port
CLAUDE_PROXY_PORT=9090 start-claude-proxy
```

### 3. Terminal Viewer Updates
Location: `/home/zack/dev/claude-terminal-viewer`

The viewer now supports a new log type: **API Calls**
- Filter by "API Calls Only" to see intercepted API traffic
- Orange badge for API logs
- JSON-formatted display of requests/responses

## Setup Instructions

### Step 1: Install MITMproxy CA Certificate

MITMproxy generates a CA certificate that must be trusted by your system to intercept HTTPS traffic.

#### On Arch Linux:

1. Start the proxy once to generate certificates:
   ```bash
   start-claude-proxy
   # Press Ctrl+C after a few seconds
   ```

2. Install the CA certificate:
   ```bash
   sudo trust anchor --store ~/.mitmproxy/mitmproxy-ca-cert.pem
   ```

   Or manually:
   ```bash
   sudo cp ~/.mitmproxy/mitmproxy-ca-cert.pem /etc/ca-certificates/trust-source/anchors/mitmproxy.crt
   sudo trust extract-compat
   ```

3. Verify installation:
   ```bash
   trust list | grep -i mitmproxy
   ```

#### For Claude Desktop Application:

If Claude Desktop uses Electron, you may need to add the certificate to its trust store:

```bash
# Find Claude Desktop's certificate directory
# This varies by application

# Option 1: Set environment variable
export NODE_EXTRA_CA_CERTS="$HOME/.mitmproxy/mitmproxy-ca-cert.pem"

# Option 2: For Electron apps, disable certificate validation (INSECURE, dev only)
# Add to desktop file or launcher:
claude --ignore-certificate-errors
```

### Step 2: Configure Proxy

You need to configure the application to use the proxy. There are several methods:

#### Method 1: Environment Variables (Recommended - Only for Claude)
```bash
export HTTP_PROXY="http://localhost:8888"
export HTTPS_PROXY="http://localhost:8888"
export http_proxy="http://localhost:8888"
export https_proxy="http://localhost:8888"

# Then run your application
claude-desktop
```

**Important**: This only proxies the specific application you launch with these variables. Your normal web browsing is unaffected.

#### Method 2: Application-Specific Configuration (Recommended)

For Claude Desktop, create a launcher script:
```bash
#!/usr/bin/env bash
# ~/.local/bin/claude-desktop-proxied

export HTTP_PROXY="http://localhost:8888"
export HTTPS_PROXY="http://localhost:8888"
export NODE_EXTRA_CA_CERTS="$HOME/.mitmproxy/mitmproxy-ca-cert.pem"

/usr/bin/claude-desktop "$@"
```

This ensures ONLY Claude Desktop uses the proxy, leaving all other applications unaffected.

#### Method 3: System-Wide Proxy (NOT Recommended)
**Warning**: This will route ALL system traffic through the proxy, including your web browser.

1. Open System Settings > Network > Proxy
2. Select "Manually specify proxy settings"
3. Set HTTP and HTTPS proxy to `localhost:8888`
4. Add exceptions if needed (e.g., `localhost,127.0.0.1`)

Only use this if you want to monitor all applications.

Make it executable:
```bash
chmod +x ~/.local/bin/claude-desktop-proxied
```

### Step 3: Start All Components

1. Start the terminal viewer (if not already running):
   ```bash
   cd ~/dev/claude-terminal-viewer
   npm run dev -- --port 3001
   ```

2. Start the MITMproxy logger:
   ```bash
   start-claude-proxy
   ```

3. Launch Claude Desktop (with proxy configuration):
   ```bash
   # If using environment variables:
   HTTP_PROXY=http://localhost:8888 HTTPS_PROXY=http://localhost:8888 claude-desktop

   # Or if using launcher script:
   claude-desktop-proxied
   ```

4. Open the terminal viewer:
   ```
   http://localhost:3001
   ```

### Step 4: Verify Logging

1. Make a request in Claude Desktop (e.g., ask Opus a question)
2. Check the MITMproxy console output for intercepted requests
3. Check the terminal viewer at localhost:3001
4. Select "API Calls Only" filter
5. You should see the API requests/responses in orange badges

## Troubleshooting

### Certificate Errors

If you see SSL certificate verification errors:

1. Verify the certificate is installed:
   ```bash
   trust list | grep -i mitmproxy
   ```

2. Check certificate permissions:
   ```bash
   ls -la ~/.mitmproxy/
   ```

3. Regenerate certificates:
   ```bash
   rm -rf ~/.mitmproxy
   start-claude-proxy  # Regenerates certificates
   # Re-install using Step 1
   ```

### No Logs Appearing

1. Check proxy is running:
   ```bash
   netstat -tulpn | grep 8888
   ```

2. Verify log directory exists:
   ```bash
   ls -la ~/.claude/api-logs/
   ```

3. Check application is using proxy:
   ```bash
   # In Claude Desktop, check network settings
   # Or use:
   ss -tunap | grep ESTABLISHED | grep 8888
   ```

4. Check MITMproxy console for errors

### Terminal Viewer Not Showing API Logs

1. Restart the Next.js dev server:
   ```bash
   cd ~/dev/claude-terminal-viewer
   npm run dev -- --port 3001
   ```

2. Check browser console for errors (F12)

3. Manually verify logs exist:
   ```bash
   ls -la ~/.claude/api-logs/
   cat ~/.claude/api-logs/session_*.jsonl | tail -20
   ```

## SSL Pinning Bypass

Claude Desktop may implement SSL certificate pinning, which prevents MITMproxy from intercepting traffic even with a trusted certificate.

### Detection
If you see:
- No API calls logged
- Certificate errors despite certificate installation
- Connection failures when proxy is active

Then SSL pinning is likely active.

### Bypass Techniques

#### Method 1: Frida (Runtime Instrumentation)

1. Install Frida:
   ```bash
   pip install frida-tools
   ```

2. Create SSL pinning bypass script:
   ```bash
   # This would require reverse engineering Claude Desktop
   # Not recommended without authorization
   ```

#### Method 2: Electron Developer Tools

If Claude Desktop is an Electron app:

1. Enable dev tools:
   ```bash
   claude-desktop --remote-debugging-port=9222
   ```

2. Open DevTools at `chrome://inspect` in Chrome

3. Check Network tab for API calls directly

#### Method 3: Patch Binary (Advanced)

This requires reverse engineering and may violate terms of service. Not recommended.

## Architecture Analysis

Once logging is working, you can analyze the API architecture:

1. **View in Terminal Viewer**: See all API calls with timestamps
2. **Inspect Request/Response Format**: Understand Claude API structure
3. **Track Session Flow**: See how conversations are maintained
4. **Analyze Rate Limits**: Monitor API usage patterns
5. **Debug Issues**: See exact error responses

### Example API Call Structure

Requests typically follow this pattern:
```json
{
  "timestamp": "2025-11-24T15:30:00Z",
  "type": "request",
  "method": "POST",
  "url": "https://api.anthropic.com/v1/messages",
  "headers": {
    "anthropic-version": "2023-06-01",
    "content-type": "application/json",
    "x-api-key": "sk-ant-..."
  },
  "body": {
    "model": "claude-opus-4-20250514",
    "max_tokens": 4096,
    "messages": [...]
  }
}
```

## Security Considerations

1. **API Keys**: Logs contain API keys. Protect them:
   ```bash
   chmod 600 ~/.claude/api-logs/*
   ```

2. **Sensitive Data**: Logs may contain conversation content. Store securely.

3. **Development Only**: Don't use this setup for production traffic.

4. **Certificate Trust**: Only trust MITMproxy certificate on development machines.

## Automation

Create a startup script to launch everything:

```bash
#!/usr/bin/env bash
# ~/.local/bin/start-claude-monitoring

# Start terminal viewer in background
cd ~/dev/claude-terminal-viewer
npm run dev -- --port 3001 &
VIEWER_PID=$!

# Wait for viewer to start
sleep 3

# Start MITMproxy
start-claude-proxy &
PROXY_PID=$!

# Print info
echo "Terminal Viewer: http://localhost:3001 (PID: $VIEWER_PID)"
echo "MITMproxy: localhost:8888 (PID: $PROXY_PID)"
echo ""
echo "Press Ctrl+C to stop all services"

# Wait for interrupt
trap "kill $VIEWER_PID $PROXY_PID 2>/dev/null" EXIT
wait
```

## Next Steps

1. Explore the API structure
2. Document endpoints and request formats
3. Build custom tools using the API knowledge
4. Monitor performance and optimize usage

---

For issues or questions, check:
- MITMproxy docs: https://docs.mitmproxy.org/
- Terminal viewer: http://localhost:3001
- Logs: `~/.claude/api-logs/`
