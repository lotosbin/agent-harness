# MiniMax CLI 入门指南

## 前置要求

- Node.js >= 18
- MiniMax Token Plan（Global 或 CN 区域）

## 安装

### 方式一：为 AI Agent 安装（推荐）

Claude Code、OpenClaw、Cursor 等 Agent 环境：

```bash
npx skills add MiniMax-AI/cli -y -g
```

### 方式二：全局安装 CLI

```bash
npm install -g mmx-cli
```

## 获取 API Key

- Global: https://platform.minimax.io/subscribe/token-plan
- CN: https://platform.minimaxi.com/subscribe/token-plan

## 认证

```bash
mmx auth login --api-key sk-xxxxx
# 或浏览器交互式登录
mmx auth login
```

查看认证状态：

```bash
mmx auth status
```

## 快速示例

### 文本对话

```bash
mmx text chat --message "什么是 MiniMax？"
# 流式输出
mmx text chat --message "写一首诗" --stream
# 多轮对话
mmx text chat --message "用户:你好" --message "assistant:你好！" --message "今天天气如何？"
```

### 图像生成

```bash
mmx image "一只穿着宇航服的猫"
# 批量生成，16:9 比例
mmx image generate --prompt "logo设计" --n 3 --aspect-ratio 16:9
# 指定输出目录
mmx image generate --prompt "产品图" --out-dir ./output/
```

### 视频生成

```bash
# 异步生成（推荐，用于 Agent）
mmx video generate --prompt "海浪日落" --async
# 下载到本地
mmx video generate --prompt "机器人画画" --download robot.mp4
# 查询任务状态
mmx video task get --task-id 123456
# 通过文件 ID 下载
mmx video download --file-id 176844028768320 --out video.mp4
```

### 语音合成

```bash
# 基本合成
mmx speech synthesize --text "你好！" --out hello.mp3
# 流式播放
mmx speech synthesize --text "实时播报" --stream | mpv -
# 选择音色和语速
mmx speech synthesize --text "快速播报" --voice English_magnetic_voiced_man --speed 1.2
# 列出所有可用音色
mmx speech voices
```

### 音乐创作

```bash
# 有歌词
mmx music generate --prompt "欢快的流行音乐" --lyrics "[verse] La da dee, sunny day"
# 纯器乐
mmx music generate --prompt "电影管弦乐" --instrumental --out bgm.mp3
```

### 图像理解

```bash
# 本地图片
mmx vision photo.jpg
# 网络图片 + 自定义问题
mmx vision describe --image https://example.com/img.jpg --prompt "这是什么品种的狗？"
```

### 搜索

```bash
mmx search "MiniMax AI 最新动态"
# 结构化 JSON 输出
mmx search query --q "最新资讯" --output json
```

### 查看 Token 用量

```bash
mmx quota
```

## Agent 集成最佳实践

### 输出隔离模式（推荐用于 Agent）

```bash
mmx text chat --message "任务" --quiet --output json
```

stdout 只输出干净数据，stderr 输出进度信息。

### 异步视频生成

```bash
# 后台执行，不阻塞
mmx video generate --prompt "日落" --async
# Agent 可以同时执行其他任务
```

### 语义退出码处理（伪代码）

```python
result = run("mmx video generate --prompt 'xxx' --async")
if result.exit_code == 0:
    task_id = result.stdout
elif result.exit_code == AUTH_FAILED:
    refresh_token()
elif result.exit_code == TIMEOUT:
    retry_with_backoff()
```

### 完整 Agent 工作流示例

```bash
# 1. 搜集资料
mmx search "AI 最新新闻" --output json > news.json

# 2. 生成文案
mmx text chat --system "你是新闻摘要助手" --message "总结以下内容：$(cat news.json)" --output json > summary.json

# 3. 合成语音
mmx speech synthesize --text "$(cat summary.json)" --out news.mp3

# 4. 生成配图
mmx image "AI科技新闻配图" --out-dir ./output/

# 5. 生成背景音乐
mmx music generate --prompt "新闻背景音乐" --instrumental --out bgm.mp3
```

## 配置

```bash
# 查看当前配置
mmx config show

# 设置区域（cn 或 global）
mmx config set --key region --value cn

# 导出配置 schema
mmx config export-schema | jq .

# 检查更新
mmx update
mmx update latest
```

## 故障排除

```bash
# Token 失效
mmx auth refresh

# 登出并重新登录
mmx auth logout && mmx auth login --api-key sk-xxxxx

# 查看版本
mmx --version
```
