"""
Scan resource for the Litecard API.
"""

from typing import Dict, Any, List, Union, Optional
from datetime import datetime
from .base import LitecardResource, PaginatedResponse
from ..models_ import ScanRequest, ScanResponse, Scan as ScanModel


class Scan(LitecardResource):
    """
    Scan resource for managing card scans and redemptions.
    """
    
    endpoint = "scans"
    model_class = ScanModel
    
    def scan_barcode(self, barcode_value: str, business_id: Optional[str] = None) -> ScanResponse:
        """
        Scan a barcode (public endpoint).
        
        Args:
            barcode_value: Barcode value to scan
            business_id: Optional business ID
            
        Returns:
            Scan response with card and card owner info
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data = {"barcodeValue": barcode_value}
        if business_id:
            request_data["businessId"] = business_id
        
        response = self._client._make_request_sync(
            "POST",
            self._build_url(),
            json_data=request_data
        )
        
        return ScanResponse(**response["body"])
    
    def scan_barcode_private(self, barcode_value: str) -> ScanResponse:
        """
        Scan a barcode (private endpoint with authentication).
        
        Args:
            barcode_value: Barcode value to scan
            
        Returns:
            Scan response with card and card owner info
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data = {"barcodeValue": barcode_value}
        
        url = "/api/v1/private/scans"
        response = self._client._make_request_sync(
            "POST",
            url,
            json_data=request_data
        )
        
        return ScanResponse(**response["body"])
    
    def list_scans(
        self,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        card_id: Optional[str] = None,
        start_date_time: Optional[datetime] = None,
        end_date_time: Optional[datetime] = None,
        paginated: bool = False
    ) -> Union[List['Scan'], PaginatedResponse['Scan']]:
        """
        List all scans for a business.
        
        Args:
            limit: Maximum number of scans to return
            next_token: Token for pagination
            card_id: Filter by card ID
            start_date_time: Filter by start date
            end_date_time: Filter by end date
            paginated: Return PaginatedResponse instead of list
            
        Returns:
            List of scans or paginated response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        params = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        if card_id:
            params["cardId"] = card_id
        if start_date_time:
            params["startDateTime"] = start_date_time.isoformat()
        if end_date_time:
            params["endDateTime"] = end_date_time.isoformat()
        
        url = "/api/v1/private/scans"
        return self.list(url=url, paginated=paginated, **params)
    
    def delete_scan(self, scan_id: str) -> Dict[str, Any]:
        """
        Delete a scan by ID.
        
        Args:
            scan_id: Scan ID to delete
            
        Returns:
            Delete response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = f"/api/v1/private/scans/{scan_id}"
        response = self._client._make_request_sync("DELETE", url)
        
        return response["body"]
    
    def apply_template_actions(
        self,
        card_id: str,
        actions: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Apply scanning business rules/actions.
        
        Args:
            card_id: Card ID
            actions: List of actions to apply
            
        Returns:
            Action response
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data = {
            "cardId": card_id,
            "actions": actions
        }
        
        url = "/api/v1/scans/actions"
        response = self._client._make_request_sync(
            "POST",
            url,
            json_data=request_data
        )
        
        return response["body"]
    
    # Async methods
    
    async def scan_barcode_async(
        self, 
        barcode_value: str, 
        business_id: Optional[str] = None
    ) -> ScanResponse:
        """Scan a barcode asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data = {"barcodeValue": barcode_value}
        if business_id:
            request_data["businessId"] = business_id
        
        response = await self._client._make_request_async(
            "POST",
            self._build_url(),
            json_data=request_data
        )
        
        return ScanResponse(**response["body"])
    
    async def scan_barcode_private_async(self, barcode_value: str) -> ScanResponse:
        """Scan a barcode (private) asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data = {"barcodeValue": barcode_value}
        
        url = "/api/v1/private/scans"
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data=request_data
        )
        
        return ScanResponse(**response["body"])
    
    async def list_scans_async(
        self,
        limit: Optional[int] = None,
        next_token: Optional[str] = None,
        card_id: Optional[str] = None,
        start_date_time: Optional[datetime] = None,
        end_date_time: Optional[datetime] = None,
        paginated: bool = False
    ) -> Union[List['Scan'], PaginatedResponse['Scan']]:
        """List all scans asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        params = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        if card_id:
            params["cardId"] = card_id
        if start_date_time:
            params["startDateTime"] = start_date_time.isoformat()
        if end_date_time:
            params["endDateTime"] = end_date_time.isoformat()
        
        url = "/api/v1/private/scans"
        return await self.list_async(url=url, paginated=paginated, **params)
    
    async def delete_scan_async(self, scan_id: str) -> Dict[str, Any]:
        """Delete a scan by ID asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = f"/api/v1/private/scans/{scan_id}"
        response = await self._client._make_request_async("DELETE", url)
        
        return response["body"]
    
    async def apply_template_actions_async(
        self,
        card_id: str,
        actions: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Apply scanning business rules/actions asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data = {
            "cardId": card_id,
            "actions": actions
        }
        
        url = "/api/v1/scans/actions"
        response = await self._client._make_request_async(
            "POST",
            url,
            json_data=request_data
        )
        
        return response["body"]
