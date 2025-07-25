"""
Authentication resource for the Litecard API.
"""

from typing import Dict, Any
from .base import LitecardResource
from ..models_ import AuthenticationRequest, AuthenticationResponse


class Authentication(LitecardResource):
    """
    Authentication resource for managing API tokens.
    """
    
    endpoint = "token"
    model_class = AuthenticationResponse
    
    def authenticate(self, username: str, password: str, tenant: str = None) -> AuthenticationResponse:
        """
        Authenticate and get access token.
        
        Args:
            username: User credential
            password: User credential  
            tenant: Optional tenant identifier
            
        Returns:
            Authentication response with access token
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        auth_data = AuthenticationRequest(username=username, password=password)
        headers = {}
        if tenant:
            headers["x-user-tenant"] = tenant
            
        response = self._client._make_request_sync(
            "POST", 
            self._build_url(),
            json_data=auth_data.model_dump(),
            # Override headers for this specific request
        )
        
        return AuthenticationResponse(**response)
    
    async def authenticate_async(self, username: str, password: str, tenant: str = None) -> AuthenticationResponse:
        """
        Authenticate and get access token asynchronously.
        
        Args:
            username: User credential
            password: User credential
            tenant: Optional tenant identifier
            
        Returns:
            Authentication response with access token
        """
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        auth_data = AuthenticationRequest(username=username, password=password)
        headers = {}
        if tenant:
            headers["x-user-tenant"] = tenant
            
        response = await self._client._make_request_async(
            "POST",
            self._build_url(), 
            json_data=auth_data.model_dump()
        )
        
        return AuthenticationResponse(**response)
