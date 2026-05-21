---
category: "02-Claude-Code-CLI"
fetched_at: "2026-05-19T21:22:56Z"
source_url: "https://code.claude.com/docs/en/network-config"
title: "Enterprise network configuration - Claude Code Docs"
---

# Enterprise network configuration


Configure Claude Code for enterprise environments with proxy servers, custom Certificate Authorities (CA), and mutual Transport Layer Security (mTLS) authentication.


> ## Documentation Index
>
> Fetch the complete documentation index at: <https://code.claude.com/docs/llms.txt>
>
> Use this file to discover all available pages before exploring further.

Claude Code supports various enterprise network and security configurations through environment variables. This includes routing traffic through corporate proxy servers, trusting custom Certificate Authorities (CA), and authenticating with mutual Transport Layer Security (mTLS) certificates for enhanced security.

All environment variables shown on this page can also be configured in [`settings.json`](/docs/en/settings).


[​](#proxy-configuration)

Proxy configuration


[​](#environment-variables)

Environment variables

Claude Code respects standard proxy environment variables:

```python
# HTTPS proxy (recommended)
export HTTPS_PROXY=https://proxy.example.com:8080

# HTTP proxy (if HTTPS not available)
export HTTP_PROXY=http://proxy.example.com:8080

# Bypass proxy for specific requests - space-separated format
export NO_PROXY="localhost 192.168.1.1 example.com .example.com"
# Bypass proxy for specific requests - comma-separated format
export NO_PROXY="localhost,192.168.1.1,example.com,.example.com"
# Bypass proxy for all requests
export NO_PROXY="*"
```

Claude Code does not support SOCKS proxies.


[​](#basic-authentication)

Basic authentication

If your proxy requires basic authentication, include credentials in the proxy URL:

```python
export HTTPS_PROXY=http://username:password@proxy.example.com:8080
```

Avoid hardcoding passwords in scripts. Use environment variables or secure credential storage instead.

For proxies requiring advanced authentication (NTLM, Kerberos, etc.), consider using an LLM Gateway service that supports your authentication method.


[​](#ca-certificate-store)

CA certificate store

By default, Claude Code trusts both its bundled Mozilla CA certificates and your operating system’s certificate store. Enterprise TLS-inspection proxies such as CrowdStrike Falcon and Zscaler work without additional configuration when their root certificate is installed in the OS trust store. `CLAUDE_CODE_CERT_STORE` accepts a comma-separated list of sources. Recognized values are `bundled` for the Mozilla CA set shipped with Claude Code and `system` for the operating system trust store. The default is `bundled,system`. To trust only the bundled Mozilla CA set:

```python
export CLAUDE_CODE_CERT_STORE=bundled
```

To trust only the OS certificate store:

```python
export CLAUDE_CODE_CERT_STORE=system
```

`CLAUDE_CODE_CERT_STORE` has no dedicated `settings.json` schema key. Set it via the `env` block in `~/.claude/settings.json` or directly in the process environment.


[​](#custom-ca-certificates)

Custom CA certificates

If your enterprise environment uses a custom CA, configure Claude Code to trust it directly:

```python
export NODE_EXTRA_CA_CERTS=/path/to/ca-cert.pem
```


[​](#mtls-authentication)

mTLS authentication

For enterprise environments requiring client certificate authentication:

```python
# Client certificate for authentication
export CLAUDE_CODE_CLIENT_CERT=/path/to/client-cert.pem

# Client private key
export CLAUDE_CODE_CLIENT_KEY=/path/to/client-key.pem

# Optional: Passphrase for encrypted private key
export CLAUDE_CODE_CLIENT_KEY_PASSPHRASE="your-passphrase"
```


[​](#network-access-requirements)

Network access requirements

Claude Code requires access to the following URLs. Allowlist these in your proxy configuration and firewall rules, especially in containerized or restricted network environments.

| URL                            | Required for                                                                                                                           |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `api.anthropic.com`            | Claude API requests                                                                                                                    |
| `claude.ai`                    | claude.ai account authentication                                                                                                       |
| `platform.claude.com`          | Anthropic Console account authentication                                                                                               |
| `downloads.claude.ai`          | Plugin executable downloads; native installer and native auto-updater                                                                  |
| `storage.googleapis.com`       | Native installer and native auto-updater on versions prior to 2.1.116                                                                  |
| `bridge.claudeusercontent.com` | [Claude in Chrome](/docs/en/chrome) extension WebSocket bridge                                                                         |
| `raw.githubusercontent.com`    | Changelog feed for [`/release-notes`](/docs/en/commands) and the release notes shown after updating; plugin marketplace install counts |

If you install Claude Code through npm or manage your own binary distribution, end users may not need access to `downloads.claude.ai` or `storage.googleapis.com`. Claude Code also sends optional operational telemetry by default, which you can disable with environment variables. See [Telemetry services](/docs/en/data-usage#telemetry-services) for how to disable it before finalizing your allowlist. When using [Amazon Bedrock](/docs/en/amazon-bedrock), [Google Vertex AI](/docs/en/google-vertex-ai), or [Microsoft Foundry](/docs/en/microsoft-foundry), model traffic and authentication go to your provider instead of `api.anthropic.com`, `claude.ai`, or `platform.claude.com`. The WebFetch tool still calls `api.anthropic.com` for its [domain safety check](/docs/en/data-usage#webfetch-domain-safety-check) unless you set `skipWebFetchPreflight: true` in [settings](/docs/en/settings). [Claude Code on the web](/docs/en/claude-code-on-the-web) and [Code Review](/docs/en/code-review) connect to your repositories from Anthropic-managed infrastructure. If your GitHub Enterprise Cloud organization restricts access by IP address, enable [IP allow list inheritance for installed GitHub Apps](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps). The Claude GitHub App registers its IP ranges, so enabling this setting allows access without manual configuration. To [add the ranges to your allow list manually](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#adding-an-allowed-ip-address) instead, or to configure other firewalls, see the [Anthropic API IP addresses](https://platform.claude.com/docs/en/api/ip-addresses). For self-hosted [GitHub Enterprise Server](/docs/en/github-enterprise-server) instances behind a firewall, allowlist the same [Anthropic API IP addresses](https://platform.claude.com/docs/en/api/ip-addresses) so Anthropic infrastructure can reach your GHES host to clone repositories and post review comments.


[​](#additional-resources)

Additional resources

- [Claude Code settings](/docs/en/settings)
- [Environment variables reference](/docs/en/env-vars)
- [Troubleshooting guide](/docs/en/troubleshooting)
