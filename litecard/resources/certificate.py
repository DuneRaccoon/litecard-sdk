"""
Certificate resource for the Litecard API.
"""

from typing import Dict, Any, List, Union, Optional
from .base import LitecardResource, PaginatedResponse
from ..models import Certificate as CertificateModel, CertificateUpload


class Certificate(LitecardResource):
    """
    Certificate resource for managing Apple certificates.
    """
    
    endpoint = "certificates"
    model_class = CertificateModel
    
    def list_certificates(
        self,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        paginated: bool = False
    ) -> Union[List['Certificate'], PaginatedResponse['Certificate']]:
        """
        List certificates.
        
        Args:
            limit: Maximum number of certificates to return
            next_token: Token for pagination
            paginated: Return PaginatedResponse instead of list
            
        Returns:
            List of certificates or paginated response
        """
        params = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        
        return self.list(paginated=paginated, **params)
    
    def upload_certificate(self, certificate: str, description: Optional[str] = None) -> Dict[str, Any]:
        """
        Upload a certificate.
        
        Args:
            certificate: Base64 encoded certificate
            description: Optional description
            
        Returns:
            Certificate upload response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        upload_data = CertificateUpload(certificate=certificate, description=description)
        
        url = "/api/v1/certificate/upload"
        response = self._client._make_request_sync(
            "POST",
            url,
            json_data=upload_data.model_dump(exclude_none=True)
        )
        
        return response
    
    def get_csr(self) -> Dict[str, str]:
        """
        Get Certificate Signing Request.
        
        Returns:
            CSR data
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = "/api/v1/certificate/csr"
        response = self._client._make_request_sync("GET", url)
        
        return response
    
    # Async methods
    
    async def list_certificates_async(
        self,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        paginated: bool = False
    ) -> Union[List['Certificate'], PaginatedResponse['Certificate']]:
        """List certificates asynchronously."""
        params = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        
        return await self.list_async(paginated=paginated, **params)
    
    async def upload_certificate_async(
        self, 
        certificate: str, 
        description: Optional[str] = None
    ) -> Dict[str, Any]:
        """Upload a certificate asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        upload_data = CertificateUpload(certificate=certificate, description=description)
        
        url = "/api/v1/certificate/upload"
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data=upload_data.model_dump(exclude_none=True)
        )
        
        return response
    
    async def get_csr_async(self) -> Dict[str, str]:
        """Get Certificate Signing Request asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = "/api/v1/certificate/csr"
        response = await self._client._make_request_async("GET", url)
        
        return response
