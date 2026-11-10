---
title: "Action URLs - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/user_profiles/action_urls"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-06T06:33:45Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/user_profiles/action_urls).

1.  [API reference](http.md)
2.  [User Profiles](https://platform.claude.com/docs/en/api/http/user_profiles)

# Action URLs

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create Action URL](https://platform.claude.com/docs/en/api/http/user_profiles/action_urls/create)

POST/v1/user_profiles/{user_profile_id}/action_urls

##### Models



UserProfileAction = [UserProfileEnrollEndUserAction](https://platform.claude.com/docs/en/api/http/user_profiles/action_urls#user_profile_enroll_end_user_action)



The action that the person who opens the URL takes, discriminated by `type`.

One of the following:



UserProfileEnrollEndUserAction object{ type: "enroll_end_user" }



The end-user that the profile represents enrolls in a program.

type: "enroll_end_user"





UserProfileActionURL object{ type: "user_profile_action_url", expires_at, url }



A URL to give to the person who takes the requested action.

type: "user_profile_action_url"



Object type. Always `user_profile_action_url`.



expires_at: string



When the URL stops working, in RFC 3339 format.

formatdate-time

url: string



The URL to give to the person who takes the action. Anyone who holds it can open it until `expires_at`.



UserProfileEnrollEndUserAction object{ type: "enroll_end_user" }



The end-user that the profile represents enrolls in a program.
