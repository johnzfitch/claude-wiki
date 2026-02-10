---
category: "99-Other"
fetched_at: "2026-02-10T10:49:32Z"
source_url: "https://support.claude.com/en/articles/12922490-remote-mcp-server-submission-guide"
title: "Remote MCP Server Submission Guide | Claude Help Center"
---

[](/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

Search for articles...

Table of contents

[](#h_33710f89e6)

[](#h_24d55bda64)

[](#h_99ed45ebea)

[](#h_9179e67b9a)

[](#h_1fb976bf24)

[](#h_1b254b8583)

[](#h_7643b8d967)

[All Collections](/en/)

[Connectors](https://support.claude.com/en/collections/15399129-connectors)

Remote MCP Server Submission Guide

# Remote MCP Server Submission Guide

Updated this week

Table of contents

[](#h_33710f89e6)

[](#h_24d55bda64)

[](#h_99ed45ebea)

[](#h_9179e67b9a)

[](#h_1fb976bf24)

[](#h_1b254b8583)

[](#h_7643b8d967)

This is a complete guide for submitting your remote MCP server to Anthropic's MCP Directory for broader distribution and discoverability.

## Prerequisites

Before server submission, you should have:

- A working and fully-tested remote MCP server

- OAuth 2.0 authentication implemented (if authentication required)

- All tools with proper safety annotations

- Production-ready deployment

- A dedicated support channel (email or web)

- Provisioned test account with sample data

- Comprehensive documentation

New to remote MCP development? See [Getting Started with Custom Connectors Using Remote MCP](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp) first. For technical best practices and protocol details, see [MCP Protocol Documentation](https://modelcontextprotocol.io/).

**Note:** This guide covers remote MCP servers (cloud-hosted, HTTPS). For local desktop extensions, see [Local MCP Server Submission Guide](https://support.claude.com/en/articles/12922832-local-mcp-server-submission-guide).

------------------------------------------------------------------------

## 1. Directory Overview

### What are the benefits of directory inclusion?

**Discoverability and trust:**

- Listed in official Anthropic MCP Directory accessible from Claude.ai

- Accessible to Claude users across all platforms (web, desktop, mobile)

- Professional visibility for your service

**User experience:**

- One-click connection from directory

- Integrated with Claude's connector interface

- Standardized presentation across platforms

- OAuth flow handled seamlessly

**Support and credibility:**

- Anthropic review of quality, security, and compliance

- Listed alongside other vetted connectors

- Community visibility and feedback

- Professional distribution channel

### What Claude platforms support remote MCP servers?

**All major Claude platforms:**

- **Claude.ai (web)** - Full support with OAuth

- **Claude Desktop** - Full support with OAuth

- **Claude Code** - Direct connection from user's machine (with OAuth support)

- **Claude API** - Integration support

- **Claude Mobile apps** - Connector support

------------------------------------------------------------------------

## 2. Mandatory Requirements

All requirements in this section are **mandatory for directory approval**. Missing any of these will result in rejection or revision requests.

### Are safety annotations required?

YES - Every tool MUST have accurate safety annotations.

**Required on every tool:**

- readOnlyHint: true - For tools that only read data

- destructiveHint: true - For tools that modify data or have side effects

See [MCP Protocol - Tool Annotations](https://modelcontextprotocol.io/legacy/concepts/tools) for complete schema and implementation details.

**Not optional.** This is a hard requirement derived from the [MCP Directory Policy](https://support.claude.com/en/articles/11697096-anthropic-mcp-directory-policy).

**How to decide which annotation:**

[TABLE]

**Additional recommended annotation:**

- title - Human-readable tool name for UI display (improves user experience)

### Do I need to provide test accounts?

YES - If your server requires authentication.

**What to provide:**

- Test account credentials (username/password or API keys)

- Sample data in account (necessary for functional testing)

- Setup instructions for test environment

- Access limitations (if any)

**Test accounts should have:**

- Access to all tools being reviewed

- Representative sample data

- Appropriate permissions for full functionality testing

- Active status throughout review period and beyond

**How to provide:**

- Include credentials in submission form (ideally shared via secure method, such as 1Password link)

- Ensure accounts remain active during and after review for periodic post-admission reviews

- Provide sufficient access for comprehensive testing

### Is OAuth 2.0 required?

YES - If your server requires authentication.

**OAuth implementation requirements:**

- Must use OAuth 2.0 authorization code flow

- Certificates from recognized authorities

- Allowlist local MCP client (e.g. Claude Code, MCP Inspector) callback URLs:

  - http://localhost:6274/oauth/callback

  - http://localhost:6274/oauth/callback/debug

- Allowlist Claude callback URLs:

  - [https://claude.ai/api/mcp/auth_callback](https://claude.ai/api/mcp/auth_callback)

  - [https://claude.com/api/mcp/auth_callback](https://claude.com/api/mcp/auth_callback)

- Proper redirect URI configuration

**Common OAuth issues to avoid:**

- Invalid redirect URI errors (ensure both callback URLs are allowlisted)

- HEAD requests without tokens (handle gracefully after OAuth flow)

Implementation guidance: See [OAuth 2.0 Authorization Framework](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) for complete OAuth implementation details.

### Are there firewall requirements?

**YES - Must allowlist Claude's IP addresses for claude.ai compatibility**

For servers behind firewalls, allowlist IP addresses from [https://docs.claude.com/en/api/ip-addresses](https://docs.claude.com/en/api/ip-addresses).

Required for: Claude.ai and Claude Desktop

Not required for: Claude Code (connects directly from user's machine)

**Important:** IP allowlisting alone is not recommended as a security measure. Use OAuth 2.0 for authentication whenever possible.

### What documentation is required?

Comprehensive server documentation with specific sections.

**Recommended sections:**

1.  **Server Description** - Clear explanation of what your server does

2.  **Features** - Key capabilities and use cases

3.  **Setup Instructions** - How users connect and configure

4.  **Authentication** - OAuth setup and requirements (if applicable)

5.  **Usage Examples** - Minimum 3 working examples with prompts (required)

6.  **Privacy Policy** - Link to full privacy policy

7.  **Support** - How users can get help or report issues

**Example documentation structure:**

    # [Your Service Name] MCP Server

    ## Description
    [Brief description of service integration and capabilities]

    ## Features
    - Feature 1: [description and value]
    - Feature 2: [description and value]  
    - Feature 3: [description and value]

    ## Setup
    1. Visit the [Anthropic MCP Directory](https://claude.com/connectors)
    2. Find and connect to [Your Service]
    3. Complete OAuth authentication
    4. Configure any required settings

    ## Authentication
    This server requires OAuth authentication. You'll need:
    - Valid [Your Service] account
    - [Any specific permissions or account types]

    ## Examples
    [See minimum 3 examples section below]

    ## Privacy Policy
    See our privacy policy: https://your-domain.com/privacy

    ## Support
    - Email: [email protected]
    - Documentation: https://your-domain.com/mcp-docs
    - Issues: https://github.com/yourcompany/mcp-server/issues

### How many usage examples are required?

MINIMUM of three working examples demonstrating core functionality.

**What qualifies as a good example:**

- Shows realistic user prompt/request

- Demonstrates actual server functionality

- Includes expected output or behavior

- Clear and understandable workflow

- Covers different capabilities

**Example format:**

    ## Examples

    ### Example 1: Search for documents
    **User prompt:** "Find recent project reports in my workspace"
    **What happens:**
    - Server searches your workspace
    - Returns matching documents with metadata
    - Provides quick access links

    ### Example 2: Create new content
    **User prompt:** "Create a new task list for the marketing campaign"
    **What happens:**
    - Server creates new task list
    - Adds initial structure based on context
    - Returns link to newly created list

    ### Example 3: Update existing data
    **User prompt:** "Update the project status to 'In Progress' and add today's milestone"
    **What happens:**
    - Server locates the project
    - Updates status field
    - Adds milestone with current date
    - Confirms changes made

**Requirements:**

- Minimum 3 examples (no maximum)

- Cover different tools/capabilities

- Show realistic user interactions

- Demonstrate value proposition

- Include in server documentation

### What are the production readiness requirements?

Server must be in General Availability (GA) status.

**Production-ready means:**

- Server is stable and reliable in production

- Not marked as "beta," "alpha," or "development"

- All features fully implemented and tested

- Proper error handling and graceful failures

- Scalable infrastructure and monitoring

- Complete documentation and support channels

**Cannot be included:** Beta versions, development servers, or limited-access services.\
​

### What technical requirements must be met?

Must meet the core technical compliance standards.

**Transport and Performance:**

- Must support Streamable HTTP transport (SSE support may be deprecated)

- Fast response times with high availability

- Graceful error handling with helpful messages

- Token-efficient responses (max 25,000 tokens per tool result)

**Security and Data:**

- HTTPS/TLS with valid certificates

- CORS properly configured for browser clients

- Support for all required Claude client origins

- Collect only data necessary for functionality

- No collection of extraneous conversation data

- Privacy-compliant data practices

------------------------------------------------------------------------

## 3. Submission Process

### How do I submit my remote MCP server?

Follow this step-by-step submission process:

**1. Pre-submission checklist:**

Verify mandatory requirements:

- \[ \] All tools have readOnlyHint OR destructiveHint annotations

- \[ \] OAuth 2.0 implemented (if authentication required)

- \[ \] Server accessible via HTTPS

- \[ \] Claude IP addresses allowlisted (if behind firewall)

- \[ \] Comprehensive documentation published

- \[ \] Privacy policy published and accessible

- \[ \] Dedicated support channels (email or web)

- \[ \] Test account ready (if authentication required)

- \[ \] Server is production-ready (GA status)

**Test your server:**

- \[ \] Works correctly from Claude.ai

- \[ \] Works correctly from Claude Desktop

- \[ \] Works correctly from Claude Code (if no IP restrictions)

- \[ \] OAuth flow completes successfully

- \[ \] All tools function as documented

- \[ \] Error messages are helpful and user-friendly

- \[ \] Performance is acceptable under load

**2. Complete submission form:**

**Submission form:** [MCP Directory Server Review Form](https://docs.google.com/forms/d/e/1FAIpQLSeafJF2NDI7oYx1r8o0ycivCSVLNq92Mpc1FPxMKSw1CzDkqA/viewform)

**Required information:** Server details, documentation links, test credentials, examples (minimum 3), and contact information. Form provides a complete list.

While we strive to review every submission as quickly as we can, due to the amount of interest we cannot promise that we will accept your submission or respond to it individually.

------------------------------------------------------------------------

## 4. Common Issues

### What are the most common reasons for revision requests?

These are the top issues based on submission data:

**1. Missing tool annotations**

- **Problem:** Tools missing required safety annotations

- **Fix:** Add readOnlyHint or destructiveHint to ALL tools

- **Impact:** Immediate rejection, requires code changes

- **Prevention:** Validate all tools before submission

**2. OAuth implementation issues**

- **Problem:** OAuth flow fails or has configuration errors

- **Common causes:**

  - Missing callback URLs in OAuth provider

  - Invalid redirect URI configuration

  - Firewall misconfiguration

- **Fix:** Test OAuth flow thoroughly with MCP Inspector, Claude Code or Claude.ai

- **Impact:** Cannot complete functional testing, delays approval

**3. Incomplete documentation**

- **Problem:** Missing examples, unclear setup instructions, or missing required sections

- **Fix:** Provide minimum 3 detailed examples and complete all documentation sections

- **Impact:** Revision request, delays approval

- **Prevention:** Follow documentation template exactly

**4. Production readiness concerns**

- **Problem:** Server marked as "beta" or shows instability issues

- **Fix:** Ensure GA status and stable production deployment

- **Impact:** Cannot be included until production-ready

- **Prevention:** Complete internal testing and stability validation

**5. Privacy policy/support channel issues**

- **Problem:** Missing or inaccessible URLs for privacy policy/support channels

- **Fix:** Provide proper privacy policy and support channels (email or web)

- **Impact:** Immediate rejection due to policy requirement

- **Prevention:** Verify privacy policy/support channel accessibility before submission

### How can I avoid these issues?

Follow these prevention best practices:

**1. Complete the checklist thoroughly**

- Follow pre-submission checklist item by item

- Don't skip any requirements

- Get second-person review if possible

- Test from user perspective, not developer environment

**2. Test OAuth implementation extensively**

- Test with MCP Inspector, Claude Code or Claude.ai

- Verify all callback URLs work

- Test authentication flow end-to-end

- Ensure proper token handling

**3. Validate tool annotations**

- Verify every tool has safety annotations

- Check that annotations match actual tool behavior

- Ensure consistency across all tools

**4. Test server connectivity**

- Verify server accessible from intended IP ranges

- Test CORS configuration with browser clients

- Confirm HTTPS certificate validity

- Check firewall rules if applicable

**5. Document comprehensively**

- Include minimum 3 detailed examples

- Cover all setup and configuration steps

- Provide clear troubleshooting guidance

- Test documentation with new users

**Success rate:** Servers following this prevention guide have significantly fewer revision requests and faster approval times.

------------------------------------------------------------------------

## 5. Directory Policy

### What policies must I comply with?

All servers must comply with the [Anthropic MCP Directory Policy](https://support.claude.com/en/articles/11697096-anthropic-mcp-directory-policy).

### Can my server be removed from the directory?

Yes. Removal can occur for various reasons.

**Voluntary removal:**

- Request removal anytime through support channels

- No penalties for voluntary removal

- Can resubmit later after improvements

- Useful for major rework or updates

**Removal by Anthropic:**

Anthropic may remove extensions from the directory at any time and for any reason, at its sole discretion.

**Recommendations to avoid removal:**

- Monitor server performance and uptime

- Respond promptly to user issues and support requests

- Keep dependencies updated and secure

- Maintain compliance with evolving policies

- Set up monitoring and alerting for server health

------------------------------------------------------------------------

## Quick Reference

### Key Resources

1.  **Submission Form:** [MCP Directory Server Review Form](https://docs.google.com/forms/d/e/1FAIpQLSeafJF2NDI7oYx1r8o0ycivCSVLNq92Mpc1FPxMKSw1CzDkqA/viewform)

2.  **Directory Policy:** [MCP Directory Policy](https://support.claude.com/en/articles/11697096-anthropic-mcp-directory-policy)

3.  **Directory Terms:** [MCP Directory Terms and Conditions](https://support.claude.com/en/articles/11697081-anthropic-mcp-directory-terms-and-conditions)

4.  **Claude IP Addresses:** [API IP Addresses](https://docs.claude.com/en/api/ip-addresses)

5.  **MCP Protocol:** [Model Context Protocol Documentation](https://modelcontextprotocol.io/)

6.  **Getting Started Guide:** [Custom Connectors Using Remote MCP](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)

### Pre-Submission Checklist

- \[ \] All tools have safety annotations (readOnlyHint OR destructiveHint)

- \[ \] OAuth 2.0 implemented correctly (if authentication required)

- \[ \] Server accessible via HTTPS with valid certificates

- \[ \] Claude IP addresses allowlisted (if server behind firewall)

- \[ \] Comprehensive documentation published and accessible

- \[ \] Privacy policy published at stable HTTPS URL

- \[ \] Dedicated support channels (email or web)

- \[ \] Test account prepared with sample data (if authentication required)

- \[ \] Server is production-ready (GA status, not beta)

- \[ \] Minimum 3 usage examples documented

- \[ \] Error handling implemented with helpful messages

- \[ \] Performance tested under realistic load

- \[ \] OAuth flow tested end-to-end

- \[ \] All tools tested and verified functional

### Support and Questions

For technical questions about MCP development, consult the [MCP Protocol Documentation](https://modelcontextprotocol.io/).

For directory submission questions, use the submission form or contact support through official channels.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers)

Building Custom Connectors via Remote MCP Servers

[](https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq)

Anthropic Connectors Directory FAQ

[](https://support.claude.com/en/articles/12922832-local-mcp-server-submission-guide)

Local MCP Server Submission Guide

[](https://support.claude.com/en/articles/12922929-building-desktop-extensions-with-mcpb)

Building Desktop Extensions with MCPB

[](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy)

Anthropic Software Directory Policy

Did this answer your question?

😞

😐

😃

[](/en/)

- [Product](https://www.anthropic.com/product)
- [Research](https://www.anthropic.com/research)
- [Company](https://www.anthropic.com/company)
- [News](https://www.anthropic.com/news)
- [Careers](https://www.anthropic.com/careers)

- [Terms of Service - Consumer](https://www.anthropic.com/terms)
- [Terms of Service - Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Privacy Policy](https://www.anthropic.com/privacy)
- [Usage Policy](https://www.anthropic.com/aup)
- [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Compliance](https://trust.anthropic.com/)
