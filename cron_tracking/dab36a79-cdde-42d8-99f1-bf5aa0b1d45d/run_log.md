# Cron Run Log — Weekly Tech/VC Intelligence

Cron ID: `dab36a79-cdde-42d8-99f1-bf5aa0b1d45d`
Schedule: `0 13 * * 6` (Saturday 13:00 UTC)

---

## Run 1 — 2026-05-09 (Saturday)

- **Triggered**: 2026-05-09T13:01:48Z
- **Branch**: `cursor/weekly-tech-vc-intelligence-903c`
- **Date range covered**: 2026-05-03 → 2026-05-09

### Outputs
- `research_science_breakthroughs.md` — 8 substantive science breakthroughs identified; section included in report.
- `research_us_industries.md` — 3 industries: Enterprise AI Agents, Defense Tech & Space, Nuclear + AI power.
- `research_china_industries.md` — 3 industries: Open-weight LLMs + AI infra, NEV/Battery, Embodied AI.
- `research_us_top10.md` — Top 10 US deals/events anchored by Sierra ($950M), Anthropic (~$50B in talks), SpaceX×Anthropic + S-1, Astranis, Anagram, Blitzy, Corgi, Panthalassa, Reserv, DeepInfra.
- `research_china_top10.md` — Top 10 China deals: Moonshot ($2B), DeepSeek (in talks), Kunlunxin IPO, CATL HK placement & ATH, Xiaomi SU7/YU7, LDROBOT IPO, WeRide-Lenovo, Pony.ai, Hua Hong/Huali export ban, Galbot/Galaxea/Unitree wave.
- `Weekly_Tech_VC_Report_2026-05-09.md` — bilingual Mandarin Markdown master report.
- `Weekly_Tech_VC_Report_2026-05-09.pdf` — 11-page PDF, 249,365 bytes.
- `email_body.txt` — Mandarin email body to be sent to recipients.

### PDF QC
- Built via `build_pdf.py` using ReportLab.
- Font fallback: WQY Zen Hei TTC was specified but unavailable on this Cloud Agent VM (`/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc` not present). Used WQY Micro Hei TTC (`wqy-microhei.ttc`) as fallback — full CJK coverage, clean rendering verified by rendering pages 1, 5, 11 to PNG.
- Verified: 101 ▶ bullets in PDF (no ●). Headings teal #01696F. Hyperlinks underlined teal. `wordWrap='CJK'`, `TA_LEFT` applied.
- Subscript glyphs (₇₀₂₀) absent in WQY Micro Hei → fallback to plain "C70H20" in source.

### Email & Share — DEFERRED
- The task references `gcal send_email` and `share_file` tools. These are MCP integrations that are **not configured** in this Cloud Agent VM. No `mail`/`mutt`/`sendmail`/`msmtp` available either, and no Google credentials wired in.
- Recipients prepared: `jingwangbeijing@163.com`, `tjc8822@gmail.com`, `zrj@ruc.edu.cn`.
- Subject prepared: `【一级市场周报 v4】2026-05-03 至 2026-05-09 科学突破 + 三大热门行业 + 美中各 Top 10 科技/VC 重磅事件`.
- Plain-text Mandarin body saved as `email_body.txt`.
- Action required from user: configure Gmail / Google Calendar MCP server (or add SMTP credentials in Cursor Dashboard → Cloud Agents → Secrets) for next cron run; or manually forward `Weekly_Tech_VC_Report_2026-05-09.pdf` plus `email_body.txt`.
- `share_file` similarly unavailable — PDF is committed in-repo for now.

### Git
- Commits will be pushed to `cursor/weekly-tech-vc-intelligence-903c` for the user's review and PR integration.
