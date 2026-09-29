---
title: "Use WIF with Microsoft Entra ID - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/wif-providers/azure"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:36Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fwif-providers%2Fazure)





SearchCtrlK

Organization

[Admin API](/docs/en/manage-claude/admin-api)[User management](/docs/en/manage-claude/user-management)[Workspaces](/docs/en/manage-claude/workspaces)

Authentication

[Overview](/docs/en/manage-claude/authentication)[Create an Admin API key](/docs/en/manage-claude/admin-api-keys)[App Attest](/docs/en/manage-claude/app-attest)[Workload Identity Federation](/docs/en/manage-claude/workload-identity-federation)[Manage WIF via API](/docs/en/manage-claude/wif-admin-api)[WIF reference](/docs/en/manage-claude/wif-reference)

Identity providers

[AWS](/docs/en/manage-claude/wif-providers/aws)[Google Cloud](/docs/en/manage-claude/wif-providers/gcp)[Microsoft Entra ID](/docs/en/manage-claude/wif-providers/azure)[GitHub Actions](/docs/en/manage-claude/wif-providers/github-actions)[Kubernetes](/docs/en/manage-claude/wif-providers/kubernetes)[SPIFFE](/docs/en/manage-claude/wif-providers/spiffe)[Okta](/docs/en/manage-claude/wif-providers/okta)

Monitoring

[Usage and Cost API](/docs/en/manage-claude/usage-cost-api)[Rate Limits API](/docs/en/manage-claude/rate-limits-api)[Analytics APIs](/docs/en/manage-claude/analytics-api)[Claude Code Analytics API](/docs/en/manage-claude/claude-code-analytics-api)[Spend Limits API](/docs/en/manage-claude/spend-limits-api)

Data & compliance

[Data residency](/docs/en/manage-claude/data-residency)[API and data retention](/docs/en/manage-claude/api-and-data-retention)[Access Transparency](/docs/en/manage-claude/access-transparency)

[Encryption keys](/docs/en/manage-claude/cmek)

[Inference hooks](/docs/en/manage-claude/inference-hooks)

Compliance API

[Overview](/docs/en/manage-claude/compliance-api)[Set up the Compliance API](/docs/en/manage-claude/compliance-api-access)[Activity Feed](/docs/en/manage-claude/compliance-activity-feed)[Chats, files, and projects](/docs/en/manage-claude/compliance-content-data)[Session transcripts](/docs/en/manage-claude/compliance-sessions)[Organizations, users, roles, groups, and settings](/docs/en/manage-claude/compliance-org-data)[Design your integration](/docs/en/manage-claude/compliance-integration-patterns)[Errors](/docs/en/manage-claude/compliance-errors)[FAQ](/docs/en/manage-claude/compliance-faq)

[Console](/)

[Admin](/docs/en/manage-claude/admin-api)Identity providers

# Use WIF with Microsoft Entra ID

Copy page



Federate Azure managed identities and Entra Workload Identity with the Claude API so your Azure workloads can call Claude without static API keys.

Copy page



Azure workloads authenticate to the Claude API by presenting a JSON Web Token (JWT) issued by Microsoft Entra ID, then exchanging it for a short-lived Anthropic access token. The setup follows the same shape on every Azure platform:

1.  **Register the token audience:** Create one app registration in your Microsoft Entra tenant to represent the Claude API audience. Every workload in the tenant requests Entra tokens for it.
2.  **Set up the identity for your platform:** A managed identity on VMs, VM Scale Sets, App Service, Functions, and Container Apps, or Entra Workload Identity on AKS.
3.  **Configure Anthropic:** Register your tenant's Entra issuer, create a service account, and write a federation rule that matches the token's claims.
4.  **Exchange at runtime:** Your workload exchanges its Entra-issued token at `POST /v1/oauth/token` for an `sk-ant-oat01-...` Anthropic access token and calls Claude with it.

On both paths the token you present to Anthropic carries your tenant-specific Entra issuer and the managed identity's object ID in the `sub` and `oid` claims; only how the workload obtains that token differs. Pick the section for where your workload runs: [Use a managed identity](#use-a-managed-identity) for VMs, VM Scale Sets, App Service, Functions, or Container Apps; [Use Entra Workload Identity on AKS](#use-entra-workload-identity-on-aks) for AKS.

## Prerequisites

- Familiarity with [WIF concepts](/docs/en/manage-claude/workload-identity-federation#concepts): service accounts, federation issuers, and federation rules.
- An Azure subscription with permission to assign managed identities (or configure Entra Workload Identity on AKS).
- Permission to create one app registration and service principal in your Microsoft Entra tenant (the shared Claude API audience). Entra only issues tokens for an audience that exists in the tenant, so the [Register the token audience](#register-the-token-audience) step is required before any token request succeeds.
- Your Microsoft Entra tenant ID. Find it in the Azure portal under **Microsoft Entra ID → Overview → Tenant ID**.
- Permission to create service accounts, federation issuers, and federation rules in the Claude Console for your Anthropic organization.

## Register the token audience

Microsoft Entra ID only issues a token when the requested audience exists in your tenant as an app registration with a service principal. Create one app registration to represent the Claude API audience; every workload in the tenant can request tokens for it. Without this registration, token requests fail with a "resource not found in tenant" error (`AADSTS50001` from the managed identity endpoints, `AADSTS500011` from the Entra token endpoint).

```python
# Create the app registration that represents the Claude API audience.
APP_ID=$(az ad app create --display-name claude-api-federation --query appId -o tsv)

# Request v2.0 access tokens and set the api://<APP_ID> identifier URI.
az ad app update --id "$APP_ID" \
  --identifier-uris "api://$APP_ID" \
  --set api.requestedAccessTokenVersion=2

# Create the service principal so the audience resolves in your tenant.
az ad sp create --id "$APP_ID"
```





Use the `api://<APP_ID>` identifier URI format. Entra restricts `https://` identifier URIs to verified domains of your own tenant, so a URI such as `https://api.anthropic.com` cannot be registered in most tenants; `api://<APP_ID>` is accepted everywhere. With `requestedAccessTokenVersion: 2`, tokens for this audience are v2.0, which is what this guide assumes. If you reuse an existing registration that emits v1.0 tokens, see [If your tokens are v1.0](#if-your-tokens-are-v1-0).

## Use a managed identity

Use this path when your workload runs on a VM, a VM Scale Set, App Service, Functions, or Container Apps. The workload requests an Entra-issued JWT for its assigned managed identity from the platform's local token endpoint, then exchanges that JWT with Anthropic.

### Configure the managed identity

1.  1

    ### Attach a managed identity

    Enable a system-assigned or user-assigned managed identity on your Azure resource. In the Azure portal, open the resource, go to **Identity**, and turn on **System assigned** (or attach a user-assigned identity).

    After the identity is created, note its **Object (principal) ID**. This GUID appears as both the `sub` and `oid` claims in the issued token, and your Anthropic federation rule will match on it. You can find it on the resource's **Identity** page; for a user-assigned identity, it is the **Object (principal) ID** on the managed identity resource's **Overview** page. (A managed identity has only a service principal in Microsoft Entra ID, not an app registration.)

2.  2

    ### Find the platform's token endpoint

    The platform exposes a local token endpoint once the identity is attached:

    - **VMs and VM Scale Sets:** IMDS at `http://169.254.169.254/metadata/identity/oauth2/token` with the header `Metadata: true` and `api-version=2018-02-01`.
    - **App Service, Functions, and Container Apps:** The URL in the `IDENTITY_ENDPOINT` environment variable with the header `X-IDENTITY-HEADER` set to the value of `IDENTITY_HEADER`, and `api-version=2019-08-01`. IMDS is not reachable on these platforms.

    If the resource has more than one user-assigned managed identity, add `client_id=<IDENTITY_CLIENT_ID>` to the token request to select one. Azure recommends always specifying it. Without it, the outcome depends on whether the resource also has a system-assigned identity enabled: if it does, the request silently falls back to that identity and then fails your federation rule's `oid` match; if it does not, the request fails outright as soon as a second user-assigned identity is attached.

3.  3

    ### Decode a sample token

    Request a token from the endpoint and decode its payload to confirm the claims your federation rule needs to match. (For the decode command, see [Troubleshoot a failed exchange](/docs/en/manage-claude/wif-reference#troubleshoot-a-failed-exchange).) A v2.0 token for a managed identity carries these claims:

    ``` shiki
    {
      "iss": "https://login.microsoftonline.com/<TENANT_ID>/v2.0",
      "sub": "9f8e7d6c-1a2b-3c4d-5e6f-...",
      "aud": "<APP_ID>",
      "oid": "9f8e7d6c-1a2b-3c4d-5e6f-...",
      "tid": "<TENANT_ID>",
      "azp": "<IDENTITY_CLIENT_ID>",
      "ver": "2.0",
      "exp": 1775527120
    }
    ```

    

    | Claim | Value                                                                                                                            | Match this when                                                                                                                                                |
    |:------|:---------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | `oid` | The managed identity's object ID, identical to `sub`                                                                             | You want to authorize one specific managed identity. This is the default; the rule in [Configure Anthropic](#configure-anthropic) matches it.                  |
    | `azp` | The calling identity's client ID                                                                                                 | You want to authorize every workload that shares one app registration. For a managed identity, `azp` is unique to that identity, so it is equivalent to `oid`. |
    | `aud` | The audience app registration's client ID (the `<APP_ID>` GUID from [Register the token audience](#register-the-token-audience)) | Always. The rule's `audience` field must equal the token's `aud` value exactly.                                                                                |
    | `tid` | Your tenant ID                                                                                                                   | You want defense in depth. The issuer URL already pins the tenant.                                                                                             |

    If the decoded token's `ver` claim is `1.0`, the claim names and values differ. See [If your tokens are v1.0](#if-your-tokens-are-v1-0) before continuing.

### Configure Anthropic

In the Claude Console, open **Settings → Workload identity**, click **Connect workload**, and select the **Microsoft Entra** tile. The wizard walks you through registering the issuer, creating a service account, and creating a federation rule.

The wizard creates these resources for you. Use the following values whether you enter them in the wizard or send them to the [Admin API](/docs/en/manage-claude/wif-admin-api):

**Federation issuer:** Choose **v2.0 (login.microsoftonline.com)** in the wizard's **Token issuer** selector. (The selector defaults to v1; that default exists for tenants reusing older registrations that still emit v1.0 tokens.) Entra publishes an OIDC discovery document at the per-tenant issuer URL, so use discovery mode. Each Microsoft Entra tenant you federate needs its own issuer record.

```python
{
  "name": "azure-prod-tenant",
  "issuer_url": "https://login.microsoftonline.com/<TENANT_ID>/v2.0",
  "jwks": { "type": "discovery" },
  "max_jwt_lifetime_seconds": 86400
}
```





Managed identity workloads need `max_jwt_lifetime_seconds: 86400`. Azure issues managed identity tokens with up to 24 hours between `iat` and `exp` because it caches each resource's token for that window and offers no way to force an early refresh, and the issuer's 1-hour default rejects those tokens, so the exchange fails with the opaque `401` `authentication_error` response (message `Authentication failed`). The Connect workload wizard's Microsoft Entra tile creates the issuer with `max_jwt_lifetime_seconds` set to `7500` and provides no field to change it during creation, so finish the wizard, then open **Settings → Workload identity → Issuers**, edit the issuer, and raise the value to `86400`. You can also update the issuer through the Admin API.

A longer accepted lifetime means a leaked Entra token stays exchangeable for longer. If a token leaks, the lever is disabling the federation rule; a tight `oid` match limits which identities can exchange a token in the first place, as described in [Scope your rule](#scope-your-rule).

**Federation rule:** Match on the managed identity's object ID and your tenant ID. For the v2.0 tokens this guide configures, the `audience` value is the audience app registration's client ID (the `<APP_ID>` GUID from [Register the token audience](#register-the-token-audience)). Use the exact `aud` value from your decoded token.

```python
{
  "name": "azure-inference-worker",
  "issuer_id": "fdis_...",
  "match": {
    "audience": "<APP_ID>",
    "claims": {
      "oid": "9f8e7d6c-1a2b-3c4d-5e6f-...",
      "tid": "<TENANT_ID>"
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

`token_lifetime_seconds` is the lifetime of the Anthropic access token the exchange returns, not of the Entra token; the SDK refreshes it for you.

### Acquire and use the token

At runtime your workload fetches its Entra token, exchanges it at `POST /v1/oauth/token`, and uses the returned bearer token to call Claude. Each Anthropic SDK handles the exchange and refresh loop when you supply `identity_token_provider`, as shown in the following examples. The cURL tab shows the raw flow.

The samples fetch the managed identity token from the platform's token endpoint: IMDS on VMs and VM Scale Sets, or the `IDENTITY_ENDPOINT` service on App Service, Functions, and Container Apps. Replace `<APP_ID>` in the `api://<APP_ID>` resource value with the audience app registration's client ID from [Register the token audience](#register-the-token-audience).



If your workload already uses the Azure Identity client library, pass its token acquisition (`DefaultAzureCredential` with the scope `api://<APP_ID>/.default`) to `identity_token_provider` instead of calling the token endpoints directly. The library selects the correct endpoint on every Azure platform, including AKS with Entra Workload Identity.

cURL

Python

TypeScript

Go

Java

C#

PHP

Ruby

CLI



```python
import os

import anthropic
import requests
from anthropic import WorkloadIdentityCredentials

# The audience app registration's identifier URI (see Register the token audience).
AUDIENCE = "api://<APP_ID>"


def fetch_entra_token() -> str:
    """Fetch a managed identity token from the platform's token endpoint."""
    # With multiple user-assigned identities, add client_id=<IDENTITY_CLIENT_ID>
    # to the request params to select one.
    if endpoint := os.environ.get("IDENTITY_ENDPOINT"):
        # App Service, Functions, Container Apps
        response = requests.get(
            endpoint,
            headers={"X-IDENTITY-HEADER": os.environ["IDENTITY_HEADER"]},
            params={"api-version": "2019-08-01", "resource": AUDIENCE},
            timeout=5,
        )
    else:
        # VM or VM Scale Set: Azure Instance Metadata Service (IMDS)
        response = requests.get(
            "http://169.254.169.254/metadata/identity/oauth2/token",
            headers={"Metadata": "true"},
            params={"api-version": "2018-02-01", "resource": AUDIENCE},
            timeout=5,
        )
    response.raise_for_status()
    return response.json()["access_token"]


client = anthropic.Anthropic(
    credentials=WorkloadIdentityCredentials(
        identity_token_provider=fetch_entra_token,
        federation_rule_id=os.environ["ANTHROPIC_FEDERATION_RULE_ID"],
        organization_id=os.environ["ANTHROPIC_ORGANIZATION_ID"],
        service_account_id=os.environ["ANTHROPIC_SERVICE_ACCOUNT_ID"],
        workspace_id=os.environ.get("ANTHROPIC_WORKSPACE_ID"),
    ),
)

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello from Azure"}],
)
print(next(block.text for block in message.content if block.type == "text"))
```

### Verify the setup

From your Azure resource, run the cURL exchange shown in [Acquire and use the token](#acquire-and-use-the-token) and confirm that `POST /v1/oauth/token` returns a `200` with an `access_token` beginning with `sk-ant-oat01-` and an `expires_in` value in seconds. If the exchange fails with the opaque `401` `authentication_error` response (message `Authentication failed`), check the [authentication history page](https://platform.claude.com/settings/workload-identity-federation?tab=history) for the deny reason, then decode the Entra token (see [Troubleshoot a failed exchange](/docs/en/manage-claude/wif-reference#troubleshoot-a-failed-exchange) for the command) and check the most common Azure-side causes:

- **Issuer mismatch:** The registered `issuer_url` must match the token's `iss` claim exactly. A v2.0 token carries `https://login.microsoftonline.com/<TENANT_ID>/v2.0`; if the decoded `ver` claim is `1.0`, see [If your tokens are v1.0](#if-your-tokens-are-v1-0).
- **Token lifetime:** Managed identity tokens carry up to 24 hours between `iat` and `exp`. If the issuer still has the wizard's `7500` (or the 1-hour default), raise `max_jwt_lifetime_seconds` to `86400` as described in [Configure Anthropic](#configure-anthropic).
- **Audience mismatch:** The rule's `audience` must equal the token's `aud` exactly: the audience app registration's client ID for the v2.0 tokens this guide configures.
- **Claim name mismatch:** A rule that matches on a claim the token does not carry never passes. v1.0 tokens carry the client ID in `appid`, not `azp`; see [If your tokens are v1.0](#if-your-tokens-are-v1-0).

## Use Entra Workload Identity on AKS

Use this path when your workload runs in an AKS pod. Entra Workload Identity federates a Kubernetes service account with a user-assigned managed identity: Kubernetes projects a service account token (signed by the AKS cluster's OIDC issuer) into the pod at the path in `AZURE_FEDERATED_TOKEN_FILE`. That projected token is not an Entra-issued token, so to stay on the Entra-mediated path described on this page, the workload performs a two-hop exchange: it first redeems the projected token at `https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/token` (federated `client_credentials` grant) for an Entra-issued access token, then passes that Entra token to the Anthropic SDK as the identity token.



AKS pods can alternatively skip the Entra exchange and present the Kubernetes-projected service account token to Anthropic directly. That path registers your AKS cluster's OIDC issuer with Anthropic instead of your Entra tenant. See [Use WIF with Kubernetes](/docs/en/manage-claude/wif-providers/kubernetes) for that flow.

### Configure Entra Workload Identity

1.  1

    ### Enable the OIDC issuer and workload identity on your cluster

    Enabling workload identity installs the `azure-workload-identity` mutating webhook for you; deploy it manually only on non-AKS clusters. Capture the cluster's OIDC issuer URL for the federated credential you create in a later step.

    ``` shiki
    az aks update \
      --resource-group <RESOURCE_GROUP> \
      --name <CLUSTER_NAME> \
      --enable-oidc-issuer \
      --enable-workload-identity

    AKS_OIDC_ISSUER=$(az aks show \
      --resource-group <RESOURCE_GROUP> \
      --name <CLUSTER_NAME> \
      --query oidcIssuerProfile.issuerUrl -o tsv)
    ```

    

2.  2

    ### Create a user-assigned managed identity

    Capture two values from the identity: the **Client ID** goes into the service account annotation (and is injected into the pod as `AZURE_CLIENT_ID`), and the **Object (principal) ID** appears as the `oid` claim that your Anthropic federation rule matches.

    ``` shiki
    az identity create \
      --resource-group <RESOURCE_GROUP> \
      --name claude-inference-identity \
      --location <LOCATION>

    # Goes in the service account annotation; injected into the pod as AZURE_CLIENT_ID.
    IDENTITY_CLIENT_ID=$(az identity show \
      --resource-group <RESOURCE_GROUP> \
      --name claude-inference-identity \
      --query clientId -o tsv)

    # Appears as the oid claim that your federation rule matches.
    IDENTITY_OBJECT_ID=$(az identity show \
      --resource-group <RESOURCE_GROUP> \
      --name claude-inference-identity \
      --query principalId -o tsv)
    ```

    

3.  3

    ### Create the annotated Kubernetes service account

    The `azure-workload-identity` webhook reads the `azure.workload.identity/client-id` annotation to inject `AZURE_CLIENT_ID` into the pod, which the samples in [Acquire and use the token](#acquire-and-use-the-token-2) read from the environment.

    ``` shiki
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: claude-inference
      namespace: inference
      annotations:
        azure.workload.identity/client-id: <IDENTITY_CLIENT_ID>
    ```

    

4.  4

    ### Create the federated credential on the managed identity

    The federated credential trusts your cluster's OIDC issuer for that specific service account. The `--audience api://AzureADTokenExchange` value is Entra's fixed audience for incoming Kubernetes service account tokens; it is unrelated to the Claude API audience you registered earlier.

    ``` shiki
    az identity federated-credential create \
      --resource-group <RESOURCE_GROUP> \
      --identity-name claude-inference-identity \
      --name claude-inference-aks \
      --issuer "$AKS_OIDC_ISSUER" \
      --subject system:serviceaccount:inference:claude-inference \
      --audience api://AzureADTokenExchange
    ```

    

5.  5

    ### Label the pod and set its service account

    The pod must carry the `azure.workload.identity/use: "true"` label and run as the annotated service account. The webhook then injects `AZURE_FEDERATED_TOKEN_FILE`, `AZURE_CLIENT_ID`, and `AZURE_TENANT_ID` into the pod. The file at `AZURE_FEDERATED_TOKEN_FILE` contains the Kubernetes-projected service account token, signed by the AKS cluster's OIDC issuer.

    ``` shiki
    apiVersion: v1
    kind: Pod
    metadata:
      name: inference-worker
      namespace: inference
      labels:
        azure.workload.identity/use: "true"
    spec:
      serviceAccountName: claude-inference
      containers:
        - name: app
          image: your-registry/inference-worker:latest
    ```

    

6.  6

    ### Decode a sample token

    The token your Anthropic federation rule sees is not the projected file; it is the Entra-issued token returned by the `client_credentials` exchange. From inside a labeled pod, run step 1 of the cURL sample in [Acquire and use the token](#acquire-and-use-the-token-2) and decode the result. It carries the same claim shape as the managed identity path:

    ``` shiki
    {
      "iss": "https://login.microsoftonline.com/<TENANT_ID>/v2.0",
      "sub": "9f8e7d6c-1a2b-3c4d-5e6f-...",
      "aud": "<APP_ID>",
      "oid": "9f8e7d6c-1a2b-3c4d-5e6f-...",
      "tid": "<TENANT_ID>",
      "azp": "<IDENTITY_CLIENT_ID>",
      "ver": "2.0",
      "exp": 1775527120
    }
    ```

    

    `sub` and `oid` are the managed identity's object ID, `aud` is the audience app registration's client ID, and `azp` is the managed identity's client ID (the value of `AZURE_CLIENT_ID`). The lifetime differs from the managed identity path: `client_credentials` tokens default to a random 60 to 90 minute window between `iat` and `exp`, not 24 hours.

### Configure Anthropic

In the Claude Console, open **Settings → Workload identity**, click **Connect workload**, and select the **Microsoft Entra** tile. The wizard walks you through registering the issuer, creating a service account, and creating a federation rule.

The wizard creates these resources for you. Use the following values whether you enter them in the wizard or send them to the [Admin API](/docs/en/manage-claude/wif-admin-api):

**Federation issuer:** Choose **v2.0 (login.microsoftonline.com)** in the wizard's **Token issuer** selector. (The selector defaults to v1; that default exists for tenants reusing older registrations that still emit v1.0 tokens.) Entra publishes an OIDC discovery document at the per-tenant issuer URL, so use discovery mode. Each Microsoft Entra tenant you federate needs its own issuer record.

```python
{
  "name": "azure-prod-tenant",
  "issuer_url": "https://login.microsoftonline.com/<TENANT_ID>/v2.0",
  "jwks": { "type": "discovery" },
  "max_jwt_lifetime_seconds": 7500
}
```





The Connect workload wizard's Microsoft Entra tile creates the issuer with `max_jwt_lifetime_seconds` set to `7500` (just over 2 hours), which covers the default 60 to 90 minute lifetime of `client_credentials` tokens. A tenant token-lifetime policy or Continuous Access Evaluation (CAE) can extend that lifetime. If your decoded token's `exp` minus `iat` exceeds 7500 seconds, edit the issuer in **Settings → Workload identity → Issuers** and raise `max_jwt_lifetime_seconds` to match, or exchanges fail with the opaque `401` `authentication_error` response (message `Authentication failed`). If your tenant also runs managed-identity workloads from [Use a managed identity](#use-a-managed-identity), use that section's `86400` value, which covers both paths.

A longer accepted lifetime means a leaked Entra token stays exchangeable for longer. If a token leaks, the lever is disabling the federation rule; a tight `oid` match limits which identities can exchange a token in the first place, as described in [Scope your rule](#scope-your-rule).

**Federation rule:** Match on the managed identity's object ID and your tenant ID. For the v2.0 tokens this guide configures, the `audience` value is the audience app registration's client ID (the `<APP_ID>` GUID from [Register the token audience](#register-the-token-audience)). Use the exact `aud` value from your decoded token.

```python
{
  "name": "azure-inference-worker",
  "issuer_id": "fdis_...",
  "match": {
    "audience": "<APP_ID>",
    "claims": {
      "oid": "9f8e7d6c-1a2b-3c4d-5e6f-...",
      "tid": "<TENANT_ID>"
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

`token_lifetime_seconds` is the lifetime of the Anthropic access token the exchange returns, not of the Entra token; the SDK refreshes it for you.

### Acquire and use the token

At runtime the pod performs the two-hop exchange: it sends the Kubernetes-projected token (the file at `AZURE_FEDERATED_TOKEN_FILE`) to Entra's token endpoint as a federated `client_credentials` assertion, then exchanges the resulting Entra access token at `POST /v1/oauth/token`. Each Anthropic SDK handles the second exchange and the refresh loop when you pass the Entra fetch to `identity_token_provider`, as shown in the following examples. The cURL tab shows the raw flow.

Two different client IDs appear in the samples. `<APP_ID>` is the audience app registration's client ID from [Register the token audience](#register-the-token-audience); the scope `api://<APP_ID>/.default` asks Entra for a token addressed to that audience. `$AZURE_CLIENT_ID` is the managed identity's client ID, injected by the webhook, and identifies the caller. Do not substitute one for the other.



If your workload already uses the Azure Identity client library, pass its token acquisition (`DefaultAzureCredential` with the scope `api://<APP_ID>/.default`) to `identity_token_provider` instead of performing the two-hop exchange yourself. The library reads the same `AZURE_FEDERATED_TOKEN_FILE`, `AZURE_CLIENT_ID`, and `AZURE_TENANT_ID` environment variables and handles the Entra exchange.

cURL

Python

TypeScript

Go

Java

C#

PHP

Ruby

CLI



```python
import os
from pathlib import Path

import anthropic
import requests
from anthropic import WorkloadIdentityCredentials


def fetch_entra_token_via_federation() -> str:
    federated_token = Path(os.environ["AZURE_FEDERATED_TOKEN_FILE"]).read_text()
    response = requests.post(
        f"https://login.microsoftonline.com/{os.environ['AZURE_TENANT_ID']}/oauth2/v2.0/token",
        data={
            "client_id": os.environ["AZURE_CLIENT_ID"],
            "grant_type": "client_credentials",
            "scope": "api://<APP_ID>/.default",
            "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
            "client_assertion": federated_token,
        },
        timeout=5,
    )
    response.raise_for_status()
    return response.json()["access_token"]


client = anthropic.Anthropic(
    credentials=WorkloadIdentityCredentials(
        identity_token_provider=fetch_entra_token_via_federation,
        federation_rule_id=os.environ["ANTHROPIC_FEDERATION_RULE_ID"],
        organization_id=os.environ["ANTHROPIC_ORGANIZATION_ID"],
        service_account_id=os.environ["ANTHROPIC_SERVICE_ACCOUNT_ID"],
        workspace_id=os.environ.get("ANTHROPIC_WORKSPACE_ID"),
    ),
)

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello from Azure"}],
)
print(next(block.text for block in message.content if block.type == "text"))
```

### Verify the setup

From inside a labeled pod, run the cURL exchange shown in [Acquire and use the token](#acquire-and-use-the-token-2) and confirm that `POST /v1/oauth/token` returns a `200` with an `access_token` beginning with `sk-ant-oat01-` and an `expires_in` value in seconds. If the exchange fails with the opaque `401` `authentication_error` response (message `Authentication failed`), check the [authentication history page](https://platform.claude.com/settings/workload-identity-federation?tab=history) for the deny reason, then decode the Entra-issued token from step 1 (see [Troubleshoot a failed exchange](/docs/en/manage-claude/wif-reference#troubleshoot-a-failed-exchange) for the command) and check the most common Azure-side causes:

- **Issuer mismatch:** The registered `issuer_url` must match the token's `iss` claim exactly. A v2.0 token carries `https://login.microsoftonline.com/<TENANT_ID>/v2.0`; if the decoded `ver` claim is `1.0`, see [If your tokens are v1.0](#if-your-tokens-are-v1-0).
- **Token lifetime:** If a tenant token-lifetime policy or CAE extends the `client_credentials` token past 7500 seconds, raise the issuer's `max_jwt_lifetime_seconds` as described in [Configure Anthropic](#configure-anthropic-2).
- **Audience mismatch:** The rule's `audience` must equal the token's `aud` exactly: the audience app registration's client ID for the v2.0 tokens this guide configures.
- **Claim name mismatch:** A rule that matches on a claim the token does not carry never passes. v1.0 tokens carry the client ID in `appid`, not `azp`; see [If your tokens are v1.0](#if-your-tokens-are-v1-0).

## If your tokens are v1.0

This guide configures the audience app registration with `api.requestedAccessTokenVersion: 2`, so every token it shows is v2.0. If you reuse an existing registration that leaves `requestedAccessTokenVersion` unset, Entra issues v1.0 tokens instead. Decode a sample token and check its `ver` claim; if it is `1.0`, four things change:

- **Issuer:** The `iss` claim is `https://sts.windows.net/<TENANT_ID>/` instead of `https://login.microsoftonline.com/<TENANT_ID>/v2.0`. Register the issuer URL exactly as your token's `iss` claim carries it. The two URLs share the same JWKS, so discovery mode works for either.
- **Wizard selector:** Pick **v1 (sts.windows.net)** in the Connect workload wizard's **Token issuer** selector instead of **v2.0 (login.microsoftonline.com)**.
- **Audience:** The `aud` claim is the identifier URI you passed as `resource` (for example, `api://<APP_ID>`), not the registration's client ID. Set the federation rule's `audience` to the exact `aud` value from your decoded token.
- **Client ID claim:** The calling identity's client ID appears in `appid`, not `azp`. The two claims never appear in the same token, so a rule that matches on `azp` never passes against a v1.0 token.

The `oid`, `sub`, and `tid` claims carry the same values in both versions, so the rest of this guide applies unchanged.

## Scope your rule

A federation rule can match the token's subject with `subject_prefix` in addition to (or instead of) the `claims` map; see [Rule matching semantics](/docs/en/manage-claude/wif-reference#rule-matching-semantics) for how the fields combine. Entra `sub` values for these identities are fixed-length canonical GUIDs, so a `subject_prefix` containing the full 36-character object ID matches only that subject; this is a property of Entra's subject format, not of `subject_prefix` in general.



Every identity in your tenant can request a token for the registered audience, so `audience` and `tid` alone do not identify a specific workload. A rule that omits an `oid` (or `azp`/`appid`) match, or that uses a wildcard or partial-GUID `subject_prefix`, authorizes every managed identity and service principal in the tenant.

Lock the rule's `match` block to the narrowest scope that fits your use case:

- **Match `oid` as an exact value:** Set `claims.oid` to the managed identity's full object ID. A `subject_prefix` set to that full object ID is equivalent (the Console wizard sets both); never use a wildcard or partial-GUID `subject_prefix`, which matches more identities than you intend.
- **Pin `tid` as defense in depth:** The issuer URL already pins your tenant, but adding `claims.tid` guards against configuration drift if the issuer record is later edited.
- **Pin the audience:** Set `audience` to the exact `aud` value from your decoded token so tokens minted for other applications are rejected.
- **Use a separate rule for each managed identity:** Create one rule for each identity rather than one rule that authorizes several, so you can revoke a single workload's access without affecting others.

## Next steps

- Review the full configuration model in [Workload Identity Federation](/docs/en/manage-claude/workload-identity-federation).
- See the [provider guides](/docs/en/manage-claude/workload-identity-federation#identity-providers) for AWS, Google Cloud, GitHub Actions, and Kubernetes.
- For environment variables, profile files, and credential precedence, see the [WIF reference](/docs/en/manage-claude/wif-reference).
