"""
SubBusiness resource for the Litecard API.
"""

from typing import Dict, Any
from .base import LitecardResource


class SubBusiness(LitecardResource):
    """
    SubBusiness resource for managing sub businesses.
    """
    
    endpoint = "subBusiness"
    
    def create_sub_business(self, business_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a sub business.
        
        Args:
            business_data: Sub business configuration data
            
        Returns:
            Created sub business data
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        response = self._client._make_request_sync(
            "POST",
            self._build_url(),
            json_data=business_data
        )
        return response
    
    async def create_sub_business_async(self, business_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a sub business asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        response = await self._client._make_request_async(
            "POST",
            self._build_url(),
            json_data=business_data
        )
        return response
