---
title: "Vision - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/vision"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-13T06:36:38Z"
tags: ["api"]
---

# Vision

Copy page



Claude’s vision capabilities allow it to process and analyze images, opening up exciting possibilities for multimodal interaction.

Copy page



Vision (images)

[Models](#feature-availability)  
- All models

[APIs](#feature-availability)  
- Messages API
- Managed Agents

[Cloud platforms](#feature-availability)  
- All platforms

This guide describes how to send images to Claude, the limits and costs that apply, and where to find guidance for [coordinate-based workflows](build-with-claude-vision-coordinates.md).

------------------------------------------------------------------------

## Send images to Claude

Use Claude’s vision capabilities through:

- [claude.ai](https://claude.ai/). Upload an image like you would a file, or drag and drop an image directly into the chat window.
- [Playground](../Other/playground.md) in the Claude Console. Add images directly to any **User** message block.
- API request. See the following examples.

On the API, provide images to Claude as `image` content blocks using one of three source types:

1.  A base64-encoded image embedded in the request body
2.  A URL reference to an image hosted online
3.  A `file_id` returned by the [Files API](build-with-claude-files.md) (upload once, reference many times)



On Claude Models on Google Cloud (Google managed) and Amazon Bedrock, only base64-encoded sources are available.



Just as [placing long documents before your query](../../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md#long-context-prompting) improves results in text prompts, Claude works best when images come before text. Images placed after text or interpolated with text still perform well, but if your use case allows it, prefer an image-then-text structure.

### Base64-encoded image example

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
image1_data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGP4z8AAAAMBAQDJ/pLvAAAAAElFTkSuQmCC"
image1_media_type = "image/png"

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image1_media_type,
                        "data": image1_data,
                    },
                },
                {"type": "text", "text": "Describe this image."},
            ],
        }
    ],
)
print(message)
```

### URL-based image example

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "url",
                        "url": "https://platform.claude.com/docs/images/vision-example.jpg",
                    },
                },
                {"type": "text", "text": "Describe this image."},
            ],
        }
    ],
)
print(message)
```

### Files API image example

For images you’ll use repeatedly or when you want to avoid encoding overhead, use the [Files API](build-with-claude-files.md). Upload the image once, then reference the returned `file_id` in subsequent messages instead of resending base64 data.



In multi-turn conversations and agentic workflows, each request resends the full conversation history. If images are base64-encoded, the full image bytes are included in the payload on every turn, which can significantly increase request size and latency as the conversation grows. Uploading images to the Files API and referencing them by `file_id` keeps request payloads small regardless of how many images accumulate in the conversation history.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

# Upload the image file
with open("vision-example.jpg", "rb") as f:
    file_upload = client.files.upload(file=("vision-example.jpg", f, "image/jpeg"))

# Use the uploaded file in a message
message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {"type": "file", "file_id": file_upload.id},
                },
                {"type": "text", "text": "Describe this image."},
            ],
        }
    ],
)

print(message.content)
```

See [Messages API examples](../Endpoints/messages-create.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. for more example code and parameter details.

### Multiple images

You can include multiple images in a single request, and Claude analyzes them jointly. This is useful for comparing images, asking about differences, or working with a sequence such as pages of a document. When sending several images, introduce each one with a short text label (`Image 1:`, `Image 2:`, and so on) so you can refer to them by name in your prompt and in follow-up turns.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
image1_data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGP4z8AAAAMBAQDJ/pLvAAAAAElFTkSuQmCC"
image2_data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGNgYPgPAAEDAQAIicLsAAAAAElFTkSuQmCC"

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Image 1:"},
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": image1_data,
                    },
                },
                {"type": "text", "text": "Image 2:"},
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": image2_data,
                    },
                },
                {"type": "text", "text": "How are these images different?"},
            ],
        }
    ],
)
print(message)
```

In a multi-turn conversation, add new images in later `user` turns the same way. Claude has access to every image from earlier turns, so follow-up questions such as “Are these similar to the first two?” work without including the earlier images again in the new turn’s content.

------------------------------------------------------------------------

## Image limits and costs

### Request limits

The maximum number of images for each message or request is:

- 20 for each message on [claude.ai](https://claude.ai/)
- 100 for each request on the API, for models with a 200k-token context window
- 600 for each request on the API, for all other models

The maximum dimensions for each image are 8000x8000 px.

If a single API request contains more than 20 images, a stricter per-image dimension limit applies to every image in that request. All `image` blocks in the request count toward this threshold, including images from earlier conversation turns that you resend and images nested inside `tool_result` content (for example, screenshots returned to the computer use tool). On Claude Models on Google Cloud (Google managed) and Amazon Bedrock, document blocks such as PDFs also count toward this threshold. Images exceeding the stricter limit are rejected with an `invalid_request_error` whose message references “many-image requests” and states the current limit in pixels. To stay under the limit on all platforms, either resize each image so that neither dimension exceeds 3,000 px, or keep the request to 20 or fewer image and document blocks.

The maximum size per image is:

- 10 MB (base64-encoded) on the Claude API and Claude Models on Google Cloud (Google managed).
- 5 MB (base64-encoded) on Amazon Bedrock.
- 10 MB on [claude.ai](https://claude.ai/).



Although the API supports up to 600 images for each request, [request size limits](../Endpoints/overview.md#request-size-limits) can be reached first. The limit is 128 MB on the first-party Claude API, and other platforms have their own limits. For many images, consider [uploading with the Files API](#files-api-image-example) and referencing by `file_id` to keep request payloads small.

Even when using the Files API, requests with many large images can fail before reaching the 600-image count. Reduce image dimensions or file sizes (for example, by downsampling) before uploading (see [Resolution and token cost](#evaluate-image-size)).

### Supported formats

Claude supports JPEG, PNG, GIF, and WebP images (`image/jpeg`, `image/png`, `image/gif`, `image/webp`). Animations are unsupported, and only the first frame is used.

### Resolution and token cost

Claude processes images in patches instead of pixels. Each patch is a 28×28-pixel block of the image, referred to as a visual token. An image, therefore, costs `⌈width / 28⌉ × ⌈height / 28⌉` visual tokens.

Each model has a maximum native image resolution, expressed as a long-edge limit and a visual-token limit. Images larger than either limit are downscaled before processing; see [How Claude resizes and pads images](build-with-claude-vision-coordinates.md#how-claude-resizes-and-pads-images) for the exact rule. The exception is screenshots and zoom images that you return to the [computer use](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#handle-coordinate-scaling-for-higher-resolutions) and [browser use](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md#targets-and-coordinates) toolsets: the API rejects a `tool_result` image that exceeds the model’s limits with a validation error instead of downscaling it, so resize those images in your application before returning them. To have any other oversized image rejected with an error instead of downscaled, set the image block’s [`transformations` field](build-with-claude-vision-coordinates.md#oversized-image-error).

| Resolution tier | Models                      | Max long edge | Max visual tokens |
|-----------------|-----------------------------|---------------|-------------------|
| High-resolution | Claude 4.7 and later models | 2,576 px      | 4,784             |
| Standard        | All other models            | 1,568 px      | 1,568             |

High-resolution support is automatic on the listed models and requires no beta header or client-side opt-in.

The following table shows the downsized resolution and visual-token cost for several image sizes on each tier:

| Image size | Standard tier: downsized to | Standard tier: tokens | High-resolution tier: downsized to | High-resolution tier: tokens |
|----|----|----|----|----|
| 200x200 px (0.04 megapixels) | Not resized | 64 | Not resized | 64 |
| 1000x1000 px (1 megapixel) | Not resized | 1,296 | Not resized | 1,296 |
| 1092x1092 px (1.19 megapixels) | Not resized | 1,521 | Not resized | 1,521 |
| 1920x1080 px (2.07 megapixels) | 1456x819 px | 1,560 | Not resized | 2,691 |
| 2000x1500 px (3 megapixels) | 1269x952 px | 1,564 | Not resized | 3,888 |
| 3840x2160 px (8.29 megapixels) | 1456x819 px | 1,560 | 2576x1449 px | 4,784 |

When an image is downsized, Claude scales it to the largest size that fits the tier’s limits while preserving its aspect ratio. This caps the token cost. For the precise rule and a reference implementation, see [How Claude resizes and pads images](build-with-claude-vision-coordinates.md#how-claude-resizes-and-pads-images).

To estimate cost, multiply the token count by the [per-token price of the model](../../17-Billing-Plans/pricing.md) you’re using. For example, at Claude Haiku 4.5’s \$1 USD per million input tokens (standard tier), the 1000×1000 image costs about \$1.30 USD per thousand images. At Claude Opus 5.5’s \$4 USD per million (high-resolution tier), the same image costs about \$5.18 USD per thousand and the 4K image about \$19.14 USD per thousand.

High-resolution images can use up to roughly three times more visual tokens than the same image on a standard-tier model. If you don’t need the additional fidelity that high resolution provides for computer use, screenshot understanding, and dense documents, downsample images before sending to control token costs. To minimize latency and to simplify [coordinate-based workflows](build-with-claude-vision-coordinates.md), prefer resizing images before uploading them.

### Image quality guidance

When providing images to Claude, keep the following in mind for best results:

- **Image clarity:** Ensure images are clear and not too blurry or pixelated.
- **Text:** If the image contains important text, make sure it’s legible and not too small. Avoid cropping out key visual context solely to enlarge the text.
- **Resizing:** Take into account that your image might be resized if it is too large (see [Resolution and token cost](#evaluate-image-size)); this might, for example, make text less legible. Consider pre-resizing your images, cropping them, or both. To have an oversized image rejected with an error instead of resized (important for [coordinate workflows](build-with-claude-vision-coordinates.md)), mark the image block with [`"oversized_image": "error"`](build-with-claude-vision-coordinates.md#oversized-image-error).
- **Image compression:** Compressing images before sending them, using a lossy format such as JPEG or WebP (lossy mode), can reduce latency by reducing the size of requests. However, this can introduce artifacts that are detrimental to model performance, especially when multiple compression passes are applied. For example, heavy JPEG compression can make text difficult to read. Confirm your compression settings are appropriate for the task by inspecting the actual images sent to the API.

------------------------------------------------------------------------

## Coordinates and bounding boxes

For bounding boxes, points, and pixel coordinates, see [Coordinates and bounding boxes](build-with-claude-vision-coordinates.md). Claude returns absolute pixel coordinates relative to the image it processes after resizing; that guide covers how Claude resizes and pads images and how to pre-resize or rescale so coordinates line up with your original image.

------------------------------------------------------------------------

## Limitations

Although Claude’s image understanding capabilities are advanced, there are some limitations to be aware of:

- **People identification:** Claude cannot be used to name people in images and refuses to do so (see the [Usage Policy](https://www.anthropic.com/legal/aup)).
- **Accuracy:** Claude might hallucinate or make mistakes when interpreting low-quality, rotated, or very small images under 200 pixels.
- **Spatial reasoning:** Claude’s coordinate and localization outputs are approximate. Follow the guidance in [Coordinates and bounding boxes](build-with-claude-vision-coordinates.md) and verify outputs before relying on them.
- **Counting:** Claude can give approximate counts of objects in an image but might not always be precisely accurate, especially with large numbers of small objects.
- **AI-generated images:** Claude cannot determine whether an image is AI-generated and might be incorrect if asked. Do not rely on it to detect fake or synthetic images.
- **Inappropriate content:** Claude does not process inappropriate or explicit images that violate the [Usage Policy](https://www.anthropic.com/legal/aup).
- **Healthcare applications:** Although Claude can analyze general medical images, it is not designed to interpret complex diagnostic scans such as CTs or MRIs. Claude’s outputs should not be considered a substitute for professional medical advice or diagnosis.

Always carefully review and verify Claude’s image interpretations, especially for high-stakes use cases. Do not use Claude for tasks requiring perfect precision or sensitive image analysis without human oversight.

------------------------------------------------------------------------

## FAQ

### What image file types does Claude support?

JPEG, PNG, GIF, and WebP. See [Supported formats](#supported-formats).

### Can Claude read image URLs?

Yes. Use the `url` source type instead of `base64` in the `image` content block. See the [URL-based image example](#url-based-image-example).

### Is there a limit to the image file size I can upload?

Yes. See [Request limits](#request-limits) for per-image and overall request size limits across the Claude API, Amazon Bedrock, Claude Models on Google Cloud (Google managed), and claude.ai.

### How many images can I include in one request?

Up to 600 for each API request (100 for models with a 200k-token context window) and 20 for each turn on claude.ai. See [Request limits](#request-limits) for details and the lower per-image dimension limit that applies above 20 images.

### Does Claude read image metadata?

No, Claude does not parse or receive any metadata from images passed to it.

### Can I delete images I’ve uploaded?

No. See [API and data retention](../Other/manage-claude-api-and-data-retention.md) for how long images are kept. If you upload images with the [Files API](build-with-claude-files.md), you can delete them there.

### Where can I find details on data privacy for image uploads?

Refer to the Anthropic privacy policy page for information on how uploaded images and other data are handled. Anthropic does not use uploaded images to train models.

### What if Claude’s image interpretation seems wrong?

If Claude’s image interpretation seems incorrect:

1.  Ensure the image is clear, high-quality, and correctly oriented.
2.  Try prompt engineering techniques to improve results.
3.  If the issue persists, flag the output in claude.ai (thumbs up/down) or contact the [support team](https://support.claude.com/).

Your feedback helps improve Claude!

### Can Claude generate or edit images?

No, Claude is an image understanding model only. It can interpret and analyze images, but it cannot generate, produce, edit, manipulate, or create images.

------------------------------------------------------------------------

## Next steps



[Multimodal recipe](https://platform.claude.com/cookbook/multimodal-getting-started-with-vision)

Get tips and best-practice techniques for tasks such as interpreting charts and extracting content from forms.



[API reference](../Endpoints/messages-create.md)

See the Messages API documentation, including example API calls involving images.

## Availability

Vision (images)

Cloud platform

Cloud platform: Claude API

Claude API

APIs  
- Messages API
- Managed Agents

Models  
- All models

Amazon Bedrock

API  
- Messages API

Models  
- All models

Note  
Only base64 image sources; per-image limit 5 MB (base64-encoded) and a lower total request size.

Amazon Bedrock (bedrock-runtime)

API  
- Messages API

Models  
- All models

Note  
Only base64 image sources; per-image limit 5 MB (base64-encoded) and a lower total request size.

Claude Platform on AWS

APIs  
- Messages API
- Managed Agents

Models  
- All models

Claude Models on Google Cloud (Anthropic managed)

APIs  
- Messages API
- Managed Agents

Models  
- All models

Claude Models on Google Cloud (Google managed)

API  
- Messages API

Models  
- All models

Note  
Only base64 image sources; per-image limit 5 MB (base64-encoded) and a lower total request size.

Microsoft Foundry

API  
- Messages API

Models  
- All models
