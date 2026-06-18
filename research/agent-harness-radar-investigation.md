## Investigation

### 需求分析

YUA-43 要求参考 Thoughtworks Technology Radar 格式，在 agent-harness 项目中增加 `radar.md` 文件，跟踪 AI Coding Agent 领域的工具、技术、框架动态。

#### Thoughtworks Technology Radar 格式规范

- **象限 (Quadrants, 4个)**: Techniques（技术）/ Platforms（平台）/ Tools（工具）/ Languages & Frameworks（框架与语言）
- **环 (Rings, 4个)**: Adopt（采纳）/ Trial（试验）/ Assess（评估）/ Hold（暂缓）
- **数据格式**: CSV 或 JSON，含字段：`name`, `ring`, `quadrant`, `isNew`, `description`（字段名大小写敏感，无空格）
- **可视化**: 可通过 radar.thoughtworks.com 直接构建雷达图（BYOR 工具）

#### 调研发现

通过 agent 对 Agent Harness 领域进行了全面调研，覆盖范围：

| 象限 | 核心内容 |
|------|----------|
| Techniques | ReAct/CoT 模式（ADOPT）、SDD（Trial）、多 Agent 编排（Trial）、Harness Engineering（Trial）、Agentic RAG（Assess） |
| Tools | Claude Code/GitHub Copilot/Cursor（ADOPT）、Windsurf/Aider/OpenCode/Gemini CLI（Trial）、Devin/SWE-agent/Trae（Assess） |
| Platforms | MCP（ADOPT）、LangGraph/CrewAI（Trial）、A2A/AutoGen/LlamaIndex（Assess）、纯 LangChain（Hold） |
| Languages & Frameworks | Python/TypeScript（ADOPT）、Claude Agent SDK/Rust/C#（Trial）、Go（Assess） |

#### 关键洞见

1. **Harness > Model**: Agent 上限由 Harness 决定，而非模型本身
2. **MCP 一统天下**: 2025年4月爆发，成为事实标准
3. **多 Agent 从实验到标配**: Claude Code Subagents、Cursor 3.0 8路并行
4. **CLI Agent 崛起**: Claude Code 周提交量从 10 万增长至 250 万次
5. **Spec-Driven 从概念到实践**: SDD 在企业级场景已具备可操作性

### 受影响文件

- **新增**: `research/agent-harness-radar.md` — 完整的 Technology Radar 研究文档（已由 research agent 生成）
- **后续可增**: `radar.md`（位于项目根目录）— 精简版雷达图，供快速查阅

### Proposed approach

- **立即实施**: 将 `research/agent-harness-radar.md` 内容精简为项目根目录的 `radar.md`，格式参照 Thoughtworks 雷达图，提供象限×环的矩阵视图，支持每季度更新
- **数据层分离**: 调研数据保存在 `research/agent-harness-radar.md`，展示层为 `radar.md`
- **格式设计**: 优先 Markdown 格式（便于版本控制），后续可扩展 CSV/JSON 格式支持 radar.thoughtworks.com 可视化
- **更新机制**: 结合 CLAUDE.md 中的"研究步骤"，每次新研究一个项目时同步更新 radar.md

### 开放问题

1. **radar.md 位置**: 放根目录还是 `docs/` 目录？建议放根目录便于快速查阅
2. **更新节奏**: 每季度复审一次，或随每次新研究项目自动同步
3. **可视化**: 是否需要生成 CSV/JSON 格式以支持 radar.thoughtworks.com 的雷达图可视化

### 网络限制说明

当前无法访问 Linear API 和 GitHub API，无法直接发布评论。调研结果已保存在 `research/agent-harness-radar.md`。

<!-- END STOKOWSKI LIFECYCLE -->
