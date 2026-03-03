---
category: "10-Prompting-Guides"
fetched_at: "2026-03-03T14:56:35Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/alliteration-alchemist"
title: "Alliteration alchemist - Claude API Docs"
---

# Alliteration alchemist


Generate alliterative phrases and sentences for any given subject.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

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
    messages=[{"role": "user", "content": [{"type": "text", "text": "Ocean"}]}],
)
print(message.content)
```
