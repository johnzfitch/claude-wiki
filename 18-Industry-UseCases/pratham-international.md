---
title: "Pratham International Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/pratham-international"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:31:46Z"
tags: ["api", "case-studies", "enterprise", "security"]
---

# How Pratham delivers personalized assessment feedback to thousands of students across India with Claude

[Try Claude](https://claude.ai)

Industry:  
Beneficial Deployments

Company size:  
Large

Product:  
Claude Platform

Location:  
India

1,500+ student assessments

completed across 20 schools

30% → 80% grading accuracy

through iterative prompt engineering with Anthropic

Nonprofits

Turn limited resources into lasting impact. Generate grant proposals, track program outcomes, and free your team to focus on serving your community.

[Read more](nonprofits.md)

Education

Trusted, responsible AI tools for students and educators, from personalized learning to research assistance.

[Read more](education.md)

[Pratham](https://pratham.org/) is one of the world’s largest education nonprofits. Founded 30 years ago in India, the organization reaches millions of children annually through programs spanning early literacy to vocational training. Its methods have been validated through more than 10 randomized controlled trials, including studies by MIT's J-PAL. The World Bank has also recognized the Pratham method as one of the best investments in education for global education. Today, Pratham’s programs operate in nearly every Indian state and have been adopted in more than 30 countries.

## With Claude, Pratham achieved:

- **1,500+ student assessments** completed across 20 schools
- **30% → 80% grading accuracy** through iterative prompt engineering with Anthropic
- **90% accuracy** in generating questions aligned to Bloom's Taxonomy—the universal educational framework for assessing everything from basic factual recall to complex, higher-order reasoning

## The challenge: Thousands of practice exams, no way to give individual feedback

In classrooms across India, assessments tend to tell students their results but not how to improve. A teacher managing 60 or more students has little time to provide individualized feedback on each practice exam, and the students who need that feedback the most—those in under-resourced schools and communities—are the least likely to get it. The information exists in their answers, but the problem is turning it into something a student can actually act on.

Pratham has spent 30 years working on exactly these kinds of gaps. But even with a track record of large-scale impact, Pratham kept running into a fundamental constraint: there were never enough people to grade enough practice exams to give students the repetition and feedback they needed.

The issue became especially clear in Pratham's Second Chance program, which helps young women who dropped out of school prepare for India's 10th-grade board exam, a credential required for many jobs. The program serves women without access to trained subject-matter instructors. "These women didn’t get a chance to practice the exam enough times because we didn't have enough people to grade all those answers," said Nishant Baghel, Director of Technology Innovations at Pratham and a visiting scientist at MIT Media Lab. The bottleneck wasn't curriculum or motivation. It was grading.

Pratham's ATM had already reached more than 4,000 learners and auto-graded roughly 8,000 assessments across six Indian states through the Second Chance Program. But the system was challenging to scale: grading could be inconsistent, and there was no structured way to measure accuracy against curriculum standards.

## The solution: Designing an automated assessment and feedback engine for real classroom conditions

That constraint led Pratham to create the Anytime Testing Machine, or ATM: an end-to-end practice assessment system that uses Claude to generate curriculum-aligned questions, digitize handwritten student answers, grade them against structured rubrics, and deliver personalized feedback. The system is designed for the conditions Pratham actually works in. Students write answers by hand on paper and photograph them. The system converts those images to text, then Claude evaluates the responses for content, accuracy, and expression.

Pratham chose Claude after running evaluations across multiple models. "Claude did consistently well across tasks including question generation, checking the quality of generated questions, grading, and feedback," said Sravana Chandra, AI Lead at Pratham. "This, along with Anthropic's focus on safety and responsible AI, led us to choose Claude over other LLMs."

The collaboration was hands-on. Anthropic and Pratham teams met one to two times per week over several months, not just to integrate the model but to calibrate every stage of the pipeline. Grading accuracy started at around 30% when measured against expert-reviewed benchmarks. Through iterative prompt refinement and evaluation design, the teams brought that number to roughly 80%. “We implemented an LLM-as-a-judge framework, benchmarking model evaluations against internally developed golden datasets that were manually validated by subject matter experts,” Chandra explained.

On the feedback generation side, Claude's multilingual fluency was a key advantage. “Given Claude’s linguistic capabilities, it was readily able to handle feedback generation in a mix of Hindi and English, using English terms where relevant (such as for scientific terms) while keeping most of the text in Hindi,” Chandra said.

## The approach: Keeping teachers at the center

A core design principle throughout: teachers review and can refine AI-generated feedback before it reaches students. It reflects Pratham's belief that the teacher's role becomes more important, not less, when AI enters the classroom.

The response from educators has borne that out. Teachers report that automating the grading frees them to focus on targeted instruction rather than administrative work. "Teachers feel empowered because they remain the final evaluators who validate AI feedback before it reaches the student," Chandra noted. The system acts as a capacity multiplier: instead of replacing judgment, it gives teachers better information to exercise it.

For students, the shift is about dignity as much as scores. In these settings, receiving a grade without explanation can be discouraging. Claude's feedback gives learners something specific to work with. Rather than seeing a wrong answer with no context, a student receives a concrete explanation of the concept they missed, with a clear direction for what to study next.

"Human agency is something we focus on,” Baghel says. “Instead of asking what AI can do without teachers, we ask: how can AI help our teachers and students exactly where they're stuck?”

## The results: Personalized feedback reaching learners across six states

With Claude, the ATM now delivers 90% accuracy in generating questions aligned to Bloom's Taxonomy, the global educational framework. On the grading front, accuracy is roughly 80% aligned with content experts on rubric-based scoring. The Claude-powered system has completed more than 1,500 student assessments across 20 schools, with plans to expand to hundreds of thousands of students across India. Separately, the Second Chance program, which currently serves 15,000 women preparing for the grade 10 exam, plans to migrate fully to the Claude-powered pipeline by the end of 2026.

"AI tools like Claude give us a way to reimagine learning for students who do not have access to advanced educational resources," said Madhav Chavan, Pratham's co-founder. "In addition to providing personalized support to understand the textbook, the ATM innovation will help children verify and authenticate their knowledge beyond the textbooks."

## What’s next: Flipping the education system

Chavan sees assessment as just the starting point for something larger: a system where students can eventually be tested on any topic, not only what the curriculum prescribes, and receive a credential for what they actually know.

"Instead of asking children questions about the curriculum, ask them what they know," Chavan said. "If we flip that, we can flip the education system from being a filtration mechanism to one that offers differentiated pathways based on a child's interests and background knowledge. Before AI, this was not possible."

The partnership is already expanding. Anthropic will support Pratham's Tech in TaRL (Teaching at the Right Level) initiative, an AI-powered teacher support system with a randomized controlled trial planned for several thousand students. The two organizations are also exploring educational digital public infrastructure (including knowledge graphs), as well as geographic expansion to Kenya, Rwanda, and communities across the Global South. Pratham's three-year goal is to evolve the ATM into a learning and credentialing engine that recognizes competencies gained through non-linear pathways, available to learners worldwide.

## Related stories


### Mercy Corps on what AI makes possible in humanitarian work


### Mercy Corps accelerates global humanitarian response to community feedback with Claude


### The Epilepsy Foundation turns years of expert content into a personal epilepsy assistant with Claude


### How the Epilepsy Foundation uses Claude across the organization

[](https://www.claude.com/)

© 2026 Anthropic PBC

## Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Download app](https://www.claude.com/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](https://www.claude.com/features/artifacts)
- [Design](../15-Claude-AI-Features/product-design.md)
- [Connectors](https://www.claude.com/marketplace/connectors-plugins)
- [Plugins](https://www.claude.com/marketplace/plugins)
- [Skills](https://www.claude.com/skills)

## Extensions

- [Claude in Chrome](https://www.claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://www.claude.com/claude-for-microsoft-365)

## Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

## Enterprise

- [Overview](enterprise.md)
- [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)

## Departments

- [Customer support](customer-support.md)
- [Cybersecurity](cybersecurity.md)
- [Legal](legal.md)
- [Sales](sales.md)

## Industries

- [Financial services](finance.md)
- [Government](government.md)
- [Healthcare](healthcare.md)
- [Higher education](education.md)
- [K-12 teachers](teachers.md)
- [Life sciences](life-sciences.md)
- [Nonprofits](nonprofits.md)
- [Small business](small-business.md)

## Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

## Developers

- [Developer docs](../02-Claude-Code-CLI/code-home.md)
- [Developer blog](https://claude.dev)
- [Community](https://www.claude.com/community)
- [Console](../04-API-Reference/Other/home.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](https://www.claude.com/platform/api)
- [Marketplace](https://www.claude.com/marketplace)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)

## Resources

- [Blog](https://www.claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](customers.md)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](https://www.claude.com/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](https://www.claude.com/check-files)
- [Regional compliance](https://www.claude.com/regional-compliance)
- [Report abuse](https://www.claude.com/form/anthropic-content-reporting)
- [Security and compliance](https://trust.anthropic.com/)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

## Company

- [Anthropic](https://www.anthropic.com/)
- [Careers](https://www.anthropic.com/careers)
- [Policy](https://www.anthropic.com/policy)
- [Research](../19-Reference/anthropic-com-research.md)
- [Anthropic news](../19-Reference/news.md)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](../19-Reference/announcing-our-updated-responsible-scaling-policy.md)
- [Transparency](https://anthropic.com/transparency)

## Terms and policies

- Privacy choices
- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Terms of Service: US K-12](https://anthropic.com/legal/k12-terms)
- [Data Processing Agreement: US K-12](https://anthropic.com/legal/k12-dpa)
- [Usage Policy](https://www.anthropic.com/legal/aup)

## Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Download app](https://www.claude.com/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](https://www.claude.com/features/artifacts)
- [Design](../15-Claude-AI-Features/product-design.md)
- [Connectors](https://www.claude.com/marketplace/connectors-plugins)
- [Plugins](https://www.claude.com/marketplace/plugins)
- [Skills](https://www.claude.com/skills)

## Extensions

- [Claude in Chrome](https://www.claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://www.claude.com/claude-for-microsoft-365)

## Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

## Enterprise

- [Overview](enterprise.md)
- [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)

## Departments

- [Customer support](customer-support.md)
- [Cybersecurity](cybersecurity.md)
- [Legal](legal.md)
- [Sales](sales.md)

## Industries

- [Financial services](finance.md)
- [Government](government.md)
- [Healthcare](healthcare.md)
- [Higher education](education.md)
- [K-12 teachers](teachers.md)
- [Life sciences](life-sciences.md)
- [Nonprofits](nonprofits.md)
- [Small business](small-business.md)

## Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

## Developers

- [Developer docs](../02-Claude-Code-CLI/code-home.md)
- [Developer blog](https://claude.dev)
- [Community](https://www.claude.com/community)
- [Console](../04-API-Reference/Other/home.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](https://www.claude.com/platform/api)
- [Marketplace](https://www.claude.com/marketplace)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)

## Resources

- [Blog](https://www.claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](customers.md)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](https://www.claude.com/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](https://www.claude.com/check-files)
- [Regional compliance](https://www.claude.com/regional-compliance)
- [Report abuse](https://www.claude.com/form/anthropic-content-reporting)
