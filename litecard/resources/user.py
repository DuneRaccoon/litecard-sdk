"""
User resource for the Litecard API.
"""

from typing import Dict, Any, List
from .base import LitecardResource
from ..models import User as UserModel


class User(LitecardResource):
    """
    User resource for managing users.
    """
    
    endpoint = "users"
    model_class = UserModel
    
    def list_users(self) -> Dict[str, Any]:
        """
        Get the list of users.
        
        Returns:
            User listing with roles, access, and metadata
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        response = self._client._make_request_sync("GET", self._build_url())
        return response
    
    async def list_users_async(self) -> Dict[str, Any]:
        """Get the list of users asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        response = await self._client._make_request_async("GET", self._build_url())
        return response
