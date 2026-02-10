---
category: "13-Enterprise-Admin"
source_url: "https://support.claude.com/en/articles/13198485-enforce-network-level-access-control-with-tenant-restrictions"
---


Tenant Restrictions are available for members of Enterprise plans and Console organizations.

Tenant Restrictions enable IT administrators on Enterprise plans to enforce network-level access control for Claude. This feature ensures that users on corporate networks can only access approved organizational accounts, preventing unauthorized use of personal accounts.

 

How It Works

When enabled, your network proxy injects an HTTP header into requests to Claude. Anthropic validates this header and blocks access from any organization not in the allowed list.

 

Supported Authentication Methods:

Web access (claude.ai)

Desktop / App Access

API key authentication

OAuth token authentication

 

Header Format
anthropic-allowed-org-ids: <org-uuid-1>,<org-uuid-2>,...

Comma-delimited list of organization UUIDs

No spaces between values

Example:

anthropic-allowed-org-ids: 550e8400-e29b-41d4-a716-446655440000,6ba7b810-
9dad-11d1-80b4-00c04fd430c8

 

Configuration Steps
1. Find Your Organization UUID

Members of Enterprise plans can find this in two different places:

Navigate to Settings > Account and find Organization ID.

Navigate to Admin settings > Organization and scroll down to the bottom of the page to locate Organization ID.

Members of Console organizations can find this in Settings > Organization.

 

2. Configure Your Network Proxy

Configure your proxy to inject the header for Claude traffic:

Rule: Claude Tenant Restriction
Application: claude.ai, api.anthropic.com
Action: Inject Header
Header Name: anthropic-allowed-org-ids
Header Value: 
TLS Inspection: Required

 

3. Test Your Configuration

From restricted network, test with your org's API key:

curl https://api.anthropic.com/v1/messages \
 -H "x-api-key: $CLAUDE_API_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -H "content-type: application/json" \
 -d '{"model":"claude-sonnet-4-20250514","max_tokens":1024,"messages":
 [{"role":"user","content":"Hello"}]}'

 

Error Response

When access is blocked, users receive the following error:

{
 "type": "error",
 "error": {
 "type": "permission_error",
 "message": "Access restricted by network policy. Contact IT Administrator.",
 "error_code": "tenant_restriction_violation"
 }
}

 

Supported Proxy Platforms

Zscaler ZIA (Cloud App Control policies)

Palo Alto Prisma Access (SaaS App Management)

Cato Networks (Tenant Restriction policy)

Netskope (Header Insertion rules)

Generic HTTPS proxies with header injection capability

 

Use Cases

Scenario

 

Header Value

Single Organization

 

<your-org-uuid>

Multiple Organizations (Partners)

 

<org-uuid-1>,<org-uuid-2>

 

Security Benefits

Data Loss Prevention: Block personal account usage from corporate networks.

Compliance: Enforce data residency and access policies.

Shadow IT Control: Prevent unauthorized Claude usage.

Audit Trail: Complete visibility into access attempts.

 

Backward Compatibility

No impact to networks without tenant restrictions configured.

Standard authentication continues for unmanaged networks.

Existing API key authentication remains unchanged.

Related Articles
Does Anthropic Act as a Data Processor or Controller?
Claude Code FAQ
Microsoft 365 Connector: Security Guide
Restrict access to Claude with IP allowlisting
Cowork for Team and Enterprise plans