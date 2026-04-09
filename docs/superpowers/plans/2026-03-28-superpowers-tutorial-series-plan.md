# Superpowers 系列教程实施计划

> **For agentic workers:** 建议使用 superpowers:subagent-driven-development 执行本计划，每篇文章作为一个 Task，每段作为 Step。

**Goal:** 编写 4 篇独立的 Superpowers 系列中文教程 + 1 个导航页，SEO 引流，免费系列 + 付费服务变现。

**Architecture:** 系列按难度递进设计：安装 → 原理 → 实战 → 进阶引流。每篇独立可读，内部相互引用。统一 Markdown 格式，中文写作，代码示例使用 Python/JavaScript。

**Tech Stack:** Markdown、Superpowers 技能框架、Superpowers 官方文档

---

## 文件结构

```
docs/superpowers/
├── README.md                      # 系列导航页
├── 01-installation.md             # 第1篇：安装与验证
├── 02-core-workflow.md            # 第2篇：核心工作流
├── 03-real-world-example.md       # 第3篇：实战案例
└── 04-advanced-teams.md          # 第4篇：进阶与团队
```

---

## Task 1: 创建目录结构与导航页

**Files:**
- Create: `docs/superpowers/README.md`
- Create: `docs/superpowers/01-installation.md` (空文件占位)
- Create: `docs/superpowers/02-core-workflow.md` (空文件占位)
- Create: `docs/superpowers/03-real-world-example.md` (空文件占位)
- Create: `docs/superpowers/04-advanced-teams.md` (空文件占位)

- [ ] **Step 1: 创建 superpowers 目录**

```bash
mkdir -p docs/superpowers
```

- [ ] **Step 2: 创建 5 个 Markdown 文件（含标题占位）**

文件 `docs/superpowers/README.md` 初始内容：

```markdown
# Superpowers 系列教程

> 让 AI 编程从碰运气，变成稳定输出

## 系列目录

1. [第 1 篇：安装与验证](01-installation.md) — 3 分钟快速上手
2. [第 2 篇：核心工作流详解](02-core-workflow.md) — 7 步工作流深度解析
3. [第 3 篇：实战案例](03-real-world-example.md) — 从想法到上线的完整演示
4. [第 4 篇：进阶技能与团队协作](04-advanced-teams.md) — 深入探索 + 付费服务

## 前置要求

- 安装 Claude Code 或其他支持的 IDE
- 基本了解 AI 编程助手概念

## 系列特色

- 完整可运行的代码示例
- 真实项目开发流程演示
- SEO 友好，独立可读
```

- [ ] **Step 3: 提交初始结构**

```bash
git add docs/superpowers/
git commit -m "docs: scaffold superpowers tutorial series structure"
```

---

## Task 2: 编写第 1 篇 — 安装与验证

**Files:**
- Modify: `docs/superpowers/01-installation.md`

- [ ] **Step 1: 编写开篇痛点共鸣**

```markdown
## 你是否遇到过这些困境？

- AI 生成了一堆代码，但跑不起来
- 让 AI 修 Bug，越修越多
- 每次对话都要从头解释项目背景
- AI 写的代码自己都看不懂，更不敢交给团队

**问题的根源不是 AI 不够聪明，而是缺少让 AI 稳定工作的流程。**
```

- [ ] **Step 2: 编写 Superpowers 定义与核心理念**

```markdown
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
```

- [ ] **Step 3: 编写支持平台一览表**

```markdown
## 支持的平台

| IDE / 工具 | 安装命令 | 难度 |
|-------------|----------|------|
| **Claude Code**（推荐） | `/plugin install superpowers@superpowers-marketplace` | ⭐ 简单 |
| Cursor | `/add-plugin superpowers` | ⭐ 简单 |
| Codex | Fetch `.codex/INSTALL.md` | ⭐⭐ 中等 |
| Gemini CLI | `gemini extensions install https://github.com/obra/superpowers` | ⭐⭐ 中等 |
| OpenCode | Fetch `.opencode/INSTALL.md` | ⭐⭐ 中等 |
```

- [ ] **Step 4: 编写 Claude Code 详细安装步骤**

```markdown
## 安装步骤（Claude Code）

### 1. 添加插件市场

在 Claude Code 中执行：

```
/plugin marketplace add obra/superpowers-marketplace
```

输出示例：
```
Adding marketplace...
✔ Successfully added marketplace: superpowers-marketplace
```

### 2. 安装核心技能包

```
/plugin install superpowers@superpowers-marketplace
```

输出示例：
```
Installing plugin "superpowers@superpowers-marketplace"...
✔ Successfully installed plugin: superpowers@superpowers-marketplace
```

### 3. 其他平台安装

其他平台请参考上表的安装命令。
```

- [ ] **Step 5: 编写验证安装成功的步骤**

```markdown
## 验证安装

开启新会话（新会话才能加载插件），输入：

```
帮我规划这个功能：用户登录系统
```

**预期行为**：AI 自动调用 `brainstorming` 和 `writing-plans` 技能，出现类似输出：

```
我正在使用 brainstorming 技能...
在开始之前，我需要了解一下项目背景...
```

如果没有自动调用技能，尝试：
1. 确认插件安装成功（`/plugin list` 查看）
2. 开启一个全新的会话
3. 重启 Claude Code
```

- [ ] **Step 6: 编写快速体验对话示例**

```markdown
## 快速体验

安装成功后，尝试以下对话：

### 对话 1：安装验证

```
你：帮我规划这个功能：用户登录系统
AI：我正在使用 brainstorming 技能...
    你的项目是 Web 应用、CLI 工具还是 API 服务？
```

### 对话 2：调试问题

```
你：登录功能有个 Bug，输入正确密码也报"密码错误"
AI：我正在使用 systematic-debugging 技能...
    让我们系统化地追踪问题根源...
```

这些自动调用的技能就是 Superpowers 的核心价值。
```

- [ ] **Step 7: 添加篇末钩子并更新 README 导航页**

在文末添加：

```markdown
---

## 下一步

安装完成后，继续阅读 **[第 2 篇：核心工作流详解](02-core-workflow.md)**，深入理解 Superpowers 的 7 步工作流。

或者直接动手试试：`帮我规划一个待办事项应用`
```

同时更新 `docs/superpowers/README.md`，确认第 1 篇链接正确。

- [ ] **Step 8: 提交第 1 篇**

```bash
git add docs/superpowers/01-installation.md docs/superpowers/README.md
git commit -m "docs: write tutorial part 1 - installation"
```

---

## Task 3: 编写第 2 篇 — 核心工作流详解

**Files:**
- Modify: `docs/superpowers/02-core-workflow.md`

- [ ] **Step 1: 编写工作流全景图**

```markdown
## 7 步工作流全景

```
想法 → 头脑风暴 → 设计评审 → 隔离工作区 → 任务规划 → 执行开发 → 代码审查 → 合并发布
```

每一步都有明确的输入、输出和验证标准，确保 AI 的每一步操作都可追踪、可审查。
```

- [ ] **Step 2: 编写 Step 1-2 详解**

```markdown
### Step 1：头脑风暴（Brainstorming）

**做什么**：AI 通过苏格拉底式提问帮你完善想法，直到你认可设计方案。

**关键点**：
- AI 会先了解项目背景（读取文件、分析代码）
- 一次只问一个问题
- 设计分章节展示，你需要逐节确认
- 全部确认后生成设计文档并提交到 git

**示例对话**：
```
你：我想给博客加个评论系统
AI：正在使用 brainstorming 技能...
AI：评论需要支持嵌套回复吗？
你：需要，最多三层
AI：回复是实时显示还是需要审核？
...
```

### Step 2：创建隔离工作区（Git Worktree）

**做什么**：为新功能创建独立的 git worktree，避免污染主分支。

**好处**：
- 与其他工作完全隔离
- 可以并行开发多个功能
- 出错不影响主分支
```

- [ ] **Step 3: 编写 Step 3-4 详解**

```markdown
### Step 3：编写实施计划（Writing Plans）

**做什么**：将任务分解为 2-5 分钟的微小步骤，每个步骤包含：

- 精确的文件路径
- 完整的代码示例
- 验证命令和预期输出

**关键原则**：每个任务足够小，能在 2-5 分钟内完成并验证。

### Step 4：Subagent 驱动开发

**做什么**：AI 为每个任务启动一个独立的子 Agent，完成后进行两阶段审查。

**优势**：
- 每个任务都是干净的上下文
- 两阶段审查确保质量
- 快速迭代，持续验证
```

- [ ] **Step 4: 编写 Step 5 TDD 详解（含代码）**

```markdown
### Step 5：测试驱动开发（TDD）

**做什么**：严格遵循红-绿-重构循环。

```
RED（红）：写一个失败的测试
GREEN（绿）：写最小代码让测试通过
REFACTOR（重构）：改善代码，保持测试通过
```

**铁律**：

> **没有先失败的测试，就不能写生产代码。**

**代码示例**：

```python
# RED：写测试
def test_user_login():
    result = login("admin", "wrong")
    assert result.error == "Invalid credentials"
```

```bash
# 运行测试，确认失败
$ pytest test_user_login.py
FAIL: expected 'Invalid credentials', got None
```

```python
# GREEN：最小实现
def login(username, password):
    if password != "correct_password":
        return {"error": "Invalid credentials"}
    return {"success": True}
```

```bash
# 运行测试，确认通过
$ pytest test_user_login.py
PASS
```
```

- [ ] **Step 5: 编写 Step 6-7 详解**

```markdown
### Step 6：代码审查（Requesting Code Review）

**做什么**：对照实施计划逐项检查，发现问题按严重程度分类报告。

**报告格式**：
```markdown
## 代码审查报告

### 严重问题（必须修复）
- ❌ 未处理空用户名的边界情况

### 建议改进（可选）
- 💡 可以将错误消息提取为常量

### 通过项
- ✅ 测试覆盖率符合要求
- ✅ 遵循项目代码风格
```

### Step 7：完成开发分支

**做什么**：最终验证，准备合并。

**合并选项**：
1. **Squash Merge**：保留干净的历史
2. **Merge Commit**：保留完整历史
3. **Rebase + Merge**：最线性的历史
```

- [ ] **Step 6: 编写 TDD 铁律深度解释**

```markdown
## 为什么"先写测试"这么重要？

### 常见误区

| 误区 | 真相 |
|------|------|
| "代码简单，不需要测试" | 简单代码也会 Bug，测试只需 30 秒 |
| "我手动测试过了" | 手动测试无法复现，不能防止回归 |
| "先写代码再补测试也一样" | 测试通过只能证明你记得测什么，无法发现遗漏 |

### TDD 的价值

1. **强制思考**：写测试前必须想清楚"期望什么行为"
2. **即时反馈**：每步都验证，出问题立即知道
3. **防止退化**：后续改动不会破坏已有功能
4. **活文档**：测试就是代码行为的说明书
```

- [ ] **Step 7: 添加篇末钩子并更新 README**

在文末添加：

```markdown
---

## 下一步

现在你理解了 Superpowers 的工作原理。继续阅读 **[第 3 篇：实战案例](03-real-world-example.md)**，看这些步骤如何在一个真实案例中协同工作。
```

更新 `docs/superpowers/README.md` 中第 2 篇链接。

- [ ] **Step 8: 提交第 2 篇**

```bash
git add docs/superpowers/02-core-workflow.md docs/superpowers/README.md
git commit -m "docs: write tutorial part 2 - core workflow"
```

---

## Task 4: 编写第 3 篇 — 实战案例：评论系统

**Files:**
- Modify: `docs/superpowers/03-real-world-example.md`

- [ ] **Step 1: 编写案例背景**

```markdown
## 案例背景

我们用 Superpowers 的方式，为一个博客系统开发评论功能。

**需求描述**：
- 用户可以对文章发表评论
- 评论支持最多三层嵌套回复
- 评论需要审核后才显示（可选开关）
- 提供基本的增删查 API

**技术栈**：Python + FastAPI + SQLite
```

- [ ] **Step 2: 编写头脑风暴对话节选**

```markdown
## Step 1：头脑风暴

### 对话节选

```
你：我想给博客加个评论系统
AI：我正在使用 brainstorming 技能...
    在开始之前，我需要了解一下项目背景。
    你的项目是 Web 应用、CLI 工具还是 API 服务？

你：FastAPI 写的博客后端 API
AI：评论需要支持嵌套回复吗？最多几层？

你：需要，最多三层
AI：回复是实时显示还是需要审核？

你：需要审核，管理员可以开关这个功能
AI：评论的数据需要持久化吗？还是纯内存？

你：SQLite 就够
AI：明白。最后一个问题：这个 API 需要认证吗？

你：暂时不需要，公开评论就行
AI：好的，我已经了解了需求。让我整理一下设计方案...
```

### 设计文档摘要

生成的设计文档包含：
- **数据模型**：`Comment(id, article_id, parent_id, author, content, status, created_at)`
- **API 端点**：`GET /articles/{id}/comments`、`POST /articles/{id}/comments`、`DELETE /comments/{id}`
- **核心逻辑**：嵌套层级限制、审核状态流转
```

- [ ] **Step 3: 编写任务规划输出示例**

```markdown
## Step 2：任务规划

设计确认后，AI 生成以下实施计划：

### Task 1: 数据模型

**文件：**
- 创建: `models/comment.py`
- 测试: `tests/models/test_comment.py`

- [ ] Step 1: 编写失败的测试
- [ ] Step 2: 运行测试，确认失败
- [ ] Step 3: 编写最小实现
- [ ] Step 4: 运行测试，确认通过
- [ ] Step 5: 提交代码

### Task 2: API 端点

**文件：**
- 创建: `api/comments.py`
- 测试: `tests/api/test_comments.py`

（类似 Task 1 的步骤）

### Task 3: 嵌套层级逻辑

（类似步骤）
```

- [ ] **Step 4: 编写 TDD 代码演示**

```markdown
## Step 3：TDD 代码演示

### Task 1: 数据模型完整代码

```python
# tests/models/test_comment.py
import pytest
from models.comment import Comment

def test_comment_creation():
    """评论可以正常创建"""
    comment = Comment(
        article_id=1,
        author="张三",
        content="这是一条评论"
    )
    assert comment.author == "张三"
    assert comment.content == "这是一条评论"
    assert comment.status == "pending"  # 默认待审核

def test_comment_nesting_limit():
    """嵌套层级超过限制时返回错误"""
    # 模拟已有的三层嵌套
    parent = Comment(article_id=1, content="第一层", nesting_level=3)
    child = Comment(article_id=1, content="第四层", parent_id=parent.id)
    assert child is None  # 或抛出异常
```

```python
# models/comment.py
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

MAX_NESTING_LEVEL = 3

@dataclass
class Comment:
    article_id: int
    author: str
    content: str
    parent_id: Optional[int] = None
    nesting_level: int = 1
    status: str = "pending"
    created_at: datetime = None

    def __post_init__(self):
        if self.nesting_level > MAX_NESTING_LEVEL:
            raise ValueError(f"嵌套层级不能超过 {MAX_NESTING_LEVEL}")
        if self.created_at is None:
            self.created_at = datetime.now()
```
```

- [ ] **Step 5: 编写代码审查报告示例**

```markdown
## Step 4：代码审查

### 审查报告

```markdown
## 代码审查报告 - Task 1: 数据模型

### 严重问题
- ❌ `Comment` 类未实现 `__repr__`，调试困难

### 建议改进
- 💡 可以加 `is_deleted` 软删除字段
- 💡 `nesting_level` 可考虑从 parent 自动计算

### 通过项
- ✅ 测试覆盖了核心场景
- ✅ 嵌套层级限制逻辑正确
- ✅ 使用 dataclass，代码简洁
```

修复严重问题后继续 Task 2。
```

- [ ] **Step 6: 编写避坑指南**

```markdown
## 常见陷阱与避坑指南

### 陷阱 1：跳过 TDD

**症状**：AI 直接写实现代码，不写测试
**后果**：后期 Bug 多，修改成本高
**避坑**：严格遵循"没有先失败的测试就不写代码"原则

### 陷阱 2：任务粒度太大

**症状**：一个任务包含 10+ 步骤
**后果**：中途出错难以定位，审查困难
**避坑**：每任务控制在 2-5 分钟，超过就拆分

### 陷阱 3：跳过代码审查

**症状**：AI 说"代码看起来没问题"，跳过审查
**后果**：问题遗漏到生产环境
**避坑**：每次任务完成后必须执行代码审查
```

- [ ] **Step 7: 添加篇末钩子并更新 README**

在文末添加：

```markdown
---

## 下一步

你已经看到了完整的开发流程。继续阅读 **[第 4 篇：进阶技能与团队协作](04-advanced-teams.md)**，探索更高级的能力，以及如何将 Superpowers 推广到团队。
```

更新 `docs/superpowers/README.md` 中第 3 篇链接。

- [ ] **Step 8: 提交第 3 篇**

```bash
git add docs/superpowers/03-real-world-example.md docs/superpowers/README.md
git commit -m "docs: write tutorial part 3 - real-world example"
```

---

## Task 5: 编写第 4 篇 — 进阶技能与团队协作

**Files:**
- Modify: `docs/superpowers/04-advanced-teams.md`

- [ ] **Step 1: 编写进阶技能一览**

```markdown
## 进阶技能一览

除了基础工作流的 7 个技能，Superpowers 还提供多个进阶技能。

### systematic-debugging：系统化调试

遇到 Bug 时，AI 会自动进入 4 阶段调试流程：

1. **复现**：找到最小可复现步骤
2. **隔离**：定位问题范围
3. **追溯**：找到根本原因
4. **验证**：确认修复有效

### dispatching-parallel-agents：并行任务分发

当有多个独立任务时，AI 可以同时启动多个子 Agent 并行处理：

```markdown
任务 A ──┐
         ├──► 主 Agent 汇总结果
任务 B ──┤
任务 C ──┘
```

适用于：
- 多个独立的功能模块
- 同时需要前端和后端开发
- 需要并行运行测试套件

### verification-before-completion：完成前验证

在宣布"完成"之前，AI 会自动执行验证检查清单：
- 所有测试通过
- 代码审查问题已修复
- 文档已更新
- 没有 lint 错误
```

- [ ] **Step 2: 编写团队协作模式**

```markdown
## 团队协作模式

### 统一 AI 工作流

在团队中推广 Superpowers 的关键步骤：

1. **选定试点项目**：选择一个非关键项目尝试
2. **统一安装插件**：确保团队成员使用相同版本
3. **建立技能库**：积累项目特定的调试经验和代码规范
4. **持续改进**：定期回顾 AI 表现，调整工作流

### 技能库积累

Superpowers 的 Skills 会随使用越来越高效：

- 调试过的 Bug → 形成调试经验
- 验证过的方案 → 形成最佳实践
- 审核过的代码 → 形成代码规范

**你用得越多，你的 AI Agent 越懂你的项目。**
```

- [ ] **Step 3: 编写大型代码库管理策略**

```markdown
## 大型代码库管理策略

### 分层管理

大型代码库建议采用分层技能配置：

```
根目录 skills/
├── base/           # 基础技能（所有项目）
│   ├── tdd/
│   └── code-review/
├── web/            # Web 项目专用
│   └── api-design/
└── cli/            # CLI 项目专用
    └── argument-parsing/
```

### Worktree 并行开发

```
main ────────────────────► main
       │
       ├── feature/user-auth      # 用户认证
       ├── feature/payment        # 支付功能
       └── bugfix/login-error     # 修复登录 Bug
```

每个 worktree 都是独立的 AI 会话，互不干扰。
```

- [ ] **Step 4: 编写技能自定义开发**

```markdown
## 技能可组合性与自定义

### 技能组合示例

```markdown
基础组合：
brainstorming → writing-plans → subagent-driven → TDD → code-review

调试组合：
systematic-debugging → verification-before-completion

并行组合：
dispatching-parallel-agents → executing-plans（并行模式）
```

### 自定义技能

Superpowers 支持编写自定义技能。典型场景：
- 项目特定的代码规范检查
- 专有的测试框架集成
- 特定领域的开发模板
```

- [ ] **Step 5: 编写付费服务引流段落**

```markdown
## 下一步：深入学习

### 免费资源

本系列教程涵盖了 Superpowers 的核心用法。免费内容到此为止。

### 付费服务

如果你想：
- **1 对 1 辅导**：针对你的项目，获得手把手指导
- **团队培训**：让你的团队快速上手 Superpowers
- **技能定制**：开发符合你项目需求的定制技能

**联系我们**，获取定制化服务方案。

---

## 关于 Superpowers

- GitHub：[github.com/obra/superpowers](https://github.com/obra/superpowers)（118k Stars）
- Claude Code 插件：`/plugin install superpowers@superpowers-marketplace`

*「让 AI 编程从碰运气，变成稳定输出」——这是 Superpowers 的承诺。*
```

- [ ] **Step 6: 更新 README 导航页**

完善 `docs/superpowers/README.md`，确保：
- 所有 4 篇链接正确
- 添加简短的系列介绍
- 添加 CTA（如果需要）

- [ ] **Step 7: 提交第 4 篇**

```bash
git add docs/superpowers/04-advanced-teams.md docs/superpowers/README.md
git commit -m "docs: write tutorial part 4 - advanced skills and teams"
```

---

## Task 6: 最终检查与整理

**Files:**
- Review: `docs/superpowers/` 下所有文件

- [ ] **Step 1: 验证所有内部链接**

检查所有文件中的相对链接是否正确：
- `01-installation.md` → `02-core-workflow.md`
- `02-core-workflow.md` → `03-real-world-example.md`
- `03-real-world-example.md` → `04-advanced-teams.md`
- README.md 中所有链接

- [ ] **Step 2: 验证 SEO 关键词覆盖**

确认每篇包含指定关键词：
- 第 1 篇：`Superpowers 安装`、`Claude Code 插件安装`、`AI 编程框架`
- 第 2 篇：`AI 编程工作流`、`TDD 教程`、`AI 代码审查`
- 第 3 篇：`AI 开发实战`、`Superpowers 教程`、`AI 编程案例`
- 第 4 篇：`AI 团队协作`、`Superpowers 进阶`、`AI 开发培训`

- [ ] **Step 3: 验证代码示例完整性**

确认所有代码块：
- 有正确的语言标识（```python、```bash）
- 语法正确，可运行
- 有注释说明关键部分

- [ ] **Step 4: 提交最终检查**

```bash
git add docs/superpowers/
git commit -m "docs: complete superpowers tutorial series"
```

---

## 交付物核对清单

- [ ] `docs/superpowers/README.md` - 系列导航页
- [ ] `docs/superpowers/01-installation.md` - 第 1 篇（约 1500 字）
- [ ] `docs/superpowers/02-core-workflow.md` - 第 2 篇（约 3000 字）
- [ ] `docs/superpowers/03-real-world-example.md` - 第 3 篇（约 3500 字）
- [ ] `docs/superpowers/04-advanced-teams.md` - 第 4 篇（约 2500 字）
- [ ] 所有内部链接正确
- [ ] 所有代码示例可运行
- [ ] SEO 关键词覆盖完整
- [ ] 引流设计自然有效
- [ ] 全部提交到 git

---

## 估计工作量

| Task | 步骤数 | 预估时间 |
|------|--------|----------|
| Task 1: 目录结构 | 3 | 5 分钟 |
| Task 2: 第 1 篇 | 8 | 30 分钟 |
| Task 3: 第 2 篇 | 8 | 60 分钟 |
| Task 4: 第 3 篇 | 8 | 90 分钟 |
| Task 5: 第 4 篇 | 7 | 45 分钟 |
| Task 6: 最终检查 | 4 | 15 分钟 |
| **总计** | **38 步** | **约 4 小时** |
