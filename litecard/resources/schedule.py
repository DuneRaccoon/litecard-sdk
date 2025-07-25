"""
Schedule resource for the Litecard API.
"""

from typing import Dict, Any
from .base import LitecardResource


class Schedule(LitecardResource):
    """
    Schedule resource for managing scheduled tasks.
    """
    
    endpoint = "schedule"
    
    def generate_upload_url(self) -> Dict[str, Any]:
        """
        Generate a pre-signed URL to upload CSV files for a scheduled task.
        
        Returns:
            Pre-signed URL and CSV ID
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = "/api/v1/schedule/upload"
        response = self._client._make_request_sync("GET", url)
        return response
    
    def schedule_task(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Schedule a task.
        
        Args:
            task_data: Task configuration including execute time and CSV IDs
            
        Returns:
            Task scheduling response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        response = self._client._make_request_sync(
            "POST",
            self._build_url(),
            json_data=task_data
        )
        return response
    
    # Async methods
    
    async def generate_upload_url_async(self) -> Dict[str, Any]:
        """Generate upload URL asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = "/api/v1/schedule/upload"
        response = await self._client._make_request_async("GET", url)
        return response
    
    async def schedule_task_async(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """Schedule a task asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        response = await self._client._make_request_async(
            "POST",
            self._build_url(),
            json_data=task_data
        )
        return response
