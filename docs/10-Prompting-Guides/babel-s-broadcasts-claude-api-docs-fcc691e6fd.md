---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:57Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/babels-broadcasts"
title: "Babel's broadcasts - Claude API Docs"
---

Prompt Library

# Babel's broadcasts

Copy page

Create compelling product announcement tweets in the world's 10 most spoken languages.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| User | Write me a series of product announcement tweets in the 10 most commonly spoken languages. The product is a new state of the art pair of binoculars with built-in AI systems to identify the animals viewed through the binoculars. The tweets should be exciting, cutting edge, and push consumer interest. |
| User | A future where humans can upload their consciousness into a digital realm. |

### 

Example output

> Here are a series of product announcement tweets in the 10 most commonly spoken languages for a new state-of-the-art pair of binoculars with built-in AI systems to identify animals:
>
> English:  
> Introducing the future of bird/wildlife watching! Our new AI binoculars use cutting-edge vision tech to instantly identify any animal you see. Bring the great outdoors to life like never before! \#NatureTech \#AIBinoculars
>
> Mandarin Chinese:  
> 令人兴奋的新品上市!我们的 AI 双筒望远镜融合了尖端视觉技术,可即时识别你所见的任何动物。让大自然的奇迹在你眼前展现,体验前所未有的观赏体验!#智能科技 \#AIBinoculars
>
> Hindi:  
> बर्ड/वन्यजीव वॉचिंग के लिए भविष्य का अविष्कार! हमारी नई एआई दूरबीनें अत्याधुनिक दृष्टि प्रौद्योगिकी का उपयोग करती हैं, जो आपको दिखाई देने वाले किसी भी जानवर की पहचान करने में सक्षम हैं। पहले कभी न देखी प्रकृति के अद्भुत दृश्यों का अनुभव करें! \#NatureWonders \#AIBinoculars
>
> Spanish:  
> ¡Presentamos el futuro de la observación de aves/vida silvestre! Nuestros nuevos binoculares con IA utilizan técnicas avanzadas de visión para identificar instantáneamente cualquier animal que veas. ¡Experimenta la naturaleza como nunca antes! \#TecnologíaNatural \#PrismáticosIA
>
> Arabic:  
> نقدم لكم مستقبل مراقبة الطيور/الحياة البرية! توفر نظارات المجهر الجديدة لدينا المزودة بالذكاء الاصطناعي تقنيات رؤية متطورة لتحديد هوية أي حيوان تراه على الفور. شاهد عجائب الطبيعة كما لم تفعل من قبل! \#تكنولوجيا*الطبيعة \#منظار*ذكي
>
> Bengali:  
> পাখি/বন্য প্রাণী পর্যবেক্ষণের ভবিষ্যতের উন্মোচন! আমাদের নতুন এআই দুর্বীনগুলি অত্যাধুনিক ভিশন প্রযুক্তি ব্যবহার করে যেকোনো প্রাণীকে দ্রুত চিহ্নিত করতে সক্ষম। প্রকৃতির অপরূপ দৃশ্য আগেকার চেয়ে ভিন্নভাবে উপভোগ করুন! \#প্রাকৃতিকপ্রযুক্তি \#AIBinoculars
>
> Russian:  
> Представляем будущее наблюдения за птицами/дикой природой! Наши новые бинокли с ИИ используют передовые технологии компьютерного зрения для мгновенной идентификации любого животного. Откройте для себя природу по-новому! \#ПриродныеТехнологии \#БинокльСИИ
>
> Portuguese:  
> Apresentamos o futuro da observação de aves/vida selvagem! Os nossos novos binóculos com IA usam técnicas avançadas de visão para identificar instantaneamente qualquer animal que veja. Experiencie a natureza como nunca antes! \#TecnologiaNatural \#BinóculosIA
>
> Japanese:  
> 鳥/野生動物観察の未来をご紹介!新しい AI バイノキュラーは、最先端のビジョン技術を使用して、あなたが見たあらゆる動物をすばやく特定します。自然をこれまでにない方法で体験してください!#ネイチャーテック \#AI バイノキュラー
>
> Punjabi:  
> ਪੰਛੀਆਂ/ਜੰਗਲੀ ਜੀਵਨ ਦੇਖਣ ਦੇ ਭਵਿੱਖ ਦਾ ਐਲਾਨ! ਸਾਡੀਆਂ ਨਵੀਆਂ ਏਆਈ ਦੂਰਬੀਨਾਂ ਅਤਿ ਆਧੁਨਿਕ ਦ੍ਰਿਸ਼ਟੀ ਤਕਨਾਲੋਜੀ ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ ਜੋ ਤੁਸੀਂ ਦੇਖਦੇ ਹੋ ਕਿਸੇ ਵੀ ਜਾਨਵਰ ਦੀ ਸਿੱਧੀ ਪਛਾਣ ਕਰਨ ਦੇ ਸਮਰੱਥ ਹਨ। ਪ੍ਰਕਿਰਤੀ ਦਾ ਅਨੁਭਵ ਪਹਿਲਾਂ ਨਾਲੋਂ ਵੱਖਰੇ ਢੰਗ ਨਾਲ ਕਰੋ! \#NeighborhoodTech \#AIBinoculars

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
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Write me a series of product announcement tweets in the 10 most commonly spoken languages. The product is a new state of the art pair of binoculars with built-in AI systems to identify the animals viewed through the binoculars. The tweets should be exciting, cutting edge, and push consumer interest."
                }
            ]
        }
    ]
)
print(message.content)
```

Was this page helpful?

- 

- [Example output](#example-output)

- [API request](#api-request)

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
