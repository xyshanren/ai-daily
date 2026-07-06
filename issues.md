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
| **42** | **2026-07-06** | https://ai-daily-9yz.pages.dev/ | **✅ 已发布** | 改名首期，部署在 Cloudflare Pages |

## 期数元信息（第 42 期）

- **22 条资讯**（按 5 版块分组：模型发布/更新、产品发布/更新、行业动态、论文研究、技巧与观点）
- **19 个数据源**（机器之心、量子位、36Kr、AI 科技评论、虎嗅、新智元、PaperWeekly、arXiv 等）
- **发布渠道**：微信公众平台「AI 每日头条」（规划中）

## 自动化流程（规划中）

```
05:30  cron 触发：搜索当天 22 条 AI 资讯
05:35  生成 HTML 仪表盘 → D:\work\GitRepository\ai-daily-site\index.html
05:50  复制一份为  AI晨报-YYYY-MM-DD.html 备份
06:00  git commit + git push
06:02  Cloudflare Pages 自动检测 push，30 秒内重新部署
06:05  生成封面图、长截图、文字版
06:30  推送完成，等待人工发公众号
08:00  公众号发推：长图 + 文字版 + 短链 ai-daily-9yz.pages.dev
```

## 公众号发布方案（确认版）

1. **封面图**：Hero 区截图（1344×768，标"第 42 期 AI 日报"）
2. **正文贴长图**：整页滚动截图
3. **文末放"🔗 获取原文链接"**：引导用户「后台回复 AI日报 获取带可点击链接的 Web 版」
4. **同时配短文字版**（22 条标题 + 序号 + 一句话概括）放长图前面
