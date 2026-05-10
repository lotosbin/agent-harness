# Agent Harness Technology Radar

> 参考 [Thoughtworks Technology Radar](https://www.thoughtworks.com/radar) 格式，跟踪 AI Coding Agent 领域的工具、技术与框架动态。
>
> 数据基准：2026年5月 | 覆盖范围：上下文工程 / 提示词工程 / MCP工程 / Skill工程 / SubAgent工程 / Team工程 / 编排工程

---

## 图例

| 环 | 含义 | 说明 |
|----|------|------|
| **ADOPT** | 采纳 | 成熟稳定，广泛验证，可放心用于生产 |
| **TRIAL** | 试验 | 值得积极探索，有成熟案例但需评估适用性 |
| **ASSESS** | 评估 | 值得关注，持续跟进，不急于投入 |
| **HOLD** | 暂缓 | 谨慎使用或暂时跳过 |

---

## 雷达图概览

```
                    ADOPT
            ┌─────────────────────────────────────────┐
            │  ReAct/CoT    Claude Code               │
            │  上下文工程   GitHub Copilot             │
            │  MCP          Cursor                     │
            │  Python/TS                                   │
     TRIAL ─┼─────────────────────────────────────────┼─ TRIAL
            │  SDD          LangGraph                  │
            │  多Agent编排   CrewAI                    │
            │  Harness Eng  Claude Agent SDK           │
            │  分层上下文    OpenAI Agents SDK         │
            │  Aider        OpenCode                   │
            │  Windsurf     Gemini CLI                 │
            │               Goose                      │
     ASSESS ┼─────────────────────────────────────────┼─ ASSESS
            │  Agentic RAG  A2A                       │
            │  分层规划      AutoGen/AG2               │
            │  反射自评      LlamaIndex                │
            │  持久化记忆    Semantic Kernel           │
            │  EARS         MetaGPT                    │
            │  Trae Agent    Codex                     │
            │  Devin        SWE-agent                  │
            │  Kiro         RAGFlow                    │
            │  Cline        LangFlow                   │
            │               Flowise                    │
     HOLD  ─┼─────────────────────────────────────────┼─ HOLD
            │           纯 LangChain                   │
            └─────────────────────────────────────────┘
            Techniques    Tools         Platforms
```

> 左：Techniques（技术）| 右：Tools（工具）
> 上半圆外环：ADOPT | 上半圆内环：TRIAL
> 下半圆内环：ASSESS | 下半圆外环：HOLD

---

## 一、技术 Techniques

### ADOPT

**ReAct (Reasoning + Acting) 模式**
- 将 LLM 的"思考"与"行动"循环结合，通过 Tool Call 实现与环境交互的迭代推理
- ~95% 的编码 Agent 使用，Agent 系统的核心执行范式

**Chain-of-Thought (CoT) 提示工程**
- 引导模型显式生成中间推理步骤，提升复杂任务的准确率和可解释性
- 几乎所有推理型 Agent 均内置

**上下文工程 (Context Engineering)**
- 通过分层策略管理 Agent 的上下文输入（文件级/路径级/符号级规则）
- 上下文窗口是稀缺资源，精细化管理直接决定 Agent 的任务完成质量

### TRIAL

**Spec-Driven Development (SDD)**
- 将规格文档（Spec）作为可执行的首要输入，六步流程驱动 AI 生成
- 阿里内部已实践（5人7天完成20人数周工作量），网易 CodeWave 已公开分享

**多 Agent 编排模式 (Multi-Agent Orchestration)**
- 在单一任务中协调多个专业 Agent 协作（主从模式/流水线模式/竞争模式）
- Claude Code 的 Subagents、Cursor 3.0 的 8 个并行 Agent 证明了多 Agent 的价值

**Harness Engineering (Agent Harness)**
- 将 LLM 外部的基础设施系统化：编排循环、工具、记忆、上下文管理、状态持久化、错误处理、Guardrails
- "Agent = Model + Harness"，真正决定系统上限的不是模型而是 Harness

**分层上下文工程 (Layered Context)**
- 5层上下文管理：项目级指令文件（CLAUDE.md）、路径匹配规则、符号索引（Repo Map/tree-sitter）、语义检索、实时对话
- Claude Code 的 CLAUDE.md、Cursor 的 .cursor/rules、Aider 的 Repo Map 代表了最佳实践

### ASSESS

**Agentic RAG**
- 在传统 RAG 基础上引入 Agent 机制，使检索与生成过程更具自主性和多轮决策能力
- 将知识库从被动响应升级为主动推理

**分层规划 (Hierarchical Planning)**
- 将复杂任务分解为层级子任务
- 解决单 Agent 的"概率陷阱"和"缺乏全局视角"问题

**反射与自评 (Reflection & Self-Evaluation)**
- Agent 在执行后主动反思输出质量、评估偏差并自我纠错
- 从"一次做对"到"持续优化"，提升长周期任务的可靠性

**持久化记忆与状态 (Persistent Memory & State)**
- 跨会话保持项目上下文、Agent 状态和用户偏好
- Claude Code 的会话持久化、Windsurf 的 Memory 功能是这一方向的代表

**EARS 需求结构化语法**
- 轻量级需求标准化语法，将自然语言需求转换为机器可理解的结构化文档
- SDD 的关键前置步骤

---

## 二、工具 Tools (Agent Coding Platforms)

### ADOPT

**Claude Code (Anthropic)**
- 终端原生 CLI Agent，基于 Claude 的深度推理能力，支持文件读写、命令执行、Git 操作、调试、重构、多 Subagent 协作
- 2026年周提交量增长 25 倍（从 10 万到 250 万次），后端/系统级开发首选

**GitHub Copilot (Microsoft/OpenAI)**
- IDE 内嵌的代码补全和生成工具，支持多种语言和框架，企业级安全合规
- 企业市场使用率最高（95%+ 开发者）

**Cursor**
- AI 原生代码编辑器（基于 VS Code），支持全项目感知、多模型集成、多 Agent 协作
- 年化收入突破 20 亿美元，估值超 500 亿美元，3.0版本支持 8 个 Agent 并行

### TRIAL

**Windsurf (Cascade AI)**
- 基于 VS Code 分支的 AI 编程工具，Cascade 功能重新定义人机协作边界
- 2025年7月被 Cognition AI（Devin 开发商）收购

**Amazon Q Developer**
- AWS 原生 AI 编程助手，基于 Claude Sonnet 3.7，提供 IDE 插件和 CLI 工具，Rust 实现的状态机 Agent 循环
- 企业级 AWS 场景首选，未来升级为 Kiro

**Aider**
- 开源 CLI 编码 Agent，支持 75+ 模型（Claude/GPT/Gemini/本地模型），tree-sitter 符号图构建，Git 集成
- 开源社区最活跃的 CLI Agent 之一

**OpenCode**
- 微软研究院推出的开源编码 Agent，原生终端界面、多会话支持，兼容 75+ 模型
- 2026年2月快速崛起至 12.4 万 Star

**Goose**
- 开源可扩展 AI Agent CLI，支持安装、执行、编辑、测试与任意 LLM 集成
- 2025年获得大量关注，支持 SSE 实时响应扩展

**Cody (Sourcegraph)**
- 基于代码图谱的 AI 编程助手，理解整个代码库的语义关系
- 与代码搜索引擎深度集成，适合大型代码库场景

**Gemini CLI (Google)**
- Google 官方的命令行 AI 工作流工具，深度融入开发者日常，支持多模态交互
- 已开源并获得 9000+ Star

### ASSESS

**Devin (Cognition AI)**
- AI 软件工程师，能自主完成端到端软件工程任务
- SWE-bench 的标杆，2025年收购 Windsurf

**SWE-agent (Princeton NLP)**
- 开源 AI 编码 Agent，在 SWE-bench 上实现 12.29% 准确率
- 学术界的代表实现，SWE-bench 的标准 Baseline

**Trae Agent (ByteDance)**
- 字节跳动开源的 AI Coding Agent
- 国内大厂的首个开源 CLI Agent 项目

**Kiro**
- Amazon Q Developer 的后继者，2026年发布的下一代 AI Coding Agent
- 代表了 AWS 在 AI Coding 领域的技术演进方向

**Codex (OpenAI)**
- OpenAI 的官方编程 Agent，"OpenAI 版 Claude Code"，2025年开发者大会正式发布

**Cline**
- VS Code 扩展的 AI 编程 Agent，支持多模型和自定义工具
- 开源社区高度活跃，开发者偏好定制化场景

---

## 三、平台 Platforms (Infrastructure & Orchestration)

### ADOPT

**MCP (Model Context Protocol)**
- Anthropic 推出的开放协议，标准化 AI 模型与外部数据源、工具的交互接口
- 2025年4月爆发式增长，OpenAI、Microsoft、Google、阿里、腾讯、字节跳动纷纷接入，成为事实标准
- 被比喻为"AI 领域的 USB-C"

### TRIAL

**LangGraph**
- 基于图结构的有状态多 Agent 编排框架，支持循环和非循环流程，可视化任务与 Agent 交互
- 精细控制能力最强，适合复杂多步骤工作流，45k+ GitHub Stars

**CrewAI**
- 基于角色协作的 Agent 编排框架，通过 Role/Task/Crew 概念模拟人类团队协作
- 上手最快，45k Stars，"快速启动"首选

**OpenAI Agents SDK**
- OpenAI 的轻量级多 Agent 工作流框架（Swarm 的进化版），3个核心概念（Agent/Runner/Tool）
- 内置 Guardrails 和 Tracing，支持 MCP 协议，原生沙箱环境

**Dify**
- 开源的低代码 AI 应用平台，支持 RAG、Agent、工作流编排，Apache 2.0 许可
- 企业级 AI Agent 落地的重要工具

### ASSESS

**A2A (Agent-to-Agent Protocol)**
- Microsoft 推出的 Agent 间通信协议，与 MCP 互补，实现多 Agent 间的互操作性
- "MCP 统一度量衡，A2A 实现 Agent 互联"

**AutoGen / AG2 (Microsoft)**
- Microsoft 的多 Agent 对话框架，支持 Agent 间协作和自动优化
- 2026年改名 AG2

**LlamaIndex**
- 数据框架，专注于数据索引、检索增强（RAG）、Agent 记忆管理
- 与 LangGraph 深度集成

**Semantic Kernel (Microsoft)**
- 轻量级 SDK，将 AI 集成到企业应用，支持多语言
- 与 Azure 服务深度绑定

**LangFlow / Flowise**
- 基于 LangChain 的可视化低代码平台，基于图的工作流设计
- 低门槛快速原型

**RAGFlow**
- 开源的 RAG 引擎，v0.23.0 新增 Memory、Agent 能力，支持父子分块策略
- 企业级知识管理的重要选择

**MetaGPT**
- 多 Agent 协作框架，通过模拟软件开发团队的角色分工（SDE/PM/Architect）协同工作
- 独特的多角色模拟方法论

**OmAgent**
- 以设备为中心的多模态 Agent 框架
- 面向多模态和设备场景

### HOLD

**纯 LangChain 应用（无 LangGraph）**
- 直接使用 LangChain 的链式抽象而非图结构
- 存在过度抽象和稳定性问题，推荐使用 LangGraph 替代

---

## 四、框架与语言 Frameworks & Languages

### ADOPT

**Python**
- AI Agent 开发的第一语言，几乎所有框架均提供 Python SDK
- LangGraph/CrewAI/AutoGen/LlamaIndex 均为 Python-first，~90% 的 Agent Harness 项目使用

**TypeScript / JavaScript**
- Claude Code 核心实现语言，Node.js 生态下的 Agent SDK 开发
- 大量 MCP Server 使用 TS，约 60% 的 MCP Server

### TRIAL

**Claude Agent SDK (Anthropic)**
- Anthropic 官方的 Agent 开发 SDK，"驱动 Claude Code 的脚手架"的具体实现
- 直接对齐 Claude 模型能力，代表官方推荐的 Harness 构建方式

**Rust**
- 高性能系统编程语言，Amazon Q Developer CLI 等关键工具使用
- 性能敏感的基础设施（Agent 执行循环、沙箱）首选

**OpenAI Agents SDK (Python)**
- OpenAI 官方的 Python Agent 框架，内置 MCP 支持和沙箱执行
- 大厂背书，适合 OpenAI 模型为主的场景

**C# / .NET MCP SDK (Microsoft)**
- Microsoft 官方的 .NET 环境 MCP 服务器和客户端 SDK，1.0 版本已发布
- .NET 企业场景的 MCP 支持

### ASSESS

**Go**
- 并发友好的语言，部分 Agent 工具开始采用
- 高并发场景的潜力，但生态尚在成熟

---

## 趋势概览

| 方向 | 说明 |
|------|------|
| **Harness > Model** | Agent 上限由 Harness 决定，而非模型本身。Anthropic、OpenAI、LangChain 均在构建各自版本的脚手架。 |
| **MCP 一统天下** | 从"战国时代"到统一协议，2025年4月是关键爆发点。 |
| **多 Agent 从实验到标配** | Claude Code Subagents、Cursor 3.0 8路并行——多 Agent 协作已从实验变为标准功能。 |
| **CLI Agent 崛起** | Claude Code 证明了终端 Agent 的工程能力优势，OpenCode、Aider、Goose 快速跟进。 |
| **Spec-Driven 从概念到实践** | 阿里、网易的公开案例表明，SDD 在企业级场景已具备可操作性。 |
| **LLM 自己优化 Harness** | 独立研究项目让 LLM 自己优化基础设施，达到 76.4% 的 SWE-bench 通过率。 |

### 关键判断

| 维度 | 推荐 |
|------|------|
| IDE vs CLI | Cursor 适合前端/全栈沉浸式体验，Claude Code 适合后端/系统级深度控制 |
| 框架选择 | 快速上手选 CrewAI，精细控制选 LangGraph，多 Agent 探索选 AutoGen/AG2 |
| 协议层 | MCP 是必选项，A2A 值得观望 |
| 企业 vs 个人 | 企业级优先 Copilot / Amazon Q，技术团队优先 Claude Code / Cursor / Aider / OpenCode |

---

*本雷达基于 2026年5月公开信息汇编，随着 MCP 生态快速成熟和各厂商加速迭代，部分评估可能在短期内发生变化。建议每季度复审一次。*

*详细调研数据参见 [research/agent-harness-radar.md](research/agent-harness-radar.md)*
