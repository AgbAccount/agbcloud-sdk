# AGB SDK API Reference

Complete technical API documentation for developers. This reference covers all classes, methods, parameters, and return types in the AGB SDK.

## 🚀 Quick Reference

### Core API Pattern
```python
from agb import AGB
from agb.session_params import CreateSessionParams

# Client initialization
agb = AGB()  # Uses AGB_API_KEY environment variable

# Session lifecycle
result = agb.create()
session = result.session

# Module usage
session.code.run_code(code, language, timeout_s=300)
session.command.execute_command(command, timeout_ms=1000) 
session.file_system.read_file(path)
session.oss.upload_file(local_path, remote_path)

# Cleanup
agb.delete(session)
```

## 📚 API Documentation

### 🏗️ Core Classes

| Class | Purpose | Documentation |
|-------|---------|---------------|
| **[AGB](core/agb.md)** | Main SDK client | Session creation and management |
| **[Session](core/session.md)** | Session management | Session lifecycle and information |
| **[CreateSessionParams](core/session-params.md)** | Session configuration | Parameters for session creation |

### 🔧 Modules

| Module | Purpose | Documentation |
|--------|---------|---------------|
| **[Code](modules/code.md)** | Code execution | Python and JavaScript execution |
| **[Command](modules/command.md)** | Shell commands | Command execution and output |
| **[FileSystem](modules/filesystem.md)** | File operations | File and directory management |
| **[OSS](modules/oss.md)** | Cloud storage | Object Storage Service integration |

### 📊 Response Types

| Response Type | Purpose | Documentation |
|---------------|---------|---------------|
| **[SessionResult](responses/session-result.md)** | Session creation results | Success status and session object |
| **[DeleteResult](responses/delete-result.md)** | Session deletion results | Deletion status and request ID |
| **[CodeExecutionResult](responses/code-result.md)** | Code execution results | Output, success status, and errors |
| **[CommandResult](responses/command-result.md)** | Command execution results | Command output and execution status |
| **[FileSystemResults](responses/filesystem-results.md)** | File operation results | File content, directory listings, etc. |
| **[OSSResults](responses/oss-results.md)** | OSS operation results | Upload/download status and metadata |

## 🎯 API Categories

### Session Management API
```python
# AGB class methods
agb.create(params=None) -> SessionResult
agb.list() -> List[BaseSession]
agb.delete(session) -> DeleteResult

# Session methods  
session.info() -> OperationResult
session.get_session_id() -> str
session.get_api_key() -> str
```

### Code Execution API
```python
# Code module methods
session.code.run_code(
    code: str, 
    language: str, 
    timeout_s: int = 300
) -> CodeExecutionResult
```

### Command Execution API
```python
# Command module methods
session.command.execute_command(
    command: str,
    timeout_ms: int = 1000
) -> CommandResult
```

### File System API
```python
# FileSystem module methods
session.file_system.read_file(path: str) -> FileReadResult
session.file_system.write_file(path: str, content: str) -> FileWriteResult
session.file_system.list_directory(path: str) -> DirectoryListResult
session.file_system.create_directory(path: str) -> BoolResult
session.file_system.delete_file(path: str) -> BoolResult
session.file_system.delete_directory(path: str) -> BoolResult
```

### OSS API
```python
# OSS module methods
session.oss.upload_file(local_path: str, remote_path: str) -> OSSUploadResult
session.oss.download_file(remote_path: str, local_path: str) -> OSSDownloadResult
session.oss.list_objects(prefix: str = "") -> OSSListResult
session.oss.delete_object(remote_path: str) -> BoolResult
```

## 🔧 Configuration

### Environment Variables
```bash
# Required
export AGB_API_KEY="your_api_key_here"

# Optional
export AGB_ENDPOINT="sdk-api.agb.cloud"
export AGB_TIMEOUT_MS="30000"
```

### Client Configuration
```python
from agb import AGB
from agb.config import Config

# Default configuration (recommended)
agb = AGB()

# Custom configuration
config = Config(
    endpoint="your-custom-endpoint.com",
    timeout_ms=30000,
)
agb = AGB(api_key="your_key", cfg=config)
```

## 📋 Session Capabilities

### Available Modules
All sessions provide access to the following modules:

```python
# All sessions have these capabilities
session.code         # ✅ Python & JavaScript execution
session.command      # ✅ Shell command execution  
session.file_system  # ✅ File & directory operations
session.oss          # ✅ Object Storage Service
```

## 🚨 Error Handling

### Common Response Pattern
```python
class ApiResponse:
    request_id: str      # Unique request identifier
    success: bool        # Operation success status
    error_message: str   # Error description if failed
```

### Error Handling Examples
```python
# Session creation error handling
result = agb.create()
if not result.success:
    print(f"Error: {result.error_message}")
    print(f"Request ID: {result.request_id}")

# Module operation error handling
code_result = session.code.run_code("invalid code", "python")
if not code_result.success:
    print(f"Execution failed: {code_result.error_message}")
    # Partial output may still be available
    if code_result.result:
        print(f"Partial output: {code_result.result}")
```

## 📖 Detailed Documentation

### Core Classes
- **[AGB Client](core/agb.md)** - Main SDK client class
- **[Session Management](core/session.md)** - Session lifecycle and operations
- **[Session Parameters](core/session-params.md)** - Configuration options

### Modules
- **[Code Execution](modules/code.md)** - Python and JavaScript execution
- **[Command Execution](modules/command.md)** - Shell command operations
- **[File System](modules/filesystem.md)** - File and directory management
- **[OSS Integration](modules/oss.md)** - Cloud storage operations

### Response Types
- **[Session Responses](responses/session-result.md)** - Session operation results
- **[Execution Responses](responses/execution-results.md)** - Code and command results
- **[File System Responses](responses/filesystem-results.md)** - File operation results
- **[OSS Responses](responses/oss-results.md)** - Storage operation results

## 🔗 Related Documentation

- **[User Guides](../guides/README.md)** - Task-oriented usage guides
- **[Examples](../examples/README.md)** - Practical code examples
- **[Getting Started](../quickstart.md)** - Quick start tutorial

## 📞 Developer Support

For API-specific questions:
- 📖 Check the detailed class documentation above
- 💡 Review [practical examples](../examples/)
- 🐛 [Report API issues](https://github.com/agbcloud/agbcloud-sdk/issues)