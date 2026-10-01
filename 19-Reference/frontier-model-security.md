---
title: "Frontier model security \\ Anthropic"
source_url: "https://www.anthropic.com/news/frontier-model-security"
category: "19-Reference"
fetched_at: "2026-09-10T06:45:06Z"
tags: ["news-research", "security"]
---

# Frontier model security

Jul 25, 2023

As the capabilities of frontier artificial intelligence models continue to increase rapidly, ensuring the security of these systems has become a critical priority. In our previous posts, we’ve focused on Anthropic’s [approach to safety](core-views-on-ai-safety.md), and Claude’s capabilities and applications. In this post, we are sharing some of the steps we are taking to ensure our models are developed securely. We hope to advance public discussion about how all labs can deploy top models securely, as well as share recommendations for government regulatory approaches that encourage adoption of strong cybersecurity practices. Below we discuss some of our recommendations for cybersecurity best practices, which Anthropic itself is in the process of implementing.

## Summary

Future advanced AI models have the potential to upend economic and national security affairs within and among nation-states. Given the strategic nature of this technology, frontier AI research and models must be secured to levels far exceeding standard practices for other commercial technologies in order to protect them from theft or misuse.  
  
In the near term, governments and frontier AI labs must be ready to protect advanced models and model weights, and the research that feeds into them. This should include measures such as the development of robust best practices widely diffused among industry, as well as treating the advanced AI sector as something akin to “critical infrastructure” in terms of the level of public-private partnership in securing these models and the companies developing them.  
  
Many of these measures can begin as voluntary arrangements, but in time it may be appropriate to use government procurement or regulatory powers to mandate compliance.

## Cybersecurity Best Practices

We believe “two-party control” is necessary to secure advanced AI systems. Two-party control is already used in a range of domains; for example, two people with two keys are needed to open the most secure vaults, and multi-party review patterns have been applied in manufacturing ([GMP](https://www.who.int/teams/health-product-policy-and-standards/standards-and-specifications/gmp#:~:text=GMP%20defines%20quality%20measures%20for,the%20production%20of%20pharmaceuticals%20and), [ISO 9001](https://www.iso.org/iso-9001-quality-management.html)), food ([FSMA PCQI](https://www.sqfi.com/wp-content/uploads/2018/08/FSMA-FAQs-for-website-.pdf), [ISO 22000](https://www.iso.org/iso-22000-food-safety-management.html)), medical ([ISO 13485](https://www.iso.org/standard/59752.html)) and finance tech ([SOX](https://en.wikipedia.org/wiki/Sarbanes%E2%80%93Oxley_Act)).  

- This pattern should be applied to all systems involved in the development, training, hosting, and deployment of frontier AI models.
- This pattern is already in widespread use within major tech companies to defend against the most advanced threat actors and mitigate insider risk.
- It is manifested as a system design where no person has persistent access to production-critical environments, and they must ask a coworker for time-limited access with a business justification for that request.
- Even emerging AI labs, without large enterprise resources, can implement these controls.

  
We call this **multi-party authorization to AI-critical infrastructure design**. This is a leading security requirement that depends on the gamut of cybersecurity best practices to implement correctly.  
  
In addition, secure software development practices should pervade the frontier AI model environment. The gold-standard for these practices are the NIST [Secure Software Development Framework](https://csrc.nist.gov/Projects/ssdf) (SSDF) and the [Supply Chain Levels for Software Artifacts](https://slsa.dev/) (SLSA). Executive Orders have been leveraged successfully to encourage major tech companies to adopt higher development standards: in 2021, [EO 14028](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) directed OMB to set Federal Procurement guidelines. This motivated action: the software industry has invested heavily to meet the SSDF’s requirements to retain federal contracts.  
  
While frontier AI research is already benefiting from the implementation of some of these standards by dint of cloud providers hosting their models, applying these existing standards can step-change the security of these AI systems:  
  
SSDF and SLSA are largely translatable into the development of models and their coupled software; producing a model and then deploying it is almost identical to building software and then deploying it.  
  
SSDF and SLSA coupled together mean that any AI system deployed has a chain of custody. By this, we mean that when applied correctly these practices make it so you are able to tie back a deployed model to the company that developed it, which helps provide provenance.  
  
We call this a **secure model development framework**. We encourage extending SSDF to encompass model development inside of NIST’s standard-setting process.  
  
In the near term, these two best practices could be established as procurement requirements applying to AI companies and cloud providers contracting with governments – alongside standard cybersecurity practices that also apply to these companies. As U.S. cloud providers provide the infrastructure that many current frontier model companies use, procurement requirements will have an effect similar to broad market regulation and can work in advance of regulatory requirements.  
  
Anthropic is implementing two-party controls, SSDF, SLSA, and other cybersecurity best practices. As model capabilities scale, we will need to further enhance security protections, moving beyond the above recommendations. This will necessarily be an iterative process in consultation with government and industry.  

## Public-Private Cooperation

Frontier AI research labs should participate in public-private cooperation in the same way as companies in critical infrastructure sectors like financial services. This sector could be designated as a special sub-sector of the existing IT sector, for example. Such a designation would be a vehicle for enhanced cooperation and information sharing between and among industry labs and government agencies, helping all labs better guard against highly resourced malicious cyber actors.

## Conclusion

It can be tempting to deprioritize security: when everything is going well, it can feel like it isn’t necessary or that it is in tension with other company goals. But this technology is becoming more powerful and will require enhanced precautions. We also believe that while security can sometimes interfere with productivity, that there are creative ways to ensure that its effects are limited and that research and other work can proceed effectively.  
  
The development of artificial intelligence has incredible potential to benefit humanity, but it also comes with risks if not pursued thoughtfully. As an AI company working on the frontier of this technology, we take our responsibility seriously to build and deploy Claude in a way that is safe, secure and aligned with human values. We will continue sharing our perspectives on the responsible development of AI.


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
