---
title: "Redteam Drill Report"
category: "22-Safety-Policy"
tags: ["rag", "security"]
---

# Redteam Drill Report

- Run ID: `20260301T101853Z`
- Date (UTC): `2026-03-01T10:18:53Z`
- Scope source: `/home/zack/claude-binary/all_urls_150.txt`
- Drill mode: passive analysis + low-rate live endpoint gating checks (no exploit payloads, no data exfiltration)

## What Was Run

1. Lab orchestrator:
   - `./run_pipeline.sh full all`
   - Output confirms pipeline execution, but every stage is a placeholder implementation (`run_pipeline.sh:51-79`).
2. Artifact collection:
   - `./collect_artifacts.sh /home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z`
   - Output written to `collection_meta.txt`.
3. Endpoint risk extraction:
   - Host frequency -> `domain_frequency.txt`
   - High-risk line extraction -> `high_risk_endpoints_lines.txt`

## Evidence Highlights

- Metadata target appears in extracted endpoint corpus:
  - `/home/zack/claude-binary/all_urls_150.txt:8`
- Domain gate endpoint appears and is parameterized:
  - `/home/zack/claude-binary/all_urls_150.txt:38`
  - `/home/zack/claude-binary/all_urls_150.txt:39`
- OAuth/token/callback endpoints are broadly present:
  - `/home/zack/claude-binary/all_urls_150.txt:36-37`
  - `/home/zack/claude-binary/all_urls_150.txt:105`
  - `/home/zack/claude-binary/all_urls_150.txt:248-253`
- MCP and telemetry surfaces are present:
  - `/home/zack/claude-binary/all_urls_150.txt:43`
  - `/home/zack/claude-binary/all_urls_150.txt:212-213`
  - `/home/zack/claude-binary/all_urls_150.txt:41`
  - `/home/zack/claude-binary/all_urls_150.txt:47`
  - `/home/zack/claude-binary/all_urls_150.txt:182`
- Staging/fedstart endpoints exist in corpus:
  - `/home/zack/claude-binary/all_urls_150.txt:42`
  - `/home/zack/claude-binary/all_urls_150.txt:46`
  - `/home/zack/claude-binary/all_urls_150.txt:62`
  - `/home/zack/claude-binary/all_urls_150.txt:70-71`

## Scenario Coverage Found In Repo

The lab already defines targeted SSRF scenarios:

- Domain gate checks:
  - `/home/zack/claude-binary/2.1.50/lab/tests/scenarios/01_domain_gate_checks.yaml:1-10`
- Direct metadata fetch attempts:
  - `/home/zack/claude-binary/2.1.50/lab/tests/scenarios/02_direct_metadata_targets.yaml:1-8`
- Redirect-to-metadata and redirect-to-RFC1918 paths:
  - `/home/zack/claude-binary/2.1.50/lab/tests/scenarios/03_redirect_to_metadata.yaml:1-7`
  - `/home/zack/claude-binary/2.1.50/lab/tests/scenarios/04_redirect_to_rfc1918.yaml:1-8`
- Header variant tests for metadata services:
  - `/home/zack/claude-binary/2.1.50/lab/tests/scenarios/05_header_variant_tests.yaml:1-46`

## Findings

1. High: The endpoint corpus and scenario suite still center on metadata/SSRF risk primitives (link-local targets + domain gate + redirect paths). The exposure pattern is present and testable locally from artifacts.
2. High: OAuth callback/token endpoints and staged environments materially expand identity attack surface and should be prioritized for strict redirect URI and token audience validation.
3. Medium: MCP and telemetry endpoints create additional exfiltration and trust-boundary paths that require explicit egress policy and payload redaction controls.
4. Medium: Current orchestrator does not execute real tests (`placeholder` stages), so the lab cannot yet produce pass/fail evidence for exploitability in this run.

## Prior Redteam Evidence In Repo (Corroboration)

The existing report documents live `domain_info` approvals for metadata/private targets:

- `/home/zack/claude-binary/2.1.50/hackerone_report_1_ssrf_domain_info.md:13`
- `/home/zack/claude-binary/2.1.50/hackerone_report_1_ssrf_domain_info.md:29-42`
- `/home/zack/claude-binary/2.1.50/hackerone_report_1_ssrf_domain_info.md:65-75`
- `/home/zack/claude-binary/2.1.50/hackerone_report_1_ssrf_domain_info.md:232-239`

## Drill Outcome

- Completed: passive endpoint threat drill, artifact generation, and evidence-backed triage.
- Not completed in this run: active exploit validation against live remote endpoints (out of scope for non-intrusive run).

## Scope Update Applied (VDP Export 2026-03-01)

- `/home/zack/Downloads/scopes_for_anthropic-vdp_at_2026-03-01_10_22_05_UTC.csv:4` shows `Infrastructure & Internal Apps/Services` as submission-eligible.
- `/home/zack/Downloads/scopes_for_anthropic-vdp_at_2026-03-01_10_22_05_UTC.csv:19-28` defines Claude Code behavioral scope:
  - In scope: permission prompt bypasses, out-of-working-directory write bypasses, prompt/tool parameter misrepresentation, invisible execution.
  - Out of scope: intended CLI abuse, alias/symlink env tricks, local credential/config/log storage.
- `/home/zack/Downloads/scopes_for_anthropic-vdp_at_2026-03-01_10_22_05_UTC.csv:16-18` excludes reporting OSS MCP repo issues to Anthropic unless the issue affects Anthropic implementations.

## Phase 2 Live Checks (Low-Rate)

### A. Behavioral shortlist probe

File: `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/curl_behavioral_shortlist.tsv`

Notable results:
- `api.anthropic.com` Claude Code/OAuth endpoints returned `401` or `405` (auth/method-gated).
- `api/web/domain_info?domain=` returned `200`.
- `claude.ai` user-facing paths returned `403` (access controlled from this vantage).
- `platform.claude.com/v1/oauth/token` returned `405` on GET.

### B. `domain_info` gate validation

File: `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/domain_info_probe.tsv`

Observed:
- `169.254.169.254` -> `200`, `can_fetch=true`
- `metadata.google.internal` -> `200`, `can_fetch=true`
- `127.0.0.1` -> `200`, `can_fetch=true`
- `10.0.0.1` -> `200`, `can_fetch=true`
- `172.16.0.1` -> `200`, `can_fetch=true`
- `192.168.0.1` -> `200`, `can_fetch=true`
- `localhost` -> `200`, `can_fetch=true`

### C. Method/auth matrix

File: `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/api_method_matrix.tsv`

Observed:
- `POST` to protected Claude Code endpoints mostly returns `401`.
- `GET` on action endpoints mostly returns `405`.
- `platform.claude.com/v1/oauth/token` returns `415` on POST without expected content type/body.
- `domain_info` remains unauthenticated (`GET 200`).

## Updated Findings

1. High: `domain_info` currently approves private/link-local/localhost targets in live checks (`can_fetch=true`), preserving the core SSRF gate concern.
2. Medium: Other tested control-plane endpoints appear to enforce authentication and method gating (`401/405/415`), reducing trivial unauthenticated abuse.
3. Medium: Claude Code behavioral-risk surfaces remain visible in extracted internals:
   - permission modes include `bypassPermissions` (`/home/zack/claude-binary/2.1.59/modules/SUMMARY.md:47,55`)
   - hooks can affect permission outcomes and persisted permission updates (`/home/zack/claude-binary/2.1.59/modules/hooks/report.md:1013-1017`)
   - internal invisible tool behavior is documented (`/home/zack/claude-binary/2.1.59/modules/tools/report.md:536`)

## Phase 3 Domain-Method Proof Expansion

- Adversarial input set confirms `can_fetch=true` across encoded/private/malformed variants:
  - `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/domain_info_adversarial_results.tsv`
  - `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/domain_info_fuzz_results.tsv`
- DNS-backed aliases resolving to private addresses also return `can_fetch=true`:
  - `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/domain_method_proof.tsv`
- Submission-ready rebuttal note:
  - `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/domain_method_proof_note.md`

## Security Tooling Upgrade (Template Quality)

- Generic broad `nuclei` templates were noisy/slow on protected Cloudflare fronts for this scope.
- Replaced with purpose-built templates specific to the domain gate claim:
  - `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/templates/anthropic-domain-info-private-allow.yaml`
  - `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/templates/anthropic-domain-info-malformed-allow.yaml`
- Custom scan findings:
  - `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/nuclei_custom_domain_info_findings.jsonl` (6 matches)
- Supporting infrastructure scan:
  - `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/nmap_behavioral_hosts.txt`
