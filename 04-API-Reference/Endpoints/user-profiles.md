---
title: "User Profiles - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/user_profiles"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-14T06:25:01Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](platform-claude-com-http-beta-user-profiles.md).

1.  [API reference](http.md)

# User Profiles

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create User Profile](https://platform.claude.com/docs/en/api/http/user_profiles/create)

POST/v1/user_profiles

##### [List User Profiles](https://platform.claude.com/docs/en/api/http/user_profiles/list)

GET/v1/user_profiles

##### [Get User Profile](https://platform.claude.com/docs/en/api/http/user_profiles/retrieve)

GET/v1/user_profiles/{user_profile_id}

##### [Update User Profile](https://platform.claude.com/docs/en/api/http/user_profiles/update)

POST/v1/user_profiles/{user_profile_id}

##### [Delete User Profile](https://platform.claude.com/docs/en/api/http/user_profiles/delete)

DELETE/v1/user_profiles/{user_profile_id}

##### Models



DeletedUserProfile object{ type: "user_profile_deleted", id }



type: "user_profile_deleted"



Object type. Always `user_profile_deleted`.

id: string



Identifier of the deleted user profile, prefixed `uprof_`.



UserProfile object{ type: "user_profile", id, access_type, 8 more }



A record of an entity that the platform serves through the API, such as an end-user of the platform's product or a company that the platform resells Claude access to.

A Messages, Message Batches or token counting request can send a profile's `id` in the `anthropic-user-profile-id` header to attribute the request to that entity.



UserProfileAccessType = "application" or "passthrough"



How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

One of the following:

"application"



The user profile represents an individual end-user of a product that the platform builds on the API. New profiles get this value by default.

"passthrough"



The user profile represents a company that the platform resells Claude access to.



UserProfileCyberProgram object{ requirements, status, tiers }



A user profile's standing in the Cyber Verification Program, which relaxes cyber safeguards for requests that name the profile.



UserProfileCyberRequirements object{ data_retention, human_review }



What a request that names the profile must allow to get the relaxed safeguards of the profile's `active` tiers. A field reads `true` when at least one of those tiers has the requirement and Anthropic has not waived it on that tier for the profile. A request that does not meet a requirement is still served, without the relaxed safeguards of the tiers that have it. The values differ between profiles and can change, so read them rather than assuming them.

data_retention: boolean



Whether Anthropic must be able to retain the request's inference data.

human_review: boolean



Whether Anthropic personnel must be allowed to review the data retained from the request.



UserProfileCyberTier object{ status }



One tier of the Cyber Verification Program.



status: "active" or "inactive"



`active` when the tier applies to the profile, otherwise `inactive`. The response does not say why a tier is `inactive`: it can be in review, declined, withdrawn, never applied for, or approved but not applied to this profile.

One of the following:

"active"



"inactive"





UserProfileEfsFeature object{ status }



One feature of Enterprise Frontier Safeguards.



status: "active" or "inactive"



`active` when Anthropic has approved the entity the profile represents to use the feature, otherwise `inactive`. `active` does not mean that the feature is set up or switched on, which is a separate step.

One of the following:

"active"



"inactive"





UserProfileEfsProgram object{ features, status }



A user profile's standing in Enterprise Frontier Safeguards, a program under which Anthropic approves the entity the profile represents and may approve any of the program's features.



features: map\[[UserProfileEfsFeature](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_efs_feature) { status }\]



The program's features, keyed by feature: `data_retention_exemption` (use of models that normally require data retention, without the data being retained), `cmek` (customer-managed encryption keys) and `storage` (customer-owned storage). Every feature that the caller's organization may read has a key, whether or not it is approved; a missing key does not mean that the feature is inactive. Anthropic may add features; ignore a key you do not recognize.



status: "active" or "inactive"



`active` when Anthropic has approved the entity the profile represents to use the feature, otherwise `inactive`. `active` does not mean that the feature is set up or switched on, which is a separate step.

One of the following:

"active"



"inactive"





status: [UserProfileProgramStatus](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_program_status)



Anthropic's decision on the entity the profile represents: `pending` while it is awaited, `active` once Anthropic has approved the entity for the program, or `rejected` once Anthropic has declined or has removed the entity from the program. `active` does not mean that any one feature is approved: read the feature you need in `features`.

One of the following:

"active"



The profile is in the program.

"pending"



The profile is not in the program yet, and something is still awaited.

"rejected"



The profile is not in the program and nothing is awaited: Anthropic has declined, or has withdrawn an earlier approval.



UserProfileEnforcementAction = [UserProfileEnforcementActionRestriction](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_enforcement_action_restriction) or [UserProfileEnforcementActionBan](https://platform.claude.com/docs/en/api/http/user_profiles#user_profile_enforcement_action_ban)



A limit Anthropic has placed on the entity this profile represents and not yet resolved, discriminated by `type`: `restriction` or `ban`. More types may be added; read a `type` you do not recognize as `restriction`.

One of the following:

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

UserProfileEnforcementActionNextStep = "verify"



The next step on this enforcement action: `verify` means the end user can clear the action by passing an identity check. More values may be added; read a value you do not recognize as `null`.



UserProfileEnforcementActionReason = "unsupported_region" or "fraud_or_abuse" or "high_harm" or 3 more



Why Anthropic placed this enforcement action: `unsupported_region`, `fraud_or_abuse`, `high_harm`, `usage_policy_violation`, `account_compromise` or `unspecified`. More values may be added; read a value you do not recognize as `unspecified`.

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

UserProfileEnforcementActionRestriction object{ type: "restriction", id, action, 3 more }



Anthropic has limited how it serves the end user until the action is resolved. The end user may still be served in part.



UserProfileEnforcementStatus = "unrestricted" or "pending" or "restricted" or "banned"



Anthropic's enforcement status of this profile: `unrestricted`, `pending`, `restricted` or `banned`. More values may be added; read a value you do not recognize as `restricted`.

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

UserProfileExternalUserAccountStatus = "active" or "suspended" or "blocked"



The status of the entity's account on the platform, as the platform states it: `active`; `suspended`, when the platform has restricted the account and may restore it; or `blocked`, when the platform has barred it. It records the platform's decision only. The statuses that Anthropic itself reports for the profile, such as its status in a program, are Anthropic's decisions and do not change with it.

One of the following:

"active"



The platform has neither restricted nor barred the account of the entity that the user profile represents.

"suspended"



The platform has restricted the account of the entity that the user profile represents and may restore it.

"blocked"



The platform has barred the account of the entity that the user profile represents.



UserProfileExternalUserDetails object{ account_status, country, email_hash, 4 more }



Details about the entity this profile represents, as the platform states them. Anthropic does not verify them. Every field is present, `null` until the platform supplies a value.



UserProfileExternalUserDetailsParams object{ account_status, country, email_hash, 4 more }





UserProfileExternalUserEntityType = "individual" or "business" or "non_profit" or "government"



What kind of entity the profile represents, as the platform states it: `individual`, `business`, `non_profit` or `government`.

One of the following:

"individual"



"business"



"non_profit"



"government"





UserProfileListOrder = "asc" or "desc"



The direction that a list of user profiles is sorted in.

One of the following:

"asc"



Oldest first when `order_by` is `created_at`, or names in ascending order when `order_by` is `name`.

"desc"



Newest first when `order_by` is `created_at`, or names in descending order when `order_by` is `name`. This is the default.



UserProfileListOrderBy = "created_at" or "name"



Sort field for listing user profiles: `created_at` (default) or `name` (case-insensitive; profiles without a name sort last).

One of the following:

"created_at"



Sort by when each user profile was created. This is the default.

"name"



Sort by `name`, ignoring the case of ASCII letters. Profiles without a name come last in either direction.



UserProfileNotFoundErrorDetails object{ error_code }



The request depends on a user profile that does not exist in the organization or is no longer active. The request either names this user profile by ID, or names a resource, such as an External Key, that is bound to it.

error_code: "user_profile_not_found"





UserProfileProgramStatus = "active" or "pending" or "rejected"



A user profile's status in a program. Each program's `status` field says what the values mean there.

One of the following:

"active"



The profile is in the program.

"pending"



The profile is not in the program yet, and something is still awaited.

"rejected"



The profile is not in the program and nothing is awaited: Anthropic has declined, or has withdrawn an earlier approval.



UserProfilePrograms object{ cyber, efs }



A user profile's standing in each program. A program is a set of capabilities or exemptions that Anthropic approves for the entity the profile represents. A program reads `null` when the profile has no status in it, when the caller's organization is not entitled to read programs, or when the response does not report that program. Retrieving the profile reports every program. Anthropic may add programs; ignore a key you do not recognize.

#### User Profiles[Action URLs](https://platform.claude.com/docs/en/api/http/user_profiles/action_urls)

##### [Create Action URL](https://platform.claude.com/docs/en/api/http/user_profiles/action_urls/create)

POST/v1/user_profiles/{user_profile_id}/action_urls
