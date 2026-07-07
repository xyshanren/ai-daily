# AI 日报 · 期数记录

> 项目名：**AI 日报**（原"AI 晨报"，第 42 期起改名）
> 域名：https://ai-daily-9yz.pages.dev/
> 仓库：https://github.com/xyshanren/ai-daily
> 部署：Cloudflare Pages（自动检测 git push）
> 创建：2026-07-06

## 已发布期数

| 期数 | 发布日期 | 在线链接 | 状态 | 备注 |
|------|----------|----------|------|------|
| 1-41 | 2024-xx → 2026-07-05 | — | 历史 | 旧名"AI 晨报"，本地存档 `D:\work\workspace\qclaw\daily_news\` |
| **42** | **2026-07-06** | https://ai-daily-9yz.pages.dev/ | **✅ 已发布** | 改名首期，4 主线 16 条，Cloudflare Pages 部署 |

## 第 42 期结构

- **4 条主线**：算力即权力(4条) / Agent 动手派(6条) / 评估标准升级(4条) / 研究前沿(2条)
- **16 条新闻卡片** + 2 张研究卡（Tongyi DeepResearch + Agent-SafetyBench）
- **19 个信源**
- 研究卡样式：card-research（满宽），含核心/方法/结果/复现 4 段 + 论文/开源/SOTA 3 个 chip

## 自动化流程（规划中，明天起跑）

```
05:30  cron 触发：搜索当天 AI 资讯
05:35  生成 HTML 仪表盘 → index.html
06:00  git commit + git push
06:02  Cloudflare Pages 自动部署（30 秒）
06:05  截图工具产出封面图 + 首屏图
08:00  公众号发推：文案 + 封面图 + Web 链接
```

## 公众号发布方案（v2 · 2026-07-07 确认）

1. **封面图**：cover.png（900×383，Hero 区）
2. **正文**：Markdown 文案（7 条精选 + 编辑视角 + 今日数据 + Web 链接）
3. **排版工具**：https://md.newkit.site/（Markdown → 公众号富文本）
4. **不放整页长图**（文字版已覆盖核心信息，长图冗余）
5. **文末引导**：Web 版完整 16 条 + 可点击原文链接

## 截图工具

- 路径：`C:\Users\lixia\.qclaw\workspace\screenshot-tool\screenshot.mjs`
- 零依赖（Chrome headless + CDP 协议）
- 四种模式：hero (1344×768) / cover (900×383) / fullpage (整页) / mobile (375×812)
- 产出目录：`D:\work\workspace\qclaw\daily_news\`

## 仓库文件

| 文件 | 说明 |
|------|------|
| index.html | 仪表盘主文件 |
| issues.md | 本文件 |
| rebuild.py | 工具脚本（保留） |
| .gitignore | 排除临时脚本 |
| README.md | 项目说明 |
| vercel.json | 已删除 |
