# 一张图看懂 Superpowers 原理

## 核心理念

```plantuml
@startuml
skinparam backgroundColor #1E1E1E
skinparam titleBackgroundColor #0066CC
skinparam titleFontColor #FFFFFF
skinparam componentStyle rectangle

title Superpowers 核心理念

rectangle "Superpowers" as SP #0066CC

card "测试先行\nWrite Tests First" as TDD #FF6B6B
card "系统化流程\nSystematic Process" as SYS #4ECDC4
card "证据说话\nEvidence Over Claims" as EOC #FFE66D

SP -- TDD
SP -- SYS
SP -- EOC

note bottom of SP
Superpowers 是一套让 AI 稳定输出\n高质量代码的"操作手册"
end note

@enduml
```

---

## 核心流程

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
note right: Brainstorming\n苏格拉底式提问

|#E8F4FD|步骤|
:3. 设计确认;
note right: Design Review\n确认后再实现

|#E8F4FD|步骤|
:4. 工作区;
note right: Git Worktree\n隔离环境

|#E8F4FD|步骤|
:5. 任务规划;
note right: Writing Plans\n2-5 分钟原则

|#E8F4FD|步骤|
:6. TDD 开发;
note right: Test-Driven\n红绿重构循环

|#E8F4FD|步骤|
:7. 代码审查;
note right: Code Review\n严重程度分级

|#E8F4FD|步骤|
:8. 完成合并;
note right: Finish Branch\n验证后合并

|#CCFFCC|结果|
:功能完成;
stop

@enduml
```

---

## TDD 红绿重构

```plantuml
@startuml
skinparam backgroundColor #FEFEFE

title TDD 红绿重构循环

skinparam state {
  BackgroundColor #FFFFFF
  BorderColor #333333
  FontColor #333333
}

state RED : RED（红）\n写失败的测试
state VERIFY_FAIL : 验证失败\n确认是预期失败
state GREEN : GREEN（绿）\n写最小实现
state VERIFY_PASS : 验证通过\n所有测试绿
state REFACTOR : REFACTOR\n重构优化

[*] --> RED
RED --> VERIFY_FAIL
VERIFY_FAIL --> GREEN : 失败 ✓
VERIFY_FAIL -down-> RED : 通过 ✗
GREEN --> VERIFY_PASS
VERIFY_PASS --> REFACTOR : 通过 ✓
VERIFY_PASS -down-> GREEN : 失败 ✗
REFACTOR --> VERIFY_PASS

note right of RED
**铁律：没有先失败的测试\n就不能写生产代码**
end note

@enduml
```

---

## 解决问题

```plantuml
@startuml
skinparam backgroundColor #FEFEFE
skinparam style strictuml

title Superpowers 解决问题

top to bottom direction

rectangle "AI 缺陷" #FFCCCC width 200 {
  card "❌ 不可靠\n同一问题不同答案" as D1
  card "❌ 健忘症\n每次对话丢失上下文" as D2
  card "❌ 无纪律\n倾向于快速搞定" as D3
  card "❌ 难协作\n团队难以接手" as D4
  card "❌ 难追踪\n出现问题找不到原因" as D5
}

rectangle "Superpowers 解法" #CCFFCC width 200 {
  card "✅ 强制 TDD\n先写测试再写代码" as S1
  card "✅ 设计文档\n持久化保存上下文" as S2
  card "✅ 流程约束\n每步必须验证" as S3
  card "✅ 团队可读\n文档可传承" as S4
  card "✅ Git 历史\n完整可追溯" as S5
}

D1 --> S1
D2 --> S2
D3 --> S3
D4 --> S4
D5 --> S5

@enduml
```

---

## 简化版：一目了然

```
想法 ──▶ 头脑风暴 ──▶ 设计 ──▶ 任务规划 ──▶ TDD开发 ──▶ 代码审查 ──▶ 完成
         (提问)       (确认)    (拆分)        (测试)       (检查)      (合并)
```

**一句话理解**：用流程约束 AI 行为，让每一步都有验证。

---

## 核心原则速记

```plantuml
@startuml
skinparam backgroundColor #1E1E1E
skinparam titleBackgroundColor #FF6B6B
skinparam titleFontColor #FFFFFF
skinparam componentStyle rectangle

title Superpowers 铁律

card "1. 没有失败的测试\n就不写代码" as R1 #FF6B6B
card "2. 没有设计文档\n就不写代码" as R2 #4ECDC4
card "3. 没有任务规划\n就不写代码" as R3 #FFE66D
card "4. 没有代码审查\n就不合并" as R4 #9B59B6
card "5. 没有验证通过\n就不宣布完成" as R5 #3498DB

note bottom of R5
违反铁律 = 违反 TDD 精神
end note

@enduml
```
