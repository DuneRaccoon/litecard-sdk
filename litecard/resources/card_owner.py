"""
Card Owner resource for the Litecard API.
"""

from typing import Dict, Any, Optional
from .base import LitecardResource


class CardOwner(LitecardResource):
    """
    Card Owner resource for managing card owners.
    """
    
    endpoint = "card-owner"
    
    def get_cards_by_owner(
        self, 
        email: Optional[str] = None, 
        phone: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get cards by card owner email or phone.
        
        Args:
            email: Card owner email address
            phone: Card owner phone number
            
        Returns:
            List of passes associated with the card owner
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        if not email and not phone:
            raise ValueError("Either email or phone must be provided")
        
        request_data = {}
        if email:
            request_data["email"] = email
        if phone:
            request_data["phone"] = phone
        
        response = self._client._make_request_sync(
            "POST",
            self._build_url(),
            json_data=request_data
        )
        return response
    
    async def get_cards_by_owner_async(
        self, 
        email: Optional[str] = None, 
        phone: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get cards by card owner asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        if not email and not phone:
            raise ValueError("Either email or phone must be provided")
        
        request_data = {}
        if email:
            request_data["email"] = email
        if phone:
            request_data["phone"] = phone
        
        response = await self._client._make_request_async(
            "POST",
            self._build_url(),
            json_data=request_data
        )
        return response
