"""
Basic tests for the Litecard SDK structure and imports.
"""

import pytest
from unittest.mock import Mock, patch


def test_imports():
    """Test that all main components can be imported."""
    from litecard import LitecardClient, LitecardAsyncClient
    from litecard import LitecardAPIError, AuthenticationError
    from litecard.models_ import Card, Template, SignUpResponse
    from litecard.utils import build_welcome_url, validate_email
    
    assert LitecardClient is not None
    assert LitecardAsyncClient is not None


def test_client_initialization():
    """Test client initialization with different configurations."""
    from litecard import LitecardClient
    
    # Test with username/password
    client = LitecardClient(
        username="test@example.com",
        password="password123",
        base_url="https://api.test.com"
    )
    assert client.username == "test@example.com"
    assert client.base_url == "https://api.test.com"
    
    # Test with API token
    client = LitecardClient(
        api_token="test-token",
        base_url="https://api.test.com"
    )
    assert client._api_token == "test-token"


def test_client_validation():
    """Test client initialization validation."""
    from litecard import LitecardClient
    
    # Should raise error if no credentials provided
    with pytest.raises(ValueError, match="Either api_token or both username and password are required"):
        LitecardClient()
    
    # Should raise error if only username provided
    with pytest.raises(ValueError):
        LitecardClient(username="test@example.com")


def test_resource_initialization():
    """Test that all resources are properly initialized."""
    from litecard import LitecardClient
    
    client = LitecardClient(
        username="test@example.com",
        password="password123"
    )
    
    # Check that all resources are available
    assert hasattr(client, 'cards')
    assert hasattr(client, 'templates')
    assert hasattr(client, 'scans')
    assert hasattr(client, 'notifications')
    assert hasattr(client, 'downloads')
    assert hasattr(client, 'certificates')
    assert hasattr(client, 'webhooks')
    assert hasattr(client, 'exports')


def test_model_creation():
    """Test that Pydantic models can be created."""
    from litecard.models_ import SignUpResponse, Card, Template
    
    # Test SignUpResponse model
    response = SignUpResponse(
        card_id="12345",
        success=True,
        download_id="download-123"
    )
    assert response.card_id == "12345"
    assert response.success is True
    
    # Test model field aliases work
    card_data = {
        "id": "card-123",
        "formId": "form-123",
        "templateId": "template-123",
        "businessId": "business-123",
        "createdAt": "2024-01-01T00:00:00Z",
        "status": "ACTIVE"
    }
    card = Card(**card_data)
    assert card.id == "card-123"
    assert card.form_id == "form-123"  # Snake case property
    assert card.template_id == "template-123"


def test_utils():
    """Test utility functions."""
    from litecard.utils import build_welcome_url, validate_email, format_phone_international
    
    # Test welcome URL building
    demo_url = build_welcome_url("test-download-id", "demo")
    assert demo_url == "https://main.demo.litecard.io/welcome?id=test-download-id"
    
    live_url = build_welcome_url("test-download-id", "live")
    assert live_url == "https://litecard.io/welcome?id=test-download-id"
    
    # Test email validation
    assert validate_email("test@example.com") is True
    assert validate_email("invalid-email") is False
    
    # Test phone formatting
    formatted = format_phone_international("0400000000", "+61")
    assert formatted == "+61400000000"


def test_clean_params():
    """Test parameter cleaning utility."""
    from litecard.utils import clean_params
    
    params = {
        "limit": 10,
        "next": "token",
        "enabled": True,
        "disabled": False,
        "empty": None,
        "tags": ["tag1", "tag2"]
    }
    
    cleaned = clean_params(params)
    assert cleaned["limit"] == "10"
    assert cleaned["enabled"] == "true"
    assert cleaned["disabled"] == "false"
    assert cleaned["tags"] == "tag1,tag2"
    assert "empty" not in cleaned  # None values removed


def test_extract_items():
    """Test item extraction from API responses."""
    from litecard.utils import extract_items_from_response
    
    # Test list response
    list_response = [{"id": "1"}, {"id": "2"}]
    items = extract_items_from_response(list_response)
    assert len(items) == 2
    
    # Test dict response with 'results' key
    dict_response = {"results": [{"id": "1"}, {"id": "2"}]}
    items = extract_items_from_response(dict_response)
    assert len(items) == 2
    
    # Test dict response with single item
    single_response = {"id": "1", "name": "test"}
    items = extract_items_from_response(single_response)
    assert len(items) == 1
    assert items[0]["id"] == "1"


if __name__ == "__main__":
    pytest.main([__file__])
