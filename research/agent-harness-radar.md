# Agent Harness Technology Radar

> 本雷达聚焦 AI Coding Agent 领域的工具、框架、技术与平台，助你快速评估技术选型。
> 数据基准：2026年5月 | 覆盖范围：CLI Agents / IDE Extensions / Harness Frameworks / Orchestration Patterns / Infrastructure

---

## 图例

- **ADOPT** (采纳): 成熟稳定，广泛验证，可放心用于生产
- **TRIAL** (试验): 值得积极探索，有成熟案例但需评估适用性
- **ASSESS** (评估): 值得关注，持续跟进，不急于投入
- **HOLD** (暂缓): 谨慎使用或暂时跳过

---

## 一、技术 Techniques

### ADOPT

**ReAct (Reasoning + Acting) 模式**
- **做什么**: 将 LLM 的"思考"与"行动"循环结合，通过 Tool Call 实现与环境交互的迭代推理
- **为何重要**: Agent 系统的核心执行范式，所有主流工具(Cursor, Claude Code, Aider)均内置支持
- **采用率**: ~95% 的编码 Agent 使用
- **环**: ADOPT

**Chain-of-Thought (CoT) 提示工程**
- **做什么**: 引导模型显式生成中间推理步骤，提升复杂任务的准确率和可解释性
- **为何重要**: 从简单补全进化为多步推理的关键技术，直接影响 Agent 的可靠性
- **采用率**: 几乎所有推理型 Agent 均内置
- **环**: ADOPT

**上下文工程 (Context Engineering)**
- **做什么**: 通过分层策略管理 Agent 的上下文输入（文件级/路径级/符号级规则）
- **为何重要**: 上下文窗口是稀缺资源，精细化管理直接决定 Agent 的任务完成质量
- **采用率**: 高（Cohere 3 的成功验证了"压缩即智能"）
- **环**: ADOPT

---

### TRIAL

**Spec-Driven Development (SDD)**
- **做什么**: 将规格文档（Spec）作为可执行的首要输入，通过"宪法约束→功能规格→实现计划→任务清单→测试先行→验收检查"六步流程驱动 AI 生成
- **为何重要**: 解决 Vibe Coding 质量不可控的核心痛点，使 AI 生成代码真正对齐业务意图
- **采用率**: 阿里内部已实践（5人7天完成20人数周工作量），网易 CodeWave 已公开分享
- **环**: TRIAL

**多 Agent 编排模式 (Multi-Agent Orchestration)**
- **做什么**: 在单一任务中协调多个专业 Agent 协作（主从模式/流水线模式/竞争模式）
- **为何重要**: Claude Code 的 Subagents、Cursor 3.0 的 8 个并行 Agent 证明了多 Agent 的价值
- **采用率**: 快速增长，2026年主流工具均已支持
- **环**: TRIAL

**Harness Engineering (Agent Harness)**
- **做什么**: 将 LLM 外部的基础设施系统化：编排循环、工具、记忆、上下文管理、状态持久化、错误处理、Guardrails
- **为何重要**: "Agent = Model + Harness"，真正决定系统上限的不是模型而是 Harness
- **采用率**: 各公司均在构建（Anthropic SDK、OpenAI Swarm/LlamaIndex 竞品）
- **环**: TRIAL

**分层上下文工程 (Layered Context)**
- **做什么**: 5层上下文管理：项目级指令文件（CLAUDE.md）、路径匹配规则、符号索引（Repo Map/tree-sitter）、语义检索、实时对话
- **为何重要**: Claude Code 的 CLAUDE.md、Cursor 的 .cursor/rules、Aider 的 Repo Map 代表了最佳实践
- **采用率**: 主流工具均已采纳
- **环**: TRIAL

---

### ASSESS

**Agentic RAG**
- **做什么**: 在传统 RAG 基础上引入 Agent 机制，使检索与生成过程更具自主性和多轮决策能力
- **为何重要**: 将知识库从被动响应升级为主动推理，RAGFlow 0.23.0 已集成 Memory 能力
- **采用率**: 企业级场景开始落地
- **环**: ASSESS

**分层规划 (Hierarchical Planning)**
- **做什么**: 将复杂任务分解为层级子任务（Agent 2.0 的显式规划能力）
- **为何重要**: 解决单 Agent 的"概率陷阱"和"缺乏全局视角"问题
- **采用率**: 新兴，Agent 2.0 架构的核心特征
- **环**: ASSESS

**反射与自评 (Reflection & Self-Evaluation)**
- **做什么**: Agent 在执行后主动反思输出质量、评估偏差并自我纠错
- **为何重要**: 从"一次做对"到"持续优化"，提升长周期任务的可靠性
- **采用率**: 早期探索
- **环**: ASSESS

**持久化记忆与状态 (Persistent Memory & State)**
- **做什么**: 跨会话保持项目上下文、Agent 状态和用户偏好
- **为何重要**: Claude Code 的会话持久化、Windsurf 的 Memory 功能是这一方向的代表
- **采用率**: 快速增长
- **环**: ASSESS

**EARS 需求结构化语法**
- **做什么**: 轻量级需求标准化语法，将自然语言需求转换为机器可理解的结构化文档
- **为何重要**: SDD 的关键前置步骤，网易 CodeWave 已在企业场景验证
- **采用率**: 早期
- **环**: ASSESS

---

## 二、工具 Tools (Agent Coding Platforms)

### ADOPT

**Claude Code (Anthropic)**
- **做什么**: 终端原生 CLI Agent，基于 Claude 的深度推理能力，支持文件读写、命令执行、Git 操作、调试、重构、多 Subagent 协作
- **为何重要**: 被公认为终端最强编码助手，2026年向 GitHub 公开项目周提交量增长 25 倍（从 10 万到 250 万次）
- **采用率**: 极高，尤其在后端/系统级开发场景
- **环**: ADOPT

**GitHub Copilot (Microsoft/OpenAI)**
- **做什么**: IDE 内嵌的代码补全和生成工具，支持多种语言和框架，企业级安全合规
- **为何重要**: 企业级市场的标准选择，Copilot Enterprise 订阅用户现已可直接调用 Claude 和 Codex
- **采用率**: 企业市场最高（95%+ 开发者使用率）
- **环**: ADOPT

**Cursor**
- **做什么**: AI 原生代码编辑器（基于 VS Code），支持全项目感知、多模型集成、多 Agent 协作（Cursor 2.0/3.0）
- **为何重要**: 年化收入突破 20 亿美元，估值超 500 亿美元，2026年3.0版本支持 8 个 Agent 并行，Composer 自研模型
- **采用率**: 前端/全栈开发者首选
- **环**: ADOPT

---

### TRIAL

**Windsurf (Cascade AI)**
- **做什么**: 基于 VS Code 分支的 AI 编程工具，Cascade 功能重新定义人机协作边界，Wave 13 引入 SWE-1.5 模型
- **为何重要**: 2025年7月被 Cognition AI（Devin 开发商）收购，技术路线与 Claude Code 深度融合
- **采用率**: 快速增长但已被 Cognition 整合
- **环**: TRIAL

**Amazon Q Developer**
- **做什么**: AWS 原生 AI 编程助手，基于 Claude Sonnet 3.7，提供 IDE 插件和 CLI 工具，Rust 实现的状态机 Agent 循环
- **为何重要**: 企业级 AWS 场景的首选，深度集成 AWS 服务，未来升级为 Kiro
- **采用率**: AWS 企业用户中高
- **环**: TRIAL

**Aider**
- **做什么**: 开源 CLI 编码 Agent，支持 75+ 模型（Claude/GPT/Gemini/本地模型），tree-sitter 符号图构建，Git 集成
- **为何重要**: 开源社区最活跃的 CLI Agent 之一，9.5 万 Star 的 OpenCode 受其符号索引方案启发
- **采用率**: 开源社区高，技术用户首选
- **环**: TRIAL

**OpenCode**
- **做什么**: 微软研究院推出的开源编码 Agent，原生终端界面、多会话支持，兼容 75+ 模型
- **为何重要**: 2026年2月快速崛起至 12.4 万 Star，支持 VS Code 扩展和桌面应用
- **采用率**: 快速增长
- **环**: TRIAL

**Goose**
- **做什么**: 开源可扩展 AI Agent CLI，支持安装、执行、编辑、测试与任意 LLM 集成
- **为何重要**: 2025年获得大量关注，支持 SSE 实时响应扩展，适合需要深度定制的场景
- **采用率**: 开发者社区活跃
- **环**: TRIAL

**Cody (Sourcegraph)**
- **做什么**: 基于代码图谱的 AI 编程助手，理解整个代码库的语义关系
- **为何重要**: 与代码搜索引擎深度集成，适合大型代码库场景
- **采用率**: 中等
- **环**: TRIAL

**Gemini CLI (Google)**
- **做什么**: Google 官方的命令行 AI 工作流工具，深度融入开发者日常，支持多模态交互
- **为何重要**: Google 官方的 AI Coding 入口，已开源并获得 9000+ Star
- **采用率**: 增长中
- **环**: TRIAL

---

### ASSESS

**Devin (Cognition AI)**
- **做什么**: AI 软件工程师，能自主完成端到端软件工程任务（2024年引发广泛讨论）
- **为何重要**: SWE-bench 的标杆，引爆了 AI Coding Agent 赛道，2025年收购 Windsurf
- **采用率**: 商业产品，公开案例有限
- **环**: ASSESS

**SWE-agent (Princeton NLP)**
- **做什么**: 开源 AI 编码 Agent，在 SWE-bench 上实现 12.29% 准确率，开源代码库 Issue 修复
- **为何重要**: 学术界的代表实现，SWE-bench 的标准 Baseline
- **采用率**: 研究用途为主
- **环**: ASSESS

**Trae Agent (ByteDance)**
- **做什么**: 字节跳动开源的 AI Coding Agent
- **为何重要**: 国内大厂的首个开源 CLI Agent 项目
- **采用率**: 国内社区
- **环**: ASSESS

**Kiro**
- **做什么**: Amazon Q Developer 的后继者，2026年发布的下一代 AI Coding Agent
- **为何重要**: 代表了 AWS 在 AI Coding 领域的技术演进方向
- **采用率**: 早期
- **环**: ASSESS

**Codex (OpenAI)**
- **做什么**: OpenAI 的官方编程 Agent，"OpenAI 版 Claude Code"，2025年开发者大会正式发布
- **为何重要**: 集成了 OpenAI 的深度推理模型和企业级能力
- **采用率**: 增长中
- **环**: ASSESS

**Cline**
- **做什么**: VS Code 扩展的 AI 编程 Agent，支持多模型和自定义工具
- **为何重要**: 开源社区高度活跃，开发者偏好定制化场景
- **采用率**: 中等
- **环**: ASSESS

---

## 三、平台 Platforms (Infrastructure & Orchestration)

### ADOPT

**MCP (Model Context Protocol)**
- **做什么**: Anthropic 推出的开放协议，标准化 AI 模型与外部数据源、工具的交互接口，被比喻为"AI 领域的 USB-C"
- **为何重要**: 2025年4月爆发式增长，OpenAI、Microsoft、Google、阿里、腾讯、字节跳动纷纷宣布接入，成为事实标准
- **采用率**: 极高（各主要厂商均已支持）
- **环**: ADOPT

---

### TRIAL

**LangGraph**
- **做什么**: 基于图结构的有状态多 Agent 编排框架，支持循环和非循环流程，可视化任务与 Agent 交互
- **为何重要**: LangChain 团队出品，精细控制能力最强，适合复杂多步骤工作流
- **采用率**: 高（45k+ GitHub Stars）
- **环**: TRIAL

**CrewAI**
- **做什么**: 基于角色协作的 Agent 编排框架，通过 Role/Task/Crew 概念模拟人类团队协作
- **为何重要**: 上手最快，45k Stars，2026年框架大战中的"快速启动"首选
- **采用率**: 高
- **环**: TRIAL

**OpenAI Agents SDK**
- **做什么**: OpenAI 的轻量级多 Agent 工作流框架（Swarm 的进化版），3个核心概念（Agent/Runner/Tool），内置 Guardrails 和 Tracing
- **为何重要**: 大厂背书，支持 MCP 协议，原生沙箱环境保障代码安全执行
- **采用率**: 快速增长
- **环**: TRIAL

**Dify**
- **做什么**: 开源的低代码 AI 应用平台，支持 RAG、Agent、工作流编排，Apache 2.0 许可
- **为何重要**: 企业级 AI Agent 落地的重要工具，2025年被称为"AI Agent 元年"的关键基础设施
- **采用率**: 企业级高，尤其在国内市场
- **环**: TRIAL

---

### ASSESS

**A2A (Agent-to-Agent Protocol)**
- **做什么**: Microsoft 推出的 Agent 间通信协议，与 MCP 互补，实现多 Agent 间的互操作性
- **为何重要**: "MCP 统一度量衡，A2A 实现 Agent 互联"，微软 Azure AI 的核心战略
- **采用率**: 早期，大厂支持
- **环**: ASSESS

**AutoGen / AG2 (Microsoft)**
- **做什么**: Microsoft 的多 Agent 对话框架，支持 Agent 间协作和自动优化
- **为何重要**: 微软 AI Agent 战略的核心组件，2026年改名 AG2
- **采用率**: 中等
- **环**: ASSESS

**LlamaIndex**
- **做什么**: 数据框架，专注于数据索引、检索增强（RAG）、Agent 记忆管理
- **为何重要**: RAG 和知识管理场景的核心框架，与 LangGraph 深度集成
- **采用率**: 高
- **环**: ASSESS

**Semantic Kernel (Microsoft)**
- **做什么**: 轻量级 SDK，将 AI 集成到企业应用，支持多语言，安全性与合规性内置
- **为何重要**: 微软企业 AI 战略的另一支柱，与 Azure 服务深度绑定
- **采用率**: 企业级
- **环**: ASSESS

**LangFlow**
- **做什么**: LangChain 的可视化低代码平台，基于图的工作流设计
- **为何重要**: 与 Dify 形成互补，技术导向的可视化编排
- **采用率**: 中等
- **环**: ASSESS

**Flowise**
- **做什么**: 基于 LangChain 的可视化低代码应用构建平台
- **为何重要**: 低门槛快速原型，与 LangFlow 路线相似
- **采用率**: 中等
- **环**: ASSESS

**RAGFlow**
- **做什么**: 开源的 RAG 引擎，v0.23.0 新增 Memory、Agent 能力，支持父子分块策略
- **为何重要**: 企业级知识管理的重要选择，文档处理流水线成熟
- **采用率**: 企业级知识管理场景
- **环**: ASSESS

**MetaGPT**
- **做什么**: 多 Agent 协作框架，通过模拟软件开发团队的角色分工（SDE/PM/Architect）协同工作
- **为何重要**: 独特的多角色模拟方法论，适合复杂软件工程任务
- **采用率**: 中等
- **环**: ASSESS

**OmAgent**
- **做什么**: 以设备为中心的多模态 Agent 框架
- **为何重要**: 差异化定位，面向多模态和设备场景
- **采用率**: 早期
- **环**: ASSESS

---

### HOLD

**纯 LangChain 应用（无 LangGraph）**
- **做什么**: 直接使用 LangChain 的链式抽象而非图结构
- **为何重要**: LangChain 本身存在过度抽象和稳定性问题（2024年"丑闻"），推荐使用 LangGraph 替代
- **采用率**: 下降中
- **环**: HOLD

---

## 四、框架与语言 Frameworks & Languages

### ADOPT

**Python**
- **做什么**: AI Agent 开发的第一语言，几乎所有框架均提供 Python SDK
- **为何重要**: 生态最成熟，LangGraph/CrewAI/AutoGen/LlamaIndex 均为 Python-first
- **采用率**: ~90% 的 Agent Harness 项目
- **环**: ADOPT

**TypeScript / JavaScript**
- **做什么**: Claude Code 核心实现语言，Node.js 生态下的 Agent SDK 开发
- **为何重要**: Claude Code、Cursor（部分）以及大量 MCP Server 使用 TS
- **采用率**: 高（约 40% 的前端工具和 60% 的 MCP Server）
- **环**: ADOPT

---

### TRIAL

**Claude Agent SDK (Anthropic)**
- **做什么**: Anthropic 官方的 Agent 开发 SDK，"驱动 Claude Code 的脚手架"的具体实现
- **为何重要**: 直接对齐 Claude 模型能力，代表了官方推荐的 Harness 构建方式
- **采用率**: 快速增长
- **环**: TRIAL

**Rust**
- **做什么**: 高性能系统编程语言，Amazon Q Developer CLI 等关键工具使用
- **为何重要**: 性能敏感的基础设施（Agent 执行循环、沙箱）首选
- **采用率**: 增长中（CLI 工具和性能关键组件）
- **环**: TRIAL

**OpenAI Agents SDK (Python)**
- **做什么**: OpenAI 官方的 Python Agent 框架，内置 MCP 支持和沙箱执行
- **为何重要**: 大厂背书，2026年持续更新，适合 OpenAI 模型为主的场景
- **采用率**: 高
- **环**: TRIAL

**C# / .NET MCP SDK (Microsoft)**
- **做什么**: Microsoft 官方的 .NET 环境 MCP 服务器和客户端 SDK，1.0 版本已发布
- **为何重要**: .NET 企业场景的 MCP 支持，满足企业级安全合规需求
- **采用率**: 企业级 .NET 场景
- **环**: TRIAL

---

### ASSESS

**Go**
- **做什么**: 并发友好的语言，部分 Agent 工具开始采用
- **为何重要**: 高并发场景的潜力，但生态尚在成熟
- **采用率**: 有限
- **环**: ASSESS

---

## 趋势概览

### 高频词与核心方向 (2026)

1. **Harness > Model**: 业界共识——Agent 上限由 Harness 决定，非模型本身。Anthropic、OpenAI、LangChain 均在构建各自版本的脚手架。
2. **MCP 一统天下**: 从"战国时代"到统一协议，各厂商快速跟进，2025年4月是关键爆发点。
3. **多 Agent 从概念到标配**: Claude Code Subagents、Cursor 3.0 8路并行、Windsurf Cascade——多 Agent 协作已从实验变为标准功能。
4. **CLI Agent 崛起**: Claude Code 证明了终端 Agent 的工程能力优势，开源社区的 OpenCode、Aider、Goose 快速跟进。
5. **Spec-Driven 从概念到实践**: 阿里、网易的公开案例表明，SDD 在企业级场景已具备可操作性。
6. **LLM 自己优化 Harness**: 独立研究项目让 LLM 自己优化基础设施，达到 76.4% 的 SWE-bench 通过率，超越人工设计。

### 关键判断

- **IDE vs CLI**: Cursor 适合前端/全栈的沉浸式体验，Claude Code 适合后端/系统级工程的深度控制。
- **框架选择**: 快速上手选 CrewAI，精细控制选 LangGraph，多 Agent 探索选 AutoGen/AG2。
- **协议层**: MCP 是必选项，A2A 值得观望。
- **企业 vs 个人**: 企业级优先 GitHub Copilot / Amazon Q，个人/技术团队优先 Claude Code / Cursor / Aider / OpenCode。

---

*本雷达基于 2026年5月公开信息汇编，随着 MCP 生态快速成熟和各厂商加速迭代，部分评估可能在短期内发生变化。建议每季度复审一次。*