# 一张图看懂 Superpowers 如何使用
```mermaid
flowchart LR
    A["步骤 1<br>添加插件市场"] --> B["步骤 2<br>安装核心技能包"]
    B --> C["步骤 3<br>开启新会话验证"]
    C --> D["✅ 完成<br>AI 自动调用技能"]
    style A fill:#E8F4FD
    style B fill:#E8F4FD
    style C fill:#E8F4FD
    style D fill:#CCFFCC
```
> 安装命令：
> ```
> /plugin marketplace add obra/superpowers-marketplace
> /plugin install superpowers@superpowers-marketplace
> ```
---
```mermaid
flowchart LR
    A["输入：帮我规划这个功能：用户登录系统"] --> B["AI 自动调用<br>brainstorming + writing-plans"]
    B --> C["我正在使用 brainstorming 技能..."]
    style A fill:#E8F4FD
    style B fill:#E8F4FD
    style C fill:#E8F4FD
```
> AI 会问：「你的项目是 Web 应用、CLI 工具还是 API 服务？」
---
```mermaid
flowchart TD
    A["1. 头脑风暴<br>描述需求 → AI 提问 → 确认设计"] --> B["2. 任务规划<br>AI 生成 2-5 分钟的任务"]
    B --> C["3. TDD 开发<br>RED → GREEN → REFACTOR"]
    C --> D["4. 代码审查<br>检查设计符合度"]
    D --> E["5. 完成<br>最终验证 → 合并"]
    style A fill:#E8F4FD
    style B fill:#E8F4FD
    style C fill:#E8F4FD
    style D fill:#E8F4FD
    style E fill:#E8F4FD
```
> TDD 每步：1. 写测试 → 2. 运行（失败）→ 3. 写实现 → 4. 运行（通过）→ 5. 提交
---
```mermaid
stateDiagram-v2
    [*] --> RED
    RED --> GREEN : 失败 ✓
    RED --> RED : 测试通过 ✗
    GREEN --> VERIFY : 运行测试
    VERIFY --> REFACTOR : 通过 ✓
    VERIFY --> GREEN : 失败 ✗
    REFACTOR --> VERIFY
    note right of RED
    铁律：没有先失败的测试
    就不能写生产代码
    end note
    note right of GREEN
    最小实现
    只让测试通过
    end note
```
---
| 场景 | 操作 | 触发技能 |
|------|------|----------|
| 新功能开发 | 帮我规划这个功能：xxx | brainstorming + writing-plans |
| Bug 修复 | 帮我修这个 Bug：xxx | systematic-debugging |
| 代码审查 | 这个代码审查一下 | requesting-code-review |
| 验证完成 | 可以合并了 | verification-before-completion |
| 并行任务 | 同时实现这几个功能 | dispatching-parallel-agents |
---
| 场景 | 操作 | AI 自动做什么 |
|------|------|--------------|
| 新功能开发 | 描述需求 | brainstorming → writing-plans |
| 遇到 Bug | 描述问题 | systematic-debugging |
| 并行任务 | 让 AI 并行处理 | dispatching-parallel-agents |
| 验证完成 | 说"可以合并了" | verification-before-completion |
---
```
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
/plugin list
```
- 帮我规划这个功能：xxx
- 帮我修这个 Bug：xxx
- 这个代码审查一下
- 可以合并了
---
| 技能 | 触发方式 |
|------|----------|
| brainstorming | "帮我规划..."、"我想加..." |
| writing-plans | 设计确认后自动 |
| systematic-debugging | "修 Bug"、"出问题了" |
| requesting-code-review | 任务完成后自动 |
| verification-before-completion | "完成"、"合并" |
