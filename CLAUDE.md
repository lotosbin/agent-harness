# CLAUDE.md

本文為 Claude Code（claude.ai/code）之操作指南，專用於本代碼庫。
每个研究一个专项目录
研究步骤:
1. 收集主流媒体的相关资讯
2. 官方网站和开源社区
3. 编写研究报告(结构因果体用)
4. 编写入门指导
5. 编写一张图看懂使用
6. 编写一张图看懂原理

## 項目概述

本項目名曰 `agent-harness`，旨在探索 Claude Code 及各類 AI Agent 框架，彙集相關資源與範例，以供構建 Agentic AI 系統之參考。

## 關鍵資源

- **Claude Code**： [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code)、[Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)、[garrytan/gstack](https://github.com/garrytan/gstack)
- **Open Code Agents**： [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)

## 工作環境

- 工作目錄：`/Volumes/StorageMacMini2/liubinbin/Github/lotosbin/agent-harness`
- 終端：`zsh`
- 系統：macOS（Darwin）

## 行事通則

- 言辭務求簡明，去除浮詞套語
- 引用檔案路徑時，須以 Markdown 連結標明，如 `[檔名](fleet-file://...)`
- 修改檔案：優選編輯而非重寫，優選小工具而非大範圍操作
- 多步任務，先思後行，善用 `EnterPlanMode`
- 研究類任務：前置調研用前台 Agent，獨立並行任務用後台 Agent
- 技能（Skills）可用則用，如 `Skill("pdf")`、`Skill("xlsx")` 等
- 依賴變動後，須確保依赖已安裝，程式可正常運行
- 適時建立 `.gitignore`，防止輸出檔案或依賴污染差異

## 程式碼規範

- 命名須清晰明確，用戶可見之處杜絕縮寫
- 類型標註有助理解者則加之，非處處必備
- 函式宜小而專一
- 錯誤處理設於系統邊界（用戶輸入、外部 API），內部邏輯可從簡

## 存疑之時

- 用戶意圖不明，先問後行
- 非尋常任務，使用 `EnterPlanMode` 規劃後再行
- 遇阻則另闢蹊徑，勿強行突破

## Git 規範

- 重大變更，須建功能分支（feature branch）
- 提交訊息：用命令式，首行不逾七十二字
  - 範例：`Add X feature`、`Fix Y bug`、`Refactor Z module`
- `git push` 須謹慎，涉共用系統者，先請示後執行
