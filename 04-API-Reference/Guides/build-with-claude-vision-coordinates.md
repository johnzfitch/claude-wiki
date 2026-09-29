---
title: "Coordinates and bounding boxes - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/vision-coordinates"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:38Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fvision-coordinates)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](../Other/get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](../Other/manage-claude-authentication.md)

Building with Claude

[Features overview](build-with-claude-overview.md)[Using the Messages API](build-with-claude-working-with-messages.md)[Stop reasons and fallback](build-with-claude-handling-stop-reasons.md)[Refusals and fallback](build-with-claude-refusals-and-fallback.md)[Fallback credit](build-with-claude-fallback-credit.md)

Model capabilities

[Effort](build-with-claude-effort.md)[Task budgets (beta)](build-with-claude-task-budgets.md)[Fast mode (research preview)](build-with-claude-fast-mode.md)[Structured outputs](build-with-claude-structured-outputs.md)[Citations](build-with-claude-citations.md)[Streaming Messages](build-with-claude-streaming.md)[Batch processing](build-with-claude-batch-processing.md)[Search results](build-with-claude-search-results.md)[Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](build-with-claude-multilingual-support.md)[Embeddings](build-with-claude-embeddings.md)

[Thinking](build-with-claude-thinking.md)

Tools

[Overview](../Agents-Tools/agents-and-tools-tool-use-overview.md)[How tool use works](../Agents-Tools/agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](../Agents-Tools/agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](../Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](../Agents-Tools/agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](../Agents-Tools/agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](../Agents-Tools/agents-and-tools-tool-use-tool-runner.md)[Strict tool use](../Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md)[Server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md)[Web search tool](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](../Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](../Agents-Tools/agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md)[Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md)[Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](../Agents-Tools/agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](../Agents-Tools/agents-and-tools-tool-use-tool-reference.md)[Manage tool context](../Agents-Tools/agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](../Agents-Tools/agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](../Agents-Tools/agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](../Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](../Agents-Tools/agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](build-with-claude-context-windows.md)[Context editing](build-with-claude-context-editing.md)[Prompt caching](build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](build-with-claude-cache-diagnostics.md)[Token counting](build-with-claude-token-counting.md)

[Compaction](build-with-claude-compaction.md)

Working with files

[Files API](build-with-claude-files.md)[PDF support](build-with-claude-pdf-support.md)

[Images and vision](build-with-claude-vision.md)

[Overview](build-with-claude-vision.md)[Coordinates and bounding boxes](build-with-claude-vision-coordinates.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Quickstart](../Agents-Tools/agents-and-tools-agent-skills-quickstart.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)[Skills in the API](build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)[MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md)[Google Cloud](build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](build-with-claude-claude-in-microsoft-foundry.md)

[Console](../Other/usage-limits.md)

[Messages](../../01-Getting-Started/intro.md)Images and vision

# Coordinates and bounding boxes

Copy page



How Claude resizes images, and how to work with the pixel coordinates it returns for bounding boxes, points, and UI elements.

Copy page



Claude can locate and label regions of an image (for example, returning bounding boxes for tables, form fields, chart elements, or UI components). This guide covers how Claude resizes images before processing them and how to work with the pixel coordinates it returns, so that boxes and points line up with your original image.

You'll need this for OCR pipelines, form extraction, chart parsing, UI element location, and any task where you act on a specific region of an image. For sending images, supported formats, and per-model resolution limits, see [Vision](build-with-claude-vision.md).



**Claude works best with absolute pixel coordinates.** Ask for them explicitly in your prompt. For example: *"Return the bounding box of each table as `[x1, y1, x2, y2]` (top-left and bottom-right corners) in pixel coordinates."* Claude does not work well when you ask for normalized coordinates, for example: *"Return bounding box coordinates between `0` and `1000`."* Always ask for pixel coordinates and normalize in your own code if you need to. To get coordinates as machine-readable JSON instead of prose, define a schema with [structured outputs](build-with-claude-structured-outputs.md), for example an object with an `[x1, y1, x2, y2]` array per detected element.

Coordinates follow the standard image convention: the origin `(0, 0)` is the top-left corner of the image, with x increasing to the right and y increasing downward. The coordinates Claude returns are pixel positions in the image Claude sees: your image after Claude resizes it to fit the model's native resolution (see [How Claude resizes and pads images](#how-claude-resizes-and-pads-images)). To get coordinates you can use directly, either pre-resize your image so the coordinates map one-to-one onto the image you have (see [Resize your image before uploading](#resize-your-image-before-uploading)), or rescale the coordinates Claude returns (see [Rescale coordinates when you cannot pre-resize](#rescale-coordinates-when-you-cannot-pre-resize)).



Claude's spatial reasoning has limits (see [Limitations](build-with-claude-vision.md#limitations)). Coordinate accuracy is best when you state the expected coordinate format in your prompt and spot-check results visually before processing at scale. Small elements lose precision when an image is downscaled: for fine targets, crop the region of interest and send the crop (offset returned coordinates by the crop origin), or use a high-resolution-tier model. For [PDF support](build-with-claude-pdf-support.md), pages are rasterized to images server-side at dimensions you don't control, so the returned coordinates can't be reliably mapped back onto the page. To work with coordinates on PDF content, rasterize the pages to images yourself and use the pre-resize approach.

## How Claude resizes and pads images

Claude finds the largest aspect-preserving size that satisfies both of the model's image limits:

1.  **Edge limit:** neither side exceeds the maximum edge length (1568 px on the standard tier, 2576 px on the high-resolution tier).
2.  **Visual token limit:** the image's token cost `⌈width / 28⌉ × ⌈height / 28⌉` does not exceed the model's visual token budget (1568 tokens on the standard tier, 4784 on the high-resolution tier).

See [Resolution and token cost](build-with-claude-vision.md#evaluate-image-size) for which models are in which tier.

For nearly all photos and screenshots, the visual token limit is what determines the final size. The edge limit takes over only for elongated images such as panoramas or tall phone screenshots. Compute the size with the [reference implementation](#resize-your-image-before-uploading) rather than scaling to the edge length by hand: a 1920×1080 screenshot resizes to 1456×819, not 1568×882, and assuming the edge limit puts every coordinate noticeably off target.

The token limit can also trigger a resize when neither side exceeds the edge limit. Overlooking this is the most common cause of misaligned coordinates. For example, an A4 page scanned at 130 DPI is 1075×1520 pixels: both sides are under 1568 px, but it costs `39 × 55 = 2145` visual tokens, so Claude resizes it to 924×1307.



This example assumes a model on the standard resolution tier. A high-resolution-tier model doesn't resize the same scan: 2145 tokens is within its 4784-token budget, so the coordinates it returns map directly onto the 1075×1520 original. Model tiers are listed in [Resolution and token cost](build-with-claude-vision.md#evaluate-image-size).

Claude then pads every image, resized or not, up to the next multiple of 28 pixels on the bottom and right edges (924×1307 becomes 924×1316 in the example). The padding contains no content: Claude perceives the padded image, but the page content only ever occupies the un-padded resized region. **Always normalize or rescale by the resized dimensions, not the padded dimensions**; dividing by the padded dimensions scales every coordinate by a small amount.

## Resize your image before uploading

The most reliable approach is to resize your image yourself before uploading, so the image you have is exactly the image Claude sees and the coordinates Claude returns need no conversion.

First check which resolution tier your model is on (see [Resolution and token cost](build-with-claude-vision.md#evaluate-image-size)) and pass the matching edge and token limits. The following reference implementation computes the exact size Claude resizes an image to:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
import math


def count_image_tokens(width: int, height: int) -> int:
    """Visual tokens consumed by an image: one token per 28x28 pixel patch."""
    return math.ceil(width / 28) * math.ceil(height / 28)


def resized_size(
    width: int,
    height: int,
    max_edge: int = 1568,
    max_tokens: int = 1568,
) -> tuple[int, int]:
    """The size Claude resizes an image to before padding.

    Defaults are for the standard resolution tier. For high-resolution-tier
    models, use max_edge=2576 and max_tokens=4784. Returns (width, height).
    Images that already fit within the limits are returned unchanged.
    """

    def fits(w: int, h: int) -> bool:
        return (
            math.ceil(w / 28) * 28 <= max_edge
            and math.ceil(h / 28) * 28 <= max_edge
            and count_image_tokens(w, h) <= max_tokens
        )

    if fits(width, height):
        return (width, height)
    if height > width:
        resized_h, resized_w = resized_size(height, width, max_edge, max_tokens)
        return (resized_w, resized_h)

    # Binary search along the long edge for the largest aspect-preserving
    # size that fits.
    aspect_ratio = width / height
    lo, hi = 1, width  # lo always fits; hi never fits
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if fits(mid, max(round(mid / aspect_ratio), 1)):
            lo = mid
        else:
            hi = mid
    return (lo, max(round(lo / aspect_ratio), 1))


# The A4 example from "How Claude resizes and pads images":
print(resized_size(1075, 1520))  # (924, 1307)

# To apply the resize, use your image library, for example Pillow:
# image.resize(resized_size(*image.size))
```

1.  Resize the image to the dimensions returned by the resize helper. If the image already fits within the model's limits, the helper returns its dimensions unchanged and no resize is needed.
2.  [Send the resized image](build-with-claude-vision.md#send-images-to-claude) to the API. Don't pad it yourself. Claude handles padding, and padding doesn't shift the coordinate origin.
3.  In your prompt, ask explicitly for pixel coordinates. For example: *"Return the click point for the Submit button as `[x, y]` in pixel coordinates."*
4.  Use the returned coordinates directly against the image you sent. If you need normalized coordinates, divide by the dimensions of the image you sent, not by the original image's dimensions and not by the padded dimensions.



The [Token counting](build-with-claude-token-counting.md) endpoint estimates an image's token cost from its dimensions without fully processing it, so a successful count doesn't mean the image is within the Messages API's [request limits](build-with-claude-vision.md#request-limits). An image can count successfully and still be rejected when you send it.

## Turn resizing into an error with `transformations`

Pre-resizing only protects your coordinates while your pipeline keeps producing the right sizes. A new image source or a switch to a model on a different resolution tier can quietly reintroduce server-side resizing. To turn that silent drift into a visible error, set the optional `transformations` field on an image content block in a [Messages](../Endpoints/messages.md) request:

```python
{
  "type": "image",
  "source": { "type": "base64", "media_type": "image/png", "data": "..." },
  "transformations": { "oversized_image": "error" }
}
```



A request whose marked image (any block that sets `"oversized_image": "error"`) would be resized is rejected with a 400 `invalid_request_error` naming the image's dimensions and the largest dimensions that fit. Whether an image triggers the rejection depends on the [limits of every model the request names](#how-claude-resizes-and-pads-images): the 1920×1080 example below is rejected by a standard-tier model but fits within the high-resolution tier:

``` block
messages.0.content.0: image dimensions 1920x1080 exceed the maximum image size of a model named on this request and would be downsized to 1456x819; scale the image to at most 1456x819 or set the image's oversized_image setting to "downsize"
```



Rescale to the reported target and resend: the target is the largest size, at your image's aspect ratio, that every model named on the request accepts. How marked images interact with the [server-side fallback beta](build-with-claude-refusals-and-fallback.md#server-side-fallback) is described with that feature; in every mode, a marked image is never served resized.

The setting is per image. `"oversized_image": "downsize"` (the default when the field is omitted) keeps automatic resizing as described on this page. Each image block is checked only against its own setting, so one request can mix images whose dimensions are load-bearing (a screenshot you'll click on) with images where resizing is harmless (a logo). What the setting does and does not change:

- Padding ([which never discards content](#how-claude-resizes-and-pads-images)), format conversion, and orientation correction proceed as usual.
- The hard limits (8000 px on the longest side, and the stricter per-image limit on [many-image requests](build-with-claude-vision.md#request-limits)) are separate rejections; this setting never lets an image past them.
- Images supplied by URL or file ID are checked once their bytes have been fetched; those rejections carry the same message without the leading position, so they don't identify which image failed; only embedded base64 images are named by position in the error.
- [PDF pages](build-with-claude-pdf-support.md) are rasterized server-side at dimensions you don't control; the `document` block does not accept the field (an image block nested inside a document's content accepts it like any other).
- A marked image whose dimensions cannot be determined is rejected rather than passed through: that rejection reports that the image's source dimensions could not be determined, not the resize message quoted above. No image that sets `"error"` reaches the model resized.

The [Token counting](build-with-claude-token-counting.md) endpoint honors `transformations` too, rejecting an embedded image exactly as the Messages API would, so you can check whether an embedded image fits without being resized, before running inference. Counting rejects images supplied by URL or file ID rather than fetching them, so a marked image from those sources is checked only at Messages time.

## Rescale coordinates when you cannot pre-resize

If you cannot pre-resize (for example, when the image comes from an upstream system you can't modify), use the resize helper from [Resize your image before uploading](#resize-your-image-before-uploading) to recover the dimensions Claude saw, then map the coordinates Claude returns into normalized coordinates or back onto your original image. Unless an image [opts into an error instead](#oversized-image-error), Claude resizes oversized images rather than rejecting them, up to the API's [request limits](build-with-claude-vision.md#request-limits). Beyond those limits the request fails with a validation error instead. Pass the tier limits that match the model you called: the wrong tier's limits recover the wrong resized dimensions and silently shift every coordinate. This approach requires knowing the pixel dimensions of the image you uploaded, so it does not apply to PDF uploads.

Screenshots and zoom images that you return to the [computer use](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#handle-coordinate-scaling-for-higher-resolutions) and [browser use](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md#targets-and-coordinates) toolsets are an exception to automatic resizing. The API rejects a `tool_result` image that exceeds the model's limits with a validation error instead of resizing it. Resize those images in your application before returning them, then scale the coordinates Claude returns back to your screen's dimensions.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
# This helper calls resized_size from the resize example on this page.
def to_relative_coordinates(
    x: float,
    y: float,
    original_width: int,
    original_height: int,
    max_edge: int = 1568,
    max_tokens: int = 1568,
) -> tuple[float, float]:
    """Map a pixel coordinate returned by Claude to relative coordinates in [0, 1].

    Pass the dimensions of the image you uploaded. For high-resolution-tier
    models, use max_edge=2576 and max_tokens=4784.
    """
    resized_w, resized_h = resized_size(
        original_width, original_height, max_edge, max_tokens
    )
    return (x / resized_w, y / resized_h)


# A table corner Claude returns at (462, 653.5) on the resized A4 page maps
# back onto the 1075x1520 original like this:
rel_x, rel_y = to_relative_coordinates(462, 653.5, 1075, 1520)
print((rel_x * 1075, rel_y * 1520))  # (537.5, 760.0)
```

Padding is applied only to the bottom and right edges, so the origin doesn't shift and a per-axis linear rescale is sufficient. Clamp returned coordinates to the resized dimensions before rescaling, so a point slightly outside the image can't map outside your original.

The relative coordinates multiply against whatever surface you act on: the original image, a full-resolution scan, or a screen. When you act on a screen and screenshot pixels differ from logical coordinates (HiDPI displays), also divide by the display scale factor. The [Computer use tool's scaling guidance](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md#handle-coordinate-scaling-for-higher-resolutions) covers that pattern.

## Next steps



[Agent Skills](../Agents-Tools/agents-and-tools-agent-skills-overview.md)

Agent Skills are modular capabilities that extend Claude's functionality. Each Skill packages instructions, metadata, and optional resources (scripts, templates) that Claude uses automatically when relevant.



[Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md)

Give Claude screenshot, mouse, and keyboard control of a desktop environment with the computer use tool.



[PDF support](build-with-claude-pdf-support.md)

Process PDFs with Claude. Extract text, analyze charts, and understand visual content from your documents.

[Token counting](build-with-claude-token-counting.md)

Count the tokens in a message before you send it to Claude. Use token counts to manage rate limits and costs, make model routing decisions, and fit prompts to a target length.
