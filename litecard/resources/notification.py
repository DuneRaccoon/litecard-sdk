"""
Notification resource for the Litecard API.
"""

from typing import Dict, Any, List, Union, Optional
from .base import LitecardResource, PaginatedResponse
from ..models_ import NotificationRequest, NotificationGroup
from ..request_types import (
    SendNotificationRequest,
    SendReminderRequest,
    NotificationPayload,
    NotificationSegments,
    NotificationOptions,
    SuccessResponse,
)


class Notification(LitecardResource):
    """
    Notification resource for managing push notifications and emails.
    """
    
    endpoint = "notification"
    
    def send_notification(
        self,
        notification: NotificationPayload,
        card_ids: Optional[List[str]] = None,
        template_ids: Optional[List[str]] = None,
        segments: Optional[NotificationSegments] = None,
        options: Optional[NotificationOptions] = None
    ) -> SuccessResponse:
        """
        Send instant notification (rate limited to 5 per second).
        
        Args:
            notification: Notification content with title, message, etc.
            card_ids: List of specific card IDs to send to (optional)
            template_ids: List of template IDs to send to all cards (optional)
            segments: Segmentation options (which platforms to include)
            options: Additional sending options (scheduling, priority, etc.)
            
        Returns:
            Success response
            
        Example:
            ```python
            from litecard.request_types import (
                NotificationPayload, 
                NotificationSegments, 
                NotificationOptions
            )
            
            # Create notification content
            notification = NotificationPayload(
                title="Welcome!",
                message="Thanks for joining our loyalty program",
                url="https://example.com/welcome",
                imageUrl="https://example.com/welcome.jpg"
            )
            
            # Configure which platforms to send to
            segments = NotificationSegments(
                includeApple=True,
                includeGoogle=True,
                includeEmail=True
            )
            
            # Send to specific cards
            response = notification_resource.send_notification(
                notification=notification,
                card_ids=["card_123", "card_456"],
                segments=segments
            )
            
            # Or send to all cards from specific templates
            response = notification_resource.send_notification(
                notification=notification,
                template_ids=["template_123"],
                segments=segments
            )
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data: SendNotificationRequest = {
            "notification": notification
        }
        
        if card_ids:
            request_data["cardIds"] = card_ids
        
        if template_ids:
            request_data["templateIds"] = template_ids
        
        if segments:
            request_data["segments"] = segments
        
        if options:
            request_data["options"] = options
        
        response = self._client._make_request_sync(
            "POST",
            self._build_url(),
            json_data=request_data
        )
        
        return response
    
    def send_notification_via_queue(
        self,
        notification: NotificationPayload,
        card_ids: Optional[List[str]] = None,
        template_ids: Optional[List[str]] = None,
        segments: Optional[NotificationSegments] = None,
        options: Optional[NotificationOptions] = None
    ) -> SuccessResponse:
        """
        Send notification via queue (can take up to 60 seconds).
        
        This method is better for large batches of notifications as it doesn't
        have the rate limiting of the instant notification endpoint.
        
        Args:
            notification: Notification content with title, message, etc.
            card_ids: List of specific card IDs to send to (optional)
            template_ids: List of template IDs to send to all cards (optional)
            segments: Segmentation options (which platforms to include)
            options: Additional sending options (scheduling, priority, etc.)
            
        Returns:
            Success response
            
        Example:
            ```python
            from litecard.request_types import NotificationPayload
            
            # Send to many cards via queue
            notification = NotificationPayload(
                title="Big Sale!",
                message="50% off everything this weekend"
            )
            
            response = notification_resource.send_notification_via_queue(
                notification=notification,
                template_ids=["template_123", "template_456"]
            )
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data: SendNotificationRequest = {
            "notification": notification
        }
        
        if card_ids:
            request_data["cardIds"] = card_ids
        
        if template_ids:
            request_data["templateIds"] = template_ids
        
        if segments:
            request_data["segments"] = segments
        
        if options:
            request_data["options"] = options
        
        url = "/api/v1/queue/notification"
        response = self._client._make_request_sync(
            "POST",
            url,
            json_data=request_data
        )
        
        return response
    
    def send_reminders(
        self, 
        email_template: str,
        template_id: Optional[str] = None
    ) -> SuccessResponse:
        """
        Send email reminders.
        
        Args:
            email_template: Email template to use for reminders
            template_id: Optional template ID to filter cards (send only to cards from this template)
            
        Returns:
            Success response
            
        Example:
            ```python
            # Send reminders to all cards using a specific email template
            response = notification_resource.send_reminders(
                email_template="weekly_reminder"
            )
            
            # Send reminders only to cards from a specific template
            response = notification_resource.send_reminders(
                email_template="loyalty_reminder",
                template_id="template_123"
            )
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data: SendReminderRequest = {
            "emailTemplate": email_template
        }
        
        if template_id:
            request_data["templateId"] = template_id
        
        url = self._build_url(suffix="reminder")
        response = self._client._make_request_sync(
            "POST",
            url,
            json_data=request_data
        )
        
        return response
    
    def list_notification_groups(
        self,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        paginated: bool = False
    ) -> Union[List[NotificationGroup], PaginatedResponse[NotificationGroup]]:
        """
        List notification groups (sent notifications history).
        
        Args:
            limit: Maximum number of groups to return
            next_token: Token for pagination
            paginated: Return PaginatedResponse instead of list
            
        Returns:
            List of notification groups or paginated response
            
        Example:
            ```python
            # Get recent notification groups
            groups = notification_resource.list_notification_groups(limit=20)
            
            for group in groups:
                print(f"Notification: {group.title}")
                print(f"Sent to: {group.participants_count} recipients")
                print(f"Status: {group.status}")
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        params = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        
        url = "/api/v1/notification/groups"
        return self.list(url=url, paginated=paginated, model_class=NotificationGroup, **params)
    
    # Async methods
    
    async def send_notification_async(
        self,
        notification: NotificationPayload,
        card_ids: Optional[List[str]] = None,
        template_ids: Optional[List[str]] = None,
        segments: Optional[NotificationSegments] = None,
        options: Optional[NotificationOptions] = None
    ) -> SuccessResponse:
        """Send instant notification asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data: SendNotificationRequest = {
            "notification": notification
        }
        
        if card_ids:
            request_data["cardIds"] = card_ids
        
        if template_ids:
            request_data["templateIds"] = template_ids
        
        if segments:
            request_data["segments"] = segments
        
        if options:
            request_data["options"] = options
        
        response = await self._client._make_request_async(
            "POST",
            self._build_url(),
            json_data=request_data
        )
        
        return response
    
    async def send_notification_via_queue_async(
        self,
        notification: NotificationPayload,
        card_ids: Optional[List[str]] = None,
        template_ids: Optional[List[str]] = None,
        segments: Optional[NotificationSegments] = None,
        options: Optional[NotificationOptions] = None
    ) -> SuccessResponse:
        """Send notification via queue asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data: SendNotificationRequest = {
            "notification": notification
        }
        
        if card_ids:
            request_data["cardIds"] = card_ids
        
        if template_ids:
            request_data["templateIds"] = template_ids
        
        if segments:
            request_data["segments"] = segments
        
        if options:
            request_data["options"] = options
        
        url = "/api/v1/queue/notification"
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data=request_data
        )
        
        return response
    
    async def send_reminders_async(
        self,
        email_template: str,
        template_id: Optional[str] = None
    ) -> SuccessResponse:
        """Send email reminders asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data: SendReminderRequest = {
            "emailTemplate": email_template
        }
        
        if template_id:
            request_data["templateId"] = template_id
        
        url = self._build_url(suffix="reminder")
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data=request_data
        )
        
        return response
    
    async def list_notification_groups_async(
        self,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        paginated: bool = False
    ) -> Union[List[NotificationGroup], PaginatedResponse[NotificationGroup]]:
        """List notification groups asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        params = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        
        url = "/api/v1/notification/groups"
        return await self.list_async(url=url, paginated=paginated, model_class=NotificationGroup, **params)
