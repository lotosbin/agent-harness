# YUA-41 调研：Graphify 研究报告

## Investigation

### 需求概述

本任务要求在现有研究 SOP 中增加新步骤，引入 [graphify](https://github.com/safishamsi/graphify) 作为代码库知识图谱提取工具。目标是通过 graphify 构建代码库的结构化知识图谱，丰富研究报告的输入来源。

### 一、项目定位

Graphify 是一款将代码库（代码/文档/PDF/图片/视频）转换为**可查询知识图谱**的 AI 辅助工具。通过 `/graphify` 命令调用后，生成三个文件：

```
graphify-out/
├── graph.html       # 交互式可视化（图谱可点击、过滤、搜索）
├── GRAPH_REPORT.md  # 报告：核心概念、意外连接、建议问题
└── graph.json      # 完整图谱，随时可查询
```

### 二、因（Causality）——为何存在

1. **痛点**：AI 编程助手在大型代码库中缺乏全局上下文，每次会话都从零开始，无法感知代码模块间的深层关联
2. **机会**：Tree-sitter AST 解析成熟，本地提取代码结构成本极低；LLM 具备从文档中推理关系的能力
3. **定位**：graphify 不是 RAG 替代品，而是**全局结构感知层**，让 AI 在回答任何问题前先理解代码拓扑

### 三、果（Effects）——核心能力

| 能力 | 说明 |
|------|------|
| **多语言代码解析** | 29+ 语言（Python/JS/TS/Go/Rust/Java 等），本地 Tree-sitter，零 API 费用 |
| **文档理解** | Markdown/PDF/HTML/Office/图片，通过 AI 模型语义提取 |
| **视频转录** | YouTube/本地视频，本地 faster-whisper 转录 |
| **图谱查询** | `graphify query` / `graphify path` / `graphify explain` CLI 查询 |
| **MCP 服务** | 暴露为 stdio MCP server，供 Agent 工具调用 |
| **平台集成** | Claude Code / Cursor / VS Code Copilot / Gemini CLI / Aider / Trae 等 16+ 平台 |
| **多格式导出** | HTML / Obsidian Vault / SVG / GraphML (Gephi) / Neo4j / Wiki |
| **隐私保护** | 代码本地处理，文档经 API 提取，无遥测追踪 |

### 四、体（Substance）——技术架构

**处理管线（三阶段）**：

1. **代码结构提取**（免费）— Tree-sitter 解析源码，提取类/函数/导入/调用图
2. **媒体转录**（免费）— faster-whisper 本地转录视频/音频
3. **文档语义提取**（消耗 Token）— Claude subagent 并行处理 Markdown/PDF/图片，输出 JSON 片段合并为图

**置信度体系**：

| 标签 | 含义 | 置信度 |
|------|------|--------|
| EXTRACTED | 源码直接证据 | 1.0 |
| INFERRED | LLM 推理（基于评分规则） | 0.95 ~ 0.55 |
| AMBIGUOUS | 不确定，需人工审查 | — |

**聚类算法**：Leiden 算法，基于边密度聚类，不需要独立 embeddings 或向量数据库。

**性能数据**：52 个混合文件基准测试显示，每次查询比直接读文件节省 **71.5x Token**。

### 五、用（Application）——集成到研究 SOP

在现有 SOP（收集资讯 → 官网/社区 → 研究报告 → 入门指导 → 一张图看懂使用 → 一张图看懂原理）基础上，可在**第一步"收集主流媒体相关资讯"之后**增加：

```
第 1.5 步（图谱辅助）：使用 graphify 提取代码库知识图谱
```

**集成方式**：

```bash
# 安装
pip install graphifyy && graphify install

# 为研究项目构建图谱
/graphify .

# 查看报告
cat graphify-out/GRAPH_REPORT.md

# 可视化浏览
open graphify-out/graph.html

# 追加研究（仅更新变更文件）
/graphify . --update
```

**对研究报告写作的辅助**：
- 获取"God nodes"（高连接度概念），快速理解项目核心模块
- 发现跨文件意外连接，发现架构设计中的深层关联
- 提取 `# NOTE:` / `# WHY:` / docstring 中的设计意图
- 生成调用流架构图：`graphify export callflow-html`

### 六、洞（Insights）——深度洞察

**核心优势**：

1. **本地免费提取**：代码结构完全本地化，零 Token 消耗，隐私安全
2. **多模态覆盖**：除代码外还处理文档/PDF/视频，覆盖研究场景的核心信息来源
3. **平台广泛**：支持 16+ 主流 AI 编程助手，适用范围广
4. **Token 节省**：71.5x Token 减少，显著降低 AI 推理成本
5. **团队协作**：图谱文件可提交到 git，团队成员拉取即用

**现存局限**：

1. **文档提取依赖 AI API**：需要配置 API Key（Claude/Gemini/Kimi/Ollama），无免费午餐
2. **中文文档支持待验证**：README 有简体中文翻译版，工具本身对中文代码/文档的提取质量需实测
3. **Graphify Labs 商业化**：作者主页推广 Penpax（商业产品），graphify 核心开源但存在商业转化路径
4. **大型代码库性能**：万级文件以上需关注并行度和 Token 预算控制
5. **与现有 SOP 的契合度**：作为辅助工具价值明确，但研究报告的"因果体用"结构仍需人工判断

### 七、适用场景

| 推荐 | 不推荐 |
|------|--------|
| 大型开源项目的全局理解 | 小型脚本的快速调研 |
| 多模块架构的深层关联发现 | 单一文件的功能解释 |
| 团队共享代码库上下文 | 纯自然语言问答（非代码相关） |
| 研究报告的结构化输入补充 | 需完全离线运行的场景（文档处理需 API） |

### 受影响文件

- `research/` 下各研究子目录：将新增第 1.5 步指导，建议在 CLAUDE.md 中补充 graphify 相关规范
- 研究报告模板：可考虑增加"知识图谱发现"章节

### 建议实施步骤

1. **安装测试**：在现有 research 目录运行 `/graphify .`，评估提取质量
2. **SOP 补充**：在 CLAUDE.md 中增加 graphify 使用步骤指引
3. **模板优化**：考虑在研究报告结构中增加"图谱发现"子章节
4. **效果回访**：在下一个研究任务中实际使用，根据反馈调整 SOP

<!-- END STOKOWSKI LIFECYCLE -->
