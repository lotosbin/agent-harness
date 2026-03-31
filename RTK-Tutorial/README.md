# RTK (Rust Token Killer) 完整教程

**RTK** 是一个高性能 CLI 代理工具，通过智能过滤和压缩命令输出，将 LLM token 消耗降低 **60-90%**。零依赖，<10ms 开销，单二进制文件。

[![GitHub Stars](https://img.shields.io/github/stars/rtk-ai/rtk)](https://github.com/rtk-ai/rtk)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

---

## 目录

| 章节 | 文件 | 内容 |
|------|------|------|
| [入门指导](01-getting-started/README.md) | `01-getting-started/README.md` | 5 分钟快速上手，安装、初始化、验证 |
| [一张图看懂原理](02-principle/README.md) | `02-principle/README.md` | ASCII 图展示 Hook 拦截、过滤机制、工作流程 |
| [一张图学会使用](03-usage/README.md) | `03-usage/README.md` | 速查表覆盖所有常用命令和参数 |
| [详细内容](04-detailed/README.md) | `04-detailed/README.md` | 完整功能文档、配置选项、高级技巧 |

---

## 快速开始

### 安装 (30 秒)

```bash
# macOS
brew install rtk

# Linux / macOS
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh

# Rust
cargo install --git https://github.com/rtk-ai/rtk
```

### 初始化 (1 分钟)

```bash
rtk init -g  # Claude Code / Copilot (默认)
```

### 验证

重启 Claude Code 后，运行任意命令测试:

```bash
git status
cargo test
```

---

## 核心特性

| 特性 | 说明 |
|------|------|
| **60-90% Token 节省** | 智能过滤和压缩命令输出 |
| **零依赖** | 单二进制文件，无需运行时 |
| **<10ms 开销** | 代理延迟几乎无感知 |
| **10 种 AI 工具** | Claude Code / Cursor / Gemini / Copilot 等 |
| **故障安全** | 过滤失败时自动回退原始输出 |
| **本地存储** | 所有数据存储在本地，保护隐私 |

---

## 节省示例

**30 分钟典型 Claude Code 会话:**

| 操作 | 频率 | 标准 tokens | RTK tokens | 节省 |
|------|------|-------------|------------|------|
| ls/tree | 10x | 2,000 | 400 | 80% |
| cat/read | 20x | 40,000 | 12,000 | 70% |
| git status | 10x | 3,000 | 600 | 80% |
| cargo test | 5x | 25,000 | 2,500 | 90% |
| **总计** | | **~118,000** | **~23,900** | **80%** |

---

## 命令速查

```bash
# 文件操作
rtk ls .                 # 目录树
rtk read <file>          # 读取文件
rtk read <file> -l aggressive  # 仅函数签名
rtk grep "pattern"       # 搜索

# Git 操作
rtk git status           # 状态
rtk git log -n 10        # 历史
rtk git push             # 推送

# 测试
rtk test cargo test      # 测试运行
rtk pytest               # Python 测试

# 分析
rtk gain                 # 节省统计
rtk gain --graph         # 图表

# 参数
-u  超紧凑模式
-v, -vv, -vvv  详细程度
```

---

## 相关资源

- **GitHub**: [github.com/rtk-ai/rtk](https://github.com/rtk-ai/rtk)
- **Stars**: 15.4k | Forks: 777
- **License**: MIT

---

*本文档由 Claude Code 生成，最后更新于 2026-03-30*
