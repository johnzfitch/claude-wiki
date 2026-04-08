# Claude Code Enterprise Architecture — System Interconnections

**Date**: 2026-03-13
**Visual Reference**: How all enterprise systems connect together

---

## High-Level Enterprise Platform Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ORGANIZATION MANAGEMENT LAYER                         │
│                                                                              │
│  ┌──────────────────┐    ┌──────────────────┐    ┌────────────────────┐   │
│  │  Organization    │    │   Seat Tiers     │    │  Member Accounts   │   │
│  │  UUID: org-123   │───▶│  - Free          │───▶│  user@example.com  │   │
│  │  Name: "Acme"    │    │  - Pro           │    │  Role: admin       │   │
│  │  Type: Enterprise│    │  - Max           │    │  Credits: 10000    │   │
│  └──────────────────┘    │  - Enterprise    │    └────────────────────┘   │
│                          └──────────────────┘                               │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                    ┌──────────────────┼──────────────────┐
                    │                  │                  │
                    ▼                  ▼                  ▼
┌────────────────────────┐ ┌──────────────────┐ ┌─────────────────────┐
│   BILLING & CREDITS    │ │  ACCESS CONTROL  │ │  ENTERPRISE INFRA   │
│                        │ │                  │ │                     │
│  Credit Balance        │ │  Permission      │ │  Provider Routing   │
│  Overage Tracking      │ │  Checks (4-tier) │ │  - AWS Bedrock      │
│  Usage Limits          │ │  - Org level     │ │  - Google Vertex    │
│  Admin Requests        │ │  - Seat level    │ │  - MS Foundry       │
│  - limit_increase      │ │  - Member level  │ │                     │
│                        │ │  - Service level │ │  Unix Socket Mode   │
│  Referral Campaigns    │ │                  │ │  Policy Enforcement │
│  - Guest passes        │ │  Role System     │ │  Plugin Management  │
└────────────────────────┘ │  - user          │ └─────────────────────┘
            │              │  - admin         │              │
            │              └──────────────────┘              │
            │                       │                        │
            └───────────────────────┼────────────────────────┘
                                    │
                                    ▼
                    ┌────────────────────────────────┐
                    │     RUNTIME ENFORCEMENT        │
                    │                                │
                    │  - Fast mode enable/disable    │
                    │  - Feature gating              │
                    │  - Usage telemetry             │
                    │  - Audit logging               │
                    └────────────────────────────────┘
```

---

## Credit & Overage System Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      CREDIT ALLOCATION HIERARCHY                         │
└─────────────────────────────────────────────────────────────────────────┘

    ┌──────────────────────────────────────────────────┐
    │         Organization Credit Pool                 │
    │         - Total allocated: 100,000               │
    │         - org_service_zero_credit_limit          │
    └──────────────────┬───────────────────────────────┘
                       │
         ┌─────────────┴─────────────┬─────────────────┐
         │                           │                 │
         ▼                           ▼                 ▼
┌────────────────┐          ┌────────────────┐  ┌──────────────┐
│   Seat Tier 1  │          │   Seat Tier 2  │  │  Seat Tier N │
│   (Pro)        │          │   (Enterprise) │  │  (Free)      │
│   Limit: 5,000 │          │   Limit: 25k   │  │  Limit: 500  │
│   ──────────── │          │   ──────────── │  │  ────────────│
│   seat_tier_   │          │   seat_tier_   │  │  seat_tier_  │
│   zero_credit_ │          │   zero_credit_ │  │  zero_credit_│
│   limit        │          │   limit        │  │  limit       │
└────────┬───────┘          └────────┬───────┘  └──────┬───────┘
         │                           │                 │
    ┌────┴────┬─────┐           ┌────┴────┐       ┌────┴────┐
    │         │     │           │         │       │         │
    ▼         ▼     ▼           ▼         ▼       ▼         ▼
┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
│Member│ │Member│ │Member│ │Member│ │Member│ │Member│ │Member│
│ user1│ │ user2│ │ user3│ │ user4│ │ user5│ │ user6│ │ user7│
│──────│ │──────│ │──────│ │──────│ │──────│ │──────│ │──────│
│member│ │member│ │member│ │member│ │member│ │member│ │member│
│_zero │ │_zero │ │_zero │ │_zero │ │_zero │ │_zero │ │_zero │
│_cred │ │_cred │ │_cred │ │_cred │ │_cred │ │_cred │ │_cred │
│it_   │ │it_   │ │it_   │ │it_   │ │it_   │ │it_   │ │it_   │
│limit │ │limit │ │limit │ │limit │ │limit │ │limit │ │limit │
└──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                        OVERAGE HANDLING                                 │
└─────────────────────────────────────────────────────────────────────────┘

Member usage flow:

1. Normal usage (within limit)
   │
   ├─ Credits deducted from member allocation
   │
   ▼
2. Limit reached → Switch to overage mode
   │
   ├─ isUsingOverage = true
   ├─ Charges against overage pool
   ├─ User notified: "Using extra usage"
   │
   ▼
3. Overage pool exhausted
   │
   ├─ overageDisabledReason = "out_of_credits"
   ├─ Fast mode disabled
   ├─ User sees: "You're out of extra usage · resets <time>"
   │
   ▼
4. Admin intervention
   │
   ├─ User requests: POST /admin_requests {type: "limit_increase"}
   ├─ Admin approves via dashboard
   ├─ Credits replenished
   │
   ▼
5. Back to normal usage
```

---

## Permission Check Flow (4-Tier System)

```
User attempts to use Fast Mode
│
├─ Check 1: Organization Level
│   │
│   ├─ Is feature org_level_disabled? ──────────────────────┐
│   ├─ Is feature org_level_disabled_until <timestamp>? ────┤
│   ├─ Is org_service_level_disabled? ──────────────────────┤
│   └─ Is org_service_zero_credit_limit? ───────────────────┤
│                                                           │
├─ Check 2: Seat Tier Level                                 │
│   │                                                       │
│   ├─ Does seat tier include Fast Mode?                    │
│   ├─ Is seat_tier_level_disabled? ────────────────────────┤
│   └─ Is seat_tier_zero_credit_limit? ─────────────────────┤
│                                                           │
├─ Check 3: Member Level                                    │
│   │                                                       │
│   ├─ Is user member_level_disabled? ───────────────────────┤
│   └─ Is member_zero_credit_limit? ────────────────────────┤
│                                                           │
├─ Check 4: Service Level (runtime)                         │
│   │                                                       │
│   ├─ Network connectivity OK?                             │
│   ├─ Not using enterprise provider (Bedrock/Vertex)?      │
│   └─ Not in Agent SDK mode?                               │
│                                                           │
▼                                                            ▼
✅ ALLOW                                                    ❌ DENY
Fast Mode enabled                                          Show reason:
                                                           - "extra usage disabled"
                                                           - "not available on <provider>"
                                                           - "network issues"
```

---

## Admin Request Workflow

```
┌──────────────────────────────────────────────────────────────────────┐
│                     LIMIT INCREASE REQUEST FLOW                      │
└──────────────────────────────────────────────────────────────────────┘

User (member_zero_credit_limit)
    │
    ├─ 1. Check Eligibility
    │     GET /api/oauth/organizations/{orgId}/admin_requests/eligibility
    │     ?request_type=limit_increase
    │
    ▼
  ┌──────────────┐
  │  Eligible?   │
  └───┬──────────┘
      │ YES
      ▼
    ┌─────────────────────┐
    │ 2. Submit Request   │
    │ POST /admin_requests│
    │ {                   │
    │   request_type:     │
    │   "limit_increase", │
    │   details: {...}    │
    │ }                   │
    └──────┬──────────────┘
           │
           │ Request ID: req-abc123
           │
           ▼
    ┌──────────────────────────┐
    │  3. Admin Dashboard      │
    │  https://claude.ai/      │
    │  admin-settings/usage    │
    │                          │
    │  Pending Requests:       │
    │  ┌────────────────────┐ │
    │  │ user@example.com   │ │
    │  │ Requested: +5000   │ │
    │  │ Current: 1000      │ │
    │  │ [Approve] [Deny]   │ │
    │  └────────────────────┘ │
    └──────┬───────────────────┘
           │
           │ Admin approves
           │
           ▼
    ┌──────────────────────┐
    │ 4. Limit Updated     │
    │ member_credit_limit  │
    │ 1000 → 6000          │
    └──────┬───────────────┘
           │
           ▼
    User notified via UI:
    "Your limit increase was approved"
```

---

## Enterprise Provider Routing

```
┌──────────────────────────────────────────────────────────────────────┐
│                   ENTERPRISE PROVIDER SELECTION                      │
└──────────────────────────────────────────────────────────────────────┘

Organization configuration:
  └─ enterpriseProvider: "bedrock" | "vertex" | "foundry" | null

┌───────────────┐
│  User Request │
│  (Sonnet 4.6) │
└───────┬───────┘
        │
        ├─ Check org enterpriseProvider
        │
        ▼
┌─────────────────────────────────────────────────────┐
│              Provider Routing Decision              │
├─────────────────────────────────────────────────────┤
│                                                     │
│  IF CLAUDE_CODE_USE_BEDROCK=1:                      │
│    └─ Route to AWS Bedrock                          │
│       - Model: "anthropic.claude-sonnet-4-6-v1"     │
│       - Auth: IAM or AWS_BEARER_TOKEN_BEDROCK       │
│       - Fast mode: DISABLED                         │
│                                                     │
│  ELSE IF CLAUDE_CODE_USE_VERTEX=1:                  │
│    └─ Route to Google Vertex AI                     │
│       - Model: "claude-sonnet-4-6@20260311"         │
│       - Auth: Application Default Credentials       │
│       - Fast mode: DISABLED                         │
│                                                     │
│  ELSE IF CLAUDE_CODE_USE_FOUNDRY=1:                 │
│    └─ Route to Microsoft Foundry                    │
│       - Model: "claude-sonnet-4-6"                  │
│       - Auth: Azure AD or ANTHROPIC_FOUNDRY_API_KEY │
│       - Fast mode: DISABLED                         │
│                                                     │
│  ELSE:                                              │
│    └─ Route to Anthropic (first-party)              │
│       - Model: "claude-sonnet-4-6"                  │
│       - Auth: ANTHROPIC_API_KEY or OAuth            │
│       - Fast mode: ENABLED (if credits allow)       │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## Unix Socket Proxy Architecture (Zero-Trust Mode)

```
┌──────────────────────────────────────────────────────────────────────┐
│                  UNIX SOCKET ENTERPRISE PROXY                        │
│                   (Added in 2.1.74)                                  │
└──────────────────────────────────────────────────────────────────────┘

Enterprise Environment:

  ┌───────────────────────────────────────────────────────┐
  │  Corporate Network (kubernetes/docker)                │
  │                                                       │
  │  ┌───────────────────────────────────────────────┐    │
  │  │  Pod: claude-code-worker                      │    │
  │  │                                               │    │
  │  │  Environment:                                 │    │
  │  │  ❌ ANTHROPIC_API_KEY=<not set>               │    │
  │  │  ❌ AWS_ACCESS_KEY_ID=<stripped>              │    │
  │  │  ✅ ANTHROPIC_UNIX_SOCKET=/run/claude.sock    │    │
  │  │  ✅ CLAUDE_CODE_OAUTH_TOKEN=<token>           │    │
  │  │                                               │    │
  │  │  ┌──────────────────────────────────┐         │    │
  │  │  │  Claude Code Process             │         │    │
  │  │  │  (restricted subprocess)         │         │    │
  │  │  │                                  │         │    │
  │  │  │  ✓ All creds stripped from env  │          │    │
  │  │  │  ✓ OAuth-only auth enforced     │          │    │
  │  │  │  ✓ Connects via socket only     │          │    │
  │  │  └──────────────┬───────────────────┘         │    │
  │  │                 │                             │    │
  │  │                 │ Unix Socket                 │    │
  │  │                 │ /run/claude.sock            │    │
  │  │                 ▼                             │    │
  │  │  ┌───────────────────────────────────────┐    │    │
  │  │  │  Auth Proxy Sidecar                   │    │    │
  │  │  │  (managed by IT)                      │    │    │
  │  │  │                                       │    │    │
  │  │  │  ✅ Validates OAuth token             │    │    │
  │  │  │  ✅ Injects org-level credentials     │    │    │
  │  │  │  ✅ Logs all API calls                │    │    │
  │  │  │  ✅ Enforces rate limits              │    │    │
  │  │  │  ✅ Routes to enterprise provider     │    │    │
  │  │  └───────────────┬───────────────────────┘    │    │
  │  │                  │                            │    │
  │  └──────────────────┼────────────────────────────┘    │
  │                     │ HTTPS                           │
  └─────────────────────┼─────────────────────────────────┘
                        │
                        ▼
            ┌────────────────────────┐
            │  Anthropic API         │
            │  (or Bedrock/Vertex)   │
            └────────────────────────┘

Benefits:
  ✅ Zero-trust: Worker process cannot access credentials
  ✅ Auditability: All API calls logged at proxy level
  ✅ Multi-tenant isolation: Per-org credentials at proxy
  ✅ Simplified rotation: Creds managed centrally
  ✅ Compliance: Proxy can enforce PII filtering
```

---

## Policy & Plugin Management

```
┌──────────────────────────────────────────────────────────────────────┐
│               ENTERPRISE PLUGIN & POLICY ENFORCEMENT                  │
└──────────────────────────────────────────────────────────────────────┘

Organization Admin configures:

  ┌────────────────────────────────────────────────────┐
  │  /nfs/corporate/claude-plugins/                    │
  │  (CLAUDE_CODE_PLUGIN_SEED_DIR)                     │
  │                                                    │
  │  ├── cache/                                        │
  │  │   └── corporate-internal/                       │
  │  │       ├── security-scanner/1.0.0/               │
  │  │       │   ├── package.json                      │
  │  │       │   ├── plugin.json                       │
  │  │       │   └── mcp-server/                       │
  │  │       └── compliance-agent/2.1.0/               │
  │  │                                                 │
  │  └── known_marketplaces.json                       │
  │      {                                             │
  │        "corporate-internal": {                     │
  │          "source": "https://plugins.corp.com",     │
  │          "readonly": true                          │
  │        }                                           │
  │      }                                             │
  └────────────────────────────────────────────────────┘

User's settings.json:

  {
    "policySettings": {
      "strictKnownMarketplaces": ["corporate-internal"],
      "blockedMarketplaces": ["community-untrusted"],
      "managedPlugins": {
        "security-scanner": {
          "version": "1.0.0",
          "enabled": true,
          "__readonly": true  // User cannot disable
        }
      }
    },
    "enabledPlugins": {
      "security-scanner": true,  // Locked by policy
      "my-personal-plugin": false // User can control
    }
  }

Runtime enforcement:

  User tries: `claude plugin disable security-scanner`
  │
  ├─ Check if plugin is in managedPlugins
  │  └─ YES
  │
  ├─ Error: "Plugin 'security-scanner' is managed by policy and cannot be disabled"
  │
  └─ Operation blocked

  User tries: `claude plugin marketplace add malicious --source evil.com`
  │
  ├─ Check strictKnownMarketplaces
  │  └─ "evil.com" not in allowlist
  │
  ├─ Error: "Marketplace source blocked by enterprise policy"
  │
  └─ Operation blocked
```

---

## Data Flow Summary

```
┌─────────────────────────────────────────────────────────────────────┐
│          COMPLETE ENTERPRISE DATA FLOW                              │
└─────────────────────────────────────────────────────────────────────┘

1. User Authentication
   └─ OAuth → organizationUuid + accessToken + role

2. Session Initialization
   ├─ Load org settings from API
   ├─ Check seat tier assignment
   ├─ Fetch credit balance & limits
   └─ Apply managed settings (if enterprise tier)

3. Feature Gate Check (e.g., Fast Mode)
   ├─ Org level: Is feature enabled for org?
   ├─ Seat level: Does tier include feature?
   ├─ Member level: User's credit balance OK?
   └─ Service level: Runtime constraints (network, provider)

4. API Request
   ├─ Route to provider (first-party / Bedrock / Vertex / Foundry)
   ├─ Deduct credits from member balance
   ├─ Track usage for billing
   └─ Emit telemetry (if metrics_enabled)

5. Credit Exhaustion
   ├─ Switch to overage mode
   ├─ User sees warning
   └─ If overage exhausted → disable features

6. Admin Request
   ├─ User requests limit increase
   ├─ Admin reviews in dashboard
   └─ Approval → credits replenished

7. Audit & Compliance
   ├─ All API calls logged (if unix socket mode)
   ├─ Usage data sent to org admin dashboard
   └─ Periodic reports for billing
```

---

## Key Integration Points

| System | Integrates With | Data Exchanged |
|--------|----------------|----------------|
| **Billing** | Credit system, Overage tracking, Admin requests | Credit balance, usage metrics, limit changes |
| **Access Control** | Org settings, Seat tiers, Member roles | Permission states, feature flags |
| **Enterprise Providers** | Org config, Unix socket proxy | Provider selection, credential routing |
| **Plugin Management** | Policy enforcement, Seed directory | Allowed marketplaces, managed plugins |
| **Telemetry** | Org metrics toggle, Usage tracking | Event streams, audit logs |
| **Admin Dashboard** | All systems | Consolidated view, approval workflows |

---

## Conclusion

Claude Code 2.1.74 implements a **fully-integrated enterprise SaaS architecture** with:

- ✅ **Multi-tenancy** at org/seat/member levels
- ✅ **Fine-grained access control** (4-tier permission checks)
- ✅ **Production billing system** (credits, overage, admin approval)
- ✅ **Enterprise-grade security** (Unix socket proxy, OAuth-only mode)
- ✅ **Policy governance** (plugin management, managed settings)
- ✅ **Scalable provider routing** (Bedrock, Vertex, Foundry)

All systems work together to provide **enterprise-ready Claude Code** for large organizations.
