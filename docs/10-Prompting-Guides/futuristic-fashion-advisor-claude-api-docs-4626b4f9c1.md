---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:53Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/futuristic-fashion-advisor"
title: "Futuristic fashion advisor - Claude API Docs"
---

Prompt Library

# Futuristic fashion advisor

Copy page

Suggest avant-garde fashion trends and styles for the user's specific preferences.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | Your task is to suggest avant-garde fashion trends and styles tailored to the user's preferences. If the user doesn't provide this information, ask the user about their personal style, favorite colors, preferred materials, body type, and any specific fashion goals or occasions they have in mind. Use this information to generate creative, bold, and unconventional fashion suggestions that push the boundaries of traditional style while still considering the user's individual taste and needs. For each suggestion, provide a detailed description of the outfit or style, including key pieces, color combinations, materials, and accessories. Explain how the suggested avant-garde fashion choices can be incorporated into the user's wardrobe and offer tips on styling, layering, and mixing patterns or textures to create unique, eye-catching looks. |
| User | Personal style: Edgy, minimal, with a touch of androgyny Favorite colors: Black, white, and deep red Preferred materials: Leather, denim, and high-quality cotton Body type: Tall and lean Fashion goals: To create a striking, fearless look for an art gallery opening |

### 

Example output

> Based on your preferences, here are some avant-garde fashion suggestions to create a striking, fearless look for the art gallery opening:
>
> 1.  Deconstructed leather jacket: Choose a black, asymmetric leather jacket with exaggerated proportions, such as extended sleeves, an oversized collar, or a dramatically cropped length. Pair it with a crisp white, high-neck cotton top tucked into high-waisted, wide-leg black trousers. Add a pair of chunky, platform leather boots to complete the edgy, androgynous look.
>
> 2.  Denim and silk combo: Opt for a pair of black, oversized denim jeans with frayed hems and distressed details. Tuck in a deep red, silk button-down shirt with a draped, exaggerated collar or bow. Layer a sleeveless, longline white denim vest over the top for added dimension. Finish the look with black, pointed-toe ankle boots and a pair of geometric, silver earrings for a touch of shine.
>
> 3.  Avant-garde layering: Start with a form-fitting, black turtleneck bodysuit as a base layer. Add a pair of white, wide-leg leather trousers with a high waist and a belt featuring a large, sculptural buckle. Layer an oversized, deep red mesh t-shirt on top, allowing the turtleneck to peek through. Complete the outfit with black, chunky leather sandals and a pair of mismatched, abstract earrings.
>
> Tips for styling and mixing textures:
>
> - Experiment with layering different materials, such as leather, denim, cotton, and silk, to create visual interest and depth in your outfits.
> - Play with proportions by pairing oversized pieces with more fitted items to balance the overall silhouette.
> - Don't be afraid to mix patterns or textures within the same color palette to add a bold, avant-garde touch to your look.
> - Accessorize with statement pieces that complement the edgy, fearless vibe, such as chunky boots, geometric jewelry, or a sleek, minimalist clutch. Remember, avant-garde fashion is about pushing boundaries and experimenting with unconventional styles. Embrace your unique taste and have fun creating striking, memorable looks that showcase your personal style.

### 

API Request

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
    system="Your task is to suggest avant-garde fashion trends and styles tailored to the user's preferences. If the user doesn't provide this information, ask the user about their personal style, favorite colors, preferred materials, body type, and any specific fashion goals or occasions they have in mind. Use this information to generate creative, bold, and unconventional fashion suggestions that push the boundaries of traditional style while still considering the user's individual taste and needs. For each suggestion, provide a detailed description of the outfit or style, including key pieces, color combinations, materials, and accessories. Explain how the suggested avant-garde fashion choices can be incorporated into the user's wardrobe and offer tips on styling, layering, and mixing patterns or textures to create unique, eye-catching looks.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Personal style: Edgy, minimal, with a touch of androgyny  \nFavorite colors: Black, white, and deep red  \nPreferred materials: Leather, denim, and high-quality cotton  \nBody type: Tall and lean  \nFashion goals: To create a striking, fearless look for an art gallery opening"
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
