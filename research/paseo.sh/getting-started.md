# Paseo Network 入門指南

本指南協助開發者在 30 分鐘內完成 Paseo Network 的基礎接入，開始測試你的 Polkadot/Substrate 應用。

## 前置需求

- 一台 Linux/macOS 電腦（建議 4 核 CPU、8GB RAM）
- 已安裝 Rust 工具鏈（参考 [rustup.rs](https://rustup.rs)）
- 基本的命令行操作能力

## 第一步：獲取測試代幣（PAS）

1. 前往 [Polkadot Faucet](https://faucet.polkadot.io/)
2. 在錢包（如 Talisman、SubWallet、Polkadot.js）中複製你的 Paseo 地址
3. 在 Faucet 頁面粘貼地址，選擇 **Paseo** 網絡
4. 點擊「Request」領取代幣

> 每次請求大約獲得 500 PAS，冷卻時間約 24 小時。

## 第二步：選擇接入方式

### 方案 A：使用 Polkadot.js Apps（最簡單）

無需安裝任何東西，直接使用瀏覽器訪問：

```
https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Fpaseo-rpc.dwellir.com
```

常用公共 RPC 端點：

| 提供商 | 端點 |
|--------|------|
| Dwellir | `wss://paseo-rpc.dwellir.com` |
| Radium Block | `wss://paseo-rpc.radiumblock.io` |
| Lightning Labs | `wss://paseo.elara.patract.io` |

切換網絡：在 Apps 頁面左上角點擊「測試網絡」→「Paseo」

### 方案 B：運行自有節點

```bash
# 克隆 Polkadot SDK
git clone https://github.com/paritytech/polkadot-sdk
cd polkadot-sdk/polkadot

# 運行 Paseo full node
cargo build --release --bin polkadot
./target/release/polkadot \
  --chain paseo \
  --name "你的節點名" \
  --telemetry-url "wss://telemetry.polkadot.io/submit/ 0" \
  --ws-port 9944
```

### 方案 C：使用 Docker

```bash
docker run -d \
  --name polkadot-paseo \
  -p 30333:30333 \
  -p 9944:9944 \
  parity/polkadot:latest \
  --chain paseo \
  --name "你的節點名"
```

## 第三步：連接錢包

1. 安裝錢包擴展：Talisman、SubWallet 或 Polkadot.js Extension
2. 創建或導入帳戶
3. 在錢包中添加 **Paseo** 網絡（通常錢包會自動識別）
4. 手動配置的網絡參數：
   - **RPC URL**：`wss://paseo-rpc.dwellir.com`
   - **Chain ID**：Paseo relay chain
   - **Symbol**：PAS
   - **Decimals**：12

## 第四步：部署智能合約

### 在 Asset Hub 上部署 Solidity 合約（EVM）

1. 在 Polkadot.js Apps 中，切換到 **Asset Hub Paseo** parachain
2. 進入「開發者」→「合約」
3. 選擇 Remix IDE 或 Hardhat 作為部署工具
4. 連接到 Paseo Asset Hub 的 RPC：`wss://paseo-asset-hub-rpc.dwellir.com`

**Remix 配置示例**：

```javascript
// 在 Remix 中選擇 "Injected Web3" 環境
// 網絡：AssetHub Paseo
// 部署你的 Solidity 合約
```

### 使用 Hardhat 部署

```javascript
// hardhat.config.js
module.exports = {
  networks: {
    paseo: {
      url: "https://paseo-asset-hub-rpc.dwellir.com",
      chainId: 10000111,  // Paseo Asset Hub chain ID
    }
  }
};
```

### 在 Asset Hub 上部署 Ink! 合約（WASM）

1. 編寫 Ink! 合約（Rust）
2. 使用 `cargo contract` 工具編譯
3. 在 Polkadot.js Apps 的 Asset Hub 中上傳 `.contract` 文件

## 第五步：測試 XCM 跨鏈消息

1. 在 Polkadot.js Apps 中連接 Paseo Relay Chain
2. 進入「開發者」→「Extrinsics」
3. 選擇 `xcmPallet.send()` 或 `polkadotXcm.send()`
4. 指定目標 parachain 和要傳輸的資產/消息

```javascript
// 從 Relay Chain 發送 XCM 到 Asset Hub
xcmPallet.send(
  { V3: { parents: 0, interior: { X1: { Parachain: 1000 } } } },  // Asset Hub
  {
    V3: [
      { WithdrawAsset: [...] },
      { BuyExecution: { ... } },
      { Transact: { ... } }
    ]
  }
)
```

## 第六步：申請 Parachain Slot 或 Coretime

### 申請 Coretime（推薦）

1. 前往 https://app.regionx.tech/
2. 連接錢包，選擇 Paseo 網絡
3. 購買 Coretime（使用 PAS 代幣）
4. 將 Coretime 分配給你的 parachain

> Paseo 的 Coretime interlude 周期為 **2 天**（Polkadot 主網為 7 天），適合快速測試。

### 申請 Parachain Slot

通過 PAS 提案（PAS-9）申請：

1. 準備 parachain 規格文件和 head-data
2. 在 SubSquare（https://app.paseo.place/）提交 slot 申請提案
3. 等待治理投票通過
4. 通過眾籌（crowdloan）租用 slot

## 常見問題

### Q：為什麼我的餘額顯示為 0？

確保錢包已切換到 **Paseo 網絡**（不是 Polkadot 主網或 Kusama）。檢查 RPC 端點是否正確指向 Paseo。

### Q：Faucet 領取失敗怎麼辦？

- 檢查冷卻時間是否已過
- 嘗試更換 RPC 端點
- 加入 [Matrix 房間](https://matrix.to/#/#paseo:matrix.org) 請求幫助

### Q：如何運行驗證人節點？

參考 [PAS-7 硬體規格](https://github.com/paseo-network/paseo-action-submission) 並聯繫 Paseo Governance Team 完成 KYC/Whitelist 流程。

### Q：EVM 合約 gas 費用高怎麼辦？

PAS 代幣無真實價值，可多次從 Faucet 領取。若費用異常高，檢查是否連接到了 Relay Chain 而非 Asset Hub。

## 下一步

- 閱讀完整的 [Paseo 文檔](https://docs.paseo.sh)
- 參與 [PAS 提案討論](https://github.com/paseo-network/paseo-action-submission)
- 加入 Paseo Matrix 社區：[#paseo:matrix.org](https://matrix.to/#/#paseo:matrix.org)
- 探索 [Passet Hub](https://github.com/paseo-network/passet-hub) 的合約範例
