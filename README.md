# Telegram Accounting Bot - THẰNG KHÙNG 🤖

[![Bot Status](https://img.shields.io/badge/Bot-Running-brightgreen)](https://t.me/THANGKHUNGBOT)
[![Version](https://img.shields.io/badge/Version-2.0-blue)]()
[![Python](https://img.shields.io/badge/Python-3.11%2B-yellow)]()
[![Phases](https://img.shields.io/badge/Phases-10%20Complete-success)]()

🤖 **Bot Telegram**: [@THANGKHUNGBOT](https://t.me/THANGKHUNGBOT)  
📊 **Bot ID**: `8673724321`  
🌐 **Status**: ✅ Active  

## 📱 Main Features

### ✅ 10 Complete Phases
- **Phase 1-4**: Basic accounting, operators, parser, grouping
- **Phase 5**: View commands with pagination
- **Phase 6**: Daily cutoff functionality
- **Phase 7**: Group functions
- **Phase 8**: Undo & clear bill
- **Phase 9**: Settings & personal center
- **Phase 10**: Enhanced USDT APIs

### 🎯 4-Button Menu
```
┌─────────────┬─────────────┐
│ ✍️ 开始记账  │ 📝 使用说明  │
├─────────────┼─────────────┤
│ ⚙️ 功能设置  │ 👤 个人中心  │
└─────────────┴─────────────┘
```

### 📊 42 Handlers
- Basic: /start, /help, /health, +<amount>, -<amount>
- View: /config, /bill, /personal_bill, /balance
- Stats: /stats, /statsd, /statsw, /statsm, /top
- Admin: /start_accounting, /clear_bill, /set_daily_cutoff
- Group: /add_operator, /start_class, /set_currency
- Export: /export, /export_today, /export_week
- Currency: /rate, /convert, z0, h0, usdt

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env with BOT_TOKEN and database credentials
```

### 3. Run Bot
```bash
python -m app.main
```

## 📚 Documentation

- 📖 [API Documentation](docs/API.md)
- 🏗️ [Architecture](docs/ARCHITECTURE.md)
- 📝 [Changelog](docs/CHANGELOG.md)

## 🔧 Tech Stack

- **Framework**: aiogram 3.26.0
- **Database**: PostgreSQL
- **Cache**: Redis 7.1.0
- **Excel**: openpyxl 3.1.5
- **Testing**: pytest

## 📊 Performance

- **Concurrent Users**: 1000+
- **Response Time**: <500ms
- **Memory**: <100MB

## 🔒 Security

- RBAC (Role-Based Access Control)
- Rate Limiting (anti-spam)
- Input Validation

## 📄 License

MIT License

---

*Version: 2.0 | Status: ✅ Production Ready*
