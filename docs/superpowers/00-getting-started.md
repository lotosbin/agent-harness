# Superpowers 入门指南：从问题到解决

> 用因果体结构理解为什么需要 Superpowers，以及它如何解决问题

---

## 因果链概览

```
问题（果） → 表面原因 → 深层原因 → 根本原因 → 解决方案 → 最终结果
```

---

## 第一层：问题现象

### 你是否遇到过这些情况？

| 问题 | 场景描述 | 发生频率 |
|------|----------|----------|
| 代码跑不起来 | AI 生成了一堆代码，运行时报错 | 每次 |
| Bug 越修越多 | 让 AI 修一个 Bug，结果引入三个新 Bug | 经常 |
| 上下文丢失 | 每次对话都要重新解释项目背景 | 每次 |
| 代码看不懂 | AI 写的代码自己都看不懂，更不敢交给团队 | 经常 |
| 重复造轮子 | 同样的功能，AI 换了个方式重复实现 | 经常 |

**如果你遇到过以上任意 2 个问题，请继续阅读。**

---

## 第二层：表面原因

### 人们通常以为是 AI 不够聪明

```plantuml
@startuml
skinparam backgroundColor #FEFEFE
skinparam handwritten false

title 表面原因：以为是 AI 不够聪明

rectangle "❌ 错觉 1" as A1 {
  card "GPT-5 不够强\n换个模型就好了"
}

rectangle "❌ 错觉 2" as A2 {
  card "Claude 不够好\n试试 Claude 4"
}

rectangle "❌ 错觉 3" as A3 {
  card "Cursor 更好用\n换 IDE"
}

A1 -[hidden]down-> A2
A2 -[hidden]down-> A3

note bottom of A3
但换了无数工具
问题依然存在
end note

@enduml
```

---

## 第三层：深层原因

### 真正的问题：AI 缺乏稳定的流程

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

title 深层原因：AI 缺乏流程约束

top to bottom direction

rectangle "问题现象" {
  card "代码跑不起来"
  card "Bug 越修越多"
  card "上下文丢失"
}

rectangle "表面原因" {
  card "AI 跳过测试"
  card "没有调试流程"
  card "没有设计文档"
}

rectangle "深层原因" {
  card "直接写实现"
  card "临时应对问题"
  card "没有任务规划"
}

"问题现象" -down-> "表面原因"
"表面原因" -down-> "深层原因"

note bottom of "深层原因"
**核心问题：AI 行为没有约束**
end note

@enduml
```

---

## 第四层：根本原因

### AI 的三大缺陷

```plantuml
@startuml
skinparam backgroundColor #1E1E1E
skinparam titleBackgroundColor #3A3A3A
skinparam titleFontColor #FFFFFF
skinparam componentStyle rectangle

title AI 的三大缺陷

card "1. 不可靠\n\n同一问题\n可能给出不同答案" as D1 #FF6B6B

card "2. 健忘症\n\n每次对话\n都是新上下文" as D2 #4ECDC4

card "3. 无纪律\n\n倾向于快速"搞定"\n而非正确做事" as D3 #FFE66D

note bottom of D3
**这三点决定了：没有流程约束的 AI 编程，就是一场赌博。**
end note

@enduml
```

---

## 第五层：解决方案

### Superpowers 的因果解法

```plantuml
@startuml
skinparam backgroundColor #FEFEFE
skinparam style strictuml

title Superpowers 的因果解法

top to bottom direction

rectangle "AI 缺陷" #FFCCCC {
  card "不可靠"
  card "健忘症"
  card "无纪律"
}

rectangle "Superpowers 解法" #CCFFCC {
  card "强制 TDD\n先写测试"
  card "设计文档\n持久化"
  card "流程约束\n7 步工作流"
}

rectangle "最终效果" #CCCCFF {
  card "每步验证"
  card "上下文延续"
  card "行为可预测"
}

"AI 缺陷" -down-> "Superpowers 解法"
"Superpowers 解法" -down-> "最终效果"

@enduml
```

---

## 第六层：7 步工作流

### 每一步都有约束

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

title Superpowers 7 步工作流

rectangle "1. 头脑风暴\nBrainstorming" as S1 #E8F4FD
rectangle "2. Git Worktree\n隔离工作区" as S2 #E8F4FD
rectangle "3. 任务规划\nWriting Plans" as S3 #E8F4FD
rectangle "4. Subagent 开发\n子 Agent 执行" as S4 #E8F4FD
rectangle "5. TDD 测试\n红绿重构" as S5 #E8F4FD
rectangle "6. 代码审查\nCode Review" as S6 #E8F4FD
rectangle "7. 完成分支\nFinish Branch" as S7 #E8F4FD

S1 --> S2
S2 --> S3
S3 --> S4
S4 --> S5
S5 --> S6
S6 --> S7

note right of S1
**约束：必须先设计\n不能直接写代码**
end note

note right of S3
**约束：必须拆分任务\n不能一口吃**
end note

note right of S5
**约束：必须先写测试\n不能跳过**
end note

note right of S6
**约束：必须检查问题\n不能盲目自信**
end note

@enduml
```

---

## 第七层：TDD 红绿重构

### 测试先行的核心循环

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

title TDD 红绿重构循环

state "RED\n写失败的测试" as RED #FFCCCC
state "验证失败" as VERIFY_RED #FFE6CC
state "GREEN\n写最小实现" as GREEN #CCFFCC
state "验证通过" as VERIFY_GREEN #CCE6FF
state "REFACTOR\n重构优化" as REFACTOR #CCCCFF

RED --> VERIFY_RED
VERIFY_RED --> GREEN : 测试失败\n符合预期
VERIFY_RED --> RED : 测试通过\n需要修复
GREEN --> VERIFY_GREEN
VERIFY_GREEN --> REFACTOR : 所有测试\n通过
VERIFY_GREEN --> GREEN : 测试失败\n需要修复
REFACTOR --> VERIFY_GREEN : 重构完成\n保持测试通过

note right of RED
**没有先失败的测试\n就不能写生产代码**
end note

@enduml
```

---

## 第八层：实际效果

### 效果对比

| 指标 | 无流程 AI | Superpowers |
|------|-----------|-------------|
| 代码质量 | 靠运气 | 流程保证 |
| Bug 率 | 高（3-5 个/功能） | 低（0-1 个/功能） |
| 上下文管理 | 每次丢失 | 持久化保存 |
| 团队协作 | 难以交接 | 文档可传承 |
| 调试效率 | 1 小时+/Bug | 10 分钟/Bug |

### 开发时间对比

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

title 无流程 AI vs Superpowers 开发流程

left to right direction

rectangle "无流程 AI" #FFCCCC {
  card "需求：加个登录功能" as A1
  card "AI 生成 500 行代码" as A2
  card "运行报错" as A3
  card "让 AI 修" as A4
  card "引入新 Bug" as A5
  card "继续修..." as A6
  card "2 小时后：\n代码自己都看不懂" as A7
}

rectangle "Superpowers" #CCFFCC {
  card "需求：加个登录功能" as B1
  card "头脑风暴：明确需求" as B2
  card "设计文档：确定方案" as B3
  card "任务规划：\n拆分为 5 个小任务" as B4
  card "TDD 开发：\n每步测试通过" as B5
  card "代码审查：\n发现并修复问题" as B6
  card "1.5 小时后：\n功能完整\n测试覆盖\n代码可维护" as B7
}

@enduml
```

---

## 第九层：行动召唤

### 立即开始

**Step 1：安装（3 分钟）**

```
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

**Step 2：验证（1 分钟）**

开启新会话，输入：
```
帮我规划这个功能：待办事项列表
```

**Step 3：观察**

观察 AI 是否自动调用 `brainstorming` 和 `writing-plans` 技能。

---

### 你会得到

```
✅ 一个经过设计的功能方案
✅ 一个可执行的实施计划
✅ 每步都有测试保护的代码
✅ 可审查、可维护的最终结果
```

---

## 常见误区

| 误区 | 真相 |
|------|------|
| Superpowers 会让 AI 变慢 | 前期多花时间，但调试时间大幅减少 |
| 只有大项目才需要 | 小项目更需要流程约束 |
| 学会了就不需要 | Superpowers 让 AI 遵循流程，流程本身就是价值 |

---

## 下一步

**免费系列教程**：

1. [第 1 篇：安装与验证](01-installation.md)
2. [第 2 篇：核心工作流详解](02-core-workflow.md)
3. [第 3 篇：实战案例](03-real-world-example.md)
4. [第 4 篇：进阶技能与团队协作](04-advanced-teams.md)

---

*「让 AI 编程从碰运气，变成稳定输出」——这是 Superpowers 的承诺。*
