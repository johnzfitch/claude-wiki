---
title: "User profiles for end-customer attribution - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/user-profiles"
category: "04-API-Reference/Other"
fetched_at: "2026-10-21T06:29:18Z"
tags: ["api"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fuser-profiles)





SearchCtrlK

Organization

[Admin API](manage-claude-admin-api.md)[User management](manage-claude-user-management.md)[Plugins API](manage-claude-plugins-api.md)[Workspaces](manage-claude-workspaces.md)[Organization webhooks (beta)](manage-claude-organization-webhooks.md)[User profiles](manage-claude-user-profiles.md)[Verification Portal links](manage-claude-user-profiles-verification-portal.md)

Authentication

[Overview](manage-claude-authentication.md)[Create an Admin API key](manage-claude-admin-api-keys.md)[App Attest](manage-claude-app-attest.md)[Workload Identity Federation](manage-claude-workload-identity-federation.md)[Manage WIF via API](manage-claude-wif-admin-api.md)[WIF reference](manage-claude-wif-reference.md)

Identity providers

Monitoring

[Usage and Cost API](manage-claude-usage-cost-api.md)[Rate Limits API](manage-claude-rate-limits-api.md)[Analytics APIs](manage-claude-analytics-api.md)[Claude Code Analytics API](manage-claude-claude-code-analytics-api.md)[Spend Limits API](manage-claude-spend-limits-api.md)

[OpenTelemetry](manage-claude-opentelemetry.md)

Data & compliance

[Data residency](manage-claude-data-residency.md)[API and data retention](manage-claude-api-and-data-retention.md)

[Access Transparency](manage-claude-access-transparency.md)

[Encryption keys (CMEK)](manage-claude-cmek.md)

[Inference hooks](manage-claude-inference-hooks.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](playground.md)

[Admin](manage-claude-admin-api.md)Organization

# User profiles for end-customer attribution

Copy page



Attribute API requests to the end customers your platform serves, so a safety enforcement action can apply to one profile instead of your whole organization.

Copy page



User profiles ("profiles") tell Anthropic which of your end customers each API request is for. A safety enforcement action, such as a restriction or a ban, can then apply to one end customer instead of your whole organization. When it does, the rest of your traffic is unaffected.

If you operate a platform or gateway, or resell API access, the requests you send for your end customers arrive under your organization. Anthropic runs automated safety classifiers over API traffic. Without a profile on the request, one end customer can trigger an enforcement action that applies to your whole organization.

You register each end customer once with `POST /v1/user_profiles` and store the `uprof_` ID it returns. Then you send that ID in the `anthropic-user-profile-id` header on every request you make on that end customer's behalf.

Profiles aren't billable and don't affect pricing.

## Decide who gets a profile

What a profile stands for depends on how you sell Claude: a person who uses your product, or a company you resell API access to. These two cases cover most platforms. The profile's `access_type` field says which one applies.

| Who the traffic is for                                       | Profile                                                                                                                                 | `access_type`                                                     |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| A signed-up user of your product                             | One for each user, created when they sign up.                                                                                           | `application` (the default, set when you leave `access_type` out) |
| A company you resell API access to, for example as a gateway | One for each company, not for each person within it.                                                                                    | `passthrough` (not the default, so you have to send it)           |
| Your own organization                                        | None. Anthropic counts a request with no profile ID as your own usage. Keep that usage in a [separate organization](#before-you-begin). | Not applicable                                                    |
| A workspace in your organization                             | No separate profile. A profile belongs to your organization, and its ID works on requests through any workspace in it.                  | Not applicable                                                    |

## What a profile contains and how Anthropic uses it

A profile contains only what you send about the end customer, plus any [program status](manage-claude-user-profiles-verification-portal.md#after-the-end-customer-links-the-profile) that Anthropic sets. It doesn't contain conversation content. Anthropic uses the details you send to attribute requests, to monitor for abuse, for enforcement of the [Usage Policy](https://www.anthropic.com/legal/aup), and to enable application and access to trusted access programs. Anthropic doesn't verify the details.

Anthropic processes profiles in accordance with the [Privacy Policy](https://www.anthropic.com/legal/privacy).

## Before you begin

You create and manage profiles in one of the following:

- An organization on the Claude API.
- An organization on [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md). The calling principal needs the [user profile IAM actions](../Endpoints/claude-platform-on-aws-iam-actions.md#user-profiles).
- A [Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md) deployment [hosted on Anthropic](../Guides/build-with-claude-claude-in-microsoft-foundry.md#hosting-options), not one hosted on Azure. You don't need an organization on the Claude API or Claude Platform on AWS. Use your Foundry endpoint, with the same base URL and authentication that you use for inference.

Amazon Bedrock and Google Cloud don't have the `/v1/user_profiles` endpoints. If your inference runs there, create your profiles in an organization on the Claude API or Claude Platform on AWS. On Amazon Bedrock, profiles work only with [Claude in Amazon Bedrock](../Guides/build-with-claude-claude-in-amazon-bedrock.md). See [Attribute requests on Amazon Bedrock and Google Cloud](#attribute-requests-on-amazon-bedrock-and-google-cloud).

Keep the traffic you send for your end customers in one organization and your own internal usage in another. Profiles belong to an organization, not a workspace, so separate workspaces in one organization aren't enough. Only the organization for end-customer traffic needs user profiles. To create another organization on the Claude API, see the "How to create a new organization" section of [Creating and managing Workspaces in the Claude Console](https://support.claude.com/en/articles/9796807) in the Claude Help Center.

The examples call the Claude API with an API key. You don't need an [Admin API key](manage-claude-admin-api-keys.md). On Claude Platform on AWS, use its base URL and authentication.

## Create a profile for each end customer

Create one profile for each end customer whose traffic you send to Claude. Create it once, in your customer-onboarding flow. `POST /v1/user_profiles` isn't idempotent, so every call creates a new profile, even when `reference_id` matches an existing one. If you already have end customers without profiles, see the guidance on registering an existing customer base later in this section.

The following example registers a company that buys API access through a gateway, so it sets `access_type` to `passthrough`. For an `application` profile, leave out `access_type`, and describe one end user in `name` and `external_user_details` instead of a company. [Decide who gets a profile](#decide-who-gets-a-profile) compares the two access types.

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

profile = client.user_profiles.create(
    name="Acme Analytics, Inc.",
    access_type="passthrough",
    external_user_details={"reference_id": "cust-8f2a1c", "country": "US"},
)

print(profile.id)
```

The response is the new profile:

```python
{
  "type": "user_profile",
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "name": "Acme Analytics, Inc.",
  "access_type": "passthrough",
  "external_user_details": {
    "reference_id": "cust-8f2a1c",
    "onboarded_at": null,
    "account_status": null,
    "entity_type": null,
    "country": "US",
    "name_hash": null,
    "email_hash": null
  },
  "metadata": {},
  "programs": {
    "cyber": null,
    "efs": null
  },
  "created_at": "2026-03-15T10:00:00Z",
  "updated_at": "2026-03-15T10:00:00Z"
}
```



Store the `id` on your customer record, and have your service instances read it from there instead of creating their own profile. You retrieve, update, and delete a profile by that `id`. The `programs` field is read-only, and attribution doesn't use it. It holds the end customer's status in each program that Anthropic runs. For what its values mean, see [which programs apply to a profile](manage-claude-user-profiles-verification-portal.md#after-the-end-customer-links-the-profile).

There's no cap on the number of profiles in an organization, but profile creation is rate limited. Before you register an existing customer base in bulk, contact your Anthropic account team.

### What to tell Anthropic about an end customer

Every field is optional. You can send `name`, `metadata`, and these fields in `external_user_details`: `entity_type`, `country`, `reference_id`, `onboarded_at`, `account_status`, `name_hash`, and `email_hash`. The [Create a profile](../Endpoints/user-profiles-create.md) reference describes each field, with its type, format, and length limit.

Follow these rules when you set the fields:

- **Unknown values:** If you don't know a value, leave it out instead of sending a placeholder. You can replace a value in `external_user_details` later, but you can't clear it.
- **Company names:** For a `passthrough` profile, send the company's legal name in `name` if you know it.
- **Country:** In `country`, send the end customer's country, not yours.
- **Your own ID:** In `reference_id`, send your own stable identifier for the end customer. It doesn't have to be unique.
- **Names and email addresses you can't share:** Leave out `name` and send `external_user_details.name_hash` instead. For the email address, send `external_user_details.email_hash`. A profile has no field for the address itself.
- **Hashes:** Compute the hashes yourself, with a function you choose. They show Anthropic which of your profiles share a name or an email address. Use the same function and the same case and whitespace normalization for every profile, because only values computed the same way match.

## Attribute each request

Send the profile ID in the `anthropic-user-profile-id` header on every request you make on the end customer's behalf. The SDK and the CLI have an argument that sends the header for you: `user_profile_id`.

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

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    user_profile_id=profile_id,
)

print(message)
```

The header works the same way on [token counting](../Guides/build-with-claude-token-counting.md), [Message Batches](../Guides/build-with-claude-batch-processing.md), and [OpenAI SDK compatibility](cli-sdks-libraries-libraries-openai-sdk.md) requests. On a batch, it applies to every request in the batch.

The Claude API, Claude Platform on AWS, and Microsoft Foundry deployments hosted on Anthropic check the ID on every request. If the ID is malformed or doesn't belong to the organization that sends the request, the API returns a `400` `invalid_request_error`. By default, these platforms accept a profile ID only on requests from the organization that created the profile. This means that if you send traffic under more than one organization, for example one on the Claude API and one on Claude Platform on AWS, a request from an organization that didn't create the profile gets the same `400`.

Message Batches is the exception: creating a batch checks only the ID's format. If a well-formed ID doesn't belong to the organization that sends the batch, the batch is still created, and each request in it then fails with an `errored` result that contains the same `invalid_request_error`.

### Attribute requests on Amazon Bedrock and Google Cloud

A profile ID of either access type also works on [Claude in Amazon Bedrock](../Guides/build-with-claude-claude-in-amazon-bedrock.md) and on Google Cloud. It doesn't work with the [earlier Amazon Bedrock integration](../Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md) that you call with `InvokeModel` or `Converse`. You use your Anthropic organization's credentials only to create and manage profiles. Inference stays on your existing AWS or Google Cloud credentials.

| Platform                                                                                                     | Create profiles                                              | Send the profile ID in                      |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|---------------------------------------------|
| Claude API                                                                                                   | Yes                                                          | `anthropic-user-profile-id` header          |
| [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)                                  | Yes                                                          | `anthropic-user-profile-id` header          |
| [Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md), deployments hosted on Anthropic | Yes                                                          | `anthropic-user-profile-id` header          |
| [Google Cloud](../Guides/build-with-claude-claude-on-vertex-ai.md)                                               | No. Create them on the Claude API or Claude Platform on AWS. | `anthropic-user-profile-id` header          |
| [Claude in Amazon Bedrock](../Guides/build-with-claude-claude-in-amazon-bedrock.md)                              | No. Create them on the Claude API or Claude Platform on AWS. | `user_profile_id` field in the request body |

On Claude in Amazon Bedrock, put the ID at the top level of the request body:

```python
{
  "model": "anthropic.claude-opus-5-5",
  "max_tokens": 1024,
  "user_profile_id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "messages": [{ "role": "user", "content": "Hello, Claude" }]
}
```



Link each AWS account that sends requests to Claude in Amazon Bedrock, and each Google Cloud project that sends requests on Google Cloud, to the Anthropic organization that creates your profiles:

1.  An admin or owner of that organization starts the link in the Verification Portal at `portal.anthropic.com`, under **Linked accounts**.
2.  Someone who can manage IAM in the AWS account or Google Cloud project runs a command that the portal provides.
3.  The admin or owner completes the verification in the portal.

Programs that apply to a profile apply to an account's requests only after the account is linked and the portal shows it as **Linked**. Those programs include the ones an end customer's organization is approved for after the end customer [links the profile to that organization](manage-claude-user-profiles-verification-portal.md) and, for Cyber Verification Program access levels, turns them on for the profile in the portal.

Claude in Amazon Bedrock and Google Cloud check the format of the ID but don't look the profile up. They reject a malformed ID with a `400`. They accept any well-formed ID, so a successful response doesn't confirm that the ID matches a profile. A request with no ID goes through unattributed, and if it triggers an enforcement action, the action applies to your whole organization.

### Identify individual users within a company

A `passthrough` profile identifies a company, not the person making the request. If a request comes from one identifiable person, also send an identifier for that person in the [`metadata.user_id`](../Endpoints/messages-create.md) field of the Messages request. This is the request's own `metadata` object, not the profile's `metadata` field. The identifier is optional, and it helps Anthropic detect misuse by one person.

## Keep profiles current

Update a profile when the end customer's details or account status change, and delete it when they close their account or ask you to erase their data.

### Update a profile

[`POST /v1/user_profiles/{id}`](../Endpoints/user-profiles-update.md) changes only the fields you send. For example, use it when a company rebrands or you suspend an account.

- `name` and `access_type` replace the stored value.
- Each field you send in `external_user_details` replaces the stored value. You can't clear a value. The API rejects `null` with a `400`.
- `metadata` merges key by key. A key you send overwrites the stored value, an empty string deletes the key, and keys you leave out stay as they are.

The following example marks the account as suspended and removes a `trial_cohort` metadata key.

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

profile = client.user_profiles.update(
    profile_id,
    external_user_details={"account_status": "suspended"},
    metadata={"trial_cohort": ""},
)

print(profile)
```

### Delete a profile

[`DELETE /v1/user_profiles/{id}`](../Endpoints/user-profiles-delete.md) permanently deletes a profile and everything you supplied for it, including `name`, `external_user_details`, and `metadata`. It doesn't remove the trust and safety records that Anthropic keeps about that profile ID.

Delete a profile when an end customer closes their account or asks you to erase their data. Before you delete a profile, stop sending its ID on that end customer's requests. If the end customer stays with you after an erasure request, create a new profile and switch to its ID. Then delete the old one.

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

deleted = client.user_profiles.delete(profile_id)

print(deleted.id)
```

The response repeats the ID with `"type": "user_profile_deleted"`. If a delete returns a server error, retry it. A `404` on the retry means the first delete went through.

After a delete, the profile endpoints return a `404` for that ID. For up to about 10 minutes, inference requests that carry the deleted ID can still succeed. After that, the platforms that check the ID on every request reject the request with a `400`. Claude in Amazon Bedrock and Google Cloud don't look profiles up, so they still accept it.

## Next steps

The API reference has each endpoint's fields, types, and limits: [Create a profile](../Endpoints/user-profiles-create.md), [Retrieve a profile](../Endpoints/user-profiles-retrieve.md), [Update a profile](../Endpoints/user-profiles-update.md), [Delete a profile](../Endpoints/user-profiles-delete.md), and [List profiles](../Endpoints/user-profiles-list.md).

If an end customer's program approvals should apply when they use Claude through your platform, see [Send an end customer a link to the Verification Portal](manage-claude-user-profiles-verification-portal.md).

To get an event when Anthropic restricts or bans one of your end customers, or when the restriction or ban ends, see [Organization webhooks](manage-claude-organization-webhooks.md).

[Authentication](manage-claude-authentication.md)

Choose how your services authenticate to the Claude API.

[Usage and Cost API](manage-claude-usage-cost-api.md)

Track API token usage and costs for your organization.

[Data residency](manage-claude-data-residency.md)

Manage where model inference runs and where data is stored.

[Compliance API](manage-claude-compliance-api.md)

Audit activity across your organization.
