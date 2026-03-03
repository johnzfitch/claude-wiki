---
category: "10-Prompting-Guides"
fetched_at: "2026-03-03T14:56:25Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/memo-maestro"
title: "Memo maestro - Claude API Docs"
---

# Memo maestro


Compose comprehensive company memos based on key points.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

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

Partnerships and Discounts: To further support your wellness journey, we have partnered with local gyms and wellness centers to offer discounted memberships exclusively for our employees. Take advantage of these special rates to access a wide range of fitness facilities and classes.

Incentives for Participation: To encourage active participation in the Fit4Success program, we will be offering the following incentives:

- Fitness trackers for all participants to monitor their progress and set personal goals
- Wellness points earned through program participation, redeemable for additional rewards
- Monthly prize drawings for participants who meet specific wellness milestones

Enrollment Process: To enroll in the Fit4Success program, please visit our company intranet and complete the online registration form. The deadline for enrollment is May 25, 2023. If you have any questions or concerns about the enrollment process, please contact our Human Resources team.

Program Coordination: The Fit4Success program will be jointly coordinated by our Human Resources and Employee Engagement teams. They will be available to provide guidance, support, and resources throughout your wellness journey.

We strongly believe that investing in the well-being of our employees is crucial to the success and growth of our organization. We encourage you to take advantage of this exciting opportunity and join us in creating a healthier, happier, and more productive workplace.

Let's embrace the Fit4Success program and work together towards a healthier future!

Best regards, \[Your Name\] \[Your Title\]

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
                    "text": '- Announcement of a new employee wellness program: "Fit4Success"  \n- Program objectives: promote physical and mental well-being, reduce stress, and increase productivity  \n- Components: on-site fitness classes, healthy meal options, mental health resources, and wellness workshops  \n- Partnership with local gyms and wellness centers for discounted memberships  \n- Incentives for participation: fitness trackers, wellness points, and prize drawings  \n- Program launch date: June 1, 2023  \n- Enrollment process: online registration through company intranet  \n- Program coordinators: Human Resources and Employee Engagement teams',
                }
            ],
        }
    ],
)
print(message.content)
```
