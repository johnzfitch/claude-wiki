---
category: "06-MCP-Tools"
fetched_at: "2026-02-08T20:52:01Z"
source_url: "https://support.claude.com/en/articles/12922832-local-mcp-server-submission-guide"
title: "Local MCP Server Submission Guide | Claude Help Center"
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

[](#h_66c80b744c)

[](#h_18be112eac)

[](#h_4b3cb2cfba)

[](#h_79753ed54f)

[](#h_8d1c1b5ee4)

[](#h_3c4a72cbd4)

[](#h_32242aa788)

[](#h_8bce6a7e64)

[All Collections](/en/)

[Connectors](https://support.claude.com/en/collections/15399129-connectors)

Local MCP Server Submission Guide

# Local MCP Server Submission Guide

Updated yesterday

Table of contents

[](#h_66c80b744c)

[](#h_18be112eac)

[](#h_4b3cb2cfba)

[](#h_79753ed54f)

[](#h_8d1c1b5ee4)

[](#h_3c4a72cbd4)

[](#h_32242aa788)

[](#h_8bce6a7e64)

This is a complete guide for submitting your local server (MCPB) to Anthropic's public directory for broader distribution and discoverability.

## Prerequisites

**Before reading this guide, you should have:**

- A working MCPB

- Portable code using variable substitution

- Good error messages and user experience

- Clean, bundled dependencies

**New to MCPB development?** See [Building MCPB Extensions](https://support.claude.com/en/articles/12922929-building-desktop-extensions-with-mcpb) first. For technical best practices (testing, error messages, portability), see [MCPB Repository](https://github.com/anthropics/mcpb).

**Note:** This guide covers local MCP servers. For remote desktop extensions, see [Remote MCP Server Submission Guide](https://support.claude.com/en/articles/12922490-remote-mcp-server-submission-guide).

------------------------------------------------------------------------

## 1. Directory Overview

### What are the benefits of directory inclusion?

**Discoverability and trust:**

- Listed in official Anthropic directory within Claude Desktop

- Searchable by individual Claude Desktop users

- Visible to Teams/Enterprise users when added to allowlist by admins

- Anthropic review builds user trust

**User experience:**

- One-click installation from directory

- Integrated with Claude Desktop settings UI

- Standardized presentation

**Support and credibility:**

- Anthropic review of quality and security

- Listed alongside other reviewed extensions

- Community visibility and feedback

- Professional distribution channel

------------------------------------------------------------------------

## 2. Mandatory Requirements

**All requirements in this section are mandatory for directory approval.** Missing any of these will result in rejection or a revision request.

**Note:** These are Anthropic directory-specific requirements.

For general MCPB development best practices (testing, error handling, portability), see the [MCPB Repository README](https://github.com/modelcontextprotocol/mcpb/blob/main/README.md).

------------------------------------------------------------------------

### Are tool annotations required?

YES. Every tool MUST have and maintain accurate safety annotations.

**Required on every tool:**

- readOnlyHint: true - For tools that only read data

- destructiveHint: true - For tools that modify data or have side effects

See [MCP Protocol - Tool Annotations](https://modelcontextprotocol.io/legacy/concepts/tools) for complete schema and implementation details.

**Not optional.** This is a hard requirement derived from the [MCP Directory Policy](https://support.claude.com/en/articles/11697096-anthropic-mcp-directory-policy).

**How to decide which annotation:**

[TABLE]

**Implementation details:** See [MCP Protocol - Tools](https://modelcontextprotocol.io/docs/concepts/tools) for:

- Complete tool schema with annotations

- Tool definition structure

- Input/output schema specifications

- Additional tool properties (including optional title field)

**Validation before submission:**

\# Check all tools have annotations

grep -A 5 -B 5 "readOnlyHint\\destructiveHint" server/

\# Verify each tool has exactly one annotation

**Impact:** The first thing we check and the most common reason for a revision request.

**Additional recommended annotation:**

- title - Human-readable tool name for UI display (improves user experience)

------------------------------------------------------------------------

### Are privacy policies required?

Yes, privacy policies are required in two locations:

**Location 1: README.md**

Add a "Privacy Policy" section to your README with link to your full privacy policy so that users are aware of your practices:

    ## Privacy Policy

    This extension collects [describe data types]. For complete privacy information, see our privacy policy: https://your-domain.com/privacy-policy

    ### Data Collection
    - [List what data is collected]
    - [How it's used]
    - [Whether it's shared with third parties]
    - [Retention period]

**Location 2: manifest.json**

Add `privacy_policies` array with publicly accessible HTTPS URLs:

**Complete implementation:** See [MCPB Manifest Spec - Privacy Policies](https://github.com/anthropics/mcpb/blob/main/MANIFEST.md) for:

- Privacy policy field structure

- Manifest version requirements (0.3+)

- Multiple policy URL support

- Validation requirements

**Privacy policy must cover:**

- What data your MCPB collects

- How data is used and stored

- Whether data is shared with third parties

- User data retention policies

- Contact information for privacy questions

**Requirements:**

- Must be publicly accessible HTTPS URL

- Must be from your domain (not third-party hosting)

- Must be current and accurate

- Must be in README **AND** manifest.json

- Must use manifest_version "0.3" or higher

**Common mistakes:**

- Privacy policy in manifest but not README

- Privacy policy in README but not manifest

- Using manifest_version "0.2" or older

- Invalid or inaccessible URLs

- Privacy policy hosted on third-party site

**Impact:** One of the most common causes of rejection - straightforward to fix but frequently overlooked.

------------------------------------------------------------------------

### How many examples are required?

MINIMUM of three working examples demonstrating core functionality.

**What qualifies as a good example:**

- Shows realistic use case

- Includes expected user input/prompt

- Shows expected output/behavior

- Demonstrates actual tool usage

- Clear and understandable workflow

**Example format (in README.md):**

    ## Examples

    ### Example 1: Search for files
    **User prompt:** "Find all JavaScript files in my project"

    **Expected behavior:**
    - Extension searches workspace directory
    - Returns list of .js files with paths
    - Shows file count in summary

    ### Example 2: Read file contents
    **User prompt:** "Show me the contents of config.json"

    **Expected behavior:**
    - Extension reads config.json
    - Returns formatted JSON content
    - Handles file not found gracefully

    ### Example 3: Create new file
    **User prompt:** "Create a new file called notes.txt with 'Hello World'"

    **Expected behavior:**
    - Extension creates notes.txt
    - Writes content to file
    - Confirms creation with file path

**What to include:**

- Realistic user prompts (how users will interact)

- Expected tool calls (what happens behind the scenes)

- Expected outputs (what users will see)

- Error handling examples (optional but recommended)

**Requirements:**

- Minimum 3 examples (no maximum)

- Cover core functionality

- Show different tools/capabilities

- Demonstrate value proposition

- Include in README.md

**Impact:** A frequent source of delays or rejections - reviewers need complete documentation to properly evaluate submissions.

------------------------------------------------------------------------

### Do I need to provide testing credentials?

If your MCPB requires authentication or external service access, then YES.

**Required when:**

- Your MCPB connects to external APIs

- Authentication is needed for functionality

- The MCPB user must have an account to use features

- External service integration otherwise present

**Not required when:**

- Purely local MCPB (filesystem operations only)

- No external connections

- No authentication needed

- Completely self-contained

**What to provide:**

- Test account credentials (username/password or API keys)

- Sample data in account (helpful for functional testing)

- Setup instructions (how to configure and use test account)

- Access limitations or restrictions (if any)

- Account expiration date (if temporary)

**How to provide:**

- Include in submission form

- Send via secure method if highly sensitive

- Ensure account remains active throughout review period

- Provide sufficient access level for complete testing

**Best practice:** Create dedicated test account separate from production to:

- Avoid exposing production data

- Control what reviewers can access

- Easily revoke access after approval

- Track test account usage

**Impact:** Delays review process if missing when needed

------------------------------------------------------------------------

### What documentation is required?

Comprehensive documentation in README.md with minimum required sections.

**Minimum required sections:**

1.  **Description** - Clear explanation of what your MCPB does

2.  **Features** - Key capabilities and use cases

3.  **Installation** - How to install (typically: "Install from Anthropic Directory")

4.  **Configuration** - Required settings and setup steps

5.  **Usage Examples** - Minimum 3 examples (see above section)

6.  **Privacy Policy** - Link to full privacy policy

7.  **Support** - How users can get help or report issues

**Example README.md structure:**

    # My MCPB Extension

    ## Description
    Brief description of what this extension does and why it's useful.

    ## Features
    - Feature 1: [description]
    - Feature 2: [description]
    - Feature 3: [description]

    ## Installation
    Install from the Anthropic Directory in Claude Desktop Settings → Extensions.

    ## Configuration
    1. Open Settings → Extensions → [Extension Name]
    2. Add API key (if required)
    3. Select workspace directory
    4. Configure optional settings

    ## Examples
    [See minimum 3 examples section above]

    ## Privacy Policy
    See our privacy policy: https://your-domain.com/privacy

    ## Support
    For issues or questions: [email protected]
    GitHub Issues: https://github.com/your-username/your-extension/issues

**Additional recommended sections:**

- Troubleshooting - Common issues and solutions

- Version compatibility - Which Claude Desktop versions supported

- Changelog - Version history and changes

- Contributing - How others can contribute (for open source)

**Best practices:**

- Clear, concise writing

- Screenshots (optional but very helpful)

- Step-by-step instructions

- Links to additional resources

------------------------------------------------------------------------

## 3. Submission Process

### How do I submit to the directory?

Before submitting to the directory, complete this step-by-step submission process:

**1. Pre-submission checklist:**

**Test your MCPB:**

- Passes all 4 testing phases (development, clean environment, cross-platform, Claude Desktop)

- Works in clean environment without development tools

- Portable across macOS and Windows

- Dependencies current and bundled

- Error messages are helpful and actionable

- Performance is acceptable

**Verify mandatory requirements:**

- All tools have readOnlyHint OR destructiveHint annotations

- Privacy policy present in README.md

- Privacy policy present in manifest.json privacy_policies array

- Use latest Manifest version for best compatibility

- Minimum 3 working examples documented in README

- Testing credentials provided (if applicable)

**Prepare documentation:**

- README.md complete with all required sections

- LICENSE file included

- Icon included (recommended, 512×512px PNG)

- CHANGELOG.md (optional but recommended)

**2. Package final version:**

    # Clean build
    rm -rf node_modules/.cache
    npm install --production

    # Package
    mcpb pack

    # Verify package
    mcpb info your-extension.mcpb

**3. Submit via official form:**

**Submission form:** [https://forms.gle/tyiAZvch1kDADKoP9](https://forms.gle/tyiAZvch1kDADKoP9)

**Required information:** Server details, documentation links, test credentials, examples (minimum 3), and contact information. Form provides a complete list.

While we strive to review every submission as quickly as we can, due to the amount of interest we cannot promise that we will accept your submission or respond to it individually.

------------------------------------------------------------------------

## 4. Common Issues

### What are the most common reasons for revision requests?

These are the top issues based on submission data:

**1. Missing tool annotations**

- **Problem:** Tools missing required readOnlyHint or destructiveHint annotations

- **Fix:** Add annotations to ALL tools in your server implementation

- **Impact:** Immediate rejection, requires code changes

- **Prevention:** Run validation command before submission

**2. Portability issues**

- **Problem:** Works in developer environment but fails for end users

- **Common causes:** Hardcoded paths, missing dependencies, platform assumptions

- **Fix:** Test in clean environment, use variable substitution, bundle dependencies

- **Impact:** 1-2 week delay for troubleshooting and resubmission

- **Prevention:** Clean environment testing phase

**3. Missing privacy policy**

- **Problem:** Privacy policy missing from README.md or manifest.json (or both)

- **Fix:** Add privacy policy section to README and privacy_policies array to manifest

- **Impact:** Immediate rejection

- **Prevention:** Use pre-submission checklist

**4. Incomplete documentation**

- **Problem:** Fewer than 3 examples, unclear setup instructions, missing sections

- **Fix:** Add comprehensive examples (minimum 3) and complete all required README sections

- **Impact:** Revision request, delays approval

- **Prevention:** Follow README structure template

**Note:** These issues account for 90% of revision requests based on submission data. All are preventable with thorough pre-submission testing and checklist completion.

------------------------------------------------------------------------

### How can I avoid these issues?

Follow these prevention best practices:

**1. Complete the checklist**

- Follow entire pre-submission checklist item-by-item

- Don't skip clean environment testing

- Verify each requirement twice before submitting

- Get second person to review if possible

**2. Test like an end user**

- Use fresh virtual machine or container

- Install no development tools

- Follow only your README instructions

- Verify everything works without prior knowledge

**3. Validate tool annotations**

    # Quick check - should show all your tools with annotations
    grep -A 5 -B 5 "readOnlyHint\|destructiveHint" server/

    # Verify each tool has exactly one annotation (not both, not neither)
    # Count should match your total number of tools

**4. Privacy policy verification**

    # Check README has privacy section
    grep -i "privacy" README.md

    # Check manifest has privacy_policies array
    grep "privacy_policies" manifest.json

    # Verify URLs are accessible
    curl -I https://your-domain.com/privacy-policy

**5. Example quality self-assessment**

- Read your examples as if you're a completely new user

- Do they make sense without additional context?

- Do they show realistic, practical usage?

- Are there at least 3 distinct examples?

- Do they cover your core functionality?

**Success rate:** Extensions following this prevention guide have fewer revision requests.

------------------------------------------------------------------------

### Can my MCPB be removed from the directory?

Yes. Removal can occur for various reasons.

**Voluntary removal (your choice):**

- Request removal anytime via contact form

- No penalties for voluntary removal

- Can resubmit later after improvements

- Useful if major rework needed

**Removal by Anthropic:**

Anthropic may remove extensions from the directory at any time and for any reason, at its sole discretion.

**Recommendations to avoid removal:**

- Maintain quality standards consistently

- Respond to issues promptly (within days, not weeks)

- Keep dependencies updated quarterly

- Monitor user feedback actively

- Maintain compliance with evolving policies

- Set up monitoring for runtime errors

------------------------------------------------------------------------

## 5. Directory Policy

### What policies must I comply with?

All extensions must comply with the [Anthropic MCP Directory Policy](https://support.claude.com/en/articles/11697096-anthropic-mcp-directory-policy).

------------------------------------------------------------------------

## Quick Reference

### Key resources

- Submission form: [https://forms.gle/tyiAZvch1kDADKoP9](https://forms.gle/tyiAZvch1kDADKoP9)

- [Anthropic MCP Directory Policy](https://support.claude.com/en/articles/11697096-anthropic-mcp-directory-policy)

- [Anthropic MCP Directory Terms and Conditions](https://support.claude.com/en/articles/11697081-anthropic-mcp-directory-terms-and-conditions)

- MCPB Manifest Spec: [https://github.com/anthropics/mcpb/blob/main/MANIFEST.md](https://github.com/anthropics/mcpb/blob/main/MANIFEST.md)

- MCP Protocol - Tools: [https://modelcontextprotocol.io/docs/concepts/tools](https://modelcontextprotocol.io/docs/concepts/tools)

------------------------------------------------------------------------

## Need Help Building Your MCPB First?

This guide assumes you already have a working MCPB. If you're just getting started with MCPB development, see our companion guide: [Building Desktop Extensions with MCPB](https://support.claude.com/en/articles/12922929-building-desktop-extensions-with-mcpb).

The building guide covers:

- Creating your first MCPB

- Development best practices and testing

- Configuration and manifest.json

- Distribution options

- Maintenance approaches

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)

Getting Started with Local MCP Servers on Claude Desktop

[](https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq)

Anthropic Connectors Directory FAQ

[](https://support.claude.com/en/articles/12922490-remote-mcp-server-submission-guide)

Remote MCP Server Submission Guide

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
