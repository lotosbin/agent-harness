# Paseo（paseo.sh）研究报告

## 一、因：为何存在

**Paseo** 是一个开源的 **coding agent 编排工具**，让开发者能够从任意设备（桌面、手机、终端）远程控制 Claude Code、Codex、OpenCode 等 coding agent。

**背景脉络**：随着 Claude Code、Copilot 等 CLI coding agent 的兴起，开发者面临几个痛点：
- agent 只能在本地终端运行，无法远程控制
- 多 provider 需要切换不同工具
- 移动办公时无法继续用 agent 工作
- 缺乏统一的 agent 管理界面

Paseo 的出现填补了这一空白——一个统一的 agent 编排层，让代码留在本地，agent 却可以从任何地方控制。

## 二、果：带来的改变

### 2.1 核心价值

- **设备无关**：从手机、平板、桌面、网页随时控制 agent
- **全功能保留**：使用原生 CLI，skills、config、MCP servers 全部保留
- **隐私优先**：代码留在本地，无遥测，登录可选
- **多 provider 统一**：Claude Code、Codex、OpenCode、Copilot、Pi 一个界面

### 2.2 核心功能

| 功能 | 说明 |
|------|------|
| **多设备客户端** | Desktop（Electron）、Web、iOS、Android、CLI |
| **E2E 加密 Relay** | 远程访问无需公网 IP，支持直接连接 |
| **键盘优先** | ⌘K 命令面板、⌘N 新 agent、⌘D 分屏 |
| **本地语音栈** | 完全本地化的语音输入/输出 |
| **Git Worktree** | 隔离分支运行 agent |
| **可编程 CLI** | 自动化脚本集成 |
| **MCP 服务器** | 内置 MCP server 支持 |

## 三、体：架构与设计

### 3.1 技术栈

```
├── packages/
│   ├── server/        # WebSocket API + MCP 服务器
│   ├── app/           # Expo 移动客户端
│   ├── cli/           # 终端界面
│   ├── desktop/       # Electron 桌面应用
│   ├── relay/         # 远程连接服务
│   └── website/       # 文档网站
├── skills/            # 内置 skills
└── docs/              # 文档
```

- **语言**：TypeScript（为主）
- **许可证**：AGPL-3.0
- **平台**：macOS、Linux、Windows、Web、iOS、Android
- **Stars**：~2.2k

### 3.2 架构设计

```
┌─────────────────────────────────────────────────────────────┐
│                        客户端层                              │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐       │
│  │ Desktop │  │   iOS   │  │ Android │  │   CLI   │       │
│  │(Electron│  │  (Expo) │  │ (Expo)  │  │         │       │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘       │
│       │            │            │            │             │
│       └────────────┴─────┬──────┴────────────┘             │
│                          │                                 │
│                    WebSocket API                            │
│                          │                                 │
├──────────────────────────┼─────────────────────────────────┤
│                   packages/server                            │
│                          │                                 │
│       ┌──────────────────┼──────────────────┐              │
│       │                  │                  │              │
│       ▼                  ▼                  ▼              │
│  ┌─────────┐       ┌─────────┐       ┌─────────┐          │
│  │ MCP     │       │ Agent   │       │ Worktree│          │
│  │ Server  │       │ Manager │       │ Manager │          │
│  └─────────┘       └─────────┘       └─────────┘          │
│                          │                                 │
├──────────────────────────┼─────────────────────────────────┤
│                   本地执行层                                │
│       ┌──────────────────┼──────────────────┐              │
│       │                  │                  │              │
│       ▼                  ▼                  ▼              │
│  ┌─────────┐       ┌─────────┐       ┌─────────┐          │
│  │ Claude  │       │  Codex  │       │OpenCode │          │
│  │  Code   │       │         │       │         │          │
│  └─────────┘       └─────────┘       └─────────┘          │
│                          │                                 │
│              ┌───────────┴───────────┐                    │
│              │    本地开发环境         │                    │
│              │  (skills/config/MCP)  │                    │
│              └───────────────────────┘                    │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 远程连接机制

```
┌──────────────┐                    ┌──────────────┐
│   手机客户端   │ ──── E2E 加密 ──── │   Relay      │
│              │                    │   Server     │
└──────┬───────┘                    └──────┬───────┘
       │                                  │
       │         直接连接（同一网络）        │
       │◄─────────────────────────────────┤
       │                                  │
       ▼                                  ▼
┌─────────────────────────────────────────────────────────────┐
│                  本地 Agent Server                           │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│  │ Claude  │  │  Codex  │  │OpenCode │  │ Copilot │        │
│  │  Code   │  │         │  │         │  │         │        │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘        │
└─────────────────────────────────────────────────────────────┘
```

## 四、用：使用场景与方式

### 4.1 主要使用场景

| 场景 | 说明 |
|------|------|
| **移动开发** | 手机上继续 agent 工作，语音输入任务 |
| **远程开发** | 在服务器上运行 agent，本地监控 |
| **多任务并行** | 同时运行多个 agent，不同分支/任务 |
| **自动化集成** | CLI 脚本调用 agent，CI/CD 集成 |
| **统一管理** | 一个界面管理所有 coding agent |

### 4.2 CLI 命令

```bash
# 安装
npm install -g @getpaseo/cli

# 启动（显示 QR 码）
paseo

# 运行 agent
paseo run --provider claude "implement user authentication"
paseo run --provider opus-4 "implement feature X"

# 列出 agent
paseo ls

# 附加到运行中的 agent
paseo attach <agent-id>

# 发送消息
paseo send <agent-id> "also add tests"

# Worktree 隔离分支
paseo run --worktree feature-x "implement feature X"
```

### 4.3 键盘快捷键

| 快捷键 | 功能 |
|--------|------|
| ⌘K | 命令面板 |
| ⌘N | 新建 agent |
| ⌘D | 垂直分屏 |
| ⌘⇧D | 水平分屏 |
| ⌘W | 关闭面板 |
| ⌘1-9 | 切换面板 |

## 五、洞：深度洞察

### 5.1 与其他工具对比

| 维度 | Paseo | Claude Code | Cursor | GitHub Copilot |
|------|-------|-------------|--------|----------------|
| 部署方式 | 自托管 | 本地 CLI | 桌面应用 | 插件 |
| 多 agent | ✅ | ❌ | ❌ | ❌ |
| 远程控制 | ✅ | ❌ | ❌ | ❌ |
| 多 provider | ✅ | ❌ | ❌ | ❌ |
| 移动端 | ✅ | ❌ | ❌ | ❌ |
| 开源 | ✅ | ❌ | 部分 | ❌ |

### 5.2 关键洞察

1. **定位独特**：Paseo 不是又一个 coding agent，而是 agent 的「编排层」——保持现有工具优势的同时解决多设备协作问题。

2. **隐私设计**：代码从不离开本地，只传输 agent 的输出和指令。这一设计在企业安全场景中尤为重要。

3. **生态整合**：支持 Claude Code、Codex、OpenCode、Copilot 等多种 agent，不绑定单一 provider。

4. **自托管优先**：无需云服务，完全在本地运行，适合有安全要求的企业。

5. **开发活跃**：GitHub 2.2k stars，184 forks，活跃开发中。

## 六、资源索引

| 资源 | 链接 |
|------|------|
| 官方网站 | https://paseo.sh |
| GitHub | https://github.com/getpaseo/paseo |
| Discord | 官方 Discord 社区 |
| 文档 | https://paseo.sh/docs |
| CLI 参考 | https://paseo.sh/docs/cli |
| 配置指南 | https://paseo.sh/docs/configuration |
| 安全文档 | https://paseo.sh/docs/security |
| Voice 文档 | https://paseo.sh/docs/voice |
| Worktrees | https://paseo.sh/docs/worktrees |
| Skills | https://paseo.sh/docs/skills |

### 主要 GitHub 仓库

- [getpaseo/paseo](https://github.com/getpaseo/paseo) — 主仓库（monorepo）
- [packages/server](https://github.com/getpaseo/paseo/tree/main/packages/server) — Agent 服务器
- [packages/cli](https://github.com/getpaseo/paseo/tree/main/packages/cli) — CLI 客户端
- [packages/desktop](https://github.com/getpaseo/paseo/tree/main/packages/desktop) — Electron 桌面应用
- [packages/app](https://github.com/getpaseo/paseo/tree/main/packages/app) — Expo 移动应用
