"""
Pass resource for the Litecard API.
"""

from typing import Dict, Any, List, Union, Optional
from .base import LitecardResource, PaginatedResponse


class Pass(LitecardResource):
    """
    Pass resource for managing digital wallet passes.
    """
    
    endpoint = "pass"
    
    def list_passes(self, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        List passes associated with business ID.
        
        Args:
            request_data: Request parameters for filtering passes
            
        Returns:
            Pass listing response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        response = self._client._make_request_sync(
            "POST",
            self._build_url(),
            json_data=request_data
        )
        return response
    
    def get_downloads_count(self, duration: str = "PAST_7_DAYS") -> Dict[str, Any]:
        """
        Get pass downloads count for a specific period.
        
        Args:
            duration: Duration (PAST_7_DAYS, PAST_30_DAYS, ALL)
            
        Returns:
            Pass downloads count data
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = "/api/v1/pass/downloads/count"
        params = {"duration": duration}
        response = self._client._make_request_sync("GET", url, params=params)
        return response
    
    def get_download_trend(self, days: int = 7) -> Dict[str, Any]:
        """
        Get pass download trend for a specific period.
        
        Args:
            days: Number of days (7 or 30)
            
        Returns:
            Pass download trend data
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = "/api/v1/pass/downloads/trend"
        params = {"days": days}
        response = self._client._make_request_sync("GET", url, params=params)
        return response
    
    # Async methods
    
    async def list_passes_async(self, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """List passes asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        response = await self._client._make_request_async(
            "POST",
            self._build_url(),
            json_data=request_data
        )
        return response
    
    async def get_downloads_count_async(self, duration: str = "PAST_7_DAYS") -> Dict[str, Any]:
        """Get pass downloads count asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = "/api/v1/pass/downloads/count"
        params = {"duration": duration}
        response = await self._client._make_request_async("GET", url, params=params)
        return response
    
    async def get_download_trend_async(self, days: int = 7) -> Dict[str, Any]:
        """Get pass download trend asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = "/api/v1/pass/downloads/trend"
        params = {"days": days}
        response = await self._client._make_request_async("GET", url, params=params)
        return response
