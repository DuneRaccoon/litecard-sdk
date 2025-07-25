# Litecard Python SDK

A comprehensive Python SDK for integrating with the Litecard API. Create and manage digital wallet cards (Apple Wallet, Google Pay, Samsung Wallet) programmatically.

## Features

- 🎫 **Digital Wallet Cards**: Create and manage cards for Apple Wallet, Google Pay, and Samsung Wallet
- 🔄 **Async/Sync Support**: Full support for both synchronous and asynchronous programming
- 📝 **Type Safety**: Built with Pydantic for robust type checking and validation
- 🚀 **Production Ready**: Includes authentication, rate limiting, retries, and error handling
- 📊 **Analytics**: Track card downloads, scans, and user engagement
- 🔔 **Notifications**: Send push notifications and emails to card holders
- 📋 **Templates**: Manage card templates and bulk operations
- 🔒 **Security**: Token caching and automatic refresh

## Installation

```bash
pip install litecard-sdk
```

## Quick Start

### Basic Usage

```python
from litecard import LitecardClient

# Initialize client with your credentials
client = LitecardClient(
    username="your-username@litecard.com.au",
    password="your-password",
    base_url="https://bff-api.demo.litecard.io",  # Demo environment
    tenant="litecard"  # Optional
)

# Create a digital wallet card
card_response = client.cards.create_card(
    template_id="your-template-id",
    card_payload={
        "firstName": "John",
        "lastName": "Doe",
        "email": "john@example.com",
        "phone": "+61400000000"
    },
    options={
        "emailInvitationEnabled": True
    }
)

print(f"Card created! ID: {card_response.card_id}")
print(f"Apple Wallet: {card_response.apple_link}")
print(f"Google Pay: {card_response.google_link}")

# Close the client when done
client.close()
```

### Async Usage

```python
import asyncio
from litecard import LitecardAsyncClient

async def create_card_async():
    client = LitecardAsyncClient(
        username="your-username@litecard.com.au",
        password="your-password",
        base_url="https://bff-api.demo.litecard.io"
    )
    
    # Refresh token for async client
    await client._refresh_token_async()
    
    # Create card asynchronously
    card_response = await client.cards.create_card_async(
        template_id="your-template-id",
        card_payload={
            "firstName": "Jane",
            "lastName": "Smith",
            "email": "jane@example.com"
        }
    )
    
    print(f"Async card created! ID: {card_response.card_id}")
    
    await client.close()

# Run async function
asyncio.run(create_card_async())
```

## Demo Environment

For testing, use the demo environment with the provided credentials:

```python
from litecard import LitecardClient

USERNAME = "your_username"
PASSWORD = "your_password"

client = LitecardClient(
    username=USERNAME,
    password=PASSWORD,
    base_url="https://bff-api.demo.litecard.io"
)

# Use demo template ID
card_response = client.cards.create_card(
    template_id="roo5JkXsvf2Cx-0IsVFY1",  # Demo template
    card_payload={
        "firstName": "Demo",
        "lastName": "User",
        "email": "demo@example.com",
        "XXXid": "123456789",
        "expiry": "2024-12-31T00:00:00.000Z"
    },
    options={"emailInvitationEnabled": True}
)
```

## Core Features

### 📱 Card Management

```python
# Create a card
card = client.cards.create_card(template_id="...", card_payload={...})

# Update card data
client.cards.update_card(card_id="...", card_payload={"points": 500})

# Get card details
card = client.cards.get_card("card-id")

# Change card status
client.cards.set_card_status("card-id", "INACTIVE")

# List cards by template
cards = client.cards.list_cards_by_template("template-id", limit=10)
```

### 🎨 Template Management

```python
# List templates
templates = client.templates.list_templates(limit=10)

# Get template details
template = client.templates.get("template-id")

# Create a new template
template = client.templates.create_template({
    "name": "My Loyalty Card",
    "description": "Customer loyalty program",
    # ... template configuration
})

# Update template
client.templates.update_template({
    "id": "template-id",
    # ... updated configuration
})
```

### 🔍 Scanning & Analytics

```python
# Scan a card barcode
scan_result = client.scans.scan_barcode("barcode-value")
print(f"Scanned card: {scan_result.card.id}")

# List recent scans
scans = client.scans.list_scans(limit=50)

# Get download statistics
stats = client.passes.get_downloads_count(duration="PAST_7_DAYS")
```

### 🔔 Notifications

```python
# Send push notification
client.notifications.send_notification({
    "cardIds": ["card-id-1", "card-id-2"],
    "notification": {
        "title": "Special Offer!",
        "message": "Get 20% off your next purchase",
        "dataFieldKey": "notificationKey"
    },
    "options": {
        "pushNotification": True,
        "email": True
    }
})

# Send email reminders
client.notifications.send_reminders(
    email_template="litecardpass",
    template_id="template-id"
)
```

### 📊 Pagination

```python
# Simple pagination
templates = client.templates.list_templates(limit=10, paginated=True)
print(f"Found {len(templates.items)} templates")
if templates.has_more:
    next_page = client.templates.list_templates(
        limit=10, 
        next_token=templates.next_token
    )

# Automatic pagination with generator
for template in client.templates.paginate(limit=10):
    print(f"Template: {template.name}")
```

### 🚀 Bulk Operations

```python
# Upload CSV to create multiple cards
upload_result = client.card_uploads.upload_csv({
    "file": "data:text/csv;base64,...",  # Base64 encoded CSV
    "templateId": "template-id",
    "headerMappings": {
        "name": "Full Name",
        "email": "Email Address"
    },
    "fileName": "customers.csv",
    "emailInvitationEnabled": True
})

# Check upload status
groups = client.card_uploads.list_upload_groups(limit=10)
```

## Error Handling

The SDK provides comprehensive error handling:

```python
from litecard import LitecardAPIError, AuthenticationError, RateLimitError

try:
    card = client.cards.create_card(...)
except AuthenticationError:
    print("Invalid credentials")
except RateLimitError as e:
    print(f"Rate limited. Retry after {e.retry_after} seconds")
except LitecardAPIError as e:
    print(f"API Error: {e.message}")
    print(f"Status Code: {e.status_code}")
```

## Configuration

### Environment URLs

- **Demo**: `https://bff-api.demo.litecard.io`
- **Production**: `https://bff-api.litecard.io`

### Client Options

```python
client = LitecardClient(
    username="your-username",
    password="your-password", 
    base_url="https://bff-api.demo.litecard.io",
    timeout=60.0,              # Request timeout in seconds
    max_retries=5,             # Max retry attempts
    tenant="litecard",         # Optional tenant
    active_business_id="..."   # Optional business ID
)
```

## Utilities

The SDK includes helpful utility functions:

```python
from litecard.utils import build_welcome_url, validate_email, format_phone_international

# Build welcome page URL
welcome_url = build_welcome_url("download-id", environment="demo")

# Validate email
is_valid = validate_email("user@example.com")

# Format phone number
formatted = format_phone_international("0400000000", "+61")
```

## Models and Type Safety

All API responses are typed using Pydantic models:

```python
from litecard import Card, Template, SignUpResponse

# Type-safe card creation
response: SignUpResponse = client.cards.create_card(...)
print(response.card_id)  # IDE autocomplete and type checking

# Access card properties
card: Card = client.cards.get_card("card-id")
print(card.status)  # CardStatus enum
print(card.created_at)  # datetime object
```

## Advanced Features

### Custom Headers

```python
# Set custom business context
client = LitecardClient(
    username="...",
    password="...",
    active_business_id="your-business-id"  # Automatically added to headers
)
```

### Token Management

```python
# Tokens are automatically cached and refreshed
# Manual refresh (rarely needed):
client._refresh_token_sync()

# Check token validity
if client._is_token_valid():
    print("Token is valid")
```

### Resource Access

```python
# All resources are available on the client
client.cards          # Card operations
client.templates      # Template operations  
client.scans          # Scanning operations
client.notifications  # Notification operations
client.downloads      # Download URL operations
client.certificates   # Certificate management
client.webhooks       # Webhook management
client.exports        # Data export operations
# ... and more
```

## Examples

Check out the `examples/` directory for comprehensive examples:

- `basic_usage.py` - Complete examples for common operations
- Card creation and management
- Template operations
- Async/await patterns
- Notification sending
- Error handling

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions about the Litecard API or this SDK:

- 📖 API Documentation: [Litecard API Docs](https://bff-api.demo.litecard.io/api/v1/swagger)
- 🐛 Issues: [GitHub Issues](https://github.com/DuneRaccoon/litecard-sdk/issues)
- 📧 Email: [Support](mailto:support@litecard.com.au)

## Changelog

### v0.1.0
- Initial release
- Complete API coverage
- Async/sync support
- Type safety with Pydantic
- Comprehensive error handling
- Token caching and refresh
- Pagination support
- Utility functions
