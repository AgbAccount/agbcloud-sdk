# AGB SDK Examples

This directory contains practical examples demonstrating how to use the AGB SDK effectively. Examples are organized by complexity and use case to help you find the right starting point.

## 🚀 Quick Start Examples

### Basic Usage
- **[Authentication](basic/authentication.py)** - Setting up API keys and basic client initialization
- **[Session Creation](basic/quickstart.py)** - Creating and managing your first session
- **[Error Handling](basic/error_handling.py)** - Proper error handling patterns

### Core Modules
- **[Code Execution](modules/code/)** - Running Python and JavaScript code
- **[Command Execution](modules/command/)** - Shell command operations
- **[File Operations](modules/file_system/)** - File and directory management
- **[OSS Integration](modules/oss/)** - Cloud storage operations

## 📚 By Use Case

### Development & Debugging
```python
# Quick code execution
from agb import AGB

agb = AGB()
session = agb.create().session

result = session.code.run_code("""
import sys
print(f"Python version: {sys.version}")
print("Hello from AGB!")
""", "python")

print(result.result)
agb.delete(session)
```

### Data Processing
```python
# File processing pipeline
session = agb.create().session

# Upload data
session.file_system.write_file("/tmp/data.csv", "name,age\nAlice,25\nBob,30")

# Process data
session.code.run_code("""
import pandas as pd
df = pd.read_csv('/tmp/data.csv')
df['age_group'] = df['age'].apply(lambda x: 'young' if x < 30 else 'adult')
df.to_csv('/tmp/processed.csv', index=False)
print("Data processed successfully")
""", "python")

# Download results
result = session.file_system.read_file("/tmp/processed.csv")
print("Processed data:", result.content)
```

### Cloud Storage Integration
```python
# OSS operations
session = agb.create().session

# Upload to cloud storage
upload_result = session.oss.upload_file(
    local_path="/tmp/local_file.txt",
    remote_path="bucket/remote_file.txt"
)

if upload_result.success:
    print("File uploaded successfully")
```

## 📁 Directory Structure

```
examples/
├── README.md                    # This file - examples overview
└── python/                     # Python examples
    ├── session_creation/        # Session creation examples
    │   ├── main.py             # Basic session creation
    │   └── README.md           # Session creation guide
    ├── file_system/            # File operations examples
    │   ├── main.py             # File system operations
    │   └── README.md           # File operations guide
    └── oss_management/         # Cloud storage examples
        ├── main.py             # OSS operations
        └── README.md           # OSS management guide
```

## 🎯 Getting Started

### 1. Choose Your Starting Point

**New to AGB?** Start with:
- [Basic Authentication](basic/authentication.py)
- [Quick Start](basic/quickstart.py)
- [Simple Code Execution](modules/code/python_execution.py)

**Experienced Developer?** Jump to:
- [Advanced Examples](advanced/)
- [Use Cases](use_cases/)
- [Concurrent Sessions](advanced/concurrent_sessions.py)

### 2. Run Examples

All examples are self-contained Python scripts. To run them:

```bash
# Set your API key
export AGB_API_KEY="your_api_key_here"

# Run any example
python examples/python/session_creation/main.py
python examples/python/file_system/main.py
python examples/python/oss_management/main.py
```

### 3. Modify and Experiment

Each example includes:
- ✅ Complete, runnable code
- 📝 Detailed comments explaining each step
- 🔧 Customization suggestions
- ❌ Error handling patterns

## 📋 Available Examples

### Session Creation (`python/session_creation/`)
Learn the fundamentals of AGB sessions:
- Basic session creation and management
- Session configuration with labels
- Error handling patterns
- Session lifecycle best practices

### File System Operations (`python/file_system/`)
Master file and directory operations:
- Reading and writing files
- Directory navigation and management
- File permissions and metadata
- Batch file operations

### OSS Management (`python/oss_management/`)
Cloud storage integration patterns:
- File uploads and downloads
- Object metadata management
- Batch operations
- Error handling for cloud operations

## 🔧 Prerequisites

Before running examples, ensure you have:

1. **AGB SDK installed**:
   ```bash
   pip install agbcloud-sdk
   ```

2. **API key configured**:
   ```bash
   export AGB_API_KEY="your_api_key"
   ```

3. **Python 3.7+** (for running examples locally)

## 💡 Tips for Using Examples

### Customization
- Modify timeout values for your use case
- Adjust file paths and names
- Change session labels for organization
- Experiment with different code languages

### Error Handling
- Always check result.success before proceeding
- Log request_id for debugging
- Implement retry logic for production use
- Clean up sessions in finally blocks

### Performance
- Reuse sessions for multiple operations
- Use concurrent execution for independent tasks
- Monitor resource usage with session.info()
- Batch operations when possible

## 🤝 Contributing Examples

Have a useful example? We'd love to include it! Examples should be:
- **Self-contained**: Runnable without external dependencies
- **Well-documented**: Clear comments and explanations
- **Error-handled**: Proper error checking and cleanup
- **Practical**: Solving real-world problems

## 📞 Getting Help

If you have questions about examples:
- 📖 Check the [API Reference](../api-reference/README.md)
- 📚 Read the [Guides](../guides/)
- 🐛 [Report Issues](https://github.com/agbcloud/agbcloud-sdk/issues)

## 🔗 Related Documentation

- **[Getting Started Guide](../quickstart.md)** - First steps with AGB
- **[Session Management](../guides/session-management.md)** - Session lifecycle
- **[Code Execution Guide](../guides/code-execution.md)** - Running code
- **[API Reference](../api-reference/README.md)** - Complete API docs