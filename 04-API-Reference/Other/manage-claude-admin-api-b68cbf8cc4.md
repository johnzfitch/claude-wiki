---
title: "Admin API - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/admin-api"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:32Z"
tags: ["api", "authentication", "claude-code"]
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fadmin-api)

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

AdminOrganization

# Admin API

Copy page



Manage organization members, workspaces, invites, and API keys programmatically with the Admin API, using an Admin API key, an `org:admin` OAuth token, or a personal or service account key.

Copy page





**The Admin API is unavailable for individual accounts.** To collaborate with teammates and add members, set up your organization in **Console → Settings → Organization**.

The [Admin API](/docs/en/api/beta/organization) lets you manage your organization's members, workspaces, invites, and API keys programmatically instead of by hand in the [Claude Console](/).



**The Admin API requires special access**

The Admin API accepts three credentials:

- An **Admin API key** (starting with `sk-ant-admin...`) sent in the `x-api-key` header. Only organization members with the admin role can provision one. See [Create an Admin API key](/docs/en/manage-claude/admin-api-keys).
- An **OAuth bearer token** with the `org:admin` scope sent in the `authorization: Bearer` header. Only members with the admin, owner, or primary owner role can obtain one. See [Obtain an OAuth bearer token](#oauth-bearer-token).
- A **personal key** or **service account key** that isn't scoped to a specific workspace, sent in the `x-api-key` header. The key has the same permissions as the linked account. See [Key types](/docs/en/manage-claude/authentication#key-types).



**Claude Enterprise:** Claude Enterprise (claude.ai) organizations call the Admin API with a scoped API key created in claude.ai. From this page, only the members and invites endpoints apply to them. They also get Enterprise-only endpoints: group and custom-role reads, and [spend limits](/docs/en/manage-claude/spend-limits-api). See [User management](/docs/en/manage-claude/user-management).



**Claude Platform on AWS:** Only the workspace endpoints (create, get, list, update, and archive on `/v1/organizations/workspaces`) and the external key endpoints (register, get, list, update, and delete on `/v1/organizations/external_keys`, for [CMEK](/docs/en/manage-claude/cmek-aws-kms#claude-platform-on-aws); there is no validate endpoint, because keys are validated when attached to a workspace) are available on Claude Platform on AWS. Organization members, workspace members, invites, API keys, and the usage, cost, and rate limit reports aren't. See [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws).

## Authentication

Authenticate with any of the three credentials. An Admin API key covers most endpoints. The service-account, federation-issuer, and federation-rule endpoints accept only an `org:admin` OAuth token. Send a personal key or service account key in the `x-api-key` header, as you would an Admin API key. The following examples call the [organization info endpoint](#accessing-organization-info) with an OAuth token and with an Admin API key.

The Python, TypeScript, C#, Go, Java, PHP, and Ruby SDKs expose the Admin API under `client.beta.organization`, and the `ant` CLI under `ant beta:organization`. The examples on this page use the default client, which reads an Admin API key from `ANTHROPIC_API_KEY` or an OAuth bearer token from `ANTHROPIC_AUTH_TOKEN`. SDK list methods in Python, TypeScript, C#, Go, and Java return an iterator that fetches more pages on demand, so `limit` sets the page size, not the total. The PHP, Ruby, and curl examples return one page. In the CLI, `--limit` caps the results on the member, invite, workspace, workspace-member, and API-key lists. For each endpoint's parameters and responses, see the [Admin API reference](/docs/en/api/beta/organization).

### OAuth bearer token

Log in with the [`ant` CLI](/docs/en/cli-sdks-libraries/cli/quickstart) under a dedicated profile with the `org:admin` scope (see [Admin access](/docs/en/cli-sdks-libraries/cli/authentication#admin-access)), then export the bearer token. `--profile admin` stores the `org:admin` credential under its own profile and makes it the CLI's active profile. The exported variable applies to every SDK and CLI call in that shell. Use a shell you reserve for administration, unset the variable when you're done, and switch the CLI back with `ant profile activate default`:

CLI



```python
ant auth login --profile admin --scope "org:admin"
export ANTHROPIC_AUTH_TOKEN=$(ant auth print-credentials --profile admin --access-token)
```

Interactive tokens are short-lived. If requests start returning 401, re-run the `export` command to refresh the token.

The SDKs and the `ant` CLI read `ANTHROPIC_AUTH_TOKEN` automatically. Leave `ANTHROPIC_API_KEY` unset in the same shell so they send the bearer token. Automated workloads skip the login: they authenticate through workload identity federation, and the SDKs and CLI perform the token exchange from the federation environment variables. See [Bootstrap a workload to manage WIF](/docs/en/manage-claude/wif-admin-api#bootstrap-a-workload-to-manage-wif).

Call the Admin API with the exported token:

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

organization = client.beta.organization.retrieve()

print(f"id: {organization.id}")
print(f"name: {organization.name}")
```

An `org:admin` token grants access to the whole organization, regardless of the workspace the underlying profile or [federation rule](#federation-rules) is bound to.

For CI and other non-interactive workloads, mint the token with Workload Identity Federation instead of logging in interactively. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api#workload-ci-and-automation).

### Admin API key

To create an Admin API key for your organization type, see [Create an Admin API key](/docs/en/manage-claude/admin-api-keys).

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

organization = client.beta.organization.retrieve()

print(f"id: {organization.id}")
print(f"name: {organization.name}")
```

## How the Admin API works

Authenticate with any credential from [Authentication](#authentication), then manage the following resources:

- Organization members and their roles
- Organization invites
- Workspaces and their members
- API keys
- Service accounts, federation issuers, and federation rules (`org:admin` OAuth token only)

Common uses include automating onboarding and offboarding, managing workspace access, and auditing API keys.

## Organization roles and permissions

There are five organization-level roles. For details, see [API Console roles and permissions](https://support.claude.com/en/articles/10186004-api-console-roles-and-permissions).

| Role             | Permissions                                                                    |
|------------------|--------------------------------------------------------------------------------|
| user             | Can use playground                                                             |
| claude_code_user | Can use playground and [Claude Code](https://code.claude.com/docs/en/overview) |
| developer        | Can use playground and manage API keys                                         |
| billing          | Can use playground and manage billing details                                  |
| admin            | Can do all of the preceding, plus manage users                                 |

Organization owners and primary owners have all admin permissions and can also manage admins. All references to the admin role on this page also apply to owners and primary owners.

## Key concepts

### Organization members

List [organization members](/docs/en/api/beta/organization/users/retrieve), update their roles, and remove them.

List the members of your organization:

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

users = client.beta.organization.users.list(limit=10)

# Automatically fetches more pages as needed.
for user in users:
    print(f"{user.id}: {user.email} ({user.role})")
```

Update a member's role:

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

user = client.beta.organization.users.update(
    "user_01XyDMpzjS89pFZXqSFUBDr6", role="developer"
)

print(f"id: {user.id}")
print(f"role: {user.role}")
```

Remove a member from the organization:

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

removed_user = client.beta.organization.users.remove("user_01XyDMpzjS89pFZXqSFUBDr6")

print(f"id: {removed_user.id}")
```

### Organization invites

Invite users to your organization and manage pending [invites](/docs/en/api/beta/organization/invites/retrieve).

Invite a user to your organization:

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

invite = client.beta.organization.invites.create(
    email="user@example.com", role="developer"
)

print(f"id: {invite.id}")
print(f"email: {invite.email}")
print(f"status: {invite.status}")
print(f"expires_at: {invite.expires_at}")
```

List pending invites:

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

invites = client.beta.organization.invites.list(limit=10)

# Automatically fetches more pages as needed.
for invite in invites:
    print(f"{invite.id}: {invite.email} ({invite.status})")
```

Delete an invite:

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

deleted_invite = client.beta.organization.invites.delete(
    "invite_015gWxHNr6h6TdRPZTmuCGnn"
)

print(f"id: {deleted_invite.id}")
```

### Workspaces

See [Workspaces](/docs/en/manage-claude/workspaces) for Console and API examples.

### Workspace members

Manage [user access to specific workspaces](/docs/en/api/beta/organization/workspaces/members/retrieve):

Add a member to a workspace:

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

member = client.beta.organization.workspaces.members.add(
    "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
    user_id="user_01XyDMpzjS89pFZXqSFUBDr6",
    workspace_role="workspace_developer",
)

print(f"user_id: {member.user_id}")
print(f"workspace_role: {member.workspace_role}")
```

List the members of a workspace:

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

members = client.beta.organization.workspaces.members.list(
    "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ", limit=10
)

# Automatically fetches more pages as needed.
for member in members:
    print(f"{member.user_id}: {member.workspace_role}")
```

Update a workspace member's role:

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

member = client.beta.organization.workspaces.members.update(
    "user_01XyDMpzjS89pFZXqSFUBDr6",
    workspace_id="wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
    workspace_role="workspace_admin",
)

print(f"user_id: {member.user_id}")
print(f"workspace_role: {member.workspace_role}")
```

Remove a member from a workspace:

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

removed_member = client.beta.organization.workspaces.members.remove(
    "user_01XyDMpzjS89pFZXqSFUBDr6", workspace_id="wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
)

print(f"user_id: {removed_member.user_id}")
```

### API keys

Monitor and manage [API keys](/docs/en/api/beta/organization/api_keys/list). Each key in the response includes its `expires_at` timestamp (`null` for keys without an [expiration](/docs/en/manage-claude/authentication#key-expiration)) and `principal`, the identity it acts as (see [Key types](/docs/en/manage-claude/authentication#key-types)). For a personal key, `principal` is `{"type": "user_actor", "user_id": "user_..."}`; for a service account key, `{"type": "service_account_actor", "service_account_id": "svac_..."}`; and for a workspace key, `null`. Each key also has a `scope` object: `{"type": "workspace", "workspace_id": "wrkspc_..."}` for a key bound to one workspace, or `{"type": "organization"}` for a key that can work across any workspace the account has access to. The top-level `workspace_id` field is deprecated and is `null` both for keys bound to the Default Workspace and for keys without a workspace scope; use `scope` to tell them apart. Filtering the list by `workspace_id` with the Default Workspace's ID returns only keys bound to the Default Workspace; keys without a workspace scope aren't returned under any `workspace_id` filter.

List the active API keys in a workspace:

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

api_keys = client.beta.organization.api_keys.list(
    limit=10, status="active", workspace_id="wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
)

# Automatically fetches more pages as needed.
for api_key in api_keys:
    print(f"{api_key.id}: {api_key.name} ({api_key.status})")
```

Rename or deactivate an API key:

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

api_key = client.beta.organization.api_keys.update(
    "apikey_01Rj2N8SVvo6BePZj99NhmiT", status="inactive", name="New Key Name"
)

print(f"id: {api_key.id}")
print(f"name: {api_key.name}")
print(f"status: {api_key.status}")
```

### Service accounts

Create and manage service accounts (`svac_...`), the non-human identities that [service account keys](/docs/en/manage-claude/authentication#key-types) and [Workload Identity Federation](/docs/en/manage-claude/workload-identity-federation) tokens act as. These endpoints, like the federation-issuer and federation-rule endpoints, require an `org:admin` OAuth token. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api#service-accounts).

### Federation issuers

Register the OIDC identity providers (`fdis_...`) whose tokens may assert workload identity for your organization. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api#federation-issuers).

### Federation rules

Manage the rules (`fdrl_...`) that map issuer tokens to service accounts and scopes. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api#federation-rules).

## Accessing organization info

The `/v1/organizations/me` endpoint returns the organization that your credential belongs to:

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

organization = client.beta.organization.retrieve()

print(f"id: {organization.id}")
print(f"name: {organization.name}")
```

```python
{
  "id": "12345678-1234-5678-1234-567812345678",
  "type": "organization",
  "name": "Organization Name"
}
```



For parameter details and response schemas, see the [Organization Info API reference](/docs/en/api/beta/organization/retrieve).

## Usage and cost reports

Track your organization's usage and costs with the [Usage and Cost API](/docs/en/manage-claude/usage-cost-api).

## Claude Code analytics

Monitor developer productivity and Claude Code adoption with the [Claude Code Analytics API](/docs/en/manage-claude/claude-code-analytics-api).

## Rate limits

Read the rate limits configured for your organization and its workspaces with the [Rate Limits API](/docs/en/manage-claude/rate-limits-api).

## Compliance API

Retrieve audit and activity data for your organization with the [Compliance API](/docs/en/manage-claude/compliance-api). Admin API keys can read only the Activity Feed. For full access, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).

## Best practices

- Use meaningful names and descriptions for workspaces and API keys
- Handle errors from failed operations
- Regularly audit member roles and permissions
- Clean up unused workspaces and expired invites
- Monitor API key usage, audit each key's [`expires_at`](/docs/en/manage-claude/authentication#key-expiration), and rotate keys periodically

## FAQ

### What permissions are needed to use the Admin API?

The Admin API accepts an Admin API key (starting with `sk-ant-admin`), an OAuth bearer token with the `org:admin` scope, or a personal key or service account key that isn't scoped to a specific workspace. Only organization members with the admin role can provision Admin API keys, and only members with the admin, owner, or primary owner role can obtain `org:admin` tokens. A personal key or service account key has the same permissions as the linked account. See [Authentication](#authentication).

### Can I create new API keys through the Admin API?

No. You create API keys in the Claude Console. The Admin API can only read, rename, and change the status of existing keys.

### What happens to API keys when removing a user?

Behavior depends on the [key type](/docs/en/manage-claude/authentication#key-types).

Personal keys stop working when their user is removed from the organization. Service account keys stop working if their service account is archived, but continue to work even if the user that created them is removed. Workspace API keys continue to work. In the [Claude Code workspace](/docs/en/manage-claude/workspaces#claude-code-workspace), each key is bound to the member who created it and stops working when that member is removed.

### Can organization admins be removed through the API?

No. The API can't remove members with the admin role.

### How long do organization invites last?

Invites expire after 21 days. The expiration period isn't configurable.

For workspace-specific questions, see the [Workspaces FAQ](/docs/en/manage-claude/workspaces#faq).
