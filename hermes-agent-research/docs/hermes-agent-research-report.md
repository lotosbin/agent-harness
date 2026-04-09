# Hermes Agent 调研报告

> 调研日期：2026-04-08
> 官网：https://hermes-agent.nousresearch.com/
> GitHub：https://github.com/NousResearch/hermes-agent
> GitHub Stars：~27,000+

---

## 一、项目概述

Hermes Agent 是由 **Nous Research** 开发的自学习型 AI Agent，定位为「与你共同成长的智能体」（The Agent That Grows With You）。与大多数能力固定的 AI 工具不同，Hermes Agent 能够从使用经验中持续学习、自我进化。

**核心定位**：不是又一个 Agent 框架，而是一个具体的、会成长的个人 Agent。它声称是**唯一一个内置学习闭环的 Agent**。

**开发者背景**：主要贡献者 Teknium（ Nous Research 创始人），主分支 2,912 次提交，社区贡献活跃（v0.2.0 包含 216 个合并 PR，来自 63 位贡献者）。

---

## 二、项目规模与社区

| 指标 | 数值 |
|------|------|
| GitHub Stars | ~27,000+ |
| 贡献者 | 200+ |
| 提交次数 | 2,912 |
| 当前版本 | v0.5.0（持续活跃开发）|
| 许可证 | MIT |

---

## 三、核心功能特性

### 3.1 自我学习闭环（最独特功能）

Hermes Agent 的核心竞争力在于其内置的持续学习能力：

1. **自动创建技能（Auto-Skill Creation）**
   - 完成复杂任务后，Agent 自动将操作过程封装为可复用的技能（Skill）
   - 这些技能以 YAML/文档形式持久化存储

2. **技能自我改进（Skill Self-Improvement）**
   - 每次使用技能后，Agent 评估执行效果并优化技能表现
   - 形成越用越精准的正向循环

3. **记忆持久化（Memory Persistence）**
   - 定期主动将重要信息写入长期记忆
   - 不依赖外部数据库，内置管理

4. **跨会话搜索（Cross-Session Search）**
   - 搜索历史对话，LLM 总结关键内容
   - 真正实现「记住上次对话」

5. **用户建模（User Profiling）**
   - 集成 Honcho 对话式建模
   - 理解「你是谁」——工作风格、偏好、常用任务

### 3.2 跨平台消息网关（Gateway）

一个 Agent 实例，多个入口：

| 平台 | 特点 |
|------|------|
| **CLI** | 完整终端界面 |
| **Telegram** | 语音转文字，跨平台对话 |
| **Discord** | 服务器集成 |
| **Slack** | 工作流集成 |
| **WhatsApp** | 移动端入口 |
| **Signal** | 隐私优先通信 |
| **Email** | IMAP/SMTP，邮件处理 |
| **Home Assistant** | 智能家居控制 |

> 只需运行一个 Gateway 进程，即可从任何平台访问同一个 Agent 会话。

### 3.3 多模型支持（不绑定提供商）

| 提供商 | 说明 |
|--------|------|
| Nous Portal | Nous Research 自有服务 |
| OpenRouter | 200+ 模型可选 |
| z.ai / GLM | 智谱 AI |
| Kimi / Moonshot | 月之暗面 |
| MiniMax | 稀宇科技 |
| OpenAI | GPT 系列 |
| Anthropic | Claude 系列 |
| 自定义端点 | 任何兼容 API |

切换模型命令：
```bash
hermes model
```
一行命令，无需改代码。

### 3.4 灵活部署（6种后端）

| 部署方式 | 适用场景 |
|---------|---------|
| **本地** | 直接在笔记本运行 |
| **Docker** | 容器化部署 |
| **SSH** | 远程服务器 |
| **Daytona** | 无服务器持久化，按需唤醒 |
| **Singularity** | 无服务器 |
| **Modal** | 空闲时几乎零成本，按使用计费 |

最低可在 **5 美元 VPS** 上运行，也支持 GPU 集群。

### 3.5 定时任务（Cron Scheduler）

内置自然语言配置的调度器：
- 日报 / 周报自动生成
- 定期备份
- 自动审计

全部用自然语言配置，无人值守运行。

---

## 四、技术架构详解

### 4.1 四层记忆系统

Hermes Agent 没有单一的记忆系统，而是**四层协作**：

| 层级 | 名称 | 存储位置 | 用途 |
|------|------|---------|------|
| L1 | 提示记忆 | `MEMORY.md` / `USER.md` | 最精炼的上下文提示 |
| L2 | 工作记忆 | 会话上下文 | 当前会话信息 |
| L3 | 技能记忆 | `skills/` 目录 | 封装的操作技能 |
| L4 | 长期记忆 | 数据库/文件 | 持久化的知识 |

> 这与 OpenClaw（单层记忆，容易遗忘）形成鲜明对比。Hermes 的多层次设计避免了「把所有东西都塞进上下文」导致的 token 膨胀和性能下降。

### 4.2 ACP 协议（Agent Communication Protocol）

Hermes Agent 使用自研的 **ACP** 标准实现多 Agent 通信：

- **ACP Server**：VS Code、Zed、JetBrains 编辑器集成
- **ACP Adapter**：通用适配器，支持外部 Agent 接入
- **ACP Registry**：技能与服务注册中心

这使得 Hermes Agent 可以作为团队中的「Managed Employee」运行（官方提供了 Paperclip 公司演示示例）。

### 4.3 MCP 支持（Model Context Protocol）

原生 MCP 客户端支持：
- stdio 和 HTTP 传输
- 自动重连
- 资源 / 提示词发现
- 采样（服务端发起的 LLM 请求）

### 4.4 技能生态系统（Skills Ecosystem）

- **70+** 内置和可选技能
- **15+** 分类
- Skills Hub：社区技能发现与共享
- 支持按平台启用/禁用
- 支持基于工具可用性的条件激活

技能分类示例：
- `mlops/` — MLOps 相关
- 各类工具集成

### 4.5 项目目录结构

```
hermes-agent/
├── agent/           # 核心 Agent 逻辑
├── acp_adapter/    # ACP 协议适配器
├── acp_registry/   # ACP 注册中心
├── agent/           # Agent 实现
├── cron/            # 定时任务调度
├── docs/            # 文档
├── environments/   # 环境配置
├── gateway/         # 跨平台网关
│   └── platforms/  # 各平台适配器
│       ├── telegram.py
│       ├── discord.py
│       ├── slack.py
│       └── ...
├── hermes_cli/     # CLI 界面
├── skills/          # 技能目录
├── honcho_integration/  # Honcho 用户建模
├── docker/          # Docker 部署
├── cli.py           # CLI 入口
└── ...
```

---

## 五、版本演进

| 版本 | 发布日期 | 亮点 |
|------|---------|------|
| v0.1.0 | 早期内部版本 | 基础框架 |
| **v0.2.0** | 2026-03-12 | 多平台网关、ACP 编辑器集成、70+技能、生态爆发 |
| v0.3.0 - v0.5.0 | 持续迭代 | 持续优化与功能扩展 |

---

## 六、与 OpenClaw 的关系

Hermes Agent 来自 Nous Research，而 OpenClaw 是之前流行的开源 Agent 项目。

**迁移支持**：
```bash
hermes claw migrate
```
自动导入 OpenClaw 配置和工作流。

> Hermes Agent 的记忆系统是针对 OpenClaw 的痛点（单层记忆、上下文膨胀）重新设计的。

---

## 七、快速上手

### 安装（Linux/macOS）

```bash
curl -L https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

### 首次运行

```bash
hermes
```

### 配置模型

```bash
hermes model
```

### 部署 Telegram Bot

```bash
hermes gateway telegram --token YOUR_BOT_TOKEN
```

---

## 八、优势与局限性

### 优势

1. **真正的自我进化** — 不是噱头，是完整的学习闭环实现
2. **极低运行成本** — 5 美元 VPS 可运行
3. **真正的多平台** — 一次部署，全平台接入
4. **模型无关** — 不绑定任何提供商
5. **开源透明** — 可审计代码，无黑盒
6. **社区活跃** — 快速迭代，贡献者众多
7. **MCP 原生支持** — 生态兼容性强

### 局限性

1. **依赖 LLM API** — 需要稳定的模型调用后端
2. **技能生成质量** — 自动生成的技能仍需人工审核
3. **多平台配置** — 初期配置有一定复杂度
4. **安全考量** — Telegram/Discord Bot 需妥善管理 token
5. **文档尚在完善** — 社区文档质量参差不齐

---

## 九、适用场景

- **个人助手**：日常任务、日程、跨设备同步
- **团队协作**：作为团队成员参与工作流（ACP 协议）
- **自动化运维**：定时任务、备份、监控
- **开发伴侣**：代码审查、文档生成、调试辅助
- **客服机器人**：多平台接入的客户支持

---

## 十、结论

Hermes Agent 代表了 AI Agent 的一个新方向：**从固定工具到学习型伙伴**。其四层记忆系统、自我技能创建机制、以及多平台网关设计，构成了一套完整且可行的自进化 Agent 架构。

对于希望拥有「越用越懂你」的私人 AI 助手的用户，Hermes Agent 是一个值得关注和尝试的开源项目。

---

## 参考资源

- 官网：https://hermes-agent.nousresearch.com/
- GitHub：https://github.com/NousResearch/hermes-agent
- Nous Research：https://nousresearch.com/
- CSDN 中文攻略：15K Star 中文首发!5分钟部署一个会自我进化的私人Agent
- 技术博客：OpenClaw vs Hermes Agent 记忆系统对比分析
