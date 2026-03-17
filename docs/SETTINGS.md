# ⚙️ Settings Center Guide - Telegram Accounting Bot

**Version:** 2.0.1  
**Last Updated:** 2026-03-17

---

## 📋 Overview

Settings Center cho phép cấu hình chi tiết bot ở cấp độ group và user, bao gồm:

- **Group Settings**: Cấu hình cho nhóm chat
- **User Settings**: Cấu hình cá nhân
- **Display Settings**: Chế độ hiển thị
- **Notification Settings**: Thông báo
- **Export Settings**: Cấu hình xuất dữ liệu

---

## 🎛️ Group Settings

### **Cài đặt cơ bản**

| Setting | Default | Description |
|---------|---------|-------------|
| `group_id` | Auto | ID nhóm chat |
| `group_name` | Auto | Tên nhóm |
| `accounting_unit` | "USDT" | Đơn vị kế toán |
| `timezone` | "UTC+7" | Múi giờ |
| `language` | "zh" | Ngôn ngữ (zh/vi/en) |

### **Cài đặt nâng cao**

| Setting | Default | Description |
|---------|---------|-------------|
| `daily_cutoff` | None | Giờ cắt sổ ngày (HH:MM) |
| `auto_commit` | True | Tự động commit giao dịch |
| `require_confirmation` | False | Yêu cầu xác nhận giao dịch |
| `allow_negative_balance` | False | Cho phép số dư âm |

### **Cấu hình Group Settings**

```python
# Admin command
/settings group accounting_unit VND
/settings group timezone UTC+8
/settings group language vi
/settings group daily_cutoff 23:30
```

---

## 👤 User Settings

### **Cài đặt cá nhân**

| Setting | Default | Description |
|---------|---------|-------------|
| `user_id` | Auto | Telegram user ID |
| `display_mode` | "compact" | Chế độ hiển thị (compact/detailed) |
| `currency_display` | "symbol" | Hiển thị tiền (symbol/code/full) |
| `notifications_enabled` | True | Bật thông báo |

### **Cài đặt hiển thị**

```python
# User command
/settings display_mode detailed
/settings currency_display code
/settings notifications off
```

---

## 📊 Display Settings

### **Display Modes**

1. **Compact Mode** (Mặc định)
   - Hiển thị ngắn gọn
   - Ít thông tin chi tiết
   - Phù hợp xem nhanh

2. **Detailed Mode**
   - Hiển thị đầy đủ thông tin
   - Bao gồm metadata
   - Phù hợp phân tích

### **Currency Display Options**

1. **Symbol**: `$1000`
2. **Code**: `1000 USDT`
3. **Full**: `1000 USDT (Tether)`

---

## 🔔 Notification Settings

### **Types of Notifications**

1. **Transaction Notifications**: Thông báo giao dịch
2. **Balance Alerts**: Cảnh báo số dư
3. **Daily Reports**: Báo cáo ngày
4. **System Updates**: Cập nhật hệ thống

### **Configure Notifications**

```python
# Bật/tắt thông báo
/settings notifications on
/settings notifications off

# Cấu hình chi tiết
/settings notify_transaction on
/settings notify_balance off
/settings notify_daily on
```

---

## 📊 Export Settings

### **Export Formats**

1. **Excel (.xlsx)** - Mặc định
   - 13 columns dữ liệu
   - Styling và formatting
   - Phù hợp phân tích

2. **CSV (.csv)** - Sắp thêm
   - Plain text
   - Dễ import vào hệ thống khác

3. **JSON (.json)** - Sắp thêm
   - Structured data
   - API integration

### **Export Configuration**

```python
# Cấu hình export
/settings export_format excel
/settings export_include_headers true
/settings export_date_format YYYY-MM-DD
```

### **Excel Export Settings**

| Setting | Default | Description |
|---------|---------|-------------|
| `include_headers` | True | Bao gồm header row |
| `apply_styling` | True | Áp dụng styling |
| `freeze_panes` | "A2" | Freeze row/column |
| `number_format` | "0.00" | Định dạng số |
| `date_format` | "YYYY-MM-DD HH:mm" | Định dạng ngày |

---

## 🎯 Settings Commands

### **Admin Commands**

```bash
# Group settings
/settings group accounting_unit <unit>
/settings group timezone <tz>
/settings group language <lang>
/settings group daily_cutoff <HH:MM>

# View settings
/settings group              # Xem group settings
/settings group <key>        # Xem setting cụ thể
```

### **User Commands**

```bash
# Personal settings
/settings display_mode <mode>
/settings currency_display <display>
/settings notifications <on|off>
/settings page_size <size>

# View settings
/settings                  # Xem tất cả settings
/settings display          # Xem display settings
```

---

## 🔧 Settings Architecture

### **Settings Storage**

```sql
CREATE TABLE group_settings (
    group_id BIGINT PRIMARY KEY,
    accounting_unit VARCHAR(10) DEFAULT 'USDT',
    timezone VARCHAR(20) DEFAULT 'UTC+7',
    language VARCHAR(5) DEFAULT 'zh',
    daily_cutoff TIME,
    auto_commit BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE user_settings (
    user_id BIGINT PRIMARY KEY,
    display_mode VARCHAR(20) DEFAULT 'compact',
    currency_display VARCHAR(20) DEFAULT 'symbol',
    notifications_enabled BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### **Settings Service**

```python
from app.services.settings import SettingsService

settings = SettingsService()

# Get group settings
group_settings = await settings.get_group_settings(group_id)

# Update group settings
await settings.update_group_settings(
    group_id=group_id,
    accounting_unit='VND'
)

# Get user settings
user_settings = await settings.get_user_settings(user_id)
```

---

## 📝 Best Practices

### **1. Group Settings**

✅ **Nên làm:**
- Đặt accounting_unit phù hợp với quốc gia
- Cấu hình timezone chính xác
- Set daily_cutoff nếu cần báo cáo ngày

❌ **Tránh:**
- Thay đổi accounting_unit giữa chừng
- Để timezone sai (gây lệch ngày)
- Daily_cutoff quá gần midnight

### **2. User Settings**

✅ **Nên làm:**
- Chọn display_mode phù hợp nhu cầu
- Bật notifications cho giao dịch quan trọng
- Configure currency_display nhất quán

❌ **Tránh:**
- Để notifications off (miss thông báo)
- Thay đổi display_mode liên tục

### **3. Export Settings**

✅ **Nên làm:**
- Sử dụng Excel format cho phân tích
- Giữ nguyên styling để dễ đọc
- Export định kỳ để backup

❌ **Tránh:**
- Export quá nhiều data cùng lúc
- Thay đổi format giữa các lần export

---

## 🔍 Troubleshooting

### **Settings not saving**

```python
# Check database connection
# Verify group_id/user_id correct
# Check permissions (admin only for group settings)
```

### **Settings not applying**

```python
# Clear cache: redis-cli FLUSHDB
# Restart bot
# Check settings service logs
```

### **Export settings ignored**

```python
# Verify export service initialized
# Check settings loaded correctly
# Review export logs for errors
```

---

## 📚 Related Documentation

- [API.md](API.md) - Settings API endpoints
- [ARCHITECTURE.md](ARCHITECTURE.md) - Settings architecture
- [DEPENDENCIES.md](DEPENDENCIES.md) - Settings-related dependencies
- [EXCEL_EXPORT.md](EXCEL_EXPORT.md) - Export functionality

---

## 🆘 Support

For settings-related issues:

1. Check this guide first
2. Review logs for errors
3. Verify database connection
4. Check Redis cache
5. Contact admin if needed

**Bot Status:** ✅ Settings Center fully functional with group and user configuration support.
