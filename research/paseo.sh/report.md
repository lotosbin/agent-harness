# Paseo Network（paseo.sh）研究报告

## 一、因：为何存在

Paseo Network（`paseo.sh`）是 **Polkadot 生態系的去中心化、社區運營測試網**。它於 2024 年由 Polkadot 國庫資助成立，旨在取代原本由 Parity Technologies 維護的 Rococo 測試網，成為社區主導的公共測試基礎設施。

**背景脈絡**：Polkadot 生態系長期以來缺乏一個真正由社區運營、模擬生產環境特性的測試網。Rococo 由 Parity 維護，更新節奏與生產網脫節，且 parachain 團隊無法自由進行實驗性功能測試。Paseo 的出現填補了這一缺口——由 parachain 團隊和基礎設施提供商共同治理，讓測試網的演進與生態需求同步。

## 二、果：帶來的改變

### 2.1 生態影響

- **測試基礎設施民主化**：從 Parity 集中維護轉為社區共治，降低了單點失敗風險
- **功能同步**：與 Polkadot 主網保持功能對齊，包括最新的 Agile Coretime、Async Backing、Elastic Scaling
- **成本模擬**：使用 PAS 測試代幣模擬真實經濟成本，幫助開發者在部署前估算主網費用

### 2.2 核心功能

| 功能 | 說明 |
|------|------|
| **Relay Chain** | Paseo 主鏈，驗證人/提名機制完整 |
| **System Parachains** | Asset Hub、Bridge Hub、Coretime、People、Collectives 全部部署 |
| **Agile Coretime** | 與 Polkadot 2.0 同步的 coretime 模型 |
| **Async Backing** | 異步支持，提升 parachain 區塊產出效率 |
| **Elastic Scaling** | 彈性擴展，動態調整 parachain 容量 |
| **PolkaVM Contracts** | WASM 智能合約runtime |
| **ERC-20 Precompile** | EVM 兼容性，支援 Solidity 合約部署 |
| **XCM Precompile** | 跨鏈消息預編譯介面 |
| **Asset Hub Migration** | 資產遷移測試 |

## 三、體：架構與治理

### 3.1 治理結構

Paseo 由 **Paseo Governance Team（PGT）**——一個 sudo 多簽錢包——進行核心管理，但重大決策通過 **PAS（Paseo Action Submission）** 提案流程公開討論。

**PAS 提案體系**（類比 Polkadot 的 POP/PFC）：

- **PAS-1**：基礎設施提供商入職標準
- **PAS-2**：核心支持模型（含事故管理 SLA）
- **PAS-3**：索引器/區塊瀏覽器規範
- **PAS-4**：支持 Wiki
- **PAS-5**：支持 Repository
- **PAS-6**：團隊會議日程
- **PAS-7**：硬體規格要求
- **PAS-8**：付款流程
- **PAS-9**：Parachain Slot 入職
- **PAS-10**：Coretime 入職
- **PAS-11**：節點提供商需求

提案狀態：Open（徵集中）→ Merged（已批准）→ Closed（已否決）

### 3.2 系統架構

```
┌─────────────────────────────────────────────────────┐
│                  Paseo Relay Chain                  │
│  (驗證人 + 提名機制 + 治理 + staking)                  │
└────────┬──────────┬──────────┬──────────┬──────────┘
         │          │          │          │
    ┌────▼────┐ ┌───▼────┐ ┌──▼──────┐ ┌▼──────────┐
    │Asset Hub│ │Bridge   │ │Coretime  │ │  People   │
    │ (EVM+   │ │  Hub    │ │ (2天     │ │ (身份     │
    │ PolkaVM)│ │(跨鏈橋) │ │ interlude)│ │  鏈)     │
    └─────────┘ └────────┘ └─────────┘ └───────────┘
    ┌──────────────────────────────────────────────┐
    │           Paseo Collectives                  │
    │    ( fellowship, 技術委員會, 願景論壇 )        │
    └──────────────────────────────────────────────┘
```

**Runtime 最新版本**：v2.1.0（2026 年 3 月 23 日發布）

### 3.3 技術棧

- **語言**：Rust（99.4%）
- **SDK**：Polkadot SDK（基於 Substrate）
- **許可**：GPL-3.0（runtimes），Apache-2.0（passet-hub）
- **鏈規範**：https://zondax.ch/paseo（含普通版與 light-client 友好版）

## 四、用：應用場景與使用方式

### 4.1 主要使用者

| 使用者類型 | 使用目的 |
|-----------|---------|
| **Parachain 團隊** | 測試鏈升級、runtime 迁移、parachain slot 申請 |
| **DApp 開發者** | 部署智能合約、測試跨鏈消息（XCM） |
| **錢包/工具開發者** | 測試錢包整合、RPC 端點、簽名流程 |
| **基礎設施提供商** | 運行驗證人/全節點、提供 API 服務 |
| ** Polkadot 核心開發者** | 測試新功能（Coretime、Async Backing 等） |

### 4.2 費用模擬（相較主網）

| 操作 | Paseo 成本（PAS） | 主網對應（DOT） |
|------|-----------------|----------------|
| Parachain 註冊 | ~3,200 PAS | ~3,200 DOT |
| Asset 創建 | ~0.0017 PAS + 0.4 押金 | 相當 |
| Identity 創建 | ~0.002 PAS + 0.2 押金 | 相當 |

### 4.3 接入方式

- **測試代幣領取**：https://faucet.polkadot.io/（輸入 Paseo 地址領取 PAS）
- **Coretime 購買**：https://app.regionx.tech/
- **區塊瀏覽器**：Subscan、Statescan、Blockscout（EVM 合約）
- **治理入口**：SubSquare、Polkassembly
- **支持渠道**：Matrix 房間（公告+技術支持）

## 五、洞：深度洞察

### 5.1 與其他測試網的差異

| 維度 | Paseo | Rococo（舊） | Westend（Polkadot官方） |
|------|-------|-------------|------------------------|
| 運營主體 | 社區（PGT） | Parity | Parity |
| 功能更新 | 與主網同步 | 延遲 | 延遲 |
| Coretime 支持 | 完全支持 | 無 | 無 |
| 治理方式 | PAS 提案流程 | 無 | 無 |
| 穩定性 | 依賴社區響應 | 較高 | 較高 |

### 5.2 關鍵洞察

1. **社區治理示範意義**：Paseo 可能是 Substrate/Polkadot 生態中最接近「真實去中心化治理」的測試網——它不只是一個測試工具，更是一個治理實驗場。

2. **Polkadot 2.0 搶先體驗**：Polkadot 主網尚未完全上線的功能（如 Elastic Scaling、Agile Coretime interlude），開發者可以在 Paseo 上搶先測試和熟悉。

3. **與主網的功能差距極小**：Paseo runtimes 幾乎是生產環境的直接鏡像，降低了「測試環境正常但生產環境出問題」的風險。

4. **國庫資助的可持續性**：由 Polkadot 國庫資助，但依賴於國庫持續投票——若生態熱度下降，資助可能中斷。

5. **EVM + WASM 雙runtime**：Asset Hub 同時支持 PolkaVM（WASM）和 EVM（Solidity），覆蓋了兩類開發者群體。

## 六、資源索引

| 資源 | 連結 |
|------|------|
| 官方網站 | https://paseo.sh |
| 文檔 | https://docs.paseo.sh |
| GitHub 組織 | https://github.com/paseo-network |
| Faucet | https://faucet.polkadot.io/ |
| Coretime 應用 | https://app.regionx.tech/ |
| 鏈規範下載 | https://zondax.ch/paseo |
| Subscan 瀏覽器 | https://paseo.subscan.io/ |
| 治理入口 | https://app.paseo.place/（SubSquare） |

### 主要 GitHub 倉庫

- [paseo-network/runtimes](https://github.com/paseo-network/runtimes) — Runtime 原始碼
- [paseo-network/paseo-chain-specs](https://github.com/paseo-network/paseo-chain-specs) — 鏈規範文件
- [paseo-network/paseo-action-submission](https://github.com/paseo-network/paseo-action-submission) — 提案與治理
- [paseo-network/passet-hub](https://github.com/paseo-network/passet-hub) — Asset Hub runtime
- [paseo-network/apps](https://github.com/paseo-network/apps) — Polkadot.js Apps UI fork
