# Browser Automation Examples

This directory contains practical examples demonstrating various browser automation capabilities using the AGB SDK.

## 📁 Example Categories

### Basic Automation
- [**basic_navigation.py**](basic_navigation.py) - Simple page navigation and interaction
- [**form_filling.py**](form_filling.py) - Automated form filling and submission
- [**element_interaction.py**](element_interaction.py) - Clicking, scrolling, and basic interactions

### AI Agent Operations
- [**natural_language_actions.py**](natural_language_actions.py) - Using natural language to control the browser
- [**page_observation.py**](page_observation.py) - Observing and analyzing page elements
- [**data_extraction.py**](data_extraction.py) - Extracting structured data from web pages

### Advanced Configuration
- [**stealth_mode.py**](stealth_mode.py) - Using stealth mode to avoid detection
- [**proxy_configuration.py**](proxy_configuration.py) - Setting up and using proxies
- [**fingerprint_customization.py**](fingerprint_customization.py) - Customizing browser fingerprints
- [**mobile_emulation.py**](mobile_emulation.py) - Emulating mobile devices

### Real-World Use Cases
- [**ecommerce_automation.py**](ecommerce_automation.py) - Automating e-commerce workflows
- [**search_and_scrape.py**](search_and_scrape.py) - Search engines and data scraping
- [**social_media_automation.py**](social_media_automation.py) - Social media interactions
- [**multi_step_workflow.py**](multi_step_workflow.py) - Complex multi-step automation

### Error Handling & Best Practices
- [**error_handling.py**](error_handling.py) - Robust error handling patterns
- [**retry_mechanisms.py**](retry_mechanisms.py) - Implementing retry logic
- [**resource_management.py**](resource_management.py) - Proper resource cleanup

## 🚀 Quick Start

### Prerequisites

1. Install required dependencies:
```bash
pip install agbcloud-sdk playwright pydantic
python -m playwright install chromium
```

2. Set your API key:
```bash
export AGB_API_KEY=your_api_key_here
```

### Running Examples

Each example is self-contained and can be run directly:

```bash
python basic_navigation.py
python natural_language_actions.py
python data_extraction.py
```

## 📖 Example Descriptions

### Basic Automation Examples

#### basic_navigation.py
Demonstrates fundamental browser operations:
- Creating and initializing a browser session
- Navigating to web pages
- Getting page information (title, URL, etc.)
- Basic Playwright integration

#### form_filling.py
Shows how to interact with web forms:
- Finding and filling input fields
- Selecting dropdown options
- Clicking buttons and submitting forms
- Handling form validation

#### element_interaction.py
Covers various element interactions:
- Clicking buttons and links
- Scrolling and page navigation
- Handling dynamic content
- Working with different element types

### AI Agent Examples

#### natural_language_actions.py
Demonstrates AI-powered browser control:
- Using natural language to describe actions
- Complex multi-step operations
- Handling dynamic page content
- Error recovery with AI assistance

#### page_observation.py
Shows how to analyze page content:
- Finding elements using natural language
- Analyzing page structure
- Identifying interactive elements
- Getting element properties and states

#### data_extraction.py
Demonstrates structured data extraction:
- Defining data schemas with Pydantic
- Extracting product information
- Handling lists and nested data
- Text-based vs DOM-based extraction

### Advanced Configuration Examples

#### stealth_mode.py
Shows how to avoid bot detection:
- Enabling stealth mode
- Customizing user agents
- Fingerprint randomization
- Best practices for stealth browsing

#### proxy_configuration.py
Demonstrates proxy usage:
- Custom proxy setup
- Built-in proxy services
- Rotating IP addresses
- Handling proxy authentication

#### fingerprint_customization.py
Shows browser fingerprint control:
- Device type emulation
- Operating system spoofing
- Locale and language settings
- Advanced fingerprinting techniques

### Real-World Use Cases

#### ecommerce_automation.py
Complete e-commerce workflow:
- Product search and filtering
- Adding items to cart
- Checkout process automation
- Price monitoring and comparison

#### search_and_scrape.py
Search engine automation:
- Performing searches
- Extracting search results
- Following pagination
- Handling different search engines

#### multi_step_workflow.py
Complex automation scenarios:
- Multi-page workflows
- State management between pages
- Conditional logic and branching
- Error recovery and continuation

## 🛠️ Common Patterns

### Session Management
```python
import os
from agb import AGB
from agb.session_params import CreateSessionParams

# Standard session setup
api_key = os.getenv("AGB_API_KEY")
agb = AGB(api_key=api_key)
params = CreateSessionParams(image_id="agb-browser-use-1")
result = agb.create(params)
session = result.session
```

### Browser Initialization
```python
from agb.modules.browser import BrowserOption, BrowserViewport

# Basic initialization
option = BrowserOption(use_stealth=True)
success = await session.browser.initialize_async(option)

# Advanced configuration
option = BrowserOption(
    use_stealth=True,
    viewport=BrowserViewport(width=1366, height=768),
    user_agent="Custom User Agent"
)
```

### Playwright Integration
```python
from playwright.async_api import async_playwright

endpoint_url = session.browser.get_endpoint_url()
async with async_playwright() as p:
    browser = await p.chromium.connect_over_cdp(endpoint_url)
    page = await browser.new_page()
    # Your automation code here
    await browser.close()
```

### AI Agent Usage
```python
from agb.modules.browser import ActOptions, ObserveOptions, ExtractOptions

# Perform actions
result = await session.browser.agent.act_async(page, ActOptions(
    action="Click the submit button",
    timeoutMS=10000
))

# Observe elements
success, results = await session.browser.agent.observe_async(page, ObserveOptions(
    instruction="Find all product cards",
    returnActions=10
))

# Extract data
success, data = await session.browser.agent.extract_async(page, ExtractOptions(
    instruction="Extract product information",
    schema=ProductSchema
))
```

## 🔧 Troubleshooting

### Common Issues

1. **Browser initialization fails**
   - Check your API key and session image
   - Verify network connectivity
   - See `error_handling.py` for debugging techniques

2. **CDP connection issues**
   - Ensure browser is properly initialized
   - Check endpoint URL validity
   - Try reinitializing the browser

3. **AI agent actions fail**
   - Make instructions more specific
   - Increase timeout values
   - Check page loading state

4. **Resource cleanup**
   - Always close browsers and delete sessions
   - Use try-finally blocks for cleanup
   - See `resource_management.py` for best practices

### Debug Mode

Enable detailed logging for troubleshooting:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📚 Additional Resources

- [Browser Automation Guide](../../guides/browser-automation.md) - Comprehensive guide
- [API Reference](../../api-reference/modules/browser.md) - Detailed API documentation
- [Best Practices](../../guides/best-practices.md) - Production deployment tips
- [Session Management](../../guides/session-management.md) - Advanced session handling

## 🤝 Contributing

Found a bug or want to add an example? Please:
1. Check existing issues and examples
2. Create a clear, focused example
3. Include proper error handling
4. Add documentation and comments
5. Test thoroughly before submitting

## 📄 License

These examples are provided under the same license as the AGB SDK. See the main LICENSE file for details. 