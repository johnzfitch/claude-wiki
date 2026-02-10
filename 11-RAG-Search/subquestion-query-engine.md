::: {.cell .markdown id="XvksyJE6Onz_"}
# SubQuestionQueryEngine

Often, we encounter scenarios where our queries span across multiple
documents.

In this notebook, we delve into addressing complex queries that extend
over various documents by breaking them down into simpler sub-queries
and generate answers using the `SubQuestionQueryEngine`.
:::

::: {.cell .markdown id="jrGtIJogMsC5"}
### Installation
:::

::: {.cell .code id="s2vK4JUD4Yxg"}
``` python
!pip install llama-index
!pip install llama-index-llms-anthropic
!pip install llama-index-embeddings-huggingface
```
:::

::: {.cell .markdown id="BK17UTVoMuns"}
### Setup API Key
:::

::: {.cell .code execution_count="1" id="2XlJDsnB4v2_"}
``` python
import os

os.environ["ANTHROPIC_API_KEY"] = "YOUR Claude API KEY"
```
:::

::: {.cell .markdown id="toeP1CYRMxuf"}
### Setup LLM and Embedding model

We will use anthropic latest released `Claude-3 Opus` LLM.
:::

::: {.cell .code execution_count="2" id="E6xhHINq4ynN"}
``` python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.anthropic import Anthropic
```
:::

::: {.cell .code execution_count="3" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":313,\"referenced_widgets\":[\"80fc006d4df8498a816e17cefc18ca2d\",\"e79bcee6519a4b6ab01b1bfa337cfe10\",\"66eef0ef7951416cbd6533d4845629cf\",\"d6d9e55994814729b3b68a79ba4198ce\",\"e460d00a45084a91a3cc0567bc8354e9\",\"879fa26aa4a04edeb5b79215067ce019\",\"e41c5f311d0e47e98f20502601dc87f4\",\"896de50f7e914df087f789315410addf\",\"76c0154ec5fe4be9b1fc9cb50c4ce7cb\",\"d7fe74b431364318b71c54f50f5062d2\",\"75f6b0b8bc8241deb83422857bb014c6\",\"6dbce7cfd7a6496dac0e0d75c3d3d89a\",\"a0b718321c544580b33665fc4d898c3f\",\"0c4f37adc854457a8e1e93e81f554909\",\"1ad42c23709242ae81e30144424342a4\",\"95414fde3b474d8987030ebad3123cf1\",\"fc448faa0d1349f3b2b99faf0d23df25\",\"16a40c3609114bff9d0574beebbd7f90\",\"f1a06c3d41ff4d6fa55ab10a8b968625\",\"bcaa0ae8f12c4c11b866711d130a5082\",\"3ac67761c43d4859a55b79e719ceb9eb\",\"5069cc3d6e444710a10464eb582d8667\",\"48c1eb1fef554a46a76573dc3175ddc9\",\"95305cdc84d74184ab385d51c18bc6b9\",\"c939510250db45f7a6ac46e1f9826c43\",\"b052069c77df4a8f9e53aae07bd5d354\",\"c752757087ba47bd9d66fc6937ec7e50\",\"eacd788bd8744cdc867799446cf96ece\",\"bd14648db88b47d79ec20a2b36eddd1a\",\"403c7c4189a647d59d101af4b9505bc4\",\"a3d5f40478804b3f8d74308777cbdb54\",\"8c5a99b093d94fe68dc95e002740ae45\",\"fb74a1b313964bda95083d682f5ee7ed\",\"db4a859d68274fad90dc1e734c603905\",\"042aa71a671c478b84e1f705f596cd8f\",\"545f291465ec4429b53047c8a553a947\",\"394a95ab8c2c4141ab87c602d163dad0\",\"7ee4bd7836774c1886019c336ba4eb0c\",\"5ffcec13f4354e0d941694fd31a6bb3a\",\"ef196e67ba4844fe84c40084931c6a45\",\"4db2d7d911b24198b2f2e0e627a4442b\",\"be1607bb5bc242e9a97e8e782b112ef2\",\"dc7d72d4cc2d4e1aaf4ebd1b9bdd7c34\",\"fd323e1105d744cb836e5388df45c8b7\",\"5b3061f6a3ba4b5aac88c9f5d93b51bc\",\"c117b7eebe0b46aa8999f5f507b83953\",\"30fbb2ead374431d8d595c2af9beb904\",\"ee1b883ed1f04a3c91a78be9003c6ce1\",\"d4e896d589e24ab39a7874756bbb53b7\",\"9566a05413924cfdb9f373b7512a9669\",\"ec4c3693cd51495082d9c1486d9ffecf\",\"0bdcd931790046ff85d806438979b905\",\"e44abbb2de714804a27906796acd141d\",\"48496204daf0451da5489bda293522db\",\"5938d2f27d564559861523e8aff1562c\",\"e9a8a9befc1e47a1ae664732d8393433\",\"24289de0731346fea8e800222afa93b9\",\"824931b749144703ac79dfe489e9ea05\",\"107683e48eed4188886fc1d78d61e240\",\"a8e9a6e25e3b48029a943af73e62dd3c\",\"51320c89d8dd41dd802e76e047d980a9\",\"5121931a2b614938b9f2b1b5a511e022\",\"013ede19019f48c693882cc9caf3ff51\",\"20bb8e32267c4b628c2daa337b119105\",\"4186402c66e446dd9e12545c6a19f30a\",\"400027c1605a4676833f6ea0810699ab\"]}" id="GIsJJBFo40Jq" outputId="ed4d7267-327a-4ead-a61f-801ae9a69481"}
``` python
llm = Anthropic(temperature=0.0, model="claude-opus-4-1")
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
```
:::

::: {.cell .code execution_count="4" id="2Hqi93hb41nV"}
``` python
from llama_index.core import Settings

Settings.llm = llm
Settings.embed_model = embed_model
Settings.chunk_size = 512
```
:::

::: {.cell .markdown id="ZM0Ksh5QM1yc"}
### Setup logging
:::

::: {.cell .code execution_count="5" id="pY6CL0_e429M"}
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

::: {.cell .markdown id="MhFt3P-IM4ai"}
### Download Data

We will use Uber and Lyft 2021 10K SEC Filings
:::

:::: {.cell .code execution_count="6" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="ukHLfRJC44fG" outputId="2f5f2a1b-645d-4fa4-f6ab-b8f65373ba07"}
``` python
!wget 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/10k/uber_2021.pdf' -O './uber_2021.pdf'
!wget 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/10k/lyft_2021.pdf' -O './lyft_2021.pdf'
```

::: {.output .stream .stdout}
    --2024-03-08 07:07:32--  https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/10k/uber_2021.pdf
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.109.133, 185.199.108.133, 185.199.110.133, ...
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.109.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 1880483 (1.8M) [application/octet-stream]
    Saving to: ‘./uber_2021.pdf’

    ./uber_2021.pdf     100%[===================>]   1.79M  --.-KB/s    in 0.02s   

    2024-03-08 07:07:32 (87.4 MB/s) - ‘./uber_2021.pdf’ saved [1880483/1880483]

    --2024-03-08 07:07:33--  https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/10k/lyft_2021.pdf
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.111.133, 185.199.109.133, ...
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 1440303 (1.4M) [application/octet-stream]
    Saving to: ‘./lyft_2021.pdf’

    ./lyft_2021.pdf     100%[===================>]   1.37M  --.-KB/s    in 0.02s   

    2024-03-08 07:07:33 (74.9 MB/s) - ‘./lyft_2021.pdf’ saved [1440303/1440303]
:::
::::

::: {.cell .markdown id="ItM1L4OmM-Wb"}
### Load Data
:::

::: {.cell .code execution_count="7" id="pltY8vjU59mQ"}
``` python
from llama_index.core import SimpleDirectoryReader

lyft_docs = SimpleDirectoryReader(input_files=["lyft_2021.pdf"]).load_data()
uber_docs = SimpleDirectoryReader(input_files=["uber_2021.pdf"]).load_data()
```
:::

:::: {.cell .code execution_count="8" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="7dTY-clm5_k_" outputId="7ef4e12e-6348-476b-cab0-a3e38b2c5c98"}
``` python
print(f"Loaded lyft 10-K with {len(lyft_docs)} pages")
print(f"Loaded Uber 10-K with {len(uber_docs)} pages")
```

::: {.output .stream .stdout}
    Loaded lyft 10-K with 238 pages
    Loaded Uber 10-K with 307 pages
:::
::::

::: {.cell .markdown id="xSDF_QEsNBci"}
### Index Data
:::

::: {.cell .code execution_count="9" colab="{\"background_save\":true}" id="LRAZWegi6Dyi"}
``` python
from llama_index.core import VectorStoreIndex

lyft_index = VectorStoreIndex.from_documents(lyft_docs[:100])
uber_index = VectorStoreIndex.from_documents(uber_docs[:100])
```
:::

::: {.cell .markdown id="p6hwyc5DNGMk"}
### Create Query Engines
:::

::: {.cell .code execution_count="10" id="EHmUyRcC6F5f"}
``` python
lyft_engine = lyft_index.as_query_engine(similarity_top_k=5)
```
:::

::: {.cell .code execution_count="11" id="15hf7apf6HWF"}
``` python
uber_engine = uber_index.as_query_engine(similarity_top_k=5)
```
:::

::: {.cell .markdown id="ebyg3tfNNIzM"}
### Querying
:::

::::: {.cell .code execution_count="12" colab="{\"background_save\":true}" id="_6-FAxif6InL" outputId="4d1adf30-cc28-4f79-a906-aabf82a03e8d"}
``` python
response = await lyft_engine.aquery(
    "What is the revenue of Lyft in 2021? Answer in millions with page reference"
)
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))
```

::: {.output .stream .stdout}
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
:::

::: {.output .display_data}
<p style="font-size:20px">According to the consolidated statements of operations on page 79, Lyft's total revenue for the year ended December 31, 2021 was $3,208.3 million.</p>
:::
:::::

::::: {.cell .code execution_count="13" colab="{\"background_save\":true}" id="2VSINSWB6SjI" outputId="9b5e0403-b613-464a-835a-e15689bc86b5"}
``` python
response = await uber_engine.aquery(
    "What is the revenue of Uber in 2021? Answer in millions, with page reference"
)
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))
```

::: {.output .stream .stdout}
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
:::

::: {.output .display_data}
<p style="font-size:20px">According to the Consolidated Statements of Operations on page 77, Uber's revenue for the year ended December 31, 2021 was $17,455 million.</p>
:::
:::::

::: {.cell .markdown id="przIf6LINKuI"}
### Create Tools
:::

::: {.cell .code execution_count="14" id="kgK60jJq6VEz"}
``` python
from llama_index.core.query_engine import SubQuestionQueryEngine
from llama_index.core.tools import QueryEngineTool, ToolMetadata

query_engine_tools = [
    QueryEngineTool(
        query_engine=lyft_engine,
        metadata=ToolMetadata(
            name="lyft_10k", description="Provides information about Lyft financials for year 2021"
        ),
    ),
    QueryEngineTool(
        query_engine=uber_engine,
        metadata=ToolMetadata(
            name="uber_10k", description="Provides information about Uber financials for year 2021"
        ),
    ),
]
```
:::

::: {.cell .markdown id="kL1xN3SnNNr_"}
### Create `SubQuestionQueryEngine`
:::

::: {.cell .code execution_count="15" id="d-4zLgq8NTaR"}
``` python
sub_question_query_engine = SubQuestionQueryEngine.from_defaults(
    query_engine_tools=query_engine_tools
)
```
:::

::: {.cell .markdown id="umqoF0qNNZL8"}
### Querying {#querying}
:::

:::: {.cell .code execution_count="17" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":409}" id="k5wLiAiD6Xsy" outputId="2a7b85df-0be9-4f9e-be45-3413d9838395"}
``` python
response = await sub_question_query_engine.aquery(
    "Compare revenue growth of Uber and Lyft from 2020 to 2021"
)
```

::: {.output .stream .stdout}
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    Generated 4 sub questions.
    [uber_10k] Q: What was Uber's revenue in 2020?
    [uber_10k] Q: What was Uber's revenue in 2021?
    [lyft_10k] Q: What was Lyft's revenue in 2020?
    [lyft_10k] Q: What was Lyft's revenue in 2021?
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    [lyft_10k] A: According to Lyft's consolidated statements of operations data, Lyft's total revenue in 2020 was $2,364,681,000.
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    [uber_10k] A: According to Uber's consolidated statements of operations, Uber's revenue in 2021 was $17,455 million.
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    [uber_10k] A: According to Uber's consolidated statements of operations, Uber's revenue in 2020 was $11,139 million.
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    [lyft_10k] A: According to Lyft's consolidated statements of operations, Lyft's total revenue in 2021 was $3,208,323,000. This consisted of:

    - Revenue from contracts with customers (under ASC 606) of $2,957,979,000
    - Rental revenue (under ASC 842) of $250,344,000

    So in total, Lyft generated revenue of $3,208,323,000 in the year ended December 31, 2021.
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
:::
::::

:::: {.cell .code execution_count="18" id="PgVULcF6I0bH"}
``` python
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))
```

::: {.output .display_data}
<p style="font-size:20px">Uber and Lyft both saw significant revenue growth from 2020 to 2021:

Uber's revenue increased from $11,139 million in 2020 to $17,455 million in 2021. This represents year-over-year growth of about 56.7%.

Lyft's total revenue grew from $2,364,681,000 in 2020 to $3,208,323,000 in 2021, an increase of approximately 35.7%. 

So while Lyft started from a lower revenue base, Uber achieved higher revenue growth in percentage terms between 2020 and 2021 (56.7% vs 35.7%).

Both companies rebounded strongly in 2021 after seeing major impacts to their ride-sharing businesses in 2020 due to the COVID-19 pandemic. But Uber was able to grow its revenue more rapidly to reach $17.5 billion, compared to $3.2 billion for Lyft.</p>
:::
::::

:::: {.cell .code execution_count="19"}
``` python
response = await sub_question_query_engine.aquery("Compare the investments made by Uber and Lyft")
```

::: {.output .stream .stdout}
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    Generated 4 sub questions.
    [uber_10k] Q: What investments did Uber make in 2021
    [uber_10k] Q: What was the total amount invested by Uber in 2021
    [lyft_10k] Q: What investments did Lyft make in 2021
    [lyft_10k] Q: What was the total amount invested by Lyft in 2021
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    [uber_10k] A: Based on the context provided, in 2021 Uber invested:

    - $2.3 billion in acquisition of businesses, net of cash acquired
    - $1.1 billion in purchases of marketable securities  
    - $982 million in purchases of non-marketable equity securities
    - $297 million in purchases of notes receivable
    - $298 million in purchases of property and equipment

    So in total, Uber invested approximately $5.0 billion in 2021 across business acquisitions, marketable and non-marketable securities, notes receivable, and property and equipment purchases.
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    [lyft_10k] A: Based on the context provided, in 2021 Lyft invested in marketable securities and term deposits:

    - Lyft purchased marketable securities of $3.8 billion in 2021. The marketable securities consisted of investment grade available-for-sale debt securities. 

    - Lyft also invested in term deposits of $0.5 billion in 2021. The term deposits were at cost, which approximated fair value.

    As of December 31, 2021, Lyft's investment portfolio had a weighted-average remaining maturity of less than one year. Lyft's investment policy is designed to minimize exposure to credit losses.
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    [uber_10k] A: Based on the provided context, in 2021 Uber made investments to:

    - Increase the number of Drivers, consumers, merchants, shippers, and carriers using their platform through incentives, discounts, and promotions
    - Expand within existing markets and into new markets  
    - Increase research and development expenses
    - Expand marketing channels and operations
    - Hire additional employees
    - Add new products and offerings to their platform

    The context indicates Uber expected to incur losses in the near term as a result of substantial increases in operating expenses from continuing to make these types of investments.
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
    [lyft_10k] A: Based on the financial information provided in the context, the cash flow statement shows that Lyft had net cash provided by investing activities of $267.0 million for the year ended December 31, 2021. This primarily consisted of:

    - Proceeds from sales and maturities of marketable securities of $3.8 billion  
    - Maturities of term deposits of $675.5 million
    - Partially offset by purchases of marketable securities of $3.8 billion and term deposits of $0.5 billion

    So while the total proceeds from sales/maturities was around $4.5 billion, Lyft reinvested most of that, with net new investments of approximately $267 million in 2021.
    HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
:::
::::

:::: {.cell .code execution_count="20"}
``` python
display(HTML(f'<p style="font-size:20px">{response.response}</p>'))
```

::: {.output .display_data}
<p style="font-size:20px">In 2021, Uber and Lyft made different types of investments:

Uber invested a total of approximately $5.0 billion, which included:
- $2.3 billion in acquisition of businesses 
- $1.1 billion in marketable securities
- $982 million in non-marketable equity securities
- $297 million in notes receivable 
- $298 million in property and equipment

Lyft had net investments of around $267 million, primarily in:
- Marketable securities, with purchases of $3.8 billion, offset by sales and maturities of $3.8 billion
- Term deposits of $0.5 billion, offset by maturities of $675.5 million

So while Uber invested heavily in acquiring businesses, securities, notes, and property, Lyft focused its investments on shorter-term marketable securities and term deposits, with most proceeds being reinvested. Uber's investments were substantially larger in total dollar amount compared to Lyft's net investments in 2021.</p>
:::
::::
