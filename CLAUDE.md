# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Testing
- `make test` - Run all tests on all supported Python versions using tox
- `pipenv run tox -e py38` - Run tests for specific Python version
- `pipenv run tox -e py38 -- tests/path/to/test.py` - Run specific test file
- `pipenv run tox -e py38 -- tests/path/to/test.py::TestClass::test_method` - Run specific test
- `make ci` - Run tests with coverage using pytest

### Code Quality
- `make lint` - Run linting (flake8, isort, pylint errors-only)  
- `make fmt` - Format code using Black and isort
- `make fmtcheck` - Check code formatting without making changes
- `make pylintcheck` - Run full pylint analysis

### Setup
- `make init` - Install pipenv and development dependencies
- `pipenv install --dev` - Install all dependencies for development

## Architecture Overview

### Core Structure
The Telnyx Python SDK follows a resource-oriented architecture similar to Stripe's SDK:

- **`telnyx/`** - Main package containing all SDK code
- **`telnyx/api_resources/`** - API resource classes for each Telnyx API endpoint
- **`telnyx/api_resources/abstract/`** - Base classes defining common resource behaviors
- **`telnyx/telnyx_object.py`** - Base object class with request handling
- **`telnyx/api_requestor.py`** - HTTP client and request logic
- **`telnyx/util.py`** - Utilities including object conversion and reserved word handling

### API Resource Pattern
Each API resource inherits from one or more abstract base classes:
- `CreateableAPIResource` - Resources that can be created via POST
- `ListableAPIResource` - Resources that can be listed/paginated
- `UpdateableAPIResource` - Resources that can be updated via PUT/PATCH  
- `DeletableAPIResource` - Resources that can be deleted
- `SingletonAPIResource` - Resources with only one instance (like Balance)

### Object Conversion System
The SDK automatically converts API responses to appropriate Python objects using:
- `OBJECT_CLASSES` dict in `util.py` mapping record types to classes
- `convert_to_telnyx_object()` function for dynamic object creation
- Reserved word handling (e.g., `from_` parameter becomes `from` in API calls)

### Configuration
Global configuration is set in `telnyx/__init__.py`:
- `api_key` - Authentication (can also be set per-request)
- `api_base` - API base URL (defaults to https://api.telnyx.com)
- `verify_ssl_certs` - SSL verification toggle
- `max_network_retries` - Retry configuration
- `log` - Logging level ('debug' or 'info')

## Adding New API Resources

When adding a new endpoint:

1. Create resource class in `telnyx/api_resources/` inheriting from appropriate abstract classes
2. Add import to `telnyx/api_resources/__init__.py`
3. Add to `OBJECT_CLASSES` dict in `telnyx/util.py`
4. Create tests in `tests/api_resources/`
5. Ensure the resource's `OBJECT_NAME` matches the API's `record_type`

## Testing Infrastructure

- Uses `telnyx-mock` server for testing (must be running on localhost)
- `tests/conftest.py` contains pytest fixtures
- `tests/telnyx_mock.py` and `tests/request_mock.py` provide mocking utilities
- Tests are organized to mirror the `telnyx/api_resources/` structure

## Development Environment

- Python 3.9+ required (supports through 3.12 and PyPy)
- Uses pipenv for dependency management
- Black for code formatting (88 character line limit)
- Supports multiple HTTP clients: requests (preferred), urllib2, pycurl, urlfetch