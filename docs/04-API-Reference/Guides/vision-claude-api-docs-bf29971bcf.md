---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:04:17Z"
source_url: "https://platform.claude.com/docs/en/build-with-claude/vision"
title: "Vision - Claude API Docs"
---

Capabilities

# Vision

Copy page

Claude's vision capabilities allow it to understand and analyze images, opening up exciting possibilities for multimodal interaction.

Copy page

This guide describes how to work with images in Claude, including best practices, code examples, and limitations to keep in mind.

------------------------------------------------------------------------

## 

How to use vision

Use Claude’s vision capabilities via:

- [claude.ai](https://claude.ai/). Upload an image like you would a file, or drag and drop an image directly into the chat window.
- The [Console Workbench](/workbench). A button to add images appears at the top right of every User message block.
- **API request**. See the examples in this guide.

------------------------------------------------------------------------

## 

Before you upload

### 

Basics and Limits

You can include multiple images in a single request (up to 20 for [claude.ai](https://claude.ai/) and 100 for API requests). Claude will analyze all provided images when formulating its response. This can be helpful for comparing or contrasting images.

If you submit an image larger than 8000x8000 px, it will be rejected. If you submit more than 20 images in one API request, this limit is 2000x2000 px.

While the API supports 100 images per request, there is a [32MB request size limit](/docs/en/api/overview#request-size-limits) for standard endpoints.

### 

Evaluate image size

For optimal performance, resize images before uploading if they are too large. If your image’s long edge is more than 1568 pixels, or your image is more than ~1,600 tokens, it will first be scaled down, preserving aspect ratio, until it’s within the size limits.

If your input image is too large and needs to be resized, it will increase latency of [time-to-first-token](/docs/en/about-claude/glossary), without giving you any additional model performance. Very small images under 200 pixels on any given edge may degrade performance.

To improve [time-to-first-token](/docs/en/about-claude/glossary), consider resizing images to no more than 1.15 megapixels (and within 1568 pixels in both dimensions).

Here is a table of maximum image sizes accepted by the API that will not be resized for common aspect ratios. With Claude Opus 4.6, these images use approximately 1,600 tokens and around \$4.80/1K images.

| Aspect ratio | Image size   |
|--------------|--------------|
| 1:1          | 1092x1092 px |
| 3:4          | 951x1268 px  |
| 2:3          | 896x1344 px  |
| 9:16         | 819x1456 px  |
| 1:2          | 784x1568 px  |

### 

Calculate image costs

Each image you include in a request to Claude counts towards your token usage. To calculate the approximate cost, multiply the approximate number of image tokens by the [per-token price of the model](https://claude.com/pricing) you’re using.

If your image does not need to be resized, you can estimate the number of tokens used through this algorithm: `tokens = (width px * height px)/750`

Here are examples of approximate tokenization and costs for different image sizes within the API's size constraints based on Claude Opus 4.6 per-token price of \$3 per million input tokens:

| Image size                    | \# of Tokens | Cost / image | Cost / 1K images |
|-------------------------------|--------------|--------------|------------------|
| 200x200 px(0.04 megapixels)   | ~54          | ~\$0.00016   | ~\$0.16          |
| 1000x1000 px(1 megapixel)     | ~1334        | ~\$0.004     | ~\$4.00          |
| 1092x1092 px(1.19 megapixels) | ~1590        | ~\$0.0048    | ~\$4.80          |

### 

Ensuring image quality

When providing images to Claude, keep the following in mind for best results:

- **Image format**: Use a supported image format: JPEG, PNG, GIF, or WebP.
- **Image clarity**: Ensure images are clear and not too blurry or pixelated.
- **Text**: If the image contains important text, make sure it’s legible and not too small. Avoid cropping out key visual context just to enlarge the text.

------------------------------------------------------------------------

## 

Prompt examples

Many of the [prompting techniques](/docs/en/build-with-claude/prompt-engineering/overview) that work well for text-based interactions with Claude can also be applied to image-based prompts.

These examples demonstrate best practice prompt structures involving images.

Just as with document-query placement, Claude works best when images come before text. Images placed after text or interpolated with text will still perform well, but if your use case allows it, prefer an image-then-text structure.

### 

About the prompt examples

The following examples demonstrate how to use Claude's vision capabilities using various programming languages and approaches. You can provide images to Claude in three ways:

1.  As a base64-encoded image in `image` content blocks
2.  As a URL reference to an image hosted online
3.  Using the Files API (upload once, use multiple times)

The base64 example prompts use these variables:

Shell

``` shiki
    # For URL-based images, you can use the URL directly in your JSON request
    
    # For base64-encoded images, you need to first encode the image
    # Example of how to encode an image to base64 in bash:
    BASE64_IMAGE_DATA=$(curl -s "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg" | base64)
    
    # The encoded data can now be used in your API calls
```

Below are examples of how to include images in a Messages API request using base64-encoded images and URL references:

### 

Base64-encoded image example

Shell

``` shiki
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-4-6",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "image",
            "source": {
              "type": "base64",
              "media_type": "image/jpeg",
              "data": "'"$BASE64_IMAGE_DATA"'"
            }
          },
          {
            "type": "text",
            "text": "Describe this image."
          }
        ]
      }
    ]
  }'
```

### 

URL-based image example

Shell

``` shiki
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-4-6",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "image",
            "source": {
              "type": "url",
              "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
            }
          },
          {
            "type": "text",
            "text": "Describe this image."
          }
        ]
      }
    ]
  }'
```

### 

Files API image example

For images you'll use repeatedly or when you want to avoid encoding overhead, use the [Files API](/docs/en/build-with-claude/files):

Shell

``` shiki
# First, upload your image to the Files API
curl -X POST https://api.anthropic.com/v1/files \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  -F "file=@image.jpg"

# Then use the returned file_id in your message
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-4-6",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "image",
            "source": {
              "type": "file",
              "file_id": "file_abc123"
            }
          },
          {
            "type": "text",
            "text": "Describe this image."
          }
        ]
      }
    ]
  }'
```

See [Messages API examples](/docs/en/api/messages) for more example code and parameter details.

### Example: One image

### Example: Multiple images

### Example: Multiple images with a system prompt

### Example: Four images across two conversation turns

------------------------------------------------------------------------

## 

Limitations

While Claude's image understanding capabilities are cutting-edge, there are some limitations to be aware of:

- **People identification**: Claude [cannot be used](https://www.anthropic.com/legal/aup) to identify (i.e., name) people in images and will refuse to do so.
- **Accuracy**: Claude may hallucinate or make mistakes when interpreting low-quality, rotated, or very small images under 200 pixels.
- **Spatial reasoning**: Claude's spatial reasoning abilities are limited. It may struggle with tasks requiring precise localization or layouts, like reading an analog clock face or describing exact positions of chess pieces.
- **Counting**: Claude can give approximate counts of objects in an image but may not always be precisely accurate, especially with large numbers of small objects.
- **AI generated images**: Claude does not know if an image is AI-generated and may be incorrect if asked. Do not rely on it to detect fake or synthetic images.
- **Inappropriate content**: Claude will not process inappropriate or explicit images that violate the [Acceptable Use Policy](https://www.anthropic.com/legal/aup).
- **Healthcare applications**: While Claude can analyze general medical images, it is not designed to interpret complex diagnostic scans such as CTs or MRIs. Claude's outputs should not be considered a substitute for professional medical advice or diagnosis.

Always carefully review and verify Claude's image interpretations, especially for high-stakes use cases. Do not use Claude for tasks requiring perfect precision or sensitive image analysis without human oversight.

------------------------------------------------------------------------

## 

FAQ

### What image file types does Claude support?

### Can Claude read image URLs?

### Is there a limit to the image file size I can upload?

### How many images can I include in one request?

### Does Claude read image metadata?

### Can I delete images I've uploaded?

### Where can I find details on data privacy for image uploads?

### What if Claude's image interpretation seems wrong?

### Can Claude generate or edit images?

------------------------------------------------------------------------

## 

Dive deeper into vision

Ready to start building with images using Claude? Here are a few helpful resources:

- [Multimodal cookbook](https://platform.claude.com/cookbook/multimodal-getting-started-with-vision): This cookbook has tips on [getting started with images](https://platform.claude.com/cookbook/multimodal-getting-started-with-vision) and [best practice techniques](https://platform.claude.com/cookbook/multimodal-best-practices-for-vision) to ensure the highest quality performance with images. See how you can effectively prompt Claude with images to carry out tasks such as [interpreting and analyzing charts](https://platform.claude.com/cookbook/multimodal-reading-charts-graphs-powerpoints) or [extracting content from forms](https://platform.claude.com/cookbook/multimodal-how-to-transcribe-text).
- [API reference](/docs/en/api/messages): Documentation for the Messages API, including example [API calls involving images](/docs/en/build-with-claude/working-with-messages#vision).

If you have any other questions, reach out to the [support team](https://support.claude.com/). You can also join the [developer community](https://www.anthropic.com/discord) to connect with other creators and get help from Anthropic experts.

Was this page helpful?

- 

- [How to use vision](#how-to-use-vision)

- [Before you upload](#before-you-upload)

- [Basics and Limits](#basics-and-limits)

- [Evaluate image size](#evaluate-image-size)

- [Calculate image costs](#calculate-image-costs)

- [Ensuring image quality](#ensuring-image-quality)

- [Prompt examples](#prompt-examples)

- [About the prompt examples](#about-the-prompt-examples)

- [Base64-encoded image example](#base64-encoded-image-example)

- [URL-based image example](#url-based-image-example)

- [Files API image example](#files-api-image-example)

- [Limitations](#limitations)

- [FAQ](#faq)

- [Dive deeper into vision](#dive-deeper-into-vision)

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
