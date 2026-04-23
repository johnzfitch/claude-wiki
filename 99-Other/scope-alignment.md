---
title: "Scope Alignment (from `/home/zack/scope.txt`)"
category: "99-Other"
---

# Scope Alignment (from `/home/zack/scope.txt`)

## Key Constraints Extracted

- Program scope is internet-facing systems owned/operated/controlled by Anthropic (`/home/zack/scope.txt:5-7`).
- Third-party systems are out of scope, even if related to Anthropic domains (`/home/zack/scope.txt:7`).
- Testing must avoid harm, avoid substantial traffic, and avoid data access/exfiltration (`/home/zack/scope.txt:33-37`).
- Reports must include validated working proof-of-concept; theoretical scanner-only results are disfavored (`/home/zack/scope.txt:40`).
- The policy excludes “red-teaming, adversarial testing of our models” (`/home/zack/scope.txt:19`).

## Host Buckets Produced

- Likely in-scope candidates:
  - `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/hosts_likely_in_scope.txt`
- Ownership verification required before testing:
  - `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/hosts_verify_ownership.txt`
- External / likely out-of-scope:
  - `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/hosts_out_of_scope_or_external.txt`

## Immediate Drill Implication

For compliance, active checks should be limited to `hosts_likely_in_scope.txt`, with low-rate, non-destructive validation and no data exfiltration behavior.

## Official Scope Files (2026-03-01 UTC)

- `/home/zack/Downloads/anthropic-vdp-2026-03-01T10_21_55Z.json` defines URL scope include rules for:
  - host `^claude\\.ai$`
  - protocol `http` on port `80`, and `https` on port `443`
  - file/path `^/.*`
- `/home/zack/Downloads/scopes_for_anthropic-vdp_at_2026-03-01_10_22_05_UTC.csv` includes an entry for `claude.ai` as URL asset and additional non-URL asset classes.

### Strict URL Sets Derived From Official Matcher

- From `/home/zack/claude-binary/all_urls_150.txt`:
  - `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/urls_all_strict_scope_claude_ai_normalized.txt` (12 URLs)
- From `/home/zack/claude-binary/2.1.50/evidence/urls_focus.txt` (normalized):
  - `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/urls_focus_strict_scope_claude_ai.txt` (12 URLs)
