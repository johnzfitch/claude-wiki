::: {.cell .markdown id="813NspGRKhc2"}
# RAG Pipeline with LlamaIndex

In this notebook we will look into building Basic RAG Pipeline with
LlamaIndex. The pipeline has following steps.

1.  Setup LLM and Embedding Model.
2.  Download Data.
3.  Load Data.
4.  Index Data.
5.  Create Query Engine.
6.  Querying.
:::

::: {.cell .markdown id="qYHCYDecKDRZ"}
### Installation
:::

::: {.cell .code id="mLTzvn__ldjd"}
``` python
!pip install llama-index
!pip install llama-index-llms-anthropic
!pip install llama-index-embeddings-huggingface
```
:::

::: {.cell .markdown id="Iu-wU44BKF9c"}
### Setup API Keys
:::

::: {.cell .code execution_count="1" id="ku5rkxtIlpCs"}
``` python
import os

os.environ["ANTHROPIC_API_KEY"] = "YOUR Claude API KEY"
```
:::

::: {.cell .markdown id="jJTRVhkJKH4r"}
### Setup LLM and Embedding model

We will use anthropic latest released `Claude 3 Opus` models
:::

::: {.cell .code execution_count="2" id="fQ0tqJL_mSe0"}
``` python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.anthropic import Anthropic
```
:::

::::::::: {.cell .code execution_count="3" id="snc2jpj4nlXJ"}
``` python
llm = Anthropic(temperature=0.0, model="claude-opus-4-1")
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
```

::: {.output .display_data}
``` json
{"model_id":"74a676bbd1d04390b4449a42b98a4428","version_major":2,"version_minor":0}
```
:::

::: {.output .display_data}
``` json
{"model_id":"779eefefc7dc49bb9244dc54822d2195","version_major":2,"version_minor":0}
```
:::

::: {.output .display_data}
``` json
{"model_id":"167e22b0490c4c17a6a2ac3c1861e75a","version_major":2,"version_minor":0}
```
:::

::: {.output .display_data}
``` json
{"model_id":"7f0e9e699cfb47b2bbe92756e95131ac","version_major":2,"version_minor":0}
```
:::

::: {.output .display_data}
``` json
{"model_id":"2623fec06f4c4fcd8fbaa496a0652b5e","version_major":2,"version_minor":0}
```
:::

::: {.output .display_data}
``` json
{"model_id":"33d6ff6e06214af08c3474e2c9daf830","version_major":2,"version_minor":0}
```
:::
:::::::::

::: {.cell .code execution_count="4" id="YmN2FEQFnx6Y"}
``` python
from llama_index.core import Settings

Settings.llm = llm
Settings.embed_model = embed_model
Settings.chunk_size = 512
```
:::

::: {.cell .markdown id="BqdSyD2_KK-m"}
### Download Data
:::

:::: {.cell .code execution_count="5" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="zC7CD222n72t" outputId="42c54b8a-bec9-4c2e-9cd5-97387f7011eb"}
``` python
!mkdir -p 'data/paul_graham/'
!wget 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/paul_graham/paul_graham_essay.txt' -O 'data/paul_graham/paul_graham_essay.txt'
```

::: {.output .stream .stdout}
    --2024-03-08 06:51:30--  https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/paul_graham/paul_graham_essay.txt
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.109.133, 185.199.108.133, 185.199.110.133, ...
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.109.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 75042 (73K) [text/plain]
    Saving to: ‘data/paul_graham/paul_graham_essay.txt’

    data/paul_graham/pa 100%[===================>]  73.28K  --.-KB/s    in 0.002s  

    2024-03-08 06:51:30 (34.6 MB/s) - ‘data/paul_graham/paul_graham_essay.txt’ saved [75042/75042]
:::
::::

::: {.cell .code execution_count="6" id="Ea9GbN2poO3V"}
``` python
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
)
```
:::

::: {.cell .markdown id="2dOGl_SKKUNH"}
### Load Data
:::

::: {.cell .code execution_count="7" id="Q4hWhnhxoUBj"}
``` python
documents = SimpleDirectoryReader("./data/paul_graham").load_data()
```
:::

::: {.cell .markdown id="XM3-kLhdKRk1"}
### Index Data
:::

::: {.cell .code execution_count="8" id="yvblCnWYKSrh"}
``` python
index = VectorStoreIndex.from_documents(
    documents,
)
```
:::

::: {.cell .markdown id="a17Tz644KZ_P"}
### Create Query Engine
:::

::: {.cell .code execution_count="9" id="LIT8kqYKoaRq"}
``` python
query_engine = index.as_query_engine(similarity_top_k=3)
```
:::

::: {.cell .markdown id="n6ODGRTxKd-u"}
### Test Query
:::

::: {.cell .code execution_count="10" id="igdrBclbKYrJ"}
``` python
response = query_engine.query("What did author do growing up?")
```
:::

:::: {.cell .code execution_count="11" colab="{\"base_uri\":\"https://localhost:8080/\"}" id="ap-6RUvSozgE" outputId="37ba0327-afe7-4f1e-d862-0412085954c8"}
``` python
print(response)
```

::: {.output .stream .stdout}
    Based on the information provided, the author worked on two main things outside of school before college: writing and programming.

    For writing, he wrote short stories as a beginning writer, though he felt they were awful, with hardly any plot and just characters with strong feelings.

    In terms of programming, in 9th grade he tried writing his first programs on an IBM 1401 computer that his school district used. He and his friend got permission to use it, programming in an early version of Fortran using punch cards. However, he had difficulty figuring out what to actually do with the computer at that stage given the limited inputs available.
:::
::::
