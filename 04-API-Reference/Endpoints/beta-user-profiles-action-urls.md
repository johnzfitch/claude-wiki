---
title: "Action URLs - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/user_profiles/action_urls"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-06T06:27:02Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)
3.  [User Profiles](platform-claude-com-http-beta-user-profiles.md)

# Action URLs

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create Action URL](https://platform.claude.com/docs/en/api/http/beta/user_profiles/action_urls/create)

POST/v1/user_profiles/{user_profile_id}/action_urls

##### Models



BetaUserProfileAction = [BetaUserProfileEnrollEndUserAction](https://platform.claude.com/docs/en/api/http/beta/user_profiles/action_urls#beta_user_profile_enroll_end_user_action)



The action that the person who opens the URL takes, discriminated by `type`.

One of the following:



BetaUserProfileEnrollEndUserAction object{ type: "enroll_end_user" }



The end-user that the profile represents enrolls in a program.

type: "enroll_end_user"





BetaUserProfileActionURL object{ type: "user_profile_action_url", expires_at, url }

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

BetaUserProfileEnrollEndUserAction object{ type: "enroll_end_user" }



The end-user that the profile represents enrolls in a program.
