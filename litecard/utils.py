import re
from uuid import UUID
from typing import Any, Dict, List, Optional, Union, Generator
from urllib.parse import urlencode


def to_snake_case(string: str) -> str:
    """Convert CamelCase to snake_case."""
    # Insert an underscore before any uppercase letter that follows a lowercase letter
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    # Insert an underscore before any uppercase letter that follows a lowercase letter or digit
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def to_camel_case(string: str) -> str:
    """Convert snake_case to camelCase."""
    components = string.split('_')
    return components[0] + ''.join(word.capitalize() for word in components[1:])


def clean_params(params: Dict[str, Any]) -> Dict[str, Any]:
    """Clean parameters by removing None values and converting types."""
    cleaned = {}
    for key, value in params.items():
        if value is not None:
            if isinstance(value, bool):
                cleaned[key] = str(value).lower()
            elif isinstance(value, list):
                # Handle array parameters
                if value:  # Only add non-empty lists
                    cleaned[key] = value
            else:
                cleaned[key] = value
    return cleaned


def build_query_string(params: Dict[str, Any]) -> str:
    """Build a query string from parameters."""
    if not params:
        return ""
    
    query_parts = []
    for key, value in params.items():
        if isinstance(value, list):
            # For array parameters, add each item separately
            for item in value:
                query_parts.append(f"{key}={item}")
        else:
            query_parts.append(f"{key}={value}")
    
    return "?" + "&".join(query_parts) if query_parts else ""


def validate_identifier(identifier: Union[str, UUID], identifier_type: str = "identifier") -> str:
    """Validate and clean an identifier for use in API calls."""
    if isinstance(identifier, UUID):
        # If it's a UUID, convert to string
        identifier = str(identifier)
        
    if not identifier or not isinstance(identifier, str):
        raise ValueError(f"Invalid {identifier_type}: must be a non-empty string")
    
    # Remove leading/trailing whitespace
    identifier = identifier.strip()
    
    if not identifier:
        raise ValueError(f"Invalid {identifier_type}: cannot be empty or whitespace only")
    
    return identifier


def chunk_list(items: List[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    """Split a list into chunks of specified size."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]


def safe_get_nested(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Safely get a nested value from a dictionary using dot notation."""
    keys = path.split('.')
    current = data
    
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    
    return current


def format_pagination_response(response: Dict[str, Any], items_key: str = "items") -> Dict[str, Any]:
    """Format a paginated response to extract pagination info."""
    pagination_info = {
        'total_count': response.get('total_count'),
        'offset': response.get('offset', 0),
        'limit': response.get('limit', 50),
        'items': response.get(items_key, [])
    }
    
    return pagination_info


def build_api_url(base_url: str, path: str) -> str:
    """Build a complete API URL."""
    base_url = base_url.rstrip('/')
    path = path.lstrip('/')
    return f"{base_url}/{path}"


def extract_items_from_response(response: Any, items_key: str = "items") -> List[Dict[str, Any]]:
    """Extract items from a Litecard API response."""
    if isinstance(response, dict):
        # Try common keys first
        for key in [items_key, "data", "results", "records"]:
            if key in response:
                return response[key]
        # Single item response
        return [response]
    elif isinstance(response, list):
        return response
    else:
        return []


def validate_currency(currency: str) -> str:
    """Validate currency code."""
    if not currency or not isinstance(currency, str):
        raise ValueError("Currency must be a non-empty string")
    
    currency = currency.strip().upper()
    
    # Common ISO currency codes - expand as needed
    allowed_currencies = [
        "USD", "EUR", "GBP", "JPY", "CHF", "CAD", "AUD", "NZD", 
        "SEK", "NOK", "DKK", "SGD", "HKD", "MXN", "BRL", "ARS",
        "CLP", "COP", "PEN", "UYU", "MYR", "PHP", "THB", "INR",
        "PKR", "BDT", "LKR", "NPR", "AED", "SAR", "QAR", "KWD",
        "BHD", "OMR", "JOD", "ILS", "TRY", "ZAR", "NGN", "KES",
        "GHS", "MAD", "EGP", "CNY", "KRW", "TWD", "RUB", "PLN",
        "CZK", "HUF", "RON", "BGN", "HRK", "UAH", "KZT"
    ]
    
    if currency not in allowed_currencies:
        raise ValueError(f"Currency '{currency}' not supported.")
    
    return currency


def validate_country_code(country_code: str) -> str:
    """Validate ISO 3166-1 alpha-2 country code."""
    if not country_code or not isinstance(country_code, str):
        raise ValueError("Country code must be a non-empty string")
    
    country_code = country_code.strip().upper()
    
    if len(country_code) != 2:
        raise ValueError(f"Country code must be exactly 2 characters, got '{country_code}'")
    
    # This is a subset - in production, you'd want a complete list
    # or use a library like pycountry
    common_country_codes = [
        "US", "GB", "CA", "AU", "NZ", "IE", "SG", "HK", "JP", "KR",
        "CN", "TW", "IN", "PK", "BD", "LK", "NP", "MY", "TH", "PH",
        "VN", "ID", "AE", "SA", "QA", "KW", "BH", "OM", "JO", "IL",
        "TR", "EG", "ZA", "NG", "KE", "GH", "MA", "BR", "AR", "CL",
        "CO", "PE", "UY", "MX", "FR", "DE", "IT", "ES", "PT", "NL",
        "BE", "AT", "CH", "SE", "NO", "DK", "FI", "IS", "PL", "CZ",
        "HU", "RO", "BG", "HR", "RS", "SI", "SK", "EE", "LV", "LT",
        "RU", "UA", "BY", "KZ", "GE", "AM", "AZ"
    ]
    
    if country_code not in common_country_codes:
        # Still allow it but log a warning
        import logging
        logger = logging.getLogger(__name__)
        logger.warning(f"Country code '{country_code}' is not in the common list but will be accepted")
    
    return country_code


def validate_email(email: str) -> str:
    """Basic email validation."""
    if not email or not isinstance(email, str):
        raise ValueError("Email must be a non-empty string")
    
    email = email.strip().lower()
    
    # Basic regex for email validation
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    if not email_pattern.match(email):
        raise ValueError(f"Invalid email format: '{email}'")
    
    return email


def validate_phone_number(phone: str) -> str:
    """Basic phone number validation and normalization."""
    if not phone or not isinstance(phone, str):
        raise ValueError("Phone number must be a non-empty string")
    
    # Remove common formatting characters
    phone = re.sub(r'[\s\-\(\)\.]', '', phone)
    
    # Ensure it starts with + for international format
    if not phone.startswith('+'):
        # Assume US number if no country code
        if len(phone) == 10 and phone[0] in '23456789':
            phone = '+1' + phone
        else:
            raise ValueError("Phone number must include country code (e.g., +1 for US)")
    
    # Basic validation - must be digits after the +
    if not re.match(r'^\+\d{7,15}$', phone):
        raise ValueError(f"Invalid phone number format: '{phone}'")
    
    return phone


def format_datetime(dt: Any) -> str:
    """Format datetime for API requests."""
    from datetime import datetime
    
    if isinstance(dt, str):
        return dt
    elif isinstance(dt, datetime):
        return dt.isoformat()
    else:
        raise ValueError(f"Cannot format datetime from type {type(dt)}")


def parse_datetime(dt_str: str) -> Any:
    """Parse datetime string from API response."""
    from datetime import datetime
    
    if not dt_str:
        return None
    
    # Try common formats
    for fmt in [
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d"
    ]:
        try:
            return datetime.strptime(dt_str, fmt)
        except ValueError:
            continue
    
    # If all else fails, return the string
    return dt_str


def validate_url(url: str) -> str:
    """Validate URL format."""
    if not url or not isinstance(url, str):
        raise ValueError("URL must be a non-empty string")
    
    url = url.strip()
    
    # Basic URL validation
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    if not url_pattern.match(url):
        raise ValueError(f"Invalid URL format: '{url}'")
    
    return url


def mask_sensitive_data(data: Any, fields_to_mask: Optional[List[str]] = None) -> Any:
    """Mask sensitive data in logs or error messages."""
    if fields_to_mask is None:
        fields_to_mask = [
            'password', 'token', 'api_key', 'secret', 'authorization',
            'card_number', 'cvv', 'pin', 'ssn', 'bank_account'
        ]
    
    if isinstance(data, dict):
        masked = {}
        for key, value in data.items():
            if any(field in key.lower() for field in fields_to_mask):
                if isinstance(value, str) and len(value) > 4:
                    masked[key] = value[:2] + '*' * (len(value) - 4) + value[-2:]
                else:
                    masked[key] = '***'
            elif isinstance(value, (dict, list)):
                masked[key] = mask_sensitive_data(value, fields_to_mask)
            else:
                masked[key] = value
        return masked
    elif isinstance(data, list):
        return [mask_sensitive_data(item, fields_to_mask) for item in data]
    else:
        return data


def deep_merge_dicts(base: Dict[str, Any], update: Dict[str, Any]) -> Dict[str, Any]:
    """Deep merge two dictionaries."""
    result = base.copy()
    
    for key, value in update.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = value
    
    return result
