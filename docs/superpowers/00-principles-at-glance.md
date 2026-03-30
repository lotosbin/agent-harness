# 一张图看懂 Superpowers 原理
```plantuml
@startuml
skinparam backgroundColor #1E1E1E
skinparam titleBackgroundColor #0066CC
skinparam titleFontColor #FFFFFF
skinparam componentStyle rectangle
title Superpowers 核心理念
rectangle "Superpowers" as SP #0066CC
card "测试先行
Write Tests First" as TDD #FF6B6B
card "系统化流程
Systematic Process" as SYS #4ECDC4
card "证据说话
Evidence Over Claims" as EOC #FFE66D
SP -- TDD
SP -- SYS
SP -- EOC
note bottom of SP
Superpowers 是一套让 AI 稳定输出
高质量代码的"操作手册"
end note
@enduml
```
---
```plantuml
@startuml
skinparam backgroundColor #FEFEFE
skinparam defaultTextAlignment center
title Superpowers 7 步工作流
|步骤|
start
:1. 想法;
note right: Idea
|#E8F4FD|步骤|
:2. 头脑风暴;
note right: Brainstorming
苏格拉底式提问
|#E8F4FD|步骤|
:3. 设计确认;
note right: Design Review
确认后再实现
|#E8F4FD|步骤|
:4. 工作区;
note right: Git Worktree
隔离环境
|#E8F4FD|步骤|
:5. 任务规划;
note right: Writing Plans
2-5 分钟原则
|#E8F4FD|步骤|
:6. TDD 开发;
note right: Test-Driven
红绿重构循环
|#E8F4FD|步骤|
:7. 代码审查;
note right: Code Review
严重程度分级
|#E8F4FD|步骤|
:8. 完成合并;
note right: Finish Branch
验证后合并
|#CCFFCC|结果|
:功能完成;
stop
@enduml
```
---
```plantuml
@startuml
skinparam backgroundColor #FEFEFE
title TDD 红绿重构循环
skinparam state {
  BackgroundColor #FFFFFF
  BorderColor #333333
  FontColor #333333
}
state RED : RED（红）
写失败的测试
state VERIFY_FAIL : 验证失败
确认是预期失败
state GREEN : GREEN（绿）
写最小实现
state VERIFY_PASS : 验证通过
所有测试绿
state REFACTOR : REFACTOR
重构优化
[*] --> RED
RED --> VERIFY_FAIL
VERIFY_FAIL --> GREEN : 失败 ✓
VERIFY_FAIL -down-> RED : 通过 ✗
GREEN --> VERIFY_PASS
VERIFY_PASS --> REFACTOR : 通过 ✓
VERIFY_PASS -down-> GREEN : 失败 ✗
REFACTOR --> VERIFY_PASS
note right of RED
铁律：没有先失败的测试
就不能写生产代码
end note
@enduml
```
---
```plantuml
@startuml
skinparam backgroundColor #FEFEFE
skinparam style strictuml
title Superpowers 解决问题
top to bottom direction
rectangle "AI 缺陷" #FFCCCC width 200 {
  card "❌ 不可靠
同一问题不同答案" as D1
  card "❌ 健忘症
每次对话丢失上下文" as D2
  card "❌ 无纪律
倾向于快速搞定" as D3
  card "❌ 难协作
团队难以接手" as D4
  card "❌ 难追踪
出现问题找不到原因" as D5
}
rectangle "Superpowers 解法" #CCFFCC width 200 {
  card "✅ 强制 TDD
先写测试再写代码" as S1
  card "✅ 设计文档
持久化保存上下文" as S2
  card "✅ 流程约束
每步必须验证" as S3
  card "✅ 团队可读
文档可传承" as S4
  card "✅ Git 历史
完整可追溯" as S5
}
D1 --> S1
D2 --> S2
D3 --> S3
D4 --> S4
D5 --> S5
@enduml
```
---
```
想法 ──▶ 头脑风暴 ──▶ 设计 ──▶ 任务规划 ──▶ TDD开发 ──▶ 代码审查 ──▶ 完成
         (提问)       (确认)    (拆分)        (测试)       (检查)      (合并)
```
**一句话理解**：用流程约束 AI 行为，让每一步都有验证。
---
```plantuml
@startuml
skinparam backgroundColor #1E1E1E
skinparam titleBackgroundColor #FF6B6B
skinparam titleFontColor #FFFFFF
skinparam componentStyle rectangle
title Superpowers 铁律
card "1. 没有失败的测试
就不写代码" as R1 #FF6B6B
card "2. 没有设计文档
就不写代码" as R2 #4ECDC4
card "3. 没有任务规划
就不写代码" as R3 #FFE66D
card "4. 没有代码审查
就不合并" as R4 #9B59B6
card "5. 没有验证通过
就不宣布完成" as R5 #3498DB
note bottom of R5
违反铁律 = 违反 TDD 精神
end note
@enduml
```
