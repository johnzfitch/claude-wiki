::: {#20de56a8 .cell .markdown}
# Prompting Claude for \"JSON Mode\"
:::

::: {#8e7fe136 .cell .markdown}
Claude doesn\'t have a formal \"JSON Mode\" with constrained sampling.
But not to worry \-- you can still get reliable JSON from Claude! This
recipe will show you how.
:::

::: {#e5e1a230 .cell .markdown}
First, let\'s look at Claude\'s default behavior.
:::

::: {#0c07a2c1 .cell .code}
``` python
%pip install anthropic
```
:::

::: {#fc39114b .cell .code execution_count="1"}
``` python
import json
import re
from pprint import pprint

from anthropic import Anthropic
```
:::

::: {#1b991340 .cell .code execution_count="3"}
``` python
client = Anthropic()
MODEL_NAME = "claude-opus-4-1"
```
:::

:::: {#c28ca1ad .cell .code execution_count="4"}
``` python
message = (
    client.messages.create(
        model=MODEL_NAME,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Give me a JSON dict with names of famous athletes & their sports.",
            },
        ],
    )
    .content[0]
    .text
)
print(message)
```

::: {.output .stream .stdout}
    Here is a JSON dictionary with names of famous athletes and their respective sports:

    {
      "athletes": [
        {
          "name": "Usain Bolt",
          "sport": "Track and Field"
        },
        {
          "name": "Michael Phelps",
          "sport": "Swimming"
        },
        {
          "name": "Serena Williams",
          "sport": "Tennis"
        },
        {
          "name": "LeBron James",
          "sport": "Basketball"
        },
        {
          "name": "Lionel Messi",
          "sport": "Soccer"
        },
        {
          "name": "Simone Biles",
          "sport": "Gymnastics"
        },
        {
          "name": "Tom Brady",
          "sport": "American Football"
        },
        {
          "name": "Muhammad Ali",
          "sport": "Boxing"
        },
        {
          "name": "Nadia Comaneci",
          "sport": "Gymnastics"
        },
        {
          "name": "Michael Jordan",
          "sport": "Basketball"
        },
        {
          "name": "Pelé",
          "sport": "Soccer"
        },
        {
          "name": "Roger Federer",
          "sport": "Tennis"
        }
      ]
    }
:::
::::

::: {#0a63ad7e .cell .markdown}
Claude followed instructions and outputted a nice dictionary, which we
can extract with code:
:::

:::: {#08626553 .cell .code execution_count="8"}
``` python
def extract_json(response):
    json_start = response.index("{")
    json_end = response.rfind("}")
    return json.loads(response[json_start : json_end + 1])


extract_json(message)
```

::: {.output .execute_result execution_count="8"}
    {'athletes': [{'name': 'Usain Bolt', 'sport': 'Track and Field'},
      {'name': 'Michael Phelps', 'sport': 'Swimming'},
      {'name': 'Serena Williams', 'sport': 'Tennis'},
      {'name': 'LeBron James', 'sport': 'Basketball'},
      {'name': 'Lionel Messi', 'sport': 'Soccer'},
      {'name': 'Simone Biles', 'sport': 'Gymnastics'},
      {'name': 'Tom Brady', 'sport': 'American Football'},
      {'name': 'Muhammad Ali', 'sport': 'Boxing'},
      {'name': 'Nadia Comaneci', 'sport': 'Gymnastics'},
      {'name': 'Michael Jordan', 'sport': 'Basketball'},
      {'name': 'Pelé', 'sport': 'Soccer'},
      {'name': 'Roger Federer', 'sport': 'Tennis'}]}
:::
::::

::: {#39275885 .cell .markdown}
But what if we want Claude to skip the preamble and go straight to the
JSON? One simple way is to prefill Claude\'s response and include a
\"{\" character.
:::

:::: {#155e088a .cell .code execution_count="9"}
``` python
message = (
    client.messages.create(
        model=MODEL_NAME,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Give me a JSON dict with names of famous athletes & their sports.",
            },
            {"role": "assistant", "content": "Here is the JSON requested:\n{"},
        ],
    )
    .content[0]
    .text
)
print(message)
```

::: {.output .stream .stdout}

       "athletes":[
          {
             "name":"Michael Jordan",
             "sport":"Basketball"
          },
          {
             "name":"Babe Ruth",
             "sport":"Baseball"
          },
          {
             "name":"Muhammad Ali",
             "sport":"Boxing"
          },
          {
             "name":"Serena Williams",
             "sport":"Tennis"
          },
          {
             "name":"Wayne Gretzky",
             "sport":"Hockey"
          },
          {
             "name":"Michael Phelps",
             "sport":"Swimming"
          },
          {
             "name":"Usain Bolt",
             "sport":"Track and Field"
          },
          {
             "name":"Mia Hamm",
             "sport":"Soccer"
          },
          {
             "name":"Michael Schumacher",
             "sport":"Formula 1 Racing"
          },
          {
             "name":"Simone Biles",
             "sport":"Gymnastics"
          }
       ]
    }
:::
::::

::: {#64e94c65 .cell .markdown}
Now all we have to do is add back the \"{\" that we prefilled and we can
extract the JSON.
:::

:::: {#6c066ac6 .cell .code execution_count="11"}
``` python
output_json = json.loads("{" + message[: message.rfind("}") + 1])
output_json
```

::: {.output .execute_result execution_count="11"}
    {'athletes': [{'name': 'Michael Jordan', 'sport': 'Basketball'},
      {'name': 'Babe Ruth', 'sport': 'Baseball'},
      {'name': 'Muhammad Ali', 'sport': 'Boxing'},
      {'name': 'Serena Williams', 'sport': 'Tennis'},
      {'name': 'Wayne Gretzky', 'sport': 'Hockey'},
      {'name': 'Michael Phelps', 'sport': 'Swimming'},
      {'name': 'Usain Bolt', 'sport': 'Track and Field'},
      {'name': 'Mia Hamm', 'sport': 'Soccer'},
      {'name': 'Michael Schumacher', 'sport': 'Formula 1 Racing'},
      {'name': 'Simone Biles', 'sport': 'Gymnastics'}]}
:::
::::

::: {#cd4492fd .cell .markdown}
For very long and complicated prompts, which contain multiple JSON
outputs so that a string search for \"{\" and \"}\" don\'t do the trick,
you can also have Claude output each JSON item in specified tags for
future extraction.
:::

:::: {#443ad932 .cell .code execution_count="13"}
``` python
message = (
    client.messages.create(
        model=MODEL_NAME,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": """Give me a JSON dict with the names of 5 famous athletes & their sports.
Put this dictionary in <athlete_sports> tags.

Then, for each athlete, output an additional JSON dictionary. In each of these additional dictionaries:
- Include two keys: the athlete's first name and last name.
- For the values, list three words that start with the same letter as that name.
Put each of these additional dictionaries in separate <athlete_name> tags.""",
            },
            {"role": "assistant", "content": "Here is the JSON requested:"},
        ],
    )
    .content[0]
    .text
)
print(message)
```

::: {.output .stream .stdout}
     

    <athlete_sports>
    {
      "Michael Jordan": "Basketball",
      "Serena Williams": "Tennis",
      "Lionel Messi": "Soccer", 
      "Usain Bolt": "Track and Field",
      "Michael Phelps": "Swimming"
    }
    </athlete_sports>

    <athlete_name>
    {
      "first": ["Magnificent", "Motivating", "Memorable"],
      "last": ["Joyful", "Jumping", "Jocular"]
    }
    </athlete_name>

    <athlete_name>
    {
      "first": ["Skillful", "Strong", "Superstar"],
      "last": ["Winning", "Willful", "Wise"]
    }
    </athlete_name>

    <athlete_name>
    {
      "first": ["Legendary", "Lively", "Leaping"],
      "last": ["Magical", "Marvelous", "Masterful"]  
    }
    </athlete_name>

    <athlete_name>
    {
      "first": ["Unbeatable", "Unbelievable", "Unstoppable"],
      "last": ["Brave", "Bold", "Brilliant"]
    }
    </athlete_name>

    <athlete_name>
    {
      "first": ["Marvelous", "Methodical", "Medalist"],
      "last": ["Powerful", "Persevering", "Precise"]
    }
    </athlete_name>
:::
::::

::: {#74043369 .cell .markdown}
Now, we can use an extraction regex to get all the dictionaries.
:::

::: {#bd847a70 .cell .code execution_count="14"}
``` python
import re


def extract_between_tags(tag: str, string: str, strip: bool = False) -> list[str]:
    ext_list = re.findall(f"<{tag}>(.+?)</{tag}>", string, re.DOTALL)
    if strip:
        ext_list = [e.strip() for e in ext_list]
    return ext_list


athlete_sports_dict = json.loads(extract_between_tags("athlete_sports", message)[0])
athlete_name_dicts = [json.loads(d) for d in extract_between_tags("athlete_name", message)]
```
:::

:::: {#eb61ee06 .cell .code execution_count="15"}
``` python
pprint(athlete_sports_dict)
```

::: {.output .stream .stdout}
    {'Lionel Messi': 'Soccer',
     'Michael Jordan': 'Basketball',
     'Michael Phelps': 'Swimming',
     'Serena Williams': 'Tennis',
     'Usain Bolt': 'Track and Field'}
:::
::::

:::: {#57dade0f .cell .code execution_count="16"}
``` python
pprint(athlete_name_dicts, width=1)
```

::: {.output .stream .stdout}
    [{'first': ['Magnificent',
                'Motivating',
                'Memorable'],
      'last': ['Joyful',
               'Jumping',
               'Jocular']},
     {'first': ['Skillful',
                'Strong',
                'Superstar'],
      'last': ['Winning',
               'Willful',
               'Wise']},
     {'first': ['Legendary',
                'Lively',
                'Leaping'],
      'last': ['Magical',
               'Marvelous',
               'Masterful']},
     {'first': ['Unbeatable',
                'Unbelievable',
                'Unstoppable'],
      'last': ['Brave',
               'Bold',
               'Brilliant']},
     {'first': ['Marvelous',
                'Methodical',
                'Medalist'],
      'last': ['Powerful',
               'Persevering',
               'Precise']}]
:::
::::

::: {#5e5854c0 .cell .markdown}
So to recap:

- You can use string parsing to extract the text between
  \"`json" and "`\" to get the JSON.
- You can remove preambles *before* the JSON via a partial Assistant
  message. (However, this removes the possibility of having Claude do
  \"Chain of Thought\" for increased intelligence before beginning to
  output the JSON.)
- You can get rid of text that comes *after* the JSON by using a stop
  sequence.
- You can instruct Claude to output JSON in XML tags to make it easy to
  collect afterward for more complex prompts.
:::
