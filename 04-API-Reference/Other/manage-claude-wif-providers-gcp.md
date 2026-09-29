---
title: "Use WIF with Google Cloud - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/wif-providers/gcp"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:37Z"
tags: ["api"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fwif-providers%2Fgcp)





SearchCtrlK

Organization

[Admin API](manage-claude-admin-api.md)[User management](manage-claude-user-management.md)[Workspaces](manage-claude-workspaces.md)

Authentication

[Overview](manage-claude-authentication.md)[Create an Admin API key](manage-claude-admin-api-keys.md)[App Attest](manage-claude-app-attest.md)[Workload Identity Federation](manage-claude-workload-identity-federation.md)[Manage WIF via API](manage-claude-wif-admin-api.md)[WIF reference](manage-claude-wif-reference.md)

Identity providers

[AWS](manage-claude-wif-providers-aws.md)[Google Cloud](manage-claude-wif-providers-gcp.md)[Microsoft Entra ID](manage-claude-wif-providers-azure.md)[GitHub Actions](manage-claude-wif-providers-github-actions.md)[Kubernetes](manage-claude-wif-providers-kubernetes.md)[SPIFFE](manage-claude-wif-providers-spiffe.md)[Okta](manage-claude-wif-providers-okta.md)

Monitoring

[Usage and Cost API](manage-claude-usage-cost-api.md)[Rate Limits API](manage-claude-rate-limits-api.md)[Analytics APIs](manage-claude-analytics-api.md)[Claude Code Analytics API](manage-claude-claude-code-analytics-api.md)[Spend Limits API](manage-claude-spend-limits-api.md)

Data & compliance

[Data residency](../Guides/build-with-claude-data-residency.md)[API and data retention](manage-claude-api-and-data-retention.md)[Access Transparency](manage-claude-access-transparency.md)

[Encryption keys](manage-claude-cmek.md)

[Inference hooks](manage-claude-inference-hooks.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](usage-limits.md)

[Admin](manage-claude-admin-api.md)Identity providers

# Use WIF with Google Cloud

Copy page



Federate Google Cloud workloads (Cloud Run, Cloud Functions, App Engine, GCE, GKE) to the Claude API using Google-signed identity tokens instead of static API keys.

Copy page



Any Google Cloud compute environment with access to the instance metadata server (Cloud Run, Cloud Functions, App Engine, Compute Engine (GCE), and GKE with Workload Identity) can request a Google-signed identity token for its attached service account. The token's issuer is `https://accounts.google.com`, and Anthropic can validate it directly through standard OIDC discovery, with no extra Google Cloud configuration required.

This guide shows how to register the Google issuer with Anthropic, bind a Google service account to an Anthropic service account, and have your workload exchange its identity token for a short-lived Claude API access token.

## Prerequisites

- Familiarity with [WIF concepts](manage-claude-workload-identity-federation.md#concepts): service accounts, federation issuers, and federation rules.
- A Google Cloud project with a workload running on Cloud Run, Cloud Functions, App Engine, Compute Engine, or GKE.
- A user-managed Google service account attached to that workload (not the Compute Engine default service account).
- Permission to create service accounts, federation issuers, and federation rules in the Claude Console for your Anthropic organization.

## Configure Google Cloud

Google issues identity tokens automatically to any workload with an attached service account. There is nothing to enable on the Google side beyond attaching the right service account, but the steps differ slightly between standard compute and GKE.

Cloud Run, Cloud Functions, App Engine, GCE

GKE with Workload Identity

Attach a dedicated service account to your service or instance:

CLI



```python
gcloud run deploy my-service \
  --service-account inference-worker@my-project.iam.gserviceaccount.com
```

Inside the workload, the metadata server returns a signed identity token on demand. Request it with the `audience` you intend to register on the Anthropic side, and include `format=full` so the response carries the `email` claim:

``` block
GET http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity?audience=https://api.anthropic.com&format=full
Metadata-Flavor: Google
```



Or, with the gcloud CLI:

CLI



```python
gcloud auth print-identity-token \
  --audiences="https://api.anthropic.com" \
  --include-email
```

The SDK equivalents are shown in [Acquire and use the token](#acquire-and-use-the-token).

The decoded token payload looks like this:

```python
{
  "iss": "https://accounts.google.com",
  "aud": "https://api.anthropic.com",
  "sub": "104892...",
  "azp": "104892...",
  "email": "inference-worker@my-project.iam.gserviceaccount.com",
  "email_verified": true,
  "exp": 1775527120
}
```



The `sub` claim is the Google service account's opaque numeric unique ID. The `email` claim is the human-readable service account address. Match on both `sub` and `email` in your federation rule.

## Configure Anthropic

In the Claude Console, open **Settings → Workload identity**, click **Connect workload**, and select the **Google Cloud** tile. The wizard walks you through registering the issuer, creating a service account, and creating a federation rule.

The wizard creates these resources for you. Use the following values whether you enter them in the wizard or send them to the [Admin API](manage-claude-wif-admin-api.md):

**Federation issuer:** Google publishes its OIDC discovery document publicly, so use discovery mode. This single issuer covers every Google Cloud surface (Cloud Run, GCE, Cloud Functions, App Engine, and GKE with Workload Identity). Differentiate workloads with rules, not issuers.

```python
{
  "name": "gcp",
  "issuer_url": "https://accounts.google.com",
  "jwks": { "type": "discovery" }
}
```



**Federation rule:** Match on both the `sub` and `email` claims. `email` is the readable service-account address; `sub` is the service account's numeric unique ID, which Google never reuses, so pinning it protects the rule if the service account is deleted and a new one is later created with the same email. Find the unique ID with `gcloud iam service-accounts describe SA_EMAIL --format='value(uniqueId)'`.

```python
{
  "name": "gcp-inference-worker",
  "issuer_id": "fdis_...",
  "match": {
    "audience": "https://api.anthropic.com",
    "claims": {
      "sub": "104892101234567890123",
      "email": "inference-worker@my-project.iam.gserviceaccount.com"
    }
  },
  "target": {
    "type": "service_account",
    "service_account_id": "svac_..."
  },
  "workspace_id": "wrkspc_...",
  "oauth_scope": "workspace:developer",
  "token_lifetime_seconds": 600
}
```



## Acquire and use the token

Inside your Google Cloud workload, fetch the identity token from the metadata server, exchange it at `POST /v1/oauth/token`, and use the returned bearer token to call the Claude API. Each Anthropic SDK handles the exchange and refresh loop for you when you pass a callable that returns a fresh identity token from the metadata server to `identity_token_provider`, as shown in the following examples.

cURL

Python

TypeScript

Go

Java

C#

CLI

PHP

Ruby



```python
import os
import anthropic
import google.auth.transport.requests
import google.oauth2.id_token
from anthropic import WorkloadIdentityCredentials

AUDIENCE = "https://api.anthropic.com"


def fetch_google_identity_token() -> str:
    request = google.auth.transport.requests.Request()
    return google.oauth2.id_token.fetch_id_token(request, AUDIENCE)


client = anthropic.Anthropic(
    credentials=WorkloadIdentityCredentials(
        identity_token_provider=fetch_google_identity_token,
        federation_rule_id=os.environ["ANTHROPIC_FEDERATION_RULE_ID"],
        organization_id=os.environ["ANTHROPIC_ORGANIZATION_ID"],
        service_account_id=os.environ["ANTHROPIC_SERVICE_ACCOUNT_ID"],
        workspace_id=os.environ.get("ANTHROPIC_WORKSPACE_ID"),
    ),
)

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello from Cloud Run"}],
)
print(next(block.text for block in message.content if block.type == "text"))
```

Google identity tokens expire after roughly one hour. The SDKs re-invoke the token provider and re-exchange automatically before expiry. For shell scripts that run longer than the access token's `expires_in`, refresh on a timer and repeat the exchange.

## Verify the setup

From inside your workload, decode the identity token and confirm the claims match your rule:

cURL



```python
curl -sS -H "Metadata-Flavor: Google" \
  "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity?audience=https://api.anthropic.com&format=full" \
  | jq -rR 'split(".")[1] | gsub("-";"+") | gsub("_";"/") | @base64d | fromjson'
```

Check that `iss` is `https://accounts.google.com`, `aud` is `https://api.anthropic.com`, and `email` matches the value in your federation rule. Then run the exchange from the previous section. A successful exchange returns an `access_token` beginning with `sk-ant-oat01-` and an `expires_in` value in seconds. If the exchange fails with the opaque `401` `authentication_error` response (message `Authentication failed`), check the [authentication history page](https://platform.claude.com/settings/workload-identity-federation?tab=history) for the deny reason and see [Troubleshoot a failed exchange](manage-claude-wif-reference.md#troubleshoot-a-failed-exchange); the most common Google Cloud-side cause is the `email` claim missing (request the token with `format=full` so it is included).

## Scope your rule



The Google `sub` claim is the service account's opaque numeric unique ID and has no stable prefix. A `subject_prefix` with a trailing `*` matches arbitrary service accounts across every Google Cloud project, and any of them could obtain a federated Anthropic token.

Lock the rule's `match` block to the narrowest scope that fits your use case:

- **Match `sub` exactly:** Set the full numeric unique ID in `claims.sub` and never use `subject_prefix` for Google tokens.
- **Pin the `email` claim:** Add `claims.email` alongside `sub` so both the stable ID and the readable address must match.
- **Pin the audience:** Set `audience` to the exact value you request from the metadata server so tokens minted for other consumers are rejected.
- **Pin the project on GKE:** For `format=full` tokens, add a `condition` such as `claims.google.compute_engine.project_id == "my-project"` to restrict the rule to one project's nodes.

## Next steps

- Read the [Workload Identity Federation](manage-claude-workload-identity-federation.md) page for the full resource model and SDK credential precedence.
- Add a separate federation rule per environment (production, staging) so you can revoke one without affecting the others.
