# 第 3 篇：实战案例

> AI 开发实战 | Superpowers 教程 | AI 编程案例

## 案例背景

我们用 Superpowers 的方式，为一个博客系统开发评论功能。

### 需求描述

- 用户可以对文章发表评论
- 评论支持最多三层嵌套回复
- 评论需要审核后才显示（管理员可开关）
- 提供基本的增删查 API

### 技术栈

- **后端**：Python + FastAPI
- **数据库**：SQLite
- **测试**：pytest

---

## Step 1：头脑风暴

### 启动对话

```
你：我想给博客加个评论系统
AI：我正在使用 brainstorming 技能...

    在开始之前，我需要了解一下项目背景。
    你的项目是 Web 应用、CLI 工具还是 API 服务？

你：FastAPI 写的博客后端 API
AI：好的，我看到你有一个 FastAPI 项目。
    评论需要支持嵌套回复吗？如果需要，最多几层？

你：需要，最多三层
AI：了解。三层嵌套的评论系统。
    回复是实时显示还是需要审核？

你：需要审核，管理员可以开关这个功能
AI：明白。需要审核功能。
    评论的数据需要持久化吗？还是纯内存？

你：SQLite 就够
AI：好的，使用 SQLite。
    最后问一下：这个 API 需要认证吗？

你：暂时不需要，公开评论就行
AI：好的，公开评论 API。
    我已经了解了需求。让我整理一下设计方案...
```

### 生成的设计文档

```markdown
# 博客评论系统设计

## 数据模型

### Comment

| 字段 | 类型 | 说明 |
|------|------|------|
| id | int | 主键，自增 |
| article_id | int | 文章 ID |
| parent_id | int? | 父评论 ID，NULL 表示顶层评论 |
| author | str | 评论者名称 |
| content | str | 评论内容 |
| status | str | pending/approved/rejected |
| nesting_level | int | 嵌套层级，1-3 |
| created_at | datetime | 创建时间 |

## API 端点

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /articles/{id}/comments | 获取文章的所有评论 |
| POST | /articles/{id}/comments | 创建评论 |
| DELETE | /comments/{id} | 删除评论 |

## 核心逻辑

1. **嵌套层级限制**：nesting_level 超过 3 则拒绝
2. **审核状态**：默认 pending，需管理员审核
3. **软删除**：DELETE 操作设置 status=deleted
```

---

## Step 2：任务规划

设计确认后，AI 生成以下实施计划：

### Task 1: 数据模型

**文件：**
- 创建: `models/comment.py`
- 测试: `tests/models/test_comment.py`

### Task 2: API 端点

**文件：**
- 创建: `api/comments.py`
- 测试: `tests/api/test_comments.py`

### Task 3: 嵌套层级逻辑

**文件：**
- 修改: `models/comment.py`
- 修改: `tests/models/test_comment.py`

---

## Step 3：TDD 代码演示

### Task 1: 数据模型完整代码

```python
# tests/models/test_comment.py
import pytest
from models.comment import Comment, MAX_NESTING_LEVEL

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
    with pytest.raises(ValueError) as exc:
        Comment(
            article_id=1,
            author="李四",
            content="第四层回复",
            nesting_level=4  # 超过限制
        )
    assert "嵌套层级不能超过" in str(exc.value)

def test_valid_nesting_levels():
    """合法的嵌套层级应该正常创建"""
    for level in range(1, MAX_NESTING_LEVEL + 1):
        comment = Comment(
            article_id=1,
            author=f"用户{level}",
            content=f"第{level}层评论",
            nesting_level=level
        )
        assert comment.nesting_level == level
```

```python
# models/comment.py
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

# 最大嵌套层级
MAX_NESTING_LEVEL = 3

@dataclass
class Comment:
    article_id: int
    author: str
    content: str
    parent_id: Optional[int] = None
    nesting_level: int = 1
    status: str = "pending"
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        """验证嵌套层级"""
        if self.nesting_level > MAX_NESTING_LEVEL:
            raise ValueError(f"嵌套层级不能超过 {MAX_NESTING_LEVEL}")
```

### 运行测试

```bash
# RED 阶段：确认测试失败
$ pytest tests/models/test_comment.py -v
FAILED tests/models/test_comment.py::test_comment_creation
FAILED tests/models/test_comment.py::test_comment_nesting_limit
...
# 预期失败：ModuleNotFoundError 或 AssertionError

# GREEN 阶段：实现代码后
$ pytest tests/models/test_comment.py -v
PASSED tests/models/test_comment.py::test_comment_creation
PASSED tests/models/test_comment.py::test_comment_nesting_limit
PASSED tests/models/test_comment.py::test_valid_nesting_levels
===================== 3 passed =====================
```

---

## Step 4：代码审查

### 审查报告

```markdown
## 代码审查报告 - Task 1: 数据模型

### 严重问题
- ❌ 无（代码质量良好）

### 建议改进
- 💡 可以添加 `__repr__` 方法，便于调试

### 通过项
- ✅ 测试覆盖了核心场景
- ✅ 嵌套层级限制逻辑正确
- ✅ 使用 dataclass，代码简洁
- ✅ 有适当的类型注解

---

## 代码审查报告 - Task 2: API 端点

### 严重问题
- ❌ 未验证评论内容长度（空内容应被拒绝）

### 建议改进
- 💡 可以添加分页支持

### 通过项
- ✅ RESTful 设计规范
- ✅ 有适当的错误处理
```

---

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

### 陷阱 4：猴子补丁（Monkey Patching）测试

**症状**：测试中用 mock 替换核心逻辑

**后果**：测试通过但实际功能可能损坏

**避坑**：尽量测试真实行为，只在必要时使用 mock

---

## 实战效果总结

### 效率提升

| 指标 | 无流程 AI | Superpowers |
|------|----------|-------------|
| 开发时间 | ~4 小时 | ~3 小时 |
| Bug 数量 | 3-5 个 | 0-1 个 |
| 调试时间 | 1 小时 | 10 分钟 |
| 代码可维护性 | 低 | 高 |

### 关键差异

1. **测试先行**：每写一行代码都有一个测试保护
2. **小步快跑**：每次提交都是完整的功能点
3. **持续验证**：不等到最后才发现问题
4. **设计文档**：团队成员可以快速理解系统

---

## 完整流程回顾

```
想法：我想要评论功能
   ↓
头脑风暴：明确需求细节
   ↓
设计文档：确定数据模型和 API
   ↓
任务规划：拆分为小步骤
   ↓
Task 1 → TDD → 代码审查
   ↓
Task 2 → TDD → 代码审查
   ↓
...
   ↓
完成分支 → 合并
```

---

## 下一步

你已经看到了完整的开发流程。继续阅读 **[第 4 篇：进阶技能与团队协作](04-advanced-teams.md)**，探索更高级的能力，以及如何将 Superpowers 推广到团队。
