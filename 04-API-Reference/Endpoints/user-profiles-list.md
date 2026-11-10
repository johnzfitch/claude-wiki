---
title: "List User Profiles - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/user_profiles/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-06T06:33:46Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](platform-claude-com-http-beta-user-profiles-list.md).

1.  [API reference](http.md)
2.  [User Profiles](https://platform.claude.com/docs/en/api/http/user_profiles)

# List User Profiles

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/user_profiles

List User Profiles

##### Query parameters



enforcement_status: optional array of [UserProfileEnforcementStatus](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_enforcement_status)



Return only the user profiles whose `enforcement_status` is one of these values: `unrestricted`, `pending`, `restricted` or `banned`. Repeat the parameter to match any of several. With it set, a page may hold fewer than `limit` profiles, or none, and still carry a `next_page`: the service examines a bounded number of profiles per request, and only a null `next_page` means the listing is complete. Rejected with `invalid_request_error` under the `user-profiles-2026-09-04` and earlier beta headers. Fails with `overloaded_error` when a profile's enforcement actions cannot be read for the moment.

One of the following:

"unrestricted"



"pending"



"restricted"



"banned"





limit: optional number



The maximum number of user profiles to return, from 1 to 100. Defaults to 20.

formatint32



order: optional [UserProfileListOrder](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_list_order)

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

order_by: optional [UserProfileListOrderBy](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_list_order_by)

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

"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Returns



data: array of [UserProfile](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile) { type: "user_profile", id, access_type, 8 more }



User profiles on this page.

type: "user_profile"



Object type. Always `user_profile`.

id: string



Unique identifier for this user profile, prefixed `uprof_`.



access_type: [UserProfileAccessType](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_access_type)



How the platform uses the API for this entity: `application` (default) or `passthrough`. Absent under the legacy `user-profiles-2026-03-24` beta header.

One of the following:

"application"



The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.

"passthrough"



The user profile represents a company that the platform resells Claude access to.



created_at: string



When this user profile was created, in RFC 3339 format.

formatdate-time



enforcement_actions: array of [UserProfileEnforcementAction](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_enforcement_action)



The enforcement actions open on this profile; empty when none is open. Absent under the `user-profiles-2026-09-04` and earlier beta headers.

One of the following:



UserProfileEnforcementActionRestriction object{ type: "restriction", id, action, 3 more }



Anthropic has limited how it serves the end user until the action is resolved. The end user may still be served in part.



UserProfileEnforcementActionBan object{ type: "ban", id, action, 3 more }



Anthropic has stopped serving the end user where the ban applies and does not plan to serve them there again.

type: "ban"



id: string



The action's ID (`enac_...`), stable while the action is open.

action: [UserProfileEnforcementActionNextStep](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_enforcement_action_next_step) or null



Always `null`: the end user cannot clear a ban.



expires_at: string or null



Always `null`: a ban has no end date.

formatdate-time



opened_at: string



When Anthropic opened the action, in RFC 3339 format.

formatdate-time



reason: [UserProfileEnforcementActionReason](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_enforcement_action_reason)



Why Anthropic placed the limit: `unsupported_region`, `fraud_or_abuse`, `high_harm`, `usage_policy_violation`, `account_compromise` or `unspecified`.

One of the following:

"unsupported_region"



"fraud_or_abuse"



"high_harm"



"usage_policy_violation"



"account_compromise"



"unspecified"





enforcement_status: [UserProfileEnforcementStatus](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_enforcement_status)



Anthropic's enforcement status of this profile, from its open enforcement actions and any identity check under review, by the first rule that applies: `banned` while any open action is a `ban`; `pending` while a restriction that an identity check can clear is open, the end user has submitted that check, Anthropic's review of it has not ended, and no open action's `reason` is `account_compromise`; `restricted` while any action is open; `unrestricted` while none is. Absent under the `user-profiles-2026-09-04` and earlier beta headers.

One of the following:

"unrestricted"



"pending"



"restricted"



"banned"





external_user_details: [UserProfileExternalUserDetails](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_external_user_details) { account_status, country, email_hash, 4 more }



Details about the entity this profile represents, as the platform states them; not verified by Anthropic. Every field is present, `null` until the platform supplies a value. Absent under the legacy `user-profiles-2026-03-24` and `user-profiles-2026-08-18` beta headers, which serve `reference_id` as the top-level `external_id` and, under `user-profiles-2026-08-18`, `onboarded_at` as `external_user_onboarded_at`.

metadata: map\[string\]



Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

name: string or null



Real-world name of the entity this profile represents (company or individual). For a company the platform resells Claude access to (`access_type` `passthrough`) this is that company's name. `null` until the platform supplies one.



programs: [UserProfilePrograms](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_programs) { cyber, efs }



The profile's standing in each Anthropic program, such as the Cyber Verification Program. Present when the request sends no user-profiles beta header; absent under the `user-profiles-2026-09-04` and earlier beta headers, which serve `trust_grants` instead.



updated_at: string



When this user profile was last modified, in RFC 3339 format. It normally also updates shortly after Anthropic gives the profile an approval or withdraws one. Other changes to the statuses that Anthropic reports do not always update it, so read the status itself rather than watching this timestamp.

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
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
      "access_type": "application",
      "created_at": "2026-03-15T10:00:00Z",
      "enforcement_actions": [
        {
          "id": "enac_011CZkZCu8hGbp5mYRQgUmz9",
          "action": "verify",
          "expires_at": null,
          "opened_at": "2026-10-02T19:30:00Z",
          "reason": "fraud_or_abuse",
          "type": "restriction"
        }
      ],
      "enforcement_status": "unrestricted",
      "external_user_details": {
        "account_status": "active",
        "country": "US",
        "email_hash": null,
        "entity_type": "business",
        "name_hash": null,
        "onboarded_at": "2024-11-02T08:15:00Z",
        "reference_id": "user_12345"
      },
      "metadata": {},
      "name": "Example User",
      "programs": {
        "cyber": {
          "requirements": {
            "data_retention": true,
            "human_review": true
          },
          "status": "active",
          "tiers": {}
        },
        "efs": {
          "features": {
            "data_retention_exemption": {
              "status": "inactive"
            },
            "cmek": {
              "status": "active"
            },
            "storage": {
              "status": "inactive"
            }
          },
          "status": "active"
        }
      },
      "type": "user_profile",
      "updated_at": "2026-03-15T10:00:00Z"
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
      "access_type": "application",
      "created_at": "2026-03-15T10:00:00Z",
      "enforcement_actions": [
        {
          "id": "enac_011CZkZCu8hGbp5mYRQgUmz9",
          "action": "verify",
          "expires_at": null,
          "opened_at": "2026-10-02T19:30:00Z",
          "reason": "fraud_or_abuse",
          "type": "restriction"
        }
      ],
      "enforcement_status": "unrestricted",
      "external_user_details": {
        "account_status": "active",
        "country": "US",
        "email_hash": null,
        "entity_type": "business",
        "name_hash": null,
        "onboarded_at": "2024-11-02T08:15:00Z",
        "reference_id": "user_12345"
      },
      "metadata": {},
      "name": "Example User",
      "programs": {
        "cyber": {
          "requirements": {
            "data_retention": true,
            "human_review": true
          },
          "status": "active",
          "tiers": {}
        },
        "efs": {
          "features": {
            "data_retention_exemption": {
              "status": "inactive"
            },
            "cmek": {
              "status": "active"
            },
            "storage": {
              "status": "inactive"
            }
          },
          "status": "active"
        }
      },
      "type": "user_profile",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
