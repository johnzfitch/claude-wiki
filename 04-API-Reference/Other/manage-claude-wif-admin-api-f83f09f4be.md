---
title: "Manage WIF with the Admin API - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/wif-admin-api"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:37Z"
tags: ["api", "authentication"]
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fwif-admin-api)





SearchCtrlK

Organization

[Admin API](/docs/en/manage-claude/admin-api)[User management](/docs/en/manage-claude/user-management)[Workspaces](/docs/en/manage-claude/workspaces)

Authentication

[Overview](/docs/en/manage-claude/authentication)[Create an Admin API key](/docs/en/manage-claude/admin-api-keys)[App Attest](/docs/en/manage-claude/app-attest)[Workload Identity Federation](/docs/en/manage-claude/workload-identity-federation)[Manage WIF via API](/docs/en/manage-claude/wif-admin-api)[WIF reference](/docs/en/manage-claude/wif-reference)

Identity providers

Monitoring

[Usage and Cost API](/docs/en/manage-claude/usage-cost-api)[Rate Limits API](/docs/en/manage-claude/rate-limits-api)[Analytics APIs](/docs/en/manage-claude/analytics-api)[Claude Code Analytics API](/docs/en/manage-claude/claude-code-analytics-api)[Spend Limits API](/docs/en/manage-claude/spend-limits-api)

Data & compliance

[Data residency](/docs/en/manage-claude/data-residency)[API and data retention](/docs/en/manage-claude/api-and-data-retention)[Access Transparency](/docs/en/manage-claude/access-transparency)

[Encryption keys](/docs/en/manage-claude/cmek)

[Inference hooks](/docs/en/manage-claude/inference-hooks)

Compliance API

[Overview](/docs/en/manage-claude/compliance-api)[Set up the Compliance API](/docs/en/manage-claude/compliance-api-access)[Activity Feed](/docs/en/manage-claude/compliance-activity-feed)[Chats, files, and projects](/docs/en/manage-claude/compliance-content-data)[Session transcripts](/docs/en/manage-claude/compliance-sessions)[Organizations, users, roles, groups, and settings](/docs/en/manage-claude/compliance-org-data)[Design your integration](/docs/en/manage-claude/compliance-integration-patterns)[Errors](/docs/en/manage-claude/compliance-errors)[FAQ](/docs/en/manage-claude/compliance-faq)

[Console](/)

[Admin](/docs/en/manage-claude/admin-api)Authentication

# Manage WIF with the Admin API

Copy page



Create and manage Workload Identity Federation service accounts, issuers, and rules programmatically for infrastructure-as-code and CI workflows.

Copy page



The Admin API lets you create and manage [Workload Identity Federation](/docs/en/manage-claude/workload-identity-federation) resources programmatically: service accounts, federation issuers, and federation rules. Use it to keep your federation configuration in infrastructure as code, provision it from CI, and reproduce it across organizations instead of clicking through the Claude Console. These endpoints share the `/v1/organizations` path prefix with the rest of the [Admin API](/docs/en/manage-claude/admin-api).

## Prerequisites

Every request on this page authenticates with an OAuth bearer token that carries the `org:admin` scope. The scope is granted only to organization members with the admin, owner, or primary owner role, and it grants access to the whole organization: any workspace binding is ignored. There are two ways to obtain a token, and they carry different permissions: a token from your own login acts as a user, whereas a federated token acts as a service account and cannot perform every operation on this page.

### Interactive (your terminal)

Log in with the [`ant` CLI](/docs/en/cli-sdks-libraries/cli/quickstart) under a dedicated profile, requesting the `org:admin` scope (see [Admin access](/docs/en/cli-sdks-libraries/cli/authentication#admin-access)), then export the bearer token. Logging in with `--profile admin` stores the `org:admin` credential under its own profile name and also makes it the CLI's active profile, and the exported variable applies to every SDK and CLI call in that shell; so use a shell you reserve for administration, unset the variable when you are done, and switch the CLI back with `ant profile activate default`:

CLI



```python
ant auth login --profile admin --scope "org:admin"
export ANTHROPIC_AUTH_TOKEN=$(ant auth print-credentials --profile admin --access-token)
```

Interactive tokens are short-lived; if requests start returning 401, re-run the export command (it refreshes the token automatically).

The SDKs and the `ant` CLI read `ANTHROPIC_AUTH_TOKEN` automatically; leave `ANTHROPIC_API_KEY` unset in the same shell, because these endpoints reject API keys and some clients prefer the key when both are set.

### Workload (CI and automation)

Create a federation rule with `oauth_scope: org:admin` that targets a service account whose `organization_role` is `admin`. The rule itself must be created in the Claude Console: granting a workload organization-admin access is a deliberate human action, not something automation can bootstrap for itself. The next section walks through this once-per-organization setup.

## Bootstrap a workload to manage WIF

One Console-created rule is enough to put the rest of your federation configuration under infrastructure as code: grant a single trusted workload the `org:admin` scope, and let that workload manage federation issuers and every workspace-scoped federation rule through this API.

1.  1

    ### Create the org:admin rule in the Console

    In the Claude Console, go to **Settings → Workload identity** and select **Connect workload** to create one federation rule for your automation workload, for example a GitHub Actions workflow in your infrastructure repository. Under **Advanced rule options**, set the rule's OAuth scope to `org:admin`: the wizard then creates the new service account with the Admin organization role (or asks you to pick an existing admin service account as the target).

    
    Match the rule to one exact workload identity, not a broad pattern. `subject_prefix` is an exact match unless it ends in `*`. For GitHub Actions, pin the subject to a protected branch, such as `repo:my-org/my-repo:ref:refs/heads/main`. A trailing wildcard such as `repo:my-org/my-repo:*` also matches `pull_request` runs, including runs triggered from forks, so anyone who could open a pull request against the repository could mint an `org:admin` token. See [Restrict which workflows can authenticate](/docs/en/manage-claude/wif-providers/github-actions#restrict-which-workflows-can-authenticate).

2.  2

    ### Exchange the workload's identity token

    A workload that uses one of the SDKs or the `ant` CLI does not perform the exchange itself. Point the client at the rule with the federation environment variables and construct it with no arguments, exactly as for inference in [Construct the SDK client](/docs/en/manage-claude/workload-identity-federation#construct-the-sdk-client); the client exchanges the identity token on the first request and, before the resulting access token expires, re-reads the identity token and exchanges it again:

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

    The `ant` CLI reads the same variables, or takes `--federation-rule`, `--organization-id`, `--service-account-id`, and `--identity-token-file` flags. For a workload that runs more than one `ant` command, use a [federation profile](/docs/en/manage-claude/wif-reference#profile-configuration-file) rather than flags or environment variables: with flags or variables the CLI exchanges the identity token again in every process, and identity tokens that carry a `jti` claim (GitHub Actions tokens do) are accepted only once, so a second command would be rejected; a profile is also the only way to give the CLI a `workspace_id` for the exchange when the rule is enabled for all workspaces or more than one, because unlike the SDKs the CLI does not pass `ANTHROPIC_WORKSPACE_ID` or `--workspace-id` into the exchange. Every SDK also accepts the same settings as explicit constructor arguments, shown per language in [Construct the SDK client](/docs/en/manage-claude/workload-identity-federation#construct-the-sdk-client). See [Environment variables](/docs/en/manage-claude/wif-reference#environment-variables) and [Credential precedence](/docs/en/manage-claude/wif-reference#credential-precedence) for the full list and ordering.

    A workload that calls the API with curl exchanges the JWT for a short-lived `org:admin` bearer token itself, using the same [token exchange](/docs/en/manage-claude/workload-identity-federation#authenticate-from-your-workload) as any other federated workload, and sends it in the `authorization: Bearer` header.

3.  3

    ### Manage issuers and workspace-scoped rules through the API

    With the client configured (or, for curl, the minted token in `ANTHROPIC_AUTH_TOKEN`), the workload creates and manages your federation configuration using the endpoints on this page.

For the operations a workload-minted token can and cannot perform, see [Permissions and constraints](#permissions-and-constraints). If you already created issuers, service accounts, or rules with the **Connect workload** wizard, list them with the following endpoints and import them into your infrastructure-as-code state instead of recreating them.

## Authentication

All endpoints live under `https://api.anthropic.com/v1/organizations/`. Every request to the federation and service-account endpoints needs the API version header and the bearer token:

In the SDKs these endpoints are `client.beta.organization.service_accounts`, `client.beta.organization.federation.issuers`, and `client.beta.organization.federation.rules` (`ant beta:organization:service-accounts`, `federation:issuers`, and `federation:rules` in the CLI). The SDK and CLI examples construct the default client, which sends the bearer token from `ANTHROPIC_AUTH_TOKEN`, or, in an automated workload, performs the federation exchange itself as described in [Bootstrap a workload to manage WIF](#bootstrap-a-workload-to-manage-wif). SDK list methods fetch further pages on demand, so `limit` sets the page size; the PHP and Ruby examples read one page.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

service_accounts = client.beta.organization.service_accounts.list()

for service_account in service_accounts:
    print(f"{service_account.id}: {service_account.name}")
```

Admin API keys are not accepted on these endpoints; the Admin API page's `x-api-key` examples do not apply here.

## Service accounts

A [service account](/docs/en/manage-claude/workload-identity-federation#service-accounts) (`svac_...`) is the non-human identity that a federated token acts as. Set `organization_role` to `developer`.

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



```python
client = anthropic.Anthropic()

service_account = client.beta.organization.service_accounts.create(
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



```python
client = anthropic.Anthropic()

service_accounts = client.beta.organization.service_accounts.list(limit=20)

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



```python
client = anthropic.Anthropic()

service_account = client.beta.organization.service_accounts.archive(
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

To read or update a single service account, use `GET` and `POST` on `/v1/organizations/service_accounts/{service_account_id}`. A service account must be a member of a workspace before federated tokens can act in it. Every service account has an implicit membership in your organization's default workspace; add explicit memberships for other workspaces with `GET`, `POST`, and `DELETE` on `/v1/organizations/service_accounts/{service_account_id}/workspaces`, where `DELETE` targets `.../workspaces/{workspace_id}`.

For complete parameter details and response schemas, see the [Service accounts API reference](/docs/en/api/beta/organization/service_accounts).

## Federation issuers

A [federation issuer](/docs/en/manage-claude/workload-identity-federation#federation-issuers) (`fdis_...`) registers an OIDC identity provider with your organization. The `jwks` field is a discriminated union that controls how Anthropic fetches the provider's signing keys:

| `jwks` value                             | When to use                                                                       |
|------------------------------------------|-----------------------------------------------------------------------------------|
| `{"type": "discovery"}`                  | The provider serves `/.well-known/openid-configuration` at the issuer URL.        |
| `{"type": "explicit_url", "url": "..."}` | Point at a JWKS endpoint directly.                                                |
| `{"type": "inline", "keys": [...]}`      | Upload the key set for providers that are not reachable from the public internet. |

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



```python
client = anthropic.Anthropic()

issuer = client.beta.organization.federation.issuers.create(
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



```python
client = anthropic.Anthropic()

issuers = client.beta.organization.federation.issuers.list(limit=20)

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



```python
client = anthropic.Anthropic()

issuer = client.beta.organization.federation.issuers.archive(
    "fdis_01ABCDEFabcdef0123456789XY"
)

print(f"id: {issuer.id}")
print(f"archived_at: {issuer.archived_at}")
```

To read or update a single issuer, use `GET` and `POST` on `/v1/organizations/federation_issuers/{issuer_id}`. An OAuth caller cannot update an issuer that backs a rule whose `oauth_scope` is anything other than `workspace:developer` or `workspace:inference`; see [Permissions and constraints](#permissions-and-constraints).

For complete parameter details and response schemas, see the [Federation issuers API reference](/docs/en/api/beta/organization/federation/issuers).

## Federation rules

A [federation rule](/docs/en/manage-claude/workload-identity-federation#federation-rules) (`fdrl_...`) binds an issuer to a service account: JWTs from the issuer that satisfy the rule's match conditions can mint tokens that act as the rule's target. The `workspace_id` in the create request enables the rule in that workspace at creation; add more workspaces later through the `/federation_rules/{rule_id}/workspaces` sub-resource. Either `workspace_id` or `applies_to_all_workspaces: true` is required on create.

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



```python
client = anthropic.Anthropic()

rule = client.beta.organization.federation.rules.create(
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



```python
client = anthropic.Anthropic()

rules = client.beta.organization.federation.rules.list(
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



```python
client = anthropic.Anthropic()

rule = client.beta.organization.federation.rules.archive(
    "fdrl_01ABCDEFabcdef0123456789XY"
)

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

For complete parameter details and response schemas, see the [Federation rules API reference](/docs/en/api/beta/organization/federation/rules).

## Permissions and constraints



- OAuth-authenticated callers can only create or modify rules whose `oauth_scope` is `workspace:developer` or `workspace:inference`. To create or modify a rule with any other scope (such as `org:admin` or `workspace:manage_tunnels`), use the Console.
- An OAuth caller cannot update a federation issuer that backs a rule whose `oauth_scope` is anything other than `workspace:developer` or `workspace:inference` (such as `org:admin` or `workspace:manage_tunnels`). Consider registering a dedicated issuer for the bootstrap rule so the issuers behind workspace-scoped rules stay updatable through the API.
- Admin API keys are not accepted on these endpoints, for reads or writes; use an `org:admin` OAuth token.

A rule with `oauth_scope: org:admin` must target a service account whose `organization_role` is `admin`. Resource names must match `^[a-z0-9-]+$`, be 1 to 255 characters, and be unique within an organization for each resource type; for the full field-level constraints, see [Validation rules](/docs/en/manage-claude/wif-reference#validation-rules).

## Pagination and archiving

The service-account, federation-issuer, and federation-rule list endpoints accept `limit` (1 to 100, default 20) and a `page` cursor taken from the previous response. Pass the response's `next_page` value as the `page` query parameter on the next request. The rule-workspaces sub-resource list returns the full set without pagination. Archived resources are hidden from lists by default; pass `include_archived=true` to include them.

Archiving is a soft delete and is idempotent: archiving an already-archived resource succeeds. Archiving an issuer or a service account returns `400` while a live federation rule still references it; archive the rule first.

## See also

- [Workload Identity Federation](/docs/en/manage-claude/workload-identity-federation): concepts and the Console setup walkthrough
- [WIF reference](/docs/en/manage-claude/wif-reference): environment variables, validation rules, OAuth scopes, and error codes
- [Admin API](/docs/en/manage-claude/admin-api): the rest of the organization management surface
- [Admin API reference](/docs/en/api/beta/organization): generated request and response schemas for every Admin API endpoint
