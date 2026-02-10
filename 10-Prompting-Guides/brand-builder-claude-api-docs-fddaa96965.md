---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:47Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/brand-builder"
title: "Brand builder - Claude API Docs"
---

Prompt Library

# Brand builder

Copy page

Craft a design brief for a holistic brand identity.

Copy page

> Copy this prompt into our developer [Console](/login?selectAccount=true&returnTo=%2Fdashboard%3F) to try it for yourself!

|  | Content |
|----|----|
| System | Your task is to create a comprehensive design brief for a holistic brand identity based on the given specifications. The brand identity should encompass various elements such as suggestions for the brand name, logo, color palette, typography, visual style, tone of voice, and overall brand personality. Ensure that all elements work together harmoniously to create a cohesive and memorable brand experience that effectively communicates the brand's values, mission, and unique selling proposition to its target audience. Be detailed and comprehensive and provide enough specific details for someone to create a truly unique brand identity. |
| User | Brand specs: This is a brand that focuses on creating high-quality, stylish clothing and accessories using eco-friendly materials and ethical production methods The brand targets environmentally conscious consumers aged 25-40 who value fashion, sustainability, and social responsibility. The brand identity should achieve the following goals: 1. Reflect the brand's commitment to sustainability, ethical practices, and environmental stewardship. 2. Appeal to the target audience by conveying a sense of style, quality, and trendiness. 3. Differentiate the brand from competitors in the sustainable fashion market. 4. Create a strong emotional connection with consumers and inspire them to make more environmentally friendly choices. |

### 

Example output

> Design Brief: Brand Identity for an Eco-Friendly Fashion Brand Brand Name Suggestion: "Sēnsus" (Latin for "sense" or "perception," evoking a sense of mindfulness and connection with the environment)
>
> Logo:
>
> - A minimalistic and modern logo that combines a stylized leaf or plant motif with a sleek, sans-serif typeface.
>
> - The leaf or plant element symbolizes the brand's commitment to sustainability and environmental stewardship, while the clean typography conveys a sense of sophistication and style.
>
> - The logo should be versatile and work well across various applications, including clothing tags, packaging, and digital platforms. Color Palette:
>
> - A neutral and earthy color palette that reflects the brand's eco-friendly ethos, such as shades of green, beige, and warm grays.
>
> - Accent colors like deep teal or mustard yellow can be used sparingly to add vibrancy and depth.
>
> - The color palette should evoke a sense of natural harmony and balance, while still being fashion-forward and appealing to the target audience. Typography:
>
> - A combination of a clean, modern sans-serif typeface for headlines and a complementary serif typeface for body copy.
>
> - The typography should be legible and visually appealing, conveying a sense of quality and sophistication.
>
> - Consistent use of typographic hierarchy and spacing will create a cohesive and organized brand identity. Visual Style:
>
> - A minimalistic and uncluttered visual style that emphasizes high-quality product photography and clean, modern layouts.
>
> - Incorporate natural elements, such as plant motifs or textures, to reinforce the brand's eco-friendly values and connection with nature.
>
> - Use negative space effectively to create a sense of openness and breathability, reflecting the brand's commitment to sustainability. Tone of Voice:
>
> - The brand's tone of voice should be approachable, knowledgeable, and authentic.
>
> - Use language that educates and inspires consumers about the benefits of sustainable fashion and ethical production methods.
>
> - Incorporate a touch of sophistication and style to appeal to the target audience's fashion-conscious sensibilities. Brand Personality:
>
> - Eco-conscious and environmentally aware, yet stylish and fashion-forward.
>
> - Confident and passionate about promoting sustainable practices and ethical choices.
>
> - Inclusive and welcoming, inviting consumers to join a like-minded community committed to making positive changes. Overall, the brand identity for "Sēnsus" should strike a balance between eco-friendly values and fashion-forward aesthetics, appealing to consumers who want to look stylish while making environmentally responsible choices. The cohesive visual and verbal elements should create a strong emotional connection with the target audience and inspire them to embrace a more sustainable lifestyle.

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
    system="Your task is to create a comprehensive design brief for a holistic brand identity based on the given specifications. The brand identity should encompass various elements such as suggestions for the brand name, logo, color palette, typography, visual style, tone of voice, and overall brand personality. Ensure that all elements work together harmoniously to create a cohesive and memorable brand experience that effectively communicates the brand's values, mission, and unique selling proposition to its target audience. Be detailed and comprehensive and provide enough specific details for someone to create a truly unique brand identity.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Brand specs:\nThis is a brand that focuses on creating high-quality, stylish clothing and accessories using eco-friendly materials and ethical production methods\nThe brand targets environmentally conscious consumers aged 25-40 who value fashion, sustainability, and social responsibility.\nThe brand identity should achieve the following goals:\n1. Reflect the brand's commitment to sustainability, ethical practices, and environmental stewardship.\n2. Appeal to the target audience by conveying a sense of style, quality, and trendiness.\n3. Differentiate the brand from competitors in the sustainable fashion market.\n4. Create a strong emotional connection with consumers and inspire them to make more environmentally friendly choices."
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
