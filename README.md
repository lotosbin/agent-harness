# OpenSpec 调研报告

## 什么是 OpenSpec

**OpenSpec** 是一个轻量级、开源的**规格驱动开发（Spec-Driven Development, SDD）框架**，专为 AI 编程助手设计。它在不依赖 API Key 或 MCP 连接的情况下，作为通用的规划层，弥合开发者意图与 AI 生成代码之间的鸿沟。

官网：[openspec.dev](https://openspec.dev)
GitHub：[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)

---

## 核心理念

> "Fluid not rigid, iterative not waterfall, easy not complex, built for brownfield not just greenfield."
> （流动而非僵化，迭代而非瀑布，简单而非复杂，为棕地开发而生而不仅是绿地开发。）

---

## 核心特性

| 特性 | 说明 |
|------|------|
| **规格变更审查** | 每个变更生成 `spec delta`，捕获系统需求变更 |
| **持久化上下文** | 规格与代码共存于仓库，按能力组织 |
| **综合规划** | 生成提案文档、实施任务分解、技术设计决策、规格差异 |
| **30+ AI 助手支持** | Claude Code, Cursor, Codex, GitHub Copilot, Windsurf, Gemini CLI 等 |
| **无需 API Key** | 不依赖外部连接，直接在本地运行 |

---

## 工作流程

### 核心命令

```bash
npm install -g @fission-ai/openspec@latest  # 安装

openspec init          # 初始化项目
openspec update        # 刷新 AI 代理指令
openspec config profile # 选择工作流配置
```

### 斜杠命令

| 命令 | 用途 |
|------|------|
| `/opsx:propose <想法>` | 创建包含规格、设计、任务的变更提案 |
| `/opsx:apply` | 执行提案中的任务 |
| `/opsx:archive` | 归档已完成的变更 |
| `/opsx:new` | 新建变更 |
| `/opsx:continue` | 继续未完成的变更 |
| `/opsx:verify` | 验证变更 |
| `/opsx:sync` | 同步状态 |

---

## 目录结构

```
your-project/
├── .changeset/           # 变更提案和归档
├── openspec/specs/       # 规格定义（按能力组织）
│   ├── auth-login/
│   ├── auth-session/
│   ├── checkout-cart/
│   └── checkout-payment/
└── AGENTS.md             # AI 代理指令
```

变更提案生成的结构：
```
.changeset/
└── your-change/
    ├── proposal.md       # 提案文档
    ├── design.md         # 技术设计
    ├── tasks.md          # 实施任务
    └── spec-deltas/      # 规格差异
```

---

## 技术细节

| 项目 | 值 |
|------|-----|
| 语言 | TypeScript (98.7%) |
| Node.js 要求 | v20.19.0+ |
| 包管理器 | npm, pnpm, yarn, bun, nix |
| 许可证 | MIT |

---

## 推荐实践

- **模型选择**：使用高推理能力模型（Opus 4.5, GPT 5.2）
- **上下文管理**：保持干净的上下文窗口，实施前清空
- **工具支持**：20+ AI 助手支持

---

## 正在开发中的功能

OpenSpec 正在开发 **"Workspaces"** 功能，目标是：
- 团队协作支持
- 大型代码库支持
- 多仓库规划
- 定制化能力
- 更多集成

---

## 安装与使用

```bash
# 安装
npm install -g @fission-ai/openspec@latest

# 在项目中初始化
cd your-project
openspec init
openspec update

# 禁用遥测（可选）
export OPENSPEC_TELEMETRY=0
# 或
export DO_NOT_TRACK=1
```

---

## 对比传统开发方式

| 维度 | 传统开发 | OpenSpec |
|------|----------|-----------|
| 规划 | 口头或文档分散 | 规格与代码共存 |
| AI 协作 | 每次会话重置上下文 | 持久化规格供 AI 引用 |
| 变更追踪 | git commit 记录代码变更 | `spec delta` 记录需求变更 |
| 团队交接 | 需要大量 onboarding | AI 可直接读取规格文档 |
| 审查流程 | 代码审查为主 | 需求、规格、设计、任务全面审查 |

---

## 适用场景

- 使用 AI 编程助手的团队
- 需要在团队中保持 AI 上下文一致性的项目
- 规格驱动开发的实践者
- 大型代码库的多人协作项目

---

## 参考链接

- 官网：[openspec.dev](https://openspec.dev)
- GitHub：[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)
- NPM：[@fission-ai/openspec](https://www.npmjs.com/package/@fission-ai/openspec)
