---
title: "HackerOne VDP Report: Internal Artifactory Instance Publicly Exposed with Unpatched CVE-2025-14830"
category: "22-Safety-Policy"
---

# HackerOne VDP Report: Internal Artifactory Instance Publicly Exposed with Unpatched CVE-2025-14830

**Program**: Anthropic (VDP)
**Researcher**: [your HackerOne handle]
**Suggested Severity**: High (P2)
**Vulnerability Type**: Exposed Internal Service + Unauthenticated Version Disclosure + Confirmed Unpatched CVE
**Affected Component**: `https://artifactory.infra.ant.dev/` (AWS EC2, 54.174.170.169)

---

## Summary

Anthropic's internal JFrog Artifactory instance — used as the Cargo package registry for Claude Code's native Rust components — is directly reachable from the public internet with no network-level access controls. Three compounding issues are present:

1. **Unauthenticated version disclosure**: HTTP response headers expose the exact Artifactory version (`7.111.9`) on every request, without requiring authentication. The Artifactory UI import map additionally confirms the UI asset version as `7.111.8`.

2. **Confirmed unpatched CVE-2025-14830**: Version `7.111.9` falls within the affected range for CVE-2025-14830 (JFrog Artifactory DOM-based XSS in the Workers component, affects `>= 7.94.0` and `< 7.117.10`). The Workers feature is confirmed installed on this instance. The fix version `7.117.10` has not been applied.

3. **Cluster topology exposed unauthenticated**: Response headers leak the Artifactory node identity (`jfrog-platform-artifactory-3`) and instance fingerprint, confirming this is a multi-node HA deployment with at least 3 nodes.

The hostname was discovered via string extraction from the publicly distributed Claude Code 2.1.50 release binary, where it appears in Rust panic message source paths embedded by the Cargo build toolchain.

---

## Discovery

### How the hostname was found

The string `artifactory.infra.ant.dev` is embedded in the Claude Code 2.1.50 linux-x64 ELF binary as a Rust panic source path. Rust embeds absolute `file!()` paths from the build machine into compiled panic messages; because Cargo downloaded crate sources from an internal Artifactory registry, those paths contain the Artifactory hostname.

```bash
strings claude-2.1.50 | grep artifactory
# /Users/kurt/.cargo/registry/src/artifactory.infra.ant.dev-7db23613d841872b/regex-syntax-0.8.4/src/unicode.rs
# /Users/wolffiex/.cargo/registry/src/artifactory.infra.ant.dev-7db23613d841872b/napi-2.16.17/src/...
# /root/.cargo/registry/src/artifactory.infra.ant.dev-7db23613d841872b/nucleo-0.5.0/src/...
```

The hostname appears across multiple developer build environments (macOS ARM, Linux container), confirming it is the organization's primary Cargo registry.

```bash
dig +short artifactory.infra.ant.dev
# 54.174.170.169  (AWS EC2, us-east-1, confirmed live 2026-02-23)
```

---

## Steps to Reproduce

### Step 1 — Confirm public reachability

```bash
curl -sI https://artifactory.infra.ant.dev/artifactory/api/system/ping
```

Response (observed 2026-02-23):
```
HTTP/1.1 200 OK
X-JFrog-Version: Artifactory/7.111.9 81109900
X-Artifactory-Id: 2dbd3d8347d07007d71ae66724ca9c6a7562f099
X-Artifactory-Node-Id: jfrog-platform-artifactory-3
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

Body: `OK`

The ping endpoint is accessible without authentication. Every response from this host — including 401 and 403 error responses — returns the full `X-JFrog-Version`, `X-Artifactory-Id`, and `X-Artifactory-Node-Id` headers. No authentication is required to read the exact version.

### Step 2 — Confirm exact version via response headers

Any unauthenticated request discloses the version:

```bash
curl -sI https://artifactory.infra.ant.dev/artifactory/api/repositories
# HTTP/1.1 401 Unauthorized
# X-JFrog-Version: Artifactory/7.111.9 81109900
# X-Artifactory-Id: 2dbd3d8347d07007d71ae66724ca9c6a7562f099
# X-Artifactory-Node-Id: jfrog-platform-artifactory-3
```

The UI import map confirms the UI asset version independently:

```bash
curl -s https://artifactory.infra.ant.dev/ui/imports-map/imports.json
# {
#   "imports": {
#     "@jfrog/ui-platform-microfrontend-artifactory": "/ui/api/v1/ui/webapp/js/app.umd.js?v=7.111.8",
#     "@jfrog/ui-platform-microfrontend-worker": "/ui/api/v1/worker/webapp/js/app.umd.js?v=",
#     ...
#   }
# }
```

**Confirmed version**: Artifactory `7.111.9` (server), `7.111.8` (UI assets).

### Step 3 — Map version to CVE-2025-14830

CVE-2025-14830 (published 2026-01-04, JFrog Security Advisory):

| Field | Detail |
|---|---|
| CVE | CVE-2025-14830 |
| Severity | Medium |
| Type | DOM-based XSS (CWE-79) |
| Affected | Artifactory `> 7.94.0` and `< 7.117.10` (Enterprise+/Enterprise X) |
| Fixed in | 7.117.10 |
| Description | Improper handling of the import validation mechanism in the Workers component leads to DOM-based XSS |

Running version `7.111.9` falls within `(7.94.0, 7.117.10)`. **The fix has not been applied.**

### Step 4 — Confirm Workers feature is installed

The CVE requires the Workers feature to be enabled. The following endpoints return HTTP **403** (access denied by auth layer) rather than **404** (not found), confirming the Workers feature is present on disk and registered:

```bash
curl -sI https://artifactory.infra.ant.dev/ui/admin/workers/
# HTTP/1.1 403 Forbidden

curl -sI https://artifactory.infra.ant.dev/ui/api/v1/worker/webapp/js/app.umd.js
# HTTP/1.1 403 Forbidden

curl -sI https://artifactory.infra.ant.dev/ui/api/v1/worker/
# HTTP/1.1 401 Unauthorized   (Artifactory backend: auth required)
```

The import map (Step 2) also includes `@jfrog/ui-platform-microfrontend-worker` as a registered module, consistent with Workers being installed.

**Workers feature confirmed present.** CVE-2025-14830 is applicable.

---

## What Was NOT Done

- No authentication was attempted
- No repositories were browsed or listed (all 401)
- No data was accessed or exfiltrated
- No write operations were performed
- The Workers XSS was not triggered (requires admin credentials; no public PoC exists)
- Scope was limited to HTTP GET requests confirming version, topology, and feature presence

---

## Risk Analysis

### CVE-2025-14830

The vulnerability is a DOM-based XSS in the Workers component's import validation mechanism. Per the JFrog advisory, exploitation requires high-level (admin) privileges and no additional user interaction — consistent with a stored XSS that executes when an admin views the Workers administration page. Impact includes session token theft and actions on behalf of other admin users.

The direct exploitability by an external unauthenticated attacker is low for the XSS itself. However, the combination of factors elevates the overall severity:

- The instance is directly internet-reachable, eliminating VPN/perimeter as a backstop
- An attacker who obtains any admin credential (phishing, credential stuffing, other vulnerability) can immediately exploit CVE-2025-14830 against other admin sessions
- The `unsafe-eval` directive in the CSP (`script-src 'self' 'unsafe-eval'`) means a successful XSS injection can evaluate arbitrary JavaScript without CSP restriction

### Topology disclosure

`X-Artifactory-Node-Id: jfrog-platform-artifactory-3` confirms an HA cluster with at least 3 nodes. `X-Artifactory-Id: 2dbd3d8347d07007d71ae66724ca9c6a7562f099` is the unique fingerprint of this installation. Both are disclosed on every unauthenticated response.

### Unsupported version track

`7.111.x` is not a current supported self-hosted LTS track in JFrog's release schedule. The active self-hosted maintenance tracks are `7.98.x`, `7.104.x`, `7.117.x`, `7.125.x`, and `7.133.x`. Running an off-track version means security patches may not be backported to this line, and the upgrade path to the next supported track (`7.117.x`) also happens to be the CVE-2025-14830 fix.

### Supply chain risk

This Artifactory instance serves as the Cargo registry for Claude Code's native components (confirmed via embedded paths for `napi`, `tokio`, `image`, `nucleo`, and other crates). Compromise of the registry — through the XSS or any future pre-auth CVE — could enable artifact poisoning of Claude Code's native layer.

---

## Impact

**Severity: High (P2)**

The combination of: (1) confirmed exact version via unauthenticated header disclosure, (2) confirmed unpatched CVE-2025-14830 applicable to that version, (3) Workers feature confirmed installed, (4) instance publicly reachable on the internet, and (5) the instance serving as Anthropic's internal Cargo build registry makes this a meaningful finding beyond a simple misconfiguration.

---

## Suggested Remediation

**1. Immediate: Apply CVE-2025-14830 patch**
Upgrade to Artifactory `7.117.10` or later. This is the minimum version that patches CVE-2025-14830. The next supported LTS track (`7.117.x`) is the direct upgrade path.

**2. Immediate workaround (while scheduling upgrade)**
Block `/ui/admin/workers/` at the WAF/proxy layer, or uninstall the Workers feature if not in use. Per the JFrog advisory, this eliminates the XSS attack surface without requiring an immediate version upgrade.

**3. Network-level access control**
Restrict `54.174.170.169:443` to Anthropic's VPN egress and internal network ranges via AWS Security Group rules. There is no legitimate reason for the Cargo package registry to be reachable from arbitrary internet IPs.

**4. Suppress version headers**
The `X-JFrog-Version`, `X-Artifactory-Id`, and `X-Artifactory-Node-Id` response headers should be stripped by the nginx proxy layer for unauthenticated requests. This eliminates the unauthenticated version disclosure that enables precise CVE mapping.

**5. Remove hostname from distributed binaries**
`artifactory.infra.ant.dev` is embedded in the Claude Code release binary via Rust panic source paths. Consider setting `CARGO_BUILD_RUSTFLAGS=--remap-path-prefix` in the CI pipeline to remap local source paths to a fixed non-sensitive prefix in compiled output, preventing internal infrastructure hostnames from appearing in distributed binaries.

---

## Supporting Evidence

| Evidence | Value |
|---|---|
| Hostname discovered in | Claude Code 2.1.50 linux-x64 ELF binary (Rust panic paths) |
| DNS (live 2026-02-23) | `artifactory.infra.ant.dev` → `54.174.170.169` (AWS EC2 us-east-1) |
| Server version (unauthenticated) | `X-JFrog-Version: Artifactory/7.111.9 81109900` |
| UI version (unauthenticated) | `?v=7.111.8` in `/ui/imports-map/imports.json` |
| Node ID (unauthenticated) | `X-Artifactory-Node-Id: jfrog-platform-artifactory-3` |
| Instance fingerprint (unauthenticated) | `X-Artifactory-Id: 2dbd3d8347d07007d71ae66724ca9c6a7562f099` |
| Ping endpoint (unauthenticated) | `GET /artifactory/api/system/ping` → HTTP 200 "OK" |
| Workers UI endpoint | `GET /ui/admin/workers/` → HTTP 403 (present, not 404) |
| Workers JS asset | `GET /ui/api/v1/worker/webapp/js/app.umd.js` → HTTP 403 (present, not 404) |
| CVE reference | [CVE-2025-14830](https://jfrog.com/help/r/jfrog-release-information/cves-impacting-artifactory), published 2026-01-04 |
| Affected range | Artifactory `> 7.94.0` and `< 7.117.10` |
| Fix version | 7.117.10 |

---

*Research was conducted passively via HTTP GET requests only. No authentication was attempted, no data was accessed, no write operations were performed, and the XSS was not triggered. Submitted in accordance with Anthropic's responsible disclosure policy.*
