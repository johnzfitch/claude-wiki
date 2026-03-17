# Domain Method Proof Pack (Submission Draft)

## What this proves

1. `GET /api/web/domain_info?domain=...` is reachable unauthenticated and returns `200`.
2. The endpoint returns `{"can_fetch": true}` for:
   - private IP literals (`10.0.0.1`, `172.16.0.1`, `192.168.0.1`)
   - loopback/link-local (`127.0.0.1`, `169.254.169.254`, `::1`)
   - private-resolving public aliases (`localtest.me`, `127.0.0.1.nip.io`, `169.254.169.254.nip.io`)
   - malformed/non-domain inputs (`""`, `.`, `..`, `%00`, `http://127.0.0.1`)
3. This is consistent with an allow-all decision surface, not an effective domain safety gate.

## Reproduction Artifacts

- `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/domain_info_probe.tsv`
- `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/domain_info_adversarial_results.tsv`
- `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/domain_method_proof.tsv`
- `/home/zack/claude-binary/2.1.50/lab/evidence/runs/20260301T101853Z/domain_info_fuzz_results.tsv`

## Key data points

- `169.254.169.254 -> 200 true`
- `metadata.google.internal -> 200 true`
- `127.0.0.1.nip.io -> 200 true` (resolves to loopback)
- `localtest.me -> 200 true` (resolves to `127.0.0.1` and `::1`)
- empty domain input -> `200 true`
- `%00` domain input -> `200 true`

## Why this is security-relevant (concise argument)

Even if the endpoint was originally intended as a policy or categorization service, the extracted Claude Code logic uses its `can_fetch` value as a preflight decision in the WebFetch path (allow/blocked branch behavior documented in local reverse-engineering artifacts). If this decision surface is allow-all for private/loopback/link-local and malformed inputs, it cannot provide meaningful SSRF risk reduction when integrated into request authorization flow.

## Suggested triage comment (ready to paste)

The additional proof requested for the **domain method** is attached as TSV artifacts.  
In this run, `/api/web/domain_info` returned `200` + `can_fetch:true` for:
- private ranges (`10/8`, `172.16/12`, `192.168/16`)
- loopback/link-local (`127.0.0.1`, `169.254.169.254`, `::1`)
- private-resolving aliases (`localtest.me`, `127.0.0.1.nip.io`, `169.254.169.254.nip.io`)
- malformed inputs (empty, `.`, `..`, `%00`, URL-shaped strings)

This demonstrates the method behaves as permissive/allow-all for sensitive destinations and malformed values.  
Given the previously provided call-path evidence that WebFetch branches on `can_fetch`, this means the method does not enforce the expected safety boundary against internal targets.
