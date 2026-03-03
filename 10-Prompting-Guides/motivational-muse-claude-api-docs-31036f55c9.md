---
category: "10-Prompting-Guides"
fetched_at: "2026-03-03T14:56:33Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/motivational-muse"
title: "Motivational muse - Claude API Docs"
---

# Motivational muse


Provide personalized motivational messages and affirmations based on user input.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

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
                    "text": "I've been struggling to find motivation to work on my novel. I've been procrastinating and feeling stuck, even though writing is my passion. I'm afraid I might never finish it.",
                }
            ],
        }
    ],
)
print(message.content)
```
