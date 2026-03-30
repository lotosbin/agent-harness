# 一张图看懂 Superpowers 原理
```mermaid
mindmap
  root((Superpowers))
    测试先行
      Write Tests First
    系统化流程
      Systematic Process
    证据说话
      Evidence Over Claims
```
> Superpowers 是一套让 AI 稳定输出高质量代码的"操作手册"
---
```mermaid
flowchart LR
    subgraph 想法
        I[想法]
    end
    subgraph 工作流
        A["1. 头脑风暴<br>Brainstorming"]
        B["2. 设计确认"]
        C["3. 任务规划<br>Writing Plans"]
        D["4. TDD 开发"]
        E["5. 代码审查"]
        F["6. 完成合并"]
    end
    I --> A --> B --> C --> D --> E --> F
    style I fill:#FFE66D
    style A fill:#E8F4FD
    style B fill:#E8F4FD
    style C fill:#E8F4FD
    style D fill:#E8F4FD
    style E fill:#E8F4FD
    style F fill:#E8F4FD
```
---
```mermaid
stateDiagram-v2
    [*] --> RED
    RED --> VERIFY_RED : 写失败测试
    VERIFY_RED --> GREEN : 失败 ✓
    VERIFY_RED --> RED : 测试通过 ✗
    GREEN --> VERIFY_GREEN : 写最小实现
    VERIFY_GREEN --> REFACTOR : 通过 ✓
    VERIFY_GREEN --> GREEN : 失败 ✗
    REFACTOR --> VERIFY_GREEN : 重构完成
    note right of RED
    铁律：没有先失败的测试
    就不能写生产代码
    end note
```
---
```mermaid
flowchart LR
    subgraph "AI 缺陷"
        D1["❌ 不可靠"]
        D2["❌ 健忘症"]
        D3["❌ 无纪律"]
        D4["❌ 难协作"]
        D5["❌ 难追踪"]
    end
    subgraph "Superpowers 解法"
        S1["✅ 强制 TDD"]
        S2["✅ 设计文档"]
        S3["✅ 流程约束"]
        S4["✅ 团队可读"]
        S5["✅ Git 历史"]
    end
    D1 --> S1
    D2 --> S2
    D3 --> S3
    D4 --> S4
    D5 --> S5
    style D1 fill:#FFCCCC
    style D2 fill:#FFCCCC
    style D3 fill:#FFCCCC
    style D4 fill:#FFCCCC
    style D5 fill:#FFCCCC
    style S1 fill:#CCFFCC
    style S2 fill:#CCFFCC
    style S3 fill:#CCFFCC
    style S4 fill:#CCFFCC
    style S5 fill:#CCFFCC
```
---
```
想法 ──▶ 头脑风暴 ──▶ 设计 ──▶ 任务规划 ──▶ TDD开发 ──▶ 代码审查 ──▶ 完成
         (提问)       (确认)    (拆分)        (测试)       (检查)      (合并)
```
**一句话理解**：用流程约束 AI 行为，让每一步都有验证。
---
| 铁律 | 说明 |
|------|------|
| 1. 没有失败的测试，就不写代码 | TDD 核心 |
| 2. 没有设计文档，就不写代码 | 先想清楚 |
| 3. 没有任务规划，就不写代码 | 小步快跑 |
| 4. 没有代码审查，就不合并 | 质量把控 |
| 5. 没有验证通过，就不宣布完成 | 证据说话 |
