# Telnyx Python SDK 3.0.0-alpha Migration Guide

## Overview

This guide documents the migration from the current Telnyx Python SDK (v2.1.6) to the upcoming 3.0.0-alpha release. The new SDK represents a complete architectural rewrite with modern Python patterns, comprehensive type safety, and enhanced developer experience.

## Why Migrate to the New SDK?

### 1. **Complete Architecture Rewrite**
- **Generated with Stainless**: The 3.0.0-alpha SDK is automatically generated from Telnyx's OpenAPI specification using [Stainless](https://www.stainless.com/), ensuring better API coverage and consistency.
- Full type safety with Pydantic models for all request/response objects

### 2. **Native Async/Await Support**
- **Current SDK**: Synchronous only with requests library
- **3.0.0-alpha**: Both sync (`Telnyx`) and async (`AsyncTelnyx`) clients
- **aiohttp integration** available as optional dependency for improved concurrency
- **Streaming responses** for handling large datasets efficiently

### 3. **Modern Dependencies & Build System**
- **HTTP Client**: Replaced `requests` with modern `httpx` (async-capable)
- **Dependencies**: New deps include `pydantic`, `typing-extensions`, `anyio`  
- **Build System**: Modern `pyproject.toml` with Hatchling instead of setup.py
- **Project Structure**: Moved to `src/` layout following modern Python standards

### 4. **Enhanced Developer Experience**
- **Type Safety**: Full type hints with IDE autocompletion and static analysis
- **Error Handling**: Comprehensive exception hierarchy with specific HTTP status mappings
- **Raw Response Access**: Easy access to underlying HTTP responses and headers
- **Request/Response Logging**: Built-in debugging capabilities

## What's New in 3.0.0-alpha

### 🔧 **Complete Architecture Rewrite**
- **Generated with Stainless**: The 3.0.0-alpha SDK is automatically generated from Telnyx's OpenAPI specification using [Stainless](https://www.stainless.com/), ensuring better API coverage and consistency.
- **Type Safety**: Full TypeScript-style type hints with Pydantic models for all request/response objects.
- **Modern Python**: Built with modern Python patterns using `httpx`, `pydantic`, and `typing-extensions`.

### 🚀 **Async Support**
- **Native async/await support** with `AsyncTelnyx` client
- **aiohttp integration** available as optional dependency for improved concurrency
- **Streaming responses** for handling large datasets efficiently

### 📦 **New Dependencies & Requirements**
```python
# 3.0.0-alpha dependencies
httpx>=0.23.0, <1
pydantic>=1.9.0, <3  
typing-extensions>=4.10, <5
anyio>=3.5.0, <5
distro>=1.7.0, <2
sniffio
```

### 🏗️ **Improved Project Structure**
- **src/ layout**: Code moved from `telnyx/` to `src/telnyx/` following modern Python packaging standards
- **pyproject.toml**: Modern build system using Hatchling instead of setup.py
- **Rye/Nox**: Modern development tooling for dependencies and testing

### 🔗 **Better HTTP Client Support**
- **httpx by default**: Modern async-capable HTTP client
- **aiohttp support**: Optional for enhanced async performance
- **Automatic retries**: Built-in retry logic with exponential backoff

### ⚡ **Enhanced Developer Experience**
- **Detailed error messages**: Structured exception hierarchy
- **Raw response access**: Easy access to underlying HTTP responses
- **Request/response logging**: Better debugging capabilities
- **IDE support**: Full type hints for better autocompletion

---

## What's Different/Removed

### 🚫 **Breaking Changes**

#### **1. Import Structure**
**Current (v2.1.6):**
```python
import telnyx
telnyx.api_key = "your-key"
profile = telnyx.MessagingProfile.retrieve("123")
```

**3.0.0-alpha:**
```python
from telnyx import Telnyx
client = Telnyx(api_key="your-key")
profile = client.messaging_profiles.retrieve("123")
```

#### **2. Global Configuration Removed**
- No more global `telnyx.api_key`, `telnyx.api_base` configuration
- All configuration now happens through client instantiation
- Per-request configuration through client methods instead of global overrides

#### **3. Resource Access Pattern**
**Current:** Class-based access (`telnyx.MessagingProfile.list()`) 
**3.0.0-alpha:** Client-based access (`client.messaging_profiles.list()`)

#### **4. Reduced API Coverage (Currently)**
- **Current SDK:** 148 API resource files
- **3.0.0-alpha:** 109 API resource files
- Some specialized resources may not be available yet in alpha

#### **5. Dependency Changes**
**Removed:**
- `requests` (replaced with `httpx`)
- `six` (Python 2 compatibility no longer needed)
- `PyNaCl` (webhook signature validation handled differently)

**Added:**
- `httpx` (modern HTTP client)
- `pydantic` (data validation)
- `typing-extensions` (enhanced type support)

#### **6. HTTP Client Configuration**
- No more `telnyx.default_http_client` configuration
- HTTP client configuration done through client instantiation
- Different client class hierarchy

#### **7. Error Handling**
**Current:** Basic exception classes
**3.0.0-alpha:** Comprehensive exception hierarchy with specific HTTP status mappings

---

## Migration Steps

### Step 1: Update Dependencies
```bash
# Remove current version
pip uninstall telnyx

# Install alpha version  
pip install --pre telnyx
```

### Step 2: Update Import Statements
```python
# OLD
import telnyx

# NEW
from telnyx import Telnyx  # for sync
from telnyx import AsyncTelnyx  # for async
```

### Step 3: Initialize Client
```python
# OLD
import telnyx
telnyx.api_key = "your-api-key"

# NEW
from telnyx import Telnyx
client = Telnyx(api_key="your-api-key")
```

### Step 4: Update Resource Access
```python
# OLD
profiles = telnyx.MessagingProfile.list()
profile = telnyx.MessagingProfile.retrieve("123")

# NEW  
profiles = client.messaging_profiles.list()
profile = client.messaging_profiles.retrieve("123")
```

### Step 5: Handle Async Operations (Optional)
```python
import asyncio
from telnyx import AsyncTelnyx

async def main():
    client = AsyncTelnyx(api_key="your-api-key")
    profiles = await client.messaging_profiles.list()
    await client.aclose()  # Clean up resources

asyncio.run(main())
```

### Step 6: Update Error Handling
```python
# OLD
try:
    profile = telnyx.MessagingProfile.retrieve("123")
except Exception as e:
    print(f"Error: {e}")

# NEW
from telnyx import NotFoundError, APIError

try:
    profile = client.messaging_profiles.retrieve("123")
except NotFoundError:
    print("Profile not found")
except APIError as e:
    print(f"API Error: {e}")
```

### Step 7: Configuration Changes
```python
# OLD
telnyx.api_base = "https://api.example.com"
telnyx.max_network_retries = 3

# NEW
client = Telnyx(
    api_key="your-key",
    base_url="https://api.example.com",
    max_retries=3,
    timeout=30.0
)
```

---

## Staying on Current Version

If you prefer to stay on the current stable SDK version:

### Option 1: Pin to Current Major Version
```bash
pip install "telnyx>=2.0.0,<3.0.0"
```

**Or in requirements.txt:**
```
telnyx>=2.1.0,<3.0.0
```

**Or in pyproject.toml:**
```toml
[project]
dependencies = [
    "telnyx>=2.1.0,<3.0.0"
]
```

### Option 2: Pin to Exact Version
```bash
pip install "telnyx==2.1.6"
```

### What You'll Miss
- Modern async/await support
- Better type safety and IDE support  
- Automatic API updates from OpenAPI spec
- Enhanced error handling
- Performance improvements with httpx

### What You'll Keep
- Stable, battle-tested codebase
- Familiar API patterns
- All current integrations work unchanged
- No migration effort required

---

## Need Help?

- **Current SDK Issues**: [GitHub Issues](https://github.com/team-telnyx/telnyx-python/issues)
- **Documentation**: [Telnyx API Docs](https://developers.telnyx.com/docs/api/v2/overview)  
- **Community**: [Telnyx Slack](https://joinslack.telnyx.com/)
- **Support**: [Telnyx Support](https://telnyx.com/support)

---

*This migration guide will be updated as the 3.0.0-alpha SDK evolves towards stable release.*

## Key Differences Summary

| Aspect | Current SDK (v2.1.6) | 3.0.0-alpha |
|--------|----------------------|-------------|
| **Architecture** | Custom resource classes | Generated with Stainless |
| **Python Support** | Python 3.9+ | Python 3.8+ |
| **HTTP Client** | requests | httpx |
| **Async Support** | None | Native async/await |
| **Type Safety** | Minimal | Full type hints |
| **Configuration** | Global variables | Client instantiation |
| **Error Handling** | Basic exceptions | Comprehensive hierarchy |
| **API Resources** | 148 files | 109 files |
| **Build System** | setup.py | pyproject.toml |
| **Dependencies** | requests, six, PyNaCl | httpx, pydantic, typing-extensions |

The 3.0.0-alpha represents a foundational upgrade that will enable faster development, better maintainability, and access to new Telnyx features as they become available.