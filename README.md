# Litecard Python SDK

A Python SDK for interacting with the Litecard API.

## Installation

```bash
pip install litecard-sdk
```

## Quick Start

### Synchronous Client

```python
from litecard import LitecardClient

# Initialize the client
client = LitecardClient(api_token="your-api-token")

# Example usage will be added once API endpoints are defined
# client.cards.list()
# client.transactions.get("transaction-id")

# Don't forget to close the client when done
client.close()
```

### Asynchronous Client

```python
import asyncio
from litecard import LitecardAsyncClient

async def main():
    # Initialize the async client
    client = LitecardAsyncClient(api_token="your-api-token")
    
    # Example usage will be added once API endpoints are defined
    # cards = await client.cards.list_async()
    # transaction = await client.transactions.get_async("transaction-id")
    
    # Don't forget to close the client when done
    await client.close()

asyncio.run(main())
```

## Features

- **Type Safety**: Built with Pydantic for robust data validation and type hints
- **Async Support**: Both synchronous and asynchronous clients available
- **Rate Limiting**: Built-in rate limiting using leaky bucket algorithm
- **Automatic Retries**: Configurable automatic retries with exponential backoff
- **Pagination**: Support for both offset/limit and cursor-based pagination
- **Error Handling**: Comprehensive error handling with specific exception types

## Configuration

### Client Options

- `api_token` (required): Your Litecard API token
- `base_url`: API base URL (default: https://api.litecard.com)
- `timeout`: Request timeout in seconds (default: 60.0)
- `max_retries`: Maximum number of retries for failed requests (default: 5)

## Error Handling

The SDK provides specific exception types for different error scenarios:

```python
from litecard import (
    LitecardAPIError,      # Base exception for all API errors
    AuthenticationError,   # 401 errors
    RateLimitError,       # 429 errors
    ValidationError,      # 422 errors
    NotFoundError,        # 404 errors
    ServerError          # 5xx errors
)

try:
    # API call
    pass
except AuthenticationError:
    print("Invalid API token")
except RateLimitError as e:
    print(f"Rate limit exceeded. Retry after {e.retry_after} seconds")
except LitecardAPIError as e:
    print(f"API error: {e.message}")
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/DuneRaccoon/litecard-sdk.git
cd litecard-sdk

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black litecard
isort litecard
```

### Type Checking

```bash
mypy litecard
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
