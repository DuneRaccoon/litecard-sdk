"""
Webhook resource for the Litecard API.
"""

from typing import Dict, Any, List, Optional
from .base import LitecardResource
from ..models_ import WebhookRegistrationRequest
from ..request_types import (
    RegisterWebhookRequest,
    DeleteWebhookRequest,
    WebhookAuthConfig,
    SuccessResponse,
)


class Webhook(LitecardResource):
    """
    Webhook resource for managing client webhooks.
    """
    
    endpoint = "webhook/external"
    
    def register_webhook(
        self,
        webhook_url: str,
        auth_type: str,
        auth_config: WebhookAuthConfig,
        events: List[str],
        method: str = "POST",
        provider: Optional[str] = None
    ) -> SuccessResponse:
        """
        Register a client webhook for supported events.
        
        Args:
            webhook_url: URL endpoint for webhook delivery
            auth_type: Authentication type ("API_KEY", "BEARER_TOKEN", "BASIC_AUTH", "NONE")
            auth_config: Authentication configuration based on auth_type
            events: List of events to subscribe to
            method: HTTP method for webhook calls (default: "POST")
            provider: Optional provider schema identifier
            
        Returns:
            Webhook registration response
            
        Example:
            ```python
            from litecard.request_types import WebhookAuthConfig
            
            # Register webhook with API key authentication
            auth_config = WebhookAuthConfig(
                apiKey="your-api-key-here"
            )
            
            response = webhook_resource.register_webhook(
                webhook_url="https://your-domain.com/webhook",
                auth_type="API_KEY",
                auth_config=auth_config,
                events=["CARD_CREATED", "CARD_SCANNED", "CARD_DOWNLOADED"]
            )
            
            # Register webhook with bearer token
            auth_config = WebhookAuthConfig(
                bearerToken="your-bearer-token"
            )
            
            response = webhook_resource.register_webhook(
                webhook_url="https://your-domain.com/webhook",
                auth_type="BEARER_TOKEN",
                auth_config=auth_config,
                events=["CARD_CREATED", "NOTIFICATION_SENT"]
            )
            
            # Register webhook with basic authentication
            auth_config = WebhookAuthConfig(
                basicAuth={
                    "username": "webhook_user",
                    "password": "secure_password"
                }
            )
            
            response = webhook_resource.register_webhook(
                webhook_url="https://your-domain.com/webhook",
                auth_type="BASIC_AUTH",
                auth_config=auth_config,
                events=["CARD_SCANNED"]
            )
            
            # Register webhook with custom headers
            auth_config = WebhookAuthConfig(
                customHeaders={
                    "X-API-Key": "your-key",
                    "X-Client-ID": "your-client-id"
                }
            )
            
            response = webhook_resource.register_webhook(
                webhook_url="https://your-domain.com/webhook",
                auth_type="NONE",  # Using custom headers instead
                auth_config=auth_config,
                events=["CARD_CREATED", "CARD_UPDATED"]
            )
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data: RegisterWebhookRequest = {
            "webhookUrl": webhook_url,
            "authType": auth_type,
            "authConfig": auth_config,
            "events": events,
            "method": method
        }
        
        if provider:
            request_data["provider"] = provider
        
        response = self._client._make_request_sync(
            "POST",
            self._build_url(),
            json_data=request_data
        )
        return response
    
    def delete_webhook(self, webhook_id: str) -> SuccessResponse:
        """
        Delete a customer webhook.
        
        Args:
            webhook_id: Webhook ID to delete
            
        Returns:
            Delete response
            
        Example:
            ```python
            response = webhook_resource.delete_webhook("webhook_123")
            print(f"Webhook deleted: {response['success']}")
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        params = {"webhookId": webhook_id}
        response = self._client._make_request_sync(
            "DELETE",
            self._build_url(),
            params=params
        )
        return response
    
    def list_webhooks(self) -> List[Dict[str, Any]]:
        """
        List all registered webhooks for the business.
        
        Returns:
            List of webhook configurations
            
        Example:
            ```python
            webhooks = webhook_resource.list_webhooks()
            
            for webhook in webhooks:
                print(f"Webhook ID: {webhook['id']}")
                print(f"URL: {webhook['webhookUrl']}")
                print(f"Events: {webhook['events']}")
                print(f"Status: {webhook['status']}")
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        response = self._client._make_request_sync(
            "GET",
            self._build_url()
        )
        return response.get("webhooks", [])
    
    def test_webhook(
        self, 
        webhook_id: str, 
        event_type: str = "CARD_CREATED"
    ) -> SuccessResponse:
        """
        Send a test event to a registered webhook.
        
        Args:
            webhook_id: Webhook ID to test
            event_type: Type of event to simulate for testing
            
        Returns:
            Test response indicating success/failure
            
        Example:
            ```python
            # Test webhook with a card creation event
            result = webhook_resource.test_webhook(
                webhook_id="webhook_123",
                event_type="CARD_CREATED"
            )
            
            if result['success']:
                print("Webhook test successful!")
            else:
                print(f"Webhook test failed: {result.get('error')}")
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data = {
            "webhookId": webhook_id,
            "eventType": event_type
        }
        
        url = self._build_url(suffix="test")
        response = self._client._make_request_sync(
            "POST",
            url,
            json_data=request_data
        )
        return response
    
    def get_webhook_events(self) -> List[str]:
        """
        Get list of available webhook events.
        
        Returns:
            List of supported event types
            
        Example:
            ```python
            events = webhook_resource.get_webhook_events()
            print("Available webhook events:")
            for event in events:
                print(f"  - {event}")
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = self._build_url(suffix="events")
        response = self._client._make_request_sync("GET", url)
        return response.get("events", [])
    
    # Async methods
    
    async def register_webhook_async(
        self,
        webhook_url: str,
        auth_type: str,
        auth_config: WebhookAuthConfig,
        events: List[str],
        method: str = "POST",
        provider: Optional[str] = None
    ) -> SuccessResponse:
        """Register a webhook asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data: RegisterWebhookRequest = {
            "webhookUrl": webhook_url,
            "authType": auth_type,
            "authConfig": auth_config,
            "events": events,
            "method": method
        }
        
        if provider:
            request_data["provider"] = provider
        
        response = await self._client._make_request_async(
            "POST",
            self._build_url(),
            json_data=request_data
        )
        return response
    
    async def delete_webhook_async(self, webhook_id: str) -> SuccessResponse:
        """Delete a webhook asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        params = {"webhookId": webhook_id}
        response = await self._client._make_request_async(
            "DELETE",
            self._build_url(),
            params=params
        )
        return response
    
    async def list_webhooks_async(self) -> List[Dict[str, Any]]:
        """List all registered webhooks asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        response = await self._client._make_request_async(
            "GET",
            self._build_url()
        )
        return response.get("webhooks", [])
    
    async def test_webhook_async(
        self, 
        webhook_id: str, 
        event_type: str = "CARD_CREATED"
    ) -> SuccessResponse:
        """Send a test event to a registered webhook asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data = {
            "webhookId": webhook_id,
            "eventType": event_type
        }
        
        url = self._build_url(suffix="test")
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data=request_data
        )
        return response
    
    async def get_webhook_events_async(self) -> List[str]:
        """Get list of available webhook events asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = self._build_url(suffix="events")
        response = await self._client._make_request_async("GET", url)
        return response.get("events", [])


# Available webhook events for reference
WEBHOOK_EVENTS = [
    "CARD_CREATED",
    "CARD_UPDATED", 
    "CARD_DELETED",
    "CARD_SCANNED",
    "CARD_DOWNLOADED",
    "CARD_STATUS_CHANGED",
    "NOTIFICATION_SENT",
    "NOTIFICATION_FAILED",
    "TEMPLATE_CREATED",
    "TEMPLATE_UPDATED",
    "TEMPLATE_DELETED",
    "FORM_SUBMITTED",
    "EXPORT_COMPLETED",
    "CERTIFICATE_EXPIRED",
    "BUSINESS_UPDATED"
]

# Authentication types for reference
WEBHOOK_AUTH_TYPES = [
    "NONE",         # No authentication
    "API_KEY",      # API key in header or query param
    "BEARER_TOKEN", # Bearer token in Authorization header
    "BASIC_AUTH",   # Basic authentication with username/password
    "CUSTOM"        # Custom headers
]
