# argue 研究报告

## 一、因：为何存在

**argue** 是一个结构化的多 Agent 辩论引擎，让多个 AI Agent 独立分析同一问题、跨轮次互相质疑彼此的主张，最终通过投票达成共识——产出比任何单一 Agent 更高质量的结果。

**背景脉络**：在使用 AI coding agent 时，单个 agent 容易出现幻觉、视角单一、缺乏交叉验证等问题。传统的解决方案是让人工审查，但这成为了自动化的瓶颈。argue 的出现填补了这一空白——用多个 Agent 互相辩论来替代人工审查，实现自动化的多角度审视和质量提升。

## 二、果：带来的改变

### 2.1 核心价值

- **更高质量输出**：通过交叉质疑和共识机制，显著减少幻觉，提升结论的严谨性
- **透明可追溯**：每条主张的来源、判断过程、投票结果全程记录
- **可嵌入架构**：既可 CLI 使用，也可作为库嵌入任何系统
- **自动化后续行动**：共识达成后，代表 Agent 可执行真实世界的操作

### 2.2 核心功能

| 功能 | 说明 |
|------|------|
| **多 Agent 辩论** | 支持多个 Agent 同时参与，跨轮次互相质疑 |
| **主张合并** | 自动检测并合并重复主张，避免冗余 |
| **共识计算** | 可配置阈值（默认全票），自动计算每条主张的共识程度 |
| **同行评审评分** | 正确性 35%、完整性 25%、可操作性 25%、一致性 15% |
| **代表报告生成** | 得分最高的 Agent 撰写最终报告 |
| **可视化报告** | 纯前端 viewer，数据完全不离开本地 |
| **Agent 淘汰机制** | 超时或出错的 Agent 被移除，共识分母自动调整 |
| **可选 Action** | 代表 Agent 达成共识后可执行真实操作（如开 PR） |

## 三、体：架构与设计

### 3.1 技术栈

```
├── packages/
│   ├── argue/           # 核心辩论引擎库（@onevcat/argue）
│   ├── argue-cli/       # 命令行工具（@onevcat/argue-cli）
│   └── argue-viewer/    # Web 可视化报告页面
└── skills/
    └── argue/           # Claude Code agent skill
```

- **语言**：TypeScript（98%+）
- **许可证**：MIT
- **版本**：0.5.0（2026 年）
- **平台**：macOS、Linux、Windows
- **Stars**：220（截至 2026-05-09）
- **作者**：onevcat（王国龙，Knight 喵神，知名 iOS/Swift 开源作者）

### 3.2 辩论流程架构

```
+------+      +--------+       +---------+       +---------+
| Host |      | Engine |       | Agent A |       | Agent B |
+------+      +--------+       +---------+       +---------+
   |              |                |                 |
   |  start()     |                |                 |
   |------------->                |                 |
   |              |                |                 |
   |              |    +-------------------+        |
   |              |    | Round 0: Initial   |        |
   |              |    +-------------------+        |
   |              |                |                 |
   |              |  dispatch(initial)              |
   |              |---------------------------->    |
   |              |              dispatch(initial)  |
   |              |--------------------------------->
   |              |    claims        |              |
   |              |<...............................|
   |              |                claims          |
   |              |<..................................|
   |              |                |                 |
   |              |   +---------------------+        |
   |              |   | Round 1..N: Debate  |        |
   |              |   +---------------------+        |
   |              |                |                 |
   |              |  dispatch(debate + peer ctx)   |
   |              |---------------------------->    |
   |              |         dispatch(debate + ctx)  |
   |              |--------------------------------->
   |              |   judgements, merges            |
   |              |<...............................|
   |              |               judgements, merges|
   |              |<..................................|
   |              |                |                 |
   |              |    +------------------------+   |
   |              |    | Round N+1: Final Vote  |   |
   |              |    +------------------------+   |
   |              |                |                 |
   |              |  dispatch(final_vote)            |
   |              |---------------------------->    |
   |              |           dispatch(final_vote)  |
   |              |--------------------------------->
   |              |  accept/reject per claim        |
   |              |<...............................|
   |              |              accept/reject      |
   |              |<..................................|
   |              |                |                 |
   |              |  consensus + scoring             |
   |              |                |                 |
   |              |     dispatch(report)            |
   |              |---------------------------->    |
   |              |    representative report       |
   |              |<...............................|
   |              |                |                 |
   |         ArgueResult           |                 |
   |<..............................|                 |
+------+      +--------+       +---------+       +---------+
```

### 3.3 三阶段详解

| 阶段 | Agent 行为 | 引擎行为 |
|------|-----------|---------|
| **Initial（Round 0）** | 提出主张（claims），对他人的主张做初步判断 | 收集所有主张进入共享池 |
| **Debate（Round 1..N）** | 互相判断（agree/disagree/revise），提出合并建议 | 合并重复主张，追踪立场变化，检测早期收敛 |
| **Final Vote（Round N+1）** | 对每条活跃主张投 accept/reject | 按阈值计算每条主张的共识 |

### 3.4 四种 Agent 接入方式

| 类型 | 适用场景 | 代表产品 | 推理参数传递 |
|------|---------|---------|------------|
| `cli` | 有 CLI 界面的 Coding Agent | Claude Code、Codex CLI、Copilot CLI、Gemini CLI | `claude` → `--effort`；`codex` → `model_reasoning_effort=`；`generic` → stdin envelope |
| `api` | 直连模型 API | OpenAI、Anthropic、Ollama | 暂不转发（预留字段） |
| `sdk` | 自定义 Agent 框架适配器 | 自研 SDK 集成 | 由用户控制 |
| `mock` | 测试和开发 | 确定性响应、模拟超时 | 不适用 |

## 四、用：使用场景与方式

### 4.1 主要使用场景

| 场景 | 说明 |
|------|------|
| **PR/Issue 多角度审查** | 让安全审查员、架构审查员、正确性审查员辩论式审查 |
| **技术决策评审** | 辩论 monorepo vs polyrepo、技术选型等架构决策 |
| **Agent 自我纠错** | 通过交叉质疑减少单个 Agent 的幻觉 |
| **报告自动生成** | 代表 Agent 基于共识产出结构化结论报告 |
| **自动化行动触发** | 代表 Agent 执行真实操作（如开 PR、修 bug） |

### 4.2 安装与配置

```bash
# 作为 CLI 使用
npm install -g @onevcat/argue-cli

# 初始化配置
argue config init

# 添加 provider 和 agent
argue config add-provider --id claude --type cli --cli-type claude --model-id sonnet --agent claude-agent
argue config add-provider --id codex --type cli --cli-type codex --model-id gpt-5.3-codex --agent codex-agent
```

### 4.3 运行辩论

```bash
# 基础用法
argue run --task "微服务架构应该用 monorepo 还是 polyrepo？"

# 详细模式（实时查看推理过程）
argue run --task "微服务架构应该用 monorepo 还是 polyrepo？" --verbose

# 带后续 action
argue run \
  --task "研究这个 issue 的解法：https://github.com/xxx/issues/22" \
  --action "根据讨论结果，实际解决这个 issue，开 PR" \
  --verbose
```

### 4.4 常用参数

| 参数 | 说明 | 默认值 |
|------|------|------|
| `--agents a1,a2` | 从配置中选择特定 agent | 全部 |
| `--min-participants 2` | 继续辩论所需最少存活参与者数 | - |
| `--on-insufficient-participants interrupt` | 人数不足时 interrupt 或 fail | interrupt |
| `--min-rounds 2` | 最少辩论轮数 | 2 |
| `--max-rounds 5` | 辩论轮数上限 | 5 |
| `--threshold 0.67` | 共识阈值（1.0=全票通过） | 1.0 |
| `--action "Fix it"` | 辩论后由代表执行的操作 | - |
| `--verbose` | 实时显示每个 agent 的推理过程 | - |
| `--view` | 运行完成后自动打开报告 | - |

### 4.5 作为库使用

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
  consensusPolicy: { threshold: 0.67 },
  reportPolicy: { composer: "representative" },
  actionPolicy: { prompt: "修复所有发现的问题并发布总结评论。" }
});
// result.status → "consensus" | "partial_consensus" | "unresolved" | "interrupted" | "failed"
```

### 4.6 Claude Code Skill 集成

```bash
# 一键安装为 Claude Code skill
npx skills add https://github.com/onevcat/argue --skill argue

# 安装后直接用自然语言驱动
"让 argue 讨论一下 X"
"帮我问一下第二意见"
```

### 4.7 Claude Code Hook 示例

```jsonc
// .claude/settings.json
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

## 五、洞：深度洞察

### 5.1 与其他工具对比

| 维度 | argue | 人工审查 | 单 Agent 审查 | OpenSpec |
|------|-------|---------|-------------|---------|
| 自动化程度 | ✅ 全自动 | ❌ | ✅ 全自动 | ✅ 全自动 |
| 多角度交叉 | ✅ | ✅ | ❌ | ❌ |
| 共识量化 | ✅ | ❌ | ❌ | ❌ |
| 代表报告 | ✅ | ❌ | ❌ | ❌ |
| 后续 action | ✅ | ❌ | ❌ | ❌ |
| 报告可视化 | ✅ | ❌ | ❌ | ❌ |
| 嵌入系统 | ✅ | ❌ | ❌ | ❌ |

### 5.2 关键洞察

1. **定位独特**：argue 不是又一个 coding agent，而是一个**多 Agent 编排层**——它站在 Claude Code、Codex 等工具之上，通过辩论机制提升输出质量。

2. **质量保证机制**：通过同行评审评分（正确性 35%、完整性 25%、可操作性 25%、一致性 15%）和多轮辩论，显著降低幻觉率。

3. **与 Claude Code 深度整合**：既是 skill 安装、也支持 CLI provider 配置、还支持 Hook 触发，是当前 Claude Code 生态中最完整的辩论/审查方案。

4. **隐私设计**：报告数据完全在本地，viewer 是纯前端，数据不离开设备。

5. **可扩展性强**：通过 `AgentTaskDelegate` 接口可以接入任何 Agent 框架，不绑定特定 provider。

6. **版本成熟度**：v0.5.0，已有完整的 CLI、引擎、viewer，发布频率活跃（最后更新 2026-05-09），适合生产使用。

### 5.3 局限性与风险

- **Token 消耗较高**：多 Agent 辩论意味着多倍的 token 消耗（每个 Agent 每轮都需推理）
- **依赖外部 Agent**：CLI 模式下依赖 Claude Code、Codex 等外部 CLI 工具
- **中文资料少**：README_CN 之外缺乏中文文档和社区讨论
- **推理参数兼容**：reasoning 参数的传递依赖于各 provider 的实现细节，维护成本较高

## 六、资源索引

| 资源 | 链接 |
|------|------|
| GitHub | https://github.com/onevcat/argue |
| 在线 Demo | https://argue.onev.cat/example |
| NPM 核心库 | `@onevcat/argue` |
| NPM CLI | `@onevcat/argue-cli` |
| Skill 安装 | `npx skills add https://github.com/onevcat/argue --skill argue` |

### 主要 GitHub 仓库

- [onevcat/argue](https://github.com/onevcat/argue) — 主仓库（monorepo，含全部模块）
- [packages/argue](https://github.com/onevcat/argue/tree/master/packages/argue) — 核心引擎
- [packages/argue-cli](https://github.com/onevcat/argue/tree/master/packages/argue-cli) — CLI 工具
- [packages/argue-viewer](https://github.com/onevcat/argue/tree/master/packages/argue-viewer) — Web viewer