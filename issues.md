# AI 日报 · 发布记录

> 项目名：**AI 日报**（原"AI 晨报"，2026-07-06 第 42 期起改名）
> 域名：https://ai-daily-9yz.pages.dev/
> 仓库：https://github.com/xyshanren/ai-daily
> 部署：Cloudflare Pages（git push 自动部署）
> 编号方式：**日期标题制**（2026-07-08 起，不再使用连续期号）

## 已发布记录

| 日期 | 标题 | 链接 | 状态 |
|------|------|------|------|
| 1-41 期 | 旧"AI 晨报" | 本地存档 | 历史 |
| 2026-07-06 | 改名首期 · 4 主线 16 条 | https://ai-daily-9yz.pages.dev/ | ✅ |
| 2026-07-08 | 国产算力大爆发 · 4 主线 14 条 | https://ai-daily-9yz.pages.dev/ | ✅ |

## 最新一期结构（2026-07-08）

- **4 条主线**：国产算力大爆发(4条) / 大模型分层竞争(4条) / AI+产业落地加速(4条) / 研究前沿(2条)
- **14 条卡片** + 2 篇论文
- **16 个信源**

## 自动化流程

```
每周一至五 06:30（北京时间）
→ OpenClaw cron isolated session 启动
→ 搜索当日 AI 资讯 → 生成 HTML 仪表盘
→ 生成 MD 简报（briefings/） + 公众号文案（wechat/）
→ Git push → Cloudflare 自动部署
→ 截图 cover 封面图（screenshots/cover-YYYY-MM-DD.png）
→ 上传 IMA 知识库
⏱ 预计 15 分钟完成
```

## 目录结构

```
daily_news/
├── briefings/      ← AI-News-YYYY-MM-DD.md 每日简报
├── wechat/         ← wechat-YYYY-MM-DD.md 公众号文案
├── screenshots/    ← cover-YYYY-MM-DD.png 封面截图
├── scripts/        ← *.py *.ps1 脚本
├── config/         ← TEMPLATE.md issue_count.json
└── archive/        ← 旧文件、历史任务报告
```

## 公众号发布方案（v3 · 2026-07-08）

1. **封面图**：screenshots/cover-YYYY-MM-DD.png（900×383，Hero 截图）
2. **正文**：公众号文案（wechat/wechat-YYYY-MM-DD.md）
3. **排版工具**：https://md.newkit.site/（Markdown → 公众号富文本）
4. **不放截图**：文案不含 hero/fullpage 截图，纯文字排版
5. **阅读原文**：公众号唯一可用的外部跳转，填 `https://ai-daily-9yz.pages.dev/`
   - ⚠️ 公众号正文中的链接不可点击，仅「阅读原文」有效

## 截图工具

- 路径：`C:\Users\lixia\.qclaw\workspace\screenshot-tool\screenshot.mjs`
- 零依赖（Chrome headless + CDP 协议）
- 仅使用 cover 模式（900×383）

## 仓库文件

| 文件 | 说明 |
|------|------|
| index.html | 仪表盘主文件（每日覆盖） |
| issues.md | 本文件 |
| automation-prompt.md | cron 任务 prompt 模板 |
| rebuild.py | 工具脚本（保留） |
| .gitignore | 排除临时脚本 |
| README.md | 项目说明 |
