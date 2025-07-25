#!/usr/bin/env python3
"""
Simple verification script to test SDK alignment with API documentation.
"""

import sys
import os
sys.path.insert(0, '/Users/benjaminherro/github/litecard-sdk')

def test_imports():
    """Test basic imports."""
    try:
        import litecard
        print("✓ Main SDK import successful")
        
        from litecard import create_card_payload, create_location_override, create_notification_payload
        print("✓ Utility function imports successful")
        
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_utility_functions():
    """Test utility functions match API docs format."""
    try:
        from litecard import create_card_payload, create_location_override, create_notification_payload
        
        # Test card payload creation (API docs format)
        payload = create_card_payload(
            email="test@example.com",
            first_name="John", 
            last_name="Doe",
            barcode_value="123456"
        )
        assert "email" in payload
        assert "firstName" in payload
        assert "lastName" in payload
        assert "barcodeValue" in payload
        print("✓ Card payload creation matches API docs format")
        
        # Test location override (API docs format)
        location = create_location_override(
            location_id="test-location",
            latitude="-37.806454120154115",
            longitude="144.9864286613659",
            lock_screen_message="Test message"
        )
        assert location["id"] == "test-location"
        assert location["lat"] == "-37.806454120154115"
        assert location["lon"] == "144.9864286613659"
        assert location["apple"]["lockScreenMessage"] == "Test message"
        assert location["usage"] == ["APPLE_WALLET"]
        print("✓ Location override creation matches API docs format")
        
        # Test notification payload (API docs format)
        notification = create_notification_payload(
            card_ids=["card-123"],
            title="Test Title",
            message="Test message"
        )
        assert "cardIds" in notification
        assert "notification" in notification
        assert "options" in notification
        assert notification["notification"]["dataFieldKey"] == "notificationKey"
        print("✓ Notification payload creation matches API docs format")
        
        return True
    except Exception as e:
        print(f"❌ Utility function error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_client_configuration():
    """Test client configuration for different environments."""
    try:
        import litecard
        
        # Test demo environment
        demo_client = litecard.LitecardClient(
            username="test@example.com",
            password="password",
            base_url="https://bff-api.demo.litecard.io"
        )
        assert demo_client.base_url == "https://bff-api.demo.litecard.io"
        print("✓ Demo environment configuration successful")
        
        # Test production environment  
        prod_client = litecard.LitecardClient(
            username="test@example.com",
            password="password",
            base_url="https://bff-api.enterprise.litecard.io"
        )
        assert prod_client.base_url == "https://bff-api.enterprise.litecard.io"
        print("✓ Production environment configuration successful")
        
        # Test master/sub account configuration
        master_client = litecard.LitecardClient(
            username="master@example.com",
            password="password",
            active_business_id="sub-business-123"
        )
        assert master_client.active_business_id == "sub-business-123"
        print("✓ Master/sub account configuration successful")
        
        return True
    except Exception as e:
        print(f"❌ Client configuration error: {e}")
        return False

def test_card_methods():
    """Test card methods support template overrides."""
    try:
        import litecard
        from unittest.mock import Mock, patch
        
        client = litecard.LitecardClient(username="test@example.com", password="password")
        
        # Check that create_card method has template_overrides parameter
        import inspect
        create_card_sig = inspect.signature(client.cards.create_card)
        assert "template_overrides" in create_card_sig.parameters
        print("✓ create_card method supports template_overrides")
        
        # Check that update_card method has template_overrides parameter
        update_card_sig = inspect.signature(client.cards.update_card)
        assert "template_overrides" in update_card_sig.parameters
        print("✓ update_card method supports template_overrides")
        
        return True
    except Exception as e:
        print(f"❌ Card methods error: {e}")
        return False

def main():
    """Run all verification tests."""
    print("=== SDK API Documentation Alignment Verification ===\n")
    
    tests = [
        ("Import Tests", test_imports),
        ("Utility Functions", test_utility_functions),
        ("Client Configuration", test_client_configuration),
        ("Card Methods", test_card_methods)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        if test_func():
            passed += 1
        
    print(f"\n=== Results: {passed}/{total} tests passed ===")
    
    if passed == total:
        print("🎉 All SDK alignment tests passed! The SDK properly follows the API documentation.")
    else:
        print("❌ Some tests failed. Please check the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
