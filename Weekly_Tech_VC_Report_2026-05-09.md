# 本周全球及中国一级市场科技重磅事件周报

**报告周期**：2026 年 5 月 3 日 – 2026 年 5 月 9 日
**编制日期**：2026 年 5 月 9 日（周六）
**覆盖范围**：美国 + 中国大陆 + 香港 一级市场科技/VC 重磅事件、三大热门行业聚焦，并以一节"重大科学突破"作为开篇

---

## 引言

本周全球一级市场延续 2026 年以来的"AI + 国防 + 能源 + 具身智能"四主线大爆发：美国 Sierra 单笔 9.5 亿美元、Anthropic 据 FT 报道筹划近 1 万亿美元估值的 500 亿美元巨额融资、SpaceX S-1 即将提交并与 Anthropic 签订算力合作；中国 Moonshot AI 完成 20 亿美元 D 轮、CATL 港股配售后股价创新高、百度昆仑芯启动科创板 IPO 流程并锁定 100 亿美元 + 港股估值。资本流向高度集中在「LLM 智能体」、「太空国防」、「核电+数据中心」、「新能源车与电池」、「具身智能机器人」五大轨道。本周报开篇先以纯科学视角总结过去 7 天值得记入"长周期"的**重大科学突破**，再进入产业与一级市场深度分析；所有关键事实均带主源链接。

---

# 重大科学突破 (本周纯科学亮点)

> 仅纯科学维度，不涉及商业/VC 含义；如下条目均带 inline 引用。

▶ **二维 KPZ 生长普适律首次在量子系统中被实验验证** — 维尔茨堡大学利用半导体内的极化子量子体系，验证了 40 年前提出的 Kardar-Parisi-Zhang (KPZ) 方程在二维系统中同样成立，意味着从晶体生长到肿瘤扩张的众多过程可能共享同一数学规律。([ScienceDaily, 2026-05-05](https://www.sciencedaily.com/releases/2026/05/260505234622.htm))

▶ **宇宙基本常数处于"恰好允许细胞内液体流动"的极窄甜点带** — 伦敦玛丽女王大学发现普朗克常数、电子电荷等基本常数若略有偏移，血液会过粘、水会过稠，生命无法存在；为"微调宇宙"假说提供新证据。([ScienceDaily, 2026-05-08](https://www.sciencedaily.com/releases/2026/05/260508022653.htm))

▶ **AlphaFold2 引导下首次造出"19 个氨基酸"的活细菌 Ec19** — 工程菌株 Ec19 在去除一种规范氨基酸后，连续繁殖 450 代仍生长正常，挑战"生命必需 20 种氨基酸"的金科玉律。([Phys.org, 2026-05](https://phys.org/news/2026-05-life-bacteria-amino-acid.html))

▶ **14.5 km 城域多路复用量子中继器实现 Bell 非局域性** — 在 78.6% Bell 态保真度下完成异地量子记忆体之间的纠缠分发，且无需相位稳定，是量子互联网的关键里程碑。([Nature Photonics, 2026-05](https://www.nature.com/articles/s41566-026-01911-5))

▶ **牛津在单囚禁离子上首次演示"四维压缩 (quadsqueezing)"量子相互作用** — 通过两种非对易力组合，制造出此前从未被观测到的量子态，为量子传感与量子模拟开辟新路径。([SciTechDaily, 2026-05](https://scitechdaily.com/quantum-breakthrough-turns-simple-forces-into-powerful-new-interactions/))

▶ **人类基因组发现 1,700+ 类蛋白"peptidein"小分子** — 国际团队在以往视为"暗区"的基因组区段内识别出超过 1,700 种新型小肽样分子，显著扩展人类蛋白组学边界，对癌症、慢病机制研究意义重大。([ISB Science, 2026-05](https://isbscience.org/news/chronic-illness/proteins-and-disease/new-protein-like-molecules-human-genome/))

▶ **片上连续可调频率梳半导体激光器** — Nature 报告一款单片半导体激光器可在 4–16 GHz 范围内连续调谐重复频率，为高分辨光谱、激光雷达、光通信提供全新光源。([Nature, 2026-05](https://www.nature.com/articles/s41586-026-10387-w))

▶ **首次温和合成原子级精确"碳锥" C70H20** — 中国主导的团队成功合成首个原子级精确的碳锥分子，解决 20 年悬而未决的合成难题，为新型碳材料家族再添成员。([Science Advances, 2026-05](https://www.science.org/doi/10.1126/sciadv.aaw0982))

---

# 第一部分：三大热门行业聚焦

## 美国三大热门行业

### 一、企业级 AI 智能体与基础模型基础设施 (Enterprise AI Agents & Foundation-Model Infra)

▶ **行业概述**：从对话式 LLM 向"端到端代理工作流"演进，企业 SaaS 与 LLM 服务边界融合；底层是 NVIDIA、AMD、自研 ASIC、推理云、向量数据库等基础设施栈。

▶ **资本动量**：2026 Q1 美国 VC 投资 2,672 亿美元创纪录，OpenAI ($122B)、Anthropic ($30.6B)、xAI ($20B)、Waymo ($16B) 四大巨型轮支撑；本周 Sierra 9.5 亿美元 / 估值 >150 亿美元，Anthropic 据 FT 在谈 500 亿美元、估值近 1 万亿美元。([KPMG Venture Pulse Q1 2026](https://kpmg.com/us/en/articles/2026/venture-pulse-q1-2026.html), [TechCrunch 2026-05-04](https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/), [Tech Startups 2026-05-08](https://techstartups.com/2026/05/08/anthropic-eyes-1-trillion-valuation-in-new-funding-round-as-revenue-surges-ft-reports/))

▶ **政策与政府姿态**：白宫 AI Action Plan 推动联邦机构、国防部加速采购 AI 智能体；OpenAI、Anthropic 已签署国防部框架合同；HALEU 燃料与电力配套也按"AI 国家战略"推进。([AI Action Plan](https://www.ai.gov/action-plan))

▶ **5 年货币化路径**：已从理论走向实证 — Sierra 三个月 ARR 从 1 亿美元跃升至 1.5 亿，Anthropic 年化收入将突破 450 亿美元。可清晰看到"按交互结果计费"的代理 SaaS、推理算力按需销售两条主曲线在 2027–2030 进入百亿到千亿美元收入区间。([CNBC 2026-05-04](https://www.cnbc.com/2026/05/04/bret-taylor-sierra-fundraise-openai.html))

### 二、国防科技与太空优势 (Defense Tech & Space Superiority)

▶ **行业概述**：自主无人机/船舶/卫星 + 太空态势感知 + AI 指挥控制软件；面向"金穹 (Golden Dome)"导弹防御和印太前沿部署形成完整产业链。

▶ **资本动量**：True Anomaly 6.5 亿美元 D 轮 (4/28，估值 22 亿美元)、Astranis 4.5 亿美元 (5 月初)；2025 年国防科技 IPO 表现优于大盘，Anduril 估值 310 亿美元。([SpaceNews](https://spacenews.com/true-anomaly-raises-650-million-reaching-2-2-billion-valuation/), [Astranis](https://www.astranis.com/blog/series-e-raise-advanced-high-orbit-spacecraft), [Fortune 2026-05-06](https://fortune.com/2026/05/06/anduril-ceo-brian-schimpf-defense-tech-military-pentagon-palmer-luckey/))

▶ **政策与政府姿态**：金穹项目签 12 家承包商共 32 亿美元原型合同，True Anomaly 是唯一专注太空防御的入围方；国防部"无人机优势"项目持续放量；FY2026 国防预算明确为商业双重用途科技倾斜。([TheNextWeb](https://thenextweb.com/news/true-anomaly-650m-space-defence-golden-dome), [Bessemer Defense Roadmap](https://www.bvp.com/atlas/defense-tech-roadmap-five-frontiers-for-2026))

▶ **5 年货币化路径**：5 年内 SpaceX (1.5–2 万亿美元 IPO 预计 6 月路演)、Anduril、True Anomaly 等头部公司将通过 IPO/二级市场释放数千亿美元流动性；周期性国防订单和"按任务收费"卫星即服务形成稳定经常性收入。([Motley Fool](https://www.fool.com/investing/2026/05/05/most-important-spacex-ipo-filing-is-2-weeks-away/))

### 三、核电与 AI 数据中心电力 (Nuclear + Power for AI)

▶ **行业概述**：包括小型模块化反应堆 (SMR、TerraPower、Oklo、X-energy)、HALEU 燃料、传统核电改造、超大型数据中心专用电力 PPA。

▶ **资本动量**：美国共有 ~111 个核能资本项目、合计 ~2,110 亿美元在建；DOE 向南方公司提供 265 亿美元贷款/补助；本周 SpaceX-Anthropic 协议确认 Colossus 1 数据中心 >300 MW 容量并研究 SpaceX 轨道数据中心方案。([Industrial Info](https://www.industrialinfo.com/news/article/us-nuclear-renaissance-enters-steel-in-ground-phase--357223), [SpaceNews 2026-05-06](https://spacenews.com/anthropic-to-consider-using-spacex-orbital-data-center-satellites/))

▶ **政策与政府姿态**：特朗普 2025 年 5 月《国家安全先进核能反应堆部署》行政令仍在落地：陆军基地建堆、DOE 站点 30 个月内部署、20 公吨 HALEU 释放给私营 AI 反应堆。([White House](https://www.whitehouse.gov/fact-sheets/2025/05/fact-sheet-president-donald-j-trump-deploys-advanced-nuclear-reactor-technologies-for-national-security/), [Akin Gump](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/executive-order-links-nuclear-reactor-development-to-ai-infrastructure-needs-for-national-security))

▶ **5 年货币化路径**：超大规模厂商已锁定 6,600 MW 新核电协议；TerraPower (Natrium 2030)、Oklo (Aurora 2028)、X-energy (Xe-100 2029) 进入兑现期；Brookfield、KKR 等资管巨头已布局电力基础设施基金，形成"长久期、通胀对冲、AI 兑现"三重叙事。([Morgan Lewis](http://www.morganlewis.com/pubs/2026/02/the-nuclear-industry-at-a-turning-point))

## 中国三大热门行业

### 一、开源大模型与 AI 自主基础设施

▶ **行业概述**：以 DeepSeek、Moonshot、智谱、阿里 Qwen、字节豆包为代表的开源/开权重大模型 + 华为昇腾、寒武纪、百度昆仑芯、海光等国产算力栈，构成"模型-芯片-云"自主闭环。

▶ **资本动量**：本周 Moonshot AI 20 亿美元 / 估值 200 亿美元；DeepSeek 与腾讯、Big Fund 谈 4 亿–40 亿美元区间不等的首次外部融资；昆仑芯启动科创板程序 + 港股 100 亿美元起步估值；上月 Lightelligence 港股首日涨 383% 至 100 亿美元。([TechCrunch 2026-05-07](https://techcrunch.com/2026/05/07/chinas-moonshot-ai-raises-2b-at-20b-valuation-as-demand-for-open-source-ai-skyrockets/), [TFN DeepSeek](https://techfundingnews.com/tencent-to-back-deepseek-in-4b-round-at-50b-valuation-marking-first-external-funding-report/), [SCMP 昆仑芯](https://www.scmp.com/tech/tech-trends/article/3352891/baidu-chip-unit-kunlunxin-eyes-us146b-valuation-hong-kong-ipo-sources))

▶ **政策与政府姿态**："十五五" (2026-2030) 规划将人工智能、量子、6G、脑机接口、生物制造列为"未来产业"；国家 AI 产业投资基金三期首次入股具身智能与 AI 芯片；外销 Kimi、DeepSeek 等开源模型被视为软实力工具。([Global Times 2026-01](https://www.globaltimes.cn/page/202601/1353864.shtml), [China.org 2026-03](http://www.china.org.cn/2026-03/10/content_118374605.shtml))

▶ **5 年货币化路径**：Moonshot ARR 已破 2 亿美元、Kimi K2.6 跃居 OpenRouter 第二；昆仑芯外部客户营收占比 >50%；2027–2030 期间国产算力 + 开源模型可形成 1,000 亿元人民币级别的国内 SaaS+API 市场，并向东南亚/中东输出。([Global Times 2026-04](https://www.globaltimes.cn/page/202604/1359843.shtml))

### 二、新能源车、动力电池与充换电网络

▶ **行业概述**：BYD、CATL、宁德、Xiaomi、Nio、Xpeng、理想 + 钠电、固态电池、800V 充电、换电网络、海外组装产能；产业链与"出海"深度绑定。

▶ **资本动量**：CATL 完成 50 亿美元港股配售（2026 港股最大），股价 5/6 创新高 460 元；Xiaomi SU7 改款 48 天斩获 8 万订单；CATL 钠电 60 GWh 全球最大订单。([Nikkei Asia](https://asia.nikkei.com/business/markets/equities/chinese-ev-battery-maker-catl-raises-5bn-in-hong-kong), [PaulTan 2026-05-07](https://paultan.org/2026/05/07/2026-xiaomi-su7-in-beijing/), [CarNewsChina 钠电](https://carnewschina.com/2026/04/27/catl-secures-worlds-largest-sodium-ion-battery-order-with-60-gwh-deal/))

▶ **政策与政府姿态**：十五五规划将"智能网联新能源汽车"列为战略新兴；国家继续以以旧换新、汽车下乡、L3/L4 路权扩张推动；地方电力部门为充换电、退役电池循环出台配套。([CIO 五年规划](http://english.scio.gov.cn/in-depth/2026-03/16/content_118384324.html))

▶ **5 年货币化路径**：2025 NEV 销量 1,649 万辆 (+28.2% YoY)，2030 估算渗透率 >75%；CATL 全球份额 40.7% 且在欧洲、北美、印尼、墨西哥布局；钠电+固态电池打开储能十年级新赛道。([CnEVPost CATL](https://cnevpost.com/2026/05/06/catl-shares-record-high-strong-may-battery-production-outlook/))

### 三、具身智能：人形机器人与 Robotaxi

▶ **行业概述**：上游 (减速器、6D 力觉、电机)、本体 (Unitree、AgiBot、Galbot、Galaxea、UBTech)、大脑模型 (空间智能 / 世界模型 / VLA)、应用 (汽车厂、仓储、零售、家庭) 完整产业链。

▶ **资本动量**：2026 YTD 中国机器人融资 ¥61.3B、人形机器人 ¥25.9B；Galbot ¥2.5B、Galaxea AI ¥2B、Unitree 申报科创板 IPO ¥4.2B；本周 LDROBOT 5/11 港股挂牌、估值 13 亿美元。([NewsGlobeNow](https://www.newsglobenow.com/new337440.html), [Caixin Galbot](https://www.caixinglobal.com/2026-03-03/galbot-raises-362-million-in-fresh-funding-eyes-hong-kong-ipo-102418742.html), [Caproasia LDROBOT](https://www.caproasia.com/2026/05/01/china-intelligent-robot-visual-technology-company-shenzhen-ldrobot-ledong-robotics-hong-kong-ipo-to-raise-128-million-at-1-3-billion-valuation-with-expected-ipo-listing-on-11th-may-2026-founded-i/))

▶ **政策与政府姿态**：国家 AI 产业投资基金三期首次入股具身智能（领投 Galbot），地方政府从北京、深圳到上海设具身智能基金、试点产线；"机器人 +"行动计划纳入工信部年度重点。([CnTechPost](https://cntechpost.com/2026/03/02/galbot-secures-major-state-backing/))

▶ **5 年货币化路径**：AgiBot 累计交付突破 1 万台、估算 38% 全球份额；WeRide-Lenovo 5 年 20 万辆部署；Pony.ai 第七代 Robotaxi BOM <23 万元，2027 年起在汽车厂和港口/园区落地有望年贡献 100 亿元级别营收。([SCMP Robotaxi](https://www.scmp.com/tech/tech-trends/article/3351581/chinese-robotaxi-firms-accelerate-global-roll-outs-cost-edge-drives-expansion))

---

# 第二部分：美国一级市场 Top 10

> 排序按本周一级市场冲击力（融资金额 × 估值跃升 × 行业代表性）综合。

## 1. Sierra ($950M / >$15B post)

▶ **公司简介与商业模式**：Sierra 由前 Salesforce 联席 CEO Bret Taylor 与前 Google 高管 Clay Bavor 创立，定位"企业级对话与工作流 AI 智能体平台"，按交互结果（成功解决率/转化率）计费，已服务 40% 财富 50 强，包括 Prudential、Cigna、Blue Cross Blue Shield 与三大美国银行之一。

▶ **本周事件**：5 月 4 日 Sierra 宣布 Tiger Global 与 Google Ventures (GV) 联合领投 9.5 亿美元，估值跃升至 150–158 亿美元，距上次（2025 年 9 月 100 亿美元）八个月翻 1.5 倍；ARR 从 2025 年 11 月的 1 亿美元跃升至 2026 年 2 月的 1.5 亿美元。([TechCrunch](https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/), [CNBC](https://www.cnbc.com/2026/05/04/bret-taylor-sierra-fundraise-openai.html), [SiliconANGLE](https://siliconangle.com/2026/05/04/ai-agent-startup-sierra-valued-15b-new-950m-funding-round/))

▶ **一级市场投资意义**：Sierra 是 OpenAI/Anthropic "模型层垄断"叙事下"应用层智能体平台"少数能维持 100% 留存与高毛利、并被 Tiger 这类成长型基金强力站台的标的，标志一级市场对"代理 SaaS"按结果计费模式的定价正式锚定 100x ARR 起步；同时验证 Bret Taylor 这条"OpenAI Chair + Sierra CEO"双线赛道形成的渠道与品牌护城河，可能成为 2027–2028 年最高确定性 IPO 候选。([TechCrunch](https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/))

## 2. Anthropic (~$50B 在谈 / 估值近 $1T 报道)

▶ **公司简介与商业模式**：Anthropic 是 OpenAI 联合创始人 Dario / Daniela Amodei 兄妹离职后创办的"安全优先" AI 实验室，以 Claude 系列大模型为核心 — Claude API、Claude.ai 订阅、Bedrock/Vertex 渠道分发，并提供 Government/DoD 专属版本。

▶ **本周事件**：FT 5 月 8 日报道 Anthropic 在与 Dragoneer、General Catalyst、Lightspeed 谈判一轮高达 500 亿美元的融资，估值近 9,000 亿至 1 万亿美元，比 2026 年 2 月 3,800 亿美元估值再翻倍；CFO Krishna Rao 主导，预计两个月内完成。年化收入将突破 450 亿美元，相比 2025 年底的 90 亿美元飙升。([Tech Startups](https://techstartups.com/2026/05/08/anthropic-eyes-1-trillion-valuation-in-new-funding-round-as-revenue-surges-ft-reports/), [Economic Times](https://m.economictimes.com/tech/funding/anthropic-weighs-fundraising-for-near-1-trillion-valuation-financial-times/articleshow/130947861.cms))

▶ **一级市场投资意义**：若成事，Anthropic 估值将一举超越 OpenAI 3 月 8,520 亿美元，并把美国一级市场"前沿模型实验室"的估值锚定推到万亿美元级，为 OpenAI、xAI、Mistral、Cohere 估值提供新天花板；同时也将抽走全球成长基金可投资本，挤压中型 AI 应用与基础设施 round 的竞争空间。还反向凸显 NVIDIA、AMD、TSMC、电力公司等"卖铲"环节的长期需求确定性。([PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/anthropic-valuation-could-eclipse-openai-50-billion-dollar-funding-round/))

## 3. SpaceX × Anthropic 算力联盟 + S-1 临门

▶ **公司简介与商业模式**：SpaceX 是 Elon Musk 创办的火箭+卫星+互联网+轨道数据中心一体化公司，主要收入来自 NASA/USSF 发射合同、Starlink 全球宽带订阅与企业/军政合同；Anthropic 见上条。

▶ **本周事件**：5 月 6 日 SpaceX 宣布将向 Anthropic 提供其德州地面 Colossus 1 数据中心 >300 MW 算力，并探索接入 SpaceX 在研的"轨道数据中心"卫星群（计划部署最多 100 万颗）；Motley Fool 5 月 5 日报道 SpaceX 的 IPO S-1 文件预计 2 周内提交，估值 1.75 万亿–2 万亿美元，6 月第二周开启路演。([SpaceNews](https://spacenews.com/anthropic-to-consider-using-spacex-orbital-data-center-satellites/), [Motley Fool](https://www.fool.com/investing/2026/05/05/most-important-spacex-ipo-filing-is-2-weeks-away/), [Economic Times](https://economictimes.indiatimes.com/markets/us-stocks/news/us-stock-market-spacex-openai-and-anthropic-set-stage-for-record-breaking-ipo-wave/articleshow/130483601.cms))

▶ **一级市场投资意义**：这是史上首次"前沿 AI 实验室 + 私营航天龙头"形成"算力+发射+网络"三位一体战略联盟，意味着大型语言模型对电力/算力供给的需求已突破地面工业能力上限，转向太空寻找解决方案；同时 SpaceX 1.75 万亿美元 IPO 一旦成行，将一举重写美国一级市场流动性结构，为 SpaceX 老股东（Founders Fund、a16z、Sequoia 等）兑现数百亿美元，并对国防、航天、能源等长周期资本的回报率假设产生连锁影响。([Motley Fool](https://www.fool.com/investing/2026/05/05/most-important-spacex-ipo-filing-is-2-weeks-away/))

## 4. Astranis ($300M Series E + $155M 信贷)

▶ **公司简介与商业模式**：Astranis 是位于旧金山的同步轨道 (GEO) 小型卫星制造商，为电信运营商和国防客户提供"专属国家"宽带和军事通信卫星，按"卫星即服务"模式销售。

▶ **本周事件**：5 月初 Astranis 宣布 Snowpoint Ventures 与 Franklin Templeton 联合领投 3 亿美元 E 轮股权融资 + 1.55 亿美元信贷，主要用于扩产以应对高轨道先进卫星暴增需求，已是一周第二大融资 round。([Astranis Blog](https://www.astranis.com/blog/series-e-raise-advanced-high-orbit-spacecraft), [Crunchbase Weekly](https://news.crunchbase.com/venture/biggest-funding-rounds-sierra-astrani-anagram-therapeutics/))

▶ **一级市场投资意义**：在 SpaceX 主导 LEO 发射链的背景下，Astranis 把 GEO 小卫星打造成"低门槛主权通信"产品，正赶上美国/盟友因 SpaceX 集中度过高而寻求多元化；4.5 亿美元的混合融资结构（股权 + 信贷）显示一级市场已开始用"基础设施金融"工具支持航天硬件公司，预示后续 Sequoia、KKR、Brookfield 等基金将加速布局"航天 PPP"赛道。([Crunchbase Weekly](https://news.crunchbase.com/venture/biggest-funding-rounds-sierra-astrani-anagram-therapeutics/))

## 5. Anagram Therapeutics ($250M Blackstone)

▶ **公司简介与商业模式**：位于马萨诸塞州 Natick 的临床期生物科技公司，专注于囊性纤维化等胰腺外分泌不全患者的口服小分子治疗，临床推进至关键 III 期，目标替代终生酶替代疗法。

▶ **本周事件**：5 月 7 日 Bloomberg 披露 Blackstone Life Sciences 通过股权 + 里程碑结构向 Anagram 投资 2.5 亿美元，是本周最大单笔生物科技融资，将用于完成 III 期试验和上市准备。([Bloomberg](https://www.bloomberg.com/news/articles/2026-05-07/blackstone-invests-250-million-in-biotech-startup-anagram-therapeutics), [Crunchbase Weekly](https://news.crunchbase.com/venture/biggest-funding-rounds-sierra-astrani-anagram-therapeutics/))

▶ **一级市场投资意义**：Blackstone 单一投资 2.5 亿美元是典型的"晚期权益替代 IPO"打法，意味着一级市场对临床末期生物科技"以买代发"的偏好回升；在美股小盘生科 IPO 窗口疲软情况下，大型 PE 接力填补 Series D/E 空白，这种模式在 2026 下半年可能扩展到罕见病和肿瘤靶向药领域，是观察 PE-VC 边界进一步模糊的关键案例。([Bloomberg](https://www.bloomberg.com/news/articles/2026-05-07/blackstone-invests-250-million-in-biotech-startup-anagram-therapeutics))

## 6. Blitzy ($200M @ $1.4B)

▶ **公司简介与商业模式**：Blitzy 是"自治软件开发"平台（vibe-coding 主力厂商之一），通过多智能体协同自动写代码、做架构决策与质量保障，按工程师等价人月或代码产物计价，已被数十家 Global 2000 企业使用。

▶ **本周事件**：本周 Blitzy 宣布 Northzone 领投 2 亿美元融资，估值 14 亿美元，正式跻身"自治编码独角兽"梯队，并计划用资金扩展企业销售团队、深化与 GitHub Enterprise、Atlassian 等开发栈集成。([Crunchbase News](https://news.crunchbase.com/ai/blitzy-funding-valuation-autonomous-software-development-vibe-coding-startups/))

▶ **一级市场投资意义**：这是 Cursor、Cognition、Magic、Augment 之后第四个"代码生成方向"独角兽，与 xAI 4 月底 600 亿美元收购 Cursor 期权事件形成共振，确认"AI 写代码"赛道已变成成长基金的"必投赛道"；同时 Northzone 这种欧洲基金提速进入北美 AI Tier-1 deal，反映欧洲 LP 对 AI 配置敞口的迫切补救。([Crunchbase News](https://news.crunchbase.com/ai/blitzy-funding-valuation-autonomous-software-development-vibe-coding-startups/))

## 7. Corgi Insurance ($160M Series B @ $1.3B)

▶ **公司简介与商业模式**：Corgi 是面向初创/中小企业的"AI 原生全栈商业保险平台"，从智能核保、批单、理赔到保单管理全数字化，正从科技 SaaS 公司主险扩展到货运、医疗等垂直行业。

▶ **本周事件**：本周 Corgi 宣布 TCV 领投 1.6 亿美元 B 轮，估值 13 亿美元，累计融资突破 2.68 亿美元，并宣布扩展到货运保险垂直。([PR Newswire](https://www.prnewswire.com/news-releases/corgi-raises-160-million-series-b-to-continue-expanding-its-full-stack-insurance-platform-into-new-verticals-302764003.html))

▶ **一级市场投资意义**：与同周 Reserv 的 1.25 亿美元一道，标志保险科技在历经 2022–2024 重估之后，新一代"AI 智能体改造承保/理赔"的公司正再度获得一线美元基金的高估值再融资，显示 InsurTech 2.0（智能体驱动）正在与"InsurTech 1.0"（D2C 直销）拉开差距。([VentureBeat Reserv](https://venturebeat.com/business/reserv-announces-125-million-series-c-financing-led-by-kkr-to-accelerate-ai-driven-transformation-of-insurance-claims))

## 8. Panthalassa ($140M led by Peter Thiel)

▶ **公司简介与商业模式**：Panthalassa 致力于"海上自主、海洋能驱动"的 AI 算力基础设施，将集装箱化数据中心放置于浮动平台上，利用海水冷却 + 离岸风/波浪能供电，目标成为下一代"零电网" AI Hyperscaler 的硬件层。

▶ **本周事件**：5 月 4 日 Panthalassa 宣布 Peter Thiel 领投 1.4 亿美元 B 轮，将用于在墨西哥湾及加州沿岸部署首批商用海上数据中心模块。([BusinessWire](https://www.businesswire.com/news/home/20260504552400/en/Panthalassa-Raises-%24140-Million-to-Power-AI-at-Sea))

▶ **一级市场投资意义**：与 SpaceX-Anthropic 轨道数据中心呼应，Panthalassa 提供"海上"答案，意味着投资者已开始为"地面电网无法满足 AI 用电"的硬约束寻找替代解；Founders Fund 系背书显示这类硬科技基础设施进入"早期独角兽 → 战略基础设施"快通道，5 年内可能与超大规模 hyperscaler 形成上游捆绑。([BusinessWire](https://www.businesswire.com/news/home/20260504552400/en/Panthalassa-Raises-%24140-Million-to-Power-AI-at-Sea))

## 9. Reserv ($125M Series C, KKR)

▶ **公司简介与商业模式**：Reserv 是 AI 驱动的第三方理赔服务商 (TPA)，通过智能体处理意外、财产、车险理赔的资料采集、欺诈识别与赔付决策，目标 4 年内将年理赔量从 50 万件扩至 3,000 万件。

▶ **本周事件**：本周 Reserv 宣布 KKR 领投 1.25 亿美元 C 轮，将用于扩展 AI 模型与并购同业 TPA。([VentureBeat](https://venturebeat.com/business/reserv-announces-125-million-series-c-financing-led-by-kkr-to-accelerate-ai-driven-transformation-of-insurance-claims))

▶ **一级市场投资意义**：KKR 这类大型 PE 直接做 Series C，等于把"AI 智能体改造保险后台"作为基础设施级 buy-and-build 战略，意味着未来 1–2 年保险中后台合规、理赔、再保险等环节将出现一连串 PE 牵头的 AI 整合并购，给传统保险后台 BPO 带来巨大重估压力。([VentureBeat](https://venturebeat.com/business/reserv-announces-125-million-series-c-financing-led-by-kkr-to-accelerate-ai-driven-transformation-of-insurance-claims))

## 10. DeepInfra ($107M Series B)

▶ **公司简介与商业模式**：DeepInfra 是面向企业的开源大模型推理云，提供 Llama、Mistral、DeepSeek、Qwen 等模型即服务，按 Token 计费，定位"成本效率优先"的推理 hyperscaler 替代品。

▶ **本周事件**：5 月初 DeepInfra 宣布 500 Global 与 Georges Harik 联合领投 1.07 亿美元 B 轮，将用于扩张推理 GPU 产能并接入更多客户的私有部署。([Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/deepinfra-closes-107m-series-b-160000545.html))

▶ **一级市场投资意义**：DeepInfra 与 Together AI、Fireworks、Anyscale 一同形成"独立推理云"梯队，挑战 AWS/Azure/GCP 在 AI 推理这一 100 亿美元 + 增长最快子市场上的定价权；与本周 SpaceX 数据中心、Panthalassa 海上数据中心、Anthropic 算力扩张事件相互印证：算力、能源、推理云三条供给侧曲线已成为 2026 一级市场最确定的"卖铲"主线。([Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/deepinfra-closes-107m-series-b-160000545.html))

## 美国全周趋势总结

▶ **资本量级断层式分化**：本周美国披露融资额（含报道中）合计接近 540 亿美元，仅 Anthropic + Sierra + SpaceX 三家就占绝对主导，AI/算力/航天/国防形成新的"四龙头集中度"。

▶ **新主题"AI 物理基础设施"成型**：地面核电 (Trump EO)、海上数据中心 (Panthalassa)、轨道数据中心 (SpaceX)、独立推理云 (DeepInfra) 同步获得资本，标志 AI 不再只是软件和模型，而是对全美能源-土地-海洋-太空资源的整体重新组织。

▶ **代理 SaaS 估值锚被 Sierra 锚定 100x ARR**，将带来下半年同类公司（Decagon、Ada、Gleen 等）估值再涨；同时 Blitzy、Cursor 这类自治编码公司正与 GitHub/Microsoft/JetBrains 形成新对峙。

▶ **PE 对成长资本的入侵**：KKR (Reserv)、Blackstone (Anagram)、TCV (Corgi) 一周内三笔 1 亿美元级 deal，显示一级与二级、PE 与 VC 边界融合的趋势加剧；SpaceX、Anthropic 是这种"PE 化 VC"的极致版本。

---

# 第三部分：中国一级市场 Top 10

## 1. Moonshot AI ($2B / >$20B)

▶ **公司简介与商业模式**：Moonshot AI 由清华叉院杨植麟 (前 Meta AI、Google Brain) 于 2023 年创办，核心产品是开权重 Kimi 系列 LLM 与对应 Kimi 智能助手；商业模式包括 To-C 订阅 (Kimi+/Kimi 探索版)、To-B API、海外 OpenRouter 分发与企业私有化部署。

▶ **本周事件**：5 月 7 日 Moonshot AI 宣布完成 20 亿美元融资，估值超过 200 亿美元，由美团旗下 Long-Z Investments 领投，清华系资本、中国移动、CPE 源峰跟投；半年内累计募资 39 亿美元，估值从 2025 年底的 43 亿美元跃升至 200 亿美元；4 月 ARR 突破 2 亿美元；最新模型 Kimi K2.6 在 OpenRouter 平台用量稳居全球第二。([TechCrunch](https://techcrunch.com/2026/05/07/chinas-moonshot-ai-raises-2b-at-20b-valuation-as-demand-for-open-source-ai-skyrockets/), [TechNode](https://technode.com/2026/05/07/kimi-reportedly-nears-2-billion-funding-round-at-over-20-billion-valuation/), [SiliconANGLE](https://siliconangle.com/2026/05/07/open-source-ai-developer-moonshot-ai-raises-2b-20b-valuation/))

▶ **一级市场投资意义**：Moonshot 与 DeepSeek 之后，中国大模型已形成"开源开权重 + 国产算力 + 海外分发"的全球可定价模型；美团领投反映互联网大厂从被动布局转为主动收购式控盘，"AI 六小龙"格局事实上重组为"DeepSeek + Moonshot + 阿里 Qwen + 字节豆包"四强，其余智谱、百川、MiniMax、零一被边缘化；Moonshot 估值锚定将托起 6 月份后整个国内 LLM 公司新一轮融资定价，并刺激港股 18C/科创板 LLM 上市潮。([TechCrunch](https://techcrunch.com/2026/05/07/chinas-moonshot-ai-raises-2b-at-20b-valuation-as-demand-for-open-source-ai-skyrockets/))

## 2. DeepSeek (Tencent / Big Fund $4B 在谈)

▶ **公司简介与商业模式**：DeepSeek 是杭州幻方系孵化的开源大模型实验室，凭 V3/R1 系列在低成本推理与代码/数学上对标海外前沿；商业模式以 To-B API、私有化部署 + 开源社区影响力变现为主，To-C 流量入口为 deepseek.com 与 App Store 应用。

▶ **本周事件**：5 月初消息陆续披露：腾讯提议占股不超过 20%，但被 DeepSeek 拒绝；阿里因生态契合度低退出谈判；目前 Big Fund 与腾讯主谈 4 亿美元起步、估值在 200 亿–500 亿美元区间浮动，5 月 9 日最新版本回落至 5 亿美元 / 估值 3,000 亿元人民币。([TFN](https://techfundingnews.com/tencent-to-back-deepseek-in-4b-round-at-50b-valuation-marking-first-external-funding-report/), [Gate News](https://www.gate.com/news/detail/deepseek-fails-to-reach-financing-terms-with-alibaba-tencent-proposes-up-to-20948543))

▶ **一级市场投资意义**：DeepSeek 是中国唯一一个未真正接受外部融资且已在全球用户量与开发者影响力上对标 OpenAI / Anthropic 的 AI 公司，本轮一旦落地 (无论是 4 亿还是 40 亿美元) 都将定义"准国家级 AI 资产"的估值方法论；股权占比谈判反映中国 AI 在战略主权与商业化之间的拉锯，Big Fund 的入局将推动"国家队 + 互联网大厂 + 老股东"三角格局成为后续大模型轮的新模板。([TFN](https://techfundingnews.com/tencent-to-back-deepseek-in-4b-round-at-50b-valuation-marking-first-external-funding-report/))

## 3. Kunlunxin (百度昆仑芯) STAR + HK IPO 启动

▶ **公司简介与商业模式**：百度昆仑芯是百度 2018 年内部孵化、2021 年独立的 AI 芯片公司，代表产品 R200/R300 通用 AI 加速器（兼推理与训练），主要服务百度搜索 + 文心一言 + 智能云，外部客户包括运营商、金融与互联网厂商。

▶ **本周事件**：5 月 8 日 SCMP / TrendForce 披露百度已正式向上交所提交昆仑芯科创板 IPO 材料，并同步启动港股 18C 双重上市，港股估值起步 ≥1,000 亿元人民币（约 147 亿美元），JPMorgan 内部估值则给出 400 亿–490 亿美元区间；2024 年营收约 20 亿元、2025 年预计 35 亿元 + 实现盈亏平衡。([SCMP](https://www.scmp.com/tech/tech-trends/article/3352891/baidu-chip-unit-kunlunxin-eyes-us146b-valuation-hong-kong-ipo-sources), [TrendForce](https://www.trendforce.com/news/2026/05/08/news-baidu-chip-unit-kunlunxin-reportedly-launches-star-market-ipo-process-hk-listing-valuation-seen-near-hk100b/))

▶ **一级市场投资意义**：在华为昇腾、寒武纪之外，昆仑芯 IPO 将提供国内第三个"千亿元级国产 GPU 替代品"流动性出口，与 Lightelligence (光子计算) 4 月底港股首日 +383%、估值 100 亿美元的强势演绎形成共振，并将打开"互联网大厂分拆芯片业务上市"模板（如阿里平头哥、字节 Iota、腾讯蓬莱实验室），使中国 AI 算力栈在资本市场的估值空间显著抬升。([Nikkei](https://asia.nikkei.com/business/china-tech/baidu-s-spun-off-chip-unit-plans-dual-listing-in-shanghai-and-hong-kong))

## 4. CATL — $5B HK 配售完成 + 5/6 创新高

▶ **公司简介与商业模式**：CATL (宁德时代) 是全球最大动力电池厂商，业务覆盖三元/磷酸铁锂/钠离子/凝聚态电池、储能系统、电池回收、滑板底盘 (CIIC)、换电服务 (EVOGO)；客户包括特斯拉、宝马、大众、福特、Stellantis、上汽、蔚来、理想、华为问界等。

▶ **本周事件**：4 月 30 日 CATL 完成 392 亿港元 (50 亿美元) H 股配售，按 628.20 港元定价、超额认购，是 2026 港股最大单笔股权融资；5 月 6 日 A 股冲至 460 元创历史新高，全国 5 月锂电池排产 249 GWh 创单月纪录；近期还拿下 HyperStrong 60 GWh 全球最大钠电订单。([CnEVPost](https://cnevpost.com/2026/04/30/catl-completes-hong-kong-share-placement/), [Nikkei](https://asia.nikkei.com/business/markets/equities/chinese-ev-battery-maker-catl-raises-5bn-in-hong-kong), [CnEVPost 5/6](https://cnevpost.com/2026/05/06/catl-shares-record-high-strong-may-battery-production-outlook/))

▶ **一级市场投资意义**：CATL 单家 50 亿美元 HK 配售再次确立香港市场"中国硬科技 + 全球资本"主桥头堡地位，意味着南向 + 中东主权基金对中国新能源龙头的配置仍在加码；钠电 60 GWh 订单则把储能商业化拐点提前到 2026–2027，刺激钠电池上下游 (中科海钠、华阳股份、维科技术、传艺科技) 的一级市场估值再上台阶；CATL "电池金融化"路径 (港股配售 + 海外建厂 + 储能 PPA) 也将被中创新航、亿纬锂能、欣旺达模仿。([CnEVPost](https://cnevpost.com/2026/05/06/catl-shares-record-high-strong-may-battery-production-outlook/))

## 5. Xiaomi SU7 改款 + YU7 GT (5/7 北京车展节奏)

▶ **公司简介与商业模式**：小米汽车 (Xiaomi EV) 是雷军主导、整合 IoT 生态的智能电动车业务，主销车型 SU7 (中大型轿车)、YU7 (中型 SUV)、YU7 GT (高性能 SUV)；商业模式以高性价比硬件 + HyperOS 软件 + 米家 IoT 生态绑定，并通过自有渠道和小米线下零售网络销售。

▶ **本周事件**：5 月 7 日 SU7 改款现身北京车展，三款车型起售 21.99 万元、最长续航 902 km、800V 架构、NVIDIA Thor + LiDAR 全系标配；改款上市 48 天斩获 8 万订单、4 月单月交付 3 万 +；高性能 YU7 GT 计划 5 月底发布，990 hp、300 km/h、Brembo 碳陶刹车。([PaulTan](https://paultan.org/2026/05/07/2026-xiaomi-su7-in-beijing/), [CarNewsChina YU7 GT](https://carnewschina.com/2026/05/04/xiaomi-yu7-gt-crossovers-with-990-hp-piling-up-at-the-factory-ahead-of-launch/), [CarNewsChina 订单](https://carnewschina.com/2026/05/06/xiaomi-su7-hits-80000-orders-in-48-days-april-deliveries-exceed-30000-units/))

▶ **一级市场投资意义**：小米将 NVIDIA Thor + LiDAR 下放到 22 万元价格带，等于"硬件军备竞赛"再升级，倒逼蔚小理、华为问界、阿维塔等同档对手提速；YU7 GT 990 hp 的产品定义与保时捷 Macan EV、Model Y Performance 直接对标，将带动一级市场对国产高性能电动车产业链 (碳化硅、空气悬架、碳陶刹车、800V 高压插件、AI 芯片) 持续加配；同时 Xiaomi 自建二期工厂 30 GWh 电池线为电池产业链一级市场公司带来新订单变量。([PaulTan](https://paultan.org/2026/05/07/2026-xiaomi-su7-in-beijing/))

## 6. LDROBOT (乐动机器人) HK IPO ($128M / $1.3B, 5/11 上市)

▶ **公司简介与商业模式**：LDROBOT (深圳乐动机器人) 是视觉 AI 机器人模组公司，主打消费级与商用清洁/服务机器人定位、感知 (LiDAR + VSLAM) 解决方案；客户包括家用扫地机器人厂商、服务机器人厂商等。

▶ **本周事件**：港股招股已完成定价，预计 5 月 11 日挂牌，募资 1.28 亿美元、估值 13 亿美元；本周路演与基石名单陆续公布。([Caproasia](https://www.caproasia.com/2026/05/01/china-intelligent-robot-visual-technology-company-shenzhen-ldrobot-ledong-robotics-hong-kong-ipo-to-raise-128-million-at-1-3-billion-valuation-with-expected-ipo-listing-on-11th-may-2026-founded-i/))

▶ **一级市场投资意义**：LDROBOT 是 4 月 Lightelligence、5 月 11 日 LDROBOT 之后，香港"AI + 硬件 IPO 流水线"再添一例，验证 18C 通道对未盈利但具有产业链卡位优势的硬件 AI 公司的接纳力；其上市将带动云鲸、追觅、九号、石头、科沃斯等扫地机/服务机器人产业链估值上修，并为感知模块 (奥比中光、海康机器人) 的一级市场后续融资提供锚定参考。([Caproasia](https://www.caproasia.com/2026/05/01/china-intelligent-robot-visual-technology-company-shenzhen-ldrobot-ledong-robotics-hong-kong-ipo-to-raise-128-million-at-1-3-billion-valuation-with-expected-ipo-listing-on-11th-may-2026-founded-i/))

## 7. WeRide × Lenovo 200,000 辆 5 年 Robotaxi 协议

▶ **公司简介与商业模式**：WeRide (文远知行) 是广州 + 美国双总部的 L4 自动驾驶公司，业务覆盖 Robotaxi、Robobus、自动清扫车、自动小巴；商业模式包括"自营运营 + 与 OEM/Tier1 合作 + 软件 License"。

▶ **本周事件**：本周 WeRide 与联想宣布扩展战略合作，未来 5 年内全球部署约 20 万辆自动驾驶车辆 (Robotaxi、Robobus、清扫车)，核心是基于 HPC 3.0 高性能计算平台 — 该平台将自动驾驶套件成本降低 50%、TCO 降低 84%，并支持 WeRide GXR (Robotaxi)、Robosweeper 等多款车型量产。([Automotive World](https://www.automotiveworld.com/news/weride-lenovo-deal-expands-beyond-robotaxi-rollout/), [SCMP](https://www.scmp.com/tech/tech-trends/article/3351581/chinese-robotaxi-firms-accelerate-global-roll-outs-cost-edge-drives-expansion))

▶ **一级市场投资意义**：联想这种"标准 PC 厂"切入自动驾驶基础设施，意味着 Robotaxi 套件正在被 commodity 化，单车成本下降速度远快于此前预期，将快速摧毁海外同行 (Waymo、Cruise、Zoox) 的成本护城河；20 万辆部署目标若兑现一半，将在中东、东南亚、欧洲市场为中国 Robotaxi 系统供应商 (禾赛激光雷达、地平线/英伟达 Orin/Thor、华为 ADS) 创造长达 5 年的可持续订单流，是 2026 下半年自动驾驶硬件 + 软件赛道一级市场加注的关键背书。([SCMP](https://www.scmp.com/tech/tech-trends/article/3351581/chinese-robotaxi-firms-accelerate-global-roll-outs-cost-edge-drives-expansion))

## 8. Pony.ai 第七代 Robotaxi BOM <23 万 + Q1 业绩定档 5/26

▶ **公司简介与商业模式**：Pony.ai (小马智行) 是 Nasdaq + HK 双重上市的 L4 自动驾驶头部公司，业务包括 Robotaxi、Robotruck (大马智卡)、L2/L3 量产方案 (与北汽、广汽合作)；2024 年 11 月 Nasdaq IPO 募资 4.13 亿美元、2025 年 11 月再港股 IPO 67 亿港元。

▶ **本周事件**：5 月 6 日 Pony.ai 公告将于 5 月 26 日发布 2026 Q1 业绩；CEO 彭军近日披露第七代 Robotaxi 整车 BOM 已下沉到 23 万元以下，比 Tesla Model 3 还低；PonyWorld 自动驾驶系统从强化学习升级到"自主决策"框架，车辆可自评驾驶质量。([GlobeNewswire](https://www.globenewswire.com/news-release/2026/05/06/3288550/0/en/PONY-AI-Inc-to-Report-First-Quarter-2026-Financial-Results-on-May-26-2026.html), [CNA](https://www.channelnewsasia.com/east-asia/ponyai-robotaxi-artificial-intelligence-auto-china-6099966))

▶ **一级市场投资意义**：第七代 BOM 23 万元意味着 Robotaxi 单车 5 年回本周期可缩短到 1.5–2 年，单台车毛利模型对一级市场未上市的同行 (元戎启行、Momenta、轻舟智航、新石器) 形成强压力，融资估值将向"按落地车辆数量"而非"技术叙事"重新锚定；同时 PonyWorld 朝端到端世界模型靠拢，与特斯拉 FSD V14、Momenta R7 形成"端到端世界模型"三足鼎立格局，是 VC 重估自动驾驶大模型基础设施 (合成数据、世界模型训练) 的重要催化。([GlobeNewswire](https://www.globenewswire.com/news-release/2026/05/06/3288550/0/en/PONY-AI-Inc-to-Report-First-Quarter-2026-Financial-Results-on-May-26-2026.html))

## 9. 华虹 / 华力 7nm 推进 + 美国设备出口管制再升级

▶ **公司简介与商业模式**：华虹集团 (Hua Hong) 是中国第二大晶圆代工厂，主力工艺为 28/22nm 及以下成熟节点，子公司华力 (HLMC) 上海 12 寸厂正在攻关 7nm；客户涵盖 IoT、汽车电子、特色工艺与部分 AI 芯片。

▶ **本周事件**：4 月底至 5 月初 Reuters / TrendForce 等独家披露美国商务部要求 Lam Research、Applied Materials、KLA 暂停部分对华虹 / 华力的设备出货，目标是延缓其上海 7nm 试产 (年底数千片/月)；华为已计划将部分 AI 芯片产能从中芯国际转移到华虹。([Yahoo / Reuters](https://finance.yahoo.com/sectors/technology/articles/exclusive-us-orders-multiple-chip-equipment-companies-halt-175356047.html), [TrendForce](https://www.trendforce.com/news/2026/04/29/news-u-s-reportedly-moves-to-block-chip-tool-shipments-to-china-no-2-foundry-hua-hong-as-it-seeks-7nm-after-smic/), [Tom's Hardware](https://www.tomshardware.com/tech-industry/us-stops-exports-of-chip-making-tools-to-chinas-number-two-chip-maker-hua-hong-and-huali-microelectronics-reportedly-on-the-cusp-of-starting-a-7-nm-fab-in-shanghai))

▶ **一级市场投资意义**：管制升级直接利好国产半导体设备股 (北方华创、中微公司、拓荆、华海清科、芯源微、盛美) 与零部件公司 (新莱、富创、昌红、英杰电气) 在一级市场的非公开融资估值；同时驱动半导体材料国产化二轮替代 (光刻胶、CMP 抛光液、光掩模、特气) 的并购整合机会增加；中长期看，华虹/华力一旦突破 7nm，将打开科创板"先进制程纯代工厂"再融资窗口，影响 SMIC + 华虹 + 华力的资本结构再平衡。([Yahoo / Reuters](https://finance.yahoo.com/sectors/technology/articles/exclusive-us-orders-multiple-chip-equipment-companies-halt-175356047.html))

## 10. 具身智能持续放量：Galbot / Galaxea / Unitree / 国家 AI 基金三期

▶ **公司简介与商业模式**：Galbot (银河通用) 主攻通用人形机器人 + 大模型 VLA；Galaxea AI (星动纪元) 做工业级人形与轮式具身机器人；Unitree (宇树) 是消费级与工业级四足/人形机器人头部厂商。

▶ **本周事件**：3 月 Galbot 完成 25 亿元人民币融资 (3.62 亿美元)，由国家 AI 产业投资基金三期领投，中石化、中信、中行、上汽参投；4 月 Galaxea AI 完成 20 亿元人民币 (2.91 亿美元) 融资，估值突破 200 亿元；Unitree 已申报科创板 IPO，募资 42.02 亿元；2026 年至今中国机器人行业累计融资 613 亿元、其中人形 259 亿元；本周 LDROBOT 港股挂牌进一步巩固赛道热度。([Caixin Galbot](https://www.caixinglobal.com/2026-03-03/galbot-raises-362-million-in-fresh-funding-eyes-hong-kong-ipo-102418742.html), [Caixin Galaxea](https://www.caixinglobal.com/2026-04-02/robot-startup-galaxea-ai-raises-291-million-102430297.html), [NewsGlobeNow](https://www.newsglobenow.com/new337440.html))

▶ **一级市场投资意义**：国家 AI 基金三期首次入股具身智能 (Galbot)，等同对赛道作"国家战略背书"，相当于 2014 年 Big Fund 一期入股 SMIC 之于半导体；这将引导地方政府基金、国资 LP、央企产业基金加速涌入，2026 下半年人形机器人赛道有望累计融资突破 1,000 亿元，并推动 Unitree、AgiBot、Galbot 进入"科创板/港股 IPO 双轨"赛道；同时减速器 (绿的、双环)、力觉传感 (柯力、坤维)、电机 (步科、汇川) 等核心零部件供应商将出现新一批一级市场独角兽。([CnTechPost](https://cntechpost.com/2026/03/02/galbot-secures-major-state-backing/))

## 中国全周趋势总结

▶ **AI + 算力 + 芯片三位一体**：Moonshot 20 亿美元、DeepSeek 进入实质融资谈判、昆仑芯 IPO 启动 + 上月 Lightelligence 港股暴涨，国内"开源大模型 + 国产算力 + 中外资本"三角结构正式定型，估值锚由 200 亿美元 (Moonshot)、≥147 亿美元 (昆仑芯) 双向支撑。

▶ **港股 18C / 科创板"双引擎" IPO 通道高度活跃**：CATL HK 配售 50 亿美元、LDROBOT 5/11 挂牌、昆仑芯启动 STAR + HK 双重上市、Unitree STAR 申报中，Hong Kong 全年 IPO 预计达 200 家、募资逾 3,860 亿港元，中国硬科技 IPO 进入 2021 年以来最强窗口。([China Daily Asia](https://www.chinadailyasia.com/article/626370))

▶ **"国家队 + 互联网大厂"双轮成 LP 主力**：国家 AI 基金三期 (Galbot)、Big Fund 三期 (DeepSeek 谈判)、美团 Long-Z (Moonshot)、腾讯 (DeepSeek)、阿里 (Qwen 自营)，本周再次验证此结构是中国 AI、芯片、机器人融资的主流模板。

▶ **新能源车与具身智能双双进入"成本下沉 → 全球出海"主升浪**：CATL 钠电 60 GWh、Xiaomi SU7 BOM 全系标配 LiDAR + Thor、Pony.ai 第七代 23 万元 BOM、WeRide-Lenovo 5 年 20 万辆部署，中国硬件创新由"概念阶段"切换到"成本-规模阶段"，是未来 5 年全球供应链最强变量。

▶ **管制驱动国产替代再加码**：美国对华虹 / 华力新一轮设备出口管制将再度催化半导体设备、材料、零部件、EDA、IP 核国产替代赛道的一级市场再融资和并购整合机会，类似 2019 年实体清单后的"硬科技小高潮 2.0"。

---

*报告完毕，下周同时间发布。*
