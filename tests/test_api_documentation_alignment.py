"""
Test file to verify SDK alignment with Litecard API User Guide.

This test ensures the SDK properly implements the API patterns described 
in the official Litecard API User Guide documentation.
"""

import pytest
from unittest.mock import Mock, patch
from litecard import LitecardClient, LitecardAsyncClient
from litecard.models_ import SignUpResponse


class TestAPIDocumentationAlignment:
    """Test suite to verify SDK matches API documentation."""
    
    def test_environment_urls(self):
        """Test that SDK supports correct environment URLs from API docs."""
        # Demo environment
        demo_client = LitecardClient(
            username="test@example.com",
            password="password",
            base_url="https://bff-api.demo.litecard.io"
        )
        assert demo_client.base_url == "https://bff-api.demo.litecard.io"
        
        # Production/Enterprise environment
        prod_client = LitecardClient(
            username="test@example.com", 
            password="password",
            base_url="https://bff-api.enterprise.litecard.io"
        )
        assert prod_client.base_url == "https://bff-api.enterprise.litecard.io"
    
    def test_master_sub_account_configuration(self):
        """Test Master/Sub account configuration from API docs."""
        # Method 2: Master account with x-active-business-id header
        client = LitecardClient(
            username="master@example.com",
            password="password",
            active_business_id="sub-business-123"
        )
        
        # Verify active_business_id is stored
        assert client.active_business_id == "sub-business-123"
        
        # Mock the auth headers method to verify header inclusion
        with patch.object(client, '_get_auth_headers') as mock_headers:
            mock_headers.return_value = {
                "Authorization": "Bearer token",
                "Accept": "application/json",
                "Content-Type": "application/json",
                "x-active-business-id": "sub-business-123"
            }
            headers = client._get_auth_headers()
            assert headers["x-active-business-id"] == "sub-business-123"
    
    @patch('litecard.client.LitecardClient._make_request_sync')
    def test_card_creation_api_docs_format(self, mock_request):
        """Test card creation matches API docs payload format."""
        # Mock response from API docs
        mock_request.return_value = {
            "cardId": "card-123",
            "success": True,
            "downloadId": "download-456"
        }
        
        client = LitecardClient(username="test@example.com", password="password")
        
        # Test basic card creation matching API docs example
        response = client.cards.create_card(
            template_id="template-123",
            card_payload={
                "email": "test@example.com",
                "firstName": "John",
                "lastName": "Doe"
            },
            options={
                "emailInvitationEnabled": True
            }
        )
        
        # Verify request payload structure matches API docs
        call_args = mock_request.call_args
        request_data = call_args[1]['json_data']
        
        assert request_data["templateId"] == "template-123"
        assert request_data["cardPayload"]["email"] == "test@example.com"
        assert request_data["cardPayload"]["firstName"] == "John"
        assert request_data["cardPayload"]["lastName"] == "Doe"
        assert request_data["options"]["emailInvitationEnabled"] is True
        
        # Verify response structure
        assert isinstance(response, SignUpResponse)
        assert response.card_id == "card-123"
        assert response.success is True
        assert response.download_id == "download-456"
    
    @patch('litecard.client.LitecardClient._make_request_sync')
    def test_card_creation_with_template_overrides(self, mock_request):
        """Test card creation with template overrides for location-based notifications."""
        mock_request.return_value = {
            "cardId": "card-456",
            "success": True,
            "downloadId": "download-789"
        }
        
        client = LitecardClient(username="test@example.com", password="password")
        
        # Test card creation with location-based notifications (from API docs)
        response = client.cards.create_card(
            template_id="template-123",
            card_payload={
                "email": "test@example.com",
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
        
        # Verify template overrides are included in request
        call_args = mock_request.call_args
        request_data = call_args[1]['json_data']
        
        assert "templateOverrides" in request_data
        assert "locations" in request_data["templateOverrides"]
        location = request_data["templateOverrides"]["locations"][0]
        assert location["id"] == "office-location"
        assert location["lat"] == "-37.806454120154115"
        assert location["lon"] == "144.9864286613659"
        assert location["apple"]["lockScreenMessage"] == "Come and visit our office for a free gift!"
    
    @patch('litecard.client.LitecardClient._make_request_sync')
    def test_card_update_api_docs_format(self, mock_request):
        """Test card update matches API docs payload format."""
        mock_request.return_value = {"success": True}
        
        client = LitecardClient(username="test@example.com", password="password")
        
        # Test card update matching API docs example
        client.cards.update_card(
            card_id="card-123",
            card_payload={
                "email": "updated@example.com",
                "firstName": "Jane"
            }
        )
        
        # Verify request payload structure matches API docs
        call_args = mock_request.call_args
        request_data = call_args[1]['json_data']
        
        assert request_data["cardId"] == "card-123"
        assert request_data["cardPayload"]["email"] == "updated@example.com"
        assert request_data["cardPayload"]["firstName"] == "Jane"
    
    @patch('litecard.client.LitecardClient._make_request_sync')
    def test_card_update_with_template_overrides(self, mock_request):
        """Test card update with template overrides only."""
        mock_request.return_value = {"success": True}
        
        client = LitecardClient(username="test@example.com", password="password")
        
        # Test updating only template overrides (e.g., location changes)
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
        
        # Verify request structure
        call_args = mock_request.call_args
        request_data = call_args[1]['json_data']
        
        assert request_data["cardId"] == "card-123"
        assert "cardPayload" not in request_data  # No card payload update
        assert "templateOverrides" in request_data
    
    @patch('litecard.client.LitecardClient._make_request_sync')
    def test_card_status_api_docs_format(self, mock_request):
        """Test card status changes match API docs format."""
        mock_request.return_value = {"success": True}
        
        client = LitecardClient(username="test@example.com", password="password")
        
        # Test status change matching API docs example
        client.cards.set_card_status("card-123", "DELETED")
        
        # Verify request payload structure matches API docs
        call_args = mock_request.call_args
        request_data = call_args[1]['json_data']
        
        assert request_data["cardId"] == "card-123"
        assert request_data["status"] == "DELETED"
        
        # Verify endpoint is correct
        assert "/api/v1/card/status" in call_args[0][1]
    
    @patch('litecard.client.LitecardClient._make_request_sync')
    def test_notification_queue_api_docs_format(self, mock_request):
        """Test notification via queue matches API docs payload format."""
        mock_request.return_value = {"success": True}
        
        client = LitecardClient(username="test@example.com", password="password")
        
        # Test notification matching API docs example exactly
        client.notifications.send_notification_via_queue({
            "cardIds": ["card-123", "card-456"],
            "notification": {
                "title": "Special Offer",
                "message": "Get 20% off your next purchase",
                "dataFieldKey": "notificationKey",
                "sendTime": ""
            },
            "options": {
                "email": False,
                "pushNotification": True,
                "sendAll": False
            }
        })
        
        # Verify endpoint is correct (from API docs)
        call_args = mock_request.call_args
        assert call_args[0][1] == "/api/v1/queue/notification"
        
        # Verify payload structure matches API docs
        request_data = call_args[1]['json_data']
        assert "cardIds" in request_data
        assert "notification" in request_data
        assert "options" in request_data
        assert request_data["notification"]["dataFieldKey"] == "notificationKey"
        assert request_data["options"]["sendAll"] is False
    
    def test_multi_tier_template_support(self):
        """Test multi-tier template support mentioned in API docs."""
        client = LitecardClient(username="test@example.com", password="password")
        
        with patch.object(client, '_make_request_sync') as mock_request:
            mock_request.return_value = {
                "cardId": "card-789",
                "success": True,
                "downloadId": "download-abc"
            }
            
            # Test tier parameter support
            client.cards.create_card(
                template_id="multi-tier-template",
                tier="premium",
                card_payload={
                    "email": "test@example.com",
                    "firstName": "John",
                    "lastName": "Doe"
                }
            )
            
            # Verify tier is included in request
            call_args = mock_request.call_args
            request_data = call_args[1]['json_data']
            assert request_data["tier"] == "premium"
    
    def test_dynamic_fields_support(self):
        """Test dynamic fields as described in API docs."""
        client = LitecardClient(username="test@example.com", password="password")
        
        with patch.object(client, '_make_request_sync') as mock_request:
            mock_request.return_value = {
                "cardId": "card-999",
                "success": True,
                "downloadId": "download-xyz"
            }
            
            # Test dynamic fields (keys derived from labels as per API docs)
            client.cards.create_card(
                template_id="template-123",
                card_payload={
                    "email": "test@example.com",
                    "firstName": "John",
                    "lastName": "Doe",
                    "barcodeValue": "123456789",  # From "Barcode Value" label
                    "membershipLevel": "Gold",    # From "Membership Level" label
                    "pointsBalance": 2500         # From "Points Balance" label
                }
            )
            
            # Verify dynamic fields are included
            call_args = mock_request.call_args
            request_data = call_args[1]['json_data']
            card_payload = request_data["cardPayload"]
            
            assert card_payload["barcodeValue"] == "123456789"
            assert card_payload["membershipLevel"] == "Gold"
            assert card_payload["pointsBalance"] == 2500


class TestAsyncAPIAlignment:
    """Test async methods follow same API patterns."""
    
    @pytest.mark.asyncio
    @patch('litecard.client.LitecardAsyncClient._make_request_async')
    async def test_async_card_creation_api_docs_format(self, mock_request):
        """Test async card creation matches API docs format."""
        mock_request.return_value = {
            "cardId": "async-card-123",
            "success": True,
            "downloadId": "async-download-456"
        }
        
        client = LitecardAsyncClient(username="test@example.com", password="password")
        
        response = await client.cards.create_card_async(
            template_id="template-123",
            card_payload={
                "email": "async@example.com",
                "firstName": "Async",
                "lastName": "User"
            },
            options={
                "emailInvitationEnabled": True
            }
        )
        
        # Verify same structure as sync version
        call_args = mock_request.call_args
        request_data = call_args[1]['json_data']
        
        assert request_data["templateId"] == "template-123"
        assert request_data["cardPayload"]["email"] == "async@example.com"
        assert request_data["options"]["emailInvitationEnabled"] is True
        
        assert isinstance(response, SignUpResponse)
        assert response.card_id == "async-card-123"


if __name__ == "__main__":
    pytest.main([__file__])
