---
title: "Use WIF with Okta - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/wif-providers/okta"
category: "04-API-Reference/Other"
fetched_at: "2026-11-13T06:34:08Z"
tags: ["api"]
---

# Use WIF with Okta

Copy page



Federate Okta service application identities to the Claude API with Workload Identity Federation.

Copy page



Okta can act as a workload identity provider by issuing OIDC access tokens to a **service application** through the OAuth 2.0 `client_credentials` grant. Your workload authenticates to Okta (typically with `private_key_jwt`, so you store no shared secret) and receives a signed JSON Web Token (JWT). It then exchanges that JWT with Anthropic for a short-lived access token.

The Okta authorization server’s issuer URL takes the form `https://<your-domain>.okta.com/oauth2/<auth-server-id>`. If you use the built-in default server, the path is `/oauth2/default`.



You must use an Okta **custom authorization server** (including the `default` one). External parties cannot validate tokens that the Okta org authorization server issues directly, because Okta does not publish signing keys for them. The org authorization server’s token endpoint is `/oauth2/v1/token`, with no authorization server ID in the path.

This page shows one way to configure and authenticate to Okta. Make sure your configuration and authentication mechanisms follow your company’s guidance and security practices.

## Prerequisites

- Familiarity with [Workload Identity Federation (WIF) concepts](manage-claude-workload-identity-federation.md#concepts): service accounts, federation issuers, and federation rules.
- An Okta organization with API Access Management enabled (required for custom authorization servers).
- Permission to create service accounts, federation issuers, and federation rules in the Claude Console for your Anthropic organization.
- A workload that can request a token from Okta’s `/v1/token` endpoint and reach `api.anthropic.com`.

## Configure Okta

At a high level you need to:

1.  Create an Okta service application.
2.  Configure your default authorization server (or create a new custom authorization server) with an audience, a scope, an access policy, and any custom claims you want to match on.

The exact navigation depends on your Okta org configuration and admin console version. The following numbered steps walk through one common path:

1.  **Create a service app integration.** In the Okta Admin Console, create a new app integration of type **API Services** (OIDC, machine-to-machine). Note the generated **Client ID**.
2.  **Configure client authentication.** For a keyless setup, select **Public key / Private key** (`private_key_jwt`) and register your workload’s public JWK. Alternatively, use a client secret if your environment can store one securely. For the following example, you might need to disable the Demonstrating Proof of Possession (DPoP) requirement on the application. Make sure your production setup meets your organization’s security requirements.
3.  **Set the audience.** On your custom authorization server, set the audience to `https://api.anthropic.com` so issued access tokens carry that `aud` claim. Anthropic validates `aud` against this fixed value.
4.  **Grant a scope.** On your custom authorization server, ensure at least one scope exists that the service app can request (for example, `anthropic.access`). Okta rejects `client_credentials` requests that do not include a granted scope.
5.  **Create an access policy.** On your custom authorization server, create an access policy with at least one rule that allows your service app to request the scope you granted in step 4.
6.  **(Optional) Add custom claims.** If you want to match on something other than the client ID, add a claim to the access token in your authorization server’s **Claims** tab.

For a service app using `client_credentials`, Okta sets the `sub` claim of the issued access token to the application’s **Client ID**, and `iss` to the authorization server’s issuer URL.

## Configure Anthropic

In the Claude Console, go to the [Workload identity](https://platform.claude.com/settings/workload-identity-federation) page (`platform.claude.com/settings/workload-identity-federation`), click **Connect workload**, and select **Custom OIDC**. The wizard walks you through registering the issuer, creating a service account, and creating a federation rule.

The wizard creates these resources for you. Use the following values whether you enter them in the wizard or send them to the [Admin API](manage-claude-wif-admin-api.md):

**Federation issuer:** Use your Okta custom authorization server URL and discovery mode. Anthropic reads Okta’s `.well-known/openid-configuration` discovery document and fetches the JWKS from the `jwks_uri` it advertises.

```python
{
  "name": "okta-prod",
  "issuer_url": "https://acme.okta.com/oauth2/aus1a2b3c4d5e6f7g8h9",
  "jwks": { "type": "discovery" }
}
```



**Federation rule:** Match on the Okta `sub` claim, which is the service app’s Client ID. If you defined custom claims in Okta, you can match on those instead with the `claims` map or a Common Expression Language (CEL) `condition`.

```python
{
  "name": "okta-pipeline",
  "issuer_id": "fdis_...",
  "match": {
    "subject_prefix": "0oa1b2c3d4e5f6g7h8i9",
    "audience": "https://api.anthropic.com"
  },
  "target": { "type": "service_account", "service_account_id": "svac_..." },
  "workspace_id": "wrkspc_...",
  "oauth_scope": "workspace:developer",
  "token_lifetime_seconds": 600
}
```



## Acquire a token and call the Claude API

Platform-native providers (AWS, Google Cloud, Kubernetes) make a token available inside the workload’s runtime, through a projected file or local metadata endpoint. Okta does not. Your workload must call Okta’s token endpoint to obtain a JWT, then pass that JWT to the SDK as the identity token.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
import os
import httpx2
import anthropic
from anthropic import WorkloadIdentityCredentials


def fetch_okta_token() -> str:
    response = httpx2.post(
        f"{os.environ['OKTA_ISSUER']}/v1/token",
        data={
            "grant_type": "client_credentials",
            "scope": "anthropic.access",
            "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
            # Build the RFC 7523 client_assertion JWT signed with your Okta app's private key
            "client_assertion": build_signed_client_assertion(),
        },
    )
    response.raise_for_status()
    return response.json()["access_token"]


client = anthropic.Anthropic(
    credentials=WorkloadIdentityCredentials(
        identity_token_provider=fetch_okta_token,
        federation_rule_id=os.environ["ANTHROPIC_FEDERATION_RULE_ID"],
        organization_id=os.environ["ANTHROPIC_ORGANIZATION_ID"],
        service_account_id=os.environ["ANTHROPIC_SERVICE_ACCOUNT_ID"],
        workspace_id=os.environ.get("ANTHROPIC_WORKSPACE_ID"),
    ),
)

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(next(block.text for block in message.content if block.type == "text"))
```

In the SDK, pass your Okta token to `identity_token_provider`. Where that option takes a token provider, the SDK calls the provider each time the Anthropic access token approaches expiry. The provider should return a fresh token on each call rather than caching one indefinitely. The `ant` CLI rereads `ANTHROPIC_IDENTITY_TOKEN_FILE` on each exchange, so refresh that file on a timer for long-running shells.

## Verify the setup

A successful exchange returns an `access_token` starting with `sk-ant-oat01-` and an `expires_in` value in seconds. If the exchange fails with the opaque `401` `authentication_error` response (message `Authentication failed`), check the [authentication history page](https://platform.claude.com/settings/workload-identity-federation?tab=history) in the Claude Console for the deny reason. Then see [Troubleshoot a failed exchange](manage-claude-wif-reference.md#troubleshoot-a-failed-exchange). The most common Okta-side cause is an `issuer_url` mismatch. The `issuer_url` must include the `/oauth2/<auth-server-id>` path, and the Okta org authorization server is not usable.

## Scope your rule



Multiple service apps under the same Okta authorization server share the same issuer. A rule that omits `subject_prefix` matches every service app on that server, so any team that can register one could obtain a federated Anthropic token.

Lock the rule’s `match` block to the narrowest scope that fits your use case:

- **Pin the exact Client ID:** Set `subject_prefix` to the service app’s full Client ID with no trailing `*`.
- **Pin the audience:** Match the `audience` value you configured on the authorization server so Anthropic rejects tokens issued for a different audience.
- **Match on custom claims:** For finer-grained scoping, add claims in the authorization server’s **Claims** tab and match them with the rule’s `claims` map or a CEL `condition`.
- **Use one rule for each service app:** Create a separate federation rule for each service app rather than sharing one rule across apps.

## Next steps

- Review the [WIF reference](manage-claude-wif-reference.md) for the full credential resolution order and profile configuration.
- See [Rule matching semantics](manage-claude-wif-reference.md#rule-matching-semantics) to match on custom Okta claims with CEL expressions.
