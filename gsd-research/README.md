# GSD 研究图表

## 概述

本目录包含两张 PlantUML 图表，用于可视化 GSD (Get Shit Done) 的原理和使用方法。

## 文件列表

| 文件 | 说明 |
|------|------|
| [01-GSD-Principle.puml](gsd-research/01-GSD-Principle.puml) | GSD 原理图源代码 |
| [01-GSD-Principle-v2.puml](gsd-research/01-GSD-Principle-v2.puml) | GSD 原理图（优化版） |
| [02-GSD-How-To-Use.puml](gsd-research/02-GSD-How-To-Use.puml) | GSD 使用流程图源代码 |
| [02-GSD-How-To-Use-v2.puml](gsd-research/02-GSD-How-To-Use-v2.puml) | GSD 使用流程图（优化版） |
| [GSD-Principle.png](gsd-research/GSD-Principle.png) | **一张图看懂 GSD 原理** |
| [GSD-How-To-Use.png](gsd-research/GSD-How-To-Use.png) | **一张图看懂 GSD 如何使用** |
| [GSD-Principle.svg](gsd-research/GSD-Principle.svg) | 矢量版本（原理） |
| [GSD-How-To-Use.svg](gsd-research/GSD-How-To-Use.svg) | 矢量版本（使用） |

## 图表说明

### 图1: GSD 原理

展示 GSD 的核心价值体系：

```
核心问题 → 解决方案 → 核心价值 → 开发哲学
```

**核心问题**（粉红色）：
- AI 生成代码与预期不符
- 每次会话上下文丢失
- 变更原因无法追溯
- 团队协作困难重重

**解决方案**（绿色）：
- 规格优先，先定规格再写代码
- 上下文持久化，规格存入仓库
- 变更追踪，spec delta 可追溯
- 团队共享，规格即文档

**核心价值**（蓝色）：
- 规格与代码共存于仓库
- AI 每次都知道要做什么
- 需求变更清晰可见
- 30+ AI助手原生支持

**开发哲学**（黄色）：
- 流动而非僵化 (Fluid not rigid)
- 迭代而非瀑布 (Iterative not waterfall)
- 简单而非复杂 (Easy not complex)
- 棕地+绿地 (Brownfield+Greenfield)

### 图2: GSD 使用流程

展示 OpenSpec 的完整工作流：

```
用户提出想法 → AI brainstorming → 设计确认 → 创建提案 → 文档生成 → 执行任务 → 验证归档
```

**关键斜杠命令**：
- `/opsx:propose` - 创建提案
- `/opsx:apply` - 执行任务
- `/opsx:verify` - 验证变更
- `/opsx:archive` - 归档完成

**适用 AI 助手**：Claude Code, Cursor, Windsurf, Gemini CLI, GitHub Copilot 等 30+

## 重新生成图表

```bash
cd gsd-research
plantuml -o . *.puml
```

## 技术栈

- PlantUML 1.2026.2
- Graphviz (dot) 14.1.4
- Java Runtime (OpenJDK)
