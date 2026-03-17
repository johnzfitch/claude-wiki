# Scope & Legal Compliance Review — HackerOne VDP Submission

**Prepared for**: Pre-submission review of all files attached to Anthropic VDP disclosures
**Reports covered**: VDP #1 (SSRF via domain_info) and VDP #2 (Artifactory exposure)
**Standard applied**: Anthropic HackerOne VDP program rules; CFAA (18 U.S.C. §1030); DMCA §1201 security research exemption (17 U.S.C. §1201(j)); common responsible disclosure norms

---

## Files Under Review

| File | Submitted | Purpose |
|---|---|---|
| `hackerone_report_1_ssrf_domain_info.md` | ✅ Yes | Primary VDP #1 disclosure |
| `hackerone_report_2_artifactory_public_exposure.md` | ✅ Yes | VDP #2 disclosure |
| `ssrf_poc.mjs` | ✅ Yes | PoC: gate approval + local listener fetch |
| `demo_scenario2_cicd_default.mjs` | ✅ Yes | CI/CD scenario demonstration |
| `demo_scenario3_codespaces.mjs` | ✅ Yes | Codespaces scenario demonstration |
| `claude_diff_2142_vs_2150.md` / `.json` | ✅ Yes | Version diff supporting evidence |
| `demo_scenario1_supply_chain.mjs` | ❌ Not submitted | Scenario removed from disclosure |

---

## Analysis by Activity

### 1. Binary strings extraction and JS bundle analysis (Claude Code 2.1.50 ELF)

**Activity**: `strings /path/to/claude` and JS parsing to extract function definitions (`C39`, `w39`, `AmD`) from the Bun single-file executable bundle. Used in VDP #1 and the diff files.

**Assessment: Within scope.**

- The Claude Code binary is publicly distributed software. Analysis of legitimately obtained software for security research purposes is standard industry practice and does not constitute unauthorized access under the CFAA.
- DMCA §1201(j) provides an explicit security research exemption: circumvention is permitted when done in good faith for the purpose of identifying and analyzing security flaws in computer software or technology. Extracting readable strings and minified JS from a binary you possess falls within this exemption.
- Anthropic's VDP program, consistent with industry-standard bug bounty programs, implicitly permits security analysis of Anthropic's own distributed software. No login bypass, credential theft, or access to private data was involved.
- The diff files (`claude_diff_2142_vs_2150.*`) compare two public Claude Code release versions and are appropriate supporting evidence.

**Risk flag**: None. This is the standard method for discovering client-side security logic in distributed software.

---

### 2. API calls to `api.anthropic.com/api/web/domain_info`

**Activity**: Unauthenticated GET requests to `https://api.anthropic.com/api/web/domain_info?domain=<value>` with various domain and IP values. Documented in VDP #1 Steps to Reproduce (Part 1) and called live by `ssrf_poc.mjs`, `demo_scenario2_cicd_default.mjs`, and `demo_scenario3_codespaces.mjs`.

**Assessment: Within scope.**

- The endpoint is publicly accessible without authentication. No credentials were obtained or bypassed.
- All requests are read-only GET calls. No state was modified on Anthropic's servers.
- The calls confirm the security behavior of a production API. This is the core of the reported vulnerability — confirming that a public security gate returns permissive responses for private IP ranges is precisely the finding, and confirming it against the live API is the appropriate verification method.
- No rate limiting was circumvented; requests were made at normal human-initiated frequency.
- Analogous to probing a public password-reset flow to confirm whether it discloses account existence: the test is against publicly reachable functionality with no authentication bypass.

**Risk flag**: None. These are GET requests to a public endpoint confirming documented behavior.

---

### 3. Server-side WebFetch test from Claude.ai Cowork session

**Activity**: During an authorized Claude.ai Cowork session, a WebFetch request was directed at `http://169.254.169.254/...` (AWS IMDS), `http://metadata.google.internal/...`, and `http://127.0.0.1/`. The IMDS request produced a 60-second timeout; the others produced ECONNREFUSED. Documented in VDP #1, "Broader Scope" section.

**Assessment: Within scope, with one note.**

- The researcher had authorized access to the Claude.ai service as an end user. Directing WebFetch at target URLs — which is a documented feature of the service — is normal use of an accessible capability.
- The 60-second timeout result means the TCP SYN was dispatched by Anthropic's backend. No data was received; the response was empty (timeout). The metadata service did not return any credentials or content.
- Testing the security behavior of a service to which you have authorized access, in ways that do not exfiltrate data or modify system state, is within normal VDP scope. Bug bounty programs routinely expect and permit exactly this kind of boundary testing.
- The analysis correctly frames the finding as demonstrating that the application-level gate was the only control that should have stopped the request, and it did not — the actual prevention was performed by network-level controls (AWS security groups or IMDSv2 enforcement), not by the application.

**Note**: The test caused Anthropic's servers to make an outbound TCP connection to an IMDS address. This is the vulnerability being demonstrated. Documenting it in the report is appropriate. No data was obtained, no system state was changed, and the test was conducted on infrastructure the researcher was authorized to use. This falls within responsible disclosure norms and standard VDP scope.

**Risk flag**: Low. The action is consistent with authorized use of the service for security research purposes. No data was accessed.

---

### 4. Artifactory reconnaissance (`artifactory.infra.ant.dev`)

**Activity**: DNS resolution of `artifactory.infra.ant.dev` (hostname discovered from strings extraction of the public binary). HTTPS GET requests to the root path (`/`), the health check endpoint (`/artifactory/api/system/ping`), and several authenticated API endpoints (`/artifactory/api/repositories`, `/api/system/version`, etc.). All non-ping endpoints returned HTTP 401. Documented in VDP #2.

**Assessment: Within scope.**

- The hostname was discovered through legitimate analysis of a public binary. No private data, internal documentation, or non-public information was used to find it.
- The service is publicly accessible from the internet (no firewall, no VPN required). Making GET requests to a publicly routable HTTPS endpoint is not unauthorized access under the CFAA. The CFAA's "without authorization" element is not met when a service is exposed to the general public internet and no authentication or access control was circumvented.
- The `/api/system/ping` endpoint returned HTTP 200 without credentials. This is the standard JFrog Artifactory health-check endpoint designed to be accessible for monitoring; returning a response here is the default behavior of Artifactory for unauthenticated requests. No information beyond service liveness was obtained from this endpoint.
- All other tested endpoints returned HTTP 401 (Authentication Required). No credentials were guessed, brute-forced, or obtained. No data was accessed. No repository contents were viewed.
- The report explicitly documents what was NOT confirmed: no repositories browsed, no credentials tested, no data accessed, no version information obtained (401 on `/api/system/version`).
- Passive security reconnaissance (confirming that a public service is publicly accessible and returns expected status codes) is squarely within VDP scope for a program that covers Anthropic's infrastructure.

**Risk flag**: None. All activity was passive GET requests to a publicly routable service, with no authentication bypass and no data access.

---

### 5. PoC and demo scripts

**Activity**: `ssrf_poc.mjs`, `demo_scenario2_cicd_default.mjs`, and `demo_scenario3_codespaces.mjs` call the live `domain_info` API and make fetch requests to a local listener at `127.0.0.1:19876` or `127.0.0.1:19999`. No requests are made to cloud IMDS endpoints.

**Assessment: Within scope.**

- All fetch targets in the PoC scripts are the researcher's own local listener. No third-party infrastructure is contacted beyond the Anthropic-operated `domain_info` API.
- The scripts simulate what would happen on a cloud VM (local listener substitutes for IMDS) without actually contacting any cloud metadata service. This is the appropriate way to demonstrate the vulnerability without exceeding scope.
- The demo scripts call `domain_info` to confirm gate approval — which is the vulnerability (see "What the PoC Proves" in VDP #1). The local listener fetch is a mechanical consequence demonstration against infrastructure the researcher controls.
- None of the scripts are designed to exfiltrate data, maintain persistence, or attack systems. They are demonstration tools for a point-in-time gate-behavior test.

**Risk flag**: None. Scripts operate exclusively against researcher-controlled local endpoints and Anthropic's public API.

---

### 6. File NOT submitted: `demo_scenario1_supply_chain.mjs`

**Activity**: This script demonstrated the `skipWebFetchPreflight: true` settings bypass scenario (Scenario 1, now removed from the disclosure).

**Assessment**: The script itself is within scope — it calls `domain_info` and uses a local listener. It was removed from the submission because the scenario's assumptions about settings-override behavior were not sufficiently verified for confident inclusion, not because of any legal or scope concern.

**Recommendation**: Do not submit this file. It is not referenced in either report as currently revised. Submitting unreferenced files may create confusion during triage.

---

## Summary Assessment

| Activity | CFAA Risk | VDP Scope | Data Accessed | Recommendation |
|---|---|---|---|---|
| Binary strings/JS extraction | None | In-scope | No | ✅ Submit |
| domain_info API calls (GET) | None | In-scope | No | ✅ Submit |
| Server-side WebFetch test (timeout) | Low | In-scope | No | ✅ Submit with disclosure note |
| Artifactory GET requests | None | In-scope | No | ✅ Submit |
| PoC/demo scripts (local listener) | None | In-scope | No | ✅ Submit |
| Scenario 1 demo script | None | In-scope | No | ❌ Do not submit (not referenced) |

**Overall**: All submitted materials are within scope. No unauthorized access occurred. No data was exfiltrated. No credentials were obtained or tested. All test targets were either Anthropic-operated public endpoints, publicly routable infrastructure, or researcher-controlled local addresses. Both reports include responsible disclosure statements accurately describing the scope of testing. The submissions are appropriate for HackerOne VDP submission as revised.

---

## Pre-Submission Checklist

- [ ] Replace `[HackerOne handle]` placeholder in both reports with actual handle
- [ ] Confirm `demo_scenario1_supply_chain.mjs` is NOT attached to the VDP #1 submission
- [ ] Verify `claude_diff_2142_vs_2150.md` / `.json` does not contain any information obtained outside the scope analysis above (e.g., no private API responses, no authenticated data)
- [ ] Confirm all timestamps in the reports reflect actual test dates (currently 2026-02-22)
- [ ] Review HackerOne program page for any program-specific rules that post-date this review

---

*This review reflects the scope of activities as documented in the submitted materials. It does not constitute legal advice. If Anthropic's VDP program terms contain specific restrictions not addressed here, those terms govern.*
