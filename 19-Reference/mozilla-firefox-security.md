---
title: "Partnering with Mozilla on Firefox security \\ Anthropic"
source_url: "https://www.anthropic.com/news/mozilla-firefox-security"
category: "19-Reference"
fetched_at: "2026-09-10T06:45:56Z"
tags: ["evaluation", "news-research", "security"]
---

# Partnering with Mozilla to improve Firefox’s security

Mar 6, 2026

AI models can now independently identify high-severity vulnerabilities in complex software. As we recently documented, Claude found more than 500 [zero-day vulnerabilities](https://red.anthropic.com/2026/zero-days/) (security flaws that are unknown to the software’s maintainers) in well-tested open-source software.

In this post, we share details of a collaboration with researchers at Mozilla in which Claude Opus 4.6 discovered 22 vulnerabilities over the course of two weeks. Of these, Mozilla assigned [14 as high-severity vulnerabilities](https://www.mozilla.org/en-US/security/advisories/mfsa2026-13/)—almost a fifth of all high-severity Firefox vulnerabilities that were remediated in 2025. In other words: AI is making it possible to detect severe security vulnerabilities at highly accelerated speeds.

As part of this collaboration, Mozilla fielded a large number of reports from us, helped us understand what types of findings warranted submitting a bug report, and shipped fixes to hundreds of millions of users in [Firefox 148.0](https://www.firefox.com/en-US/firefox/148.0/releasenotes/). [Their partnership](https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/), and the technical lessons we learned, provides a model for how AI-enabled security researchers and maintainers can work together to meet this moment.

## From model evaluations to a security partnership

In late 2025, we noticed that Opus 4.5 was close to solving all tasks in [CyberGym](https://www.cybergym.io/), a benchmark that tests whether LLMs can reproduce known security vulnerabilities. We wanted to construct a harder and more realistic evaluation that contained a higher concentration of technically complex vulnerabilities, like those present in modern web browsers. So we built a dataset of prior Firefox common vulnerabilities and exposures (CVEs) to see if Claude could reproduce those.

We chose Firefox because it’s both a complex codebase and one of the most well-tested and secure open-source projects in the world. This makes it a harder test of AI’s ability to find novel security vulnerabilities than the open-source software we previously used to test our models. Hundreds of millions of users rely on it daily, and browser vulnerabilities are particularly dangerous because users routinely encounter untrusted content and depend on the browser to keep them safe.

Our first step was to use Claude to find previously identified CVEs in older versions of the Firefox codebase. We were surprised that Opus 4.6 could reproduce a high percentage of these historical CVEs, given that each of them took significant human effort to uncover. But it was still unclear how much we should trust this result because it was possible that at least some of those historical CVEs were already in Claude’s training data.

So we tasked Claude with finding novel vulnerabilities in the *current* version of Firefox—bugs that by definition can’t have been reported before. We focused first on Firefox’s JavaScript engine but then expanded to other areas of the browser. The JavaScript engine was a convenient first step: it’s an independent slice of Firefox’s codebase that can be analyzed in isolation, and it’s particularly important to secure, given its wide attack surface (it processes untrusted external code when users browse the web).

After just twenty minutes of exploration, Claude Opus 4.6 reported that it had identified a Use After Free (a type of memory vulnerability that could allow attackers to overwrite data with arbitrary malicious content) in the JavaScript engine. One of our researchers validated this bug in an independent virtual machine with the latest Firefox release, then forwarded it to two other Anthropic researchers, who also validated the bug. We then filed a bug report in [Bugzilla](https://bugzilla.mozilla.org/enter_bug.cgi?), Mozilla’s issue tracker, along with a description of the vulnerability and a proposed patch (written by Claude and validated by the reporting team) to help triage the root cause.

In the time it took us to validate and submit this first vulnerability to Firefox, Claude had already discovered fifty more unique crashing inputs. While we were triaging these crashes, a researcher from Mozilla reached out to us. After a technical discussion about our respective processes and sharing a few more vulnerabilities we had manually validated, they encouraged us to submit all of our findings in bulk without validating each one, even if we weren’t confident that all of the crashing test cases had security implications. By the end of this effort, we had scanned nearly 6,000 C++ files and submitted a total of 112 unique reports, including the high- and moderate-severity vulnerabilities mentioned above. Most issues have been fixed in Firefox 148, with the remainder to be fixed in upcoming releases.

When doing this kind of bug hunting in external software, we’re always conscious of the fact that we may have missed something critical about the codebase that would make the discovery a false positive. We try to do the due diligence of validating the bugs ourselves, but there’s always room for error. We are extremely appreciative of Mozilla for being so transparent about their triage process, and for helping us adjust our approach to ensure we only submitted test cases they cared about (even if not all of them ended up being relevant to security). Mozilla researchers have since started experimenting with Claude for security purposes internally.

## From identifying vulnerabilities to writing primitive exploits

To measure the upper limits of Claude’s cybersecurity abilities, we also developed a new evaluation to determine whether Claude was able to *exploit* any of the bugs we discovered. In other words, we wanted to understand whether Claude could also develop the sorts of tools that a hacker would use to take advantage of these bugs to execute malicious code.

To do this, we gave Claude access to the vulnerabilities we’d submitted to Mozilla and asked Claude to create an exploit focusing on each one. To prove it had successfully exploited a vulnerability, we asked Claude to demonstrate a real attack. Specifically, we required it to read and write a local file in a target system, as an attacker would.

We ran this test several hundred times with different starting points, spending approximately \$4,000 in API credits. Despite this, Opus 4.6 was only able to actually turn the vulnerability into an exploit in two cases. This tells us two things. One, Claude is much better at finding these bugs than it is at exploiting them. Two, the cost of identifying vulnerabilities is an order of magnitude cheaper than creating an exploit for them. However, the fact that Claude *could* succeed at automatically developing a crude browser exploit, even if only in a few cases, is concerning.

“Crude” is an important caveat here. The exploits Claude wrote only worked on our testing environment, which intentionally removed some of the security features found in modern browsers. This includes, most importantly, the [sandbox](https://wiki.mozilla.org/Security/Sandbox), the purpose of which is to reduce the impact of these types of vulnerabilities. Thus, Firefox’s “defense in depth” would have been effective at mitigating these particular exploits. But vulnerabilities that escape the sandbox are not unheard of, and Claude’s attack is one necessary component of an end-to-end exploit. You can read more about how Claude developed one of these Firefox exploits on our [Frontier Red Team blog](https://red.anthropic.com/2026/exploit/).

## What's next for AI-enabled cybersecurity

These early signs of AI-enabled exploit development underscore the importance of accelerating the find-and-fix process for defenders. Towards that end, we want to share a few technical and procedural best practices we’ve found while performing this analysis.

First, when researching “patching agents,” which use LLMs to develop and validate bug fixes, we have developed a few methods we hope will help maintainers use LLMs like Claude to triage and address security reports faster.¹

In our experience, Claude works best when it's able to check its own work with another tool. We refer to this class of tool as a “task verifier”: a trusted method of confirming whether an AI agent’s output actually achieves its goal. Task verifiers give the agent real-time feedback as it explores a codebase, allowing it to iterate deeply until it succeeds.

Task verifiers helped us discover the Firefox vulnerabilities described above,² and in separate research, we’ve found that they’re also useful for *fixing* bugs. A good patching agent needs to verify at least two things: that the vulnerability has actually been removed, and that the program’s intended functionality has been preserved. In our work, we built tools that automatically tested whether the original bug could still be triggered after a proposed fix, and separately ran test suites to catch regressions (a change that accidentally breaks something else). We expect maintainers will know best how to build these verifiers for their own codebases; the key point is that giving the agent a reliable way to check both of these properties dramatically improves the quality of its output.

We can’t guarantee that all agent-generated patches that pass these tests are good enough to merge immediately. But task verifiers give us increased confidence that the produced patch will fix the specific vulnerability while preserving program functionality—and therefore achieve what’s considered to be the minimum requirement for a plausible patch. Of course, when reviewing AI-authored patches, we recommend that maintainers apply the same scrutiny they’d apply to any other patch created by an external author.

Zooming out to the process of submitting bugs and patches: we know that maintainers are underwater. Therefore, our approach is to give maintainers the information they need to trust and verify reports. The Firefox team highlighted three components of our submissions that were key for trusting our results:

1.  Accompanying minimal test cases
2.  Detailed proofs-of-concept
3.  Candidate patches

We strongly encourage researchers who use LLM-powered vulnerability research tools to include similar evidence of verification and reproducibility when submitting reports based on the output of such tooling.

We’ve also published our [Coordinated Vulnerability Disclosure operating principles](https://www.anthropic.com/coordinated-vulnerability-disclosure)**,** where we describe the procedures we will use when working with maintainers. Our processes here follow standard industry norms for the time being, but as models improve we may need to adjust our processes to keep pace with capabilities.

## The urgency of the moment

Frontier language models are now world-class vulnerability researchers. On top of the 22 CVEs we identified in Firefox, we’ve used Claude Opus 4.6 to discover vulnerabilities in other important software projects like the Linux kernel. Over the coming weeks and months, we will continue to report on how we’re using our models and working with the open-source community to improve security.

Opus 4.6 is currently far better at identifying and fixing vulnerabilities than at exploiting them. This gives defenders the advantage. And with the recent release of [Claude Code Security](claude-code-security.md) in limited research preview, we’re bringing vulnerability-discovery (and patching) capabilities directly to customers and open-source maintainers.

But looking at the rate of progress, it is unlikely that the gap between frontier models’ vulnerability discovery and exploitation abilities will last very long. If and when future language models break through this exploitation barrier, we will need to consider additional safeguards or other actions to prevent our models from being misused by malicious actors.

We urge developers to take advantage of this window to redouble their efforts to make their software more secure. For our part, we plan to significantly expand our cybersecurity efforts, including by working with developers to search for vulnerabilities (following the CVD process outlined above), developing tools to help maintainers triage bug reports, and directly proposing patches.

*If you’re interested in supporting our security efforts—writing new scaffolds to identify vulnerabilities in open-source software; triaging, patching, and reporting vulnerabilities; and developing a robust CVD process for the AI era—[apply to work at Anthropic here](https://job-boards.greenhouse.io/anthropic/jobs/5123011008).*

#### Footnotes

1.  All the advice shared here is based on our use of Claude, but it should apply to whichever LLM you prefer.
2.  Which Mozilla patched independently.


## Related content

### Developing Enterprise Frontier Safeguards with our customers

[Read more](enterprise-frontier-safeguards.md)

### Improving our alignment and security efforts

On July 30, we reported three incidents in which Claude models gained unauthorized access to real computer systems. We are conducting an in-depth analysis of both incidents, and planning to work with METR for an independent review. In the meantime, we’re sharing some of the changes we’ve made over the past month.

[Read more](improving-alignment-security-efforts.md)

### Previewing the Model Hardware Standard

We’re opening a research preview of the Model Hardware Standard (MHS), a shared specification for AI agents to safely operate physical devices, to a first group of scientific research labs and advanced manufacturers.

[Read more](model-hardware-standard-research-preview.md)

## Subscribe to the Frontier Red Team newsletter

Get updates on our latest red-teaming research and findings.

[](https://www.anthropic.com/)

### Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Code Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Design](../15-Claude-AI-Features/product-design.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Claude in Chrome](https://claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](https://www.anthropic.com/15-Claude-AI-Features/claude-opus-4-6-anthropic.md)
- [Sonnet](https://www.anthropic.com/15-Claude-AI-Features/claude-sonnet-4-6-anthropic.md)
- [Haiku](https://www.anthropic.com/15-Claude-AI-Features/claude-haiku-4-5-anthropic.md)

### Solutions

- [AI agents](../18-Industry-UseCases/agents.md)
- [Code modernization](../18-Industry-UseCases/code-modernization.md)
- [Coding](../18-Industry-UseCases/coding.md)
- [Commerce](../18-Industry-UseCases/commerce.md)
- [Customer support](../18-Industry-UseCases/customer-support.md)
- [Cybersecurity](../18-Industry-UseCases/cybersecurity.md)
- [Enterprise](../18-Industry-UseCases/enterprise.md)
- [Financial services](../18-Industry-UseCases/finance.md)
- [Government](../18-Industry-UseCases/government.md)
- [Healthcare](../18-Industry-UseCases/healthcare.md)
- [Higher education](../18-Industry-UseCases/education.md)
- [K-12 teachers](../18-Industry-UseCases/teachers.md)
- [Legal](../18-Industry-UseCases/legal.md)
- [Life sciences](../18-Industry-UseCases/life-sciences.md)
- [Nonprofits](../18-Industry-UseCases/nonprofits.md)
- [Small business](../18-Industry-UseCases/small-business.md)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](../04-API-Reference/Other/home.md)
- [Pricing](../17-Billing-Plans/pricing.md#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud-vertex-ai.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)
- [Console login](../04-API-Reference/Other/usage-limits.md)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Community](https://claude.com/community)
- [Connectors](../04-API-Reference/Other/partners-mcp.md)
- [Courses](https://academy.claude.com)
- [Customer stories](../18-Industry-UseCases/customers.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Plugins](../08-Plugins-Skills/claude-com-plugins.md)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](../04-API-Reference/Other/partners-services.md)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](company.md)
- [Careers](https://www.anthropic.com/careers)
- [Leadership](company-leadership.md)
- [Policy](https://www.anthropic.com/policy)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](anthropic-com-research.md)
- [News](news.md)
- [Claude’s Constitution](https://www.anthropic.com/constitution)
- [Claude Corps](../15-Claude-AI-Features/claude-corps.md)
- [Keep thinking](https://www.anthropic.com/path-to-hope)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](announcing-our-updated-responsible-scaling-policy.md)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](https://www.anthropic.com/transparency)
