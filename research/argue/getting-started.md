# argue 入门指南

## 安装

### 方式一：作为 Claude Code Skill 安装（推荐）

```bash
npx skills add https://github.com/onevcat/argue --skill argue
```

安装后直接用自然语言驱动辩论：

```
"让 argue 讨论一下 X"
"帮我问一下第二意见"
```

### 方式二：CLI 全局安装

```bash
npm install -g @onevcat/argue-cli
```

## 快速配置

### 1. 初始化配置

```bash
argue config init
# 创建配置文件 ~/.config/argue/config.json
```

### 2. 添加 Agent Provider

```bash
# 添加 Claude
argue config add-provider \
  --id claude \
  --type cli \
  --cli-type claude \
  --model-id sonnet \
  --agent claude-agent

# 添加 Codex
argue config add-provider \
  --id codex \
  --type cli \
  --cli-type codex \
  --model-id gpt-5.3-codex \
  --agent codex-agent
```

配置文件示例 (`~/.config/argue/config.json`)：

```json
{
  "providers": {
    "claude": {
      "type": "cli",
      "cliType": "claude",
      "models": {
        "sonnet": {
          "agent": "claude-agent"
        }
      }
    },
    "codex": {
      "type": "cli",
      "cliType": "codex",
      "models": {
        "gpt-5.3-codex": {
          "agent": "codex-agent"
        }
      }
    }
  },
  "agents": [
    { "id": "claude-agent", "provider": "claude", "model": "sonnet" },
    { "id": "codex-agent", "provider": "codex", "model": "gpt-5.3-codex" }
  ]
}
```

## 运行辩论

### 基础用法

```bash
argue run --task "微服务架构应该用 monorepo 还是 polyrepo？"
```

### 实时查看推理过程

```bash
argue run --task "微服务架构应该用 monorepo 还是 polyrepo？" --verbose
```

### 带后续 Action（自动执行）

```bash
argue run \
  --task "研究这个 issue 的解法：https://github.com/xxx/issues/22" \
  --action "根据讨论结果，实际解决这个 issue，开 PR" \
  --verbose
```

### 查看报告

```bash
argue view                  # 打开最近一次运行的报告
argue view <request-id>     # 打开指定运行
argue run --view            # 运行完成后自动打开
```

## 常用参数参考

| 参数 | 说明 | 示例 |
|------|------|------|
| `--task` | 辩论主题 | `--task "技术选型问题"` |
| `--agents` | 指定参与 Agent | `--agents claude-agent,codex-agent` |
| `--min-rounds` | 最少辩论轮数 | `--min-rounds 2` |
| `--max-rounds` | 最多辩论轮数 | `--max-rounds 5` |
| `--threshold` | 共识阈值（1.0=全票） | `--threshold 0.67` |
| `--verbose` | 实时显示推理过程 | `--verbose` |
| `--view` | 运行后打开报告 | `--view` |
| `--action` | 共识后的后续操作 | `--action "修复它"` |
| `--input` | 从 JSON 文件读取任务 | `--input task.json` |

## 配置文件查找顺序

1. `--config <path>` 命令行参数
2. `./argue.config.json`（项目本地）
3. `~/.config/argue/config.json`（全局）

## 与 Claude Code Hook 集成

在 `.claude/settings.json` 中添加 pre-commit 审查：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "node ./hooks/argue-review.mjs \"$TASK_INPUT\""
          }
        ]
      }
    ]
  }
}
```

## 作为库使用

```bash
npm install @onevcat/argue
```

```ts
import type { AgentTaskDelegate } from "@onevcat/argue";
import { ArgueEngine, MemorySessionStore, DefaultWaitCoordinator } from "@onevcat/argue";

const delegate: AgentTaskDelegate = {
  async dispatch(task) {
    const taskId = await myAgentFramework.submit(task);
    return { taskId, participantId: task.participantId, kind: task.kind };
  },
  async awaitResult(taskId, timeoutMs) {
    const result = await myAgentFramework.waitFor(taskId, timeoutMs);
    return { ok: true, output: result };
  }
};

const engine = new ArgueEngine({
  taskDelegate: delegate,
  sessionStore: new MemorySessionStore(),
  waitCoordinator: new DefaultWaitCoordinator(delegate)
});

const result = await engine.start({
  requestId: "review-42",
  task: "审查 PR #42 的安全性和正确性问题",
  participants: [
    { id: "security-agent", role: "security-reviewer" },
    { id: "arch-agent", role: "architecture-reviewer" }
  ],
  roundPolicy: { minRounds: 2, maxRounds: 4 },
  consensusPolicy: { threshold: 0.67 }
});

// result.status → "consensus" | "partial_consensus" | "unresolved" | "interrupted" | "failed"
```