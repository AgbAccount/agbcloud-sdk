# AGB SDK Documentation

## 🎯 Quick Navigation

### 👋 New Users
- **[5-Minute Quick Start](quickstart.md)** - Experience AGB immediately
- **[Session Management](guides/session-management.md)** - Manage your automation sessions
- **[Code Execution Getting Started](guides/code-execution.md)** - The simplest use case

### 🚀 Experienced Users  
- **[API Reference Documentation](api-reference/README.md)** - Complete API documentation
- **[Best Practices](guides/best-practices.md)** - Production environment usage
- **[Session Management](guides/session-management.md)** - Advanced session management

### 📋 By Use Case

| I want to... | Recommended Documentation | Example Code |
|-----------|----------|----------|
| 🤖 Browser Automation | [Browser Automation Guide](guides/browser-automation.md) | [Browser Examples](examples/browser/) |
| 🐍 Execute Code | [Code Execution Guide](guides/code-execution.md) | [Code Examples](examples/python/file_system/) |
| 💾 File Operations | [File Operations Guide](guides/file-operations.md) | [File Examples](examples/python/file_system/) |
| ⚡ Execute Commands | [Command Execution Guide](guides/command-execution.md) | [Command Examples](examples/python/session_creation/) |
| ☁️ Cloud Storage Integration | [OSS Integration Guide](guides/oss-integration.md) | [OSS Examples](examples/python/oss_management/) |

## 📚 Documentation Structure

### Core Guides (`guides/`)
- **[browser-automation.md](guides/browser-automation.md)** - AI-Powered Browser Automation Guide
- **[session-management.md](guides/session-management.md)** - Complete Session Management Guide
- **[code-execution.md](guides/code-execution.md)** - Code Execution Guide  
- **[command-execution.md](guides/command-execution.md)** - Command Execution Guide
- **[file-operations.md](guides/file-operations.md)** - File Operations Guide
- **[oss-integration.md](guides/oss-integration.md)** - OSS Cloud Storage Guide
- **[best-practices.md](guides/best-practices.md)** - Best Practices and Troubleshooting

### API Reference (`api-reference/`)
- **[README.md](api-reference/README.md)** - API Overview
- **[core/](api-reference/core/)** - Core Class API (AGB, Session, SessionParams)
- **[modules/](api-reference/modules/)** - Functional Module API (Code, Command, FileSystem, OSS, Browser)
  - **[browser.md](api-reference/modules/browser.md)** - Browser Module API Reference
- **[python/](api-reference/python/README.md)** - Python SDK API Reference

### Example Code (`examples/`)
- **[README.md](examples/README.md)** - Examples Overview
- **[browser/](examples/browser/)** - Browser Automation Examples
  - **[basic_navigation.py](examples/browser/basic_navigation.py)** - Basic browser navigation
  - **[natural_language_actions.py](examples/browser/natural_language_actions.py)** - AI-powered actions
  - **[data_extraction.py](examples/browser/data_extraction.py)** - Structured data extraction
- **[python/](examples/python/)** - Python Examples
  - **[file-system/](examples/python/file_system/README.md)** - File Operations Examples
  - **[oss-management/](examples/python/oss_management/README.md)** - OSS Integration Examples
  - **[session-creation/](examples/python/session_creation/README.md)** - Session Creation Examples

## 🚀 Quick Start

### Installation
```bash
pip install agbcloud-sdk
export AGB_API_KEY="your_api_key"
```

### First Example
```python
from agb import AGB

# Create client
agb = AGB()

# Create code execution session
session = agb.create().session

# Execute code
result = session.code.run_code("print('Hello AGB!')", "python")
print(result.result)

# Cleanup
agb.delete(session)
```

## 📞 Get Help

- 🐛 **[Issue Feedback](https://github.com/agbcloud/agbcloud-sdk/issues)** - Report bugs or request features
- 📖 **[Complete Quick Start](quickstart.md)** - Detailed getting started tutorial
- 🔧 **[Best Practices](guides/best-practices.md)** - Production environment usage guide

---