"""
Utility functions for the Litecard API SDK.
"""

from typing import Any, Dict, List, Union, Optional


def clean_params(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Clean parameters by removing None values and converting values to strings.
    
    Args:
        params: Dictionary of parameters
        
    Returns:
        Cleaned parameters dictionary
    """
    cleaned = {}
    for key, value in params.items():
        if value is not None:
            # Convert lists to comma-separated strings
            if isinstance(value, list):
                cleaned[key] = ",".join(str(v) for v in value)
            # Convert booleans to lowercase strings
            elif isinstance(value, bool):
                cleaned[key] = str(value).lower()
            else:
                cleaned[key] = str(value)
    return cleaned


def extract_items_from_response(response: Union[List[Dict[str, Any]], Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Extract items from a response that could be either a list or a dict with items.
    
    Args:
        response: API response
        
    Returns:
        List of items
    """
    if isinstance(response, list):
        return response
    elif isinstance(response, dict):
        # Try common keys for lists of items
        for key in ['results', 'items', 'data', 'templates', 'cards', 'scans', 'certificates', 'groups', 'uploads']:
            if key in response and isinstance(response[key], list):
                return response[key]
        
        # If response has a single item that looks like a resource, wrap it in a list
        if 'id' in response or 'templateId' in response or 'cardId' in response:
            return [response]
    
    return []


def build_welcome_url(download_id: str, environment: str = "demo") -> str:
    """
    Build a welcome/download URL for a given download ID.
    
    Args:
        download_id: Download ID from card creation response
        environment: Environment ("demo" or "live")
        
    Returns:
        Complete welcome URL
    """
    if environment == "demo":
        return f"https://main.demo.litecard.io/welcome?id={download_id}"
    elif environment == "live":
        return f"https://litecard.io/welcome?id={download_id}"
    else:
        raise ValueError("Environment must be 'demo' or 'live'")


def validate_email(email: str) -> bool:
    """
    Basic email validation.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if email appears valid
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """
    Basic phone number validation.
    
    Args:
        phone: Phone number to validate
        
    Returns:
        True if phone appears valid
    """
    import re
    # Remove all non-digit characters
    digits_only = re.sub(r'\D', '', phone)
    # Check if it's between 7 and 15 digits (international standard)
    return 7 <= len(digits_only) <= 15


def create_card_payload(email: str, first_name: str, last_name: str, 
                       phone: str = None, **dynamic_fields) -> Dict[str, Any]:
    """
    Create a card payload dictionary matching API documentation requirements.
    
    Args:
        email: Email address (required if phone not provided)
        first_name: First name
        last_name: Last name  
        phone: Phone number (required if email not provided)
        **dynamic_fields: Additional dynamic fields based on template configuration
        
    Returns:
        Card payload dictionary for use in card creation/updates
        
    Example:
        payload = create_card_payload(
            email="user@example.com",
            first_name="John",
            last_name="Doe",
            barcode_value="123456789",  # Dynamic field
            membership_level="Gold",    # Dynamic field
            points_balance=2500         # Dynamic field
        )
    """
    if not email and not phone:
        raise ValueError("Either email or phone must be provided")
        
    payload = {
        "firstName": first_name,
        "lastName": last_name
    }
    
    if email:
        payload["email"] = email
    if phone:
        payload["phone"] = phone
        
    # Add dynamic fields
    payload.update(dynamic_fields)
    
    return payload


def format_phone_international(phone: str, country_code: str = "+61") -> str:
    """
    Format phone number with international prefix.
    
    Args:
        phone: Phone number
        country_code: Country code (default Australian +61)
        
    Returns:
        Formatted phone number
    """
    import re
    # Remove all non-digit characters
    digits_only = re.sub(r'\D', '', phone)
    
    # Remove leading 0 if present (common in Australian numbers)
    if digits_only.startswith('0'):
        digits_only = digits_only[1:]
    
    return f"{country_code}{digits_only}"


def chunk_list(items: List[Any], chunk_size: int) -> List[List[Any]]:
    """
    Split a list into chunks of specified size.
    
    Args:
        items: List to chunk
        chunk_size: Size of each chunk
        
    Returns:
        List of chunks
    """
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def safe_get(dictionary: Dict[str, Any], key: str, default: Any = None) -> Any:
    """
    Safely get a value from a dictionary with nested key support.
    
    Args:
        dictionary: Dictionary to search
        key: Key or dot-separated path (e.g., "data.user.name")
        default: Default value if key not found
        
    Returns:
        Value or default
    """
    keys = key.split('.')
    value = dictionary
    
    try:
        for k in keys:
            value = value[k]
        return value
    except (KeyError, TypeError):
        return default


def merge_dicts(*dicts: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge multiple dictionaries, with later ones taking precedence.
    
    Args:
        *dicts: Dictionaries to merge
        
    Returns:
        Merged dictionary
    """
    result = {}
    for d in dicts:
        if d:
            result.update(d)
    return result


def snake_to_camel(snake_str: str) -> str:
    """
    Convert snake_case to camelCase.
    
    Args:
        snake_str: String in snake_case
        
    Returns:
        String in camelCase
    """
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


def camel_to_snake(camel_str: str) -> str:
    """
    Convert camelCase to snake_case.
    
    Args:
        camel_str: String in camelCase
        
    Returns:
        String in snake_case
    """
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def convert_keys_to_camel(data: Union[Dict[str, Any], List[Any]]) -> Union[Dict[str, Any], List[Any]]:
    """
    Recursively convert dictionary keys from snake_case to camelCase.
    
    Args:
        data: Data structure to convert
        
    Returns:
        Data with camelCase keys
    """
    if isinstance(data, dict):
        return {snake_to_camel(k): convert_keys_to_camel(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_keys_to_camel(item) for item in data]
    else:
        return data


def convert_keys_to_snake(data: Union[Dict[str, Any], List[Any]]) -> Union[Dict[str, Any], List[Any]]:
    """
    Recursively convert dictionary keys from camelCase to snake_case.
    
    Args:
        data: Data structure to convert
        
    Returns:
        Data with snake_case keys
    """
    if isinstance(data, dict):
        return {camel_to_snake(k): convert_keys_to_snake(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_keys_to_snake(item) for item in data]
    else:
        return data


def create_location_override(location_id: str, latitude: str, longitude: str, 
                           lock_screen_message: str, order: int = 0, 
                           usage: List[str] = None) -> Dict[str, Any]:
    """
    Create a location override for template overrides (Apple Wallet location-based notifications).
    
    Based on the API documentation location format for template overrides.
    
    Args:
        location_id: Unique identifier for the location
        latitude: Latitude coordinate as string (e.g., "-37.806454120154115")
        longitude: Longitude coordinate as string (e.g., "144.9864286613659")
        lock_screen_message: Message to show on lock screen when near location
        order: Display order (default: 0)
        usage: List of wallet types (default: ["APPLE_WALLET"])
        
    Returns:
        Location dictionary for use in template overrides
        
    Example:
        location = create_location_override(
            location_id="office-location",
            latitude="-37.806454120154115",
            longitude="144.9864286613659",
            lock_screen_message="Come and visit our office for a free gift!"
        )
    """
    if usage is None:
        usage = ["APPLE_WALLET"]
        
    return {
        "id": location_id,
        "lat": latitude,
        "lon": longitude,
        "apple": {
            "lockScreenMessage": lock_screen_message
        },
        "order": order,
        "usage": usage
    }


def create_template_overrides_with_locations(locations: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Create template overrides dictionary with locations for card creation/updates.
    
    Args:
        locations: List of location dictionaries (from create_location_override)
        
    Returns:
        Template overrides dictionary for use in card operations
        
    Example:
        location1 = create_location_override(
            "office", "-37.806454120154115", "144.9864286613659", 
            "Visit our office!"
        )
        location2 = create_location_override(
            "store", "-33.867487", "151.206990", 
            "Check out our store!"
        )
        
        overrides = create_template_overrides_with_locations([location1, location2])
    """
    return {
        "locations": locations
    }


def create_notification_payload(card_ids: List[str], title: str, message: str,
                              email: bool = False, push_notification: bool = True,
                              send_all: bool = False, send_time: str = "",
                              data_field_key: str = "notificationKey") -> Dict[str, Any]:
    """
    Create notification payload matching API documentation format.
    
    Args:
        card_ids: List of card IDs (ignored if send_all is True)
        title: Notification title
        message: Notification message
        email: Send email notification (default: False)
        push_notification: Send push notification (default: True)
        send_all: Send to all active users (default: False)
        send_time: Optional scheduled send time in ISO format (default: "")
        data_field_key: Data field key for notification (default: "notificationKey")
        
    Returns:
        Notification payload dictionary for use with send_notification_via_queue
        
    Example:
        payload = create_notification_payload(
            card_ids=["card-123", "card-456"],
            title="Special Offer",
            message="Get 20% off your next purchase!",
            push_notification=True,
            email=False
        )
    """
    return {
        "cardIds": card_ids if not send_all else [],
        "notification": {
            "title": title,
            "message": message,
            "dataFieldKey": data_field_key,
            "sendTime": send_time
        },
        "options": {
            "email": email,
            "pushNotification": push_notification,
            "sendAll": send_all
        }
    }
