"""
Scan resource for the Litecard API.
"""

from typing import Dict, Any, List, Union, Optional
from datetime import datetime
from .base import LitecardResource, PaginatedResponse
from ..models_ import ScanRequest, ScanResponse, Scan as ScanModel
from ..request_types import (
    ScanCardRequest,
    ApplyTemplateActionsRequest,
    ScanAction,
    ScanQueryParams,
    SuccessResponse,
)


class Scan(LitecardResource):
    """
    Scan resource for managing card scans and redemptions.
    """
    
    endpoint = "scans"
    model_class = ScanModel
    
    def scan_barcode(
        self, 
        barcode_value: str, 
        business_id: Optional[str] = None
    ) -> ScanResponse:
        """
        Scan a barcode (public endpoint).
        
        Args:
            barcode_value: Barcode value to scan
            business_id: Optional business ID for validation
            
        Returns:
            Scan response with card and card owner info
            
        Example:
            ```python
            # Simple barcode scan
            result = scan_resource.scan_barcode(
                barcode_value="123456789"
            )
            
            print(f"Card ID: {result.card.id}")
            print(f"Card Owner: {result.card_owner['firstName']} {result.card_owner['lastName']}")
            
            # Scan with business validation
            result = scan_resource.scan_barcode(
                barcode_value="123456789",
                business_id="business_123"
            )
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data: ScanCardRequest = {
            "barcodeValue": barcode_value
        }
        
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
        
        This endpoint requires authentication and provides additional security
        for sensitive scanning operations.
        
        Args:
            barcode_value: Barcode value to scan
            
        Returns:
            Scan response with card and card owner info
            
        Example:
            ```python
            # Authenticated scan
            result = scan_resource.scan_barcode_private(
                barcode_value="123456789"
            )
            
            print(f"Scan successful: {result.card.id}")
            if result.actions:
                print(f"Available actions: {result.actions}")
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data: ScanCardRequest = {
            "barcodeValue": barcode_value
        }
        
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
        template_id: Optional[str] = None,
        start_date_time: Optional[datetime] = None,
        end_date_time: Optional[datetime] = None,
        paginated: bool = False
    ) -> Union[List[ScanModel], PaginatedResponse[ScanModel]]:
        """
        List all scans for a business.
        
        Args:
            limit: Maximum number of scans to return
            next_token: Token for pagination
            card_id: Filter by specific card ID
            template_id: Filter by template ID
            start_date_time: Filter by start date
            end_date_time: Filter by end date
            paginated: Return PaginatedResponse instead of list
            
        Returns:
            List of scans or paginated response
            
        Example:
            ```python
            from datetime import datetime, timedelta
            
            # Get recent scans
            recent_scans = scan_resource.list_scans(
                limit=50,
                start_date_time=datetime.now() - timedelta(days=7)
            )
            
            # Get scans for a specific card
            card_scans = scan_resource.list_scans(
                card_id="card_123",
                limit=10
            )
            
            # Get paginated scans
            paginated_scans = scan_resource.list_scans(
                limit=20,
                paginated=True
            )
            
            print(f"Found {len(paginated_scans.items)} scans")
            if paginated_scans.nextToken:
                print("More scans available")
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        params: ScanQueryParams = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        if card_id:
            params["cardId"] = card_id
        if template_id:
            params["templateId"] = template_id
        if start_date_time:
            params["startDate"] = start_date_time
        if end_date_time:
            params["endDate"] = end_date_time
        
        url = "/api/v1/private/scans"
        return self.list(url=url, paginated=paginated, **params)
    
    def delete_scan(self, scan_id: str) -> SuccessResponse:
        """
        Delete a scan by ID.
        
        Args:
            scan_id: Scan ID to delete
            
        Returns:
            Success response
            
        Example:
            ```python
            response = scan_resource.delete_scan("scan_123")
            print(f"Scan deleted: {response['success']}")
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        url = f"/api/v1/private/scans/{scan_id}"
        response = self._client._make_request_sync("DELETE", url)
        
        return response["body"]
    
    def apply_template_actions(
        self,
        card_id: str,
        actions: List[ScanAction]
    ) -> SuccessResponse:
        """
        Apply scanning business rules/actions.
        
        This allows you to programmatically apply business logic when a card
        is scanned, such as adding points, incrementing visit counts, etc.
        
        Args:
            card_id: Card ID to apply actions to
            actions: List of actions to apply with their configurations
            
        Returns:
            Action response with results
            
        Example:
            ```python
            from litecard.request_types import ScanAction
            
            # Define actions to apply
            actions = [
                ScanAction(
                    actionType="POINTS_ADD",
                    value=10,
                    fieldName="points"
                ),
                ScanAction(
                    actionType="VISIT_INCREMENT",
                    fieldName="visitCount"
                ),
                ScanAction(
                    actionType="LAST_VISIT_UPDATE",
                    fieldName="lastVisit",
                    value=datetime.now().isoformat()
                )
            ]
            
            # Apply the actions
            result = scan_resource.apply_template_actions(
                card_id="card_123",
                actions=actions
            )
            
            print(f"Actions applied successfully: {result['success']}")
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        request_data: ApplyTemplateActionsRequest = {
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
    
    def get_scan_analytics(
        self,
        template_id: Optional[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> Dict[str, Any]:
        """
        Get scan analytics and metrics.
        
        Args:
            template_id: Filter analytics by template ID (optional)
            start_date: Start date for analytics period (optional)
            end_date: End date for analytics period (optional)
            
        Returns:
            Analytics data with scan metrics
            
        Example:
            ```python
            from datetime import datetime, timedelta
            
            # Get analytics for the past month
            analytics = scan_resource.get_scan_analytics(
                start_date=datetime.now() - timedelta(days=30),
                end_date=datetime.now()
            )
            
            print(f"Total scans: {analytics.get('totalScans', 0)}")
            print(f"Unique cards scanned: {analytics.get('uniqueCards', 0)}")
            ```
        """
        if not hasattr(self._client, '_make_request_sync'):
            raise TypeError("This method requires a synchronous client")
        
        params = {}
        if template_id:
            params["templateId"] = template_id
        if start_date:
            params["startDate"] = start_date.isoformat()
        if end_date:
            params["endDate"] = end_date.isoformat()
        
        url = "/api/v1/scans/analytics"
        response = self._client._make_request_sync("GET", url, params=params)
        
        return response
    
    # Async methods
    
    async def scan_barcode_async(
        self, 
        barcode_value: str, 
        business_id: Optional[str] = None
    ) -> ScanResponse:
        """Scan a barcode asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data: ScanCardRequest = {
            "barcodeValue": barcode_value
        }
        
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
        
        request_data: ScanCardRequest = {
            "barcodeValue": barcode_value
        }
        
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
        template_id: Optional[str] = None,
        start_date_time: Optional[datetime] = None,
        end_date_time: Optional[datetime] = None,
        paginated: bool = False
    ) -> Union[List[ScanModel], PaginatedResponse[ScanModel]]:
        """List all scans asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        params: ScanQueryParams = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["next"] = next_token
        if card_id:
            params["cardId"] = card_id
        if template_id:
            params["templateId"] = template_id
        if start_date_time:
            params["startDate"] = start_date_time
        if end_date_time:
            params["endDate"] = end_date_time
        
        url = "/api/v1/private/scans"
        return await self.list_async(url=url, paginated=paginated, **params)
    
    async def delete_scan_async(self, scan_id: str) -> SuccessResponse:
        """Delete a scan by ID asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        url = f"/api/v1/private/scans/{scan_id}"
        response = await self._client._make_request_async("DELETE", url)
        
        return response["body"]
    
    async def apply_template_actions_async(
        self,
        card_id: str,
        actions: List[ScanAction]
    ) -> SuccessResponse:
        """Apply scanning business rules/actions asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        request_data: ApplyTemplateActionsRequest = {
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
    
    async def get_scan_analytics_async(
        self,
        template_id: Optional[str] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> Dict[str, Any]:
        """Get scan analytics and metrics asynchronously."""
        if not hasattr(self._client, '_make_request_async'):
            raise TypeError("This method requires an asynchronous client")
        
        params = {}
        if template_id:
            params["templateId"] = template_id
        if start_date:
            params["startDate"] = start_date.isoformat()
        if end_date:
            params["endDate"] = end_date.isoformat()
        
        url = "/api/v1/scans/analytics"
        response = await self._client._make_request_async("GET", url, params=params)
        
        return response
