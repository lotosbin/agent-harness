# OpenSpec 快速入门：让 AI 编程助手真正懂你

> 本文是 OpenSpec 付费课程的免费引流教程，完整版课程包含企业实战和高级技巧。

## 开篇：你是否遇到过这些情况？

你和 AI 说："帮我加一个登录功能"。

五分钟后，AI 给你写了一个完整的 OAuth2 认证系统，包括 JWT、Refresh Token、密码重置、邮箱验证...

但你只是想要一个简单的用户名+密码登录。

Sound familiar? 这是每一个 AI 编程助手用户都经历过的痛。

问题的根源不在于 AI 不够聪明，而在于**我们没有给 AI 一个清晰的规格说明**。

## OpenSpec 是什么

OpenSpec 是一个**规格驱动开发（Spec-Driven Development）框架**，专为 AI 编程助手设计。

它的核心思想很简单：**在写代码之前，先告诉 AI 你要做什么。**

> 一句话：OpenSpec 让 AI 每次都知道你要做什么，而不是让它去猜。

### 核心价值

| 特性 | 解决的问题 |
|------|----------|
| **规格持久化** | AI 重启后还记得你的需求 |
| **变更追踪** | 清楚知道每次改了什么、为什么改 |
| **系统规划** | 提案→设计→任务，完整的工作流 |
| **30+ AI 助手支持** | Claude Code、Cursor、Windsurf...都能用 |

## 5 分钟快速上手

### 环境要求

- Node.js >= 20.19.0
- npm / pnpm / yarn / bun 任选其一

> 推荐使用 nvm 管理 Node.js 版本：
> ```bash
> nvm install 20
> nvm use 20
> ```

### 安装 OpenSpec

一行命令搞定：

```bash
npm install -g @fission-ai/openspec@latest
```

验证安装：

```bash
openspec --version
# 输出: 1.2.0
```

### 初始化项目

进入你的项目目录，初始化 OpenSpec：

```bash
cd your-awesome-project
openspec init
```

这会在项目中创建：

```
your-awesome-project/
├── openspec/
│   └── specs/           # 规格定义目录
├── .changeset/          # 变更提案目录
└── AGENTS.md            # AI 助手指令文件
```

### 创建第一个变更提案

在 AI 编程助手中（以 Claude Code 为例），输入：

```
/opsx:propose 添加用户反馈功能
```

OpenSpec 会自动为你创建完整的变更提案目录结构。

## 实战案例：添加用户反馈功能

为了让你更好地理解 OpenSpec 的工作流程，让我们用一个具体例子走一遍。

### 步骤 1：用斜杠命令创建提案

在 Claude Code 中输入：

```
/opsx:propose 添加用户反馈功能
```

### 步骤 2：查看生成的提案

OpenSpec 会生成类似这样的 `proposal.md`：

```markdown
## Why

用户反馈是产品迭代的重要依据。我们需要一个简单的反馈收集功能。

## What Changes

- 添加反馈提交表单
- 存储反馈到数据库
- 提供管理员查看界面

## Capabilities

### New Capabilities
- `user-feedback`: 用户反馈提交和查看功能
```

### 步骤 3：查看技术设计

`design.md` 包含：

- 上下文和约束
- 技术选型决策
- 风险评估

### 步骤 4：查看任务列表

`tasks.md` 把你需要做的事情分解成可执行的任务：

```markdown
## 1. 前端实现
- [ ] 1.1 创建反馈表单组件
- [ ] 1.2 添加表单验证

## 2. 后端实现
- [ ] 2.1 创建反馈 API 端点
- [ ] 2.2 实现数据存储

## 3. 管理员界面
- [ ] 3.1 创建反馈列表页面
```

### 步骤 5：执行任务

使用 `/opsx:apply` 命令开始执行任务：

```
/opsx:apply
```

AI 会逐个完成任务，每完成一个自动更新任务状态。

## 传统开发 vs OpenSpec

| 维度 | 传统开发 | OpenSpec |
|------|----------|----------|
| **规划方式** | 口头描述或分散的文档 | 规格与代码共存于仓库 |
| **AI 协作** | 每次会话都要重新解释需求 | AI 自动读取规格，保持上下文 |
| **变更追踪** | Git commit 记录代码变更 | `spec delta` 记录需求变更 |
| **团队协作** | 新成员需要大量 onboarding | AI 可直接读取规格文档 |
| **审查流程** | 代码审查为主 | 需求、规格、设计、代码全面审查 |

## 常见问题

### Q: OpenSpec 和 MCP 有什么区别？

MCP（Model Context Protocol）是连接 AI 和外部工具的协议，而 OpenSpec 是一种**开发方法论**。两者可以一起使用，OpenSpec 不依赖 MCP。

### Q: 需要付费吗？

OpenSpec 本身是免费开源的。本教程也是免费的。

### Q: 支持哪些 AI 助手？

官方支持 30+ AI 助手，包括：
- Claude Code
- Cursor
- GitHub Copilot
- Windsurf
- Gemini CLI
- 等等...

### Q: 适合什么规模的项目？

OpenSpec 适合所有规模的项目，从小功能开发到大型企业应用都可以使用。唯一的区别是规格文档的详细程度。

## 进阶路径

掌握了基础用法后，你可以探索：

- **规格文件高级用法**：深入学习 `spec.md` 的 YAML 结构
- **团队协作**：使用 OpenSpec Workspaces 进行多人协作
- **大型项目**：多仓库规划和依赖管理
- **自定义工作流**：根据团队需求定制 OpenSpec 行为

> 这些进阶内容会在付费课程中详细讲解，包括：
> - 企业级项目实战
> - 团队协作最佳实践
> - OpenSpec 与 CI/CD 集成
> - 高级规格编写技巧

---

## 下一步

1. **现在就试试**：在项目中运行 `npm install -g @fission-ai/openspec@latest`
2. **创建你的第一个提案**：用 `/opsx:propose` 命令描述你想做的功能
3. **关注我们**：获取更多 OpenSpec 使用技巧

如果你觉得这个教程有帮助，欢迎分享给需要的同学！

---

*有问题或建议？欢迎在评论区留言！*
