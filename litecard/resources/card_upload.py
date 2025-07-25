"""
Card Upload resource for the Litecard API.
"""

from typing import Dict, Any, List, Union, Optional
from .base import LitecardResource, PaginatedResponse


class CardUpload(LitecardResource):
    """
    Card Upload resource for managing bulk card uploads via CSV.
    """
    
    endpoint = "cards/upload"
    
    def upload_csv(self, upload_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Upload a CSV file to create cards.
        
        Args:
            upload_data: Upload configuration including file, template ID, mappings, etc.
            
        Returns:
            Upload response with group ID
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = "/api/v1/cards/upload/csv"
        response = self._client._make_request_sync(
            "POST",
            url,
            json_data=upload_data
        )
        return response
    
    def list_upload_groups(
        self,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        paginated: bool = False
    ) -> Union[List[Dict[str, Any]], PaginatedResponse]:
        """
        Get the list of card upload groups.
        
        Args:
            limit: Maximum number of groups to return
            next_token: Token for pagination
            paginated: Return PaginatedResponse instead of list
            
        Returns:
            List of upload groups or paginated response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        params = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        
        url = "/api/v1/cards/upload/groups"
        response = self._client._make_request_sync("GET", url, params=params)
        
        if paginated:
            # Extract pagination data and create PaginatedResponse
            groups = response.get("groups", [])
            next_token = response.get("next")
            return PaginatedResponse(
                items=groups,
                limit=params.get("limit", 10),
                next_token=next_token
            )
        
        return response.get("groups", [])
    
    def list_uploads_by_group(
        self,
        group_id: str,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        paginated: bool = False
    ) -> Union[List[Dict[str, Any]], PaginatedResponse]:
        """
        Get the list of card uploads for a specific group.
        
        Args:
            group_id: Upload group ID
            limit: Maximum number of uploads to return
            next_token: Token for pagination
            paginated: Return PaginatedResponse instead of list
            
        Returns:
            List of card uploads or paginated response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        params = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        
        url = f"/api/v1/cards/upload/groups/{group_id}"
        response = self._client._make_request_sync("GET", url, params=params)
        
        if paginated:
            # Extract pagination data and create PaginatedResponse
            uploads = response.get("uploads", [])
            next_token = response.get("next")
            return PaginatedResponse(
                items=uploads,
                limit=params.get("limit", 10),
                next_token=next_token
            )
        
        return response.get("uploads", [])
    
    # Async methods
    
    async def upload_csv_async(self, upload_data: Dict[str, Any]) -> Dict[str, Any]:
        """Upload CSV file asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = "/api/v1/cards/upload/csv"
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data=upload_data
        )
        return response
    
    async def list_upload_groups_async(
        self,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        paginated: bool = False
    ) -> Union[List[Dict[str, Any]], PaginatedResponse]:
        """List upload groups asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        params = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        
        url = "/api/v1/cards/upload/groups"
        response = await self._client._make_request_async("GET", url, params=params)
        
        if paginated:
            # Extract pagination data and create PaginatedResponse
            groups = response.get("groups", [])
            next_token = response.get("next")
            return PaginatedResponse(
                items=groups,
                limit=params.get("limit", 10),
                next_token=next_token
            )
        
        return response.get("groups", [])
    
    async def list_uploads_by_group_async(
        self,
        group_id: str,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        paginated: bool = False
    ) -> Union[List[Dict[str, Any]], PaginatedResponse]:
        """List uploads by group asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        params = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        
        url = f"/api/v1/cards/upload/groups/{group_id}"
        response = await self._client._make_request_async("GET", url, params=params)
        
        if paginated:
            # Extract pagination data and create PaginatedResponse
            uploads = response.get("uploads", [])
            next_token = response.get("next")
            return PaginatedResponse(
                items=uploads,
                limit=params.get("limit", 10),
                next_token=next_token
            )
        
        return response.get("uploads", [])
