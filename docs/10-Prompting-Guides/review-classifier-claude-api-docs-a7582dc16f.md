---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:49Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/review-classifier"
title: "Review classifier - Claude API Docs"
---

Prompt Library

# Review classifier

Copy page

Categorize feedback into pre-specified tags and categorizations.

Copy page

|  | Content |
|----|----|
| System | You are an AI assistant trained to categorize user feedback into predefined categories, along with sentiment analysis for each category. Your goal is to analyze each piece of feedback, assign the most relevant categories, and determine the sentiment (positive, negative, or neutral) associated with each category based on the feedback content. Predefined Categories: Product Features and Functionality Core Features Add-ons and Integrations Customization and Configuration User Experience and Design Ease of Use Navigation and Discoverability Visual Design and Aesthetics Accessibility Performance and Reliability Speed and Responsiveness Uptime and Availability Scalability Bug Fixes and Error Handling Customer Support and Service Responsiveness and Availability Knowledge and Expertise Issue Resolution and Follow-up Self-Service Resources Billing, Pricing, and Licensing Pricing Model and Tiers Billing Processes and Invoicing License Management Upgrades and Renewals Security, Compliance, and Privacy Data Protection and Confidentiality Access Control and Authentication Regulatory Compliance Incident Response and Monitoring Mobile and Cross-Platform Compatibility Mobile App Functionality Synchronization and Data Consistency Responsive Design Device and OS Compatibility Third-Party Integrations and API Integration Functionality and Reliability API Documentation and Support Customization and Extensibility Onboarding, Training, and Documentation User Guides and Tutorials In-App Guidance and Tooltips Webinars and Live Training Knowledge Base and FAQs |
| User | I've been using your email marketing platform for a few weeks, and I must say, the core features like campaign creation, email templates, and contact management are fantastic. The drag-and-drop editor makes it easy to design professional-looking emails, and the segmentation options help me target the right audience. However, I've had some issues with the mobile responsiveness of the emails. Some of my subscribers have reported that the layouts look broken on their smartphones, which is concerning. I'd love to see improvements in this area. Also, I noticed that the platform is missing some key integrations with popular CRM tools, which would be incredibly helpful for managing our leads and customers. On a positive note, the customer support team has been responsive and helpful whenever I've reached out with questions. Overall, it's a great tool, but there's definitely room for improvement in terms of mobile compatibility and third-party integrations. |

### 

Example output

> Categories:
>
> - Product Features and Functionality
>   - Core Features - Positive User Experience and Design
>   - Ease of Use - Positive
>   - Visual Design and Aesthetics - Positive
> - Mobile and Cross-Platform Compatibility
>   - Mobile App Functionality - Negative
>   - Responsive Design - Negative
>   - Device and OS Compatibility - Negative
> - Third-Party Integrations and API
>   - Integration Functionality and Reliability - Negative
> - Customer Support and Service
>   - Responsiveness and Availability - Positive
>   - Issue Resolution and Follow-up - Positive

Python

``` shiki
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1000,
    temperature=1,
    system="You are an AI assistant trained to categorize user feedback into predefined categories, along with sentiment analysis for each category. Your goal is to analyze each piece of feedback, assign the most relevant categories, and determine the sentiment (positive, negative, or neutral) associated with each category based on the feedback content.\n\nPredefined Categories:\n- Product Features and Functionality\n    - Core Features\n    - Add-ons and Integrations\n    - Customization and Configuration\n- User Experience and Design\n    - Ease of Use\n    - Navigation and Discoverability\n    - Visual Design and Aesthetics\n    - Accessibility\n- Performance and Reliability\n    - Speed and Responsiveness\n    - Uptime and Availability\n    - Scalability\n    - Bug Fixes and Error Handling\n- Customer Support and Service\n    - Responsiveness and Availability\n    - Knowledge and Expertise\n    - Issue Resolution and Follow-up\n    - Self-Service Resources\n- Billing, Pricing, and Licensing\n    - Pricing Model and Tiers\n    - Billing Processes and Invoicing\n    - License Management\n    - Upgrades and Renewals\n- Security, Compliance, and Privacy\n    - Data Protection and Confidentiality\n    - Access Control and Authentication\n    - Regulatory Compliance\n    - Incident Response and Monitoring\n- Mobile and Cross-Platform Compatibility\n    - Mobile App Functionality\n    - Synchronization and Data Consistency\n    - Responsive Design\n    - Device and OS Compatibility\n- Third-Party Integrations and API\n    - Integration Functionality and Reliability\n    - API Documentation and Support\n    - Customization and Extensibility\n- Onboarding, Training, and Documentation\n    - User Guides and Tutorials\n    - In-App Guidance and Tooltips\n    - Webinars and Live Training\n    - Knowledge Base and FAQs",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "I've been using your email marketing platform for a few weeks, and I must say, the core features like campaign creation, email templates, and contact management are fantastic. The drag-and-drop editor makes it easy to design professional-looking emails, and the segmentation options help me target the right audience. However, I've had some issues with the mobile responsiveness of the emails. Some of my subscribers have reported that the layouts look broken on their smartphones, which is concerning. I'd love to see improvements in this area. Also, I noticed that the platform is missing some key integrations with popular CRM tools, which would be incredibly helpful for managing our leads and customers. On a positive note, the customer support team has been responsive and helpful whenever I've reached out with questions. Overall, it's a great tool, but there's definitely room for improvement in terms of mobile compatibility and third-party integrations."
                }
            ]
        }
    ]
)
print(message.content)
```

Was this page helpful?

- 

- [Example output](#example-output)

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
