---
title: "Claude Enterprise Admin API reference guide | Claude Help Center"
source_url: "https://support.claude.com/en/articles/15330651-claude-enterprise-admin-api-reference-guide"
category: "13-Enterprise-Admin"
fetched_at: "2026-09-29T06:31:53Z"
tags: ["api", "authentication", "enterprise"]
---

# Claude Enterprise Admin API reference guide

June 24, 2026

Copy for LLM

This guide covers **spend limits** and **spend limit increase requests** for your Claude Enterprise organization using the Claude Enterprise Admin API. Spend limits let you cap each member's usage credit spending over a recurring period, see where each member's limit is inherited from, and review or act on members' requests for a higher limit.

For per-user and time-bucketed usage and cost reporting, see the **[Analytics API reference guide](https://platform.claude.com/docs/en/api/admin/analytics)**.

Claude Enterprise Admin API is currently in public beta and available to organizations on Enterprise plans with usage credits enabled.

## Overview

There are eight endpoints across two resources:

[TABLE]

Use the **spend limits** endpoints to answer, “What limit applies to each member, where does it come from, and how close are they to it?" and to set a per-user override. Use the **spend limit increase requests** endpoints to work the queue of member-submitted requests.

## Prerequisites and authentication

- Your organization must be on a Claude Enterprise plan.

- Usage credits must be enabled for your organization. Your Primary Owner can enable this under **Billing settings** in Claude.

- The Primary Owner needs to mint an Admin API key with one or both of the following scopes:

  - **`read:spend_limits`** (required for all `GET` endpoints)

  - **`write:spend_limits`** (required for `POST` and `DELETE` endpoints)

Pass the key in the **`x-api-key`** header on every request.

**Important:** Don't share API keys publicly or check them into source control.

## Create an Admin API key for your Claude Enterprise organization

1.  **Sign in as the Primary Owner**—Only the Primary Owner of your Claude Enterprise parent organization can create these keys.

2.  **Open API settings**—Go to **[Organization settings \> API](https://claude.ai/admin-settings/api-access)** and find the **Keys** section.

3.  **Click and create key**—Name the key and select the scopes you need from the **[scopes table](https://platform.claude.com/docs/en/manage-claude/admin-api-keys#choose-scopes-for-a-claude-enterprise-key)**. You can combine scopes from different APIs (for example, `read:analytics` and `read:spend_limits`) on a single key.

4.  **Copy and store the secret**—Copy the displayed secret (starting with `sk-ant-api01-`) and store it in your secrets manager. The full secret is shown only once.

## Base URL

    https://api.anthropic.com

## Rate limiting

All eight endpoints share a single per-organization limit of **60 requests per minute**. Requests over the limit return **429 Too Many Requests**.

## Pagination

`GET /v1/organizations/spend_limits/effective` and `GET /v1/organizations/spend_limit_increase_requests` are paginated with an **opaque cursor**. The first request returns up to `limit` rows plus a `next_page` cursor. Pass that cursor unchanged as the `page` parameter on the next request, and repeat until `next_page` is `null`.

**Important:** Don’t change query parameters mid-sequence. Cursors are bound to the filters that issued them. If you change `user_ids[]`, `status[]`, or `actor_ids[]` and pass an old cursor, you'll get a 400 with "cursor does not match current query parameters". Start a new sequence from the first page instead.

Treat the cursor string as opaque: don't parse, modify, or construct it yourself.

## Serializing list parameters

List parameters use bracket notation: repeat the parameter name with `[]` for each value.

    user_ids[]=user_01AbCdEfGh&user_ids[]=user_01JkLmNoPq

## Error responses

[TABLE]

Error bodies have the shape:

    {"type": "error", "error": {"type": "<error_type>", "message": "..."}, "request_id": "req_..."}

`error.type` is a status-dependent discriminator: `invalid_request_error` (400), `authentication_error` (401), `permission_error` (403), `not_found_error` (404), `rate_limit_error` (429), `api_error` (500). `request_id` is always present and is the value to quote when contacting support. The Validations table under each endpoint lists the specific messages.

------------------------------------------------------------------------

## Concepts

### The spend limit hierarchy

Each member's usage credit spending is capped by an **effective spend limit**, resolved from a hierarchy of scope levels. When a member has no per-user override, they inherit the limit configured for their seat tier, their group (if your organization uses group-based limits), or the organization-wide default.

Reading `GET /v1/organizations/spend_limits/effective` returns every current member with their resolved effective limit, where that limit was resolved from (`source`), and their period-to-date spend. Setting a per-user override via `POST /v1/organizations/spend_limits` pins a member to a specific limit regardless of what they would otherwise inherit. Deleting the override returns them to the inherited limit.

### Scope

A scope identifies the level a spend limit is written or resolved at:

[TABLE]

`scope.type` is an open string. Clients should treat unknown values as opaque and fall through rather than fail. Additional scope types may be added in future.

### Period

`period` is the recurring window over which the limit is enforced and spend resets. The only value today is `"monthly"`.

`period` is an open string. Clients should treat unknown values as opaque and fall through rather than fail. Additional period values may be added in the future.

### Amounts and currency

All monetary values are strings in **minor units of the organization's billing currency** (cents, for USD). For example, `"50000"` represents 500.00 USD. Parse as a decimal and divide by 100 to display dollars. Avoid binary floating-point for large values.

`amount` is **nullable**: `null` means **unlimited** (no limit). `"0"` means usage credits are **disabled** for that member.

`period_to_date_spend` is the member's usage credit accrued since the start of the current `period`, in the same minor-unit format. It may include a fractional part (for example, `"41280.125"`).

### Increase request lifecycle

A **spend limit increase request** is created when a member clicks "request more usage" in claude.ai. Requests are not created via this API.

[TABLE]

Both `approved` and `denied` are terminal. A member has at most one `pending` request at a time.

Approving via `POST …/approve` writes the same per-user spend limit row that `POST /v1/organizations/spend_limits` writes. Setting a spend limit directly does *not* transition a pending request. Use the approve endpoint to resolve a request.

By default, Anthropic emails the member when their request is approved or denied. Pass `suppress_notification: true` on approve or deny to suppress that email (for example, when your own system notifies the member).

------------------------------------------------------------------------

## The SpendLimit object

A configured limit at one scope level.

    {
      "type": "spend_limit",
      "id": "spl_01AbCdEfGhIjKlMnOpQrSt",
      "created_at": "2026-05-01T12:00:00Z",
      "updated_at": "2026-05-03T09:14:11Z",
      "scope": { "type": "user", "user_id": "user_01AbCdEfGh" },
      "amount": "50000",
      "currency": "USD",
      "period": "monthly"
    }

[TABLE]

## The SpendSummary object

A computed per-member report row: the member's effective limit, where it came from, and their period-to-date spend. Not an addressable resource (no `id`).

    {
      "scope": { "type": "user", "user_id": "user_01AbCdEfGh" },
      "amount": "50000",
      "currency": "USD",
      "period": "monthly",
      "source": { "type": "seat_tier", "seat_tier": "enterprise_standard" },
      "spend_limit_id": "spl_01XyZaBcDeFgHiJkLmNoPq",
      "period_to_date_spend": "31402.5"
    }

[TABLE]

## The SpendLimitIncreaseRequest object

    {
      "type": "spend_limit_increase_request",
      "id": "slir_01AbCdEfGhIjKlMnOpQrSt",
      "created_at": "2026-05-04T16:22:09Z",
      "status": "pending",
      "resolved_at": null,
      "resolved_by": null,
      "actor": {
        "type": "user_actor",
        "user_id": "user_01AbCdEfGh",
        "name": "Jane Smith",
        "email_address": "[email protected]"
      },
      "spend_summary": {
        "scope": { "type": "user", "user_id": "user_01AbCdEfGh" },
        "amount": "50000",
        "currency": "USD",
        "period": "monthly",
        "source": { "type": "seat_tier", "seat_tier": "enterprise_standard" },
        "spend_limit_id": "spl_01XyZaBcDeFgHiJkLmNoPq",
        "period_to_date_spend": "48900"
      }
    }

[TABLE]

### Actor

[TABLE]

------------------------------------------------------------------------

## Spend limits

### 1. List effective spend limits

    GET /v1/organizations/spend_limits/effective

Returns **every current member** of the organization with their resolved effective limit and period-to-date spend. Members without a per-user override appear with `source.type` of `seat_tier`, `rbac_group`, or `organization`. Ex-members aren’t listed.

Requires scope: `read:spend_limits.`

#### Query parameters

[TABLE]

#### Response fields

[TABLE]

#### Example request

    curl "https://api.anthropic.com/v1/organizations/spend_limits/effective?limit=20" \
      -H "x-api-key: $ANTHROPIC_ADMIN_KEY"

#### Example response

    {
      "data": [
        {
          "scope": { "type": "user", "user_id": "user_01AbCdEfGh" },
          "amount": "50000",
          "currency": "USD",
          "period": "monthly",
          "source": { "type": "seat_tier", "seat_tier": "enterprise_standard" },
          "spend_limit_id": "spl_01XyZaBcDeFgHiJkLmNoPq",
          "period_to_date_spend": "31402.5"
        }
      ],
      "next_page": "page_..."
    }

#### Validations

[TABLE]

------------------------------------------------------------------------

### 2. Get a spend limit

    GET /v1/organizations/spend_limits/{spend_limit_id}

Returns a single spend limit by ID. Use this to inspect the row that a `SpendSummary.spend_limit_id` or a `POST` response referenced.

Requires scope: `read:spend_limits`.

#### Path parameters

[TABLE]

#### Response

A SpendLimit object.

#### Example request

    curl "https://api.anthropic.com/v1/organizations/spend_limits/spl_01AbCdEfGhIjKlMnOpQrSt" \
      -H "x-api-key: $ANTHROPIC_ADMIN_KEY"

#### Validations

[TABLE]

------------------------------------------------------------------------

### 3. Set a spend limit

    POST /v1/organizations/spend_limits

Sets a **per-user** spend limit override. Upsert: setting a limit for a user who already has one overwrites it in place.

Only `scope.type: "user"` is accepted. Seat-tier, group, and organization-level defaults are configured in claude.ai settings.

Setting a spend limit directly does *not* transition a member's pending increase request. Use the approve endpoint to resolve a request.

Requires scope: `write:spend_limits`.

#### Request body

[TABLE]

#### Response

A SpendLimit object reflecting the written override.

#### Example request

    curl -X POST "https://api.anthropic.com/v1/organizations/spend_limits" \
      -H "x-api-key: $ANTHROPIC_ADMIN_KEY" \
      -H "content-type: application/json" \
      -d '{"scope": {"type": "user", "user_id": "user_01AbCdEfGh"}, "amount": "75000"}'

#### Example response

    {
      "type": "spend_limit",
      "id": "spl_01RsTuVwXyZaBcDeFgHiJk",
      "created_at": "2026-05-11T10:02:44Z",
      "updated_at": "2026-05-11T10:02:44Z",
      "scope": { "type": "user", "user_id": "user_01AbCdEfGh" },
      "amount": "75000",
      "currency": "USD",
      "period": "monthly"
    }

#### Validations

[TABLE]

------------------------------------------------------------------------

### 4. Remove a spend limit

    DELETE /v1/organizations/spend_limits/{spend_limit_id}

Removes a **per-user** override so the member falls back to the inherited limit (seat tier, group, or organization default). Seat-tier, group, and organization-level rows can’t be deleted via this endpoint.

Requires scope: `write:spend_limits`.

#### Path parameters

[TABLE]

#### Response

    { "type": "spend_limit_deleted", "id": "spl_01RsTuVwXyZaBcDeFgHiJk" }

#### Example request

    curl -X DELETE "https://api.anthropic.com/v1/organizations/spend_limits/spl_01RsTuVwXyZaBcDeFgHiJk" \
      -H "x-api-key: $ANTHROPIC_ADMIN_KEY"


#### Validations

[TABLE]

------------------------------------------------------------------------

## Spend limit increase requests

### 5. List increase requests

    GET /v1/organizations/spend_limit_increase_requests

Lists increase requests, most recent first. Requests whose requester is no longer a member of the organization are excluded.

Requires scope: `read:spend_limits`.

#### Query parameters

[TABLE]

#### Response fields

[TABLE]

#### Example request

    curl "https://api.anthropic.com/v1/organizations/spend_limit_increase_requests?status[]=pending&limit=50" \
      -H "x-api-key: $ANTHROPIC_ADMIN_KEY"

#### Example response

    {
      "data": [
        {
          "type": "spend_limit_increase_request",
          "id": "slir_01AbCdEfGhIjKlMnOpQrSt",
          "created_at": "2026-05-04T16:22:09Z",
          "status": "pending",
          "resolved_at": null,
          "resolved_by": null,
          "actor": {
            "type": "user_actor",
            "user_id": "user_01AbCdEfGh",
            "name": "Jane Smith",
            "email_address": "[email protected]"
          },
          "spend_summary": {
            "scope": { "type": "user", "user_id": "user_01AbCdEfGh" },
            "amount": "50000",
            "currency": "USD",
            "period": "monthly",
            "source": { "type": "seat_tier", "seat_tier": "enterprise_standard" },
            "spend_limit_id": "spl_01XyZaBcDeFgHiJkLmNoPq",
            "period_to_date_spend": "48900"
          }
        }
      ],
      "next_page": null
    }

#### Validations

[TABLE]

------------------------------------------------------------------------

### 6. Get an increase request

    GET /v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}

Returns a single increase request.

Requires scope: `read:spend_limits`.

#### Path parameters

[TABLE]

#### Response

A SpendLimitIncreaseRequest object.

#### Example request

    curl "https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/slir_01AbCdEfGhIjKlMnOpQrSt" \
      -H "x-api-key: $ANTHROPIC_ADMIN_KEY"

#### Validations

[TABLE]

------------------------------------------------------------------------

### 7. Approve an increase request

    POST /v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve

Approves a pending request. Writes a **per-user spend limit** at `amount` for the requester and transitions the request to `approved`. The request doesn’t carry a requested amount, the admin supplies the new limit on approval.

Requires scope: `write:spend_limits`.

#### Path parameters

[TABLE]

#### Request body

[TABLE]

#### Response

The SpendLimitIncreaseRequest in status `approved`, with an additional `spend_limit` field containing the SpendLimit that was written.

#### Example request

    curl -X POST "https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/slir_01AbCdEfGhIjKlMnOpQrSt/approve" \
      -H "x-api-key: $ANTHROPIC_ADMIN_KEY" \
      -H "content-type: application/json" \
      -d '{"amount": "75000", "suppress_notification": true}'

#### Example response

    {
      "type": "spend_limit_increase_request",
      "id": "slir_01AbCdEfGhIjKlMnOpQrSt",
      "created_at": "2026-05-04T16:22:09Z",
      "status": "approved",
      "resolved_at": "2026-05-11T10:05:02Z",
      "resolved_by": {
        "type": "scoped_api_key_actor",
        "scoped_api_key_id": "apikey_01ZyXwVuTsRqPoNmLkJiHg"
      },
      "actor": {
        "type": "user_actor",
        "user_id": "user_01AbCdEfGh",
        "name": "Jane Smith",
        "email_address": "[email protected]"
      },
      "spend_summary": null,
      "spend_limit": {
        "type": "spend_limit",
        "id": "spl_01RsTuVwXyZaBcDeFgHiJk",
        "created_at": "2026-05-11T10:05:02Z",
        "updated_at": "2026-05-11T10:05:02Z",
        "scope": { "type": "user", "user_id": "user_01AbCdEfGh" },
        "amount": "75000",
        "currency": "USD",
        "period": "monthly"
      }
    }

#### Validations

[TABLE]

------------------------------------------------------------------------

### 8. Deny an increase request

    POST /v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny

Denies a pending request. Idempotent on `denied`: denying an already-denied request returns 200 with the existing resource. Denying an already-approved request is rejected so automation can distinguish a retry from a conflicting decision.

Requires scope: `write:spend_limits`.

#### Path parameters

[TABLE]

#### Request body

[TABLE]

#### Response

A SpendLimitIncreaseRequest in status denied.

#### Example request

    curl -X POST "https://api.anthropic.com/v1/organizations/spend_limit_increase_requests/slir_01AbCdEfGhIjKlMnOpQrSt/deny" \
      -H "x-api-key: $ANTHROPIC_ADMIN_KEY" \
      -H "content-type: application/json" \
      -d '{"suppress_notification": true}'

#### Validations

[TABLE]
