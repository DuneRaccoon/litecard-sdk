"""
Voucher Code resource for the Litecard API.
"""

from typing import Dict, Any
from .base import LitecardResource


class VoucherCode(LitecardResource):
    """
    Voucher Code resource for managing voucher code uploads.
    """
    
    endpoint = "voucher/codes/upload"
    
    def upload_csv(self, upload_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Upload a CSV file to create voucher codes.
        
        Args:
            upload_data: Upload configuration including file, template ID, and type
            
        Returns:
            Upload response with job ID
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = "/api/v1/voucher/codes/upload/csv"
        response = self._client._make_request_sync(
            "POST",
            url,
            json_data=upload_data
        )
        return response
    
    async def upload_csv_async(self, upload_data: Dict[str, Any]) -> Dict[str, Any]:
        """Upload CSV file for voucher codes asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = "/api/v1/voucher/codes/upload/csv"
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data=upload_data
        )
        return response
