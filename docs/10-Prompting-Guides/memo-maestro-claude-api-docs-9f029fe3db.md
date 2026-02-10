---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:42Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/memo-maestro"
title: "Memo maestro - Claude API Docs"
---

Prompt Library

# Memo maestro

Copy page

Compose comprehensive company memos based on key points.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

[TABLE]

## 

Example Output

Subject: Introducing Fit4Success - Our New Employee Wellness Program

Hi all,

I am thrilled to announce the launch of our new employee wellness program, Fit4Success, designed to promote physical and mental well-being, reduce stress, and increase productivity among our team members. The program will officially commence on June 1, 2023.

Program Objectives:

- Encourage regular physical activity and healthy lifestyle choices
- Provide resources and support for mental health and stress management
- Foster a positive and engaging work environment that prioritizes employee well-being
- Enhance overall productivity and job satisfaction

Program Components:

- On-site fitness classes: yoga, Pilates, and high-intensity interval training (HIIT) sessions
- Healthy meal options: nutritious snacks and meals available in the company cafeteria
- Mental health resources: access to counseling services, meditation apps, and stress-relief workshops
- Wellness workshops: seminars on topics such as nutrition, sleep hygiene, and work-life balance

Partnerships and Discounts:  
To further support your wellness journey, we have partnered with local gyms and wellness centers to offer discounted memberships exclusively for our employees. Take advantage of these special rates to access a wide range of fitness facilities and classes.

Incentives for Participation:  
To encourage active participation in the Fit4Success program, we will be offering the following incentives:

- Fitness trackers for all participants to monitor their progress and set personal goals
- Wellness points earned through program participation, redeemable for additional rewards
- Monthly prize drawings for participants who meet specific wellness milestones

Enrollment Process:  
To enroll in the Fit4Success program, please visit our company intranet and complete the online registration form. The deadline for enrollment is May 25, 2023. If you have any questions or concerns about the enrollment process, please contact our Human Resources team.

Program Coordination:  
The Fit4Success program will be jointly coordinated by our Human Resources and Employee Engagement teams. They will be available to provide guidance, support, and resources throughout your wellness journey.

We strongly believe that investing in the well-being of our employees is crucial to the success and growth of our organization. We encourage you to take advantage of this exciting opportunity and join us in creating a healthier, happier, and more productive workplace.

Let's embrace the Fit4Success program and work together towards a healthier future!

Best regards,  
\[Your Name\]  
\[Your Title\]

------------------------------------------------------------------------

## 

API Request

Python

Python

TypeScript

TypeScript

AWS Bedrock Python

AWS Bedrock Python

AWS Bedrock TypeScript

AWS Bedrock TypeScript

Vertex AI Python

Vertex AI Python

Vertex AI TypeScript

Vertex AI TypeScript

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
    system="Your task is to compose a comprehensive company memo based on the provided key points. The memo should be written in a professional tone, addressing all the relevant information in a clear and concise manner. Use appropriate formatting, such as headings, subheadings, and bullet points, to organize the content effectively. Ensure that the memo is well-structured, coherent, and easy to understand for the intended audience.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "- Announcement of a new employee wellness program: \"Fit4Success\"  \n- Program objectives: promote physical and mental well-being, reduce stress, and increase productivity  \n- Components: on-site fitness classes, healthy meal options, mental health resources, and wellness workshops  \n- Partnership with local gyms and wellness centers for discounted memberships  \n- Incentives for participation: fitness trackers, wellness points, and prize drawings  \n- Program launch date: June 1, 2023  \n- Enrollment process: online registration through company intranet  \n- Program coordinators: Human Resources and Employee Engagement teams"
                }
            ]
        }
    ]
)
print(message.content)
```

Was this page helpful?

- 

- [Example Output](#example-output)

- [API Request](#api-request)

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
