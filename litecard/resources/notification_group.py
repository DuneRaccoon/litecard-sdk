"""
Notification Group resource for the Litecard API.
"""

from typing import Dict, Any, List, Union, Optional
from datetime import datetime
from .base import LitecardResource, PaginatedResponse
from ..models_ import NotificationGroup as NotificationGroupModel


class NotificationGroup(LitecardResource):
    """
    Notification Group resource for managing notification groups.
    """
    
    endpoint = "notification-groups"
    model_class = NotificationGroupModel
    
    def list_notification_groups(
        self,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        start_date_time: Optional[datetime] = None,
        end_date_time: Optional[datetime] = None,
        paginated: bool = False
    ) -> Union[List['NotificationGroup'], PaginatedResponse['NotificationGroup']]:
        """
        List all notification groups associated with a business ID.
        
        Args:
            limit: Maximum number of groups to return
            next_token: Token for pagination
            start_date_time: Filter by start date
            end_date_time: Filter by end date
            paginated: Return PaginatedResponse instead of list
            
        Returns:
            List of notification groups or paginated response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        params = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        if start_date_time:
            params["startDateTime"] = start_date_time.isoformat()
        if end_date_time:
            params["endDateTime"] = end_date_time.isoformat()
        
        return self.list(paginated=paginated, **params)
    
    def cancel_notifications(self, notification_group_id: str) -> Dict[str, Any]:
        """
        Cancel notifications by group ID.
        
        Args:
            notification_group_id: Notification group ID
            
        Returns:
            Success response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = f"/api/v1/notification-groups/{notification_group_id}/cancel"
        response = self._client._make_request_sync("PUT", url)
        return response
    
    # Async methods
    
    async def list_notification_groups_async(
        self,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        start_date_time: Optional[datetime] = None,
        end_date_time: Optional[datetime] = None,
        paginated: bool = False
    ) -> Union[List['NotificationGroup'], PaginatedResponse['NotificationGroup']]:
        """List notification groups asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        params = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        if start_date_time:
            params["startDateTime"] = start_date_time.isoformat()
        if end_date_time:
            params["endDateTime"] = end_date_time.isoformat()
        
        return await self.list_async(paginated=paginated, **params)
    
    async def cancel_notifications_async(self, notification_group_id: str) -> Dict[str, Any]:
        """Cancel notifications by group ID asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = f"/api/v1/notification-groups/{notification_group_id}/cancel"
        response = await self._client._make_request_async("PUT", url)
        return response
