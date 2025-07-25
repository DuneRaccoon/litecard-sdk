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
