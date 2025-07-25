"""
Export resource for the Litecard API.
"""

from typing import Dict, Any
from .base import LitecardResource
from ..models import ExportRequest, ExportResponse


class Export(LitecardResource):
    """
    Export resource for exporting data as CSV files.
    """
    
    endpoint = "exportCsv"
    
    def export_csv(self, export_data: Dict[str, Any]) -> ExportResponse:
        """
        Export CSV file.
        
        Args:
            export_data: Export configuration including table name, date range, etc.
            
        Returns:
            Export response with download URL and expiry
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        response = self._client._make_request_sync(
            "POST",
            self._build_url(),
            json_data=export_data
        )
        return ExportResponse(**response)
    
    async def export_csv_async(self, export_data: Dict[str, Any]) -> ExportResponse:
        """Export CSV file asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        response = await self._client._make_request_async(
            "POST",
            self._build_url(),
            json_data=export_data
        )
        return ExportResponse(**response)
