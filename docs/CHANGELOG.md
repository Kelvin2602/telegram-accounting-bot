# 📝 Changelog - Telegram Accounting Bot

## [2.0.1] - 2026-03-17

### 🔥 CRITICAL FIXES & EXCEL EXPORT

#### **Excel Export System**
- ✅ **Production Ready Excel Export** - Complete implementation
- **13 Columns**: 时间，分组名称，操作员，操作类型，金额，手续费率，汇率，记账单位，最终金额，备注，GroupId, OperationType, MessageId
- **Header Styling**: Bold font, background color, borders, auto-width
- **Advanced Features**: Freeze panes at A2, number formatting, row height 25px
- **Export Commands**:
  - `/export_today` - Export today's transactions
  - `/export_week` - Export this week's transactions
  - `/export month` - Export this month's transactions
  - Inline keyboard export from menu

#### **Critical Bug Fixes**
- ❌ **Fixed**: Tuple syntax bug at line 279 (main_menu_accounting_callbacks.py)
- ❌ **Fixed**: FSInputFile → BufferedInputFile conversion
- ✅ **Pattern**: Consistent BufferedInputFile usage across all handlers

#### **Test Coverage**
- ✅ **6/6 Tests Passing** (100% coverage)
- `test_export_returns_bytesio`
- `test_export_creates_valid_workbook`
- `test_header_styling`
- `test_column_count`
- `test_empty_transactions`
- `test_file_size`

#### **Documentation**
- ✅ Created `docs/EXCEL_EXPORT.md` (500+ lines)
- ✅ Updated `docs/API.md` with Excel Export API
- ✅ Updated `docs/ARCHITECTURE.md` with Excel architecture
- ✅ Updated `docs/DEPENDENCIES.md` with openpyxl, pytest
- ✅ Updated `docs/CONTRIBUTING.md` with testing guidelines
- ✅ Created `docs/SETTINGS.md` for settings center
- ✅ Updated `QUICK_START.md` with Excel examples
- ✅ Updated `README.md` with v2.0.1 badges

#### **Technical Changes**
- Added `openpyxl>=3.1.5` for Excel export
- Windows event loop configuration for pytest
- pyproject.toml asyncio configuration

---

## [2.0] - 2026-03-15

### ✅ All 10 Phases Complete

#### **Phase 1-4: Core Accounting**
- Basic transaction processing
- Operator management with RBAC
- Multi-format transaction parser
- Group-based accounting

#### **Phase 5: View Commands**
- 配置 (Settings view)
- +0 (Zero transaction)
- 个人账单 (Personal transactions)
- Pagination support

#### **Phase 6: Daily Cutoff**
- 设置日切 (Set daily cutoff)
- 关闭日切 (Disable daily cutoff)
- Automatic period separation

#### **Phase 7: Group Functions**
- 上课/下课 (Class start/end)
- Display modes (compact/detailed)
- Accounting units

#### **Phase 8: Undo & Clear**
- Reply-to-undo functionality
- 清空账单 (Clear transactions)
- Transaction reversal

#### **Phase 9: Settings Center**
- Group settings configuration
- User preferences
- Display settings
- Notification settings

#### **Phase 10: Enhanced USDT APIs**
- z0 (OKX API)
- h0 (Huobi API)
- usdt (Price comparison)
- Real-time exchange rates

---

## [1.0] - 2026-03-10

### Initial Release
- Basic bot structure
- Transaction recording
- Balance checking
- Simple commands
