"""
Webhook resource for the Litecard API.
"""

from typing import Dict, Any
from .base import LitecardResource
from ..models import WebhookRegistrationRequest


class Webhook(LitecardResource):
    """
    Webhook resource for managing client webhooks.
    """
    
    endpoint = "webhook/external"
    
    def register_webhook(self, webhook_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Register a client webhook for supported events.
        
        Args:
            webhook_data: Webhook configuration including URL, auth, and events
            
        Returns:
            Webhook registration response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        response = self._client._make_request_sync(
            "POST",
            self._build_url(),
            json_data=webhook_data
        )
        return response
    
    def delete_webhook(self, webhook_id: str) -> Dict[str, Any]:
        """
        Delete a customer webhook.
        
        Args:
            webhook_id: Webhook ID to delete
            
        Returns:
            Delete response
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
    
    # Async methods
    
    async def register_webhook_async(self, webhook_data: Dict[str, Any]) -> Dict[str, Any]:
        """Register a webhook asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        response = await self._client._make_request_async(
            "POST",
            self._build_url(),
            json_data=webhook_data
        )
        return response
    
    async def delete_webhook_async(self, webhook_id: str) -> Dict[str, Any]:
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
