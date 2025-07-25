"""
Template resource for the Litecard API.
"""

from typing import Dict, Any, List, Union, Optional
from .base import LitecardResource, PaginatedResponse
from ..models import Template as TemplateModel


class Template(LitecardResource):
    """
    Template resource for managing card templates.
    """
    
    endpoint = "template"
    model_class = TemplateModel
    
    def create_template(self, template_data: Dict[str, Any]) -> 'Template':
        """
        Create a new template.
        
        Args:
            template_data: Template configuration data
            
        Returns:
            Created template instance
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        response = self._client._make_request_sync(
            "POST",
            self._build_url(),
            json_data=template_data
        )
        
        return self._create_instance(response)
    
    def update_template(self, template_data: Dict[str, Any]) -> 'Template':
        """
        Update an existing template.
        
        Args:
            template_data: Template configuration data (must include 'id')
            
        Returns:
            Updated template instance
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        response = self._client._make_request_sync(
            "PUT",
            self._build_url(),
            json_data=template_data
        )
        
        return self._create_instance(response)
    
    def set_status(self, template_id: str, status: str) -> Dict[str, Any]:
        """
        Set template status (ACTIVE, INACTIVE, DELETED).
        
        Args:
            template_id: Template ID
            status: New status
            
        Returns:
            Success response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = self._build_url(suffix=f"status/{template_id}")
        response = self._client._make_request_sync(
            "POST",
            url,
            json_data={"status": status}
        )
        
        return response
    
    def list_templates(
        self, 
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        paginated: bool = False
    ) -> Union[List['Template'], PaginatedResponse['Template']]:
        """
        List templates.
        
        Args:
            limit: Maximum number of templates to return
            next_token: Token for pagination
            paginated: Return PaginatedResponse instead of list
            
        Returns:
            List of templates or paginated response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        params = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
            
        url = "/api/v1/templates"  # Use the correct endpoint for listing
        return self.list(url=url, paginated=paginated, **params)
    
    def get_pass_downloads_count(
        self, 
        template_id: str, 
        duration: str = "PAST_7_DAYS"
    ) -> Dict[str, Any]:
        """
        Get pass downloads count for a template.
        
        Args:
            template_id: Template ID
            duration: Duration (PAST_7_DAYS, PAST_30_DAYS, ALL)
            
        Returns:
            Pass counts data
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = f"/api/v1/template/{template_id}/downloads/count"
        params = {"duration": duration}
        
        response = self._client._make_request_sync("GET", url, params=params)
        return response
    
    def get_pass_download_trend(
        self, 
        template_id: str, 
        days: int = 7
    ) -> Dict[str, Any]:
        """
        Get pass download trend for a template.
        
        Args:
            template_id: Template ID
            days: Number of days (7 or 30)
            
        Returns:
            Trend data
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = f"/api/v1/template/{template_id}/downloads/trend"
        params = {"days": days}
        
        response = self._client._make_request_sync("GET", url, params=params)
        return response
    
    # Async methods
    
    async def create_template_async(self, template_data: Dict[str, Any]) -> 'Template':
        """Create a new template asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        response = await self._client._make_request_async(
            "POST",
            self._build_url(),
            json_data=template_data
        )
        
        return self._create_instance(response)
    
    async def update_template_async(self, template_data: Dict[str, Any]) -> 'Template':
        """Update an existing template asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        response = await self._client._make_request_async(
            "PUT",
            self._build_url(),
            json_data=template_data
        )
        
        return self._create_instance(response)
    
    async def set_status_async(self, template_id: str, status: str) -> Dict[str, Any]:
        """Set template status asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = self._build_url(suffix=f"status/{template_id}")
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data={"status": status}
        )
        
        return response
    
    async def list_templates_async(
        self,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        paginated: bool = False
    ) -> Union[List['Template'], PaginatedResponse['Template']]:
        """List templates asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        params = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
            
        url = "/api/v1/templates"
        return await self.list_async(url=url, paginated=paginated, **params)
    
    async def get_pass_downloads_count_async(
        self,
        template_id: str,
        duration: str = "PAST_7_DAYS"
    ) -> Dict[str, Any]:
        """Get pass downloads count asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = f"/api/v1/template/{template_id}/downloads/count"
        params = {"duration": duration}
        
        response = await self._client._make_request_async("GET", url, params=params)
        return response
    
    async def get_pass_download_trend_async(
        self,
        template_id: str,
        days: int = 7
    ) -> Dict[str, Any]:
        """Get pass download trend asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = f"/api/v1/template/{template_id}/downloads/trend"
        params = {"days": days}
        
        response = await self._client._make_request_async("GET", url, params=params)
        return response
