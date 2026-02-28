---
category: "10-Prompting-Guides"
fetched_at: "2026-02-22T13:23:51Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/vr-fitness-innovator"
title: "VR fitness innovator - Claude API Docs"
---
# VR fitness innovator


Brainstorm creative ideas for virtual reality fitness games.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

| Role | Content |
|----|----|
| User | Your task is to generate a list of innovative and engaging ideas for virtual reality (VR) fitness games. Consider various game genres, unique gameplay mechanics, immersive environments, and creative ways to incorporate physical exercises and movements. The ideas should be appealing to a wide range of fitness enthusiasts and gamers, encouraging them to stay active and have fun while exercising in VR. For each idea, provide a brief description of the game concept, key features, and how it promotes fitness. |

## 

Example Output

1.  Idea: VR Parkour Adventure Description: Players navigate through a dynamic urban environment, running, jumping, climbing, and performing parkour stunts to overcome obstacles and reach objectives. The game adapts to the player's movements, providing an intense full-body workout while exploring the virtual city. Key features: Realistic parkour mechanics, procedurally generated environments, multiplayer races, and challenges. Fitness aspects: Cardio, agility, coordination, and lower body strength.
2.  Idea: Rhythm Boxing Description: A high-energy boxing game set to the beat of popular music tracks. Players must punch, dodge, and block in sync with the rhythm to score points and progress through increasingly challenging levels. The game offers a variety of boxing styles and training modes. Key features: Licensed music, customizable boxers, online multiplayer, and a diverse range of boxing techniques. Fitness aspects: Cardio, upper body strength, reflexes, and endurance.
3.  Idea: VR Fitness RPG Description: An immersive role-playing game where players create their own character and embark on a quest to save a fantasy world. The game combines traditional RPG elements with fitness challenges, requiring players to perform physical exercises to cast spells, defeat enemies, and level up their character. Key features: Character customization, skill trees, epic boss battles, and a mix of strength, cardio, and flexibility exercises. Fitness aspects: Full-body workouts, strength training, cardio, and flexibility.

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
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Your task is to generate a list of innovative and engaging ideas for virtual reality (VR) fitness games. Consider various game genres, unique gameplay mechanics, immersive environments, and creative ways to incorporate physical exercises and movements. The ideas should be appealing to a wide range of fitness enthusiasts and gamers, encouraging them to stay active and have fun while exercising in VR. For each idea, provide a brief description of the game concept, key features, and how it promotes fitness.",
                }
            ],
        }
    ],
)
print(message.content)
```
