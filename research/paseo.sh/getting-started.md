# Paseo 入门指南

本指南帮助开发者在 10 分钟内完成 Paseo 的安装和基础使用。

## 前置需求

- Node.js 18+
- npm 或 yarn
- 至少一个 coding agent（Claude Code / Codex / OpenCode / Copilot）

## 安装

### 方案一：CLI（推荐）

```bash
npm install -g @getpaseo/cli
```

### 方案二：桌面应用

从 [GitHub Releases](https://github.com/getpaseo/paseo/releases) 下载最新版本

### 方案三：移动端

- iOS：App Store 搜索 "Paseo"
- Android：Google Play 搜索 "Paseo"

## 启动

### 终端启动

```bash
paseo
```

首次启动会显示 QR 码，扫描后可在移动端控制。

### Web 版本

访问 https://app.paseo.sh

## 基本使用

### 1. 运行 Agent

```bash
# 使用 Claude Code
paseo run --provider claude "implement user authentication"

# 使用 Codex
paseo run --provider codex "write unit tests"

# 使用指定模型
paseo run --provider opus-4 "implement feature X"
```

### 2. 查看运行中的 Agent

```bash
paseo ls
```

### 3. 附加到 Agent

查看实时输出：
```bash
paseo attach <agent-id>
```

### 4. 发送消息

给运行中的 agent 发送新任务：
```bash
paseo send <agent-id> "also add integration tests"
```

### 5. Worktree 隔离

在独立 Git 分支上运行 agent：
```bash
paseo run --worktree feature-x "implement feature X"
```

## 配置

Paseo 配置文件位于 `~/.config/paseo/` 或项目根目录的 `paseo.json`。

```json
{
  "providers": {
    "claude": {
      "command": "claude",
      "args": ["--print"]
    },
    "codex": {
      "command": "codex",
      "apiKey": "sk-..."
    }
  },
  "relay": {
    "enabled": true,
    "port": 8080
  }
}
```

## 快捷键

| 快捷键 | 功能 |
|--------|------|
| ⌘K | 命令面板 |
| ⌘N | 新建 agent |
| ⌘D | 垂直分屏 |
| ⌘⇧D | 水平分屏 |
| ⌘W | 关闭面板 |
| ⌘1-9 | 切换面板 |

## 常见问题

### Q: 如何连接移动端？

在移动端安装 Paseo app，然后：
1. 在桌面端运行 `paseo`
2. 扫描显示的 QR 码
3. 即可从手机控制 agent

### Q: 支持哪些 agent？

- Claude Code（Anthropic）
- Codex（OpenAI）
- OpenCode
- Copilot
- Pi

### Q: 代码安全吗？

安全！代码从不离开你的机器。Paseo 只传输：
- agent 的文字输出
- 你的指令

所有远程连接都是 E2E 加密。

### Q: 如何自托管 Relay？

```bash
paseo relay --port 8080
```

## 下一步

- 阅读完整文档：https://paseo.sh/docs
- 加入 Discord 社区
- 探索 Skills：https://paseo.sh/docs/skills
