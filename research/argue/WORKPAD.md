## Workpad

### YUA-21: 调研 argue（Rework Run 2）

**Issue:** YUA-21 — feat: 调研 https://github.com/onevcat/argue/blob/master/README_CN.md
**State:** implement
**Branch:** `yua-21-argue-research`
**PR:** #14 https://github.com/lotosbin/agent-harness/pull/14

#### 调研产出（已确认存在）

- `research/argue/report.md` — 完整研究报告（因果体用 + 洞见结构）
- `research/argue/getting-started.md` — 入门指南
- `research/argue/overview-diagram.md` — 一张图看懂使用
- `research/argue/architecture-diagram.md` — 一张图看懂原理

#### 调研结论

- argue 是多 Agent 编排层，而非又一个 coding agent
- 与 Claude Code 深度集成（skill 安装 + CLI provider + Hook）
- 三阶段辩论流程：Initial → Debate → Final Vote
- 同行评审评分：正确性 35%、完整性 25%、可操作性 25%、一致性 15%
- 纯本地 viewer，报告数据不离开本地

#### 状态

- 分支已推送至 origin ✅
- PR #14 已存在 ✅
- GitHub API 当前不可达（`error connecting to api.github.com`）
- 内容完整，未见 review comments
- 等待网络恢复或人工确认

#### 质量检查

本项目为纯 Markdown 项目，无 type-check / lint / test 配置。