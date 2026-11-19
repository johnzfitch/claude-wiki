---
title: "Manage WIF with the Admin API - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/wif-admin-api"
category: "04-API-Reference/Other"
fetched_at: "2026-11-13T06:35:06Z"
tags: ["api", "authentication"]
---

# Manage WIF with the Admin API

Copy page



Create and manage Workload Identity Federation service accounts, issuers, and rules programmatically for infrastructure-as-code and CI workflows.

Copy page



The Admin API lets you create and manage [Workload Identity Federation](manage-claude-workload-identity-federation.md) (WIF) resources programmatically: service accounts, federation issuers, and federation rules. Use it to keep your federation configuration in infrastructure as code, provision it from CI, and reproduce it across organizations instead of clicking through the Claude Console. These endpoints share the `/v1/organizations` path prefix with the rest of the [Admin API](manage-claude-admin-api.md).

## Prerequisites

Every request on this page authenticates with an OAuth bearer token that carries the `org:admin` scope. Anthropic grants the scope only to organization members with the admin, owner, or primary owner role. The scope grants access to the whole organization, and these endpoints ignore any workspace binding. There are two ways to obtain a token, and they carry different permissions. A token from your own login acts as a user. A federated token acts as a service account and cannot perform every operation on this page.

### Interactive (your terminal)

In a shell you reserve for administration, log in with the [`ant` CLI](cli-sdks-libraries-cli-quickstart.md) under a dedicated profile, requesting the `org:admin` scope (see [Admin access](cli-sdks-libraries-cli-authentication.md#admin-access)), then export the bearer token:

CLI



```python
ant auth login --profile admin --scope "org:admin"
export ANTHROPIC_AUTH_TOKEN=$(ant auth print-credentials --profile admin --access-token)
```

Logging in with `--profile admin` stores the `org:admin` credential under its own profile name and also makes it the CLI’s active profile. The exported variable applies to every SDK and CLI call in that shell. When you are done, unset the variable and switch the CLI back with `ant profile activate default`.

Interactive tokens are short-lived. If requests start returning 401, rerun the `export` command to refresh the token.

The SDK and the `ant` CLI read `ANTHROPIC_AUTH_TOKEN` automatically. Leave `ANTHROPIC_API_KEY` unset in the same shell. When both are set, the SDK and the CLI use the key, and these endpoints reject API keys.

### Workload (CI and automation)

Create a federation rule with `oauth_scope: org:admin` that targets a service account whose `organization_role` is `admin`. You must create the rule itself in the Claude Console. Granting a workload organization-admin access is a deliberate human action, not something automation can bootstrap for itself. The next section walks through this setup, which you do once for each organization.

## Bootstrap a workload to manage WIF

One Console-created rule is enough to put the rest of your federation configuration under infrastructure as code. Grant a single trusted workload the `org:admin` scope, and let that workload manage federation issuers and every workspace-scoped federation rule through this API.

1.  1

    ### Create the org:admin rule in the Console

    In the Claude Console, go to the [Workload identity](https://platform.claude.com/settings/workload-identity-federation) page (`platform.claude.com/settings/workload-identity-federation`) and select **Connect workload**. Create one federation rule for your automation workload, for example a GitHub Actions workflow in your infrastructure repository. Under **Advanced rule options**, set the rule’s OAuth scope to `org:admin`. The wizard then creates the new service account with the Admin organization role, or asks you to pick an existing admin service account as the target.

    
    Match the rule to one exact workload identity, not a broad pattern. `subject_prefix` is an exact match unless it ends in `*`. For GitHub Actions, pin the subject to a protected branch, such as `repo:my-org/my-repo:ref:refs/heads/main`. A trailing wildcard such as `repo:my-org/my-repo:*` also matches `pull_request` runs, including runs triggered from forks. With that pattern, anyone who can open a pull request against the repository can mint an `org:admin` token. See [Restrict which workflows can authenticate](manage-claude-wif-providers-github-actions.md#restrict-which-workflows-can-authenticate).

2.  2

    ### Exchange the workload’s identity token

    A workload that uses the SDK or the `ant` CLI does not perform the exchange itself. The client exchanges the identity token on the first request. Before the resulting access token expires, it reads the identity token again and repeats the exchange. Construct the client with no arguments, exactly as for inference in [Construct the SDK client](manage-claude-workload-identity-federation.md#construct-the-sdk-client), and point it at the rule with the federation environment variables:

    ``` shiki
    export ANTHROPIC_FEDERATION_RULE_ID=fdrl_...        # the org:admin rule from step 1
    export ANTHROPIC_ORGANIZATION_ID=00000000-0000-0000-0000-000000000000
    export ANTHROPIC_SERVICE_ACCOUNT_ID=svac_...       # the rule's target service account
    export ANTHROPIC_IDENTITY_TOKEN_FILE=/path/to/jwt  # or ANTHROPIC_IDENTITY_TOKEN
    # ANTHROPIC_WORKSPACE_ID is required only if the rule is enabled for all
    # workspaces or more than one; the org:admin endpoints ignore the binding.
    unset ANTHROPIC_API_KEY ANTHROPIC_AUTH_TOKEN       # both take precedence over federation
    ```

    

    The SDK also accepts these settings as explicit constructor arguments, shown in [Construct the SDK client](manage-claude-workload-identity-federation.md#construct-the-sdk-client). The `ant` CLI reads these variables too, or takes `--federation-rule`, `--organization-id`, `--service-account-id`, and `--identity-token-file` flags. See [Environment variables](manage-claude-wif-reference.md#environment-variables) and [Credential precedence](manage-claude-wif-reference.md#credential-precedence) for the full list of variables and their order.

    For a workload that runs more than one `ant` command, use a [federation profile](manage-claude-wif-reference.md#profile-configuration-file) rather than flags or environment variables. A profile caches the access token between commands. With flags or variables, every command exchanges the identity token again. By default, Anthropic accepts an identity token with a `jti` claim only once, and GitHub Actions tokens carry that claim. Anthropic rejects a second command that presents the same token.

    When the rule is enabled for all workspaces or more than one, give the `ant` CLI a federation profile that sets `workspace_id`, and set `ANTHROPIC_PROFILE` to its name. Unlike the SDK, the CLI passes `ANTHROPIC_WORKSPACE_ID` into the exchange only through a federation profile, and `--workspace-id` never reaches the exchange.

    A workload that calls the API with curl exchanges the JWT for a short-lived `org:admin` bearer token itself. It uses the same [token exchange](manage-claude-workload-identity-federation.md#authenticate-from-your-workload) as any other federated workload, and sends the token in the `authorization: Bearer` header.

3.  3

    ### Manage issuers and workspace-scoped rules through the API

    With the client configured (or, for curl, the minted token in `ANTHROPIC_AUTH_TOKEN`), the workload creates and manages your federation configuration using the endpoints on this page.

For the operations a federated token can and cannot perform, see [Permissions and constraints](#permissions-and-constraints). If you already created issuers, service accounts, or rules with the **Connect workload** wizard, list them with the following endpoints. Then import them into your infrastructure-as-code state instead of recreating them.

## Authentication

All endpoints live under `https://api.anthropic.com/v1/organizations/`. Every request to the federation and service-account endpoints needs the API version header and the bearer token.

In the SDK, these endpoints are `client.organization.service_accounts`, `client.organization.federation.issuers`, and `client.organization.federation.rules` (`ant organization:service-accounts`, `ant organization:federation:issuers`, and `ant organization:federation:rules` in the CLI). The SDK and the `ant` CLI send the bearer token from `ANTHROPIC_AUTH_TOKEN`. In an automated workload, they perform the federation exchange themselves, as described in [Bootstrap a workload to manage WIF](#bootstrap-a-workload-to-manage-wif).

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
client = anthropic.Anthropic()

service_accounts = client.organization.service_accounts.list()

for service_account in service_accounts:
    print(f"{service_account.id}: {service_account.name}")
```

These endpoints do not accept Admin API keys, so the `x-api-key` examples on the [Admin API](manage-claude-admin-api.md) page do not apply here.

## Service accounts

A [service account](manage-claude-workload-identity-federation.md#service-accounts) (`svac_...`) is the non-human identity that a federated token acts as. Set `organization_role` to `developer`.

Create a service account:

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
client = anthropic.Anthropic()

service_account = client.organization.service_accounts.create(
    name="inference-worker", organization_role="developer"
)

print(f"id: {service_account.id}")
print(f"name: {service_account.name}")
```

List service accounts:

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
client = anthropic.Anthropic()

service_accounts = client.organization.service_accounts.list(limit=20)

for service_account in service_accounts:
    print(f"{service_account.id}: {service_account.name}")
```

Archive a service account:

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
client = anthropic.Anthropic()

service_account = client.organization.service_accounts.archive(
    "svac_01ABCDEFabcdef0123456789XY"
)

print(f"id: {service_account.id}")
print(f"archived_at: {service_account.archived_at}")
```

The create endpoint returns the new service account:

```python
{
  "id": "svac_...",
  "name": "inference-worker",
  "organization_role": "developer",
  "created_at": "...",
  "type": "service_account",
  "...": "..."
}
```



To read or update a single service account, use `GET` and `POST` on `/v1/organizations/service_accounts/{service_account_id}`. A service account must be a member of a workspace before federated tokens can act in it. Every service account has an implicit membership in your organization’s default workspace. Manage explicit memberships in other workspaces with `GET`, `POST`, and `DELETE` on `/v1/organizations/service_accounts/{service_account_id}/workspaces`, where `DELETE` targets `.../workspaces/{workspace_id}`.

For complete parameter details and response schemas, see the [Service accounts API reference](../Endpoints/organization-service-accounts.md).

## Federation issuers

A [federation issuer](manage-claude-workload-identity-federation.md#federation-issuers) (`fdis_...`) registers an OIDC identity provider with your organization. The `jwks` field is a discriminated union that controls how Anthropic fetches the provider’s signing keys:

| `jwks` value | When to use |
|----|----|
| `{"type": "discovery"}` | The provider serves `/.well-known/openid-configuration` at the issuer URL. |
| `{"type": "explicit_url", "url": "..."}` | Point at a JWKS endpoint directly. |
| `{"type": "inline", "keys": [...]}` | Upload the key set for providers that are not reachable from the public internet. |

Register an issuer. This example registers GitHub Actions with JWKS discovery:

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
client = anthropic.Anthropic()

issuer = client.organization.federation.issuers.create(
    name="github-actions",
    issuer_url="https://token.actions.githubusercontent.com",
    jwks={"type": "discovery"},
)

print(f"id: {issuer.id}")
print(f"name: {issuer.name}")
print(f"issuer_url: {issuer.issuer_url}")
```

List issuers:

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
client = anthropic.Anthropic()

issuers = client.organization.federation.issuers.list(limit=20)

for issuer in issuers:
    print(f"{issuer.id}: {issuer.name}")
```

Archive an issuer:

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
client = anthropic.Anthropic()

issuer = client.organization.federation.issuers.archive(
    "fdis_01ABCDEFabcdef0123456789XY"
)

print(f"id: {issuer.id}")
print(f"archived_at: {issuer.archived_at}")
```

To read or update a single issuer, use `GET` and `POST` on `/v1/organizations/federation_issuers/{issuer_id}`. An OAuth caller cannot update an issuer that backs a rule whose `oauth_scope` is anything other than `workspace:developer` or `workspace:inference`. See [Permissions and constraints](#permissions-and-constraints).

For complete parameter details and response schemas, see the [Federation issuers API reference](../Endpoints/organization-federation-issuers.md).

## Federation rules

A [federation rule](manage-claude-workload-identity-federation.md#federation-rules) (`fdrl_...`) binds an issuer to a service account. JWTs from the issuer that satisfy the rule’s match conditions can mint tokens that act as the rule’s target. The `workspace_id` in the create request enables the rule in that workspace at creation. Add more workspaces later through the `/federation_rules/{rule_id}/workspaces` subresource. Create requests require either `workspace_id` or `applies_to_all_workspaces: true`.

Create a rule. This example lets GitHub Actions deploys from the main branch act as the service account:

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
client = anthropic.Anthropic()

rule = client.organization.federation.rules.create(
    name="gha-deploy",
    issuer_id="fdis_01ABCDEFabcdef0123456789XY",
    match={
        "subject_prefix": "repo:my-org/my-repo:ref:refs/heads/main",
        "claims": {"repository_owner": "my-org"},
    },
    target={
        "type": "service_account",
        "service_account_id": "svac_01ABCDEFabcdef0123456789XY",
    },
    workspace_id="wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
    oauth_scope="workspace:developer",
    token_lifetime_seconds=600,
)

print(f"id: {rule.id}")
print(f"name: {rule.name}")
```

List rules, optionally filtered by issuer:

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
client = anthropic.Anthropic()

rules = client.organization.federation.rules.list(
    issuer_id="fdis_01ABCDEFabcdef0123456789XY"
)

for rule in rules:
    print(f"{rule.id}: {rule.name}")
```

Archive a rule:

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
client = anthropic.Anthropic()

rule = client.organization.federation.rules.archive("fdrl_01ABCDEFabcdef0123456789XY")

print(f"id: {rule.id}")
print(f"archived_at: {rule.archived_at}")
```

The list endpoint returns a page of rules and the cursor for the next page:

```python
{
  "data": [{ "id": "fdrl_...", "name": "gha-deploy", "...": "..." }],
  "next_page": "..."
}
```



To read or update a single rule, use `GET` and `POST` on `/v1/organizations/federation_rules/{rule_id}`. To manage the workspaces a rule can mint tokens in, use `GET` and `POST` on `/v1/organizations/federation_rules/{rule_id}/workspaces`, and `DELETE` on `/v1/organizations/federation_rules/{rule_id}/workspaces/{workspace_id}`.

For complete parameter details and response schemas, see the [Federation rules API reference](../Endpoints/organization-federation-rules.md).

## Permissions and constraints



- OAuth-authenticated callers can only create or modify rules whose `oauth_scope` is `workspace:developer` or `workspace:inference`. To create or modify a rule with any other scope (such as `org:admin` or `workspace:manage_tunnels`), use the Console.
- An OAuth caller cannot update a federation issuer that backs a rule whose `oauth_scope` is anything other than `workspace:developer` or `workspace:inference` (such as `org:admin` or `workspace:manage_tunnels`). Consider registering a dedicated issuer for the bootstrap rule so the issuers behind workspace-scoped rules stay updatable through the API.
- These endpoints do not accept Admin API keys, for reads or writes. Use an `org:admin` OAuth token.
- A federated token cannot set `organization_role` to `admin` on a new or existing service account, even one that is already `admin`. To set that role, use an [interactive token](#interactive-your-terminal) or the Console.

A rule with `oauth_scope: org:admin` must target a service account whose `organization_role` is `admin`. Resource names must match `^[a-z0-9-]+$`, be 1 to 255 characters, and be unique within an organization for each resource type. For the full field-level constraints, see [Validation rules](manage-claude-wif-reference.md#validation-rules).

## Pagination and archiving

The service-account, federation-issuer, and federation-rule list endpoints accept `limit` (the page size, 1 to 100, default 20) and a `page` cursor taken from the previous response. Pass the response’s `next_page` value as the `page` query parameter on the next request. The SDK fetches further pages on demand when you iterate with `for`, and the `ant` CLI does so by default. The rule-workspaces subresource list returns the full set without pagination. Lists hide archived resources by default. Pass `include_archived=true` to include them.

Archiving is a soft delete. It is idempotent, so archiving an already-archived resource succeeds. Archiving an issuer or a service account returns `400` while a live federation rule references it. Archive the rule first.

## See also

- [Workload Identity Federation](manage-claude-workload-identity-federation.md): concepts and the Console setup walkthrough
- [WIF reference](manage-claude-wif-reference.md): environment variables, validation rules, OAuth scopes, and error codes
- [Admin API](manage-claude-admin-api.md): the rest of the organization management surface
- [Admin API reference](../Endpoints/organization.md): generated request and response schemas for the service account and federation endpoints
