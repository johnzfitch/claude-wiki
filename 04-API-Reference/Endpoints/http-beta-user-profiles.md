---
title: "User Profiles - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/user_profiles"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:34:26Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)

# User Profiles

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create User Profile](platform-claude-com-http-beta-user-profiles-create.md)

POST/v1/user_profiles

##### [List User Profiles](platform-claude-com-http-beta-user-profiles-list.md)

GET/v1/user_profiles

##### [Get User Profile](platform-claude-com-http-beta-user-profiles-retrieve.md)

GET/v1/user_profiles/{user_profile_id}

##### [Update User Profile](platform-claude-com-http-beta-user-profiles-update.md)

POST/v1/user_profiles/{user_profile_id}

##### [Delete User Profile](https://platform.claude.com/docs/en/api/http/beta/user_profiles/delete)

DELETE/v1/user_profiles/{user_profile_id}

##### [Create Enrollment URL](platform-claude-com-http-beta-user-profiles-create-enrollment-url.md)

POST/v1/user_profiles/{user_profile_id}/enrollment_url

##### Models



BetaDeletedUserProfile object{ type: "user_profile_deleted", id }



type: "user_profile_deleted"



Object type. Always `user_profile_deleted`.

id: string



Identifier of the deleted user profile, prefixed `uprof_`.



BetaUserProfile object{ type: "user_profile", id, created_at, 8 more }



A record of an entity that the platform serves through the API, such as an end-user of the platform's product or a company that the platform resells Claude access to.

A Messages, Message Batches or token counting request can send a profile's `id` in the `anthropic-user-profile-id` header to attribute the request to that entity.



BetaUserProfileEnrollmentURL object{ type: "enrollment_url", expires_at, url }



A URL to give to the entity that a user profile represents, so that the entity can enroll in a program.

type: "enrollment_url"



Object type. Always `enrollment_url`.



expires_at: string



When this enrollment URL expires, in RFC 3339 format.

formatdate-time

url: string



Enrollment URL to send to the end user. Valid until `expires_at`.



BetaUserProfileExternalUserDetails object{ account_status, country, email_hash, 4 more }



Details about the entity this profile represents, as the platform states them. Anthropic does not verify them. Every field is present, `null` until the platform supplies a value.



BetaUserProfileExternalUserDetailsParams object{ account_status, country, email_hash, 4 more }





BetaUserProfileTrustGrant object{ status }



The status of one trust grant on a user profile, listed in the profile's `trust_grants` map under the grant's name.

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

#### User Profiles[Action URLs](https://platform.claude.com/docs/en/api/http/beta/user_profiles/action_urls)

##### [Create Action URL](https://platform.claude.com/docs/en/api/http/beta/user_profiles/action_urls/create)

POST/v1/user_profiles/{user_profile_id}/action_urls
