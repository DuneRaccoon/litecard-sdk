"""
Notification resource for the Litecard API.
"""

from typing import Dict, Any, List, Union, Optional
from .base import LitecardResource, PaginatedResponse
from ..models_ import NotificationRequest


class Notification(LitecardResource):
    """
    Notification resource for managing push notifications and emails.
    """
    
    endpoint = "notification"
    
    def send_notification(self, notification_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send instant notification (rate limited to 5 per second).
        
        Args:
            notification_data: Notification configuration
            
        Returns:
            Success response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        response = self._client._make_request_sync(
            "POST",
            self._build_url(),
            json_data=notification_data
        )
        
        return response
    
    def send_notification_via_queue(self, notification_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send notification via queue (can take up to 60 seconds).
        
        Args:
            notification_data: Notification configuration
            
        Returns:
            Success response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = "/api/v1/queue/notification"
        response = self._client._make_request_sync(
            "POST",
            url,
            json_data=notification_data
        )
        
        return response
    
    def send_reminders(
        self, 
        email_template: str,
        template_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send email reminders.
        
        Args:
            email_template: Email template to use
            template_id: Optional template ID to filter cards
            
        Returns:
            Success response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data = {"emailTemplate": email_template}
        if template_id:
            request_data["templateId"] = template_id
        
        url = self._build_url(suffix="reminder")
        response = self._client._make_request_sync(
            "POST",
            url,
            json_data=request_data
        )
        
        return response
    
    # Async methods
    
    async def send_notification_async(self, notification_data: Dict[str, Any]) -> Dict[str, Any]:
        """Send instant notification asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        response = await self._client._make_request_async(
            "POST",
            self._build_url(),
            json_data=notification_data
        )
        
        return response
    
    async def send_notification_via_queue_async(self, notification_data: Dict[str, Any]) -> Dict[str, Any]:
        """Send notification via queue asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = "/api/v1/queue/notification"
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data=notification_data
        )
        
        return response
    
    async def send_reminders_async(
        self,
        email_template: str,
        template_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Send email reminders asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data = {"emailTemplate": email_template}
        if template_id:
            request_data["templateId"] = template_id
        
        url = self._build_url(suffix="reminder")
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data=request_data
        )
        
        return response
