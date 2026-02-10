::: {#6d20a415-d81e-4ec7-9394-990594f041dc .cell .markdown}
# Multi-Modal

In this notebook, we show how to use Anthropic MultiModal LLM
class/abstraction for image understanding/reasoning.
:::

::: {#d6c9bf74-513c-43ee-b827-ad5a88122909 .cell .markdown}
#### Installation
:::

::: {#868a4f29-dbf6-4b78-9996-371e5cd18a3b .cell .code}
``` python
!pip install llama-index
!pip install llama-index-multi-modal-llms-anthropic
!pip install llama-index-embeddings-huggingface
!pip install llama-index-vector-stores-qdrant
!pip install matplotlib
```
:::

::: {#b40b3831-60a4-4a8f-a0fd-dff9f2289672 .cell .markdown}
#### Setup API key
:::

::: {#34138724-eca7-4b83-bbc1-e6c8b6b0f519 .cell .code execution_count="1"}
``` python
import os

os.environ["ANTHROPIC_API_KEY"] = "YOUR Claude API KEY"
```
:::

::: {#79a4fe80-6398-4924-8e2f-344d19446132 .cell .markdown}
#### Download Sample Images
:::

:::: {#5b464880 .cell .code execution_count="2"}
``` python
!wget 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/images/prometheus_paper_card.png' -O 'prometheus_paper_card.png'
!wget 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/images/ark_email_sample.PNG' -O 'ark_email_sample.png'
```

::: {.output .stream .stdout}
    --2024-03-08 11:53:40--  https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/images/prometheus_paper_card.png
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.111.133, 185.199.109.133, ...
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 1002436 (979K) [image/png]
    Saving to: ‘prometheus_paper_card.png’

    prometheus_paper_ca 100%[===================>] 978.94K  --.-KB/s    in 0.005s  

    2024-03-08 11:53:40 (175 MB/s) - ‘prometheus_paper_card.png’ saved [1002436/1002436]

    --2024-03-08 11:53:40--  https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/images/ark_email_sample.PNG
    Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.111.133, 185.199.109.133, ...
    Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 56608 (55K) [image/png]
    Saving to: ‘ark_email_sample.png’

    ark_email_sample.pn 100%[===================>]  55.28K  --.-KB/s    in 0.001s  

    2024-03-08 11:53:40 (72.9 MB/s) - ‘ark_email_sample.png’ saved [56608/56608]
:::
::::

::: {#e4a258f6-6151-46ed-9fd2-61d0b5b599d7 .cell .markdown}
#### Use Anthropic to understand Images from Local directory
:::

::::: {#8b431bd6-8e07-4668-9c04-2690ad2c2c96 .cell .code execution_count="3"}
``` python
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open("./prometheus_paper_card.png")
plt.imshow(img)
```

::: {.output .execute_result execution_count="3"}
    <matplotlib.image.AxesImage at 0x7f69551b93c0>
:::

::: {.output .display_data}
![](5f9d5d145aca91a94839c7835c974eb10d406c5d.png)
:::
:::::

::: {#ada2979f-da8b-42dc-b465-b96603604943 .cell .code execution_count="4"}
``` python
from llama_index.core import SimpleDirectoryReader
from llama_index.multi_modal_llms.anthropic import AnthropicMultiModal

image_documents = SimpleDirectoryReader(input_files=["prometheus_paper_card.png"]).load_data()

# Initiated Anthropic MultiModal class
anthropic_mm_llm = AnthropicMultiModal(max_tokens=300)
```
:::

::: {#b0c54c4d-dad9-47c5-acbe-99139e911bda .cell .code execution_count="5"}
``` python
response = anthropic_mm_llm.complete(
    prompt="Describe the images as an alternative text",
    image_documents=image_documents,
)
```
:::

:::: {#e7223a93 .cell .code execution_count="6"}
``` python
print(response)
```

::: {.output .stream .stdout}
    The image is a diagram titled "Prometheus: Inducing Fine-Grained Evaluation Capability In Language Models". It outlines the key components and workflow of the Prometheus system.

    The main sections are:
    1. Contributions: Describes Prometheus as an open-source LLM evaluator that uses custom rubrics for fine-grained evaluations.
    2. Feedback Collection: A dataset for fine-tuning evaluator LLMs with custom, fine-grained score rubrics. This section visually shows the process of seeding score rubrics, generating scores, generating instructions, and outputting training instances to create the Feedback Collection.
    3. Results: Lists 3 key results - Prometheus matches or outperforms GPT-4 on 3 evaluation datasets, can function as a reward model to help LLMs achieve high agreement with human evaluators on ranking, and enables reference answers for LM evaluations via an ablation study and feedback distillation.
    4. Insights: Notes that strong LLMs like GPT-4 show high agreement with human evaluations, but their closed-source nature and uncontrolled variations render them a less than ideal choice for many LLM application developers compared to an equally-good open-source option.
    5. Technical Bits: Provides a citation to the full paper with more technical details.

    The diagram uses
:::
::::

::: {#b2bfe150-f9e7-4a0d-9b43-37270fe5a22f .cell .markdown}
#### Use `AnthropicMultiModal` to reason images from URLs
:::

::: {#7d68abc6-9908-40fb-9b0d-0ab06db6f125 .cell .code}
``` python
from io import BytesIO

import matplotlib.pyplot as plt
import requests
from PIL import Image

image_urls = [
    "https://venturebeat.com/wp-content/uploads/2024/03/Screenshot-2024-03-04-at-12.49.41%E2%80%AFAM.png",
]

img_response = requests.get(image_urls[0], timeout=30)
img = Image.open(BytesIO(img_response.content))
plt.imshow(img)
```
:::

::: {#4fbe6eac .cell .markdown}
#### Load images with url
:::

::: {#25e8b224 .cell .code execution_count="8"}
``` python
from llama_index.core.multi_modal_llms.generic_utils import load_image_urls

image_url_documents = load_image_urls(image_urls)
```
:::

::: {#a8496170-e1c8-4b5c-912e-cff058b48ecd .cell .code execution_count="9"}
``` python
response = anthropic_mm_llm.complete(
    prompt="Describe the images as an alternative text",
    image_documents=image_url_documents,
)
```
:::

:::: {#403e4ffa-34da-4e05-b9cc-273450fef8ec .cell .code execution_count="10"}
``` python
print(response)
```

::: {.output .stream .stdout}
    The image shows a table comparing the benchmark scores of various Claude 3 AI models (Opus, Sonnet, Haiku) against GPT-4, GPT-3.5, and two versions of Gemini (1.0 Ultra and 1.0 Pro) across different academic subjects and tests.

    The subjects covered include undergraduate and graduate level knowledge, grade school math, math problem-solving, multilingual math, code, reasoning over text, mixed evaluations, knowledge Q&A, and common knowledge.

    The scores are presented as percentages, except for the "Reasoning over text" row which shows raw scores out of a certain number of shots.

    Overall, the Claude 3 models show competitive performance compared to the GPT and Gemini models across most of the benchmarks. The Gemini models have a slight edge in some categories like undergraduate knowledge and math problem-solving.
:::
::::

::: {#fb5bd03b-f841-4a47-9189-7184d900282f .cell .markdown}
#### Structured Output Parsing from an Image

Here, we use our multi-modal Pydantic program to generate structured
output from an image.
:::

::: {#dd72fd73-0622-4e9d-b193-32546efc2e4b .cell .code execution_count="11"}
``` python
from llama_index.core import SimpleDirectoryReader

image_documents = SimpleDirectoryReader(input_files=["ark_email_sample.png"]).load_data()
```
:::

::::: {#ca0324a6-91a8-4802-b3ee-1efb49b103e1 .cell .code execution_count="12"}
``` python
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open("ark_email_sample.png")
plt.imshow(img)
```

::: {.output .execute_result execution_count="12"}
    <matplotlib.image.AxesImage at 0x7f68972716c0>
:::

::: {.output .display_data}
![](d6a4d9474ac1a461c9136a793ae9cba00b2e08c3.png)
:::
:::::

::: {#e44c3e09-f344-4251-8a95-9e00744d68b5 .cell .code execution_count="13"}
``` python
from pydantic import BaseModel


class TickerInfo(BaseModel):
    """List of ticker info."""

    direction: str
    ticker: str
    company: str
    shares_traded: int
    percent_of_total_etf: float


class TickerList(BaseModel):
    """List of stock tickers."""

    fund: str
    tickers: list[TickerInfo]
```
:::

::: {#2bf92cb4-e55b-49a9-81c4-9246d08ad81b .cell .code execution_count="14"}
``` python
from llama_index.core.program import MultiModalLLMCompletionProgram
from llama_index.multi_modal_llms.anthropic import AnthropicMultiModal

prompt_template_str = """\
Can you get the stock information in the image \
and return the answer? Pick just one fund.

Make sure the answer is a JSON format corresponding to a Pydantic schema. The Pydantic schema is given below.

"""

# Initiated Anthropic MultiModal class
anthropic_mm_llm = AnthropicMultiModal(max_tokens=300)


llm_program = MultiModalLLMCompletionProgram.from_defaults(
    output_cls=TickerList,
    image_documents=image_documents,
    prompt_template_str=prompt_template_str,
    multi_modal_llm=anthropic_mm_llm,
    verbose=True,
)
```
:::

:::: {#f3d6b2e6-d4cc-4f3a-b100-051596ef8ad5 .cell .code execution_count="15"}
``` python
response = llm_program()
```

::: {.output .stream .stdout}
    > Raw output: {
      "fund": "ARKK",
      "tickers": [
        {
          "direction": "Buy",
          "ticker": "TSLA",
          "company": "TESLA INC",
          "shares_traded": 93664,
          "percent_of_total_etf": 0.2453
        }
      ]
    }
:::
::::

:::: {#f5dfbdd8-937a-4639-b196-ef864096fdc5 .cell .code execution_count="16"}
``` python
print(response)
```

::: {.output .stream .stdout}
    fund='ARKK' tickers=[TickerInfo(direction='Buy', ticker='TSLA', company='TESLA INC', shares_traded=93664, percent_of_total_etf=0.2453)]
:::
::::
