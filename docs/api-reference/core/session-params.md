# Session Parameters API Reference

Parameters for creating and managing sessions in the AGB cloud environment.

## CreateSessionParams Class

Parameters for creating a new session.

### Class Definition

```python
class CreateSessionParams:
    def __init__(
        self,
        labels: Optional[Dict[str, str]] = None,
        image_id: Optional[str] = None,
    )
```

### Parameters

#### `labels`
- **Type:** `Optional[Dict[str, str]]`
- **Default:** `None`
- **Description:** Custom labels for the session. These can be used for organizing and filtering sessions.

#### `image_id`
- **Type:** `Optional[str]`
- **Default:** `None`
- **Description:** ID of the image to use for the session. If not provided, defaults to "code_latest".

### Usage Examples

#### Basic Session Creation

```python
from agb import AGB
from agb.session_params import CreateSessionParams

agb = AGB(api_key="your_api_key")

# Create session with default parameters
result = agb.create()
if result.success:
    session = result.session
    print(f"Created session: {session.session_id}")
```

#### With Labels

```python
# Create session with organizational labels
params = CreateSessionParams(
    labels={
        "project": "data-analysis",
        "environment": "production",
        "user": "analyst@company.com",
        "version": "v1.2.3"
    }
)

result = agb.create(params)
if result.success:
    session = result.session
    print(f"Created session with labels: {params.labels}")
```

#### With Custom Image

```python
# Create session with specific image
params = CreateSessionParams(
    image_id="agb-code-space-1",
    labels={"custom_image": "true"}
)

result = agb.create(params)
```

#### Complete Configuration

```python
from agb.session_params import CreateSessionParams

# Full configuration example
params = CreateSessionParams(
    labels={
        "project": "ml-pipeline",
        "stage": "training",
        "model": "bert-large",
        "experiment": "exp-001",
        "created_by": "data-team"
    },
    image_id="agb-code-space-1"
)

result = agb.create(params)
```

## ListSessionParams Class

Parameters for listing and filtering sessions (future use).

### Class Definition

```python
class ListSessionParams:
    def __init__(self, labels: Dict[str, str] = None)
```

**Note:** This class is defined for future functionality. Currently, the `agb.list()` method returns all sessions without filtering.

## Available Images

The following images are available for session creation:

```python
# Default images
DEFAULT_IMAGES = {
    "code_latest": "Latest general-purpose code execution environment",
    "agb-code-space-1": "Specialized code execution environment"
}
```

### Image Selection

```python
# Use default image (code_latest)
params = CreateSessionParams()

# Use specific image
params = CreateSessionParams(image_id="agb-code-space-1")
```

## Best Practices

### 1. Use Descriptive Labels
```python
params = CreateSessionParams(
    labels={
        "project": "web-scraping",
        "environment": "staging",
        "team": "data-science",
        "created_by": "john.doe@company.com"
    }
)
```

### 2. Choose Appropriate Images
- Use `"code_latest"` for general code execution
- Use `"agb-code-space-1"` for specialized environments

### 3. Session Organization
```python
# Group sessions by project
params = CreateSessionParams(
    labels={"project": "ml-training", "phase": "preprocessing"}
)
```

## Related Content

- 🔧 **API Reference**: [AGB API](agb.md)
- 💡 **Examples**: [Session Examples](../../examples/README.md)
- 📚 **Best Practices**: [Best Practices Guide](../../guides/best-practices.md) 