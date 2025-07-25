"""
Backlink resource for the Litecard API.
"""

from typing import Dict, Any
from .base import LitecardResource


class Backlink(LitecardResource):
    """
    Backlink resource for managing backlinks.
    """
    
    endpoint = "backlink"
    
    def get_backlink(self, backlink_id: str) -> Dict[str, Any]:
        """
        Get backlink based on backlinkId.
        
        Args:
            backlink_id: Backlink ID
            
        Returns:
            Backlink data
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = f"/api/v1/backlink/{backlink_id}"
        response = self._client._make_request_sync("GET", url)
        
        return response["body"]
    
    async def get_backlink_async(self, backlink_id: str) -> Dict[str, Any]:
        """Get backlink asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = f"/api/v1/backlink/{backlink_id}"
        response = await self._client._make_request_async("GET", url)
        
        return response["body"]
