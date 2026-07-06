#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
按"主线叙事"重构 AI 日报仪表盘。
- 22 条卡 → 14 条精选（保数量不缩减）
- 板块 → 3 大主线（算力 / Agent / 标准）
- Hero 5 块 → 3 块（信号/主题/来源）
- 编辑视角 → 简短一句话
- footer 简化
"""
import re
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

f = Path(r"D:\work\GitRepository\ai-daily-site\index.html")
content = f.read_text(encoding="utf-8")

# ============ 1) 切卡片 ============
parts = content.split('<div class="card">')
header = parts[0]
tail = parts[-1]
card_map = {}
idx_re = re.compile(r'<div class="idx">(\d+)</div>')
for p in parts[1:]:
    m = idx_re.search(p)
    if not m:
        continue
    idx = int(m.group(1))
    end_match = re.search(r'</div>\s*</div>\s*</div>', p)
    if not end_match:
        continue
    card_html = '<div class="card">' + p[:end_match.end()] + '</div>'
    card_map[idx] = card_html

print(f"索引到 {len(card_map)} 张卡片")

# ============ 2) 精选 14 条 + 3 主线分配 ============
# 主线 1: 算力即权力 (4 条) - 大公司+芯片
# 主线 2: Agent 走向"动手派" (6 条) - 工具+落地+安全
# 主线 3: AI 评估标准 (4 条) - 论文+标准

THEMES = {
    1: {
        'id': 't1',
        'name': '算力即权力',
        'subtitle': '自研芯片潮：大厂从"买卡"到"造卡"',
        'color': 'var(--accent)',
        'icon': '💎',
        'indexes': [1, 2, 15, 14]  # 昆仑芯 / Anthropic芯片 / OpenAI博通 / SpaceX Cursor
    },
    2: {
        'id': 't2',
        'name': 'Agent 走向"动手派"',
        'subtitle': '从对话到执行：工具平民化 + 落地鸿沟',
        'color': 'var(--green)',
        'icon': '🤖',
        'indexes': [9, 3, 10, 19, 20, 22]  # Page Agent / Seedance / Pocket / 工作流模板 / 71%落地 / Agent安全
    },
    3: {
        'id': 't3',
        'name': 'AI 评估标准升级',
        'subtitle': '模型能力见顶的信号：规范、基准、安全边界',
        'color': 'var(--purple)',
        'icon': '📐',
        'indexes': [17, 18, 11, 12]  # Open AI Infra / Claude 50% / 拟人化新规 / ChatGPT <50%
    },
}

# 验证索引存在
all_selected = []
for theme in THEMES.values():
    for idx in theme['indexes']:
        if idx in card_map:
            all_selected.append(idx)
        else:
            print(f"⚠️ 索引 {idx} 不存在")
print(f"精选 {len(all_selected)} 条: {all_selected}")

# ============ 3) 构建新 HTML ============
# 重新编号 1..N
old_to_new = {old: new for new, old in enumerate(all_selected, 1)}

new_cards_by_theme = {}
for theme_id, theme in THEMES.items():
    new_cards_by_theme[theme_id] = []
    for old_idx in theme['indexes']:
        if old_idx in card_map:
            # 替换 idx 编号
            card = card_map[old_idx]
            new_idx = old_to_new[old_idx]
            card = re.sub(r'<div class="idx">\d+</div>', f'<div class="idx">{new_idx}</div>', card, count=1)
            new_cards_by_theme[theme_id].append(card)

# ============ 4) 新 Hero ============
new_hero = '''<header class="hero">
  <div class="hero-badge">📡 第 42 期 · 2026.07.06</div>
  <h1>AI 日报</h1>
  <p class="subtitle">三条主线 · 读懂 AI 行业今天的真正信号</p>
  <div class="hero-stats">
    <div class="hero-stat total"><div class="num">14</div><div class="lbl">条新闻</div></div>
    <div class="hero-stat themes"><div class="num">3</div><div class="lbl">条主线</div></div>
    <div class="hero-stat sources"><div class="num">19</div><div class="lbl">个信源</div></div>
  </div>
</header>'''

# ============ 5) 新导航 ============
new_nav = '''<nav class="nav-wrap">
  <div class="nav-inner">
    <a href="#t1"><span class="dot" style="background:var(--accent)"></span>算力即权力</a>
    <a href="#t2"><span class="dot" style="background:var(--green)"></span>Agent 动手派</a>
    <a href="#t3"><span class="dot" style="background:var(--purple)"></span>评估标准升级</a>
  </div>
</nav>'''

# ============ 6) 新主体（3 主线 + 14 卡片） ============
sections = []
for theme_id, theme in THEMES.items():
    cards_html = '\n      '.join(new_cards_by_theme[theme_id])
    # anchor class 用 theme_id
    sections.append(f'''<section class="section anchor theme-{theme_id}" id="{theme['id']}">
    <div class="section-header" style="--theme:{theme['color']}">
      <span class="icon">{theme['icon']}</span>
      <div class="section-title-block">
        <h2>主线 {theme_id} · {theme['name']}</h2>
        <p class="section-subtitle">{theme['subtitle']}</p>
      </div>
      <span class="count-badge">{len(theme['indexes'])} 条</span>
    </div>
    <div class="card-grid">
      {cards_html}
    </div>
  </section>''')

main_content = '\n\n    '.join(sections)

# ============ 7) 新 footer ============
new_footer = '''<footer class="footer">
  <p class="footer-tagline">📌 编辑签名：今天三件事——造卡、动手、画线。<strong>没有泡沫，也没有革命，是基础设施在补完。</strong></p>
  <div class="sources-row">
    <span class="src">The Information</span>·<span class="src">36氪</span>·<span class="src">CSDN</span>·<span class="src">Anthropic</span>·<span class="src">GCC-Open AI Infra</span>
  </div>
  <p class="footer-meta">第 42 期 · 2026.07.06 · 星期一 · 共 14 条 · <a href="https://ai-daily-9yz.pages.dev/">ai-daily.pages.dev</a></p>
</footer>'''

# ============ 8) 拼接最终 HTML ============
# 头 = header 截至 <main> 之前
header_end = header.rfind('<main')
header_new = header[:header_end] + '<main class="container">' + '\n'

# 尾 = tail 找到 <main 的开始
tail_start = tail.find('</main>') + len('</main>')
tail_new = '\n\n' + new_footer + '\n\n' + tail[tail_start:]

new_content = header_new + main_content + tail_new

# 9) 替换 Hero
hero_pattern = re.compile(r'<header class="hero">.*?</header>', re.DOTALL)
new_content = hero_pattern.sub(new_hero, new_content, count=1)

# 10) 替换 Nav
nav_pattern = re.compile(r'<nav class="nav-wrap">.*?</nav>', re.DOTALL)
new_content = nav_pattern.sub(new_nav, new_content, count=1)

# 11) 写回
f.write_text(new_content, encoding="utf-8")
print(f"\n✅ 写入新文件: {len(new_content)} 字符")

# 验证
verify = Path(r"D:\work\GitRepository\ai-daily-site\index.html").read_text(encoding="utf-8")
print("\n=== 验证 ===")
n_cards = len(re.findall(r'class="card"', verify))
n_themes = len(re.findall(r'<section class="section anchor theme-', verify))
n_hero = len(re.findall(r'<div class="hero-stat', verify))
print(f"  卡片数: {n_cards} (预期 14)")
print(f"  主线 sections: {n_themes} (预期 3)")
print(f"  hero-stat: {n_hero} (预期 3)")
print(f"  '算力即权力': {verify.count('算力即权力')} (预期 1+)")
print(f"  'Agent 动手派': {verify.count('Agent 动手派')} (预期 1+)")
print(f"  '评估标准升级': {verify.count('评估标准升级')} (预期 1+)")
