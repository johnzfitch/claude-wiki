---
title: "Get User Profile - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/user_profiles/retrieve"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-06T06:27:03Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](platform-claude-com-http-beta-user-profiles-retrieve.md).

1.  [API reference](http.md)
2.  [User Profiles](https://platform.claude.com/docs/en/api/http/user_profiles)

# Get User Profile

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/user_profiles/{user_profile_id}

Get User Profile

##### Path parameters

user_profile_id: string



The ID of the user profile to get (`uprof_...`).

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

UserProfile object{ type: "user_profile", id, access_type, 8 more }



A record of an entity that the platform serves through the API, such as an end-user of the platform's product or a company that the platform resells Claude access to.

A Messages, Message Batches or token counting request can send a profile's `id` in the `anthropic-user-profile-id` header to attribute the request to that entity.

Get User Profile

cURL



```python
curl https://api.anthropic.com/v1/user_profiles/$USER_PROFILE_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
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
      "tiers": {
        "a": {
          "status": "inactive"
        },
        "b": {
          "status": "inactive"
        },
        "c": {
          "status": "inactive"
        }
      }
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
```

##### Returns Examples

Response 200



```python
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
      "tiers": {
        "a": {
          "status": "inactive"
        },
        "b": {
          "status": "inactive"
        },
        "c": {
          "status": "inactive"
        }
      }
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
