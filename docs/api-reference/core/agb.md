# AGB API Reference

The main client class for interacting with the AGB cloud runtime environment.

## Class Definition

```python
class AGB:
    def __init__(self, api_key: str = "", cfg: Optional[Config] = None)
```

## Constructor

### Parameters

#### `api_key`
- **Type:** `str`
- **Default:** `""`
- **Description:** API key for authentication. If not provided, it will be loaded from the `AGB_API_KEY` environment variable.

#### `cfg`
- **Type:** `Optional[Config]`
- **Default:** `None`
- **Description:** Configuration object. If not provided, default configuration will be used.

### Example

```python
from agb import AGB

# Using API key directly
agb = AGB(api_key="your_api_key_here")

# Using environment variable
# Set AGB_API_KEY environment variable first
agb = AGB()

# With custom configuration
from agb.config import Config
config = Config(endpoint="https://custom.endpoint.com")
agb = AGB(api_key="your_api_key", cfg=config)
```

## Methods

### `create(params=None)`

Create a new session in the AGB cloud environment.

#### Parameters

- **`params`** (`Optional[CreateSessionParams]`): Parameters for creating the session. Defaults to `None`.

#### Returns

- **`SessionResult`**: Result containing the created session and request ID.

#### Example

```python
from agb.session_params import CreateSessionParams

# Create with default parameters
result = agb.create()
if result.success:
    session = result.session
    print(f"Created session: {session.session_id}")

# Create with custom parameters
params = CreateSessionParams(
    labels={"project": "data-analysis"},
    image_id="agb-code-space-1"
)
result = agb.create(params)
```

### `list()`

List all available sessions.

#### Returns

- **`List[BaseSession]`**: A list of all available sessions.

#### Example

```python
sessions = agb.list()
for session in sessions:
    print(f"Session ID: {session.session_id}")
    if hasattr(session, 'image_id'):
        print(f"Image ID: {session.image_id}")
```

### `delete(session)`

Delete a session by session object.

#### Parameters

- **`session`** (`Session`): The session to delete.

#### Returns

- **`DeleteResult`**: Result indicating success or failure and request ID.

#### Example

```python
# Create a session
result = agb.create()
if result.success:
    session = result.session
    
    # Use the session
    # ... perform operations ...
    
    # Delete the session
    delete_result = agb.delete(session)
    if delete_result.success:
        print("Session deleted successfully")
    else:
        print(f"Failed to delete session: {delete_result.error_message}")
```

## Properties

### `api_key`
- **Type:** `str`
- **Description:** The API key used for authentication.

### `endpoint`
- **Type:** `str`
- **Description:** The API endpoint URL.

### `timeout_ms`
- **Type:** `int`
- **Description:** Request timeout in milliseconds.

### `client`
- **Type:** `Client`
- **Description:** The underlying HTTP client for API communication.

## Usage Examples

### Basic Session Management

```python
from agb import AGB

# Initialize client
agb = AGB(api_key="your_api_key")

# Create a session
result = agb.create()
if result.success:
    session = result.session
    
    # Use the session for various operations
    code_result = session.code.run_code("print('Hello World')", "python")
    if code_result.success:
        print(f"Code output: {code_result.result}")
    
    # Get session information
    info = session.info()
    if info.success:
        print(f"Session info: {info.data}")
    
    # Clean up
    delete_result = agb.delete(session)
    if delete_result.success:
        print("Session cleaned up successfully")
```

### Session with Custom Configuration

```python
from agb import AGB
from agb.session_params import CreateSessionParams

agb = AGB(api_key="your_api_key")

# Create session with labels and custom image
params = CreateSessionParams(
    labels={
        "project": "machine-learning",
        "environment": "development",
        "team": "data-science"
    },
    image_id="agb-code-space-1"
)

result = agb.create(params)
if result.success:
    session = result.session
    print(f"Created session with custom config: {session.session_id}")
    
    # Session has all modules available
    print(f"Code module available: {hasattr(session, 'code')}")
    print(f"Command module available: {hasattr(session, 'command')}")
    print(f"FileSystem module available: {hasattr(session, 'file_system')}")
    print(f"OSS module available: {hasattr(session, 'oss')}")
```

### Multiple Session Management

```python
from agb import AGB

agb = AGB(api_key="your_api_key")

# Create multiple sessions
sessions = []
for i in range(3):
    result = agb.create()
    if result.success:
        sessions.append(result.session)
        print(f"Created session {i+1}: {result.session.session_id}")

# List all sessions
all_sessions = agb.list()
print(f"Total sessions: {len(all_sessions)}")

# Clean up all sessions
for session in sessions:
    delete_result = agb.delete(session)
    if delete_result.success:
        print(f"Deleted session: {session.session_id}")
```

### Error Handling

```python
from agb import AGB

try:
    agb = AGB(api_key="your_api_key")
    
    # Create session with error handling
    result = agb.create()
    if not result.success:
        print(f"Session creation failed: {result.error_message}")
        if result.request_id:
            print(f"Request ID for debugging: {result.request_id}")
        return
    
    session = result.session
    
    # Use session with error handling
    code_result = session.code.run_code("print('Test')", "python")
    if not code_result.success:
        print(f"Code execution failed: {code_result.error_message}")
    
    # Always clean up, even on error
    delete_result = agb.delete(session)
    if not delete_result.success:
        print(f"Warning: Failed to delete session: {delete_result.error_message}")

except ValueError as e:
    print(f"Configuration error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Response Objects

### SessionResult

Result object returned by session creation methods.

```python
class SessionResult:
    request_id: str          # Unique request identifier
    success: bool           # Whether session creation succeeded
    session: BaseSession    # The created session (if successful)
    error_message: str      # Error description (if failed)
```

### DeleteResult

Result object returned by session deletion methods.

```python
class DeleteResult:
    request_id: str     # Unique request identifier
    success: bool      # Whether deletion succeeded
    error_message: str # Error description (if failed)
```

## Configuration

### Environment Variables

- **`AGB_API_KEY`**: API key for authentication (used when not provided in constructor)

### Default Configuration

```python
# Default endpoint and timeout
default_config = {
    "endpoint": "sdk-api.agb.cloud",
    "timeout_ms": 30000
}
```

## Best Practices

### 1. Always Check Results

```python
result = agb.create()
if result.success:
    # Proceed with session
    session = result.session
else:
    # Handle error
    print(f"Error: {result.error_message}")
```

### 2. Proper Resource Management

```python
# Always clean up sessions
try:
    result = agb.create()
    if result.success:
        session = result.session
        # ... use session ...
finally:
    if 'session' in locals():
        agb.delete(session)
```

### 3. Use Environment Variables for API Keys

```bash
# Set environment variable
export AGB_API_KEY="your_api_key_here"
```

```python
# Use environment variable
agb = AGB()  # Automatically uses AGB_API_KEY
```

### 4. Handle Network Errors

```python
import time

def create_session_with_retry(agb, max_retries=3):
    for attempt in range(max_retries):
        try:
            result = agb.create()
            if result.success:
                return result
            else:
                print(f"Attempt {attempt + 1} failed: {result.error_message}")
        except Exception as e:
            print(f"Network error on attempt {attempt + 1}: {e}")
        
        if attempt < max_retries - 1:
            time.sleep(2 ** attempt)  # Exponential backoff
    
    return None
```

## Related Content

- 📋 **Parameters**: [Session Parameters](session-params.md)
- 🔧 **Sessions**: [Session API](session.md)
- 💡 **Examples**: [Usage Examples](../../examples/README.md)
- 📚 **Guides**: [Best Practices](../../guides/best-practices.md) 