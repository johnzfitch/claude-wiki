# HackerOne VDP Report: Internal JFrog Artifactory Instance Publicly Exposed on Internet

**Program**: Anthropic (VDP)
**Researcher**: [your HackerOne handle]
**Suggested Severity**: Medium (P3)
**Vulnerability Type**: Information Disclosure / Misconfiguration — Exposed Internal Service
**Affected Component**: `https://artifactory.infra.ant.dev/` (AWS EC2, 54.174.170.169)

---

## Summary

An internal JFrog Artifactory instance used for Anthropic's build/CI infrastructure is directly accessible on the public internet with no network-level access controls. The `/api/system/ping` endpoint responds HTTP 200 without authentication, confirming the service is live and leaking system availability. All other API endpoints correctly require authentication (401), but the public internet exposure of an internal artifact repository host is a significant attack surface given:

1. The hostname was discovered embedded in the Claude Code 2.1.50 release binary.
2. The service is running on a raw AWS EC2 IP (54.174.170.169) behind nginx, directly reachable globally.
3. JFrog Artifactory has a well-documented CVE history; public exposure without network controls means any future (or existing) unauthenticated Artifactory CVE is directly exploitable.

---

## Discovery

The hostname `artifactory.infra.ant.dev` was identified via strings extraction from the production Claude Code 2.1.50 ELF binary (linux-x64). It is embedded in the binary section, not in the JS bundle, suggesting it's referenced by the Bun runtime or build toolchain.

```bash
strings /path/to/claude | grep artifactory
# artifactory.infra.ant.dev
```

DNS resolution:
```
artifactory.infra.ant.dev → 54.174.170.169 (AWS EC2, us-east-1)
```

---

## Steps to Reproduce

### 1. Confirm public reachability and TLS details

```bash
curl -Iv "https://artifactory.infra.ant.dev/" --max-time 10
```

Observed response (2026-02-22):
```
HTTP/1.1 200 OK
Server: nginx/1.27.5
Content-Type: text/html; charset=UTF-8
Content-Length: 3499
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

TLS: TLSv1.2, ECDHE-RSA-AES128-GCM-SHA256, certificate `CN=*.infra.ant.dev`, issued by Amazon RSA 2048 M02, valid Aug 11 2025 – Sep 9 2026.

The service serves the JFrog Artifactory web UI HTML at `/`, confirming it is a live, functional Artifactory instance.

### 2. Confirm unauthenticated ping endpoint

```bash
curl -s "https://artifactory.infra.ant.dev/artifactory/api/system/ping"
```

Response:
```
OK
HTTP 200
```

No authentication required. This is the standard Artifactory health-check endpoint and returns 200 when the system is operational.

### 3. Confirm all other endpoints require authentication

```bash
# Repository list
curl -s "https://artifactory.infra.ant.dev/artifactory/api/repositories"
# {"errors":[{"status":401,"message":"Authentication is required"}]}

# Storage summary
curl -s "https://artifactory.infra.ant.dev/artifactory/api/storage"
# {"errors":[{"status":401,"message":"Authentication is required"}]}

# Version (would reveal exact Artifactory version)
curl -s "https://artifactory.infra.ant.dev/artifactory/api/system/version"
# {"errors":[{"status":401,"message":"Authentication is required"}]}

# User info
curl -s "https://artifactory.infra.ant.dev/artifactory/ui/api/v1/ui/user"
# {"errors":[{"status":401,"message":"Authentication is required"}]}
```

No anonymous repository access was observed or attempted beyond confirming 401 responses.

---

## Risk Analysis

### Immediate risks

**System liveness oracle**: The unauthenticated `/api/system/ping` allows any external party to confirm the service is up, schedule attacks around known maintenance windows, or monitor uptime.

**CVE exposure surface**: JFrog Artifactory has a documented CVE history. Public internet exposure without network controls means any unauthenticated RCE or pre-auth vulnerability in the running version is directly exploitable. Notable historical examples include:
- CVE-2020-7931 (Server-Side Template Injection, pre-auth RCE in older versions)
- CVE-2022-0219 (various auth bypass findings in Artifactory Pro)
- Multiple XXE and SSRF vulnerabilities disclosed to JFrog over the years

The version is not readable without authentication (401 on `/api/system/version`), preventing precise CVE matching without auth, but the public exposure itself is the primary concern.

**Internal artifact access**: If credentials are leaked or obtained through other means (phishing, insider threat), Artifactory would be directly accessible to an external attacker without needing VPN access — eliminating a layer of defense-in-depth.

**Supply chain visibility**: Knowing Anthropic uses JFrog Artifactory for its build pipeline is itself useful to a targeted attacker doing reconnaissance prior to a supply chain attack.

### What was NOT confirmed

- No repositories were browsed or listed (all 401)
- No credentials were tested
- No data was accessed
- No version information was obtained (all version endpoints 401)

---

## Impact

**Severity**: Medium. The combination of (1) known internal CI/CD hostname now discoverable by anyone with access to Claude Code binaries, (2) publicly routable with no network-level access control, and (3) the unauthenticated system ping leaking liveness, constitutes a meaningful misconfiguration. The primary risk is that any future unpatched Artifactory CVE is immediately and trivially exploitable from the internet against a system handling Anthropic's build artifacts.

---

## Suggested Remediation

1. **Network-level access control (primary fix)**: Restrict `artifactory.infra.ant.dev` to Anthropic's internal network ranges and VPN egress IPs using AWS Security Groups or a WAF rule. The service should not be reachable from arbitrary internet IPs.

2. **Unauthenticated ping endpoint**: Consider requiring authentication even on `/api/system/ping`, or serve it only on a private health-check interface. JFrog allows disabling anonymous access site-wide in the Artifactory Admin panel.

3. **Remove hostname from public binaries**: `artifactory.infra.ant.dev` being embedded in the production Claude Code release binary exposes internal infrastructure hostnames to anyone who downloads the tool. This string was found in the ELF binary section (not the JS bundle), suggesting it may be embedded by the Bun runtime or build pipeline configuration. Review whether this reference needs to be in the production binary.

---

## Supporting Evidence

- DNS: `dig +short artifactory.infra.ant.dev` → `54.174.170.169` (live as of 2026-02-22)
- HTTPS 200 OK from root path, confirmed JFrog Artifactory UI HTML in response body
- `/artifactory/api/system/ping` returns HTTP 200 "OK" without credentials
- Source: string found in Claude Code 2.1.50 linux-x64 ELF binary, confirmed via `strings` extraction

---

*Submitted in accordance with Anthropic's responsible disclosure policy. Research was purely passive (HTTP GET requests only). No authentication was attempted; no data was accessed or exfiltrated.*
