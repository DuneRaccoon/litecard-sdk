"""
Download resource for the Litecard API.
"""

from typing import Dict, Any
from .base import LitecardResource
from ..models import WelcomeDetails


class Download(LitecardResource):
    """
    Download resource for managing card download URLs.
    """
    
    endpoint = "downloadId"
    model_class = WelcomeDetails
    
    def get_download_urls(self, download_id: str) -> WelcomeDetails:
        """
        Get download URLs based on downloadId.
        
        Args:
            download_id: Download ID
            
        Returns:
            Welcome details with download URLs
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = f"/api/v1/downloadId/{download_id}"
        response = self._client._make_request_sync("GET", url)
        
        return WelcomeDetails(**response["body"])
    
    async def get_download_urls_async(self, download_id: str) -> WelcomeDetails:
        """Get download URLs asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = f"/api/v1/downloadId/{download_id}"
        response = await self._client._make_request_async("GET", url)
        
        return WelcomeDetails(**response["body"])
