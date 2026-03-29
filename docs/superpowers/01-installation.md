# 第 1 篇：安装与验证

> Superpowers 安装 | Claude Code 插件安装 | AI 编程框架

## 你是否遇到过这些困境？

- AI 生成了一堆代码，但跑不起来
- 让 AI 修 Bug，越修越多
- 每次对话都要从头解释项目背景
- AI 写的代码自己都看不懂，更不敢交给团队

**问题的根源不是 AI 不够聪明，而是缺少让 AI 稳定工作的流程。**

Superpowers 就是来解决这个问题的。

---

## 什么是 Superpowers？

Superpowers 是一个**AI 编码 Agent 的技能框架与方法论**。它不依赖任何 API Key 或外部服务，通过组合式的"技能"（Skills）让 AI Agent 自动遵循经过验证的开发流程。

简单说：**Superpowers 是一套让 AI 稳定输出高质量代码的"操作手册"**。

### 核心理念

| 理念 | 含义 |
|------|------|
| **测试先行** | 先写测试，再写代码，让 AI 看到测试失败 |
| **系统化而非临时** | 流程固化，不是每次靠运气 |
| **简化复杂性** | 最小化实现，通过小步迭代达成目标 |
| **用证据说话** | 验证通过才算完成，不靠"我觉得可以" |

---

## 支持的平台

| IDE / 工具 | 安装命令 | 难度 |
|-------------|----------|------|
| **Claude Code**（推荐） | `/plugin install superpowers@superpowers-marketplace` | ⭐ 简单 |
| Cursor | `/add-plugin superpowers` | ⭐ 简单 |
| Codex | Fetch `.codex/INSTALL.md` | ⭐⭐ 中等 |
| Gemini CLI | `gemini extensions install https://github.com/obra/superpowers` | ⭐⭐ 中等 |
| OpenCode | Fetch `.opencode/INSTALL.md` | ⭐⭐ 中等 |

---

## 安装步骤（Claude Code）

### 1. 添加插件市场

在 Claude Code 中执行：

```
/plugin marketplace add obra/superpowers-marketplace
```

**预期输出**：

```
Adding marketplace...
SSH not configured, cloning via HTTPS: https://github.com/obra/superpowers-marketplace.git
✔ Successfully added marketplace: superpowers-marketplace
```

### 2. 安装核心技能包

```
/plugin install superpowers@superpowers-marketplace
```

**预期输出**：

```
Installing plugin "superpowers@superpowers-marketplace"...
✔ Successfully installed plugin: superpowers@superpowers-marketplace (scope: user)
```

### 3. 其他平台安装

#### Cursor

```
/add-plugin superpowers
```

#### Gemini CLI

```bash
gemini extensions install https://github.com/obra/superpowers
gemini extensions update superpowers
```

#### Codex / OpenCode

请访问仓库获取对应平台的安装文件：

- Codex: `.codex/INSTALL.md`
- OpenCode: `.opencode/INSTALL.md`

---

## 验证安装

**重要**：安装完成后，需要**开启新会话**才能加载插件。

在新会话中输入：

```
帮我规划这个功能：用户登录系统
```

**预期行为**：AI 自动调用 `brainstorming` 和 `writing-plans` 技能，出现类似输出：

```
我正在使用 brainstorming 技能...
在开始之前，我需要了解一下项目背景。
你的项目是 Web 应用、CLI 工具还是 API 服务？
```

如果没有自动调用技能，尝试：

1. 确认插件安装成功：执行 `/plugin list` 查看已安装插件列表
2. 开启一个全新的会话（关闭当前会话，重新打开）
3. 重启 Claude Code

---

## 快速体验

安装成功后，尝试以下对话：

### 对话 1：规划功能

```
你：帮我规划这个功能：用户登录系统
AI：我正在使用 brainstorming 技能...
    在开始之前，我需要了解一下项目背景。
    你的项目是 Web 应用、CLI 工具还是 API 服务？
```

### 对话 2：调试问题

```
你：登录功能有个 Bug，输入正确密码也报"密码错误"
AI：我正在使用 systematic-debugging 技能...
    让我们系统化地追踪问题根源...
```

这些自动调用的技能就是 Superpowers 的核心价值所在。

---

## 下一步

安装完成后，继续阅读 **[第 2 篇：核心工作流详解](02-core-workflow.md)**，深入理解 Superpowers 的 7 步工作流。

或者直接动手试试：

```
帮我规划一个待办事项应用
```
