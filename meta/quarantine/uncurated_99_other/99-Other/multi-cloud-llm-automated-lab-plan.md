# Multi-Cloud LLM-Automated SSRF Lab Plan (AWS + GCP + Azure)

## Objective
Build a fully automated, reproducible lab to validate SSRF impact claims with hard evidence:
- Real metadata/token access behavior per cloud
- Redirect-to-internal target behavior
- RFC1918 lateral reach behavior
- Artifact-grade evidence for disclosure or internal security reporting

## Scope
- In-scope: your own cloud tenants/subscriptions/projects only
- Out-of-scope: third-party or production systems you do not control
- Priority order: AWS, GCP, Azure

## Success Criteria
1. One-command deploy per cloud creates an isolated canary environment.
2. One-command run executes all test scenarios and stores logs/pcaps/artifacts.
3. One-command teardown destroys all resources.
4. Evidence package includes timestamps, source/destination IPs, request paths, and returned data class (token/no token/error).

## Architecture
Per cloud, deploy:
- `attacker_controlled_redirect` endpoint (public HTTPS)
- `canary_internal_service` (private RFC1918 HTTP/HTTPS service with deterministic response)
- `canary_compute_target` VM with managed identity/role/service account
- `evidence_collector` (pcap + structured logs + cloud flow logs)

Global:
- `orchestrator` runner (LLM-driven control loop)
- `artifact_store` (timestamped run folders)

## Repo Layout
```text
lab/
  orchestrator/
    runbook.yaml
    prompts/
      planner.md
      implementer.md
      verifier.md
      reporter.md
    scripts/
      run_pipeline.sh
      collect_artifacts.sh
  infra/
    aws/
      main.tf
      variables.tf
      outputs.tf
    gcp/
      main.tf
      variables.tf
      outputs.tf
    azure/
      main.tf
      variables.tf
      outputs.tf
  tests/
    scenarios/
      01_domain_gate_checks.yaml
      02_direct_metadata_targets.yaml
      03_redirect_to_metadata.yaml
      04_redirect_to_rfc1918.yaml
      05_header_variant_tests.yaml
  evidence/
    runs/
```

## Automation Model (Fully LLM-Driven)
Use four agent roles with strict ownership:
1. Planner agent
- Converts objectives into concrete infra + test tasks.
- Outputs machine-readable task graph (`runbook.yaml`).

2. Implementer agent
- Generates/updates Terraform and scenario files.
- Executes `fmt/validate/plan/apply`.

3. Verifier agent
- Runs scenario suite and checks expected vs actual outcomes.
- Fails run on missing evidence.

4. Reporter agent
- Produces final findings package with reproducibility details and confidence levels.

## Guardrails
- Dedicated throwaway cloud accounts/projects/subscriptions.
- Least-privilege canary identities only.
- Budget alerts and hard caps.
- Resource TTL tags (`auto_destroy_after`).
- Explicit deny egress to non-lab targets where possible.
- No secret reuse from real environments.

## Cloud-Specific Canary Design

### AWS
- EC2 canary with IAM role allowing only:
  - `sts:GetCallerIdentity`
  - optional read-only canary API
- Toggleable IMDS mode:
  - profile A: IMDSv2 required
  - profile B: IMDSv1 allowed (lab-only)
- Private service in VPC (`10.x`) returning `AWS_RFC1918_CANARY_OK`.

### GCP
- GCE canary with minimal service account scope.
- Metadata endpoint tests include required `Metadata-Flavor: Google` variants.
- Private VPC service returning `GCP_RFC1918_CANARY_OK`.

### Azure
- VM canary with managed identity.
- IMDS token path tests with API version permutations.
- Private VNet service returning `AZURE_RFC1918_CANARY_OK`.

## Test Matrix
1. Gate-only checks
- Validate policy gate decisions for:
  - `169.254.169.254`
  - metadata hostnames
  - RFC1918 IPs
  - attacker redirect host

2. Direct metadata fetch
- HTTP/HTTPS permutations
- Header/no-header permutations (especially GCP/Azure metadata requirements)

3. Redirect behavior
- Allowed public domain -> metadata target
- Allowed public domain -> RFC1918 target
- 301/302/307/308 differences

4. Internal lateral checks
- Fetch private service endpoints on `10.x`, `172.16.x`, `192.168.x`

5. Exfil simulation
- Post only canary tokens/strings to controlled collector
- Never use real privileged secrets

## Evidence Requirements Per Scenario
- Request timestamp (UTC)
- Full requested URL and redirect chain
- Worker egress IP
- Response code/body class
- Packet capture snippet or equivalent flow logs
- Cloud-native logs:
  - AWS: VPC Flow Logs + instance logs
  - GCP: VPC Flow Logs + Cloud Logging
  - Azure: NSG flow logs + Monitor logs

## Pipeline Stages
1. `bootstrap`
- Validate cloud auth contexts and quotas.

2. `provision`
- Terraform apply all three clouds in parallel.

3. `verify_infra`
- Health check every endpoint and collector.

4. `execute_tests`
- Run full scenario suite with retries and deterministic ordering.

5. `collect`
- Pull logs, flow records, pcaps, scenario outputs into one run folder.

6. `report`
- Auto-generate:
  - technical findings
  - confidence per finding
  - false-positive/limitation notes

7. `teardown`
- Destroy all resources and verify cleanup.

## Suggested Commands
```bash
# Dry run
./lab/orchestrator/scripts/run_pipeline.sh --stage plan --cloud all

# Full run
./lab/orchestrator/scripts/run_pipeline.sh --stage full --cloud all --auto-approve

# Teardown
./lab/orchestrator/scripts/run_pipeline.sh --stage teardown --cloud all --auto-approve
```

## First Implementation Sprint (Recommended)
1. Implement AWS end-to-end first (fastest path to high-signal evidence).
2. Port same pattern to GCP.
3. Port same pattern to Azure.
4. Add cross-cloud comparison report.

## Deliverables
- `evidence/runs/<timestamp>/` with all artifacts
- `final_report.md` with:
  - confirmed exploitability by cloud/provider path
  - prerequisites/mitigations
  - reproducibility appendix
- `teardown_report.md` confirming cleanup

## Acceptance Gate Before External Submission
- At least one confirmed end-to-end controlled secret retrieval in your own lab per cloud (or explicit documented blocker per cloud).
- Redirect-chain behavior proven with logs and packet/flow evidence.
- No ambiguous “could” claims without matching artifact evidence.
