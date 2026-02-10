::: {.cell .markdown id="OzsRXoCSLC14"}
# RouterQuery Engine

In this notebook we will look into `RouterQueryEngine` to route the user
queries to one of the available query engine tools. These tools can be
different indices/ query engine on same documents/ different documents.
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
### Download Document
:::

:::: {.cell .code execution_count="6" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="MozCygK32Zy0" outputId="0f8d3446-3445-419c-a976-4405c0d93759"}
``` python
!mkdir -p 'data/paul_graham/'
!wget 'https://raw.githubusercontent.com/jerryjliu/llama_index/main/docs/examples/data/paul_graham/paul_graham_essay.txt' -O 'data/paul_graham/paul_graham_essay.txt'
```

::: {.output .stream .stdout}
    --2024-03-08 07:04:27--  https://raw.githubusercontent.com/jerryjliu/llama_index/main/docs/examples/data/paul_graham/paul_graham_essay.txt
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.109.133, 185.199.110.133, 185.199.108.133, ...
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.109.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 75042 (73K) [text/plain]
    Saving to: ‘data/paul_graham/paul_graham_essay.txt’

    data/paul_graham/pa 100%[===================>]  73.28K  --.-KB/s    in 0.002s  

    2024-03-08 07:04:27 (28.6 MB/s) - ‘data/paul_graham/paul_graham_essay.txt’ saved [75042/75042]
:::
::::

::: {.cell .markdown id="G4nEvK7CKTbh"}
### Load Document
:::

::: {.cell .code execution_count="7" id="n4AGgEvf0dpo"}
``` python
# load documents
from llama_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader("data/paul_graham").load_data()
```
:::

::: {.cell .markdown id="rAlVBGBOKYmX"}
### Create Indices and Query Engines. {#create-indices-and-query-engines}
:::

::: {.cell .code execution_count="8" id="yabW13VV2Vus"}
``` python
from llama_index.core import SummaryIndex, VectorStoreIndex

# Summary Index for summarization questions
summary_index = SummaryIndex.from_documents(documents)

# Vector Index for answering specific context questions
vector_index = VectorStoreIndex.from_documents(documents)
```
:::

::: {.cell .code execution_count="9" id="GQCnJnOl2i1M"}
``` python
# Summary Index Query Engine
summary_query_engine = summary_index.as_query_engine(
    response_mode="tree_summarize",
    use_async=True,
)

# Vector Index Query Engine
vector_query_engine = vector_index.as_query_engine()
```
:::

::: {.cell .markdown id="9gxEcFxLKeSN"}
### Create tools for summary and vector query engines. {#create-tools-for-summary-and-vector-query-engines}
:::

::: {.cell .code execution_count="10" id="qM0eVXy62ohZ"}
``` python
from llama_index.core.tools.query_engine import QueryEngineTool

# Summary Index tool
summary_tool = QueryEngineTool.from_defaults(
    query_engine=summary_query_engine,
    description="Useful for summarization questions related to Paul Graham eassy on What I Worked On.",
)

# Vector Index tool
vector_tool = QueryEngineTool.from_defaults(
    query_engine=vector_query_engine,
    description="Useful for retrieving specific context from Paul Graham essay on What I Worked On.",
)
```
:::

::: {.cell .markdown id="psgZak7mKkn3"}
### Create Router Query Engine
:::

::: {.cell .code execution_count="11" id="atzdlxci2rPk"}
``` python
from llama_index.core.query_engine.router_query_engine import RouterQueryEngine
from llama_index.core.selectors.llm_selectors import LLMSingleSelector
```
:::

::: {.cell .code execution_count="12" id="AX7laiwj2ut8"}
``` python
# Create Router Query Engine
query_engine = RouterQueryEngine(
    selector=LLMSingleSelector.from_defaults(),
    query_engine_tools=[
        summary_tool,
        vector_tool,
    ],
)
```
:::

::: {.cell .markdown id="r_nIEGuNKor4"}
### Test Queries
:::

:::: {.cell .code execution_count="13" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="RCeKGLxG2wZ-" outputId="86b24d46-31c2-4370-9323-95b2573c966a"}
``` python
response = query_engine.query("What is the summary of the document?")
```

::: {.output .stream .stdout}
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    Selecting query engine 0: The question is asking for a summary of the document. Choice 1 specifically mentions that it is useful for summarization questions related to Paul Graham's essay on What I Worked On, making it the most relevant choice for answering the given question..
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
:::
::::

:::: {.cell .code execution_count="14" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":128}" id="9e74o31q3kok" outputId="49db0722-b863-495f-b6b3-8067e09555d1"}
``` python
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))
```

::: {.output .display_data}
<p style="font-size:20px">The document is an autobiographical essay by Paul Graham, describing the major projects and events in his life from childhood through his 50s. Key points include:

- As a child, he was interested in programming and writing. He attended college intending to study philosophy but switched to AI.

- After grad school, he decided to pursue art and attended RISD and the Accademia in Florence. He supported himself doing freelance Lisp programming. 

- In 1995, he and Robert Morris started Viaweb, one of the first web application companies, which was acquired by Yahoo in 1998. This made Graham wealthy.

- After leaving Yahoo, he returned to painting for a time, then started publishing essays online and working on a new Lisp dialect called Arc. 

- In 2005, he co-founded Y Combinator, a new kind of startup investment firm, with Jessica Livingston, Robert Morris and Trevor Blackwell. He was very engaged in YC for many years as it pioneered a new model of startup funding.

- In 2013 he handed over the reins of YC to Sam Altman. After a period focused on painting, in 2015 he began developing a new Lisp dialect called Bel, which he worked on intensively for 4 years.

- The essay reflects on the winding path his career took, the accidental discoveries like the YC model, and the way his interests in art, writing and programming languages have intertwined over the decades. It emphasizes the value he found in pursuing ideas despite their unprestigious status.</p>
:::
::::

:::: {.cell .code execution_count="17" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="QnuVMeJt2yE2" outputId="64b49891-4c61-43c3-c622-2fa94c3f5c62"}
``` python
response = query_engine.query("What did Paul Graham do growing up?")
```

::: {.output .stream .stdout}
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    Selecting query engine 1: The question asks about specific details from Paul Graham's life, which would likely be found in the original essay. A summary of the essay may not include all the relevant details about what he did growing up..
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
:::
::::

:::: {.cell .code execution_count="18" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":128}" id="otNC-PzI20dM" outputId="d1d389e7-57d8-4eda-bca4-14b78d549b40"}
``` python
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))
```

::: {.output .display_data}
<p style="font-size:20px">According to the context provided, the two main things Paul Graham worked on outside of school before college were writing and programming. He wrote short stories, which he admits were awful, with hardly any plot and just characters with strong feelings. 

In 9th grade, when he was 13 or 14, he started trying to write programs on an IBM 1401 computer that his school district used. The language was an early version of Fortran, and programs had to be typed on punch cards. However, he was puzzled by the 1401 and couldn't figure out what to really do with it, since the only input was data on punched cards which he didn't have. His clearest memory is learning that programs could fail to terminate when one of his didn't, which was a social faux pas on a shared machine. But everything changed for him once microcomputers became available.</p>
:::
::::
