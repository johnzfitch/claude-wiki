---
title: "Use WIF with Kubernetes - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/wif-providers/kubernetes"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:46Z"
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


[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fwif-providers%2Fkubernetes)

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

# Use WIF with Kubernetes

Copy page



Authenticate to the Claude API from self-managed Kubernetes clusters using projected service account tokens.

Copy page



Self-managed Kubernetes clusters (kubeadm, k3s, OpenShift, and on-premises distributions) sign OIDC JSON Web Tokens (JWTs) for every pod through [projected service account tokens](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#serviceaccount-token-volume-projection). The cluster's API server acts as the OIDC issuer, and each token's `sub` claim follows the form `system:serviceaccount:<namespace>:<service-account>`. You can find your cluster's issuer URL by reading its discovery document:

cURL



```python
kubectl get --raw /.well-known/openid-configuration | jq -r .issuer
```



The mechanism on this page (projected service-account token, cluster API server as the OIDC issuer) is native to Kubernetes itself, so it underlies every Kubernetes distribution. If you run on a managed Kubernetes service, the cloud provider guides walk through where to find the provider-managed issuer URL: [AWS (EKS)](manage-claude-wif-providers-aws.md#use-eks-projected-service-account-tokens), [Google Cloud (GKE)](manage-claude-wif-providers-gcp.md), or [Azure (AKS)](manage-claude-wif-providers-azure.md). If your cluster runs SPIRE, the SPIRE OIDC Discovery Provider is the issuer rather than the cluster API server; see [SPIFFE](manage-claude-wif-providers-spiffe.md). For any other distribution or a managed provider not listed there, follow this guide and use the issuer URL your cluster reports.

## Prerequisites

- Familiarity with [WIF concepts](manage-claude-workload-identity-federation.md#concepts): service accounts, federation issuers, and federation rules.
- A Kubernetes cluster with the [`--service-account-issuer`](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/) flag configured on the API server. Most distributions set this by default; kubeadm clusters typically use `https://kubernetes.default.svc.cluster.local`. Your platform team can confirm the value if you don't have direct access to the API server configuration.
- One of the following so Anthropic can validate token signatures:
  - The issuer's JWKS endpoint is reachable from the public internet over HTTPS on port 443, or
  - You can fetch the JWKS from inside the cluster and register it in `inline` mode (covered in [Configure Anthropic](#configure-anthropic)).
- Permission to create service accounts, federation issuers, and federation rules in the Claude Console for your Anthropic organization.

## Configure Kubernetes

Project a service account token into your pod with the audience and lifetime that your federation rule expects. The `serviceAccountToken` projection writes a fresh JWT to the mount path and rotates it before `expirationSeconds` elapses.

Pod



```python
apiVersion: v1
kind: Pod
metadata:
  name: inference-worker
  namespace: inference
spec:
  serviceAccountName: inference-worker
  volumes:
    - name: anthropic-token
      projected:
        sources:
          - serviceAccountToken:
              audience: https://api.anthropic.com
              expirationSeconds: 3600
              path: token
  containers:
    - name: app
      image: your-registry/inference-worker:latest
      env:
        - name: ANTHROPIC_IDENTITY_TOKEN_FILE
          value: /var/run/secrets/anthropic.com/token
        - name: ANTHROPIC_FEDERATION_RULE_ID
          value: fdrl_...
        - name: ANTHROPIC_ORGANIZATION_ID
          value: 00000000-0000-0000-0000-000000000000
        - name: ANTHROPIC_SERVICE_ACCOUNT_ID
          value: svac_...
        - name: ANTHROPIC_WORKSPACE_ID  # required when the rule covers multiple workspaces
          value: wrkspc_...
      volumeMounts:
        - name: anthropic-token
          mountPath: /var/run/secrets/anthropic.com
          readOnly: true
```

The token issued for this pod carries `sub: "system:serviceaccount:inference:inference-worker"` and `aud: ["https://api.anthropic.com"]`.

## Configure Anthropic

In the Claude Console, open **Settings → Workload identity**, click **Connect workload**, and select the **Kubernetes** tile. The wizard walks you through registering the issuer, creating a service account, and creating a federation rule.

The wizard creates these resources for you. Use the following values whether you enter them in the wizard or send them to the [Admin API](manage-claude-wif-admin-api.md):

**Federation issuer:** Many self-managed clusters use an issuer URL such as `https://kubernetes.default.svc.cluster.local` that is not reachable from the public internet. If that applies to your cluster, choose the **inline** JWKS source and paste the cluster's keys. Fetch them from inside the cluster:

cURL



```python
kubectl get --raw /openid/v1/jwks
```

Then configure the issuer with the contents of the returned `keys` array (not the surrounding `{"keys": [...]}` wrapper):

```python
{
  "name": "onprem-k8s",
  "issuer_url": "https://kubernetes.default.svc.cluster.local",
  "jwks": {
    "type": "inline",
    "keys": [{ "kty": "RSA", "kid": "...", "n": "...", "e": "AQAB" }]
  }
}
```



In `inline` mode the `issuer_url` is only compared against the JWT's `iss` claim; Anthropic never attempts to reach it. If your issuer is publicly reachable, use `"jwks": {"type": "discovery"}` instead.



With `inline` keys you are responsible for updating the issuer when the cluster rotates its service account signing key. Rotation is rare (typically only during cluster upgrades), but token exchanges fail with a signature error until you push the new JWKS.

**Federation rule:** Match the service account's `sub` claim and the audience you set on the projected token.

```python
{
  "name": "onprem-inference",
  "issuer_id": "fdis_...",
  "match": {
    "subject_prefix": "system:serviceaccount:inference:inference-worker",
    "audience": "https://api.anthropic.com"
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

Be as specific as the workload allows. Loosen `subject_prefix` to `system:serviceaccount:inference:*` (the trailing `*` makes it a prefix match) only if every service account in the namespace should map to the same Anthropic service account. Add the rule's `fdrl_...` ID to your pod's `ANTHROPIC_FEDERATION_RULE_ID` environment variable.

## Acquire and use the token

The pod spec in [Configure Kubernetes](#configure-kubernetes) sets `ANTHROPIC_IDENTITY_TOKEN_FILE` to the projected mount path, along with `ANTHROPIC_FEDERATION_RULE_ID`, `ANTHROPIC_ORGANIZATION_ID`, `ANTHROPIC_SERVICE_ACCOUNT_ID`, and `ANTHROPIC_WORKSPACE_ID`. With those in place, the SDK reads the token from disk on every exchange and refreshes the Anthropic access token automatically.

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
import anthropic

# Reads ANTHROPIC_IDENTITY_TOKEN_FILE, ANTHROPIC_FEDERATION_RULE_ID,
# ANTHROPIC_ORGANIZATION_ID, ANTHROPIC_SERVICE_ACCOUNT_ID, and ANTHROPIC_WORKSPACE_ID
# from the pod's environment.
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(next(block.text for block in message.content if block.type == "text"))
```

## Verify the setup

A successful exchange returns an `access_token` beginning with `sk-ant-oat01-` and an `expires_in` value in seconds. If the exchange fails with the opaque `401` `authentication_error` response (message `Authentication failed`), check the [authentication history page](https://platform.claude.com/settings/workload-identity-federation?tab=history) for the deny reason and see [Troubleshoot a failed exchange](manage-claude-wif-reference.md#troubleshoot-a-failed-exchange); the most common Kubernetes-side cause is a JWKS key mismatch (for `inline` mode, re-fetch with `kubectl get --raw /openid/v1/jwks` and update the issuer).

## Scope your rule



A `subject_prefix` of `system:serviceaccount:*` matches every service account in the cluster, so any pod can obtain a federated Anthropic token. Without an `audience` matcher, the rule also matches the cluster's default-audience tokens, which every pod already has projected.

Lock the rule's `match` block to the narrowest scope that fits your use case:

- **Pin namespace and service-account name:** Use the full `system:serviceaccount:<namespace>:<name>` value with no trailing `*`.
- **Always set an audience:** Require `audience` on the rule and set the same value on the pod's `serviceAccountToken` projection so default-audience tokens are rejected.
- **Use a separate rule per namespace:** Create a distinct rule and Anthropic service account for each namespace rather than widening one rule.
- **Scope inline-JWKS issuers to one cluster:** When several clusters share an issuer URL, register each cluster's JWKS as its own federation issuer and bind rules to that issuer only.

## Next steps

- [Workload Identity Federation](manage-claude-workload-identity-federation.md): concepts, the token-exchange flow, and SDK configuration options.
- [WIF reference](manage-claude-wif-reference.md): environment variables, JWKS source modes, and rule match modes.
