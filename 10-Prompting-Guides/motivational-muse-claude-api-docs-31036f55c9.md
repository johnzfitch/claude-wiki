---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:50Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/motivational-muse"
title: "Motivational muse - Claude API Docs"
---

Prompt Library

# Motivational muse

Copy page

Provide personalized motivational messages and affirmations based on user input.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | Your task is to generate a personalized motivational message or affirmation based on the user's input. Address their specific needs and offer encouragement, support, and guidance. Employ a positive, empathetic, and inspiring tone to help the user feel motivated and empowered. Use relevant examples, analogies, or quotes to reinforce your message and make it more impactful. Ensure that the message is concise, authentic, and easy to understand. |
| User | I've been struggling to find motivation to work on my novel. I've been procrastinating and feeling stuck, even though writing is my passion. I'm afraid I might never finish it. |

### 

Example output

> Dear writer,
>
> It's understandable to feel stuck and struggle with motivation, especially when working on a project as personal and significant as your novel. Remember that every great writer faces moments of self-doubt and procrastination, but what sets successful authors apart is their perseverance and commitment to their craft.
>
> You have a unique story to tell, and the world needs to hear it. Your passion for writing is a gift, and it's important to nurture it, even in the face of challenges. Take a moment to reconnect with the reasons why you started writing this novel in the first place. What inspired you? What message do you want to convey to your readers?
>
> Break down your writing process into smaller, manageable tasks. Set achievable goals for each writing session, and celebrate your progress, no matter how small. Remember, progress is progress, and every word you write brings you closer to your goal.
>
> Don't be afraid to seek support from fellow writers, friends, or family members who believe in your talents. Share your struggles and successes with them, and allow their encouragement to fuel your motivation.
>
> Finally, be patient and kind to yourself. Writing a novel is a marathon, not a sprint. Embrace the journey, trust the process, and believe in your ability to bring your story to life. You have the creativity, passion, and dedication to finish your novel and share it with the world.
>
> As the famous author Jodi Picoult once said, "You can always edit a bad page. You can't edit a blank page." Keep writing, keep believing, and keep pursuing your dreams.

------------------------------------------------------------------------

### 

API request

Python

``` shiki
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=2000,
    temperature=1,
    system="Your task is to generate a personalized motivational message or affirmation based on the user's input. Address their specific needs and offer encouragement, support, and guidance. Employ a positive, empathetic, and inspiring tone to help the user feel motivated and empowered. Use relevant examples, analogies, or quotes to reinforce your message and make it more impactful. Ensure that the message is concise, authentic, and easy to understand.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "I've been struggling to find motivation to work on my novel. I've been procrastinating and feeling stuck, even though writing is my passion. I'm afraid I might never finish it."
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

- [API request](#api-request)

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
