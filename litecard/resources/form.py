"""
Form resource for the Litecard API.
"""

from typing import Dict, Any
from .base import LitecardResource
from ..models import Form as FormModel


class Form(LitecardResource):
    """
    Form resource for managing card creation forms.
    """
    
    endpoint = "form"
    model_class = FormModel
    
    def update_form_design(self, form_id: str, design_data: Dict[str, Any]) -> FormModel:
        """
        Create or update a custom form design.
        
        Args:
            form_id: Form ID
            design_data: Form design configuration
            
        Returns:
            Updated form
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = f"/api/v1/form/{form_id}/design"
        response = self._client._make_request_sync(
            "PUT",
            url,
            json_data=design_data
        )
        
        return FormModel(**response)
    
    async def update_form_design_async(self, form_id: str, design_data: Dict[str, Any]) -> FormModel:
        """Update form design asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = f"/api/v1/form/{form_id}/design"
        response = await self._client._make_request_async(
            "PUT",
            url,
            json_data=design_data
        )
        
        return FormModel(**response)
