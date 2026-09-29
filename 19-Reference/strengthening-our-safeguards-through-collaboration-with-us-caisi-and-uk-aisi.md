---
title: "Strengthening safeguards with US CAISI and UK AISI \\ Anthropic"
source_url: "https://www.anthropic.com/news/strengthening-our-safeguards-through-collaboration-with-us-caisi-and-uk-aisi"
category: "19-Reference"
fetched_at: "2026-09-11T06:28:39Z"
tags: ["news-research"]
---

# Strengthening our safeguards through collaboration with US CAISI and UK AISI

Sep 12, 2025

Over the past year, we've collaborated with the US Center for AI Standards and Innovation (CAISI) and UK AI Security Institute (AISI), government bodies established to measure and improve the security of AI systems. Our voluntary work together began as initial consultations, but over time evolved to an ongoing partnership where CAISI and AISI teams were provided access to our systems at various stages of model development, allowing for ongoing testing of our systems.

Governments bring unique capabilities to this work, particularly deep expertise in national security areas like cybersecurity, intelligence analysis, and threat modeling that enables them to evaluate specific attack vectors and defense mechanisms when paired with their machine learning expertise. Their feedback helps us improve our security measures so our systems can withstand some of the most sophisticated attempts at misuse.

Working with independent external experts to identify vulnerabilities in AI systems is a core part of Anthropic’s [Safeguards](building-safeguards-for-claude.md) approach and is critical to preventing misuse of our models that could cause real-world harm.

## Uncovering and addressing vulnerabilities

This collaboration has already led to key findings that helped us strengthen the tools we use to prevent malicious use of our models. As part of our respective agreements with CAISI and AISI, each organization evaluated several iterations of our [Constitutional Classifiers](constitutional-classifiers.md)—a defense system we use to spot and prevent jailbreaks—on models like Claude Opus 4 and 4.1 prior to deployment to help identify vulnerabilities and build robust safeguards.

**Testing of Constitutional Classifiers.** We gave CAISI and AISI access to several early versions of our constitutional classifiers, and we’ve continued to provide access to our latest systems as we’ve made improvements. Together, we stress-tested these classifiers, with government red-teamers identifying a range of vulnerabilities—both before and after deployment—and our technical team using these findings to strengthen the safeguards. As examples, these vulnerabilities included:

- **Uncovering prompt injection vulnerabilities.** Government red-teamers identified weaknesses in our early classifiers via prompt injection attacks. Such attacks use hidden instructions to trick models into behavior that the system designer didn’t intend. Testers discovered that specific annotations, like falsely claiming human review had occurred, could bypass classifier detection entirely. We have patched these vulnerabilities.
- **Stress-testing safeguard architectures.** They developed a sophisticated universal jailbreak that encoded harmful interactions in ways that evaded our standard detection methods. Rather than simply patching this individual exploit, the discovery prompted us to fundamentally restructure our safeguard architecture to address the underlying vulnerability class.
- **Identifying cipher-based attacks.** Encoded harmful requests using ciphers, character substitutions, and other obfuscation techniques to evade our classifiers. These findings drove improvements to our detection systems, enabling them to recognize and block disguised harmful content regardless of encoding method.
- **Input and output obfuscation attacks.** Discovered universal jailbreaks using sophisticated obfuscation methods tailored to our specific defenses, such as fragmenting harmful strings into seemingly benign components within a wider context. Identifying these blind spots enabled targeted improvements to our filtering mechanisms.
- **Automated attack refinement.** Built new automated systems that progressively optimize attack strategies. They recently used this system to produce an effective universal jailbreak by iterating from a less effective jailbreak, which we are using to improve our safeguards.

**Evaluation and risk methodology.** Beyond identifying specific vulnerabilities, CAISI and AISI teams have helped strengthen our broader approach to security. Their external perspective on evidence requirements, deployment monitoring, and rapid response capabilities has been invaluable in pressure-testing our assumptions and identifying areas where additional evidence may be needed to support our threat models.

## Key lessons for effective collaborations

Our experience has taught us several important lessons about how to engage effectively with government research and standards bodies to improve the safety and security of our models.

**Comprehensive model access enhances red-teaming effectiveness.** Our experience shows that giving government red-teamers deeper access to our systems enables more sophisticated vulnerability discovery. We provided several key resources:

- **Pre-deployment safeguard prototypes**. Testers could evaluate and iterate on protection systems before they went live, identifying weaknesses *before* safeguards were deployed.
- **Multiple system configurations**. We provided models across the protection spectrum, from completely unprotected versions to models with full safeguards. This approach lets testers first develop attacks against base models, then progressively refine techniques to bypass increasingly sophisticated defenses. Helpful-only model variants also enabled precise harmful output scoring and capability benchmarking.
- **Extensive documentation and internal resources**. We provided trusted government red-teamers with our safeguard architecture details, documented vulnerabilities, safeguards reports, and granular content policy information (including specific prohibited requests and evaluation criteria). This transparency helped teams target high-value testing areas rather than searching blindly for weaknesses.
- **Real-time safeguards data accelerates vulnerability discovery.** We gave government red-teamers direct access to classifier scores. This enabled testers to refine their attack strategies and conduct more targeted exploratory research.

**Iterative testing allows for complex vulnerability discovery.** Though single evaluations provide value, sustained collaboration enables external teams to develop deep system expertise and uncover more complex vulnerabilities. During critical phases, we've maintained daily communication channels and frequent technical deep-dives with our partners.

**Complementary approaches offer more robust security.** CAISI and AISI evaluations work synergistically with our broader ecosystem. [Public bug bounty](testing-our-safety-defenses-with-a-new-bug-bounty-program.md) programs generate high-volume, diverse vulnerability reports from a wide talent pool, while specialized expert teams can help uncover complex, subtle attack vectors that require deep technical knowledge to identify. This multi-layered strategy helps ensure we catch both common exploits and sophisticated edge cases.

## Ongoing collaboration

Making powerful AI models secure and beneficial requires not just technical innovation but also new forms of collaboration between industry and government. Our experience demonstrates that public-private partnerships are most effective when technical teams work closely together to identify and address risk.

As AI capabilities advance, the role of independent evaluations of mitigations is increasingly important. We are heartened that other AI developers are also working with these government bodies, and encourage more companies to do so and share their own lessons more widely.

*We extend our gratitude to the technical teams at both US CAISI and UK AISI for their rigorous testing, thoughtful feedback, and ongoing collaboration. Their work has materially improved the security of our systems and advanced the field of measuring AI safeguard effectiveness.*

  
## Related content

### Developing Enterprise Frontier Safeguards with our customers

[Read more](enterprise-frontier-safeguards.md)

### Improving our alignment and security efforts

On July 30, we reported three incidents in which Claude models gained unauthorized access to real computer systems. We are conducting an in-depth analysis of both incidents, and planning to work with METR for an independent review. In the meantime, we’re sharing some of the changes we’ve made over the past month.

[Read more](improving-alignment-security-efforts.md)

### Previewing the Model Hardware Standard

We’re opening a research preview of the Model Hardware Standard (MHS), a shared specification for AI agents to safely operate physical devices, to a first group of scientific research labs and advanced manufacturers.

[Read more](model-hardware-standard-research-preview.md)

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
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

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
