# Claude Code Enterprise Systems — Complete Architecture

**Date**: 2026-03-13
**Binary**: 2.1.74
**Analysis**: Complete enterprise feature mapping from binary reverse engineering

---

## Executive Summary

Claude Code 2.1.74 contains a **complete enterprise SaaS platform** with:
- **Organization & Workspace Management** — Multi-tenant architecture with org-level settings
- **Seat-Based Licensing** — Tiered seat system with credit limits per tier
- **Admin Request Workflow** — Self-service limit increase requests with approval flow
- **Usage Tracking & Billing** — Per-org metrics, credit balance, overage management
- **Access Control** — Role-based restrictions, org/seat/member level disabling
- **Referral/Guest Pass System** — Org-level referral campaigns for user acquisition
- **Enterprise Provider Support** — Foundry, Bedrock, Vertex AI with org-specific routing
- **Policy Management** — Plugin marketplaces, managed settings, allowlists/blocklists

---

## 1. Organization & Workspace Architecture

### Data Model

```typescript
// Organization structure (inferred from API calls)
interface Organization {
  organizationUuid: string;        // Primary org identifier
  organizationName?: string;
  accountUuid: string;             // Associated account
  subscriptionType: "free" | "pro" | "max" | "enterprise";

  // Metadata
  deviceId: string;
  sessionId: string;
  email: string;
  appVersion: {
    VERSION: "2.1.74";
    BUILD_TIME: "2026-03-11T23:30:59Z";
    // ...
  };
}
```

### API Endpoints

| Endpoint | Purpose | Auth Required |
|----------|---------|---------------|
| `GET /api/oauth/profile` | Get user profile with org data | Bearer token |
| `GET /api/claude_code/organizations/metrics_enabled` | Check if org has metrics enabled | Bearer token |
| `GET /api/oauth/organizations/${orgId}/admin_requests/me?request_type=${type}&statuses=${status}` | List user's admin requests | Bearer + orgUUID |
| `GET /api/oauth/organizations/${orgId}/admin_requests/eligibility?request_type=${type}` | Check if user can request admin action | Bearer + orgUUID |
| `POST /api/oauth/organizations/${orgId}/admin_requests` | Submit admin request | Bearer + orgUUID |
| `GET /api/oauth/organizations/${orgId}/referral/eligibility?campaign=${name}` | Check referral program eligibility | Bearer + orgUUID |
| `GET /api/oauth/organizations/${orgId}/referral/redemptions?campaign=${name}` | Get referral redemption data | Bearer + orgUUID |

### Environment Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `CLAUDE_CODE_ORG` | Override organization ID | `org-123abc` |
| `forceLoginOrgUUID` | Force login to specific org (seen in config schema) | `uuid-string` |

---

## 2. Seat-Based Licensing & Credit System

### Seat Tiers

Claude Code uses a hierarchical licensing model with **seat tiers** that determine feature access and credit limits.

```
Organization Level
  ├─ Seat Tier Level (e.g., Pro, Enterprise)
  │   ├─ Member Level (individual user)
  │   └─ Group Level (team/department)
  └─ Service Level (org-wide service quota)
```

### Disabled Reasons Enum

Complete set of reasons why features (like fast mode) can be disabled:

| Reason Code | Level | Meaning |
|-------------|-------|---------|
| `org_level_disabled` | Organization | Org admin disabled the feature |
| `org_level_disabled_until` | Organization | Temporary org-level disable (time-bound) |
| `org_service_level_disabled` | Organization | Service tier doesn't include feature |
| `org_service_zero_credit_limit` | Organization | Org has no credits remaining |
| `seat_tier_level_disabled` | Seat Tier | Seat tier doesn't include feature |
| `seat_tier_zero_credit_limit` | Seat Tier | Seat tier out of credits |
| `member_level_disabled` | Member | Individual user disabled |
| `member_zero_credit_limit` | Member | User's personal credit limit reached |
| `group_zero_credit_limit` | Group | Team/group out of credits |
| `out_of_credits` | Any | Generic out-of-credits state |
| `no_limits_configured` | System | No usage limits set up |
| `unknown` | System | Unknown/error state |

### Credit/Overage System

```typescript
// Overage structure (inferred from usage)
interface OverageState {
  overageDisabledReason: DisabledReason;  // One of the enums above
  isUsingOverage: boolean;                // User is in overage mode
  surpassedLimit?: boolean;               // Exceeded hard limit
  resetTime?: string;                     // When credits reset (daily/monthly)

  // Overage fields found
  OverageMode: string;
  OverageProvisioningAllowed: boolean;
  overageStatus: "overage_disabled_reason" | "overage_not_provisioned" | "active";
  overageResetsAt: string;                // ISO timestamp
}
```

**Error Messages**:
- `"Your credit balance is too low"` → Triggers billing error flow
- `"You're out of extra usage"` → Shown when `overageDisabledReason === "out_of_credits"`
- `"Fast mode disabled · extra usage not available"` → Generic fast mode restriction
- `"Fast mode disabled · extra usage disabled for your account"` → Seat tier restriction

**Fast Mode Restrictions**:
Fast mode is disabled when:
1. Using Bedrock, Vertex, or Foundry (enterprise providers)
2. `overageDisabledReason` is one of: `org_level_disabled`, `org_level_disabled_until`, `out_of_credits`, `seat_tier_level_disabled`, `member_level_disabled`, `seat_tier_zero_credit_limit`, `member_zero_credit_limit`
3. Network connectivity issues
4. Using Agent SDK (programmatic access)

---

## 3. Admin Request System

### Request Types

Currently supported:
- `limit_increase` — Request higher usage limits

### Workflow

```
User → Check Eligibility
         ↓ (eligible)
       Submit Request → Admin Review
                          ↓ (approved)
                        Limit Increased
```

**API Flow**:
```typescript
// 1. Check if user can request limit increase
const eligible = await GET(`/api/oauth/organizations/${orgId}/admin_requests/eligibility?request_type=limit_increase`);

// 2. Submit request
await POST(`/api/oauth/organizations/${orgId}/admin_requests`, {
  request_type: "limit_increase",
  details: null  // or custom justification
});

// 3. Check status
const requests = await GET(`/api/oauth/organizations/${orgId}/admin_requests/me?request_type=limit_increase&statuses=pending,approved,denied`);
```

**Error Handling**:
- If limit increase submitted → Shows message: `"Request sent! Ask your org admin to approve it."`
- Auto-retries with exponential backoff on 401/403
- Falls back to generic error on billing issues

---

## 4. Usage Tracking & Telemetry

### Organization Metrics

| Endpoint | Data Collected |
|----------|----------------|
| `GET /api/oauth/usage` | User-level usage stats (5s timeout) |
| `GET /api/claude_code/organizations/metrics_enabled` | Whether org has metrics collection enabled |

**Tracked Data** (from telemetry event names):
- `tengu_oauth_role` — User's OAuth role within organization
- Organization-level feature flag states
- Per-org metrics collection toggle

### Admin Dashboard

Reference found in URLs:
- `https://claude.ai/admin-settings/usage` — Organization admin usage dashboard

---

## 5. Referral & Guest Pass System

### Purpose
Organizations can run referral campaigns to invite new users with promotional credits/access.

### API

```typescript
// Check if org is eligible for a campaign
const eligible = await GET(`/api/oauth/organizations/${orgId}/referral/eligibility?campaign=claude_code_guest_pass`);

// Get redemption data
const redemptions = await GET(`/api/oauth/organizations/${orgId}/referral/redemptions?campaign=claude_code_guest_pass`);
```

**Known Campaigns**:
- `claude_code_guest_pass` — Default guest pass campaign

**Eligibility Requirements** (from code):
```typescript
function isEligibleForReferral() {
  return !!(
    userHasOrganizationUuid() &&
    hasCLIAccess() &&
    subscriptionType() === "max"  // Requires Claude Max subscription
  );
}
```

---

## 6. Access Control & Permissions

### Role System

**Evidence**:
- `tengu_oauth_role` telemetry event
- `/api/oauth/claude_cli/roles` endpoint
- Role-based API key creation: `/api/oauth/claude_cli/create_api_key`

**Inferred Roles**:
- `user` — Standard member
- `admin` — Organization administrator (can approve admin_requests)
- Unknown additional roles (enterprise tier may have more)

### Permission Checks

The system checks permissions at multiple levels:
1. **Organization level** — Can org use feature at all?
2. **Seat tier level** — Does this tier include the feature?
3. **Member level** — Is this specific user allowed?
4. **Service level** — Does the service plan support it?

---

## 7. Enterprise Provider Integration

### Supported Providers

| Provider | Env Var | Organization Routing |
|----------|---------|----------------------|
| Anthropic (First-Party) | `ANTHROPIC_API_KEY` | Default |
| AWS Bedrock | `CLAUDE_CODE_USE_BEDROCK=1` | Enterprise tier |
| Google Vertex AI | `CLAUDE_CODE_USE_VERTEX=1` | Enterprise tier |
| Microsoft Foundry | `CLAUDE_CODE_USE_FOUNDRY=1` | Enterprise tier (added 2.1.70) |

**Organization-Level Routing**:
- Enterprise orgs can configure which provider to use org-wide
- Individual users inherit org settings
- Fast mode disabled when using enterprise providers

---

## 8. Policy Management & Governance

### Plugin Marketplace Policies

```json
{
  "policySettings": {
    "strictKnownMarketplaces": ["official", "corporate-internal"],
    "blockedMarketplaces": ["untrusted"],
    "managedPlugins": {
      "security-scanner": { "version": "1.0.0", "enabled": true }
    }
  }
}
```

**Enforcement**:
- Seed plugins (`CLAUDE_CODE_PLUGIN_SEED_DIR`) are read-only and policy-locked
- Users cannot disable managed plugins
- Marketplace sources checked against allowlist/blocklist

### Managed Settings

Organizations can enforce settings via:
1. **Seed directory** — Pre-installed plugins at `/nfs/corporate/claude-plugins`
2. **Policy settings** — Locked configuration in `settings.json`
3. **Enterprise env vars** — `CLAUDE_CODE_ORG`, provider routing, etc.

---

## 9. Unix Socket Mode (Enterprise Proxy)

**Added in 2.1.74** — Production-ready sidecar proxy architecture for managed environments.

### Architecture

```
┌─────────────────┐
│  Claude Code    │
│  (Subprocess)   │──ANTHROPIC_UNIX_SOCKET──┐
│                 │                          │
│ ❌ No API keys  │                          ▼
│ ❌ No OAuth tok │              ┌────────────────────┐
│ ✅ Only socket  │              │   Auth Proxy       │
└─────────────────┘              │  /run/claude.sock  │
                                 │                    │
                                 │ ✅ OAuth-only auth │
                                 │ ✅ Org-level creds │
                                 │ ✅ Audit logging   │
                                 └────────────────────┘
                                           │
                                           ▼
                                  Anthropic API
```

**Authentication**:
- `ANTHROPIC_UNIX_SOCKET` set → **OAuth-only mode**
- All credentials stripped from subprocess environment
- API keys, Bedrock, Vertex, Foundry auth bypassed
- Only `CLAUDE_CODE_OAUTH_TOKEN` accepted

**Use Case**: Enterprise deployments where:
- Centralized credential management required
- Audit logging enforced at proxy level
- Multi-tenant isolation needed

---

## 10. Subscription Tiers

### Detected Tiers

| Tier | Identifier | Features |
|------|------------|----------|
| Free | `"free"` | Basic access, strict limits |
| Pro | `"pro"` | Higher limits, basic enterprise features |
| Max | `"max"` | Referral eligibility, extended limits |
| Enterprise | `"enterprise"` | Custom limits, managed settings, enterprise providers |

**Detection** (from code):
```typescript
function currentTier() {
  return process.env.CLAUDE_CODE_SUBSCRIPTION_TYPE || user.subscriptionType || "free";
}
```

---

## 11. Complete Environment Variables (Enterprise-Specific)

| Variable | Purpose | Added |
|----------|---------|-------|
| `CLAUDE_CODE_ORG` | Override organization ID | Unknown |
| `CLAUDE_CODE_USE_BEDROCK` | Enable AWS Bedrock (enterprise) | 2.1.59 |
| `CLAUDE_CODE_USE_VERTEX` | Enable Google Vertex (enterprise) | 2.1.59 |
| `CLAUDE_CODE_USE_FOUNDRY` | Enable Microsoft Foundry (enterprise) | 2.1.70 |
| `ANTHROPIC_UNIX_SOCKET` | Unix socket proxy path (enterprise) | 2.1.74 |
| `CLAUDE_CODE_OAUTH_TOKEN` | OAuth token (required in socket mode) | 2.1.74 |
| `CLAUDE_CODE_PLUGIN_SEED_DIR` | Shared plugin directory (managed) | 2.1.70 |
| `CLAUDE_COWORK_MEMORY_PATH_OVERRIDE` | Team memory sync path | 2.1.70 |
| `CLAUDE_CODE_REMOTE` | Enable remote control mode | 2.1.70 |
| `CLAUDE_CODE_REMOTE_SESSION_ID` | Remote session identifier (multi-tenant) | 2.1.70 |

---

## 12. Integration Points

### Organization Onboarding Flow

```
1. User signs up → Assigned to organization (or creates one)
2. Org gets default seat tier (free/pro/max)
3. Org admin configures:
   - Enterprise provider (Bedrock/Vertex/Foundry)
   - Plugin policies (allowed marketplaces, managed plugins)
   - Usage limits per seat tier
   - Managed settings enforcement
4. Members inherit org settings
5. Usage tracked at org + member level
6. Admin approves limit increase requests
```

### Billing Integration

**Credit Balance Check**:
```typescript
// On tool use or model invocation
if (user.creditBalance < THRESHOLD) {
  throw new Error("Your credit balance is too low");
}

// Auto-redirect to buy credits
window.open("https://claude.ai/buy_credits?returnUrl=/oauth/code/success%3Fapp%3Dclaude-code");
```

**Overage Management**:
- User exceeds limit → `isUsingOverage = true`
- Charges against overage credit pool
- When overage exhausted → `overageDisabledReason = "out_of_credits"`

---

## 13. Open Questions

1. **SCIM/SAML Support** — No evidence found in 2.1.74, but enterprise tier suggests it exists
2. **Audit Logging Format** — Unix socket mode enforces audit logging, but format unclear
3. **Role Granularity** — Only `user`/`admin` roles found; enterprise tier may have more
4. **Workspace vs Organization** — Code mentions both; relationship unclear
5. **Multi-Org Membership** — Can users belong to multiple orgs? API suggests yes (`forceLoginOrgUUID`)

---

## 14. Summary: Enterprise Capabilities Matrix

| Feature | Free | Pro | Max | Enterprise |
|---------|------|-----|-----|------------|
| Organization management | ❌ | ✅ | ✅ | ✅ |
| Seat-based licensing | ❌ | ✅ | ✅ | ✅ |
| Admin request workflow | ❌ | ✅ | ✅ | ✅ |
| Credit limits | ✅ Basic | ✅ Higher | ✅ Extended | ✅ Custom |
| Usage tracking | ❌ | ✅ | ✅ | ✅ Full |
| Referral campaigns | ❌ | ❌ | ✅ | ✅ |
| Enterprise providers (Bedrock/Vertex/Foundry) | ❌ | ❌ | ❌ | ✅ |
| Plugin marketplace policies | ❌ | ❌ | ✅ Basic | ✅ Full |
| Managed settings | ❌ | ❌ | ❌ | ✅ |
| Unix socket proxy mode | ❌ | ❌ | ❌ | ✅ |
| CoWork team memory | ❌ | ❌ | ✅ | ✅ |
| Remote control mode | ❌ | ❌ | ❌ | ✅ |

---

## 15. Key Takeaways

1. **Claude Code is enterprise-ready** — Complete multi-tenant SaaS platform, not just a CLI tool
2. **Tiered licensing is production-grade** — Seat tiers, credit limits, overage management fully implemented
3. **Self-service admin workflows** — Users can request limit increases; admins approve via dashboard
4. **Enterprise provider support is mature** — Bedrock, Vertex, Foundry fully integrated with org-level routing
5. **Policy enforcement is comprehensive** — Plugin marketplaces, managed settings, access control at 4 levels
6. **Unix socket mode is unique** — OAuth-only sidecar proxy for zero-trust enterprise deployments
7. **Referral system drives growth** — Org-level campaigns for viral user acquisition (Max tier+)

The binary contains a **complete B2B SaaS platform** that rivals Slack, GitHub, or Notion in organizational sophistication.
