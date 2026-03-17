# 🤝 Contributing to Telegram Accounting Bot

**Version:** 2.0.1 (Excel Export + Testing)  
**Last Updated:** 2026-03-17

We welcome contributions to the Telegram Accounting Bot! This guide will help you get started with contributing to the project.

---

## 📋 Table of Contents

1. [Getting Started](#getting-started)
2. [Development Setup](#development-setup)
3. [Project Structure](#project-structure)
4. [Coding Standards](#coding-standards)
5. [Testing Guidelines](#testing-guidelines)
6. [Pull Request Process](#pull-request-process)
7. [Bug Reports](#bug-reports)
8. [Feature Requests](#feature-requests)
9. [Documentation](#documentation)

---

## 🧪 Testing Guidelines

### Running Tests

```bash
# Run all tests
python test_complete_implementation.py

# Run specific test file
pytest tests/test_transaction_service.py

# Run with coverage
pytest --cov=app tests/

# Run with verbose output
pytest -v tests/

# Run specific test
pytest tests/test_transaction_service.py::TestTransactionService::test_create_transaction_success

# Run Excel export tests (no database required)
pytest tests/test_excel_export_simple.py -v

# Run all Excel export tests
pytest tests/test_excel*.py -v
```

### Excel Export Testing

Testing Excel export functionality requires special considerations:

```python
# tests/test_excel_export_simple.py
import pytest
from openpyxl import load_workbook
from io import BytesIO
from app.services.excel_export import ExcelExportService

@pytest.mark.asyncio
async def test_export_returns_bytesio():
    """Test that export returns BytesIO object."""
    service = ExcelExportService()
    result = await service.export_transactions(group_id=12345)
    
    assert isinstance(result, BytesIO), "Should return BytesIO"
    assert len(result.getvalue()) > 0, "Should not be empty"

@pytest.mark.asyncio
async def test_export_creates_valid_workbook():
    """Test workbook structure."""
    service = ExcelExportService()
    excel_buffer = await service.export_transactions(group_id=12345)
    
    wb = load_workbook(excel_buffer)
    assert "账单明细" in wb.sheetnames
    assert wb["账单明细"].max_column == 13
```

### Windows Event Loop Configuration

**Important for Windows users:** psycopg async mode requires SelectorEventLoop:

```python
# tests/conftest.py
import sys
import asyncio

@pytest.fixture(scope="session")
def event_loop_policy():
    """Set WindowsSelectorEventLoopPolicy for Windows compatibility."""
    if sys.platform == "win32":
        return asyncio.WindowsSelectorEventLoopPolicy()
    return asyncio.DefaultEventLoopPolicy()
```

```toml
# pyproject.toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
asyncio_default_fixture_loop_scope = "function"
```

### Test Coverage Requirements

- **New features**: Minimum 80% coverage
- **Bug fixes**: Regression tests required
- **Critical paths**: 100% coverage required
- **Excel export**: All styling and data validation tested

### Test File Naming

```
tests/
├── test_*.py                    # Test files
├── test_excel_export_simple.py  # Unit tests (no DB)
├── test_excel_export.py         # Integration tests (with DB)
└── conftest.py                  # Shared fixtures
```

---

## 🔄 Pull Request Process

### Branch Naming

```
feature/description-of-feature
bugfix/description-of-bug
hotfix/urgent-fix-description
docs/documentation-updates
excel/excel-export-feature
```

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add Excel export functionality
fix: resolve transaction parsing error
docs: update API documentation
test: add Excel export tests
chore: update dependencies
```

---

## 📚 Documentation

### Documentation Files

- `README.md` - Main project overview
- `QUICK_START.md` - Quick start guide
- `docs/API.md` - API documentation
- `docs/ARCHITECTURE.md` - Architecture documentation
- `docs/CHANGELOG.md` - Changelog
- `docs/CONTRIBUTING.md` - Contributing guide
- `docs/DEPENDENCIES.md` - Dependencies guide
- `docs/EXCEL_EXPORT.md` - Excel export guide
- `docs/SETTINGS.md` - Settings center guide

### Writing Documentation

When adding new features:

1. **Update README.md**: Add feature to features list
2. **Update CHANGELOG.md**: Document changes
3. **Update API.md**: Add API documentation
4. **Update ARCHITECTURE.md**: Document architecture
5. **Create feature-specific docs**: If needed

---

## 📊 Excel Export Contributions

### Adding New Export Features

1. **Create service method**: `app/services/excel_export.py`
2. **Add handler**: `app/handlers/admin/export.py`
3. **Write tests**: `tests/test_excel_export*.py`
4. **Update documentation**: `docs/EXCEL_EXPORT.md`
5. **Update dependencies**: If new packages needed

### Testing Excel Export

```bash
# Run Excel export tests
pytest tests/test_excel_export_simple.py -v

# Expected output:
# test_export_returns_bytesio PASSED
# test_export_creates_valid_workbook PASSED
# test_header_styling PASSED
# test_column_count PASSED
# test_empty_transactions PASSED
# test_file_size PASSED
#
# 6/6 tests passed (100%)
```

---

## 🛠️ Development Setup

### Local Development

```bash
# 1. Clone repository
git clone https://github.com/Kelvin2602/telegram-accounting-bot.git
cd telegram-accounting-bot

# 2. Install dependencies
python install_dependencies.py

# 3. Set up environment
cp .env.example .env
# Edit .env with your configuration

# 4. Run tests
pytest tests/ -v

# 5. Start development server
python -m app.main
```

---

## 📞 Support

For questions:
1. Check documentation
2. Search existing issues
3. Create new issue with detailed description

**Bot Status:** ✅ Active development - v2.0.1
