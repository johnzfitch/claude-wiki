::: {.cell .markdown id="OzsRXoCSLC14"}
# Multi-Document Agents

In this notebook we will look into Building RAG when you have a large
number of documents using `DocumentAgents` concept with `ReAct Agent`.
:::

::: {.cell .markdown id="SxWKA6fCK0mw"}
### Installation
:::

::: {.cell .code id="csEUaulS0EQ_"}
``` python
!pip install llama-index
!pip install llama-index-llms-anthropic
!pip install llama-index-embeddings-huggingface
```
:::

::: {.cell .markdown id="Z2_M_q-pK2-1"}
### Set Logging
:::

::: {.cell .code execution_count="1" id="1Ry4vjMv0V7E"}
``` python
# NOTE: This is ONLY necessary in jupyter notebook.
# Details: Jupyter runs an event-loop behind the scenes.
#          This results in nested event-loops when we start an event-loop to make async queries.
#          This is normally not allowed, we use nest_asyncio to allow it for convenience.
import nest_asyncio

nest_asyncio.apply()

import logging
import sys

# Set up the root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Set logger level to INFO

# Clear out any existing handlers
logger.handlers = []

# Set up the StreamHandler to output to sys.stdout (Colab's output)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)  # Set handler level to INFO

# Add the handler to the logger
logger.addHandler(handler)

from IPython.display import HTML, display
```
:::

::: {.cell .markdown id="No_1L4P4K5J2"}
### Set Claude API Key
:::

::: {.cell .code execution_count="2" id="6JXQosS80PNK"}
``` python
import os

os.environ["ANTHROPIC_API_KEY"] = "YOUR Claude API KEY"
```
:::

::: {.cell .markdown id="4pEemHzPK7as"}
### Set LLM and Embedding model

We will use anthropic latest released `Claude-3 Opus` LLM.
:::

::: {.cell .code execution_count="3" id="Euj43bfS0Rqf"}
``` python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.anthropic import Anthropic
```
:::

::: {.cell .code execution_count="4" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":313,\"referenced_widgets\":[\"d2bcac509f704091a2e1d78cbab529ac\",\"8333f65239244e3ebccd03d3cc11e7cf\",\"f7452e83c16a4842891b74e0fe77964e\",\"fd642eff11e34ec487173f0b284b8eb1\",\"621440477e6649ae81f6576c3d8426b8\",\"a23860a3889b43f28b87ed5734842ed2\",\"c4c0e261c70d408497199f17710f46fa\",\"da103bb8638c4d2288eb5c96bf8e6ab2\",\"73c8ad8a3d5d4c7987104cecaca85a60\",\"e147f00bdf994cbaa96f515d2f5fbe7a\",\"3c7b010e02c945cfbba526b0beea2053\",\"5787464222eb4412b3f6d88cf1e9651a\",\"08d838a6337344cf984b48fe0b959a80\",\"6dfc9fc2dfbe4c65b3a29e3c46fc6908\",\"0b5555011ac1408bbaf8a39a63ac8ba4\",\"8701fa65b6b24302b485e217a637b7e1\",\"87a2ec99584f49faa1409d1cced0bbf4\",\"ca26dbc458c5410d82e09be213c04df8\",\"b6f3972d040447ad9044566b1bfb9bd4\",\"4dcb8d94d6cc42e9ad4245b3ced5d73a\",\"01a915c53cf34814ba59f798c46bff0a\",\"9c37e197eb0f4a79acbf86dfcfda9ee3\",\"a6dc6b641a1d4589baaf94c073b166c6\",\"66c92c089d6742d19a3ddd6ab093acce\",\"5efcb4f54e96445aab0bf6cd5c48e140\",\"64656ae50fcd435cabe838ba3fc74bf4\",\"a33c0c07eeb9433197cfc0012faaf86b\",\"d6388c264ec14c8591f2e0e8a4f508b5\",\"1f13df73c8734c6ea01dc84264d7a9a4\",\"a454a7ad6d214b46b2e22029e32713b3\",\"ab1afeb075db48dc852b38f7efb0b59a\",\"ed41ea29459b4a7297f99f56e5f5fac2\",\"5c12435c34304f78886c0dc85e812633\",\"9499cc5b0de94627addecd8765561db0\",\"8b78eb20237341758740e516ace41299\",\"d19283e264d44366acdaca17ebab70ad\",\"8b4541bc84794e399e16b0ac1f2ce5db\",\"d8ad3826d40b41c4934d896245794382\",\"b6773dc9fc6b40e2a89747ad88ac5f9d\",\"f2fcf88b1d1d4c8db80585600f373092\",\"8920704065a84c739381b3f6b8a71d33\",\"de37a9145f1f40928adf13224646523d\",\"c2baea7ddf4d4b2ebc038a7c412f99dd\",\"15a486a5a98f4011bda3a821389ccdc0\",\"ca36015e10544f55a1acbdbaf03017f0\",\"6eacd26fd23f4530baf98b65a9d8c166\",\"a9bdcf8f6140463787f41d9fb8370806\",\"10fa33db762e48048107084ce0df9688\",\"a7827923f5a14835abf070fe1a417ce6\",\"23772f2ec9e64c8ea329874661c0e72c\",\"d472cafc3561461399958630cb81c348\",\"ce089a58329e474babea74a657b6a8a8\",\"84b7eb51e38d42c3a09a2ab1f87a419b\",\"258166a5ad444e11ae291d47c29d8e95\",\"8dde20c91feb49488b45aac477379320\",\"883a09808ba74aceb03ec26cb525cb32\",\"9b9272daa2cc484b99ef22536f1e5ae9\",\"442953634e084c868c4c9be0e8530001\",\"dcd3611436f44099af77b29a9556363b\",\"b58a3ecb60904570a073ae3520867feb\",\"9d8c6c0800cf484f9a79172407fe7168\",\"5724373f8d6a4076a292be596efbdca8\",\"c7e9aab70d1541e49a55c1433898a725\",\"4a53092d22514d63bcd8e4a7906f6c6b\",\"b9dc22c807fc42d5bb5e084f191e408a\",\"7d46c9e5023543e2b82da0cf7f6bb0c4\"]}" id="wqwlOVH00TbB" outputId="1803fa26-e51e-4b9b-8f0d-5ac0d322f2e9"}
``` python
llm = Anthropic(temperature=0.0, model="claude-opus-4-1")
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
```
:::

::: {.cell .code execution_count="5" id="aIkLOdRz0Unp"}
``` python
from llama_index.core import Settings

Settings.llm = llm
Settings.embed_model = embed_model
Settings.chunk_size = 512
```
:::

::: {.cell .markdown id="JP-m752eKRWW"}
### Download Documents

We will use Wikipedia pages of `Toronto`, `Seattle`, `Chicago`,
`Boston`, `Houston` cities and build RAG pipeline.
:::

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" id="MozCygK32Zy0" outputId="0f8d3446-3445-419c-a976-4405c0d93759"}
``` python
wiki_titles = ["Toronto", "Seattle", "Chicago", "Boston", "Houston"]

from pathlib import Path

import requests

for title in wiki_titles:
    response = requests.get(
        "https://en.wikipedia.org/w/api.php",
        params={
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "extracts",
            # 'exintro': True,
            "explaintext": True,
        },
        timeout=30,
    ).json()
    page = next(iter(response["query"]["pages"].values()))
    wiki_text = page["extract"]

    data_path = Path("data")
    if not data_path.exists():
        Path.mkdir(data_path)

    with open(data_path / f"{title}.txt", "w") as fp:
        fp.write(wiki_text)
```
:::

::: {.cell .markdown id="G4nEvK7CKTbh"}
### Load Document
:::

::: {.cell .code execution_count="7" id="n4AGgEvf0dpo"}
``` python
# Load all wiki documents

from llama_index.core import SimpleDirectoryReader

city_docs = {}
for wiki_title in wiki_titles:
    city_docs[wiki_title] = SimpleDirectoryReader(
        input_files=[f"data/{wiki_title}.txt"]
    ).load_data()
```
:::

::: {.cell .markdown}
#### Build ReAct Agent for each city
:::

::: {.cell .code execution_count="8"}
``` python
from llama_index.core import SummaryIndex, VectorStoreIndex
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata

# Build agents dictionary
agents = {}

for wiki_title in wiki_titles:
    # build vector index
    vector_index = VectorStoreIndex.from_documents(
        city_docs[wiki_title],
    )
    # build summary index
    summary_index = SummaryIndex.from_documents(
        city_docs[wiki_title],
    )
    # define query engines
    vector_query_engine = vector_index.as_query_engine()
    summary_query_engine = summary_index.as_query_engine()

    # define tools
    query_engine_tools = [
        QueryEngineTool(
            query_engine=vector_query_engine,
            metadata=ToolMetadata(
                name="vector_tool",
                description=(f"Useful for retrieving specific context from {wiki_title}"),
            ),
        ),
        QueryEngineTool(
            query_engine=summary_query_engine,
            metadata=ToolMetadata(
                name="summary_tool",
                description=(f"Useful for summarization questions related to {wiki_title}"),
            ),
        ),
    ]

    # build agent
    agent = ReActAgent.from_tools(
        query_engine_tools,
        llm=llm,
        verbose=True,
    )

    agents[wiki_title] = agent
```
:::

::: {.cell .markdown}
#### Define IndexNode for each of these Agents
:::

::: {.cell .code execution_count="9"}
``` python
from llama_index.core.schema import IndexNode

# define top-level nodes
objects = []
for wiki_title in wiki_titles:
    # define index node that links to these agents
    wiki_summary = (
        f"This content contains Wikipedia articles about {wiki_title}. Use"
        " this index if you need to lookup specific facts about"
        f" {wiki_title}.\nDo not use this index if you want to analyze"
        " multiple cities."
    )
    node = IndexNode(text=wiki_summary, index_id=wiki_title, obj=agents[wiki_title])
    objects.append(node)
```
:::

::: {.cell .markdown}
#### Define Top-Level Retriever to choose an Agent
:::

::: {.cell .code execution_count="10" id="QdyS_E_w3t56"}
``` python
vector_index = VectorStoreIndex(
    objects=objects,
)
query_engine = vector_index.as_query_engine(similarity_top_k=1, verbose=True)
```
:::

::: {.cell .markdown}
#### Test Queries

Should choose a vector tool/ summary tool for a specific agent based on
the query.
:::

:::: {.cell .code execution_count="11"}
``` python
# should use Toronto agent -> vector tool
response = query_engine.query("What is the population of Toronto?")
```

::: {.output .stream .stdout}
    Retrieval entering Toronto: ReActAgent
    Retrieving from object ReActAgent with query What is the population of Toronto?
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    Thought: I need to use a tool to help me answer the question.
    Action: vector_tool
    Action Input: {'input': 'What is the population of Toronto?'}
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    Observation: According to the context information, the population of Toronto in 2021 was 2,794,356, making it the fourth-most populous city in North America.
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    Thought: I can answer without using any more tools.
    Answer: According to the information provided, the population of Toronto in 2021 was 2,794,356, making it the fourth-most populous city in North America.
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
:::
::::

:::: {.cell .code execution_count="12"}
``` python
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))
```

::: {.output .display_data}
<p style="font-size:20px">The population of Toronto is 2,794,356 as of 2021. It is the fourth-most populous city in North America.</p>
:::
::::

:::: {.cell .code execution_count="13"}
``` python
# should use Houston agent -> vector tool
response = query_engine.query("Who and when was Houston founded?")
```

::: {.output .stream .stdout}
    Retrieval entering Houston: ReActAgent
    Retrieving from object ReActAgent with query Who and when was Houston founded?
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    Thought: I need to use a tool to help me answer the question about who founded Houston and when it was founded.
    Action: vector_tool
    Action Input: {'input': 'Who founded Houston and when was it founded?'}
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    Observation: Houston was founded by land investors on August 30, 1836, at the confluence of Buffalo Bayou and White Oak Bayou, a point now known as Allen's Landing. The city was incorporated on June 5, 1837 and named after former General Sam Houston, who was president of the Republic of Texas at the time.
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    Thought: The vector_tool provided the key information needed to answer the question of who founded Houston and when it was founded. I can now provide a complete answer without using any more tools.
    Answer: Houston was founded by land investors on August 30, 1836. The city was incorporated on June 5, 1837 and named after Sam Houston, who was the president of the Republic of Texas at the time. The location where Houston was founded is at the confluence of Buffalo Bayou and White Oak Bayou, which is now known as Allen's Landing.
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
:::
::::

:::: {.cell .code execution_count="14"}
``` python
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))
```

::: {.output .display_data}
<p style="font-size:20px">Houston was founded by land investors on August 30, 1836. The city was named after Sam Houston, who was serving as the president of the Republic of Texas at that time.</p>
:::
::::

:::: {.cell .code execution_count="15"}
``` python
# should use Boston agent -> summary tool
response = query_engine.query("Summarize about the sports teams in Boston")
```

::: {.output .stream .stdout}
    Retrieval entering Boston: ReActAgent
    Retrieving from object ReActAgent with query Summarize about the sports teams in Boston
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    Thought: I need to use a tool to help me answer the question.
    Action: summary_tool
    Action Input: {'input': 'Summarize the sports teams in Boston'}
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    Observation: Boston has teams in the four major North American men's professional sports leagues plus Major League Soccer, and has won 39 championships in these leagues:

    - The Boston Red Sox (MLB) play at Fenway Park. They are one of the most storied franchises in baseball.

    - The Boston Celtics (NBA) play at TD Garden. Along with the Los Angeles Lakers, they have won the most NBA championships with 17. 

    - The Boston Bruins (NHL) also play at TD Garden. They were the first American NHL team and are an Original Six franchise.

    - The New England Patriots (NFL) play in nearby Foxborough. They have won 6 Super Bowls in the 2000s and 2010s.

    - The New England Revolution (MLS) also play in Foxborough.

    Boston also has several other professional sports teams like the Boston Breakers (women's soccer) and Boston Cannons (lacrosse). The area's many colleges field competitive NCAA Division I teams, especially in ice hockey. The annual Boston Marathon is one of the world's most famous running events.
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    Thought: The summary tool provided a good overview of the major sports teams in Boston. I think I can provide a concise summary answer to the original question based on this information.
    Answer: Boston is home to successful professional sports teams in baseball (Red Sox), basketball (Celtics), hockey (Bruins), football (Patriots), and soccer (Revolution). The Red Sox, Celtics, and Bruins are some of the most historic franchises in their respective leagues. In total, Boston teams have won 39 championships in the four major North American sports leagues and MLS. The area also hosts the famous Boston Marathon each year and has many competitive college sports programs, especially in ice hockey.
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
:::
::::

:::: {.cell .code execution_count="16"}
``` python
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))
```

::: {.output .display_data}
<p style="font-size:20px">Boston is a city with a rich sports tradition, boasting several highly successful professional teams across multiple leagues. In baseball, the Boston Red Sox are one of the most storied franchises in the sport's history. The Boston Celtics have a similarly impressive legacy in basketball, with numerous championships to their name. Hockey fans in the city passionately support the Boston Bruins, another team with a long and successful history. The New England Patriots, who play in the nearby town of Foxborough, have been a dominant force in the NFL for many years. Even in the relatively newer MLS, the New England Revolution have made their mark on the Boston sports scene. These teams have combined to win an impressive 39 championships across the five leagues. Beyond professional sports, Boston is also known for hosting the prestigious Boston Marathon annually and having strong college sports programs, particularly in ice hockey.</p>
:::
::::

:::: {.cell .code execution_count="17"}
``` python
# should use Seattle agent -> summary tool
response = query_engine.query("Give me a summary on all the positive aspects of Chicago")
```

::: {.output .stream .stdout}
    Retrieval entering Chicago: ReActAgent
    Retrieving from object ReActAgent with query Give me a summary on all the positive aspects of Chicago
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    Thought: I need to use a tool to help me summarize the positive aspects of Chicago.
    Action: summary_tool
    Action Input: {'input': 'Provide a summary of the positive aspects and attributes of the city of Chicago'}
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    Observation: Based on the provided information, some of the positive aspects and attributes of Chicago include:

    - Chicago is the third most populous city in the U.S. and a major transportation hub. It is an important component in global distribution.

    - The city has a diverse economy, with major industries including finance, commerce, industry, technology, telecommunications, and transportation. Chicago has the second largest central business district in the U.S. 

    - Chicago is an international hub for finance, culture, commerce, and industry. It has the largest derivatives market in the world and is a major financial center.

    - The city is a popular tourist destination known for its architecture, skyscrapers, parks, museums, and unique cuisine. Major attractions include Millennium Park, Navy Pier, the Magnificent Mile, and numerous cultural institutions.

    - Chicago has a rich history in the visual and performing arts, literature, film, theater, and music. It has influential art museums, a strong tradition of jazz and blues music, and acclaimed theater, dance, and comedy scenes.

    - The city has an extensive public transportation system including rail lines and buses. It also has a large network of parks and open spaces.

    - Chicago is home to several top universities, numerous major company headquarters, and a variety of unique neighborhoods and communities reflecting its diverse population and history.

    In summary, Chicago stands out for its economic strength, cultural vibrancy, tourist appeal, transportation infrastructure, higher education, and cosmopolitan character. The context portrays Chicago in an overall positive light as a thriving, world-class American city.
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    Thought: The summary tool provided a good overview of the positive aspects of Chicago. I think I can provide a satisfactory answer to the original question based on the information given.
    Answer: Chicago has many positive attributes that make it a vibrant and appealing city:

    Economy and Business: Chicago has a diverse and thriving economy, serving as a major hub for industries like finance, commerce, telecommunications, and transportation. It is home to the second largest central business district in the U.S. and the world's largest derivatives market.

    Tourism and Culture: Chicago is a popular tourist destination known for its iconic architecture, world-class museums, unique cuisine, and beautiful parks like Millennium Park. The city has a rich artistic heritage in visual arts, music (especially jazz and blues), theater, dance and comedy.

    Transportation: Chicago is a critical transportation center for the U.S. with an extensive public transit network of trains and buses. Its airports and rail lines make it an important link in the nation's distribution network.

    Education: Numerous prestigious universities call Chicago home, adding to its intellectual capital. 

    Diversity: Chicago's many neighborhoods reflect the diverse backgrounds and cultures of its residents, resulting in a cosmopolitan, international character.

    Overall, Chicago stands out as a world-class city known for its robust economy, vibrant cultural scene, strong transportation infrastructure, acclaimed educational institutions, and global status. The city has many strengths and positive qualities that make it an attractive place to live, work, and visit.
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
:::
::::

:::: {.cell .code execution_count="18"}
``` python
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))
```

::: {.output .display_data}
<p style="font-size:20px">Chicago is a dynamic and appealing city with many positive attributes:

It has a thriving, diverse economy serving as a major hub for finance, commerce, telecommunications and transportation. Chicago is a popular tourist destination, known for its iconic architecture, world-class museums, unique cuisine, and beautiful parks. 

The city is a critical transportation center with an extensive public transit network, airports and rail lines. Numerous prestigious universities call Chicago home. Its neighborhoods reflect the diverse backgrounds and cultures of residents, giving the city a cosmopolitan character.

In summary, Chicago stands out for its robust economy, vibrant culture, strong transportation infrastructure, acclaimed educational institutions, diversity, and global status - making it an attractive place to live, work and visit.</p>
:::
::::
