---
title: "List User Profiles - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/user_profiles/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-05T06:36:18Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)
3.  [User Profiles](platform-claude-com-http-beta-user-profiles.md)

# List User Profiles

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/user_profiles

List User Profiles

##### Query parameters



limit: optional number



The maximum number of user profiles to return, from 1 to 100. Defaults to 20.

formatint32



order: optional "asc" or "desc"



The sort direction, applied to the field that `order_by` selects. Defaults to `desc`.

One of the following:

"asc"



Oldest first when `order_by` is `created_at`, or names in ascending order when `order_by` is `name`.

"desc"



Newest first when `order_by` is `created_at`, or names in descending order when `order_by` is `name`. This is the default.



order_by: optional "created_at" or "name"



The field to sort user profiles by, in the direction that `order` sets. Defaults to `created_at`.

One of the following:

"created_at"



Sort by when each user profile was created. This is the default.

"name"



Sort by `name`, ignoring the case of ASCII letters. Profiles without a name come last in either direction.



page: optional string



The cursor for the page to return, taken from `next_page` in a previous response.

Leave it out to get the first page.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).



"anthropic-beta": optional array of [AnthropicBeta](platform-claude-com-http-beta.md#anthropic_beta)



Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24"



"prompt-caching-2024-07-31"



"computer-use-2024-10-22"



"computer-use-2025-01-24"



"pdfs-2024-09-25"



"token-counting-2024-11-01"



"token-efficient-tools-2025-02-19"



"output-128k-2025-02-19"



"files-api-2025-04-14"



"mcp-client-2025-04-04"



"mcp-client-2025-11-20"



"dev-full-thinking-2025-05-14"



"interleaved-thinking-2025-05-14"



"code-execution-2025-05-22"



"extended-cache-ttl-2025-04-11"



"context-1m-2025-08-07"



"context-management-2025-06-27"



"model-context-window-exceeded-2025-08-26"



"skills-2025-10-02"



"fast-mode-2026-02-01"



"output-300k-2026-03-24"



"user-profiles-2026-03-24"



"user-profiles-2026-08-18"



"user-profiles-2026-09-04"



"advisor-tool-2026-03-01"



"managed-agents-2026-04-01"



"cache-diagnosis-2026-04-07"



"dreaming-2026-04-21"



"thinking-token-count-2026-05-13"



"server-side-fallback-2026-06-01"



"server-side-fallback-2026-07-01"



"fallback-credit-2026-06-01"



"fallback-credit-2026-07-01"



"agent-memory-2026-07-22"



"mid-conversation-tool-changes-2026-07-01"



"compact-2026-01-12"



"computer-use-2025-11-24"



"mcp-tunnels-2026-06-22"



"structured-outputs-2025-11-13"



"task-budgets-2026-03-13"



"thinking-display-updates-2026-08-18"



"ce-user-management-2026-07-13"



"mid-conversation-output-config-2026-07-01"



"thinking-binding-controls-2026-08-01"



"mid-conversation-system-clear-at-2026-08-21"



"compact-2026-09-04"



"inline-tools-2026-09-15"



"mcp-client-2026-09-15"



"ce-plugins-2026-09-01"



"spend-limit-reads-2026-09-26"



"telemetry-destinations-2026-08-11"



"webhooks-2026-10-07"



"message-threads-2026-08-12"



"analytics-usage-cost-2026-08-24"



"experimental-claude-tag-2026-10-21"





"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Returns



data: array of [BetaUserProfile](platform-claude-com-http-beta-user-profiles.md#beta_user_profile) { type: "user_profile", id, created_at, 8 more }



User profiles on this page.

type: "user_profile"



Object type. Always `user_profile`.

id: string



Unique identifier for this user profile, prefixed `uprof_`.



created_at: string



When this user profile was created, in RFC 3339 format.

formatdate-time

metadata: map\[string\]



Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

name: string or null



Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name. `null` until the platform supplies one.



trust_grants: map\[[BetaUserProfileTrustGrant](platform-claude-com-http-beta-user-profiles.md#beta_user_profile_trust_grant) { status }\]

⁠





Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.



status: "active" or "pending" or "rejected"



Status of the trust grant.

One of the following:

"active"



"pending"



"rejected"





updated_at: string



When this user profile was last modified, in RFC 3339 format. It normally also updates shortly after Anthropic gives the profile an approval or withdraws one. Other changes to the statuses that Anthropic reports do not always update it, so read the status itself rather than watching this timestamp.

formatdate-time



access_type: optional "application" or "passthrough"



How the platform uses the API for this entity: `application` (default) or `passthrough`. Absent under the legacy `user-profiles-2026-03-24` beta header.

One of the following:

"application"



The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.

"passthrough"



The user profile represents a company that the platform resells Claude access to.

external_id: optional string or null

⁠





Platform's own identifier for this user. Not enforced unique. Legacy field, present only under the `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers; without one of them, the value is `external_user_details.reference_id`.



external_user_details: optional [BetaUserProfileExternalUserDetails](platform-claude-com-http-beta-user-profiles.md#beta_user_profile_external_user_details) { account_status, country, email_hash, 4 more }



Details about the entity this profile represents, as the platform states them; not verified by Anthropic. Every field is present, `null` until the platform supplies a value. Absent under the legacy `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers, which serve `reference_id` as the top-level `external_id` and, under `user-profiles-2026-08-18`, `onboarded_at` as `external_user_onboarded_at`.



external_user_onboarded_at: optional string or null

⁠





When the entity this profile represents opened its account with the platform, as stated by the platform, in RFC 3339 format (UTC). `null` until the platform supplies one. Legacy field, present only under the `user-profiles-2026-08-18` beta header; without a legacy header, the value is `external_user_details.onboarded_at`.

formatdate-time

next_page: string or null



Cursor for the next page, or `null` when there are no more results.

List User Profiles

cURL



```python
curl https://api.anthropic.com/v1/user_profiles \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: user-profiles-2026-08-18' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {},
      "name": "Example User",
      "trust_grants": {
        "cyber": {
          "status": "active"
        }
      },
      "type": "user_profile",
      "updated_at": "2026-03-15T10:00:00Z",
      "access_type": "application",
      "external_id": "user_12345",
      "external_user_details": {
        "account_status": "active",
        "country": "US",
        "email_hash": null,
        "entity_type": "business",
        "name_hash": null,
        "onboarded_at": "2024-11-02T08:15:00Z",
        "reference_id": "user_12345"
      },
      "external_user_onboarded_at": "2024-11-02T08:15:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {},
      "name": "Example User",
      "trust_grants": {
        "cyber": {
          "status": "active"
        }
      },
      "type": "user_profile",
      "updated_at": "2026-03-15T10:00:00Z",
      "access_type": "application",
      "external_id": "user_12345",
      "external_user_details": {
        "account_status": "active",
        "country": "US",
        "email_hash": null,
        "entity_type": "business",
        "name_hash": null,
        "onboarded_at": "2024-11-02T08:15:00Z",
        "reference_id": "user_12345"
      },
      "external_user_onboarded_at": "2024-11-02T08:15:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
