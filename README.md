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
# Create a card with basic payload (matches API docs format)
card = client.cards.create_card(
    template_id="your-template-id",
    card_payload={
        "email": "user@example.com",  # Required: email or phone
        "firstName": "John",
        "lastName": "Doe"
    },
    options={
        "emailInvitationEnabled": True  # Send email with download link
    }
)

# Create card with multi-tier template support
card = client.cards.create_card(
    template_id="your-template-id",
    tier="premium",  # For multi-tier templates
    card_payload={
        "email": "user@example.com",
        "firstName": "Jane",
        "lastName": "Smith"
    }
)

# Create card with location-based notifications (template overrides)
card = client.cards.create_card(
    template_id="your-template-id",
    card_payload={
        "email": "user@example.com",
        "firstName": "John",
        "lastName": "Citizen"
    },
    options={
        "emailInvitationEnabled": False
    },
    template_overrides={
        "locations": [{
            "id": "office-location",
            "lat": "-37.806454120154115",
            "lon": "144.9864286613659",
            "apple": {
                "lockScreenMessage": "Come and visit our office for a free gift!"
            },
            "order": 0,
            "usage": ["APPLE_WALLET"]
        }]
    }
)

# Update card data
client.cards.update_card(
    card_id="card-123",
    card_payload={
        "firstName": "Jane",  # Update name
        "points": 500  # Update dynamic field
    }
)

# Update card with template overrides (e.g., location changes)
client.cards.update_card(
    card_id="card-123",
    template_overrides={
        "locations": [{
            "id": "new-location",
            "lat": "-33.867487",
            "lon": "151.206990",
            "apple": {
                "lockScreenMessage": "Visit our Sydney store!"
            },
            "order": 0,
            "usage": ["APPLE_WALLET"]
        }]
    }
)

# Get card details
card = client.cards.get_card("card-id")

# Change card status (ACTIVE, INACTIVE, DELETED)
client.cards.set_card_status("card-id", "INACTIVE")  # Deactivate (can be reactivated)
client.cards.set_card_status("card-id", "DELETED")   # Delete (permanent)
client.cards.set_card_status("card-id", "ACTIVE")    # Reactivate (only if previously INACTIVE)

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
# Send notification via queue (recommended - matches API docs)
client.notifications.send_notification_via_queue({
    "cardIds": [
        "card-id-1",  # Can be left blank if setting sendAll to true
        "card-id-2"
    ],
    "notification": {
        "title": "Special Offer!",
        "message": "Get 20% off your next purchase",
        "dataFieldKey": "notificationKey",  # Default key, leave unless customized
        "sendTime": ""  # Optional - for scheduled notifications
    },
    "options": {
        "email": False,  # Send email notification
        "pushNotification": True,  # Send push notification
        "sendAll": False  # Send to all active users (overwrites cardIds)
    }
})

# Send to all users with scheduled time
client.notifications.send_notification_via_queue({
    "cardIds": [],  # Empty when sendAll is true
    "notification": {
        "title": "Maintenance Notice",
        "message": "Our store will be closed tomorrow for maintenance",
        "dataFieldKey": "notificationKey",
        "sendTime": "2025-01-15T09:00:00Z"  # ISO format for scheduled sending
    },
    "options": {
        "email": True,
        "pushNotification": True,
        "sendAll": True  # Send to all active users
    }
})

# Send instant notification (rate limited to 5 per second)
client.notifications.send_notification({
    "cardIds": ["card-id-1"],
    "notification": {
        "title": "Urgent Alert",
        "message": "Your order is ready for pickup!",
        "dataFieldKey": "notificationKey"
    },
    "options": {
        "pushNotification": True,
        "email": False
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
- **Production/Enterprise**: `https://bff-api.enterprise.litecard.io`

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

### Master/Sub Account Configuration

Litecard supports a Master/Sub account structure where one set of credentials can access multiple accounts. This matches the API documentation's authentication method.

```python
# Method 1: Use sub account credentials directly (if sub account has login credentials)
client = LitecardClient(
    username="sub-account-username",
    password="sub-account-password",
    base_url="https://bff-api.demo.litecard.io"
)

# Method 2: Use master account with x-active-business-id header
# Authenticate with master account credentials and specify sub account business ID
client = LitecardClient(
    username="master-account-username",
    password="master-account-password",
    base_url="https://bff-api.demo.litecard.io",
    active_business_id="sub-account-business-id"  # Found in Litecard dashboard -> 'Manage Accounts'
)

# The active_business_id automatically adds the x-active-business-id header to all requests
# This allows master account to operate on behalf of the sub account
```

## Utilities

The SDK includes helpful utility functions that match the API documentation patterns:

```python
from litecard import (
    create_card_payload,
    create_location_override,
    create_template_overrides_with_locations,
    create_notification_payload,
    build_welcome_url,
    validate_email,
    format_phone_international
)

# Create card payload matching API docs format
card_payload = create_card_payload(
    email="user@example.com",
    first_name="John",
    last_name="Doe",
    barcode_value="123456789",  # Dynamic field
    membership_level="Gold",    # Dynamic field
    points_balance=2500         # Dynamic field
)

# Create location override for Apple Wallet notifications
location = create_location_override(
    location_id="office-location",
    latitude="-37.806454120154115",
    longitude="144.9864286613659",
    lock_screen_message="Come and visit our office for a free gift!"
)

# Create template overrides with locations
template_overrides = create_template_overrides_with_locations([location])

# Create notification payload matching API docs format
notification_payload = create_notification_payload(
    card_ids=["card-123", "card-456"],
    title="Special Offer",
    message="Get 20% off your next purchase!",
    push_notification=True,
    email=False
)

# Use with SDK methods
card = client.cards.create_card(
    template_id="template-123",
    card_payload=card_payload,
    template_overrides=template_overrides
)

client.notifications.send_notification_via_queue(notification_payload)

# Other utility functions
welcome_url = build_welcome_url("download-id", environment="demo")
is_valid = validate_email("user@example.com")
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

### Card Status Management

**Understanding Deactivating vs Deleting** (per API documentation):

```python
# INACTIVE: Deactivating the card
# - Expires the card on user's device, rendering it unable to be scanned
# - Leaves open the possibility of re-activating the pass later
# - Status can be changed back to ACTIVE
client.cards.set_card_status("card-id", "INACTIVE")

# Later, reactivate if needed
client.cards.set_card_status("card-id", "ACTIVE")

# DELETED: Deleting the card  
# - Also expires the card on user's device
# - Completely removes the ability to re-enable the pass in the future
# - This action is PERMANENT and irreversible
client.cards.set_card_status("card-id", "DELETED")
```

### Dynamic Fields

Dynamic fields are defined by the template and can be required or optional. The key to use in `cardPayload` is derived from the field label with no spaces and in camelCase.

```python
# Example: If template has field labeled "Barcode Value", use key "barcodeValue"
card = client.cards.create_card(
    template_id="template-id",
    card_payload={
        "email": "user@example.com",
        "firstName": "John",
        "lastName": "Doe",
        "barcodeValue": "123456789",  # Dynamic field
        "membershipLevel": "Gold",   # Another dynamic field
        "points": 1000               # Numeric dynamic field
    }
)
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
