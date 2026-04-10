# 一张图看懂 MiniMax CLI 使用

```
┌─────────────────────────────────────────────────────────────────────┐
│                       MiniMax CLI 使用速查                          │
│              github.com/MiniMax-AI/cli  |  npm: mmx-cli             │
└─────────────────────────────────────────────────────────────────────┘

安装（一行命令）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Agent 环境:   npx skills add MiniMax-AI/cli -y -g
  全局安装:     npm install -g mmx-cli
  认证:         mmx auth login --api-key sk-xxxxx

八大能力速查
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  1. 文本对话
  ┌──────────────────────────────────────────────────────────┐
  │ mmx text chat --message "写一首诗"                        │
  │ mmx text chat --message "问题" --stream                   │
  │ mmx text chat --system "你是一个助手" --message "..."     │
  │ mmx text chat --message "user:Hi" --message "assistant:Hey!"│
  │ cat msgs.json | mmx text chat --messages-file - --output json│
  └──────────────────────────────────────────────────────────┘

  2. 图像生成
  ┌──────────────────────────────────────────────────────────┐
  │ mmx image "一只穿宇航服的猫"                              │
  │ mmx image generate --prompt "logo" --n 3 --aspect-ratio 16:9│
  │ mmx image generate --prompt "产品图" --out-dir ./out/     │
  └──────────────────────────────────────────────────────────┘

  3. 视频生成
  ┌──────────────────────────────────────────────────────────┐
  │ mmx video generate --prompt "海浪日落" --async           │
  │ mmx video generate --prompt "机器人" --download vid.mp4  │
  │ mmx video task get --task-id 123456                      │
  │ mmx video download --file-id 176844028768320 --out v.mp4 │
  └──────────────────────────────────────────────────────────┘

  4. 语音合成
  ┌──────────────────────────────────────────────────────────┐
  │ mmx speech synthesize --text "你好!" --out hello.mp3    │
  │ mmx speech synthesize --text "播报" --stream | mpv -      │
  │ mmx speech synthesize --text "快读" --voice ... --speed 1.2│
  │ mmx speech voices                                        │
  └──────────────────────────────────────────────────────────┘

  5. 音乐创作
  ┌──────────────────────────────────────────────────────────┐
  │ mmx music generate --prompt "欢快流行" --lyrics "[verse]..."│
  │ mmx music generate --prompt "爵士" --instrumental --out s.mp3│
  └──────────────────────────────────────────────────────────┘

  6. 图像理解
  ┌──────────────────────────────────────────────────────────┐
  │ mmx vision photo.jpg                                     │
  │ mmx vision describe --image https://x.com/a.jpg --prompt "?"│
  └──────────────────────────────────────────────────────────┘

  7. 搜索
  ┌──────────────────────────────────────────────────────────┐
  │ mmx search "MiniMax 最新动态"                            │
  │ mmx search query --q "新闻" --output json               │
  └──────────────────────────────────────────────────────────┘

  8. Token 配额
  ┌──────────────────────────────────────────────────────────┐
  │ mmx quota                                                │
  └──────────────────────────────────────────────────────────┘

Agent 专享模式
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  纯数据输出（stdout 干净）:
    mmx text chat --message "..." --quiet --output json

  后台异步执行（不阻塞）:
    mmx video generate --prompt "..." --async

  语义退出码:
    exit 0  = 成功
    exit N  = 语义错误（鉴权失败/参数错误/超时/网络异常各有编号）
              Agent 可直接根据退出码判断重试策略，无需解析英文

配置
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  mmx config show
  mmx config set --key region --value cn     # 切换 CN/Global
  mmx auth status / refresh / logout
  mmx update latest
