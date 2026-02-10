::: {.cell .markdown}
# ReAct Agent

In this notebook we will look into creating ReAct Agent over tools.

1.  ReAct Agent over simple calculator tools.
2.  ReAct Agent over QueryEngine (RAG) tools.
:::

::: {.cell .markdown id="yKr4p_aGNk-J"}
### Installation
:::

::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" id="r4mZ85izboxE" outputId="afa53065-7d83-4fa1-c7ca-a1081f592cb1"}
``` python
!pip install llama-index
!pip install llama-index-llms-anthropic
!pip install llama-index-embeddings-huggingface
```
:::

::: {.cell .markdown id="qxcpBKw4JO3N"}
### Setup API Keys
:::

::: {.cell .code execution_count="1" id="IDt-c0OEb6Sp"}
``` python
# llama-parse is async-first, running the async code in a notebook requires the use of nest_asyncio
import nest_asyncio

nest_asyncio.apply()

import os

# Using Anthropic LLM API for LLM
os.environ["ANTHROPIC_API_KEY"] = "YOUR Claude API KEY"

from IPython.display import HTML, display
```
:::

::: {.cell .markdown}
### Set LLM and Embedding model

We will use anthropic latest released `Claude-3 Opus` LLM.
:::

::: {.cell .code execution_count="2" id="NJjiCFO6cQCL"}
``` python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.anthropic import Anthropic
```
:::

::: {.cell .code execution_count="3" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":209,\"referenced_widgets\":[\"e7b5fc5b69994d4a8acf8f52a4caf788\",\"01e71cf062b3452988c8b81eb828435b\",\"c64113ed8dee43f6afa4d25062d42ad0\",\"d537be6e432c4048a133b01c09d317b1\",\"6b256fc1a2954b22b13f0b8253889f14\",\"92edac9d318940aaa9bfa4c54576b408\",\"ad4d5bfb924647ec898bd474d6532336\",\"e3195b603ce843e7ad0ffbbe4ef8cd11\",\"39d7a8908efa425ca461fcab029f7dfb\",\"d3a34fd8d33444cd8c113dfeaa9bbac6\",\"84ac06046b7a412a9877cd79d415a315\",\"9df11e8cb4994c2ea82ba5511b9a2ac6\",\"79064b863ae044a8b3d58396a3bcf429\",\"b92c0bf461f842c7a861404a2c706fa8\",\"4d182081816740739ffb6932b33d1742\",\"4ef9ee3421ef45e2a4cf5364ea70d12f\",\"de49c41eb0fc4dc19c11a655496ae6a9\",\"f24288283a6649ecbabfb9a701a60a27\",\"881ec7ba4e2a4180a9c7f1740032ab3c\",\"1f431dee65814c8daf9f974da96c6097\",\"e5fd2d52e53f4202ad0bd79c793c2e88\",\"89e77c403a164d5695db24a6275606ab\",\"5f18e7ddd05d4d588ae07a531b367be4\",\"6f579e2e1c9e45279823de8a68fa949e\",\"6a26587b197b41138cc1b81421cb14d7\",\"0e8025c92a2d4b8289c365a4c9596e00\",\"74fc5150e6e24f2d8995eef908c7b517\",\"e783b097c27f4e14bc5e85c283d88c21\",\"50fbe9aead53471cb70afeb5f8cef138\",\"79d8af55f0a74d65894571326817c821\",\"a8a00c7748f94d68a5076a7d019e60a2\",\"3da779d3881f4735a453ab4dff6ce096\",\"cf7c6cae761d467aa95386eb9f816210\",\"230d9778bcd6479cac7d41e3bad65237\",\"099ea879cc664871b221e18dda1e9a98\",\"90b873759af34552b948201a270fecdb\",\"5d3be9a81edd4644b8ec27c139762ff0\",\"b5175fd3b8154dd5a722a273fe174e75\",\"d270b8986112409a9294d14541b24704\",\"0649e4ee97204e6d8c0a765158a9fcb9\",\"72339db534e9469c916a6048dca64a21\",\"a488fe4a222b4264b298948c3a329fbc\",\"0b2d7d34c4de4e1c83050996044c1be8\",\"3412f431b58a4a10a57226d933a0352e\",\"26c63ede6fd840c39aa4a33550029a1d\",\"80cc96f4736c41b7bd5a9092ad5b75f6\",\"c415b5b483e64873b861878259ed5f98\",\"debe9699d03f4a05ab95aa7d81ad5d6a\",\"cd762731b75a42d0a011da43709a7485\",\"c5c79e2f31a24af0b451856433011cdc\",\"ee03b3ffc04e498986b6cb03dae7bb09\",\"7e814c66b5b3435da5ce8826f6780327\",\"1fcba194be3a41339603f99ea136cea1\",\"f3b995f94c8f4b37a721da11bea0094e\",\"a3b979b146a84f178660346e3c1a4378\",\"beaf2e2394a9456294c27803d1f5f7f6\",\"72ab5f7d76de4ab3814421ce2f8a7850\",\"c6ba56ca0959496ca1637b20b2596243\",\"a60c9284f47148abb3d203286872f4cb\",\"5414aeb5db3a4bb0abfafb5b2c78d133\",\"d41bd474ea084c23b8a17ac3390f214b\",\"918b38282d6b4e069fb2479610019fad\",\"baf2841cf3c34254ac93d9f0fe9a51b5\",\"48b206237d9c4e49bea35fe8ea45d45b\",\"b3463be18cce475eac2af3da5d1e9354\",\"a07c90f8b4fb4a92a4f86f723a49a719\"]}" id="ejHZjyyicRac" outputId="467b97a6-3598-4c96-99d6-78608a1611d1"}
``` python
llm = Anthropic(temperature=0.0, model="claude-opus-4-1")
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
```
:::

::: {.cell .code execution_count="4" id="dEG3EgJhcTMS"}
``` python
from llama_index.core import Settings

Settings.llm = llm
Settings.embed_model = embed_model
Settings.chunk_size = 512
```
:::

::: {.cell .markdown}
## ReAct Agent over Tools
:::

::: {.cell .markdown}
### Define Tools
:::

::: {.cell .code execution_count="5" id="my8Iu2cR1dT7"}
``` python
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
```
:::

::: {.cell .code execution_count="6" id="2Vk9QK8J1eZY"}
``` python
def multiply(a: int, b: int) -> int:
    """Multiply two integers and returns the result integer"""
    return a * b


def add(a: int, b: int) -> int:
    """Add two integers and returns the result integer"""
    return a + b


add_tool = FunctionTool.from_defaults(fn=add)
multiply_tool = FunctionTool.from_defaults(fn=multiply)
```
:::

::: {.cell .markdown}
### Create ReAct Agent

Create agent over tools and test out queries
:::

::: {.cell .code execution_count="7"}
``` python
agent = ReActAgent.from_tools([multiply_tool, add_tool], llm=llm, verbose=True)
```
:::

:::: {.cell .code execution_count="8" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="qWJHLfo11gej" outputId="61f2e3ac-85c1-458b-d72c-031858e3b5c5"}
``` python
response = agent.chat("What is 20+(2*4)? Calculate step by step ")
```

::: {.output .stream .stdout}
    Thought: I need to use the multiply tool to calculate 2*4 first, then use the add tool to add that result to 20.
    Action: multiply
    Action Input: {'a': 2, 'b': 4}
    Observation: 8
    Thought: Now that I have the result of 2*4, which is 8, I can add that to 20 to get the final answer.
    Action: add
    Action Input: {'a': 20, 'b': 8}
    Observation: 28
    Thought: I can answer without using any more tools.
    Answer: 20+(2*4) equals 28. 

    To calculate it step-by-step:
    1. First, calculate 2*4 which equals 8. 
    2. Then, add 20 to that result of 8.
    3. 20 + 8 = 28

    Therefore, 20+(2*4) = 28.
:::
::::

:::: {.cell .code execution_count="9" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="y9DRugAW1iG2" outputId="554e25bc-6574-4b4a-e288-fa725406185b"}
``` python
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))
```

::: {.output .stream .stdout}
    20+(2*4) equals 28. 

    To calculate it step-by-step:
    1. First, calculate 2*4 which equals 8. 
    2. Then, add 20 to that result of 8.
    3. 20 + 8 = 28

    Therefore, 20+(2*4) = 28.
:::
::::

::: {.cell .markdown}
### Visit Prompts

You can check prompts that the agent used to select the tools.
:::

:::: {.cell .code execution_count="10"}
``` python
prompt_dict = agent.get_prompts()
for k, v in prompt_dict.items():
    print(f"Prompt: {k}\n\nValue: {v.template}")
```

::: {.output .stream .stdout}
    Prompt: agent_worker:system_prompt

    Value: 
    You are designed to help with a variety of tasks, from answering questions     to providing summaries to other types of analyses.

    ## Tools
    You have access to a wide variety of tools. You are responsible for using
    the tools in any sequence you deem appropriate to complete the task at hand.
    This may require breaking the task into subtasks and using different tools
    to complete each subtask.

    You have access to the following tools:
    {tool_desc}

    ## Output Format
    To answer the question, please use the following format.

    ```
    Thought: I need to use a tool to help me answer the question.
    Action: tool name (one of {tool_names}) if using a tool.
    Action Input: the input to the tool, in a JSON format representing the kwargs (e.g. {{"input": "hello world", "num_beams": 5}})
    ```

    Please ALWAYS start with a Thought.

    Please use a valid JSON format for the Action Input. Do NOT do this {{'input': 'hello world', 'num_beams': 5}}.

    If this format is used, the user will respond in the following format:

    ```
    Observation: tool response
    ```

    You should keep repeating the above format until you have enough information
    to answer the question without using any more tools. At that point, you MUST respond
    in the one of the following two formats:

    ```
    Thought: I can answer without using any more tools.
    Answer: [your answer here]
    ```

    ```
    Thought: I cannot answer the question with the provided tools.
    Answer: Sorry, I cannot answer your query.
    ```

    ## Current Conversation
    Below is the current conversation consisting of interleaving human and assistant messages.
:::
::::

::: {.cell .markdown}
## ReAct Agent over `QueryEngine` Tools
:::

::: {.cell .code execution_count="11" id="8yG1aKy9198J"}
``` python
from llama_index.core.tools import QueryEngineTool, ToolMetadata
```
:::

::: {.cell .markdown}
### Download data

We will define ReAct agent over tools created on QueryEngines with Uber
and Lyft 10K SEC Filings.
:::

:::: {.cell .code execution_count="12"}
``` python
!mkdir -p 'data/10k/'
!wget 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/10k/uber_2021.pdf' -O 'data/10k/uber_2021.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/10k/lyft_2021.pdf' -O 'data/10k/lyft_2021.pdf'
```

::: {.output .stream .stdout}
    --2024-03-08 06:58:18--  https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/10k/uber_2021.pdf
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.109.133, 185.199.111.133, ...
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 1880483 (1.8M) [application/octet-stream]
    Saving to: ‘data/10k/uber_2021.pdf’

    data/10k/uber_2021. 100%[===================>]   1.79M  --.-KB/s    in 0.02s   

    2024-03-08 06:58:18 (90.6 MB/s) - ‘data/10k/uber_2021.pdf’ saved [1880483/1880483]

    --2024-03-08 06:58:19--  https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/10k/lyft_2021.pdf
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.109.133, 185.199.108.133, ...
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 1440303 (1.4M) [application/octet-stream]
    Saving to: ‘data/10k/lyft_2021.pdf’

    data/10k/lyft_2021. 100%[===================>]   1.37M  --.-KB/s    in 0.02s   

    2024-03-08 06:58:19 (60.1 MB/s) - ‘data/10k/lyft_2021.pdf’ saved [1440303/1440303]
:::
::::

::: {.cell .markdown}
### Load Data
:::

::: {.cell .code execution_count="13"}
``` python
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

lyft_docs = SimpleDirectoryReader(input_files=["./data/10k/lyft_2021.pdf"]).load_data()
uber_docs = SimpleDirectoryReader(input_files=["./data/10k/uber_2021.pdf"]).load_data()
```
:::

::: {.cell .markdown}
### Build Index
:::

::: {.cell .code execution_count="14"}
``` python
lyft_index = VectorStoreIndex.from_documents(lyft_docs)
uber_index = VectorStoreIndex.from_documents(uber_docs)
```
:::

::: {.cell .markdown}
### Create QueryEngines
:::

::: {.cell .code execution_count="15"}
``` python
lyft_engine = lyft_index.as_query_engine(similarity_top_k=3)
uber_engine = uber_index.as_query_engine(similarity_top_k=3)
```
:::

::: {.cell .markdown}
#### Create QueryEngine Tools
:::

::: {.cell .code execution_count="16"}
``` python
query_engine_tools = [
    QueryEngineTool(
        query_engine=lyft_engine,
        metadata=ToolMetadata(
            name="lyft_10k",
            description=(
                "Provides information about Lyft financials for year 2021. "
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
    QueryEngineTool(
        query_engine=uber_engine,
        metadata=ToolMetadata(
            name="uber_10k",
            description=(
                "Provides information about Uber financials for year 2021. "
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
]
```
:::

::: {.cell .markdown}
### ReAct Agent {#react-agent}
:::

::: {.cell .code execution_count="17"}
``` python
agent = ReActAgent.from_tools(
    query_engine_tools,
    llm=llm,
    verbose=True,
)
```
:::

::: {.cell .markdown}
### Querying with ReAct Agent
:::

:::: {.cell .code execution_count="18"}
``` python
response = agent.chat("What was Lyft's revenue growth in 2021?")
```

::: {.output .stream .stdout}
    Thought: I need to use a tool to help me answer the question.
    Action: lyft_10k
    Action Input: {'input': "What was Lyft's revenue growth in 2021?"}
    Observation: According to the context provided, Lyft's revenue increased by $843.6 million, or 36%, in 2021 compared to 2020. This growth was primarily driven by a significant increase in the number of Active Riders in 2021 as vaccines became more widely distributed and more communities reopened. The revenue growth in 2021 was partially offset by increased driver incentives recorded as a reduction to revenue.
    Thought: The provided observation directly answers the question about Lyft's revenue growth in 2021. I have enough information to provide a final answer without using additional tools.
    Answer: Lyft's revenue grew by $843.6 million, or 36%, in 2021 compared to 2020. The growth was mainly driven by a significant increase in Active Riders as COVID-19 vaccines became more widely available and communities reopened. However, the revenue growth was partially offset by higher driver incentives which were recorded as a reduction to revenue.
:::
::::

:::: {.cell .code execution_count="19"}
``` python
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))
```

::: {.output .stream .stdout}
    Lyft's revenue grew by $843.6 million, or 36%, in 2021 compared to 2020. The growth was mainly driven by a significant increase in Active Riders as COVID-19 vaccines became more widely available and communities reopened. However, the revenue growth was partially offset by higher driver incentives which were recorded as a reduction to revenue.
:::
::::

:::: {.cell .code execution_count="20"}
``` python
response = agent.chat(
    "Compare and contrast the revenue growth of Uber and Lyft in 2021, then give an analysis"
)
```

::: {.output .stream .stdout}
    Thought: I need to use the lyft_10k and uber_10k tools to find information about Lyft and Uber's revenue growth in 2021 to compare and contrast them.

    Action: lyft_10k
    Action Input: {"input": "What was Lyft's revenue growth in dollars and percentage in 2021 compared to 2020?"}

    Observation: Lyft's revenue grew by $843.6 million, or 36%, from $2.4 billion in 2020 to $3.2 billion in 2021.

    Thought: Now I need to find Uber's revenue growth in 2021 to compare to Lyft's.

    Action: uber_10k
    Action Input: {"input": "What was Uber's revenue growth in dollars and percentage in 2021 compared to 2020?"}

    Observation: Uber's revenue grew by $8.5 billion, or 57%, from $14.1 billion in 2020 to $22.6 billion in 2021.

    Thought: I can now compare the revenue growth figures and provide an analysis.
    Answer: In comparing Lyft and Uber's revenue growth in 2021:

    Lyft's revenue grew by $843.6 million, or 36%, from $2.4 billion in 2020 to $3.2 billion in 2021. 

    Uber's revenue grew by a much larger $8.5 billion, or 57%, from $14.1 billion in 2020 to $22.6 billion in 2021.

    So while both companies saw strong revenue growth as they recovered from the impacts of the pandemic in 2020, Uber's growth was significantly higher than Lyft's in both dollar and percentage terms. 

    A few key factors likely contributed to Uber's higher growth rate:

    1) Uber has a more diversified business with significant food delivery and freight segments in addition to ridesharing. These segments grew rapidly in 2021.

    2) Uber operates in many more international markets than Lyft. As global travel recovered in 2021, this provided a boost to Uber.

    3) Uber's overall scale is much larger than Lyft's, so similar percentage growth translates
:::
::::

:::: {.cell .code execution_count="21"}
``` python
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))
```

::: {.output .stream .stdout}
    In comparing Lyft and Uber's revenue growth in 2021:

    Lyft's revenue grew by $843.6 million, or 36%, from $2.4 billion in 2020 to $3.2 billion in 2021. 

    Uber's revenue grew by a much larger $8.5 billion, or 57%, from $14.1 billion in 2020 to $22.6 billion in 2021.

    So while both companies saw strong revenue growth as they recovered from the impacts of the pandemic in 2020, Uber's growth was significantly higher than Lyft's in both dollar and percentage terms. 

    A few key factors likely contributed to Uber's higher growth rate:

    1) Uber has a more diversified business with significant food delivery and freight segments in addition to ridesharing. These segments grew rapidly in 2021.

    2) Uber operates in many more international markets than Lyft. As global travel recovered in 2021, this provided a boost to Uber.

    3) Uber's overall scale is much larger than Lyft's, so similar percentage growth translates
:::
::::
