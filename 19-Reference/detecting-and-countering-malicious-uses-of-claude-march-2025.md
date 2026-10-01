---
title: "Detecting and countering malicious uses of Claude \\ Anthropic"
source_url: "https://www.anthropic.com/news/detecting-and-countering-malicious-uses-of-claude-march-2025"
category: "19-Reference"
fetched_at: "2026-09-11T06:28:58Z"
tags: ["news-research"]
---

# Detecting and countering malicious uses of Claude: March 2025

Apr 23, 2025

We are committed to preventing misuse of our Claude models by adversarial actors while maintaining their utility for legitimate users. While our safety measures successfully prevent many harmful outputs, threat actors continue to explore methods to circumvent these protections. We are continuously using learnings to upgrade our safeguards.

This report outlines several case studies on how actors have misused our models, as well as the steps we have taken to detect and counter such misuse. By sharing these insights, we hope to protect the safety of our users, prevent abuse or misuse of our services, enforce our Usage Policy and other terms, and share our learnings for the benefit of the wider online ecosystem. The case studies presented in this report, while specific, are representative of broader patterns we're observing across our monitoring systems. These examples were selected because they clearly illustrate emerging trends in how malicious actors are adapting to and leveraging frontier AI models. We hope to contribute to a broader understanding of the evolving threat landscape and help the wider AI ecosystem develop more robust safeguards.

The most novel case of misuse detected was a professional 'influence-as-a-service' operation showcasing a distinct evolution in how certain actors are leveraging LLMs for influence operation campaigns. What is especially novel is that this operation used Claude not just for content generation, but also to decide when social media bot accounts would comment, like, or re-share posts from authentic social media users. As described in the full report, Claude was used as an orchestrator deciding what actions social media bot accounts should take based on politically motivated personas. **Read the full report [here](https://cdn.sanity.io/files/4zrzovbb/website/45bc6adf039848841ed9e47051fb1209d6bb2b26.pdf)**.  

We have also observed cases of credential stuffing operations, recruitment fraud campaigns, and a novice actor using AI to enhance their technical capabilities for malware generation beyond their skill level, among other activities not mentioned in this blog. The impact of these activities varies:

- An influence-as-a-service operation utilized Claude to automate operations and engaged with 10s of thousands of authentic social media accounts across multiple countries and languages.
- An actor leveraged Claude to enhance systems for identifying and processing exposed usernames and passwords associated with security cameras, while simultaneously collecting information on internet-facing targets to test these credentials against. We have not confirmed successful deployment of these efforts.
- A recruitment fraud campaign leveraged Claude to enhance the content of scams targeting job seekers in Eastern European countries. We have not confirmed successful deployment of these efforts.
- An individual actor with limited technical skills developed malware that would typically require more advanced expertise. We have not confirmed successful deployment of these efforts.

**Our key learnings include:**

- Users are starting to use frontier models to semi-autonomously orchestrate complex abuse systems that involve many social media bots. As agentic AI systems improve we expect this trend to continue.
- Generative AI can accelerate capability development for less sophisticated actors, potentially allowing them to operate at a level previously only achievable by more technically proficient individuals.

Our intelligence program is meant to be a safety net by both finding harms not caught by our standard scaled detection and to add context in how bad actors are using our models maliciously. In investigating these cases, our team applied techniques described in our recently published research papers, including [Clio](clio.md) and [hierarchical summarization](https://alignment.anthropic.com/2025/summarization-for-monitoring/). These approaches allowed us to efficiently analyze large volumes of conversation data to identify patterns of misuse. These techniques, coupled with classifiers (which analyze user inputs for potentially harmful requests and evaluate Claude's responses before or after delivery) allowed us to detect, investigate, and ban the accounts associated with these cases.

The case studies below highlight the types of threats we have detected and provide insights into how threat actors are adapting their operations to leverage generative AI.

### **Case Study: Operating Multi-Client Influence Networks Across Platforms \[full report available [here](https://cdn.sanity.io/files/4zrzovbb/website/45bc6adf039848841ed9e47051fb1209d6bb2b26.pdf)\]**

We identified and banned an actor using Claude for a financially-motivated "influence-as-a-service" operation. This actor’s infrastructure leveraged Claude to orchestrate over a hundred social media bot accounts for the purpose of pushing their clients political narratives. These political narratives are consistent with what we expect from state affiliated campaigns, however we have not confirmed this attribution. Most significantly, the operation utilized Claude to make tactical engagement decisions such as determining whether social media bot accounts should like, share, comment on, or ignore specific posts created by other accounts based on political objectives aligned with their clients' interests.

**Actor Profile**: This operation managed over 100 social media bot accounts across Twitter/X and Facebook. The operator created personas for each account with distinct political alignments, and engaged with tens of thousands of authentic social media accounts. The operation's activity suggests a commercial service that served clients across several countries with varied political objectives.

**Tactics and Techniques**: The operation used Claude for multiple purposes:

- Creating and maintaining consistent personas across platforms with specific political alignments
- Determining when personas should like, share, comment on, or ignore specific content
- Generating politically-aligned responses in appropriate languages
- Creating prompts for image-generation tools and evaluating their outputs

The actor maintained distinct narrative portfolios for different clients, all outside of the United States with varied political narratives they were aimed at pushing

**Impact**: The operation engaged with tens of thousands of authentic social media accounts. No content achieved viral status, however the actor strategically focused on sustained long-term engagement promoting moderate political perspectives rather than pursuing virality.

### **Case Study: Scraping leaked credentials associated with internet of things security cameras.**

We identified and banned a sophisticated actor using our models in an attempt to develop capabilities to scrape leaked passwords & usernames associated with security cameras and build capabilities to forcibly gain access to those security cameras. After identifying this usage we banned the account associated with building these capabilities. Although this was the actor's goal, we don’t know if they were ultimately successful deploying this capability.

**Actor Profile:** This actor demonstrated sophisticated development skills and maintained an infrastructure integrating multiple intelligence sources, including commercial breach data platforms, and integration with private stealer log communities.

**Tactics and Techniques:** The actor primarily used Claude to enhance their technical capabilities:

- Rewriting their open source scraping toolkit for easier maintenance
- Creating scripts to scrape target URLs from websites
- Developing systems to process posts from stealer log telegram communities
- Improving UI and backend systems to enhance search features

Some of these techniques are dual use. In fact, a benign actor may use them for legitimate purposes, however it’s important to look at the full context of activity which in this case was to enable unauthorized access to devices.

**Impact:** The potential consequences of this group's activities include credential compromise, unauthorized access to IoT devices (particularly security cameras), and network penetration. We have not confirmed real-world success deploying this capability.

### **Case Study: Recruitment Fraud Campaign: Real-Time Language Sanitization for Scamming**

We identified and banned an actor conducting recruitment fraud targeting job seekers primarily in Eastern European countries. This campaign demonstrates how threat actors are using AI for real-time language sanitization to make their scams more convincing.

**Actor Profile:** This operation demonstrated moderately sophisticated social engineering techniques, impersonating hiring managers from legitimate companies to establish credibility.

**Tactics and Techniques:** The actor used Claude primarily to enhance their fraudulent communications:

- Requesting language refinement to improve the professionalism of their communications
- Developing more convincing recruitment narratives
- Creating interview questions and scenarios
- Formatting messages to appear more legitimate

In one notable pattern, the operators would submit poorly written text in non-native English and ask Claude to adjust the text as if written by a native english speaker - effectively laundering their communications to appear more polished. This real-time language sanitization improves the perceived legitimacy of their communications.

**Impact:** While the operation attempted to compromise personal information from job applicants, we have not confirmed successful instances of scams from this operation.

**Case Study: Novice Threat Actor Enabled to Create Malware**

We identified and banned a novice actor leveraging Claude to improve their technical capabilities and develop malicious tools beyond their actual skill level.

**Actor Profile:** This actor demonstrated limited formal coding skills but used AI to rapidly expand their capabilities, developing tools for doxing and remote access.

**Technical Evolution:** We observed this actor evolve from simple scripts to sophisticated systems with the aid of Claude.

- Their open source toolkit evolved from basic functionality (likely obtained off-the-shelf) to an advanced suite that included facial recognition and dark web scanning.
- Their malware builder evolved from a simple batch script generator to a comprehensive graphical user interface for generating undetectable malicious payloads, with particular emphasis on evading security controls and maintaining persistent access to compromised systems.

**Impact:** This case illustrates how AI can potentially flatten the learning curve for malicious actors, allowing individuals with limited technical knowledge to develop sophisticated tools and potentially accelerate their progression from low-level activities to more serious cybercriminal endeavors. We have not confirmed real world deployment of this malware.

**Next Steps**

As we continue to develop and deploy powerful AI systems, we remain committed to preventing their misuse while preserving their tremendous potential for beneficial applications. This requires continuous innovation in our safety approaches and close collaboration with the broader security and safety community.

In all the above mentioned cases we banned the accounts associated with the violative activity. In addition we are always improving our detecting methods to detect adversarial use of our models, each case of abuse described fed into our broader set of controls to prevent and more quickly detect and prevent adversarial use of our models.

We hope this report provides insights our industry, governments, and the wider research community can use to strengthen the AI industry’s collective defenses against online abuses.


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
