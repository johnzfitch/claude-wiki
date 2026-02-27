---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:52Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/alliteration-alchemist"
title: "Alliteration alchemist - Claude API Docs"
---

Prompt Library

# Alliteration alchemist

Copy page

Generate alliterative phrases and sentences for any given subject.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | Your task is to create alliterative phrases and sentences for the given subject. Ensure that the alliterations not only sound pleasing but also convey relevant information or evoke appropriate emotions related to the subject. |
| User | Ocean |

### 

Example output

> 1.  Whispering waves wash over the shore.
> 2.  Salty sea spray splashes on the sand.
> 3.  Crashing currents carve coastal cliffs.
> 4.  Deep, dark depths disguise hidden dangers.
> 5.  Bubbling brooks bring life to the beach.
> 6.  Mighty, majestic mammals migrate through the waters.
> 7.  Thundering tides toss ships to and fro.
> 8.  Shimmering shoals shelter secretive sea creatures.
> 9.  Rippling reflections reveal a world beneath the surface.
> 10. Swirling, surging seas shape the shoreline.
> 11. Foaming, frothing floes flow freely.
> 12. Graceful gulls glide above the glistening ocean.
> 13. Playful porpoises plunge through the pristine waters.
> 14. Briny breezes blow across the boundless blue.
> 15. Rhythmic ripples roll towards the rocky coast.
> 16. Coral caves conceal colorful aquatic communities.
> 17. Stormy skies and swelling seas signal nature's might.
> 18. Tumbling tides transform the tranquil bay.
> 19. Whirling, whooshing winds whip up the waves.
> 20. Serene, sapphire waters stretch to the horizon.

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
    max_tokens=1000,
    temperature=1,
    system="Your task is to create alliterative phrases and sentences for the given subject. Ensure that the alliterations not only sound pleasing but also convey relevant information or evoke appropriate emotions related to the subject.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Ocean"
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
